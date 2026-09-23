-- Test schema + RLS + apply_changes. Chạy: supabase/tests/db_test.sh (Postgres cục bộ) — dừng ở lỗi đầu tiên.
\set ON_ERROR_STOP on
set client_min_messages = warning;
insert into auth.users (id, is_anonymous, raw_app_meta_data) values
  ('00000000-0000-0000-0000-00000000000a', true, '{"provider":"anonymous","providers":["anonymous"]}'),
  ('00000000-0000-0000-0000-00000000000b', false, '{"provider":"google","providers":["google"]}'),
  ('00000000-0000-0000-0000-00000000000e', false, '{"provider":"email","providers":["email"]}');
update auth.users set raw_user_meta_data = '{"full_name":"Bình"}' where id = '00000000-0000-0000-0000-00000000000b';

-- trigger tạo profile, khách → google
do $$ begin
  assert (select ai_tier from profiles where id = '00000000-0000-0000-0000-00000000000a') = 'guest', 'guest tier';
  assert (select display_name from profiles where id = '00000000-0000-0000-0000-00000000000b') = 'Bình', 'meta name';
end $$;
do $$ begin assert (select ai_tier from profiles where id = '00000000-0000-0000-0000-00000000000e') = 'guest', 'email signup must not get google tier'; end $$;
delete from auth.users where id = '00000000-0000-0000-0000-00000000000e';
update auth.users set is_anonymous = false, raw_app_meta_data = '{"provider":"anonymous","providers":["anonymous","google"]}', raw_user_meta_data = '{"full_name":"An","avatar_url":"https://x/a.png"}' where id = '00000000-0000-0000-0000-00000000000a';
do $$ begin
  assert (select ai_tier from profiles where id = '00000000-0000-0000-0000-00000000000a') = 'google', 'linked → google tier';
  assert (select not is_anonymous from profiles where id = '00000000-0000-0000-0000-00000000000a'), 'linked → not anon';
end $$;

-- ===== user A =====
set role authenticated;
select set_config('request.jwt.claim.sub', '00000000-0000-0000-0000-00000000000a', false);

-- lô 1: tạo dữ liệu
select apply_changes('c1', '[
  {"p":"srs|deploy","v":{"ease":2.3,"int":1,"reps":1,"due":100}},
  {"p":"hist|2026-09-20","v":3},
  {"p":"cfg|track","v":"hotel"},
  {"p":"tdays|hotel|done|1","v":true},
  {"p":"tdays|hotel|cur","v":2},
  {"p":"saved|Could you help me%7Cplease?","v":{"note":"x","ts":1}}
]'::jsonb, 0, '4.0.0') ->> 'rev' as rev1 \gset
select (get_state()->>'rev')::int = 1 as ok \gset
\if :ok \else \echo 'FAIL rev after c1' \q \endif

-- gửi lại cùng id → không áp lần 2, không tăng rev
select (apply_changes('c1', '[{"p":"hist|2026-09-20","v":3}]'::jsonb, 0, '4.0.0')->>'dup')::boolean as ok \gset
\if :ok \else \echo 'FAIL dup' \q \endif
select get_rev() = 1 as ok \gset
\if :ok \else \echo 'FAIL rev after dup' \q \endif

-- không xung đột: b = giá trị hiện tại → ghi đè kể cả giảm reps (người học bấm "Quên")
select apply_changes('c2', '[{"p":"srs|deploy","b":{"ease":2.3,"int":1,"reps":1,"due":100},"v":{"ease":2.3,"int":0,"reps":0,"due":50}}]'::jsonb, 1, '4.0.0') is not null as x \gset
select (get_state()->'state'->'srs|deploy'->>'reps')::int = 0 as ok \gset
\if :ok \else \echo 'FAIL no-conflict overwrite' \q \endif

-- xung đột SRS: máy khác (b cũ) gửi reps 3 → thắng vì reps lớn hơn; gửi reps 0 với b cũ → server giữ
select apply_changes('c3', '[{"p":"srs|deploy","b":{"ease":2.3,"int":1,"reps":1,"due":100},"v":{"ease":2.5,"int":6,"reps":3,"due":900}}]'::jsonb, 1, '4.0.0') is not null as x \gset
select (get_state()->'state'->'srs|deploy'->>'reps')::int = 3 as ok \gset
\if :ok \else \echo 'FAIL srs conflict max reps' \q \endif
select (apply_changes('c4', '[{"p":"srs|deploy","b":{"reps":1},"v":{"reps":0,"due":1}}]'::jsonb, 1, '4.0.0')->'vals'->'srs|deploy'->>'reps')::int = 3 as ok \gset
\if :ok \else \echo 'FAIL srs conflict keep server' \q \endif

