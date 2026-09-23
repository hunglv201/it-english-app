# Backend Nói Nghề v4.0 — hướng dẫn dựng & vận hành

> v4.0.0 (đã merge `main`) · Bước 1 của [`BACKEND-PLAN.md`](BACKEND-PLAN.md) (P0–P6) + đợt A/C của [`TINH-NANG-MOI-2026-09-23.md`](TINH-NANG-MOI-2026-09-23.md) (nhắc học Web Push, lớp học, bảng tuần, bạn học): tài khoản khách + Google, dữ liệu người học trên server,
> offline, AI qua server, báo lỗi, thống kê, vận hành. Nội dung bài học vẫn là file tĩnh (Bước 2 · v4.1 mới đưa vào DB).
> **Chưa điền `cloud-config.js` thì app chạy y như v3.1** (chỉ lưu trên máy) — an toàn để merge trước khi có project.

## Thành phần

| File | Vai trò |
|---|---|
| `cloud-config.js` | URL + anon key Supabase, site key Turnstile (đều công khai). Để trống = tắt máy chủ |
| `sync-core.js` | Hàm thuần: làm phẳng dữ liệu học ↔ bản đồ `path → value`, tính thay đổi, luật gộp (giống hệt SQL) |
| `cloud.js` | Khách tự động, liên kết Google, bộ đồng bộ offline-first (outbox), AI qua server, gửi báo lỗi |
| `vendor/supabase.min.js` | supabase-js 2.116 tự host (CSP chỉ cho `'self'`); chỉ tải khi đã cấu hình |
| `index.html` | Thẻ tài khoản ở Tôi, màn Tài khoản & đồng bộ, chấm trạng thái trên tab Tôi (chỉ hiện khi đang gửi / offline còn thay đổi / cần xử lý), thẻ gợi ý "Lưu bằng Google", màn gộp tiến độ |
| `chinh-sach.html` · `dieu-khoan.html` · `xoa-du-lieu.html` | Trang pháp lý (cần điền email liên hệ — chỗ tô vàng) |
| `supabase/migrations/*.sql` | 0001 người dùng + RLS · 0002 đồng bộ `apply_changes` · 0003 báo lỗi, hạn mức AI, thống kê, dọn khách · 0004 nhắc học Web Push (`claim_reminders`, lời nhắc bạn học, `admin_quality`) · 0005 lớp học, bảng tuần theo ngành, bạn học · 0006 tổng kết tuần qua email (`claim_weekly_emails`, huỷ nhận bằng token) |
| `supabase/functions/ai` | Gọi Gemini (hoặc Claude) bằng key chung, kiểm hạn mức ngày + phút, không log nội dung |
| `supabase/functions/delete-account` | Người dùng tự xoá tài khoản (cần service role) |
| `supabase/functions/send-reminders` | Gửi nhắc học 15 phút/lần (header `x-cron-secret`), web-push VAPID, ≤ 1 thông báo/ngày/người · v4.2: email tổng kết tuần qua Resend (tối Chủ nhật, người dùng tự bật, chỉ Google) |
| `supabase/queries/admin.sql` | Truy vấn lưu sẵn cho Studio: báo lỗi mới, DAU, tỉ lệ đúng, lượt AI, dung lượng |
| `.github/workflows/backend-*.yml` | Sao lưu `pg_dump` hằng tuần (mã hoá) · keepalive + dọn khách hằng ngày · gọi `send-reminders` 15 phút/lần |

## Cách đồng bộ chạy

1. Mọi thao tác học ghi `localStorage` trước (app chạy ngay, kể cả offline) → `save()` gọi `NNCloud.touch()` → sau 3 giây đồng bộ.
2. Dữ liệu học được làm phẳng: `srs|deploy`, `tdays|hotel|done|12`, `saved|<câu>`, `cfg|level`… (không gồm key AI, lượt chat đầy đủ, giọng đọc, giờ nhắc).
3. So với **shadow** (bản đã khớp server lần cuối) → lô thay đổi `{p, v | d, b}` (≤ 250) → RPC `apply_changes(id, changes, base_rev)`.
   Lô đang gửi được lưu lại; mất phản hồi thì gửi lại **cùng id** → server bỏ qua, không cộng đôi.
