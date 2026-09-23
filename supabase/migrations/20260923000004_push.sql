-- Nói Nghề v4.0 · 0004 — nhắc học bằng Web Push (đợt A: A1 push thật, A2 giờ nhắc thích ứng, A4 kéo người vắng, A8 tổng kết tuần)
-- Edge Function `send-reminders` (chạy 15 phút/lần) gọi due_reminders() rồi mark_pushed(). Mỗi người tối đa 1 push/ngày.
-- Ngày = ngày UTC như app (todayStr() dùng toISOString) để khớp chuỗi/heatmap; giờ nhắc tính theo giờ địa phương (tz_offset_min).

create table public.push_subscriptions (
  id bigint generated always as identity primary key,
  user_id uuid not null references auth.users on delete cascade,
  endpoint text not null unique,
  p256dh text not null,
  auth text not null,
  ua text,
  created_at timestamptz not null default now(),
  last_ok_at timestamptz,
  fail_count int not null default 0,          -- tăng tối đa 1 lần/ngày (sự cố ngắn của dịch vụ push không làm tắt vĩnh viễn)
  last_fail_day date
);
create index push_subscriptions_user on public.push_subscriptions (user_id);
alter table public.push_subscriptions enable row level security;
revoke all on public.push_subscriptions from anon, authenticated;

create table public.reminder_prefs (
  user_id uuid primary key references auth.users on delete cascade,
  mode text not null default 'auto' check (mode in ('auto', 'fixed', 'off')),
  fixed_min int check (fixed_min between 0 and 1439),      -- giờ cố định (phút trong ngày, giờ địa phương)
  tz_offset_min int not null default 420 check (tz_offset_min between -720 and 840),
  first_min int check (first_min between 0 and 1439),      -- giờ học đầu tiên của ngày học gần nhất (địa phương)
  first_day date,
  last_push_day date,
  last_push_kind text,
  weekly_sent date,                                         -- Chủ nhật đã gửi tổng kết tuần
  updated_at timestamptz not null default now()
);
alter table public.reminder_prefs enable row level security;
create policy "reminder_prefs: own read" on public.reminder_prefs for select to authenticated using (auth.uid() = user_id);
revoke all on public.reminder_prefs from anon, authenticated;
grant select on public.reminder_prefs to authenticated;

-- lời nhắc từ bạn học (C4) — gửi qua cùng kênh push
create table public.nudges (
  id bigint generated always as identity primary key,
  to_user uuid not null references auth.users on delete cascade,
  from_user uuid not null references auth.users on delete cascade,
  from_nick text,
  created_at timestamptz not null default now(),
  sent_at timestamptz
);
create index nudges_to on public.nudges (to_user, sent_at);
alter table public.nudges enable row level security;
revoke all on public.nudges from anon, authenticated;

