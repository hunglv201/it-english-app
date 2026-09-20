# Kế hoạch triển khai backend — Nói Nghề (Supabase · server-first · offline · đăng nhập Google)

> Bản gộp 20/09/2026 · app v3.1.1 · tài liệu kế hoạch, **chưa triển khai**.
> Thay thế các bản nháp trước (local-first, có Facebook). **Không làm đăng nhập Facebook.**

---

## 0. Quyết định đã chốt

| Chủ đề | Chốt |
|---|---|
| Backend | **Supabase**, vùng **Singapore (ap-southeast-1)**, gói **Free** càng lâu càng tốt |
| Dữ liệu | **Server là nguồn gốc** cho cả nội dung bài học lẫn dữ liệu người học; máy chỉ là bản sao làm việc |
| Tài khoản | Mở app → **tài khoản khách tự động** (`signInAnonymously`) → nâng cấp bằng **Google** (`linkIdentity`) để giữ lâu dài, dùng nhiều máy |
| Đăng nhập | **Chỉ Google**. Không Facebook. Email OTP / Zalo để backlog |
| Offline | Học được đầy đủ khi mất mạng; ghi local trước, outbox đồng bộ sau |
| Frontend | Giữ **GitHub Pages** (trang tĩnh gọi thẳng Supabase) |
| AI | Qua Edge Function `ai`, key chung trong secrets; hạn mức **khách 10 / Google 20 lượt/ngày**; ai có key riêng hoặc chạy trong claude.ai thì không tốn quota |

## 1. Kiến trúc

```
Trình duyệt (GitHub Pages: index.html, game/, admin.html)
  ├─ Service Worker: vỏ app (HTML/JS/CSS, vendor/supabase.min.js)
  ├─ IndexedDB: packs (gói ngành đã xuất bản) · state (bản sao dữ liệu người học) · outbox (thay đổi chờ gửi)
  │
  ├── Auth: khách tự động + Google (OAuth PKCE, linkIdentity) ──► Supabase Auth
  ├── RPC apply_changes / get_state / report_content …       ──► Postgres (RLS)
  ├── Tải gói ngành (manifest + JSON theo version)            ──► Storage (bucket công khai, CDN)
  └── AI / xuất bản gói / xoá tài khoản                       ──► Edge Functions: ai · publish-pack · delete-account
                                                                      └► Gemini / Claude (key trong secrets)
GitHub Actions: backup pg_dump hằng tuần · keepalive hằng ngày · dọn khách không hoạt động > 30 ngày
```

- supabase-js **tự host** (`vendor/supabase.min.js`) vì CSP chỉ cho `'self'`; thêm `https://<ref>.supabase.co` + `wss://` vào `connect-src`.
- Service worker **không** cache request tới Supabase (trừ file gói đã có version).
- Repo, 2 nhánh, `push.sh` giữ nguyên; backend nằm trong thư mục `supabase/` cùng repo.
- Chuyển sang Cloudflare Pages chỉ khi cần tên miền riêng + header bảo mật + bản xem trước theo nhánh (khi đó chỉ cập nhật lại URL redirect ở Supabase và Google).

## 2. Tài khoản

### 2.1 Luồng

1. Mở app lần đầu → tạo **khách** ngầm (có Cloudflare Turnstile chống tạo user rác) → dữ liệu lên server ngay, không hỏi gì.
2. Gợi ý **"Lưu tiến độ bằng Google"** khi: học đủ 3 ngày · bấm tính năng cần tài khoản (dùng máy khác, lớp học, chia sẻ gói) · trên iOS sớm hơn (Safari có thể xoá dữ liệu trang sau 7 ngày không mở).
3. Bấm → `linkIdentity({provider:'google'})` → quay về app, cùng user id, không mất gì.
4. Nếu Google đó **đã có tài khoản khác** → màn gộp: "Tài khoản này đã có tiến độ — Gộp (mặc định) / Dùng tiến độ tài khoản / Dùng tiến độ máy này" → đăng nhập tài khoản cũ + đẩy dữ liệu khách qua `apply_changes`.
5. Máy thứ hai: "Đăng nhập bằng Google" → kéo dữ liệu về.
6. Đăng xuất: giữ bản sao trên máy cho tới khi người dùng chọn xoá. **Xoá tài khoản**: Tôi › Tài khoản › Xoá (xoá hết trên server).
7. Trước khi liên kết: 1 dòng đồng ý có link Chính sách quyền riêng tư.

