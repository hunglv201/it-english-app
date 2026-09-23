-- Nói Nghề v4.0 · 0005 — lớp học (C1, C2), bảng xếp hạng tuần theo ngành (C3), bạn học (C4)
-- Nguyên tắc riêng tư (NĐ 356/2025): chỉ biệt danh; người tạo lớp chỉ xem SỐ TỔNG HỢP (ngày học, số việc, lần học gần nhất,
-- ngành) — không xem câu trả lời, lỗi, ghi âm. Vào lớp cần đồng ý riêng (không tick sẵn), lưu thời điểm đồng ý.
-- Tất cả bảng khoá kín (RLS không policy + revoke); mọi truy cập qua RPC SECURITY DEFINER có kiểm tra quyền.

create or replace function public.nn_code(n int) returns text
language sql volatile as $$
  select string_agg(substr('ABCDEFGHJKMNPQRSTUVWXYZ23456789', 1 + floor(random() * 31)::int, 1), '') from generate_series(1, n)
$$;
revoke all on function public.nn_code(int) from public, anon, authenticated;

create or replace function public.nn_nick(p text) returns text
language sql immutable as $$
  select nullif(btrim(left(btrim(regexp_replace(regexp_replace(coalesce(p, ''), '[<>"&\x00-\x1f]', '', 'g'), '\s+', ' ', 'g')), 24)), '')
$$;

-- tuần tính từ Thứ Hai (UTC, cùng quy ước ngày với app)
create or replace function public.nn_week_start(d date default current_date) returns date
language sql immutable as $$ select d - (extract(isodow from d)::int - 1) $$;

create or replace function public.nn_streak(p_user uuid) returns int
language sql stable security definer set search_path = public as $$
  select case when coalesce(u.state->>'stats|lastActive', '') >= to_char(current_date - 1, 'YYYY-MM-DD')
              then coalesce(nullif(u.state->>'stats|streak', '')::int, 0) else 0 end
    from user_state u where u.user_id = p_user
$$;
revoke all on function public.nn_streak(uuid) from public, anon, authenticated;

-- ---------- lớp học ----------
create table public.classes (
  id uuid primary key default gen_random_uuid(),
  code text not null unique,
  name text not null,
  owner uuid not null references auth.users on delete cascade,
  track text,
  created_at timestamptz not null default now()
);
create table public.class_members (
  class_id uuid not null references public.classes on delete cascade,
  user_id uuid not null references auth.users on delete cascade,
  nick text not null,
  consent_at timestamptz not null,
  joined_at timestamptz not null default now(),
  primary key (class_id, user_id)
);
create index class_members_user on public.class_members (user_id);
alter table public.classes enable row level security;
alter table public.class_members enable row level security;
revoke all on public.classes, public.class_members from anon, authenticated;

create or replace function public.create_class(p_name text, p_track text default null)
returns jsonb language plpgsql security definer set search_path = public as $$
declare uid uuid := auth.uid(); c text; cid uuid; i int := 0;
begin
  if uid is null then raise exception 'not_authenticated' using errcode = '28000'; end if;
  if coalesce((select is_anonymous from profiles where id = uid), true) then return jsonb_build_object('error', 'google_required'); end if;
  if public.nn_nick(p_name) is null then return jsonb_build_object('error', 'bad_name'); end if;
  if (select count(*) from classes where owner = uid) >= 10 then return jsonb_build_object('error', 'too_many'); end if;
  loop
    c := public.nn_code(8); i := i + 1;
    exit when not exists (select 1 from classes where code = c) or i > 20;
  end loop;
  insert into classes (code, name, owner, track) values (c, left(public.nn_nick(p_name), 40), uid, left(p_track, 32)) returning id into cid;
  return jsonb_build_object('ok', true, 'id', cid, 'code', c);
end $$;

-- chống dò mã lớp: tối đa 10 lần nhập sai mã / giờ / tài khoản
create table public.join_attempts (
  user_id uuid not null references auth.users on delete cascade,
  at timestamptz not null default now()
);
create index join_attempts_user on public.join_attempts (user_id, at);
alter table public.join_attempts enable row level security;
revoke all on public.join_attempts from anon, authenticated;