-- xung đột số: hist, cur lấy lớn hơn
select apply_changes('c5', '[{"p":"hist|2026-09-20","b":1,"v":2},{"p":"tdays|hotel|cur","b":1,"v":1}]'::jsonb, 1, '4.0.0') is not null as x \gset
select (get_state()->'state'->>'hist|2026-09-20')::int = 3 and (get_state()->'state'->>'tdays|hotel|cur')::int = 2 as ok \gset
\if :ok \else \echo 'FAIL numeric max' \q \endif

-- xoá có xung đột → giữ; xoá không xung đột → xoá + bảng user_days đồng bộ
select apply_changes('c6', '[{"p":"saved|Could you help me%7Cplease?","b":{"note":"old","ts":0},"d":true}]'::jsonb, 1, '4.0.0') is not null as x \gset
select (get_state()->'state') ? 'saved|Could you help me%7Cplease?' as ok \gset
\if :ok \else \echo 'FAIL conflicting delete must keep' \q \endif
select count(*) = 1 as ok from user_days \gset
\if :ok \else \echo 'FAIL user_days insert' \q \endif
select apply_changes('c7', '[{"p":"tdays|hotel|done|1","b":true,"d":true}]'::jsonb, 1, '4.0.0') is not null as x \gset
select count(*) = 0 as ok from user_days \gset
\if :ok \else \echo 'FAIL user_days delete' \q \endif

-- thống kê suy ra
select tasks = 3 and track = 'hotel' as ok from daily_activity where day = '2026-09-20' \gset
\if :ok \else \echo 'FAIL daily_activity' \q \endif
select ok >= 2 and fail = 1 as ok from attempts_daily where kind = 'vocab' \gset
\if :ok \else \echo 'FAIL attempts_daily' \q \endif
select track = 'hotel' as ok from profiles where id = auth.uid() \gset
\if :ok \else \echo 'FAIL profile track from cfg' \q \endif

-- lô có dữ liệu lạ không được làm hỏng cả lô; path quá dài được bỏ qua nhưng vẫn trả giá trị
select apply_changes('c9', ('[{"p":"hist|2026-09-21","v":99999999999},{"p":"hist|2026-02-31","v":1},{"p":"cfg|x","v":1,"d":"yes"},{"p":"saved|' || repeat('x', 1200) || '","v":{"ts":1}},{"p":"cfg|ok","v":true}]')::jsonb, 1, '4.0.0') as r9 \gset
select (:'r9'::jsonb->'vals') ? ('saved|' || repeat('x', 1200)) and (get_state()->'state'->>'cfg|ok')::boolean and (get_state()->'state'->>'cfg|x')::int = 1 as ok \gset
\if :ok \else \echo 'FAIL robust batch' \q \endif

-- phiên bản app quá cũ
select apply_changes('c8', '[]'::jsonb, 1, '3.9.9')->>'error' = 'update_required' as ok \gset
\if :ok \else \echo 'FAIL min version' \q \endif

-- báo lỗi + hạn mức
select (report_content('{"at":"2026-09-20T01:00:00Z","track":"hotel","kind":"vocab","type":"Sai nghĩa","text":"deploy — triển khai"}')->>'ok')::boolean as ok \gset
\if :ok \else \echo 'FAIL report' \q \endif
select (report_content('{"at":"2026-09-20T01:00:00Z","track":"hotel"}')->>'id') is null as ok \gset
\if :ok \else \echo 'FAIL report dedupe' \q \endif
select (my_ai_quota()->>'limit')::int = 20 as ok \gset
\if :ok \else \echo 'FAIL quota google' \q \endif

-- ===== RLS: A không được làm những việc này =====
select count(*) = 0 as ok from content_reports \gset
\if :ok \else \echo 'FAIL non-admin reads reports' \q \endif
do $$ begin
  begin update profiles set ai_tier = 'plus' where id = auth.uid(); raise exception 'should fail';
  exception when insufficient_privilege then null; end;
  begin update profiles set is_admin = true where id = auth.uid(); raise exception 'should fail';
  exception when insufficient_privilege then null; end;
  begin update user_state set rev = 99; raise exception 'should fail';
  exception when insufficient_privilege then null; end;
  begin perform admin_stats(); raise exception 'should fail';
  exception when insufficient_privilege then null; end;
  begin perform ai_take(auth.uid()); raise exception 'should fail';
  exception when insufficient_privilege then null; end;
  begin insert into app_config values ('x', '1'); raise exception 'should fail';
  exception when insufficient_privilege then null; end;
  begin insert into user_state (user_id) values (auth.uid()); raise exception 'should fail';
  exception when insufficient_privilege then null; end;
  begin insert into content_reports (track) values ('x'); raise exception 'should fail';
  exception when insufficient_privilege then null; end;
  begin insert into ai_usage (user_id) values (auth.uid()); raise exception 'should fail';
  exception when insufficient_privilege then null; end;
  begin delete from profiles where id = auth.uid(); raise exception 'should fail';
  exception when insufficient_privilege then null; end;