Phân quyền: khách và Google đều là `authenticated`; phân biệt bằng claim `is_anonymous` trong RLS (khách không tạo lớp, không chia sẻ gói công khai, hạn mức AI thấp hơn).

### 2.2 Việc cần làm ở Google

1. Google Cloud Console → project → **OAuth consent screen**: *External*, tên "Nói Nghề", logo, email hỗ trợ, link chính sách + điều khoản; scope chỉ `openid email profile` (không nhạy cảm → không cần thẩm định bảo mật).
2. **OAuth client ID** loại *Web application*: origins `https://hunglv201.github.io` (+ `http://localhost:8765`); redirect URI `https://<ref>.supabase.co/auth/v1/callback`.
3. Dán Client ID/Secret vào Supabase → Auth → Providers → Google; thêm `https://hunglv201.github.io/it-english-app/**` vào Redirect URLs; bật **Anonymous sign-ins** và **Manual linking**.
4. Chuyển consent screen sang *In production* (xác minh thương hiệu vài ngày — để màn đăng nhập hiện tên + logo).

### 2.3 Trang tĩnh cần thêm

`chinh-sach.html` (quyền riêng tư) · `dieu-khoan.html` (điều khoản: AI có thể sai, nội dung tham khảo, không phải tư vấn y tế/thuế) · `xoa-du-lieu.html` (hướng dẫn tự xoá tài khoản).

## 3. Server lưu gì

### 3.1 Nội dung bài học (dùng chung, chỉ admin sửa)

| Bảng | Cột chính |
|---|---|
| `tracks` | `id`, nhãn, emoji, mô tả, `persona`, `counterpart`, `context`, `report` jsonb, `podcast`, `sort`, `is_published` |
| `track_roles` | `track_id`, `key`, nhãn, emoji, `sort` (39 vai) |
| `phases` | `id`, `track_id`, `idx`, `title`, `core_ref` (chặng lõi dùng chung) |
| `vocab` | `phase_id`, `term`, `ipa`, `pos`, `vi`, `ex`, `ex_vi`, `ja`, `ja_romaji`, `sort` (~1.190) |
| `phrase_groups` / `phrases` | `en`, `vi`, `note` (~1.600) |
| `dialogues` / `dialogue_options` | câu người kia nói; 3 lựa chọn `text`, `is_good`, `feedback` — thuộc chặng hoặc vai (~790) |
| `listen_items` | `sentence`, `blanks` text[], `hint`, `is_passage` (~710) |
| `ai_scenarios`, `reading_items`, `reverse_items`, `event_types`, `quips` | tình huống AI, bài đọc, dịch ngược, sự kiện, câu Mochi |
| `content_revisions` | lịch sử sửa (trigger): bảng, dòng, trước/sau, ai, lúc nào |
| `pack_releases` | `track_id`, `version`, `published_at`, `by`, `size`, `checksum`, `notes` |

Toàn bộ nội dung ~7.000 dòng, ~3–5 MB.

### 3.2 Dữ liệu người học (mô hình lai)

| Bảng | Lưu gì | RLS |
|---|---|---|
| `profiles` | tên, avatar (từ Google), `track`, `role`, `level`, `is_anonymous`, `ai_tier`, `is_admin`, `created_at`, `last_seen_at` | chủ đọc/sửa (trừ `is_admin`, `ai_tier`) |
| `user_state` | jsonb trạng thái chi tiết: cfg, SRS từ/câu, câu đã lưu, từ của tôi, streak, game, gói "Nghề của tôi" riêng; `rev`, `updated_at` | chủ **chỉ đọc**; ghi qua RPC `apply_changes` |
| `user_days` | ngày đã xong theo ngành (`user_id`, `track`, `day`, `done_at`) | chủ đọc; ghi qua RPC |
| `daily_activity` | 1 dòng/người/ngày: ngành, số việc xong, phút ước tính | chủ đọc; admin xem gộp |
| `attempts_daily` | số câu đúng/sai theo loại bài mỗi ngày | chủ đọc; admin xem gộp |
| `applied_changes` | id các thay đổi đã áp (chống gửi trùng), giữ 30 ngày | chỉ server |
| `ai_usage` | lượt + token AI theo ngày, không lưu nội dung | chủ đọc; chỉ function ghi |
| `content_reports` | báo lỗi: `item_type`, `item_id`, loại lỗi, gợi ý sửa, `app_version`, `status` | ai cũng gửi (RPC có giới hạn); chỉ admin đọc/sửa |

