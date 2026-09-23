-- Nói Nghề v4.2 · 0006 — tổng kết tuần qua EMAIL (tuỳ chọn, mặc định TẮT; chỉ tài khoản Google có email)
-- Edge Function `send-reminders` (cùng lịch 15 phút) gọi claim_weekly_emails() khi có secret RESEND_API_KEY + EMAIL_FROM.
-- Gửi tối Chủ nhật 19:00–21:30 giờ địa phương, tối đa 1 email/tuần. Ngừng tự động nếu 4 tuần không học.
-- Huỷ nhận: link trong email → app ?unsub=<token> → email_unsubscribe(token) (không cần đăng nhập).

create table public.email_prefs (
  user_id uuid primary key references auth.users on delete cascade,
  weekly boolean not null default false,
  consent_at timestamptz,                                   -- thời điểm bật (đồng ý riêng, không tick sẵn)
  tz_offset_min int not null default 420 check (tz_offset_min between -720 and 840),
  last_sent date,                                           -- Chủ nhật (giờ địa phương) đã gửi
  unsub_token uuid not null default gen_random_uuid() unique,
  updated_at timestamptz not null default now()
);
alter table public.email_prefs enable row level security;
revoke all on public.email_prefs from anon, authenticated;

-- email của người dùng (chỉ Google, không khách): dùng nội bộ, KHÔNG cấp cho client
create or replace function public.nn_user_email(p_user uuid)
returns text language sql stable security definer set search_path = public, auth as $$
  select u.email from auth.users u join public.profiles p on p.id = u.id
   where u.id = p_user and not coalesce(u.is_anonymous, false) and not p.is_anonymous and coalesce(u.email, '') like '%@%'
$$;
revoke all on function public.nn_user_email(uuid) from public, anon, authenticated;

create or replace function public.email_status()
returns jsonb language plpgsql stable security definer set search_path = public as $$
declare uid uuid := auth.uid(); e text; r email_prefs;
begin
  if uid is null then return jsonb_build_object('error', 'auth'); end if;
  e := public.nn_user_email(uid);
  select * into r from email_prefs where user_id = uid;
  return jsonb_build_object('available', e is not null,
    'email', case when e is null then null else regexp_replace(e, '^(.).*(@.*)$', '\1***\2') end,
    'weekly', coalesce(r.weekly, false), 'last_sent', r.last_sent);
end $$;

create or replace function public.set_email_weekly(p_on boolean, p_tz_offset int default null)
returns jsonb language plpgsql security definer set search_path = public as $$
declare uid uuid := auth.uid();
begin
  if uid is null then return jsonb_build_object('error', 'auth'); end if;
  if p_on and public.nn_user_email(uid) is null then return jsonb_build_object('error', 'google_required'); end if;
  insert into email_prefs (user_id, weekly, consent_at, tz_offset_min)
  values (uid, p_on, case when p_on then now() end, case when p_tz_offset is null then 420 else greatest(-720, least(840, p_tz_offset)) end)
  on conflict (user_id) do update set weekly = excluded.weekly,
    consent_at = case when excluded.weekly then now() else email_prefs.consent_at end,
    tz_offset_min = case when p_tz_offset is null then email_prefs.tz_offset_min else greatest(-720, least(840, p_tz_offset)) end, updated_at = now();
  return public.email_status();
end $$;

-- huỷ nhận từ link trong email (không cần đăng nhập) — chỉ tắt, không làm gì khác, không lộ thông tin
create or replace function public.email_unsubscribe(p_token uuid)
returns boolean language plpgsql security definer set search_path = public as $$
declare n int;
begin
  update email_prefs set weekly = false, updated_at = now() where unsub_token = p_token and weekly;
  get diagnostics n = row_count;
  return n = 1;
end $$;
grant execute on function public.email_unsubscribe(uuid) to anon, authenticated;

-- Ai cần email lúc p_now → đánh dấu NGUYÊN TỬ trước khi gửi (2 lượt chạy chồng nhau không gửi trùng)
create or replace function public.claim_weekly_emails(p_now timestamptz default now())
returns table (user_id uuid, email text, nick text, track text, week_days int, last_week_days int, streak_n int, tasks_week int, unsub_token uuid)
language plpgsql security definer set search_path = public as $$
declare d record; n int; today date;
begin
  for d in
    select e.user_id, e.unsub_token, ((p_now at time zone 'UTC') + make_interval(mins => e.tz_offset_min)) as lts
      from email_prefs e
     where e.weekly
  loop
    continue when extract(isodow from d.lts) <> 7;
    continue when (extract(hour from d.lts) * 60 + extract(minute from d.lts)) not between 1140 and 1290;
    today := d.lts::date;   -- ngày địa phương (daily_activity.day là ngày của app trên máy người dùng)
    continue when not exists (select 1 from daily_activity a where a.user_id = d.user_id and a.day > today - 28);
    continue when public.nn_user_email(d.user_id) is null;
    update email_prefs set last_sent = d.lts::date where email_prefs.user_id = d.user_id and last_sent is distinct from d.lts::date;
    get diagnostics n = row_count;
    continue when n <> 1;
    user_id := d.user_id; email := public.nn_user_email(d.user_id); unsub_token := d.unsub_token;
    select nullif(trim(p.display_name), ''), coalesce(p.track, 'office') into nick, track from profiles p where p.id = d.user_id;
    week_days := (select count(*) from daily_activity a where a.user_id = d.user_id and a.day > today - 7 and a.day <= today);
    last_week_days := (select count(*) from daily_activity a where a.user_id = d.user_id and a.day > today - 14 and a.day <= today - 7);
    tasks_week := (select coalesce(sum(a.tasks), 0) from daily_activity a where a.user_id = d.user_id and a.day > today - 7 and a.day <= today);
    -- chuỗi chỉ tính khi còn "sống" (học hôm nay/hôm qua); giá trị lạ do client ghi không làm hỏng cả lô
    streak_n := coalesce((select case when coalesce(u.state->>'stats|lastActive', '') >= to_char(today - 1, 'YYYY-MM-DD')
                                      then least(greatest(coalesce(public.nn_num(u.state->'stats|streak'), 0), 0), 100000)::int else 0 end
                            from user_state u where u.user_id = d.user_id), 0);
    return next;
  end loop;
end $$;

create or replace function public.release_weekly_email(p_user uuid)
returns void language sql security definer set search_path = public as $$
  update email_prefs set last_sent = null where user_id = p_user $$;

revoke all on function public.claim_weekly_emails(timestamptz) from public, anon, authenticated;
revoke all on function public.release_weekly_email(uuid) from public, anon, authenticated;
revoke all on function public.email_status() from public, anon;
revoke all on function public.set_email_weekly(boolean, int) from public, anon;
grant execute on function public.email_status() to authenticated;
grant execute on function public.set_email_weekly(boolean, int) to authenticated;
grant execute on function public.claim_weekly_emails(timestamptz), public.release_weekly_email(uuid) to service_role;