4. Server so `b` (giá trị máy thấy lần cuối) với giá trị hiện tại: khớp → ghi; khác (máy khác vừa sửa) → luật gộp:
   thẻ ôn giữ bản `reps` lớn hơn (hoà → hạn ôn muộn hơn) · `hist`, `stats` số, `cur` lấy lớn hơn · xoá thua sửa · còn lại bản sau thắng.
5. `rev` server nhảy (máy khác đã ghi) → kéo `get_state` → gộp 3 chiều (máy / shadow / server) → cập nhật màn hình.
6. Đăng nhập tài khoản đã có tiến độ trong khi máy cũng có tiến độ → hỏi **Gộp cả hai** (mặc định) / Dùng tài khoản / Dùng máy này.
7. Chạy lại khi: mở app · có mạng lại · quay lại tab · mỗi 60 giây nếu còn thay đổi · lỗi thì thử lại sau 5s, 15s, 60s, 5 phút.

Server tự suy ra bảng thống kê từ các thay đổi: `user_days` (ngày đã học), `daily_activity` (việc/ngày), `attempts_daily` (đúng/sai theo loại bài).

## Dựng project (một lần)

1. **Supabase**: tạo project vùng *Southeast Asia (Singapore)*. Cài CLI: `npm i -g supabase` → `supabase login` → `supabase link --project-ref <ref>`.
2. **Schema**: `supabase db push` (chạy 3 migration). Kiểm tra: Table Editor thấy `profiles`, `user_state`… đều bật RLS.
3. **Auth** (Dashboard → Authentication):
   - Sign In / Providers: bật **Anonymous sign-ins**, bật **Allow manual linking**, **tắt Email** (app chỉ dùng khách + Google; hạn mức AI "google" chỉ cấp khi có danh tính Google thật).
   - Google: tạo OAuth client *Web application* ở Google Cloud Console — origin `https://hunglv201.github.io`, redirect `https://<ref>.supabase.co/auth/v1/callback`; dán Client ID/Secret.
   - URL Configuration: Site URL `https://hunglv201.github.io/it-english-app/`; Redirect URLs thêm `https://hunglv201.github.io/it-english-app/**` và `http://localhost:8765/**`.
   - Attack Protection → CAPTCHA: Cloudflare Turnstile, dán secret; rồi điền `turnstileSiteKey` trong `cloud-config.js`. **Bắt buộc trước khi mở cho người dùng thật** — không có captcha thì ai cũng tạo được hàng loạt khách bằng anon key (mỗi khách 10 lượt AI/ngày; `ai_daily_global` là lưới an toàn cuối).
4. **Edge Functions**:
   ```bash
   supabase secrets set GEMINI_API_KEY=...            # key chung — đặt trần chi phí ở Google AI Studio
   # tuỳ chọn: GEMINI_MODEL=gemini-2.5-flash · AI_PROVIDER=claude + ANTHROPIC_API_KEY=... · ALLOWED_ORIGINS=https://hunglv201.github.io
   supabase functions deploy ai
   supabase functions deploy delete-account
   # nhắc học (Web Push): tạo khoá VAPID một lần
   npx web-push generate-vapid-keys            # → Public Key (điền vapidPublicKey trong cloud-config.js) + Private Key
   supabase secrets set VAPID_PUBLIC_KEY=... VAPID_PRIVATE_KEY=... VAPID_SUBJECT=mailto:<email> CRON_SECRET=<chuỗi ngẫu nhiên dài>
   supabase functions deploy send-reminders
   # tuỳ chọn v4.2 — email tổng kết tuần (không đặt thì bỏ qua phần email): tạo tài khoản Resend, xác minh tên miền gửi
   supabase secrets set RESEND_API_KEY=... EMAIL_FROM="Nói Nghề <hello@ten-mien-cua-ban>" APP_URL=https://hunglv201.github.io/it-english-app/
   ```
   Lịch chạy: workflow `backend-reminders.yml` (cần secret `CRON_SECRET` trong GitHub) **hoặc** `pg_cron` + `pg_net` trong Supabase:
   `select cron.schedule('nn-reminders', '*/15 * * * *', $$ select net.http_post(url := '<SUPABASE_URL>/functions/v1/send-reminders', headers := jsonb_build_object('x-cron-secret', '<CRON_SECRET>')) $$);` — chỉ chọn **một** trong hai (hai cái cùng chạy vẫn không gửi trùng nhờ `claim_reminders`, nhưng tốn lượt gọi).
   `SUPABASE_URL`, `SUPABASE_SERVICE_ROLE_KEY` có sẵn trong môi trường function — **không** đưa service role key vào repo hay `cloud-config.js`.