≈ **25 KB/người** → gói Free chứa khoảng **15.000 người** hoạt động.

### 3.3 Vận hành

`app_config` (hạn mức AI, phiên bản tối thiểu, bật/tắt tính năng, thông báo) · `deletion_requests` (lưu vết yêu cầu xoá).

### 3.4 Không lưu

Key AI của người dùng · ảnh chụp tài liệu · ghi âm · nội dung prompt/trả lời AI · lịch sử hội thoại đầy đủ (chỉ tóm tắt 5 buổi gần nhất) · mật khẩu · SĐT · ngày sinh.

## 4. Xuất bản nội dung

```
Admin sửa trong admin.html (hoặc Supabase Studio) ──► bảng nội dung (bản nháp)
        │ bấm "Xuất bản ngành X"
        ▼
Edge Function publish-pack: kiểm tra (luật như build.py: đủ từ/chặng, đúng 1 đáp án tốt, ô trống có thật…)
        → dựng JSON đúng định dạng packs/*.gen.js → Storage: packs/<track>/v<N>.json + packs/manifest.json
        ▼
App mở lên: tải manifest (~1 KB) → khác version thì tải gói mới (~40 KB gzip) → lưu IndexedDB → dùng offline
```

- Có nháp / đã xuất bản; lỗi thì quay về version trước.
- `packs_src/*.py` + `build.py` chỉ dùng **một lần** để nhập 9 gói + IT vào DB; sau đó DB là bản gốc (script xuất ngược ra file để sao lưu vào git).
- Bỏ `document.write` trong loader: app đọc gói từ IndexedDB (lần đầu offline dùng gói Công sở có sẵn trong Service Worker).

## 5. Offline & đồng bộ

- Mọi thao tác học **ghi bản sao IndexedDB trước** → màn hình cập nhật ngay → thêm vào outbox `{id, ts, op, data}` (vd `srs.grade`, `day.done`, `saved.add`, `report.add`, `activity.touch`).
- Bộ đồng bộ chạy khi: mở app · có mạng lại · quay lại tab · mỗi 60s nếu còn outbox · trước khi đóng tab.
  1. Đẩy outbox theo lô ≤ 50 → RPC `apply_changes(changes, base_rev)` → server áp theo luật gộp, trả `rev` mới → xoá mục đã nhận.
  2. Kéo về: so `rev`; server mới hơn → tải bản đầy đủ → gộp vào bản sao.
  3. Lỗi mạng/5xx → thử lại 5s, 15s, 60s, 5 phút; 401 → làm mới phiên rồi gửi lại.
- Mỗi thay đổi có **id duy nhất** → gửi lại không bị cộng đôi.
- **Luật gộp**: SRS theo từng từ/câu giữ bản `reps` lớn hơn (hoà thì `due` muộn hơn) · ngày đã xong hợp lại, `cur` lấy lớn hơn · câu lưu, từ của tôi hợp theo khoá · streak, `stats`, coins/xp/lv lấy lớn hơn · `cleared`, `badges` hợp · `cfg` theo thời điểm sửa sau.
- `navigator.storage.persist()` lúc đầu; không dùng Background Sync (iOS không hỗ trợ).
- Trường hợp đặc biệt: lần đầu mở không có mạng → chạy chế độ máy, ghi outbox, có mạng thì tạo khách rồi đẩy lên · phiên hết hạn khi offline lâu → vẫn học bình thường, có mạng thì làm mới phiên · outbox quá lớn → gộp bớt thao tác cùng khoá · app quá cũ → server trả mã yêu cầu cập nhật.

| Chạy offline đầy đủ | Offline có giới hạn | Cần mạng |
|---|---|---|
| Hôm nay, Lộ trình, từ vựng + SRS, câu thường dùng, nghe (giọng máy), chọn cách đáp, dịch ngược tự gõ, game (trừ Boss AI), streak, thống kê | Báo lỗi ⚑ (xếp hàng), đổi ngành (chỉ ngành đã tải), nhận giọng nói (tuỳ trình duyệt), chấm ngữ pháp bằng luật có sẵn | Mọi thứ gọi AI, liên kết Google, lớp học, tải gói chưa có |

Hiển thị: chấm trạng thái ✓ đã đồng bộ · ↻ đang đồng bộ · ⏸ offline (N chờ gửi); Tôi › Tài khoản có "Lần đồng bộ cuối" + nút "Đồng bộ ngay". Không bao giờ chặn việc học vì mất mạng.

