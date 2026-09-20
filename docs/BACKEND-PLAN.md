# Kế hoạch backend cho Nói Nghề (Supabase · đăng nhập Google + Facebook)

> Nghiên cứu 20/09/2026 · app v3.1.1 · tài liệu kế hoạch, **chưa triển khai**.
> ⚠️ **Cập nhật:** chủ repo muốn **dữ liệu lưu trên server** → xem **§11 Phương án server-first** (nội dung bài học vào DB + xuất bản, khách tự động + liên kết Google/FB). §1–§10 là phương án local-first ban đầu, vẫn dùng cho phần đăng nhập, bảo mật, pháp lý, ngân sách.
> Mục tiêu: người học **tuỳ chọn** đăng nhập bằng Google/Facebook để đồng bộ tiến độ nhiều máy, dùng AI miễn phí có hạn mức,
> vào lớp học, chia sẻ gói "Nghề của tôi"; chủ app xem báo lỗi nội dung và thống kê. Chạy trong **gói Free** của Supabase càng lâu càng tốt.

---

## 1. Nguyên tắc thiết kế

1. **Máy người dùng là gốc (local-first).** `localStorage` vẫn là nơi lưu chính; không đăng nhập thì app chạy y như bây giờ, kể cả offline.
   Backend chỉ **đồng bộ** và cung cấp thứ bắt buộc phải có server (giữ key AI, lớp học, báo lỗi, thống kê).
2. **Nội dung bài học không vào database.** 9 gói ngành vẫn là file tĩnh trên GitHub Pages (rẻ, nhanh, offline được).
3. **Lưu ít nhất có thể.** Không lưu key AI của người dùng, ảnh, ghi âm, mật khẩu; lịch sử hội thoại chỉ giữ bản tóm tắt ngắn.
4. **Mọi bảng bật Row Level Security (RLS).** Anon key để lộ trong code là bình thường; an toàn nằm ở policy.
5. **Service role key và key AI chỉ nằm trong secrets của Edge Functions**, không bao giờ vào repo hay trình duyệt.

## 2. Kiến trúc

```
Trình duyệt (GitHub Pages: index.html, game/, packs/*.gen.js)
  │  supabase-js (tự host file vendor/supabase.min.js — CSP chỉ cho 'self')
  ├── Auth: Google / Facebook (OAuth, PKCE)  ─────────►  Supabase Auth
  ├── Đồng bộ tiến độ (REST, RLS theo user)  ─────────►  Postgres: progress, profiles
  ├── Báo lỗi, lớp học, gói chia sẻ, thống kê ────────►  Postgres (RLS) + RPC
  ├── AI (khi không có key riêng)  ──────────────────►  Edge Function `ai`  ──►  Gemini / Claude (key trong secrets)
  └── Lớp học: bảng xếp hạng (chỉ khi mở màn Lớp) ───►  Realtime
Meta ──(xoá dữ liệu người dùng)──► Edge Function `fb-data-deletion`
GitHub Actions: sao lưu pg_dump hằng tuần · ping giữ project không bị tạm dừng
```

### 2.1 Frontend: vẫn để trên GitHub Pages

**Có — giữ GitHub Pages cho frontend.** App là trang tĩnh (HTML/JS), còn đăng nhập, dữ liệu và AI đều gọi thẳng tới Supabase từ trình duyệt, nên không cần server riêng cho FE.
Đăng nhập Google/Facebook chạy tốt trên trang tĩnh: sau khi đăng nhập, Supabase chuyển về `https://hunglv201.github.io/it-english-app/` kèm mã, supabase-js tự đổi mã lấy phiên.

| | GitHub Pages (hiện tại) | Cloudflare Pages / Vercel / Netlify |
|---|---|---|
| Chi phí | Miễn phí | Miễn phí (gói cá nhân) |
| Deploy | Push `main` là xong (như bây giờ) | Nối repo GitHub, push là tự deploy |
| Giới hạn | Site ≤ 1 GB, băng thông mềm ~100 GB/tháng — thừa cho app này | Rộng hơn |
| Header bảo mật (CSP thật, cache) | Không đặt được header; CSP dùng thẻ `<meta>` như hiện tại (đủ dùng, riêng `frame-ancestors` không đặt được) | Đặt được file `_headers` |
| Bản xem trước theo nhánh/PR | Không | Có (tiện test đăng nhập trên nhánh) |
| Tên miền riêng | Có | Có |

Đề xuất: **MVP giữ GitHub Pages** (không phải đổi gì, chỉ thêm URL này vào danh sách redirect của Supabase/Google/Facebook).
Chỉ chuyển sang Cloudflare Pages khi cần tên miền riêng + header bảo mật hoặc bản xem trước theo nhánh; khi chuyển chỉ phải cập nhật lại các URL redirect ở 3 nơi.
Repo và quy trình git (commit, 2 nhánh, `push.sh`) giữ nguyên; thêm thư mục `supabase/` cho backend trong cùng repo.

