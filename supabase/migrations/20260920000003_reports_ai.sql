-- Nói Nghề v4.0 · 0003 — báo lỗi nội dung, hạn mức AI, thống kê admin, dọn khách

-- ---------- báo lỗi nội dung ----------
create table public.content_reports (
  id bigint generated always as identity primary key,
  user_id uuid references auth.users on delete set null,
  client_at text,                 -- thời điểm tạo trên máy (khoá chống gửi trùng)
  track text, kind text, type text,
  excerpt text, note text, place text,
  app_version text,
  status text not null default 'new' check (status in ('new','fixed','ignored')),
  created_at timestamptz not null default now(),
  resolved_at timestamptz,
  unique (user_id, client_at)
);
alter table public.content_reports enable row level security;
create policy "reports: admin read" on public.content_reports for select to authenticated using (public.is_admin());
create policy "reports: admin update" on public.content_reports for update to authenticated using (public.is_admin()) with check (public.is_admin());
revoke all on public.content_reports from anon, authenticated;
grant select, update on public.content_reports to authenticated;
create index content_reports_status on public.content_reports (status, created_at desc);

create or replace function public.report_content(r jsonb)
returns jsonb
language plpgsql security definer set search_path = public as $$
declare uid uuid := auth.uid(); n int; rid bigint;
begin
  if uid is null then raise exception 'not_authenticated' using errcode = '28000'; end if;
  select count(*) into n from content_reports where user_id = uid and created_at > now() - interval '1 hour';
  if n >= 20 then return jsonb_build_object('error', 'rate_limited'); end if;
  insert into content_reports (user_id, client_at, track, kind, type, excerpt, note, place, app_version)
  values (uid, left(r->>'at', 40), left(r->>'track', 32), left(r->>'kind', 32), left(r->>'type', 60),
          left(r->>'text', 800), left(r->>'note', 400), left(r->>'where', 60), left(r->>'v', 20))
  on conflict (user_id, client_at) do nothing
  returning id into rid;
  return jsonb_build_object('ok', true, 'id', rid);
end $$;
revoke all on function public.report_content(jsonb) from public, anon;
grant execute on function public.report_content(jsonb) to authenticated;

-- ---------- hạn mức AI (Edge Function `ai` gọi bằng service role) ----------
create table public.ai_usage (
  user_id uuid not null references auth.users on delete cascade,
  day date not null default current_date,
  calls int not null default 0,
  tokens_in int not null default 0,
  tokens_out int not null default 0,
  minute_at timestamptz,
  minute_calls int not null default 0,
  primary key (user_id, day)
);
create index ai_usage_day on public.ai_usage (day);
alter table public.ai_usage enable row level security;
create policy "ai_usage: own read" on public.ai_usage for select to authenticated using (auth.uid() = user_id);
revoke all on public.ai_usage from anon, authenticated;
grant select on public.ai_usage to authenticated;