## 6. Hàm phía server

| Tên | Loại | Làm gì |
|---|---|---|
| `apply_changes(changes, base_rev)` | RPC | áp outbox theo luật gộp, bỏ id trùng, cập nhật `user_state`/`user_days`/`daily_activity`/`attempts_daily`, trả `rev` |
| `get_state()` | RPC | trả `user_state` + `rev` |
| `report_content(...)` | RPC | ghi báo lỗi, kiểm tra độ dài, ≤ 20 lần/giờ |
| `admin_stats(from, to)` | RPC (admin) | người mới, DAU/WAU, quay lại ngày 1/7/30, ngành được chọn, lượt AI |
| `ai` | Edge Function | JWT → kiểm hạn mức theo ngày + phút → gọi Gemini/Claude (có ảnh) → ghi `ai_usage` → trả text; chặn prompt quá dài, ảnh > 1,5 MB; không log nội dung |
| `publish-pack` | Edge Function (admin) | kiểm tra + dựng JSON + Storage + manifest + `pack_releases` |
| `delete-account` | Edge Function | xoá toàn bộ dữ liệu + `auth.users` (cần service role) |

## 7. Bảo mật

- Mọi bảng bật **RLS**; anon key lộ trong code là bình thường.
- Dữ liệu người học chỉ ghi qua RPC `security definer` → không ai ghi thẳng jsonb tuỳ ý.
- `is_admin`, `ai_tier` không cho người dùng tự sửa (policy + trigger).
- **Service role key và key AI chỉ nằm trong Supabase secrets**, không bao giờ vào repo, `.env` được push, hay trình duyệt.
- Edge Function: bắt buộc JWT, CORS chỉ `https://hunglv201.github.io` (+ localhost khi dev).
- Turnstile khi tạo khách; giới hạn tạo user 30 lần/giờ/IP.
- Test RLS tự động: 2 user giả thử đọc/ghi chéo → phải bị từ chối.

## 8. Ngân sách gói Free

| Giới hạn Free | Dùng cho | Chịu được |
|---|---|---|
| DB 500 MB | ~25 KB/người + nội dung ~5 MB | ~15.000 người hoạt động (có dọn khách 30 ngày) |
| Băng thông DB 5 GB/tháng | đồng bộ | ~8.000 người/ngày |
| Băng thông cache/CDN 5 GB | tải gói ngành | ~100.000 lượt tải gói/tháng |
| Edge Function 500.000 lượt/tháng | AI | **~1.600 người/ngày dùng AI** — nút thắt chính |
| 50.000 MAU | tính cả khách (giả định an toàn) | dư |
| Tạm dừng sau 7 ngày không có request | — | keepalive hằng ngày |

Lên **Pro (25 USD/tháng)** khi DB > 350 MB, băng thông > 4 GB/tháng hoặc Edge Function > 400.000 lượt/tháng. Chi phí thật lớn nhất là **phí gọi Gemini/Claude** → đặt trần chi phí ở nhà cung cấp AI.

## 9. Pháp lý (Việt Nam) — cần kiểm tra lại với người có chuyên môn

- Từ 01/01/2026: **Luật Bảo vệ dữ liệu cá nhân 2025** + **Nghị định 356/2025/NĐ-CP** (thay Nghị định 13/2023).
- Tối thiểu: chính sách quyền riêng tư rõ; thu thập sự đồng ý; chỉ thu dữ liệu cần thiết; cho xem/sửa/xoá/rút đồng ý; xử lý sự cố lộ lọt; lưu vết yêu cầu xoá.
- Tài khoản khách vẫn là dữ liệu cá nhân (gắn với thiết bị) → chính sách phải nói rõ ngay từ lần mở đầu (dòng thông báo nhỏ + link).
- Server ở Singapore = **chuyển dữ liệu ra nước ngoài** → có thể cần hồ sơ đánh giá tác động; xác nhận miễn trừ cho cá nhân/doanh nghiệp nhỏ trước khi mở cho người dùng thật.
- Không thu dữ liệu nhạy cảm; nhắc "đừng ghi tên công ty/khách hàng thật" ở ô mô tả công việc.

*(Thông tin tham khảo, không phải tư vấn pháp lý.)*

## 10. Cấu trúc repo