Vùng đặt project: **Singapore (ap-southeast-1)** — gần Việt Nam nhất (độ trễ thấp). Lưu ý đây là chuyển dữ liệu ra nước ngoài (xem §8).

## 3. Đăng nhập Google + Facebook

### 3.1 Luồng trong app

- Nút **"Đăng nhập để đồng bộ"** ở Tôi › Tài khoản (và gợi ý nhẹ sau 7 ngày học). Không bắt buộc, không chặn bất kỳ tính năng offline nào.
- `supabase.auth.signInWithOAuth({provider:'google'|'facebook', options:{redirectTo: 'https://hunglv201.github.io/it-english-app/'}})`, dùng **PKCE**
  (supabase-js v2 mặc định cho web). Trang quay về → `exchangeCodeForSession` tự động → lần đồng bộ đầu (§5).
- Trước khi bấm đăng nhập: 1 dòng đồng ý có link **Chính sách quyền riêng tư** (bắt buộc theo luật + Google/Meta yêu cầu).
- Đăng xuất: xoá phiên, **giữ nguyên** dữ liệu trên máy. Xoá tài khoản: Tôi › Tài khoản › Xoá (xoá hết trên server).
- Cùng email ở Google và Facebook → Supabase tự **liên kết danh tính** vào một user (identity linking theo email đã xác minh).

### 3.2 Việc cần làm ở Google

1. Google Cloud Console → tạo project → **OAuth consent screen**: loại *External*, tên "Nói Nghề", logo, email hỗ trợ,
   link chính sách quyền riêng tư + điều khoản, scope chỉ `openid`, `email`, `profile` (không phải scope nhạy cảm → không cần thẩm định bảo mật).
2. **Credentials → OAuth client ID** loại *Web application*:
   Authorized JavaScript origins `https://hunglv201.github.io` (+ `http://localhost:8765` để dev);
   Authorized redirect URI `https://<project-ref>.supabase.co/auth/v1/callback`.
3. Dán Client ID/Secret vào Supabase → Authentication → Providers → Google. Thêm `https://hunglv201.github.io/it-english-app/**` vào **Redirect URLs**.
4. Chuyển consent screen sang *In production* (xác minh thương hiệu tuỳ chọn, vài ngày làm việc — nên làm để màn đăng nhập hiện tên + logo).

### 3.3 Việc cần làm ở Facebook (Meta)

1. developers.facebook.com → tạo app, use case **Authenticate and request data from users with Facebook Login**; bật quyền `public_profile` + `email`
   (thiếu `email` thì Supabase không lấy được email → đăng nhập lỗi).
2. Valid OAuth Redirect URI: `https://<project-ref>.supabase.co/auth/v1/callback`; App domain `hunglv201.github.io`.
3. Điền icon, **Privacy Policy URL**, **Data Deletion** (URL hướng dẫn *hoặc* callback — đề xuất callback Edge Function `fb-data-deletion`).
4. App mới ở **Development mode** — chỉ admin/tester đăng nhập được. Muốn mọi người dùng: gửi **App Review** (quay video luồng đăng nhập, giải thích dùng email để làm gì),
   thường 1–5 ngày làm việc, rồi chuyển **Live**. Có thể cần xác minh doanh nghiệp/cá nhân tuỳ thời điểm — tính trước thời gian chờ.
5. Dán App ID/Secret vào Supabase → Providers → Facebook.

### 3.4 Trang tĩnh cần thêm (GitHub Pages)

- `chinh-sach.html` — chính sách quyền riêng tư (thu gì, để làm gì, lưu ở đâu/bao lâu, quyền xem/sửa/xoá, liên hệ).
- `dieu-khoan.html` — điều khoản sử dụng ngắn (AI có thể sai, nội dung tham khảo, không phải tư vấn y tế/thuế…).
- `xoa-du-lieu.html` — hướng dẫn tự xoá tài khoản + trang tra trạng thái yêu cầu xoá (Meta trả về link này).

## 4. Backend quản lý gì · lưu gì

### 4.1 Bảng dữ liệu