-- ---------- RPC cho app ----------
create or replace function public.save_push(p_sub jsonb, p_ua text default null)
returns jsonb language plpgsql security definer set search_path = public as $$
declare uid uuid := auth.uid(); ep text := p_sub->>'endpoint';
begin
  if uid is null then raise exception 'not_authenticated' using errcode = '28000'; end if;
  if ep is null or ep !~ '^https://' or length(ep) > 1000 then raise exception 'bad_endpoint'; end if;
  if (select count(*) from push_subscriptions where user_id = uid) >= 5 then
    delete from push_subscriptions where id = (select id from push_subscriptions where user_id = uid order by created_at limit 1);
  end if;
  insert into push_subscriptions (user_id, endpoint, p256dh, auth, ua)
  values (uid, ep, left(p_sub#>>'{keys,p256dh}', 200), left(p_sub#>>'{keys,auth}', 100), left(p_ua, 200))
  on conflict (endpoint) do update set user_id = excluded.user_id, p256dh = excluded.p256dh, auth = excluded.auth,
    ua = excluded.ua, fail_count = 0;
  insert into reminder_prefs (user_id) values (uid) on conflict do nothing;
  return jsonb_build_object('ok', true);
end $$;

create or replace function public.delete_push(p_endpoint text)
returns void language sql security definer set search_path = public as $$
  delete from push_subscriptions where user_id = auth.uid() and endpoint = p_endpoint
$$;

create or replace function public.set_reminder(p_mode text, p_fixed_min int default null, p_tz_offset int default null)
returns jsonb language plpgsql security definer set search_path = public as $$
declare uid uuid := auth.uid();
begin
  if uid is null then raise exception 'not_authenticated' using errcode = '28000'; end if;
  if p_mode not in ('auto', 'fixed', 'off') then raise exception 'bad_mode'; end if;
  insert into reminder_prefs (user_id, mode, fixed_min, tz_offset_min)
  values (uid, p_mode, p_fixed_min, coalesce(p_tz_offset, 420))
  on conflict (user_id) do update set mode = excluded.mode, fixed_min = coalesce(excluded.fixed_min, reminder_prefs.fixed_min),
    tz_offset_min = coalesce(p_tz_offset, reminder_prefs.tz_offset_min), updated_at = now();
  return jsonb_build_object('ok', true);
end $$;

-- app gọi một lần mỗi ngày khi học việc đầu tiên: nhớ giờ học để hôm sau nhắc lúc +23,5 giờ
create or replace function public.touch_reminder(p_first_min int, p_tz_offset int)
returns void language plpgsql security definer set search_path = public as $$
declare uid uuid := auth.uid();
begin
  if uid is null then return; end if;
  insert into reminder_prefs (user_id, first_min, first_day, tz_offset_min)
  values (uid, least(greatest(p_first_min, 0), 1439), current_date, least(greatest(coalesce(p_tz_offset, 420), -720), 840))
  on conflict (user_id) do update set
    first_min = case when reminder_prefs.first_day is distinct from current_date then excluded.first_min else reminder_prefs.first_min end,
    first_day = current_date, tz_offset_min = excluded.tz_offset_min, updated_at = now();
end $$;

revoke all on function public.save_push(jsonb, text) from public, anon;
revoke all on function public.delete_push(text) from public, anon;
revoke all on function public.set_reminder(text, int, int) from public, anon;
revoke all on function public.touch_reminder(int, int) from public, anon;
grant execute on function public.save_push(jsonb, text) to authenticated;
grant execute on function public.delete_push(text) to authenticated;
grant execute on function public.set_reminder(text, int, int) to authenticated;
grant execute on function public.touch_reminder(int, int) to authenticated;

-- ---------- cho Edge Function (service role) ----------
-- (due_reminders tham chiếu bảng buddies tạo ở 0005 → tắt kiểm tra thân hàm lúc tạo)
set check_function_bodies = off;
-- Ai cần nhắc lúc p_now. kind: daily (vắng 1 ngày) · winback2/3/4 · final7 (lần cuối, sau đó im) · weekly (tối Chủ nhật) · nudge (bạn học nhắc)
create or replace function public.due_reminders(p_now timestamptz default now())
returns table (user_id uuid, kind text, days_away int, streak_n int, freeze_n int, track text, week_days int, last_week_days int, from_nick text)
language sql stable security definer set search_path = public as $$
  with base as (
    select r.user_id, r.mode, r.fixed_min, r.first_min, r.last_push_day, r.weekly_sent, r.tz_offset_min,
           (p_now at time zone 'UTC')::date as today,
           ((p_now at time zone 'UTC') + make_interval(mins => r.tz_offset_min)) as local_ts,
           (select max(a.day) from daily_activity a where a.user_id = r.user_id) as last_day
      from reminder_prefs r
     where r.mode <> 'off' and exists (select 1 from push_subscriptions s where s.user_id = r.user_id and s.fail_count < 5)
  ), win as (
    -- khung gửi theo giờ địa phương, gói gọn trong MỘT ngày UTC (ngày của app) → "đã học hôm nay" và "1 push/ngày" luôn đúng
    select b.*, greatest(420, b.tz_offset_min) as lo, least(1290, 1439 + b.tz_offset_min) as hi from base b
  ), calc as (
    select b.*, (extract(hour from b.local_ts) * 60 + extract(minute from b.local_ts))::int as local_min,
           (b.today - b.last_day) as away,
           least(greatest(case when b.mode = 'fixed' and b.fixed_min is not null then b.fixed_min
                               else coalesce(b.first_min - 30, 1170) end, b.lo), b.hi) as target
      from win b
  ), st as (
    select c.*, least(greatest(coalesce(public.nn_num(u.state->'stats|streak'), 0), 0), 100000)::int as stk,
           least(greatest(coalesce(public.nn_num(u.state->'stats|freeze'), 0), 0), 100000)::int as frz,
           coalesce(p.track, 'office') as trk
      from calc c left join user_state u on u.user_id = c.user_id left join profiles p on p.id = c.user_id
  )
  -- bạn học nhắc (ưu tiên, 7:00–21:30 giờ địa phương)
  select s.user_id, 'nudge', s.away, s.stk, s.frz, s.trk, null::int, null::int,
         (select n.from_nick from nudges n where n.to_user = s.user_id and n.sent_at is null order by n.created_at desc limit 1)
    from st s
   where s.last_push_day is distinct from s.today and s.local_min between s.lo and s.hi and coalesce(s.away, 1) between 1 and 7
     and exists (select 1 from nudges n where n.to_user = s.user_id and n.sent_at is null and n.created_at > p_now - interval '20 hours'
                   and exists (select 1 from buddies bd where (bd.a = n.from_user and bd.b = n.to_user) or (bd.b = n.from_user and bd.a = n.to_user)))
  union all
  select s.user_id,
         case s.away when 1 then 'daily' when 2 then 'winback2' when 3 then 'winback3' when 4 then 'winback4' else 'final7' end,
         s.away, s.stk, s.frz, s.trk, null, null, null
    from st s
   where s.last_day is not null and s.away in (1, 2, 3, 4, 7)
     and s.last_push_day is distinct from s.today and s.local_min >= s.target and s.local_min <= s.hi
     and not (coalesce(s.away, 1) between 1 and 7 and exists (select 1 from nudges n where n.to_user = s.user_id and n.sent_at is null and n.created_at > p_now - interval '20 hours'
                   and exists (select 1 from buddies bd where (bd.a = n.from_user and bd.b = n.to_user) or (bd.b = n.from_user and bd.a = n.to_user))))
  union all
  select s.user_id, 'weekly', s.away, s.stk, s.frz, s.trk,
         (select count(*) from daily_activity a where a.user_id = s.user_id and a.day > s.today - 7 and a.day <= s.today)::int,
         (select count(*) from daily_activity a where a.user_id = s.user_id and a.day > s.today - 14 and a.day <= s.today - 7)::int,
         null
    from st s
   where extract(isodow from s.local_ts) = 7 and s.local_min between greatest(1140, s.lo) and s.hi
     and s.weekly_sent is distinct from s.local_ts::date and s.away = 0
     and s.last_push_day is distinct from s.today
     and exists (select 1 from daily_activity a where a.user_id = s.user_id and a.day > s.today - 14)
$$;

reset check_function_bodies;

create or replace function public.mark_pushed(p_user uuid, p_kind text, p_now timestamptz default now())
returns void language plpgsql security definer set search_path = public as $$
begin
  update reminder_prefs set last_push_day = (p_now at time zone 'UTC')::date, last_push_kind = p_kind,
         weekly_sent = case when p_kind = 'weekly'
                            then ((p_now at time zone 'UTC') + make_interval(mins => tz_offset_min))::date else weekly_sent end
   where user_id = p_user;
  if p_kind = 'nudge' then update nudges set sent_at = p_now where to_user = p_user and sent_at is null; end if;
end $$;

-- Edge Function gọi hàm này (không gọi due_reminders trực tiếp): đánh dấu "đã nhắc hôm nay" NGUYÊN TỬ trước khi gửi,
-- nên 2 lượt chạy chồng nhau không gửi trùng. Gửi hỏng hết → release_reminder() để lượt sau thử lại.
create or replace function public.claim_reminders(p_now timestamptz default now())
returns table (user_id uuid, kind text, days_away int, streak_n int, freeze_n int, track text, week_days int, last_week_days int, from_nick text)
language plpgsql security definer set search_path = public as $$
declare d record; n int;
begin
  for d in select * from public.due_reminders(p_now) loop
    update reminder_prefs r set last_push_day = (p_now at time zone 'UTC')::date, last_push_kind = d.kind,
           weekly_sent = case when d.kind = 'weekly' then ((p_now at time zone 'UTC') + make_interval(mins => r.tz_offset_min))::date else r.weekly_sent end
     where r.user_id = d.user_id and r.last_push_day is distinct from (p_now at time zone 'UTC')::date;
    get diagnostics n = row_count;
    if n = 1 then
      if d.kind = 'nudge' then update nudges set sent_at = p_now where to_user = d.user_id and sent_at is null; end if;
      user_id := d.user_id; kind := d.kind; days_away := d.days_away; streak_n := d.streak_n; freeze_n := d.freeze_n; track := d.track;
      week_days := d.week_days; last_week_days := d.last_week_days; from_nick := d.from_nick;
      return next;
    end if;
  end loop;
end $$;

create or replace function public.release_reminder(p_user uuid)
returns void language sql security definer set search_path = public as $$
  update reminder_prefs set last_push_day = null where user_id = p_user
$$;

create or replace function public.push_targets(p_user uuid)
returns table (id bigint, endpoint text, p256dh text, auth text)
language sql stable security definer set search_path = public as $$
  select id, endpoint, p256dh, auth from push_subscriptions where user_id = p_user and fail_count < 5
$$;

create or replace function public.push_result(p_id bigint, p_ok boolean, p_gone boolean default false)
returns void language plpgsql security definer set search_path = public as $$
begin
  if p_gone then delete from push_subscriptions where id = p_id; return; end if;
  update push_subscriptions set last_ok_at = case when p_ok then now() else last_ok_at end,
         fail_count = case when p_ok then 0 when last_fail_day is distinct from current_date then fail_count + 1 else fail_count end,
         last_fail_day = case when p_ok then last_fail_day else current_date end
   where id = p_id;
end $$;

revoke all on function public.due_reminders(timestamptz) from public, anon, authenticated;
revoke all on function public.claim_reminders(timestamptz) from public, anon, authenticated;
revoke all on function public.release_reminder(uuid) from public, anon, authenticated;
grant execute on function public.claim_reminders(timestamptz) to service_role;
grant execute on function public.release_reminder(uuid) to service_role;
revoke all on function public.mark_pushed(uuid, text, timestamptz) from public, anon, authenticated;
revoke all on function public.push_targets(uuid) from public, anon, authenticated;
revoke all on function public.push_result(bigint, boolean, boolean) from public, anon, authenticated;
grant execute on function public.due_reminders(timestamptz) to service_role;
grant execute on function public.mark_pushed(uuid, text, timestamptz) to service_role;
grant execute on function public.push_targets(uuid) to service_role;
grant execute on function public.push_result(bigint, boolean, boolean) to service_role;

-- A9: chỉ số "học thật" cho admin (phút nói, lượt nói với AI, ngày hoàn hảo) — lấy từ bản đồ trạng thái
create or replace function public.admin_quality()
returns jsonb language plpgsql stable security definer set search_path = public as $$
begin
  if not public.is_admin() then raise exception 'forbidden' using errcode = '42501'; end if;
  return (select jsonb_build_object(
    'talk_turns', coalesce(sum(nullif(state->>'stats|talkTurns', '')::numeric), 0),
    'speak_minutes', round(coalesce(sum(nullif(state->>'stats|speakSec', '')::numeric), 0) / 60),
    'perfect_days', coalesce(sum(nullif(state->>'stats|perfect', '')::numeric), 0),
    'users_speaking', count(*) filter (where coalesce(nullif(state->>'stats|talkTurns', '')::numeric, 0) >= 10))
    from user_state where updated_at > now() - interval '30 days');
end $$;
revoke all on function public.admin_quality() from public, anon;
grant execute on function public.admin_quality() to authenticated;

insert into public.app_config (key, value) values ('push_enabled', 'true') on conflict do nothing;
