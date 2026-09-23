-- Truy vấn lưu sẵn cho Supabase Studio (SQL Editor → lưu thành "saved query"). Chạy bằng quyền dashboard.

-- 1) Báo lỗi nội dung mới, theo ngành
select id, created_at::date, track, kind, type, left(excerpt, 120) as noi_dung, note as goi_y, place
from public.content_reports where status = 'new' order by created_at desc limit 200;

-- 2) Đánh dấu đã sửa
-- update public.content_reports set status = 'fixed', resolved_at = now() where id in (…);

-- 3) Người dùng mới mỗi ngày (khách / Google)
select created_at::date as ngay, count(*) filter (where is_anonymous) as khach, count(*) filter (where not is_anonymous) as google
from public.profiles group by 1 order by 1 desc limit 30;

-- 4) DAU 30 ngày, và theo ngành
select day, count(*) as dau from public.daily_activity where day > current_date - 30 group by day order by day desc;
select track, count(distinct user_id) as nguoi from public.daily_activity where day > current_date - 7 group by track order by 2 desc;

-- 5) Tỉ lệ đúng theo loại bài (7 ngày)
select kind, sum(ok) as dung, sum(fail) as sai, round(100.0 * sum(ok) / nullif(sum(ok) + sum(fail), 0), 1) as pct_dung
from public.attempts_daily where day > current_date - 7 group by kind;

-- 6) Lượt AI mỗi ngày + token (theo dõi chi phí)
select day, count(*) as nguoi, sum(calls) as luot, sum(tokens_in) as tok_in, sum(tokens_out) as tok_out
from public.ai_usage group by day order by day desc limit 30;

-- 7) Dung lượng DB (gói Free: 500 MB) + bảng lớn nhất
select pg_size_pretty(pg_database_size(current_database())) as db;
select relname, pg_size_pretty(pg_total_relation_size(relid)) from pg_catalog.pg_statio_user_tables order by pg_total_relation_size(relid) desc limit 10;

-- 8) Cấp quyền admin cho chính mình (lấy id ở Authentication → Users)
-- update public.profiles set is_admin = true where id = '<uuid>';
-- 9) Đổi hạn mức AI
-- update public.app_config set value = '15' where key = 'ai_daily_guest';