| Bảng | Lưu gì | Không lưu | Ai đọc / ghi (RLS) | Dung lượng ước tính |
|---|---|---|---|---|
| `profiles` | `id` (= auth user), tên hiển thị, avatar URL (từ Google/FB), `track`, `role`, `level`, `created_at`, `last_seen_at`, `is_admin`, `ai_tier` | email (đã có trong `auth.users`), SĐT, ngày sinh | Chủ tài khoản đọc/sửa (trừ `is_admin`, `ai_tier`) | < 1 KB/người |
| `progress` | `user_id`, `store` (jsonb — bản **rút gọn** của `it-english-v1`: cfg, days/trackDays, srs, psrs, saved, myVocab, streak/stats, events, standups điểm), `game` (jsonb — `it-english-game-v1`), `rev` (số phiên bản), `updated_at`, `device` | key AI, lịch sử hội thoại đầy đủ (chỉ 5 buổi gần nhất dạng tóm tắt), ảnh | Chỉ chủ tài khoản | ~15–20 KB/người (Postgres nén jsonb) |
| `ai_usage` | `user_id`, `day`, `calls`, `tokens_in/out`, `provider` | nội dung prompt/trả lời | Chủ đọc; **chỉ Edge Function ghi** | ~60 B/người/ngày |
| `content_reports` | gói, loại (vocab/phrase/…), loại lỗi, trích nội dung, gợi ý sửa, `app_version`, `status` (mới/đã sửa/bỏ qua), `resolved_at`, `user_id` (có thể null) | — | Ai cũng **ghi** được (kể cả chưa đăng nhập, qua RPC có giới hạn); **chỉ admin đọc/sửa** | ~0,5 KB/báo lỗi |
| `custom_packs` | gói "Nghề của tôi": `owner`, nhãn, mô tả nghề (rút gọn), `data` (jsonb 3 chặng), `is_public`, `share_code`, `uses` | mô tả JD đầy đủ nếu không công khai | Chủ sửa/xoá; gói `is_public` ai cũng đọc | ~30 KB/gói |
| `classes` | `code` (6 ký tự), tên lớp, `track`, `owner`, `created_at` | — | Thành viên đọc; chủ sửa | nhỏ |
| `class_members` | `class_id`, `user_id`, biệt danh trong lớp, vai (owner/member), `joined_at` | — | Thành viên cùng lớp đọc; tự vào/ra | nhỏ |
| `daily_activity` | `user_id`, `day`, `track`, số việc xong, phút học ước tính (1 dòng/người/ngày — cho streak lớp + tỉ lệ quay lại) | từng lượt bấm | Chủ ghi (RPC upsert); admin đọc gộp | ~100 B/người/ngày |
| `app_config` | cấu hình: hạn mức AI/ngày, bật/tắt tính năng, phiên bản tối thiểu, thông báo | — | Ai cũng đọc; admin sửa | rất nhỏ |
| `deletion_requests` | mã xác nhận, `user_id`, nguồn (app/facebook), thời điểm, trạng thái | — | Chỉ Edge Function / admin | rất nhỏ |

View / RPC:
- `class_leaderboard(class_id)` — *security definer*, chỉ trả biệt danh + streak + số ngày học tuần này (không lộ dữ liệu khác).
- `report_content(...)` — ghi báo lỗi có kiểm tra độ dài + giới hạn ~20 báo lỗi/giờ/địa chỉ.
- `touch_activity(day, track, tasks)` — upsert `daily_activity`.
- `admin_stats(from, to)` — gộp: người dùng mới, DAU/WAU, tỉ lệ quay lại ngày 1/7/30, ngành được chọn, lượt AI.

### 4.2 Edge Functions

| Function | Làm gì |
|---|---|
| `ai` | Nhận `{prompt|messages, tier, image?}` + JWT → kiểm tra hạn mức (`ai_usage` + `app_config`) → gọi Gemini (hoặc Claude) bằng key trong secrets → ghi usage → trả text. Chặn prompt quá dài, ảnh > 1,5 MB; không log nội dung. |
| `fb-data-deletion` | Callback Meta: kiểm tra `signed_request` (HMAC bằng App Secret) → tìm user theo FB id → xoá → trả `{url, confirmation_code}` trỏ `xoa-du-lieu.html?code=…`. |
| `delete-account` | Người dùng tự xoá: xoá `progress`, `custom_packs` riêng, thành viên lớp, `auth.users` (cần service role nên phải là function). |
| `notify-report` *(tuỳ chọn)* | Khi có báo lỗi mới → gửi Telegram/email cho chủ app (Database Webhook). |

### 4.3 Chủ app quản lý ở đâu

- Giai đoạn đầu: **Supabase Studio** (dashboard có sẵn) + vài *saved query*: báo lỗi mới theo gói, người dùng mới/ngày, lượt AI/ngày, dung lượng DB.
- Sau: `admin.html` nhỏ trong repo (chỉ tài khoản `is_admin` mới gọi được RPC admin) — duyệt báo lỗi (đánh dấu đã sửa), xem thống kê, chỉnh `app_config`.

## 5. Đồng bộ tiến độ (phần khó nhất)

- **Khi nào:** lúc mở app (nếu đã đăng nhập), khi hoàn thành một việc (gom 5 giây mới gửi), khi rời trang (`visibilitychange`). Không realtime.
- **Kéo về:** chỉ hỏi `updated_at` + `rev` (vài trăm byte); nếu server mới hơn bản máy đang có mới tải `store` đầy đủ.
- **Gộp khi 2 máy cùng sửa** (không ghi đè mù):
  - `srs` / `psrs`: theo từng từ/câu, giữ bản có `reps` lớn hơn (hoà thì `due` muộn hơn).
  - `days.done`, `trackDays`: hợp (union) các ngày đã xong; `cur` lấy lớn hơn.
  - `saved`, `myVocab`, `reports` chưa gửi: hợp theo khoá (`en` / `t`).
  - streak, `stats.done`: lấy lớn hơn; `cfg`: theo `updated_at` của máy sửa sau.
  - game: `cleared`, `badges` hợp; `coins/xp/lv` lấy lớn hơn.
