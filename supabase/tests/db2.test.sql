-- Test 0004 (push/nhắc học) + 0005 (lớp học, xếp hạng, bạn học). Chạy sau db.test.sql trên DB mới.
\set ON_ERROR_STOP on
set client_min_messages = warning;
insert into auth.users (id, is_anonymous, raw_app_meta_data) values
  ('10000000-0000-0000-0000-00000000000a', false, '{"provider":"google","providers":["google"]}'),   -- chủ lớp (Google)
  ('10000000-0000-0000-0000-00000000000b', true,  '{"provider":"anonymous"}'),                     -- học viên khách
  ('10000000-0000-0000-0000-00000000000c', true,  '{"provider":"anonymous"}');
-- hoạt động: B học hôm qua và hôm nay, C chỉ hôm qua
insert into daily_activity (user_id, day, track, tasks) values
  ('10000000-0000-0000-0000-00000000000b', current_date - 1, 'office', 3), ('10000000-0000-0000-0000-00000000000b', current_date, 'office', 2),
  ('10000000-0000-0000-0000-00000000000c', current_date - 1, 'office', 5);
insert into user_state (user_id, state) values
  ('10000000-0000-0000-0000-00000000000b', jsonb_build_object('stats|streak', 4, 'stats|lastActive', to_char(current_date, 'YYYY-MM-DD'), 'stats|talkTurns', 12, 'stats|speakSec', 300)),
  ('10000000-0000-0000-0000-00000000000c', jsonb_build_object('stats|streak', 9, 'stats|lastActive', to_char(current_date - 1, 'YYYY-MM-DD'), 'stats|freeze', 1));

set role authenticated;
-- ===== C1: khách không tạo được lớp; Google tạo được =====
select set_config('request.jwt.claim.sub', '10000000-0000-0000-0000-00000000000b', false);
select create_class('Lớp thử', 'office')->>'error' = 'google_required' as ok \gset
\if :ok \else \echo 'FAIL guest create_class' \q \endif
select set_config('request.jwt.claim.sub', '10000000-0000-0000-0000-00000000000a', false);
select create_class('Phòng Kinh doanh', 'office') as cls \gset
select (:'cls'::jsonb->>'code') as code, (:'cls'::jsonb->>'id') as cid \gset
select length(:'code') = 8 as ok \gset
\if :ok \else \echo 'FAIL class code' \q \endif
-- ===== vào lớp: phải đồng ý, biệt danh hợp lệ =====
select set_config('request.jwt.claim.sub', '10000000-0000-0000-0000-00000000000b', false);
select join_class(:'code', 'Bình', false)->>'error' = 'consent_required' as ok \gset
\if :ok \else \echo 'FAIL consent' \q \endif
select join_class(:'code', 'x', true)->>'error' = 'bad_nick' as ok \gset
\if :ok \else \echo 'FAIL nick' \q \endif
select (join_class(lower(:'code'), 'Bình', true)->>'ok')::boolean as ok \gset
\if :ok \else \echo 'FAIL join' \q \endif
select set_config('request.jwt.claim.sub', '10000000-0000-0000-0000-00000000000c', false);
select (join_class(:'code', 'Chi <b>', true)->>'ok')::boolean as ok \gset
\if :ok \else \echo 'FAIL join C' \q \endif
-- bảng xếp hạng lớp: thành viên xem được, có biệt danh + số, không có id
select class_board(:'cid'::uuid) as board \gset
select jsonb_array_length(:'board'::jsonb) = 2 and (:'board'::jsonb->0->>'nick') = 'Bình' and (:'board'::jsonb->1->>'nick') = 'Chi b'
   and (:'board'::jsonb->1->>'streak')::int = 9 and (:'board'::jsonb->1->>'me')::boolean and not (:'board'::text ~ '10000000') as ok \gset
\if :ok \else \echo 'FAIL class_board' :'board' \q \endif
-- C không phải chủ → không xem báo cáo; không đọc thẳng bảng
do $$ begin
  begin perform class_report((select id from classes limit 1)); raise exception 'should fail'; exception when insufficient_privilege then null; end;