```
supabase/
  config.toml
  migrations/
    0001_users.sql        # profiles, user_state, user_days, daily_activity, attempts_daily, applied_changes, app_config + RLS + trigger
    0002_sync.sql         # apply_changes, get_state
    0003_reports_ai.sql   # content_reports, report_content, ai_usage + hạn mức, admin_stats
    0004_content.sql      # bảng nội dung, content_revisions, pack_releases
    0005_release.sql      # quyền publish, bucket packs
  functions/ai · publish-pack · delete-account
  seed/import_packs.mjs   # nhập packs_src + gói IT vào DB, kiểm tra khớp 100%
  tests/rls.test.mjs · sync.test.mjs
vendor/supabase.min.js
chinh-sach.html · dieu-khoan.html · xoa-du-lieu.html · admin.html
.github/workflows/backup.yml · keepalive.yml · cleanup-guests.yml
```

Schema quản lý bằng **Supabase CLI** (`supabase db push`, `supabase functions deploy`); không sửa tay trên dashboard.

## 11. Kế hoạch triển khai

Đơn vị: ngày công của 1 dev quen web · số phiên làm việc với Claude.

### Bước 1 — v4.0: tài khoản + dữ liệu người học trên server + offline (nội dung vẫn là file tĩnh)

| Đợt | Nội dung | Ngày | Phiên |
|---|---|---|---|
| **P0 · Nền** | Project Singapore, Supabase CLI, thư mục `supabase/`, vendor supabase-js, CSP, `app_config` | 1 | 0,5 |
| **P1 · Tài khoản** | Khách tự động + Turnstile; Google + `linkIdentity`; màn gộp khi Google đã có tài khoản; trang Tài khoản; `delete-account`; 3 trang chính sách/điều khoản/xoá dữ liệu | 2 | 1 |
| **P2 · Schema + RLS** | Migration 0001–0003, trigger profile, test RLS tự động | 1 | 0,5 |
| **P3 · Offline & đồng bộ** | `localStorage` → IndexedDB (state/outbox), `apply_changes` gộp theo thao tác, chống trùng, backoff, chuyển dữ liệu người dùng cũ lên server lần đầu, chấm trạng thái, test offline 2 trình duyệt | 3 | 1,5 |
| **P4 · AI qua server** | Edge Function `ai` (Gemini + ảnh), hạn mức 10/20, đếm lượt còn lại, rơi về key riêng / claude.ai | 1 | 0,5 |
| **P5 · Báo lỗi + thống kê** | ⚑ ghi vào `content_reports` (GitHub issue là dự phòng), `daily_activity`, `attempts_daily`, `admin_stats`, saved queries trong Studio | 1 | 0,5 |
| **P6 · Vận hành** | Backup `pg_dump` hằng tuần, keepalive, dọn khách > 30 ngày, cảnh báo gần hết quota, cập nhật CLAUDE.md | 0,5 | 0,3 |
| **Cộng Bước 1** | | **≈ 9,5** | **≈ 4,8** |

### Bước 2 — v4.1: nội dung vào database + xuất bản + trình sửa

| Đợt | Nội dung | Ngày | Phiên |
|---|---|---|---|
| **P7 · Nội dung vào DB** | Migration 0004, `seed/import_packs.mjs` nhập 9 gói + IT, kiểm tra khớp 100% với file hiện tại | 1,5 | 0,7 |
| **P8 · Xuất bản** | `publish-pack`, Storage + manifest, app tải/cache gói theo version, bỏ `document.write` | 1,5 | 0,7 |
| **P9 · admin.html** | Duyệt báo lỗi (mở thẳng dòng cần sửa), sửa từ/câu/hội thoại/bài nghe, xem trước, lịch sử, xuất bản, sửa `app_config`, thống kê | 2,5 | 1 |
| **Cộng Bước 2** | | **≈ 5,5** | **≈ 2,4** |

**Tổng ≈ 15 ngày công ≈ 7 phiên.** Thời gian chờ bên ngoài: chỉ xác minh thương hiệu Google (vài ngày, không chặn — Google dùng được ngay).

### Backlog (sau v4.1)

Lớp học + bảng xếp hạng (1,5 ngày) · chia sẻ gói "Nghề của tôi" bằng link `?pack=CODE` (0,5) · đăng nhập email OTP với SMTP riêng (0,5) · Zalo (tự viết OAuth, 1,5–2) · chuyển sang Cloudflare Pages + tên miền riêng.

### Việc anh cần chuẩn bị