- **Lần đầu đăng nhập trên máy thứ hai:** hỏi "Gộp tiến độ của máy này với tài khoản?" (mặc định Gộp) — tránh mất dữ liệu.
- Bỏ khỏi bản đồng bộ: `ai` (key), `convos` đầy đủ (chỉ gửi 5 buổi gần nhất rút gọn), cache AI.

## 6. Bảo mật

- RLS mẫu: `progress` — `using (auth.uid() = user_id) with check (auth.uid() = user_id)`; `content_reports` — insert qua RPC, select chỉ `is_admin()`.
- Cột nhạy cảm (`is_admin`, `ai_tier`) không cho người dùng tự sửa: policy update chỉ cho các cột còn lại (hoặc trigger chặn).
- Edge Function `ai`: bắt buộc JWT hợp lệ, hạn mức theo ngày + theo phút, CORS chỉ cho `https://hunglv201.github.io`.
- Trình duyệt: thêm `https://<ref>.supabase.co` và `wss://<ref>.supabase.co` vào CSP `connect-src`; service worker **không** cache request tới Supabase.
- Kiểm thử RLS tự động: script đăng nhập 2 user giả, thử đọc/ghi chéo → phải bị từ chối.
- Sao lưu: gói Free không có backup → GitHub Action chạy `pg_dump` hằng tuần (lưu vào repo riêng tư hoặc artifact, mã hoá).
- Giữ project không bị tạm dừng (Free dừng sau 7 ngày không có request): GitHub Action gọi 1 request nhẹ mỗi ngày trong giai đoạn ít người dùng.

## 7. Ngân sách gói Free (tóm tắt từ phân tích trước)

| Giới hạn Free | Dùng cho | Chịu được |
|---|---|---|
| DB 500 MB | `progress` ~20 KB/người | ~20.000 tài khoản (chừa 30%) |
| Băng thông 5 GB/tháng | đồng bộ ~20 KB/người/ngày | ~8.000 người/ngày |
| Edge Function 500.000 lượt/tháng | AI ~10 lượt/người/ngày | **~1.600 người/ngày** — nút thắt chính |
| 50.000 MAU | đăng nhập | dư |
| Realtime 200 kết nối | bảng xếp hạng lớp (chỉ khi mở màn Lớp) | vài nghìn học viên |

Hạn mức AI mặc định đề xuất: **20 lượt/ngày/tài khoản** (chỉnh trong `app_config`); người có key riêng hoặc chạy trong claude.ai không tốn quota.
Lên **Pro (25 USD/tháng)** khi: DB > 350 MB, băng thông > 4 GB/tháng, Edge Function > 400.000 lượt/tháng hoặc ~1.000 người/ngày dùng AI qua server.
Chi phí thật lớn nhất là **phí gọi Gemini/Claude** nếu dùng key chung — cần đặt trần chi phí ở phía nhà cung cấp AI.

## 8. Pháp lý dữ liệu cá nhân (Việt Nam) — cần kiểm tra lại với người có chuyên môn

- Từ **01/01/2026**: **Luật Bảo vệ dữ liệu cá nhân 2025** và **Nghị định 356/2025/NĐ-CP** có hiệu lực, thay **Nghị định 13/2023/NĐ-CP**.
- Việc app cần làm tối thiểu: chính sách quyền riêng tư rõ ràng; **thu thập sự đồng ý** trước khi đăng nhập/đồng bộ; chỉ thu dữ liệu cần thiết;
  cho người dùng **xem, sửa, xoá, rút lại đồng ý** (nút Xoá tài khoản); xử lý sự cố lộ lọt; lưu vết yêu cầu xoá.
- Đặt server ở Singapore là **chuyển dữ liệu ra nước ngoài** → có thể phải lập hồ sơ đánh giá tác động chuyển dữ liệu; luật mới cũng có quy định về
  nhân sự/bộ phận bảo vệ dữ liệu và một số miễn trừ cho doanh nghiệp nhỏ/khởi nghiệp trong thời gian chuyển tiếp — **cần xác nhận cụ thể** trước khi mở cho người dùng thật.
- Không thu dữ liệu nhạy cảm: gói Y tế chỉ là nội dung học, app không hỏi tình trạng sức khoẻ; mô tả công việc người dùng tự nhập nên nhắc "đừng ghi tên công ty/khách hàng thật".

*(Đây là thông tin tham khảo, không phải tư vấn pháp lý.)*

## 9. Cấu trúc repo đề xuất