end $$;
do $$ begin
  begin perform 1 from classes; raise exception 'should fail'; exception when insufficient_privilege then null; end;
  begin perform 1 from push_subscriptions; raise exception 'should fail'; exception when insufficient_privilege then null; end;
  begin perform due_reminders(); raise exception 'should fail'; exception when insufficient_privilege then null; end;
  begin update profiles set league_on = true where id = auth.uid(); raise exception 'should fail'; exception when insufficient_privilege then null; end;
end $$;
-- ===== C2: chủ lớp xem số tổng hợp =====
select set_config('request.jwt.claim.sub', '10000000-0000-0000-0000-00000000000a', false);
select class_report(:'cid'::uuid) as rep \gset
select jsonb_array_length(:'rep'::jsonb) = 2 and (:'rep'::jsonb->0) ? 'days_30' and not ((:'rep'::jsonb->0) ? 'state') as ok \gset
\if :ok \else \echo 'FAIL class_report' \q \endif
select jsonb_array_length(my_classes()) = 1 and (my_classes()->0->>'owner')::boolean and (my_classes()->0->>'members')::int = 2 as ok \gset
\if :ok \else \echo 'FAIL my_classes owner' \q \endif
-- thành viên không thấy mã lớp trong my_classes (chỉ chủ lớp)
select set_config('request.jwt.claim.sub', '10000000-0000-0000-0000-00000000000b', false);
select (my_classes()->0->>'code') is null as ok \gset
\if :ok \else \echo 'FAIL member sees code' \q \endif
select leave_class(:'cid'::uuid) is null as x \gset
select jsonb_array_length(my_classes()) = 0 as ok \gset
\if :ok \else \echo 'FAIL leave' \q \endif

-- ===== C3: xếp hạng ngành — tự nguyện =====
select (league_board()->>'on')::boolean = false as ok \gset
\if :ok \else \echo 'FAIL league default off' \q \endif
select (set_league(true, 'Bình')->>'ok')::boolean as ok \gset
\if :ok \else \echo 'FAIL set_league' \q \endif
select set_config('request.jwt.claim.sub', '10000000-0000-0000-0000-00000000000c', false);
select set_league(true, 'Chi') is not null as x \gset
select league_board() as lb \gset
select (:'lb'::jsonb->>'on')::boolean and jsonb_array_length(:'lb'::jsonb->'rows') = 2 and (:'lb'::jsonb->'rows'->0->>'nick') = 'Bình' as ok \gset
\if :ok \else \echo 'FAIL league_board' :'lb' \q \endif

-- ===== C4: bạn học =====
select buddy_invite('Chi') as inv \gset
select (:'inv'::jsonb->>'code') as bcode \gset
select (buddy_accept(:'bcode', 'Chi')->>'error') = 'self' as ok \gset
\if :ok \else \echo 'FAIL buddy self' \q \endif
select set_config('request.jwt.claim.sub', '10000000-0000-0000-0000-00000000000b', false);
select (buddy_accept(lower(:'bcode'), 'Bình')->>'nick') = 'Chi' as ok \gset
\if :ok \else \echo 'FAIL buddy accept' \q \endif
select buddy_status() as bs \gset
select (:'bs'::jsonb->>'paired')::boolean and (:'bs'::jsonb->>'nick') = 'Chi' and (:'bs'::jsonb->>'shared_streak')::int = 1
   and (:'bs'::jsonb->>'me_today')::boolean and not (:'bs'::jsonb->>'buddy_today')::boolean as ok \gset
\if :ok \else \echo 'FAIL buddy_status' :'bs' \q \endif
select (buddy_nudge()->>'ok')::boolean as ok \gset
\if :ok \else \echo 'FAIL nudge' \q \endif
select (buddy_nudge()->>'error') = 'already' as ok \gset
\if :ok \else \echo 'FAIL nudge twice' \q \endif
-- dò mã lớp: 10 lần sai/giờ rồi bị chặn
do $$ begin for i in 1..10 loop perform join_class('ZZZZZZZ' || i, 'Dò', true); end loop;
  assert join_class('ZZZZZZZZ', 'Dò', true)->>'error' = 'rate_limited', 'join rate limit'; end $$;