create or replace function public.join_class(p_code text, p_nick text, p_consent boolean)
returns jsonb language plpgsql security definer set search_path = public as $$
declare uid uuid := auth.uid(); cl classes;
begin
  if uid is null then raise exception 'not_authenticated' using errcode = '28000'; end if;
  if p_consent is not true then return jsonb_build_object('error', 'consent_required'); end if;
  if public.nn_nick(p_nick) is null or length(public.nn_nick(p_nick)) < 2 then return jsonb_build_object('error', 'bad_nick'); end if;
  if (select count(*) from join_attempts where user_id = uid and at > now() - interval '1 hour') >= 10 then
    return jsonb_build_object('error', 'rate_limited');
  end if;
  select * into cl from classes where code = upper(btrim(p_code));
  if cl.id is null then
    insert into join_attempts (user_id) values (uid);
    delete from join_attempts where user_id = uid and at < now() - interval '1 day';
    return jsonb_build_object('error', 'not_found');
  end if;
  if (select count(*) from class_members where class_id = cl.id) >= 200 then return jsonb_build_object('error', 'full'); end if;
  if (select count(*) from class_members where user_id = uid) >= 10 then return jsonb_build_object('error', 'too_many'); end if;
  insert into class_members (class_id, user_id, nick, consent_at) values (cl.id, uid, public.nn_nick(p_nick), now())
  on conflict (class_id, user_id) do update set nick = excluded.nick, consent_at = now();
  return jsonb_build_object('ok', true, 'id', cl.id, 'name', cl.name);
end $$;

create or replace function public.leave_class(p_class uuid)
returns void language sql security definer set search_path = public as $$
  delete from class_members where class_id = p_class and user_id = auth.uid()
$$;

create or replace function public.delete_class(p_class uuid)
returns void language sql security definer set search_path = public as $$
  delete from classes where id = p_class and owner = auth.uid()
$$;

create or replace function public.my_classes()
returns jsonb language sql stable security definer set search_path = public as $$
  select coalesce(jsonb_agg(jsonb_build_object('id', c.id, 'name', c.name, 'code', case when c.owner = auth.uid() then c.code end,
           'owner', c.owner = auth.uid(), 'member', exists (select 1 from class_members m where m.class_id = c.id and m.user_id = auth.uid()),
           'members', (select count(*) from class_members m where m.class_id = c.id), 'track', c.track) order by c.created_at desc), '[]'::jsonb)
    from classes c
   where c.owner = auth.uid() or exists (select 1 from class_members m where m.class_id = c.id and m.user_id = auth.uid())
$$;

-- bảng xếp hạng tuần của lớp: thành viên và chủ lớp xem được; chỉ biệt danh + số ngày/số việc tuần này + chuỗi
create or replace function public.class_board(p_class uuid)
returns jsonb language plpgsql stable security definer set search_path = public as $$
declare uid uuid := auth.uid(); ws date := public.nn_week_start();
begin
  if not exists (select 1 from classes c where c.id = p_class and (c.owner = uid or exists (select 1 from class_members m where m.class_id = c.id and m.user_id = uid))) then
    raise exception 'forbidden' using errcode = '42501';
  end if;
  return (select coalesce(jsonb_agg(r order by (r->>'days')::int desc, (r->>'tasks')::int desc), '[]'::jsonb) from (
    select jsonb_build_object('nick', m.nick, 'me', m.user_id = uid,
             'days', (select count(*) from daily_activity a where a.user_id = m.user_id and a.day >= ws),
             'tasks', (select coalesce(sum(a.tasks), 0) from daily_activity a where a.user_id = m.user_id and a.day >= ws),
             'streak', coalesce(public.nn_streak(m.user_id), 0)) r
      from class_members m where m.class_id = p_class) x);
end $$;

-- màn chủ lớp: chỉ số tổng hợp (không câu trả lời, không ghi âm)
create or replace function public.class_report(p_class uuid)
returns jsonb language plpgsql stable security definer set search_path = public as $$
declare uid uuid := auth.uid(); ws date := public.nn_week_start();
begin
  if not exists (select 1 from classes c where c.id = p_class and c.owner = uid) then raise exception 'forbidden' using errcode = '42501'; end if;
  return (select coalesce(jsonb_agg(jsonb_build_object('nick', m.nick, 'joined', m.joined_at::date,
             'days_week', (select count(*) from daily_activity a where a.user_id = m.user_id and a.day >= ws),
             'tasks_week', (select coalesce(sum(a.tasks), 0) from daily_activity a where a.user_id = m.user_id and a.day >= ws),
             'days_30', (select count(*) from daily_activity a where a.user_id = m.user_id and a.day > current_date - 30),
             'last_active', (select max(a.day) from daily_activity a where a.user_id = m.user_id),
             'track', (select p.track from profiles p where p.id = m.user_id)) order by m.nick), '[]'::jsonb)
    from class_members m where m.class_id = p_class);