```
supabase/
  config.toml
  migrations/
    0001_core.sql            # profiles, progress, app_config + RLS + trigger tạo profile khi đăng ký
    0002_reports.sql         # content_reports + RPC report_content
    0003_ai_usage.sql        # ai_usage + hàm kiểm tra hạn mức
    0004_classes.sql         # classes, class_members, class_leaderboard()
    0005_packs_stats.sql     # custom_packs, daily_activity, admin_stats()
  functions/
    ai/index.ts
    fb-data-deletion/index.ts
    delete-account/index.ts
  tests/rls.test.mjs         # 2 user giả, thử đọc/ghi chéo
vendor/supabase.min.js       # supabase-js tự host (CSP 'self')
chinh-sach.html · dieu-khoan.html · xoa-du-lieu.html · admin.html (sau)
.github/workflows/backup.yml · keepalive.yml
```

Quản lý schema bằng **Supabase CLI** (`supabase db push`, `supabase functions deploy`) — mọi thay đổi DB là file migration trong git, không sửa tay trên dashboard.

## 10. Kế hoạch & ước lượng

Đơn vị: **ngày công** của 1 dev quen web (bảng bên phải: số **phiên làm việc với Claude** như các đợt trước).

| Đợt | Nội dung | Ngày công | Phiên Claude |
|---|---|---|---|
| **B0 · Nền** | Tạo project (Singapore), Supabase CLI, repo `supabase/`, vendor supabase-js, CSP, `app_config` | 0,5 | 0,3 |
| **B1 · Đăng nhập** | Google (consent screen, OAuth client), Facebook (app, quyền email, dev mode), nút đăng nhập/đăng xuất, trang Tài khoản, 3 trang chính sách/điều khoản/xoá dữ liệu | 1,5 | 0,5 |
| **B2 · Schema + RLS** | Migration 0001–0003, trigger tạo profile, test RLS tự động | 1 | 0,5 |
| **B3 · Đồng bộ** | Rút gọn store, kéo/đẩy, thuật toán gộp (§5), hỏi gộp lần đầu, đồng bộ cả game, xử lý offline/lỗi mạng, test 2 máy | 2 | 1 |
| **B4 · AI qua server** | Edge Function `ai` (Gemini + ảnh), hạn mức ngày/phút, đếm lượt còn lại trong app, rơi về key riêng / claude.ai | 1 | 0,5 |
| **B5 · Báo lỗi + xoá tài khoản** | RPC `report_content`, nút ⚑ ghi vào DB (GitHub là dự phòng), `delete-account`, `fb-data-deletion`, saved queries admin | 1 | 0,5 |
| **B6 · Vận hành** | Backup `pg_dump` hằng tuần, keepalive, cảnh báo gần hết quota, tài liệu CLAUDE.md | 0,5 | 0,3 |
| **= MVP** | Đăng nhập Google/FB · đồng bộ · AI miễn phí · báo lỗi · xoá tài khoản | **≈ 7,5** | **≈ 3,5** |
| B7 · Lớp học | classes, mã lớp, bảng xếp hạng (realtime khi mở màn), rời lớp | 1,5 | 0,7 |
| B8 · Chia sẻ gói nghề | `custom_packs` công khai, link `?pack=CODE`, đếm lượt dùng | 0,5 | 0,3 |
| B9 · Thống kê + admin.html | `daily_activity`, `admin_stats()`, trang admin duyệt báo lỗi, sửa `app_config` | 1,5 | 0,7 |
| **Tổng** | | **≈ 11** | **≈ 5** |

Thời gian chờ bên ngoài (không tính công): Meta App Review 1–5 ngày làm việc; xác minh thương hiệu Google vài ngày. **Nên nộp Meta review ngay khi xong B1**
(trong lúc chờ, Facebook chỉ dùng được với tài khoản tester; Google dùng được ngay).

### Thứ tự đề xuất

1. B0 → B1 (Google trước, Facebook ở chế độ dev) → nộp Meta review.
2. B2 → B3 (đồng bộ — phần giá trị nhất) → B4 → B5 → B6 = **bản MVP phát hành** (v4.0).
3. B7 → B8 → B9 khi đã có người dùng thật.

### Việc anh cần chuẩn bị / quyết định

- [ ] Tạo tài khoản Supabase + project (vùng Singapore), gửi **project URL + anon key** (không gửi service role key).
- [ ] Google Cloud project + consent screen (email hỗ trợ, logo); Meta developer account.
- [ ] Email liên hệ ghi trong chính sách quyền riêng tư; tên hiển thị (cá nhân hay tổ chức).
- [ ] Key AI dùng chung (Gemini) + đặt trần chi phí; chốt hạn mức miễn phí/ngày (đề xuất 20).
- [ ] Có mua tên miền riêng không (đẹp hơn cho màn đăng nhập và trang chính sách; không bắt buộc).

## 11. Phương án server-first (cập nhật theo yêu cầu: dữ liệu lưu trên server)