-- ===== A1/A2: đăng ký push + giờ nhắc =====
select set_config('request.jwt.claim.sub', '10000000-0000-0000-0000-00000000000c', false);
select (save_push('{"endpoint":"https://push.example/c1","keys":{"p256dh":"k1","auth":"a1"}}', 'test')->>'ok')::boolean as ok \gset
\if :ok \else \echo 'FAIL save_push' \q \endif
do $$ begin begin perform save_push('{"endpoint":"http://x"}'); raise exception 'should fail'; exception when raise_exception then if sqlerrm <> 'bad_endpoint' then raise; end if; end; end $$;
select touch_reminder(8*60+10, 420) is null as x \gset
select set_config('request.jwt.claim.sub', '10000000-0000-0000-0000-00000000000b', false);
select save_push('{"endpoint":"https://push.example/b1","keys":{"p256dh":"k2","auth":"a2"}}') is not null as x \gset

reset role;
-- C học lần cuối hôm qua lúc 08:10 giờ VN → hôm nay nhắc từ 07:40 giờ VN (00:40 UTC). Có lời nhắc của bạn học → kind nudge
update reminder_prefs set first_min = 490 where user_id = '10000000-0000-0000-0000-00000000000c';
select kind = 'nudge' and from_nick = 'Bình' as ok from due_reminders((current_date::timestamp + interval '1 hour') at time zone 'UTC') where user_id = '10000000-0000-0000-0000-00000000000c' \gset
\if :ok \else \echo 'FAIL nudge due' \q \endif
select mark_pushed('10000000-0000-0000-0000-00000000000c', 'nudge', (current_date::timestamp + interval '1 hour') at time zone 'UTC') is null as x \gset
select count(*) = 0 as ok from due_reminders((current_date::timestamp + interval '3 hours') at time zone 'UTC') where user_id = '10000000-0000-0000-0000-00000000000c' \gset
\if :ok \else \echo 'FAIL max 1 push/day' \q \endif
select count(*) = 0 as ok from nudges where sent_at is null \gset
\if :ok \else \echo 'FAIL nudge marked sent' \q \endif
-- ngày hôm sau: vắng 2 ngày → winback2 (freeze còn) ; B học hôm nay → không nhắc
select count(*) = 0 as ok from due_reminders(((current_date + 1)::timestamp + interval '20 minutes') at time zone 'UTC') where user_id = '10000000-0000-0000-0000-00000000000c' \gset
\if :ok \else \echo 'FAIL too early (07:20 VN, nhắc từ 07:40)' \q \endif
select kind = 'winback2' and freeze_n = 1 and streak_n = 9 as ok from due_reminders(((current_date + 1)::timestamp + interval '3 hours') at time zone 'UTC') where user_id = '10000000-0000-0000-0000-00000000000c' \gset
\if :ok \else \echo 'FAIL winback2' \q \endif
select count(*) = 0 as ok from due_reminders((current_date::timestamp + interval '12 hours') at time zone 'UTC') where user_id = '10000000-0000-0000-0000-00000000000b' \gset
\if :ok \else \echo 'FAIL learned today → no push' \q \endif
-- vắng 5–6 ngày im lặng, ngày 7 gửi lần cuối, sau đó im hẳn
select count(*) = 0 as ok from due_reminders(((current_date + 5)::timestamp + interval '3 hours') at time zone 'UTC') where user_id = '10000000-0000-0000-0000-00000000000c' \gset
\if :ok \else \echo 'FAIL silent day 6' \q \endif
select kind = 'final7' as ok from due_reminders(((current_date + 6)::timestamp + interval '3 hours') at time zone 'UTC') where user_id = '10000000-0000-0000-0000-00000000000c' \gset
\if :ok \else \echo 'FAIL final7' \q \endif
select count(*) = 0 as ok from due_reminders(((current_date + 8)::timestamp + interval '3 hours') at time zone 'UTC') where user_id = '10000000-0000-0000-0000-00000000000c' \gset
\if :ok \else \echo 'FAIL silent after 7' \q \endif
-- tắt nhắc → không gửi
update reminder_prefs set mode = 'off' where user_id = '10000000-0000-0000-0000-00000000000c';
select count(*) = 0 as ok from due_reminders(((current_date + 1)::timestamp + interval '3 hours') at time zone 'UTC') where user_id = '10000000-0000-0000-0000-00000000000c' \gset
\if :ok \else \echo 'FAIL mode off' \q \endif
-- tổng kết tuần: tối Chủ nhật, đã học hôm đó
do $$ declare sun date := current_date + ((7 - extract(isodow from current_date)::int) % 7); r record; begin
  insert into daily_activity (user_id, day, track, tasks) values ('10000000-0000-0000-0000-00000000000b', sun, 'office', 1) on conflict do nothing;
  update reminder_prefs set last_push_day = null where user_id = '10000000-0000-0000-0000-00000000000b';
  select * into r from due_reminders((sun::timestamp + interval '13 hours') at time zone 'UTC') where user_id = '10000000-0000-0000-0000-00000000000b';
  assert r.kind = 'weekly' and r.week_days >= 1, 'weekly ' || coalesce(r.kind, 'null');