5. **App**: điền `url` + `anonKey` (Project Settings → API) và `vapidPublicKey` vào `cloud-config.js`, bump `CACHE` trong `sw.js`, push.
6. **Admin**: đăng nhập app bằng Google → lấy id ở Authentication → Users → `update public.profiles set is_admin = true where id = '<id>';`
7. **GitHub Actions**: Settings → Secrets and variables → Actions:
   - Variables: `NN_BACKEND_ENABLED=true`, `SUPABASE_URL`, `SUPABASE_ANON_KEY`.
   - Secrets: `SUPABASE_DB_URL` (Project Settings → Database → Connection string, *Session pooler*), `BACKUP_PASSPHRASE`.
   - Giải mã bản sao lưu: `gpg -d noinghe-YYYY-MM-DD.sql.gz.gpg | gunzip > dump.sql`.
8. Điền email liên hệ trong 3 trang pháp lý (chỗ tô vàng).

## Cấu hình khi chạy (`app_config`)

| key | mặc định | ý nghĩa |
|---|---|---|
| `ai_daily_guest` / `ai_daily_google` / `ai_daily_plus` | 10 / 20 / 100 | lượt AI miễn phí mỗi ngày theo `profiles.ai_tier` |
| `ai_per_minute` | 6 | chống spam |
| `ai_daily_global` | 3000 | trần tổng lượt AI/ngày của cả app (bảo vệ chi phí key chung) |
| `min_app_version` | `"4.0.0"` | bản app cũ hơn → server từ chối ghi, app tự tải lại bản mới |

## Nhắc học, lớp học, bạn học (0004, 0005)

- **Nhắc học**: app đăng ký push sau khi người dùng bấm "Bật nhắc học" (thẻ ở Hôm nay sau ngày học đầu tiên, hoặc Tài khoản › Nhắc học). Mỗi ngày học đầu tiên app gửi giờ bắt đầu (`touch_reminder`) → hôm sau nhắc lúc −30 phút.
  `due_reminders()` chỉ trả người **chưa học hôm nay**, trong khung 7:00–21:30 giờ địa phương (gói trong một ngày UTC, cùng quy ước ngày với app), mỗi người ≤ 1 thông báo/ngày:
  vắng 1 ngày `daily` · 2–4 ngày `winback2/3/4` · 5–6 ngày im · ngày 7 `final7` (lần cuối) · sau đó im hẳn · tối Chủ nhật `weekly` (đã học hôm đó) · bạn học nhắc `nudge` (chỉ khi còn là bạn học, vắng ≤ 7 ngày).
  `claim_reminders()` đánh dấu nguyên tử trước khi gửi; gửi hỏng hết → `release_reminder()`; lỗi push chỉ cộng `fail_count` 1 lần/ngày, 404/410 xoá đăng ký; app gửi lại đăng ký mỗi ngày.