end $$;

-- ---------- bảng xếp hạng tuần theo ngành (tự nguyện, biệt danh, nhóm ~20 người, không rớt hạng) ----------
alter table public.profiles add column league_on boolean not null default false;
alter table public.profiles add column league_nick text;

create or replace function public.set_league(p_on boolean, p_nick text default null)
returns jsonb language plpgsql security definer set search_path = public as $$
declare uid uuid := auth.uid();
begin
  if uid is null then raise exception 'not_authenticated' using errcode = '28000'; end if;
  if p_on and (public.nn_nick(p_nick) is null or length(public.nn_nick(p_nick)) < 2) then return jsonb_build_object('error', 'bad_nick'); end if;
  update profiles set league_on = coalesce(p_on, false), league_nick = case when p_on then public.nn_nick(p_nick) else league_nick end where id = uid;
  return jsonb_build_object('ok', true);
end $$;

create or replace function public.league_board()
returns jsonb language plpgsql stable security definer set search_path = public as $$
declare uid uuid := auth.uid(); ws date := public.nn_week_start(); trk text; grp int;
begin
  select track into trk from profiles where id = uid and league_on;
  if trk is null then return jsonb_build_object('on', false); end if;
  with members as (
    select p.id, p.league_nick, (row_number() over (order by p.created_at, p.id) - 1) / 20 as g
      from profiles p where p.league_on and p.track = trk
  )
  select g into grp from members where id = uid;
  return jsonb_build_object('on', true, 'track', trk, 'week', ws, 'rows', (
    select coalesce(jsonb_agg(r order by (r->>'tasks')::int desc, (r->>'days')::int desc), '[]'::jsonb) from (
      select jsonb_build_object('nick', coalesce(m.league_nick, 'Học viên'), 'me', m.id = uid,
               'days', (select count(*) from daily_activity a where a.user_id = m.id and a.day >= ws),
               'tasks', (select coalesce(sum(a.tasks), 0) from daily_activity a where a.user_id = m.id and a.day >= ws)) r
        from (select p.id, p.league_nick, (row_number() over (order by p.created_at, p.id) - 1) / 20 as g
                from profiles p where p.league_on and p.track = trk) m
       where m.g = grp) x));
end $$;

-- ---------- bạn học (học cặp với đồng nghiệp) ----------
create table public.buddy_invites (
  code text primary key,
  user_id uuid not null references auth.users on delete cascade,
  nick text not null,
  created_at timestamptz not null default now()
);
create table public.buddies (
  a uuid not null references auth.users on delete cascade,
  b uuid not null references auth.users on delete cascade,
  nick_a text not null, nick_b text not null,
  since date not null default current_date,
  primary key (a, b),
  check (a < b)
);
create unique index buddies_one_a on public.buddies (a);
create unique index buddies_one_b on public.buddies (b);
alter table public.buddy_invites enable row level security;
alter table public.buddies enable row level security;
revoke all on public.buddy_invites, public.buddies from anon, authenticated;

create or replace function public.buddy_invite(p_nick text)
returns jsonb language plpgsql security definer set search_path = public as $$
declare uid uuid := auth.uid(); c text;
begin
  if uid is null then raise exception 'not_authenticated' using errcode = '28000'; end if;
  if public.nn_nick(p_nick) is null then return jsonb_build_object('error', 'bad_nick'); end if;
  if exists (select 1 from buddies where a = uid or b = uid) then return jsonb_build_object('error', 'has_buddy'); end if;
  delete from buddy_invites where user_id = uid;
  c := public.nn_code(8);
  insert into buddy_invites (code, user_id, nick) values (c, uid, public.nn_nick(p_nick));
  return jsonb_build_object('ok', true, 'code', c);
end $$;