> Thay đổi so với §1: **server là nguồn dữ liệu chính** cho cả **nội dung bài học** lẫn **dữ liệu người học**.
> Máy người dùng chỉ còn là **bộ nhớ đệm** để chạy nhanh và dùng tạm khi mất mạng.

### 11.1 Nội dung bài học vào database (quản trị được, không cần sửa code)

**Bảng nội dung** (dùng chung cho mọi người, chỉ admin sửa):

| Bảng | Cột chính | Ghi chú |
|---|---|---|
| `tracks` | `id` (office, it, hotel…), nhãn, emoji, mô tả, `persona`, `counterpart`, `context`, `report` (jsonb), `podcast`, `sort`, `is_published` | 9 ngành + thêm ngành mới không cần sửa code |
| `track_roles` | `track_id`, `key`, nhãn, emoji, `sort` | 39 vai |
| `phases` | `id`, `track_id`, `idx`, `title`, `core_ref` (chặng lõi dùng chung) | 12 chặng/ngành (IT 37) |
| `vocab` | `id`, `phase_id`, `term`, `ipa`, `pos`, `vi`, `ex`, `ex_vi`, `ja`, `ja_romaji`, `sort` | ~1.190 từ |
| `phrase_groups` / `phrases` | nhóm (theo chặng hoặc nhóm chung), `en`, `vi`, `note` | ~1.600 câu (có ~610 câu chung) |
| `dialogues` / `dialogue_options` | câu người kia nói; 3 lựa chọn (`text`, `is_good`, `feedback`) — thuộc chặng **hoặc** vai | ~590 + ~200 theo vai |
| `listen_items` | `phase_id`, `sentence`, `blanks` (text[]), `hint`, `is_passage` | ~710 |
| `ai_scenarios` | `track_id`, `role_id` (tuỳ chọn), `key`, nhãn, `prompt` | tình huống AI |
| `reading_items`, `reverse_items`, `event_types`, `quips` | bài đọc 30 giây, câu dịch ngược, loại sự kiện, câu Mochi | |
| `content_revisions` | `table`, `row_id`, `before`, `after`, `by`, `at` | lịch sử sửa (trigger) — ai sửa gì, khôi phục được |
| `pack_releases` | `track_id`, `version`, `published_at`, `by`, `size`, `checksum`, `notes` | mỗi lần "Xuất bản" |

Dung lượng toàn bộ nội dung: ~7.000 dòng, **~3–5 MB** — không đáng kể so với 500 MB.
`content_reports` giờ trỏ thẳng tới `item_type` + `item_id` → mở báo lỗi là tới đúng dòng để sửa.

**Phục vụ nội dung cho app: "Xuất bản" thay vì truy vấn trực tiếp**

```
Admin sửa trong admin.html (hoặc Studio) ──► bảng nội dung (bản nháp)
        │ bấm "Xuất bản ngành X"
        ▼
Edge Function `publish-pack`: kiểm tra (luật như build.py: đủ 10 từ/chặng, 1 đáp án đúng, ô trống có thật…)
        → dựng JSON đúng định dạng packs/*.gen.js hiện tại → Storage (bucket công khai, qua CDN)
          packs/<track>/v<N>.json  +  packs/manifest.json {track: version}
        ▼
App: mở lên tải manifest (~1 KB) → khác version thì tải gói mới (~150 KB, gzip ~40 KB) → lưu IndexedDB → chạy offline như cũ
```

- Vì sao không để app truy vấn thẳng ~10 bảng mỗi lần mở: chậm, tốn băng thông DB (giới hạn 5 GB), khó chạy offline.
  File đã xuất bản đi qua CDN (**băng thông cache 5 GB riêng**) → ~100.000 lượt tải gói/tháng vẫn trong gói Free.
- Có **bản nháp / đã xuất bản**: sửa thoải mái, người học chỉ thấy khi bấm xuất bản; lỗi thì quay về version trước.
- `packs_src/*.py` + `build.py` dùng **một lần** để nhập (seed) dữ liệu hiện có vào DB; sau đó DB là bản gốc (có thể giữ script xuất ngược ra file để sao lưu vào git).
- Gói IT (data/phrases/roles.gen.js) cũng nhập vào cùng schema → mọi ngành quản lý một kiểu.

### 11.2 Dữ liệu người học lưu trên server

- Mọi thay đổi (ôn từ, xong ngày, lưu câu, điểm báo cáo 60s…) **ghi lên server**; máy giữ bản sao + **hàng đợi ghi (outbox)** khi mất mạng, có mạng lại thì đẩy lên.
- Cách lưu — cân nhắc giữa gọn và dễ truy vấn:

