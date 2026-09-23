-- Test 0006 (tổng kết tuần qua email). Chạy sau db2.test.sql trên cùng DB.
\set ON_ERROR_STOP on
set client_min_messages = warning;
reset role;
insert into auth.users (id, is_anonymous, email, raw_app_meta_data) values
  ('20000000-0000-0000-0000-00000000000a', false, 'lan.nguyen@example.com', '{"provider":"google","providers":["google"]}'),
  ('20000000-0000-0000-0000-00000000000b', true,  null, '{"provider":"anonymous"}');
update profiles set display_name = 'Lan', track = 'hotel' where id = '20000000-0000-0000-0000-00000000000a';
insert into daily_activity (user_id, day, track, tasks) values
  ('20000000-0000-0000-0000-00000000000a', current_date, 'hotel', 4), ('20000000-0000-0000-0000-00000000000a', current_date - 2, 'hotel', 3),
  ('20000000-0000-0000-0000-00000000000a', current_date - 9, 'hotel', 2);
insert into user_state (user_id, state) values ('20000000-0000-0000-0000-00000000000a', jsonb_build_object('stats|streak', 6, 'stats|lastActive', '2999-01-01'));
-- người dùng khác ghi giá trị lạ vào streak + bật email → không được làm hỏng cả lô
insert into auth.users (id, is_anonymous, email, raw_app_meta_data) values ('20000000-0000-0000-0000-00000000000c', false, 'x@example.com', '{"provider":"google"}');
insert into daily_activity (user_id, day, track, tasks) values ('20000000-0000-0000-0000-00000000000c', current_date, 'office', 1);
insert into user_state (user_id, state) values ('20000000-0000-0000-0000-00000000000c', jsonb_build_object('stats|streak', 'abc', 'stats|lastActive', '2999-01-01'));
insert into email_prefs (user_id, weekly, tz_offset_min) values ('20000000-0000-0000-0000-00000000000c', true, 420);
-- Chủ nhật tuần sau lúc 20:00 giờ VN (UTC+7) = 13:00 UTC
select (date_trunc('week', now() at time zone 'UTC')::date + 6 + 7)::text as sun \gset
select (:'sun' || ' 13:00:00+00')::timestamptz as t_ok, (:'sun' || ' 08:00:00+00')::timestamptz as t_early \gset

set role authenticated;
-- khách: không bật được, không lộ email
select set_config('request.jwt.claim.sub', '20000000-0000-0000-0000-00000000000b', false);
select (email_status()->>'available')::boolean = false as ok \gset
\if :ok \else \echo 'FAIL guest status' \q \endif
select set_email_weekly(true, 420)->>'error' = 'google_required' as ok \gset
\if :ok \else \echo 'FAIL guest enable' \q \endif
-- Google: mặc định tắt, email che bớt
select set_config('request.jwt.claim.sub', '20000000-0000-0000-0000-00000000000a', false);
select email_status() as st \gset
select (:'st'::jsonb->>'available')::boolean and not (:'st'::jsonb->>'weekly')::boolean and (:'st'::jsonb->>'email') = 'l***@example.com' as ok \gset
\if :ok \else \echo 'FAIL status' :'st' \q \endif
select (set_email_weekly(true, 420)->>'weekly')::boolean as ok \gset
\if :ok \else \echo 'FAIL enable' \q \endif
select (set_email_weekly(true)->>'weekly')::boolean as ok \gset
\if :ok \else \echo 'FAIL enable no tz' \q \endif
-- client không đọc bảng, không gọi hàm của server
do $$ begin
  begin perform 1 from email_prefs; raise exception 'should fail'; exception when insufficient_privilege then null; end;
  begin perform claim_weekly_emails(); raise exception 'should fail'; exception when insufficient_privilege then null; end;
  begin perform nn_user_email(auth.uid()); raise exception 'should fail'; exception when insufficient_privilege then null; end;
end $$;

reset role;
-- sai giờ → không gửi
select count(*) = 0 as ok from claim_weekly_emails(:'t_early') \gset
\if :ok \else \echo 'FAIL early' \q \endif
-- đúng giờ Chủ nhật: gửi 1 lần, đủ số liệu; gọi lại → không trùng
select * from claim_weekly_emails(:'t_ok') where email = 'lan.nguyen@example.com' \gset e_
select :'e_email' = 'lan.nguyen@example.com' and :'e_nick' = 'Lan' and :'e_track' = 'hotel' and :'e_streak_n'::int = 6 and :'e_unsub_token' <> '' as ok \gset
\if :ok \else \echo 'FAIL claim' \q \endif
select count(*) = 0 as ok from claim_weekly_emails(:'t_ok') \gset
\if :ok \else \echo 'FAIL dup' \q \endif
select tz_offset_min = 420 as ok from email_prefs where user_id = '20000000-0000-0000-0000-00000000000a' \gset
\if :ok \else \echo 'FAIL tz kept' \q \endif
select last_sent is not null as ok from email_prefs where user_id = '20000000-0000-0000-0000-00000000000c' \gset
\if :ok \else \echo 'FAIL bad streak user' \q \endif
-- gửi hỏng → release → lượt sau gửi lại
select release_weekly_email('20000000-0000-0000-0000-00000000000a');
select count(*) = 1 as ok from claim_weekly_emails(:'t_ok') \gset
\if :ok \else \echo 'FAIL release' \q \endif
-- huỷ nhận bằng token (khách vô danh gọi được), token sai → false
set role anon;
select email_unsubscribe(gen_random_uuid()) = false as ok \gset
\if :ok \else \echo 'FAIL bad token' \q \endif
select email_unsubscribe(:'e_unsub_token'::uuid) as ok \gset
\if :ok \else \echo 'FAIL unsub' \q \endif
reset role;
select not weekly as ok from email_prefs where user_id = '20000000-0000-0000-0000-00000000000a' \gset
\if :ok \else \echo 'FAIL unsub state' \q \endif
-- 4 tuần không học → không gửi dù đang bật
update email_prefs set weekly = true, last_sent = null;
delete from daily_activity where user_id in ('20000000-0000-0000-0000-00000000000a', '20000000-0000-0000-0000-00000000000c');
select count(*) = 0 as ok from claim_weekly_emails(:'t_ok') \gset
\if :ok \else \echo 'FAIL inactive' \q \endif
-- xoá tài khoản → cascade
delete from auth.users where id in ('20000000-0000-0000-0000-00000000000a', '20000000-0000-0000-0000-00000000000c');
select count(*) = 0 as ok from email_prefs \gset
\if :ok \else \echo 'FAIL cascade' \q \endif
\echo 'ALL DB3 TESTS PASSED'