end $$;
update profiles set display_name = 'An mới', track = 'sales' where id = auth.uid();

-- ===== user B không thấy dữ liệu của A =====
select set_config('request.jwt.claim.sub', '00000000-0000-0000-0000-00000000000b', false);
select count(*) = 0 as ok from user_state where user_id <> auth.uid() \gset
\if :ok \else \echo 'FAIL B sees A state' \q \endif
select count(*) = 1 as ok from profiles \gset
\if :ok \else \echo 'FAIL B sees other profiles' \q \endif
select count(*) = 0 as ok from user_days \gset
\if :ok \else \echo 'FAIL B sees A days' \q \endif
select (get_state()->>'rev')::int = 0 as ok \gset
\if :ok \else \echo 'FAIL B get_state' \q \endif
select (my_ai_quota()->>'limit')::int = 20 as ok \gset
\if :ok \else \echo 'FAIL quota B' \q \endif

-- ===== anon: không gọi được RPC =====
reset role;
set role anon;
do $$ begin
  begin perform apply_changes('z', '[]'::jsonb); raise exception 'should fail';
  exception when insufficient_privilege then null; end;
  begin perform report_content('{}'::jsonb); raise exception 'should fail';
  exception when insufficient_privilege then null; end;
  begin perform 1 from user_state; raise exception 'should fail';
  exception when insufficient_privilege then null; end;
  begin perform 1 from profiles; raise exception 'should fail';
  exception when insufficient_privilege then null; end;
  begin perform cleanup_guests(1); raise exception 'should fail';
  exception when insufficient_privilege then null; end;
end $$;
select count(*) > 0 as ok from app_config \gset
\if :ok \else \echo 'FAIL anon reads config' \q \endif

-- ===== service role: hạn mức AI =====
reset role;
update public.profiles set ai_tier = 'guest' where id = '00000000-0000-0000-0000-00000000000b';
update public.app_config set value = '2' where key = 'ai_per_minute';
do $$ declare r jsonb; b uuid := '00000000-0000-0000-0000-00000000000b'; begin
  r := ai_take(b); assert (r->>'ok')::boolean and (r->>'remaining')::int = 9, 'take1 ' || r;
  r := ai_take(b); assert (r->>'ok')::boolean, 'take2';
  r := ai_take(b); assert r->>'error' = 'rate_limited', 'per minute ' || r;
  perform ai_record(b, 10, 20, true);
  assert (select calls from ai_usage where user_id = b) = 1, 'refund on failure';
  assert (select tokens_in from ai_usage where user_id = b) = 10, 'tokens recorded on failure';
  update ai_usage set calls = 10, minute_calls = 0 where user_id = b;
  r := ai_take(b); assert r->>'error' = 'daily_limit', 'daily ' || r;
  update ai_usage set refunds = 5, calls = 3 where user_id = b;
  perform ai_record(b, 0, 0, true);
  assert (select calls from ai_usage where user_id = b) = 3, 'refund capped';
  update app_config set value = '3' where key = 'ai_daily_global';
  r := ai_take(b); assert r->>'error' = 'global_limit', 'global ' || r;
  update app_config set value = '3000' where key = 'ai_daily_global';
end $$;

-- admin
update public.profiles set is_admin = true where id = '00000000-0000-0000-0000-00000000000b';
set role authenticated;
select set_config('request.jwt.claim.sub', '00000000-0000-0000-0000-00000000000b', false);
select (admin_stats()->>'users')::int = 2 and (admin_stats()->>'reports_new')::int = 1 as ok \gset
\if :ok \else \echo 'FAIL admin_stats' \q \endif
select count(*) = 1 as ok from content_reports \gset
\if :ok \else \echo 'FAIL admin reads reports' \q \endif

-- dọn khách
reset role;
insert into auth.users (id, is_anonymous, created_at) values ('00000000-0000-0000-0000-00000000000c', true, now() - interval '40 days');
update public.profiles set last_seen_at = now() - interval '40 days' where id = '00000000-0000-0000-0000-00000000000c';
select cleanup_guests(30) = 1 as ok \gset
\if :ok \else \echo 'FAIL cleanup_guests' \q \endif

-- xoá user → cascade
delete from auth.users where id = '00000000-0000-0000-0000-00000000000a';
select (select count(*) from public.user_state) = 0 and (select count(*) from public.content_reports where user_id is null) = 1 as ok \gset
\if :ok \else \echo 'FAIL cascade delete' \q \endif
\echo 'ALL DB TESTS PASSED'