| Cách | Mô tả | Mỗi người (≈500 từ đã ôn) | Gói Free chứa | Hợp khi |
|---|---|---|---|---|
| **JSON một dòng** (`progress.store`) | như §4 | ~20 KB | ~20.000 người | chỉ cần đồng bộ |
| **Tách bảng hoàn toàn** (`user_srs` 1 dòng/từ, `user_days`, `user_saved`…) | chuẩn hoá | ~60–80 KB (dòng + index) | ~6.000 người | cần phân tích sâu từng từ |
| **Lai (đề xuất)** | JSON cho trạng thái chi tiết (SRS, cài đặt, game) **+** bảng riêng cho thứ cần truy vấn: `daily_activity`, `user_days` (ngày đã xong theo ngành), `attempts_daily` (số câu đúng/sai theo loại bài mỗi ngày), `ai_usage` | ~25 KB | ~15.000 người | đồng bộ + thống kê học tập đủ dùng |

Với phương án lai, admin xem được: ngày học, chặng đang học, tỉ lệ đúng theo loại bài/ngành, lượt AI — mà không phải bóc JSON.

### 11.3 Chế độ đăng nhập — 3 lựa chọn (nghiên cứu)

| | A. Bắt buộc đăng nhập | **B. Khách tự động + nâng cấp (đề xuất)** | C. Đăng nhập tuỳ chọn, máy là gốc (bản §1) |
|---|---|---|---|
| Cách chạy | Mở app → phải bấm Google/Facebook mới học | Mở app → app tự tạo **tài khoản khách** (`signInAnonymously`) ngầm → dữ liệu lên server ngay; bấm "Lưu tài khoản bằng Google/Facebook" (`linkIdentity`) để giữ lâu dài, dùng nhiều máy | Không đăng nhập = chỉ lưu trên máy |
| Dữ liệu trên server | 100% | 100% (cả khách) | Chỉ người đã đăng nhập |
| Rào cản lần đầu | **Cao** — nhiều người bỏ ngay ở màn đăng nhập | Không có | Không có |
| Nhiều máy | Có | Có sau khi liên kết Google/FB | Có sau khi đăng nhập |
| Rủi ro | Mất người dùng mới | Khách xoá trình duyệt/đăng xuất trước khi liên kết → mất tài khoản khách; tạo user rác → cần CAPTCHA (Cloudflare Turnstile) + giới hạn 30 lần/giờ/IP (mặc định Supabase); dọn khách không hoạt động > 30 ngày (SQL định kỳ — Supabase chưa tự dọn); liên kết vào email đã có tài khoản khác → phải tự viết logic gộp | Thống kê thiếu người không đăng nhập |
| Phân quyền | `authenticated` | Khách cũng là `authenticated`; phân biệt bằng claim `is_anonymous` trong RLS (vd khách không được tạo lớp, không chia sẻ gói công khai, hạn mức AI thấp hơn) | — |
| Dung lượng | theo số người đăng ký | tăng vì cả khách — nhờ dọn khách 30 ngày nên vẫn trong ~15.000 người hoạt động | ít nhất |

**Đề xuất: B.** Đúng yêu cầu "dữ liệu nằm trên server" mà không làm người mới bỏ đi vì bắt đăng nhập.
Luồng: mở app → khách (không hỏi gì) → sau 3 ngày học hoặc khi bấm tính năng cần tài khoản (lớp học, chia sẻ gói, dùng máy khác) → gợi ý "Lưu tiến độ bằng Google/Facebook".
Hạn mức AI gợi ý: khách 10 lượt/ngày, đã liên kết 20 lượt/ngày.

Việc cần xác minh thêm trước khi chốt (chưa có câu trả lời chắc chắn trong tài liệu):
- Người dùng khách có **tính vào MAU** không (ảnh hưởng mốc 50.000 MAU) — tài liệu anonymous sign-in không nói rõ; giả định là **có** để tính an toàn.
- Hành vi `linkIdentity` khi email Google/FB **đã thuộc** một tài khoản khác → thiết kế màn "Tài khoản này đã có tiến độ — gộp hay dùng tiến độ nào?".
- iOS Safari có thể **xoá dữ liệu trang web sau 7 ngày không mở** (chính sách chống theo dõi) → khách chưa liên kết trên iPhone dễ mất phiên → nhắc liên kết sớm hơn trên iOS.

### 11.4 Các cách đăng nhập khác (để cân nhắc sau)

| Cách | Supabase hỗ trợ sẵn | Ghi chú |
|---|---|---|
| Google | Có | làm trước |
| Facebook | Có | cần Meta App Review |
| Email OTP / magic link | Có | dự phòng cho người không dùng Google/FB; gói Free gửi email rất hạn chế → cần SMTP riêng (vd Resend) |
| Apple | Có | chỉ bắt buộc nếu sau này lên App Store có đăng nhập mạng xã hội |
| **Zalo** | **Không** (không có sẵn) | phổ biến ở VN; muốn có phải tự viết luồng OAuth Zalo trong Edge Function rồi tạo phiên Supabase — khoảng +1,5–2 ngày công, để sau |

### 11.5 Ước lượng thêm cho phương án server-first