create or replace function public.ai_limit(p_uid uuid) returns int
language sql stable security definer set search_path = public as $$
  select coalesce((select (value #>> '{}')::int from app_config
                    where key = 'ai_daily_' || coalesce((select ai_tier from profiles where id = p_uid), 'guest')), 10)
$$;

-- giữ chỗ 1 lượt: trả {ok, remaining, limit} hoặc {ok:false, error:'daily_limit'|'rate_limited'}
create or replace function public.ai_take(p_uid uuid)
returns jsonb
language plpgsql security definer set search_path = public as $$
declare lim int := public.ai_limit(p_uid); pm int; gl int; u ai_usage;
begin
  select coalesce((value #>> '{}')::int, 6) into pm from app_config where key = 'ai_per_minute';
  select (value #>> '{}')::int into gl from app_config where key = 'ai_daily_global';
  if gl is not null and (select coalesce(sum(calls), 0) from ai_usage where day = current_date) >= gl then
    return jsonb_build_object('ok', false, 'error', 'global_limit', 'limit', lim, 'remaining', 0);
  end if;
  insert into ai_usage (user_id, day) values (p_uid, current_date) on conflict do nothing;
  select * into u from ai_usage where user_id = p_uid and day = current_date for update;
  if u.calls >= lim then return jsonb_build_object('ok', false, 'error', 'daily_limit', 'limit', lim, 'remaining', 0); end if;
  if u.minute_at is not null and u.minute_at > now() - interval '1 minute' and u.minute_calls >= coalesce(pm, 6) then
    return jsonb_build_object('ok', false, 'error', 'rate_limited', 'limit', lim, 'remaining', lim - u.calls);
  end if;
  update ai_usage set calls = calls + 1,
         minute_calls = case when minute_at is null or minute_at <= now() - interval '1 minute' then 1 else minute_calls + 1 end,
         minute_at = case when minute_at is null or minute_at <= now() - interval '1 minute' then now() else minute_at end
   where user_id = p_uid and day = current_date;
  return jsonb_build_object('ok', true, 'limit', lim, 'remaining', lim - u.calls - 1);
end $$;

-- p_refund: chỉ khi lỗi mạng / nhà cung cấp 5xx·429 (không phải lỗi do request) → trả lại lượt, tối đa 5 lần/ngày
alter table public.ai_usage add column refunds int not null default 0;
create or replace function public.ai_record(p_uid uuid, p_in int, p_out int, p_refund boolean default false)
returns void
language sql security definer set search_path = public as $$
  update ai_usage set tokens_in = tokens_in + greatest(coalesce(p_in, 0), 0),
                      tokens_out = tokens_out + greatest(coalesce(p_out, 0), 0),
                      calls = case when p_refund and refunds < 5 then greatest(calls - 1, 0) else calls end,
                      refunds = refunds + case when p_refund and refunds < 5 then 1 else 0 end
   where user_id = p_uid and day = current_date
$$;
revoke all on function public.ai_limit(uuid) from public, anon, authenticated;
revoke all on function public.ai_take(uuid) from public, anon, authenticated;
revoke all on function public.ai_record(uuid, int, int, boolean) from public, anon, authenticated;
grant execute on function public.ai_take(uuid) to service_role;
grant execute on function public.ai_record(uuid, int, int, boolean) to service_role;
grant execute on function public.ai_limit(uuid) to service_role;

create or replace function public.my_ai_quota()
returns jsonb
language sql stable security definer set search_path = public as $$
  select jsonb_build_object('limit', public.ai_limit(auth.uid()),
         'used', coalesce((select calls from ai_usage where user_id = auth.uid() and day = current_date), 0))
$$;
revoke all on function public.my_ai_quota() from public, anon;
grant execute on function public.my_ai_quota() to authenticated;

-- ---------- thống kê cho admin ----------
create or replace function public.admin_stats(p_from date default current_date - 29, p_to date default current_date)
returns jsonb
language plpgsql stable security definer set search_path = public as $$
declare res jsonb;
begin
  if not public.is_admin() then raise exception 'forbidden' using errcode = '42501'; end if;
  select jsonb_build_object(
    'users', (select count(*) from profiles),
    'guests', (select count(*) from profiles where is_anonymous),
    'google', (select count(*) from profiles where not is_anonymous),
    'new_by_day', (select coalesce(jsonb_object_agg(d, n), '{}') from
        (select created_at::date d, count(*) n from profiles where created_at::date between p_from and p_to group by 1) x),
    'dau', (select coalesce(jsonb_object_agg(day, n), '{}') from
        (select day, count(*) n from daily_activity where day between p_from and p_to group by 1) x),
    'wau', (select count(distinct user_id) from daily_activity where day > p_to - 7 and day <= p_to),
    'retention', (select jsonb_build_object(
        'd1', round(avg(case when exists (select 1 from daily_activity a where a.user_id = p.id and a.day = p.created_at::date + 1) then 1 else 0 end)::numeric, 3),
        'd7', round(avg(case when exists (select 1 from daily_activity a where a.user_id = p.id and a.day between p.created_at::date + 6 and p.created_at::date + 8) then 1 else 0 end)::numeric, 3),
        'd30', round(avg(case when exists (select 1 from daily_activity a where a.user_id = p.id and a.day between p.created_at::date + 28 and p.created_at::date + 32) then 1 else 0 end)::numeric, 3))
      from profiles p where p.created_at::date between p_from - 30 and p_to - 30),
    'tracks', (select coalesce(jsonb_object_agg(coalesce(track, '?'), n), '{}') from (select track, count(*) n from profiles group by 1) x),
    'attempts', (select coalesce(jsonb_object_agg(kind, jsonb_build_object('ok', ok, 'fail', fail)), '{}') from
        (select kind, sum(ok) ok, sum(fail) fail from attempts_daily where day between p_from and p_to group by 1) x),
    'ai_calls', (select coalesce(sum(calls), 0) from ai_usage where day between p_from and p_to),
    'ai_tokens', (select coalesce(sum(tokens_in + tokens_out), 0) from ai_usage where day between p_from and p_to),
    'reports_new', (select count(*) from content_reports where status = 'new'),
    'db_bytes', pg_database_size(current_database())
  ) into res;
  return res;
end $$;
revoke all on function public.admin_stats(date, date) from public, anon;
grant execute on function public.admin_stats(date, date) to authenticated;

-- ---------- dọn tài khoản khách không hoạt động (GitHub Action gọi bằng kết nối DB) ----------
create or replace function public.cleanup_guests(p_days int default 30)
returns int
language plpgsql security definer set search_path = public as $$
declare n int;
begin
  with gone as (
    delete from auth.users u
     where coalesce(u.is_anonymous, false)
       and greatest(coalesce(u.last_sign_in_at, u.created_at),
                    coalesce((select p.last_seen_at from profiles p where p.id = u.id), u.created_at))
           < now() - make_interval(days => greatest(p_days, 7))
    returning 1)
  select count(*) into n from gone;
  return n;
end $$;
revoke all on function public.cleanup_guests(int) from public, anon, authenticated;
grant execute on function public.cleanup_guests(int) to service_role;

-- ---------- lưu vết yêu cầu xoá tài khoản (không giữ dữ liệu cá nhân: chỉ băm id) ----------
create table public.deletion_log (
  id bigint generated always as identity primary key,
  user_hash text not null,
  source text not null default 'app',
  at timestamptz not null default now()
);
alter table public.deletion_log enable row level security;   -- không policy: chỉ service role
revoke all on public.deletion_log from anon, authenticated;