end $$;
-- múi giờ âm (-300): đã học hôm nay (UTC) → không nhắc; khung gửi không vượt sang ngày UTC khác
update reminder_prefs set mode = 'auto', tz_offset_min = -300, last_push_day = null, first_min = 600 where user_id = '10000000-0000-0000-0000-00000000000b';
select count(*) = 0 as ok from due_reminders((current_date::timestamp + interval '23 hours 50 minutes') at time zone 'UTC') where user_id = '10000000-0000-0000-0000-00000000000b' \gset
\if :ok \else \echo 'FAIL negative tz learned today' \q \endif
update reminder_prefs set tz_offset_min = 420 where user_id = '10000000-0000-0000-0000-00000000000b';
-- claim nguyên tử: gọi 2 lần liền → lần 2 không trả người đã nhận
update reminder_prefs set mode = 'auto', last_push_day = null where user_id = '10000000-0000-0000-0000-00000000000c';
select count(*) = 1 as ok from claim_reminders(((current_date + 1)::timestamp + interval '3 hours') at time zone 'UTC') where user_id = '10000000-0000-0000-0000-00000000000c' \gset
\if :ok \else \echo 'FAIL claim 1' \q \endif
select count(*) = 0 as ok from claim_reminders(((current_date + 1)::timestamp + interval '3 hours 5 minutes') at time zone 'UTC') where user_id = '10000000-0000-0000-0000-00000000000c' \gset
\if :ok \else \echo 'FAIL claim twice' \q \endif
select release_reminder('10000000-0000-0000-0000-00000000000c') is null as x \gset
select count(*) = 1 as ok from claim_reminders(((current_date + 1)::timestamp + interval '3 hours 10 minutes') at time zone 'UTC') where user_id = '10000000-0000-0000-0000-00000000000c' \gset
\if :ok \else \echo 'FAIL release' \q \endif
-- lỗi push tạm thời chỉ cộng 1 lần/ngày
do $$ declare sid bigint := (select id from push_subscriptions where endpoint = 'https://push.example/c1'); begin
  perform push_result(sid, false); perform push_result(sid, false); perform push_result(sid, false);
  assert (select fail_count from push_subscriptions where id = sid) = 1, 'fail once per day';
  perform push_result(sid, true); assert (select fail_count from push_subscriptions where id = sid) = 0, 'reset on ok';
end $$;
-- kết quả gửi: 410 → xoá đăng ký
select push_result((select id from push_subscriptions where endpoint = 'https://push.example/b1'), false, true) is null as x \gset
select count(*) = 1 as ok from push_subscriptions \gset
\if :ok \else \echo 'FAIL push gone' \q \endif
-- A9
update profiles set is_admin = true where id = '10000000-0000-0000-0000-00000000000a';
set role authenticated;
select set_config('request.jwt.claim.sub', '10000000-0000-0000-0000-00000000000a', false);
select (admin_quality()->>'talk_turns')::int = 12 and (admin_quality()->>'speak_minutes')::int = 5 as ok \gset
\if :ok \else \echo 'FAIL admin_quality' \q \endif
reset role;
-- xoá chủ lớp → lớp mất theo
delete from auth.users where id = '10000000-0000-0000-0000-00000000000a';
select count(*) = 0 as ok from classes \gset
\if :ok \else \echo 'FAIL cascade class' \q \endif
\echo 'ALL DB2 TESTS PASSED'