- [ ] Tài khoản Supabase + project vùng Singapore → gửi **project URL + anon key** (không gửi service role key; lưu ở `.env` local, không push).
- [ ] Google Cloud project + consent screen (email hỗ trợ, logo).
- [ ] Cloudflare Turnstile site key (miễn phí).
- [ ] Email liên hệ ghi trong chính sách; tên hiển thị (cá nhân hay tổ chức).
- [ ] Key Gemini dùng chung + đặt trần chi phí; xác nhận hạn mức 10/20 lượt/ngày.

## Nguồn

- [Supabase — Sign in with Google](https://supabase.com/docs/guides/auth/social-login/auth-google)
- [Supabase — Anonymous sign-ins](https://supabase.com/docs/guides/auth/auth-anonymous)
- [Supabase — Identity linking](https://supabase.com/docs/guides/auth/auth-identity-linking)
- [Supabase — PKCE flow](https://supabase.com/docs/guides/auth/sessions/pkce-flow)
- [DesignRevision — Supabase Free Tier Limits 2026](https://designrevision.com/blog/supabase-pricing) · [UI Bakery — Supabase Pricing 2026](https://uibakery.io/blog/supabase-pricing)
- [Thư viện Pháp luật — NĐ 13/2023 hết hiệu lực từ 01/01/2026](https://thuvienphapluat.vn/chinh-sach-phap-luat-moi/vn/ho-tro-phap-luat/chinh-sach-moi/102230/nghi-dinh-13-2023-nd-cp-ve-bao-ve-du-lieu-ca-nhan-het-hieu-luc-tu-01-01-2026)
- [EY — Nghị định 356/2025/NĐ-CP](https://www.ey.com/content/dam/ey-unified-site/ey-com/vi-vn/technical/tax/documents/ey-vietnam-legal-alert-march-2026-decree-no356-2025-nd-cp-providing-detailed-guidance-for-implementation-of-personal-data-protection-law-viet.pdf)

---

## Phụ lục A — SQL phác thảo (migration 0001, rút gọn)

```sql
create table public.profiles (
  id uuid primary key references auth.users on delete cascade,
  display_name text, avatar_url text,
  track text default 'office', role text, level text default 'A2',
  is_anonymous boolean not null default true,
  is_admin boolean not null default false,
  ai_tier text not null default 'guest',          -- guest | google
  created_at timestamptz default now(), last_seen_at timestamptz default now()
);
alter table public.profiles enable row level security;
create policy "own profile read" on public.profiles for select using (auth.uid() = id);
create policy "own profile update" on public.profiles for update using (auth.uid() = id)
  with check (auth.uid() = id
    and is_admin = (select p.is_admin from public.profiles p where p.id = auth.uid())
    and ai_tier  = (select p.ai_tier  from public.profiles p where p.id = auth.uid()));

-- tạo profile khi đăng ký (kể cả khách) và cập nhật khi khách liên kết Google
create function public.handle_user() returns trigger language plpgsql security definer set search_path = public as $$
begin
  insert into public.profiles (id, display_name, avatar_url, is_anonymous, ai_tier)
  values (new.id, new.raw_user_meta_data->>'full_name', new.raw_user_meta_data->>'avatar_url',
          coalesce(new.is_anonymous, false), case when coalesce(new.is_anonymous, false) then 'guest' else 'google' end)
  on conflict (id) do update set
    display_name = coalesce(excluded.display_name, profiles.display_name),
    avatar_url   = coalesce(excluded.avatar_url, profiles.avatar_url),
    is_anonymous = excluded.is_anonymous,
    ai_tier      = case when profiles.ai_tier = 'guest' then excluded.ai_tier else profiles.ai_tier end;
  return new;
end $$;
create trigger on_auth_user_ins after insert on auth.users for each row execute function public.handle_user();
create trigger on_auth_user_upd after update of is_anonymous, raw_user_meta_data on auth.users
  for each row execute function public.handle_user();

-- trạng thái chi tiết: chỉ đọc; ghi qua RPC apply_changes (security definer)
create table public.user_state (
  user_id uuid primary key references auth.users on delete cascade,
  state jsonb not null default '{}', rev bigint not null default 0,
  updated_at timestamptz not null default now()
);
alter table public.user_state enable row level security;
create policy "own state read" on public.user_state for select using (auth.uid() = user_id);

create table public.app_config (key text primary key, value jsonb not null);
alter table public.app_config enable row level security;
create policy "config readable" on public.app_config for select using (true);
insert into public.app_config values
  ('ai_daily_guest', '10'), ('ai_daily_google', '20'), ('min_app_version', '"3.1.0"');
```
