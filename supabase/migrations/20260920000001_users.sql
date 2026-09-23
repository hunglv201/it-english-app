-- Nói Nghề v4.0 · 0001 — người dùng, dữ liệu học, cấu hình + RLS
-- Server là nguồn gốc dữ liệu người học. Trạng thái chi tiết lưu dạng "bản đồ phẳng" path -> value
-- trong user_state.state (xem docs/BACKEND-PLAN.md §5). Mọi ghi đi qua RPC apply_changes (0002).

-- ---------- profiles ----------
create table public.profiles (
  id uuid primary key references auth.users on delete cascade,
  display_name text,
  avatar_url text,
  track text default 'office',
  role text,
  level text default 'A2',
  is_anonymous boolean not null default true,
  is_admin boolean not null default false,
  ai_tier text not null default 'guest' check (ai_tier in ('guest','google','plus')),
  created_at timestamptz not null default now(),
  last_seen_at timestamptz not null default now()
);
alter table public.profiles enable row level security;
create policy "profiles: own read" on public.profiles for select to authenticated using (auth.uid() = id);
-- người dùng chỉ sửa được tên hiển thị / ngành / vai / trình độ (quyền cột, không sửa is_admin, ai_tier…)
create policy "profiles: own update" on public.profiles for update to authenticated using (auth.uid() = id) with check (auth.uid() = id);
revoke all on public.profiles from anon, authenticated;
grant select on public.profiles to authenticated;
grant update (display_name, track, role, level) on public.profiles to authenticated;

create or replace function public.is_admin() returns boolean
language sql stable security definer set search_path = public as $$
  select coalesce((select p.is_admin from public.profiles p where p.id = auth.uid()), false)
$$;
revoke all on function public.is_admin() from public, anon;
grant execute on function public.is_admin() to authenticated;

-- tạo profile khi đăng ký (kể cả khách) · cập nhật khi khách liên kết Google
-- Hạn mức 'google' chỉ khi thật sự có danh tính Google (không cấp cho đăng ký email nếu provider email lỡ bật)
create or replace function public.handle_user() returns trigger
language plpgsql security definer set search_path = public as $$
declare
  anon boolean := coalesce(new.is_anonymous, false);
  g boolean := coalesce(new.raw_app_meta_data->>'provider', '') = 'google'
               or coalesce(new.raw_app_meta_data->'providers', '[]'::jsonb) ? 'google';
begin
  insert into public.profiles (id, display_name, avatar_url, is_anonymous, ai_tier)
  values (new.id,
          nullif(coalesce(new.raw_user_meta_data->>'full_name', new.raw_user_meta_data->>'name'), ''),
          nullif(new.raw_user_meta_data->>'avatar_url', ''),
          anon, case when not anon and g then 'google' else 'guest' end)
  on conflict (id) do update set
    display_name = coalesce(excluded.display_name, public.profiles.display_name),
    avatar_url   = coalesce(excluded.avatar_url, public.profiles.avatar_url),
    is_anonymous = excluded.is_anonymous,
    ai_tier      = case when public.profiles.ai_tier = 'guest' then excluded.ai_tier else public.profiles.ai_tier end;
  return new;
end $$;
create trigger nn_on_auth_user_insert after insert on auth.users
  for each row execute function public.handle_user();
create trigger nn_on_auth_user_update after update of is_anonymous, raw_user_meta_data, raw_app_meta_data on auth.users
  for each row execute function public.handle_user();
revoke all on function public.handle_user() from public, anon, authenticated;

-- ---------- user_state: bản gốc trạng thái học (bản đồ phẳng) ----------
create table public.user_state (
  user_id uuid primary key references auth.users on delete cascade,
  state jsonb not null default '{}'::jsonb,
  rev bigint not null default 0,
  app_version text,
  updated_at timestamptz not null default now()
);
alter table public.user_state enable row level security;
create policy "user_state: own read" on public.user_state for select to authenticated using (auth.uid() = user_id);
revoke all on public.user_state from anon, authenticated;
grant select on public.user_state to authenticated;   -- không có quyền ghi trực tiếp: chỉ qua apply_changes

-- ---------- bảng phục vụ truy vấn / thống kê (server tự suy ra từ các thay đổi) ----------
create table public.user_days (
  user_id uuid not null references auth.users on delete cascade,
  track text not null,
  day int not null,
  done_at timestamptz not null default now(),
  primary key (user_id, track, day)
);
create table public.daily_activity (
  user_id uuid not null references auth.users on delete cascade,
  day date not null,
  track text,
  tasks int not null default 0,
  primary key (user_id, day)
);
create table public.attempts_daily (
  user_id uuid not null references auth.users on delete cascade,
  day date not null,
  kind text not null,             -- vocab | phrase
  ok int not null default 0,
  fail int not null default 0,
  primary key (user_id, day, kind)
);
create table public.applied_changes (   -- chống áp trùng 1 lô khi gửi lại
  user_id uuid not null references auth.users on delete cascade,
  change_id text not null,
  at timestamptz not null default now(),
  primary key (user_id, change_id)
);
alter table public.user_days enable row level security;
alter table public.daily_activity enable row level security;
alter table public.attempts_daily enable row level security;
alter table public.applied_changes enable row level security;
create policy "user_days: own read" on public.user_days for select to authenticated using (auth.uid() = user_id);
create policy "daily_activity: own read" on public.daily_activity for select to authenticated using (auth.uid() = user_id);
create policy "attempts_daily: own read" on public.attempts_daily for select to authenticated using (auth.uid() = user_id);
revoke all on public.user_days, public.daily_activity, public.attempts_daily, public.applied_changes from anon, authenticated;
grant select on public.user_days, public.daily_activity, public.attempts_daily to authenticated;
create index daily_activity_day on public.daily_activity (day);

-- ---------- app_config: đọc công khai, chỉ admin sửa ----------
create table public.app_config (
  key text primary key,
  value jsonb not null,
  updated_at timestamptz not null default now()
);
alter table public.app_config enable row level security;
create policy "app_config: read all" on public.app_config for select to anon, authenticated using (true);
create policy "app_config: admin write" on public.app_config for all to authenticated using (public.is_admin()) with check (public.is_admin());
revoke all on public.app_config from anon, authenticated;
grant select on public.app_config to anon, authenticated;
grant insert, update, delete on public.app_config to authenticated;
insert into public.app_config (key, value) values
  ('ai_daily_guest', '10'),
  ('ai_daily_google', '20'),
  ('ai_daily_plus', '100'),
  ('ai_per_minute', '6'),
  ('ai_daily_global', '3000'),   -- trần tổng lượt AI/ngày của cả app (bảo vệ chi phí key chung)
  ('min_app_version', '"4.0.0"'),
  ('notice', '""');