| Việc thêm | Ngày công | Phiên Claude |
|---|---|---|
| Schema nội dung + script nhập 9 gói + IT vào DB, kiểm tra khớp 100% với file hiện tại | 1,5 | 0,7 |
| `publish-pack` (kiểm tra + dựng JSON + Storage + manifest), app tải/cache gói theo version (IndexedDB), bỏ `document.write` | 1,5 | 0,7 |
| Trình sửa nội dung trong `admin.html` (danh sách chặng, sửa từ/câu/hội thoại/bài nghe, xem trước, lịch sử, xuất bản) | 2,5 | 1 |
| Khách tự động + liên kết Google/FB + màn gộp tài khoản + dọn khách 30 ngày + Turnstile | 1 | 0,5 |
| Hàng đợi ghi offline (outbox) + bảng lai (`user_days`, `attempts_daily`) | 1 | 0,5 |
| **Cộng thêm** | **≈ 7,5** | **≈ 3,4** |

**MVP server-first** (B0–B6 ở §10 + 11.5) ≈ **15 ngày công ≈ 7 phiên**. Có thể chia 2 bước:
1. **Bước 1 (≈ 9 ngày):** khách tự động + Google/Facebook + dữ liệu người học trên server + AI qua server + báo lỗi — nội dung vẫn là file tĩnh.
2. **Bước 2 (≈ 6 ngày):** đưa nội dung vào DB + xuất bản + trình sửa nội dung cho admin.

## Nguồn

- [Supabase — Sign in with Google](https://supabase.com/docs/guides/auth/social-login/auth-google)
- [Supabase — Sign in with Facebook](https://supabase.com/docs/guides/auth/social-login/auth-facebook)
- [Supabase — Anonymous sign-ins](https://supabase.com/docs/guides/auth/auth-anonymous)
- [Supabase — PKCE flow](https://supabase.com/docs/guides/auth/sessions/pkce-flow)
- [Supabase — signInWithOAuth](https://supabase.com/docs/reference/javascript/auth-signinwithoauth)
- [DesignRevision — Supabase Free Tier Limits 2026](https://designrevision.com/blog/supabase-pricing) · [UI Bakery — Supabase Pricing 2026](https://uibakery.io/blog/supabase-pricing)
- [Thư viện Pháp luật — NĐ 13/2023 hết hiệu lực từ 01/01/2026](https://thuvienphapluat.vn/chinh-sach-phap-luat-moi/vn/ho-tro-phap-luat/chinh-sach-moi/102230/nghi-dinh-13-2023-nd-cp-ve-bao-ve-du-lieu-ca-nhan-het-hieu-luc-tu-01-01-2026)
- [EY — Nghị định 356/2025/NĐ-CP hướng dẫn Luật Bảo vệ dữ liệu cá nhân](https://www.ey.com/content/dam/ey-unified-site/ey-com/vi-vn/technical/tax/documents/ey-vietnam-legal-alert-march-2026-decree-no356-2025-nd-cp-providing-detailed-guidance-for-implementation-of-personal-data-protection-law-viet.pdf)

---

## Phụ lục A — SQL phác thảo (migration 0001)

```sql
-- profiles: tạo tự động khi user đăng ký
create table public.profiles (
  id uuid primary key references auth.users on delete cascade,
  display_name text, avatar_url text,
  track text default 'office', role text, level text default 'A2',
  is_admin boolean not null default false,
  ai_tier text not null default 'free',
  created_at timestamptz default now(), last_seen_at timestamptz default now()
);
alter table public.profiles enable row level security;
create policy "own profile read"   on public.profiles for select using (auth.uid() = id);
create policy "own profile update" on public.profiles for update using (auth.uid() = id)
  with check (auth.uid() = id and is_admin = (select is_admin from public.profiles where id = auth.uid())
              and ai_tier = (select ai_tier from public.profiles where id = auth.uid()));

create function public.handle_new_user() returns trigger language plpgsql security definer set search_path = public as $$
begin
  insert into public.profiles (id, display_name, avatar_url)
  values (new.id, new.raw_user_meta_data->>'full_name', new.raw_user_meta_data->>'avatar_url');
  return new;
end $$;
create trigger on_auth_user_created after insert on auth.users for each row execute function public.handle_new_user();

-- progress: 1 dòng / người
create table public.progress (
  user_id uuid primary key references auth.users on delete cascade,
  store jsonb not null default '{}', game jsonb, rev int not null default 0,
  device text, updated_at timestamptz not null default now()
);
alter table public.progress enable row level security;
create policy "own progress" on public.progress for all
  using (auth.uid() = user_id) with check (auth.uid() = user_id);

-- cấu hình đọc công khai
create table public.app_config (key text primary key, value jsonb not null);
alter table public.app_config enable row level security;
create policy "config readable" on public.app_config for select using (true);
insert into public.app_config values ('ai_daily_free', '20'), ('min_app_version', '"3.1.0"');
```