create or replace function public.buddy_accept(p_code text, p_nick text)
returns jsonb language plpgsql security definer set search_path = public as $$
declare uid uuid := auth.uid(); inv buddy_invites;
begin
  if uid is null then raise exception 'not_authenticated' using errcode = '28000'; end if;
  if public.nn_nick(p_nick) is null then return jsonb_build_object('error', 'bad_nick'); end if;
  select * into inv from buddy_invites where code = upper(btrim(p_code)) and created_at > now() - interval '7 days';
  if inv.code is null then return jsonb_build_object('error', 'not_found'); end if;
  if inv.user_id = uid then return jsonb_build_object('error', 'self'); end if;
  -- khoá theo 2 người để 2 lần nhận lời chạy cùng lúc không tạo 2 cặp cho một người
  perform pg_advisory_xact_lock(hashtextextended(least(uid, inv.user_id)::text, 0));
  perform pg_advisory_xact_lock(hashtextextended(greatest(uid, inv.user_id)::text, 0));
  if exists (select 1 from buddies where a in (uid, inv.user_id) or b in (uid, inv.user_id)) then return jsonb_build_object('error', 'has_buddy'); end if;
  insert into buddies (a, b, nick_a, nick_b)
  values (least(uid, inv.user_id), greatest(uid, inv.user_id),
          case when uid < inv.user_id then public.nn_nick(p_nick) else inv.nick end,
          case when uid < inv.user_id then inv.nick else public.nn_nick(p_nick) end);
  delete from buddy_invites where code = inv.code;
  return jsonb_build_object('ok', true, 'nick', inv.nick);
end $$;

create or replace function public.buddy_status()
returns jsonb language plpgsql stable security definer set search_path = public as $$
declare uid uuid := auth.uid(); bd buddies; other uuid; onick text; mnick text; d date; n int := 0; inv text;
begin
  select * into bd from buddies where a = uid or b = uid;
  if bd.a is null then
    select code into inv from buddy_invites where user_id = uid and created_at > now() - interval '7 days';
    return jsonb_build_object('paired', false, 'invite', inv);
  end if;
  if bd.a = uid then other := bd.b; onick := bd.nick_b; mnick := bd.nick_a; else other := bd.a; onick := bd.nick_a; mnick := bd.nick_b; end if;
  -- chuỗi chung: số ngày liên tiếp (tính tới hôm nay hoặc hôm qua) cả hai cùng học
  d := case when exists (select 1 from daily_activity where user_id = uid and day = current_date)
             and exists (select 1 from daily_activity where user_id = other and day = current_date) then current_date else current_date - 1 end;
  while exists (select 1 from daily_activity where user_id = uid and day = d) and exists (select 1 from daily_activity where user_id = other and day = d) and n < 1000 loop
    n := n + 1; d := d - 1;
  end loop;
  return jsonb_build_object('paired', true, 'nick', onick, 'my_nick', mnick, 'since', bd.since, 'shared_streak', n,
    'me_today', exists (select 1 from daily_activity where user_id = uid and day = current_date),
    'buddy_today', exists (select 1 from daily_activity where user_id = other and day = current_date),
    'can_nudge', not exists (select 1 from nudges where from_user = uid and created_at > now() - interval '20 hours'));
end $$;

create or replace function public.buddy_nudge()
returns jsonb language plpgsql security definer set search_path = public as $$
declare uid uuid := auth.uid(); bd buddies; other uuid; mnick text;
begin
  select * into bd from buddies where a = uid or b = uid;
  if bd.a is null then return jsonb_build_object('error', 'no_buddy'); end if;
  if bd.a = uid then other := bd.b; mnick := bd.nick_a; else other := bd.a; mnick := bd.nick_b; end if;
  if exists (select 1 from nudges where from_user = uid and created_at > now() - interval '20 hours') then return jsonb_build_object('error', 'already'); end if;
  if exists (select 1 from daily_activity where user_id = other and day = current_date) then return jsonb_build_object('error', 'already_learned'); end if;
  insert into nudges (to_user, from_user, from_nick) values (other, uid, mnick);
  return jsonb_build_object('ok', true);
end $$;

create or replace function public.buddy_remove()
returns void language plpgsql security definer set search_path = public as $$
declare uid uuid := auth.uid(); bd buddies;
begin
  select * into bd from buddies where a = uid or b = uid;
  if bd.a is null then return; end if;
  delete from nudges where sent_at is null and ((from_user = bd.a and to_user = bd.b) or (from_user = bd.b and to_user = bd.a));
  delete from buddies where a = bd.a and b = bd.b;
end $$;

do $$ declare f text; begin
  foreach f in array array['create_class(text, text)','join_class(text, text, boolean)','leave_class(uuid)','delete_class(uuid)','my_classes()',
    'class_board(uuid)','class_report(uuid)','set_league(boolean, text)','league_board()','buddy_invite(text)','buddy_accept(text, text)',
    'buddy_status()','buddy_nudge()','buddy_remove()'] loop
    execute format('revoke all on function public.%s from public, anon', f);
    execute format('grant execute on function public.%s to authenticated', f);
  end loop;
end $$;
revoke all on function public.nn_nick(text) from anon;
revoke all on function public.nn_week_start(date) from anon;