- **Lớp học**: chỉ tài khoản Google tạo lớp (≤ 10), mã 8 ký tự, ≤ 200 thành viên; vào lớp cần tick đồng ý (lưu `consent_at`), nhập sai mã ≤ 10 lần/giờ.
  Thành viên thấy: biệt danh, số ngày/số việc tuần này, chuỗi. Chủ lớp thêm: ngày vào lớp, số ngày 30 ngày, lần học gần nhất, ngành (+ CSV). Không ai thấy câu trả lời, lỗi, ghi âm, email.
- **Bảng tuần**: tự bật bằng biệt danh; nhóm ~20 người cùng ngành (theo thứ tự đăng ký), tính từ Thứ Hai, không có rớt hạng.
- **Bạn học**: link mời `?buddy=CODE` (8 ký tự, 7 ngày), mỗi người 1 bạn học, chuỗi chung = số ngày liên tiếp cả hai cùng học, nhắc bạn 1 lần/ngày (qua push).

## Kiểm thử

```bash
node tests/sync-core.test.mjs                                   # lõi đồng bộ (không cần trình duyệt)
PGHOST=... PGPORT=... PGUSER=postgres supabase/tests/db_test.sh # migration + RLS + apply_changes (db.test.sql) + nhắc học/lớp học/bạn học (db2.test.sql)
tests/run.sh                                                    # Playwright a–k; i.mjs, k.mjs dùng server giả (tests/cloud-fake.mjs)
```

`tests/i.mjs` kiểm: khách tự tạo + đẩy tiến độ sẵn có · học → tự đồng bộ · offline → chờ gửi → online gửi đủ · gửi lại lô không cộng đôi ·
AI qua server · báo lỗi lên server · liên kết Google giữ nguyên dữ liệu · máy 2 gặp "Google đã có tài khoản" → đăng nhập → tự lấy tiến độ ·
2 máy cùng offline sửa một từ → gộp đúng · máy 3 nhiều tiến độ → hỏi gộp → gộp cả hai · xoá tài khoản → về chế độ máy ·
server từ chối lô → giữ nguyên dữ liệu máy · mất phiên → không tự tạo khách, đăng nhập lại đúng tài khoản · supabase-js thật + máy chủ không tới được → app vẫn chạy, thử lại giãn dần.
Migration được kiểm thêm bằng một lượt rà soát độc lập (RLS, quyền mặc định của Supabase, hàm SECURITY DEFINER, luật gộp SQL ↔ JS).
Edge Functions đã `deno check`; mã hoá web-push (aes128gcm + VAPID) chạy được trong Deno; chưa chạy thật với Supabase (cần project).

## Giới hạn đã biết của bước này

- Bản sao trên máy vẫn là `localStorage` (khởi động đồng bộ, đủ nhanh với dữ liệu hiện tại); chuyển IndexedDB để sau nếu dữ liệu lớn lên.
- Game (`game/`) được đồng bộ khi mở app chính (đọc cùng `localStorage`), không đồng bộ riêng khi chỉ mở game.
- Đổi ngành trên máy khác: máy này nhận `cfg.track` mới nhưng chỉ chuyển gói khi mở lại app (có thông báo).
- `admin.html` (duyệt báo lỗi, sửa nội dung) thuộc Bước 2; tạm dùng Studio + `supabase/queries/admin.sql`.
- Bộ đếm (`hist`, `stats.done`, streak) gộp bằng "lấy lớn hơn": 2 máy cùng offline mỗi máy 5 việc → gộp ra 5, không phải 10. Chấp nhận được cho streak/heatmap; nếu cần đếm chính xác thì chuyển sang đếm theo từng máy.
- Máy từng có tài khoản mà mất phiên (token hết hạn, bị đăng xuất nơi khác) → **không** tự tạo khách mới; màn Tài khoản báo "Phiên đăng nhập đã hết" và cho đăng nhập lại (hoặc tạo khách mới nếu trước đó là khách).
- AI: chỉ trả lại lượt khi lỗi mạng / nhà cung cấp 5xx·429 (tối đa 5 lần/ngày); câu trả lời rỗng vẫn tính lượt; lượt cuối của hội thoại phải là người dùng.
