# Lịch sử phiên bản — Nói Nghề (trước đây IT English)

Ghi theo thứ tự mới → cũ. **Version lớn** (x.0.0) đi kèm một trang giới thiệu riêng; trang của version lớn cũ được giữ lại
làm bản lưu trữ (`gioi-thieu-v<N>.html`) để xem lại app từng trông thế nào.

| Version lớn | Trang giới thiệu | Ảnh chụp |
|---|---|---|
| **v4.x** (hiện tại) | [`gioi-thieu.html`](https://hunglv201.github.io/it-english-app/gioi-thieu.html) | `img/showcase/v4/` |
| v3.x | [`gioi-thieu-v3.html`](https://hunglv201.github.io/it-english-app/gioi-thieu-v3.html) (lưu trữ) | `img/showcase/v3/` |
| v2.0 | [`gioi-thieu-v2.html`](https://hunglv201.github.io/it-english-app/gioi-thieu-v2.html) (lưu trữ) | `img/showcase/v2/` |
| v1.x | [`gioi-thieu-v1.html`](https://hunglv201.github.io/it-english-app/gioi-thieu-v1.html) (lưu trữ 13/09/2026) | `img/showcase/` |

---

## v4.3.0 — 23/09/2026 · Anh ⇄ Nhật cho BrSE, sổ lỗi, chuẩn bị nhanh, mẫu email

**App**
- 🤝 **Anh ⇄ Nhật cho IT / BrSE** (`ja/brse.js`, nạp lười): 80 câu song ngữ trong 10 nhóm — 報告, 連絡, 相談, xác nhận spec & Q&A, ước lượng & lịch, bug & sự cố, xin lỗi & trễ hạn, họp với khách, review & nghiệm thu, email/chat. Furigana + romaji + giọng Nhật; luyện **Nghe Anh → nói Nhật** và **Nghe Nhật → nói Anh** (chấm theo ký tự / theo từ). Kiểm duyệt: `docs/review/brse.md` — nên nhờ thêm người Nhật đọc duyệt.
- 📒 **Sổ lỗi cá nhân**: tự gom lỗi từ Giao tiếp AI (phần AI sửa), dịch ngược, chọn cách đáp, nghe chép, đọc theo (từ phát âm chưa đúng) và song ngữ; chia nhóm (thì, mạo từ, giới từ, số nhiều, thiếu chủ ngữ/động từ, câu cộc, trật tự từ, phát âm…). **Ôn lỗi 5 phút** — nói lại câu đúng, đúng 2 lần liền là "đã nắm"; thẻ nhắc ở Hôm nay mỗi tuần khi có ≥ 5 lỗi.
- 📅 **Chuẩn bị nhanh** cho sự kiện sắp tới (họp, ca, phỏng vấn…): thêm giờ; bấm "Chuẩn bị" → 5 câu cần nói + 3 câu có thể bị hỏi (AI; không có AI thì lấy câu hợp chủ đề trong gói), thêm vào ôn câu, luyện nói 3 phút có dùng đúng các câu đó; sau sự kiện app hỏi "thế nào?" — Khó thì mở luyện lại.
- 📨 **Mẫu email & tin nhắn** (`mail/templates.js`, nạp lười): 55 mẫu — 16 dùng chung + 3 mẫu riêng cho mỗi ngành; điền vài ô → email/tin nhắn chuẩn, 3 giọng (chuẩn / lịch sự hơn / ngắn cho chat), sao chép, mở ứng dụng mail, nghe đọc; **AI chỉnh câu** (sửa ngữ pháp, dịch ô gõ tiếng Việt). Kiểm duyệt: `docs/review/mail.md`.

**Kỹ thuật**
- `store.mistakes[]` (đồng bộ qua máy chủ, khoá `key`), `store.events[].time/prep/after`, `store.cfg.myName/mailVals`. Test `tests/n.mjs`.

## v4.2.0 — 23/09/2026 · 2 ngành mới, boss game, rảnh tay bằng giọng nói, ảnh → bộ bài học, email tổng kết tuần

**Nội dung**
- 2 ngành mới, mỗi ngành 20 chặng · 200 ngày, 4 vai, kiểm duyệt chéo (`docs/review/education.md`, `legal.md`) → **13 ngành, 55 vai**:
  - 🎓 **Giáo dục · Đào tạo** — giáo viên song ngữ, trợ giảng, tư vấn tuyển sinh · du học, giáo vụ · liên lạc phụ huynh.
  - ⚖️ **Luật · Hành chính công** — pháp chế doanh nghiệp, trợ lý công ty luật, cán bộ một cửa, phiên dịch · dịch thuật công chứng (không nêu điều luật/mức phí cụ thể).

**Game**
- **Boss cuối mỗi chặng** theo ngành (khách khó tính, thanh tra, kiểm toán, hành khách gây rối, khách Nhật khó tính…): 3 pha — hội thoại chọn đáp → nghe điền từ → dịch, lấy từ dữ liệu của chính chặng đó.
- **Kết cục**: hạ boss chặng cuối (hoặc đủ boss mọi chặng) → câu chuyện "Bạn đã trở thành…" theo ngành + thống kê + thưởng xu; chế độ **Vô tận** lưu kỷ lục. Hồ sơ › Boss chặng & kết cục.

**App**
- **Rảnh tay**: ra lệnh bằng giọng nói tiếng Anh — *next* (bỏ qua), *again* (nghe lại), *slower* / *faster*, *stop*; nút trên tai nghe / màn khoá (Media Session) khi trình duyệt hỗ trợ.
- **Ảnh → bài học**: lưu cả bài (từ, câu trả lời mẫu, câu hỏi, tình huống) thành **bộ** để mở lại, xoá; **đọc chữ ngay trên máy** (Tesseract, tự host `vendor/tesseract/`, ≈ 11 MB tải lần đầu) khi AI không đọc được ảnh hoặc chưa cấu hình AI — ảnh không gửi đi đâu; có AI thì tạo bài từ chữ, không có thì tra từ có trong gói ngành.
- **Tổng kết tuần qua email** (tuỳ chọn, mặc định tắt, chỉ tài khoản Google): tối Chủ nhật, ≤ 1 email/tuần, tự dừng khi 4 tuần không học, huỷ 1 chạm (`?unsub=`). Cần máy chủ + secret Resend (`docs/BACKEND.md`).

**Kỹ thuật**
- Migration `0006_email.sql` (`email_prefs`, `email_status`, `set_email_weekly`, `claim_weekly_emails`, `release_weekly_email`, `email_unsubscribe`) + `supabase/tests/db3.test.sql`. `send-reminders` gửi email qua Resend khi có `RESEND_API_KEY` + `EMAIL_FROM` (thiếu VAPID vẫn chạy phần email).
- Test mới: `tests/l.mjs` (boss + kết cục game), `tests/m.mjs` (lệnh giọng nói, bộ ảnh, OCR thật trên ảnh vẽ bằng canvas); `k.mjs` thêm email + 2 ngành mới.

## v4.1.0 — 23/09/2026 · Làm giàu nội dung mọi ngành

**Nội dung**
- Mỗi ngành (10 ngành ngoài IT) thêm **8 chặng mới** → **20 chặng · 200 ngày** (trước 12 chặng · 120 ngày). Mỗi chặng: 10 từ (IPA, ví dụ, nhiều từ có tiếng Nhật), 8–10 câu mẫu, 5 hội thoại chọn đáp, 6 bài nghe (4 câu + 2 đoạn).
  - Công sở: hội nhập & văn hoá công ty, đàm phán, khách hàng & đối tác, đào tạo, làm việc từ xa, đánh giá hiệu suất, công tác nước ngoài, tiệc & xã giao.
  - Khách sạn: concierge, đưa đón sân bay, spa & hồ bơi, bar, tiệc & hội nghị, phục vụ tại phòng, đánh giá online, an ninh & khẩn cấp.
  - Bán hàng: B2B, demo, đàm phán hợp đồng, bán thêm & bán chéo, hội chợ, gọi lạnh, CRM, gia hạn.
  - Nhà máy: bản vẽ & thông số, nguyên vật liệu, đóng gói & xuất hàng, môi trường & hoá chất, tự động hoá & PLC, OEE & KPI, giao ca, sự cố khẩn cấp.
  - Logistics: air freight, hàng lạnh & hàng nguy hiểm, TMĐT & chặng cuối, bảo hiểm, L/C, đóng container, tối ưu tuyến, WMS/TMS.
  - Tài chính: lương & bảo hiểm, tài sản cố định, dòng tiền, giá thành, mua hàng & phê duyệt, ERP, vay & lãi suất, giải trình biến động.
  - Marketing: email & automation, SEO, livestream, thương hiệu, sự kiện, PR & khủng hoảng, A/B test, ngân sách năm.
  - Y tế: nhi khoa, người cao tuổi, dinh dưỡng, phục hồi chức năng, phòng mổ, kiểm soát nhiễm khuẩn, chẩn đoán hình ảnh, xuất viện.
  - Xây dựng: khảo sát & đo đạc, đào đất & móng, hoàn thiện, hợp đồng & thanh toán, nhà thầu phụ, máy thi công, họp chủ đầu tư/TVGS, PCCC & sơ cứu.
  - Hàng không: mua/đổi/hoàn vé, phòng chờ thương gia, miễn thuế, hành khách gây rối, sân đỗ, cargo, thông báo trên loa, sơ cứu trên máy bay.
- **IT** thêm 8 chặng → **45 chặng · 450 ngày**: làm với khách Nhật & BrSE, spec & Q&A, ước lượng & báo giá outsource, QA thủ công, on-call & sự cố production, mobile, sản phẩm & UX, dùng AI & LLM.
- Mỗi ngành còn thêm: 16 câu dịch ngược, 5 bài đọc 30 giây, 4 tình huống Giao tiếp AI, 3 loại sự kiện sắp tới, 6 câu Mochi; mỗi vai +2 tình huống, +4 hội thoại.
- Tổng cộng thêm **880 từ, 440 hội thoại chặng + 160 hội thoại vai, 528 bài nghe, 50 bài đọc**. Viết bởi subagent theo `packs_src/README.md`, **kiểm duyệt chéo** (`docs/review/extra-*.md`).

**Kỹ thuật**
- `packs_src/extra/<id>.py` + `phases_extra2.py`: chỉ **nối vào cuối** — ngày/từ/hội thoại cũ giữ nguyên chỉ số, tiến độ người học không đổi (đã so sánh từng phần tử).
- build.py kiểm tra thêm: trùng từ vựng trong gói, trùng tên chặng, trùng key tình huống/sự kiện.
- `tests/k.mjs`: nạp cả 11 ngành, kiểm tra mọi tham chiếu ngày hợp lệ, mở các ngày mới.

## v4.0.0 — 23/09/2026 · Nói tốt hơn, cùng nhau, tài khoản & đồng bộ

> Các tính năng cần máy chủ (tài khoản, đồng bộ, AI miễn phí, nhắc học qua thông báo, lớp học, bảng tuần, bạn học) **chỉ bật khi điền `cloud-config.js`** (xem `docs/BACKEND.md`). Để trống thì phần còn lại vẫn chạy đầy đủ, chỉ lưu trên máy.

**Nội dung**
- 2 ngành mới: 🏗️ **Xây dựng · Kỹ thuật** (kỹ sư hiện trường, QA/QC, an toàn HSE, MEP) và ✈️ **Hàng không · Sân bay** (check-in, cửa ra máy bay, tiếp viên, hành lý) — mỗi ngành 4 vai, 120 ngày, kiểm duyệt chéo (`docs/review/construction.md`, `aviation.md`) → **11 ngành, 47 vai**.
- 🇯🇵 **Tiếng Nhật công sở**: 51 câu kính ngữ & câu cố định (7 nhóm: chào hỏi, xin phép, nhận việc, 報連相, xin lỗi – nhờ vả, họp & điện thoại, email) có furigana, romaji, giọng đọc Nhật, đọc theo có chấm, đố nhanh; thuật ngữ Nhật trong thẻ từ có furigana + nút nghe.
- 🎯 **Kiểm tra trình độ 3 phút** ở bước làm quen (nghe 3 câu + đọc to 2 câu) và hỏi "bạn thường học lúc nào?" để đặt giờ nhắc.

**Giữ thói quen & cùng nhau** (cần máy chủ, trừ cam kết 7 ngày)
- 🔔 **Nhắc học qua thông báo đẩy**: tối đa 1 lần/ngày, vào khoảng giờ bạn hay bắt đầu học (hoặc giờ cố định); vắng 1–4 ngày nhắc nhẹ, ngày 7 nhắc lần cuối rồi im; tổng kết tuần tối Chủ nhật. Chỉ xin quyền sau khi đã học; iPhone có hướng dẫn cài ra màn hình chính.
- 🤝 **Cam kết 7 ngày** (đặt 50 xu game, học đủ 7 ngày liền nhận 100).
- 👥 **Lớp học** (mã 8 ký tự, vào lớp cần đồng ý riêng, chủ lớp chỉ xem số tổng hợp + xuất CSV) · **Bảng tuần theo ngành** (tự nguyện, biệt danh, nhóm ~20 người, không rớt hạng) · **Bạn học** (link mời, chuỗi chung, nhắc nhau 1 lần/ngày).

**Tài khoản**
- Mở app là có **tài khoản khách tự động** — tiến độ lưu trên máy chủ ngay, không cần đăng nhập, không hỏi gì.
- **Lưu tiến độ bằng Google** (liên kết vào chính tài khoản khách, không mất gì); gợi ý sau 3 ngày học (iPhone: sau 1 ngày).
- Google đã có tài khoản → đăng nhập vào đó; cả máy lẫn tài khoản đều có tiến độ → chọn **Gộp cả hai** (mặc định) / dùng tài khoản / dùng máy này.
- Màn **Tài khoản & đồng bộ** (Tôi › thẻ đầu trang): trạng thái, đồng bộ ngay, lượt AI miễn phí còn lại, đăng xuất, **xoá tài khoản** (gõ XOA).
- Trang **Chính sách quyền riêng tư**, **Điều khoản**, **Xoá dữ liệu**.

**Đồng bộ & offline**
- Học như cũ khi mất mạng; thay đổi xếp hàng và tự gửi khi có mạng lại. Chấm nhỏ trên tab Tôi: nhấp nháy = đang gửi, xám = offline còn thay đổi chờ gửi, cam = cần xử lý (đã đồng bộ thì không hiện).
- Gửi từng thay đổi nhỏ (thẻ ôn, ngày học, câu lưu…) nên 2 máy cùng học vẫn gộp đúng: thẻ ôn giữ bản ôn nhiều hơn, ngày đã học hợp lại, streak lấy lớn hơn.
- Không đưa lên máy chủ: key AI riêng, nội dung đầy đủ các buổi chat, ảnh, ghi âm.

**AI & báo lỗi**
- Chưa có key AI riêng vẫn dùng được AI: **10 lượt/ngày** (khách) · **20 lượt/ngày** (Google), qua máy chủ.
- Báo lỗi ⚑ gửi thẳng cho người làm app (offline thì gửi sau).

**Nói tốt hơn** (đợt B, `docs/TINH-NANG-MOI-2026-09-23.md`)
- 🎯 **Từ mục tiêu trong Giao tiếp AI**: mỗi buổi chọn 3–5 từ/câu đang tới hạn ôn hoặc hay sai; AI khéo dẫn dắt để bạn dùng; dùng đúng → ✓ và tính 1 lần ôn SRS. Tắt/bật trong ⋯ Tùy chọn.
- **Chạm từ AI nói** → nghĩa, IPA, ví dụ (tra từ điển gói trước, không có mới hỏi AI, có cache) · lưu vào "Của tôi" · dịch cả câu.
- **Bí thì gõ tiếng Việt**: app gợi ý câu tiếng Anh để bạn tự nói/gõ lại (không tính là một lượt).
- 🎤 **Phỏng vấn · Họp nêu ý kiến · Thuyết trình 2 phút** cho mọi ngành, chấm thêm theo tiêu chí (vd có ví dụ cụ thể: tình huống → việc làm → kết quả).
- **Phát âm 3 mức**: 🟩 đúng · 🟨 gần đúng (hiện từ bạn nói) · 🟥 thiếu; chạm từ để nghe chậm + IPA — ở Nhại theo, Đọc câu, Báo cáo 60s, Ôn nhanh.
- 🎤 **Phân tích bài nói**: nói tối đa 2 phút (hoặc dán chữ) → số từ, tốc độ từ/phút, từ đệm (um, like, you know…), AI sửa lỗi + nói lại tự nhiên hơn, lưu câu sửa để ôn. Không lưu ghi âm.

**Giữ chuỗi**
- 🔥 Chúc mừng khi việc đầu tiên trong ngày nối chuỗi (mốc 3/7/14/30/100 ngày) · 🌟 đếm "ngày hoàn hảo" (đủ 4 việc).
- 🛡️ **Lá chắn cuối tuần**: nghỉ Thứ Bảy/Chủ nhật mà 7 ngày trước học ≥5 ngày → chuỗi giữ nguyên.
- 🔧 **Sửa chuỗi** (1 lần/tháng, trong 2 ngày sau khi đứt): làm đủ 4 việc hôm nay để tự nối lại, hoặc đổi 150 xu game.

**Máy chủ** — Supabase (Singapore): 3 migration có RLS, RPC `apply_changes` gộp theo thao tác + chống gửi trùng, thống kê học (ngày học, việc/ngày, đúng/sai), hạn mức AI, dọn khách bỏ quá 30 ngày; Edge Functions `ai`, `delete-account`; sao lưu hằng tuần + keepalive bằng GitHub Actions.

---

## v3.1.1 — 20/09/2026 · Trang giới thiệu gọn cho điện thoại

- Trên màn ≤780px, các khối tính năng, lưới ảnh, lưới ngành, thẻ kỹ thuật thành **dải vuốt ngang** có chấm chỉ vị trí → trang ngắn từ ~29.600px còn ~12.000px (≈ 16 màn thay vì 40).
- Hero: chữ lên trước, ảnh điện thoại nhỏ lại; khoảng cách các mục gọn hơn; chữ nhỏ nhất ≥12px.
- Sửa tràn ngang: menu chọn phiên bản (màn 400–560px), thanh điều hướng ở 360px, quầng sáng hero; áp dụng cả cho trang lưu trữ v1, v2.

---

## v3.1.0 — 20/09/2026 · 9 ngành, kiểm duyệt nội dung, rảnh tay, ảnh → bài học, gói nghề riêng

**Nội dung**
- Thêm 4 ngành: 🚚 **Logistics · XNK**, 💰 **Tài chính · Kế toán**, 📣 **Marketing · TMĐT**, 🩺 **Y tế · Điều dưỡng** (mỗi ngành 4 vai, 120 ngày) → **9 ngành, 39 vai**.
- **Kiểm duyệt chéo toàn bộ 8 gói** bằng một AI biên tập độc lập: ~205 chỗ sửa (IPA, câu chưa tự nhiên, nghĩa tiếng Việt, thuật ngữ Nhật, đáp án "sai" thực ra đúng, an toàn dị ứng/y tế, thông tin thuế – hải quan quá cụ thể). Nhật ký sửa: `docs/review/*.md`.
- Nút **⚑ Báo lỗi nội dung** trên thẻ từ, câu, hội thoại, bài nghe, dịch ngược, rảnh tay; báo lỗi lưu trên máy (Tôi › Báo lỗi nội dung) và gửi được thành GitHub issue hoặc chép gửi tay.

**Tính năng**
- 🎧 **Luyện nói rảnh tay**: app đọc → tự bật mic → chấm → sang câu sau; 3 chế độ *Nghe & nhắc lại*, *Hỏi – đáp*, *Việt → Anh*; giữ màn hình sáng; câu dưới 60% vào hàng ôn.
- ✏️ **Nghề của tôi**: tả công việc → AI viết gói riêng 3 chặng (30 từ, 15 hội thoại, 12 bài nghe, 4 tình huống AI, câu dịch ngược), lưu trên máy, thành ngành riêng (ghép trước lộ trình Công sở chung); game cũng dùng được.
- 📷 **Ảnh → bài học**: chụp email, menu, phiếu QC… AI đọc ảnh → tóm tắt, từ vựng (thêm vào "Của tôi"), câu trả lời mẫu, 2 câu hỏi hiểu bài, tình huống luyện nói. Cần AI đọc được ảnh (Claude trong claude.ai, Gemini, Claude API).
- Game: đổi ngành ngay trong Hồ sơ (dùng cho bản game chạy riêng trên claude.ai).

---

## v3.0.0 — 20/09/2026 · Đổi tên thành **Nói Nghề**, đa ngành, cá nhân hoá

**Đa ngành** — mỗi ngành có lộ trình 12 chặng · 120 ngày, từ vựng (IPA, nhiều từ có tiếng Nhật), câu mẫu, hội thoại chọn đáp, bài nghe (có đoạn 2–3 câu), tình huống AI, vai trò, bài đọc hiểu, dịch ngược, sự kiện:
- 🏢 **Công sở chung** (mặc định khi không chọn ngành): 4 vai (Nhân viên văn phòng, Hành chính – Nhân sự, Trưởng nhóm, Sinh viên – ứng viên).
- 💻 **IT · Phần mềm**: giữ nguyên toàn bộ nội dung v2.0 (370 ngày, 7 vai) — người dùng cũ tự vào gói này, không mất tiến độ.
- 🏨 **Khách sạn · Du lịch**, 🎧 **Bán hàng · CSKH**, 🏭 **Sản xuất · Nhà máy**: mỗi gói 4 vai; 3 chặng lõi (Email, Nghỉ phép & hành chính, Phỏng vấn) dùng chung từ gói Công sở.
- Mỗi gói còn có ~610 câu công sở chung trong "Câu thường dùng".

**Cá nhân hoá**
- Làm quen 3 bước khi mở app lần đầu: ngành → vị trí → trình độ; **bước nào cũng bỏ qua được**, bỏ qua = gói Công sở chung. Sau 3 ngày học mới hỏi nhẹ "Bạn làm ngành gì?".
- Chip ngành dưới tên app để đổi ngành bất cứ lúc nào; **tiến độ lộ trình giữ riêng từng ngành**, từ vựng SRS · câu đã lưu · streak dùng chung. Link `?track=hotel` mở sẵn một ngành.
- "Báo cáo 60 giây" theo nghề: Standup (IT), Báo cáo nhanh (công sở), Giao ca (khách sạn), Báo cáo sale, Báo cáo ca (nhà máy).
- Cá nhân hoá bằng mô tả công việc cho **mọi ngành**: AI chọn ngành + vai, gợi ý chuyển gói hợp hơn, tạo 3 tình huống và **12 từ vựng riêng của nghề** (thêm vào "Của tôi" một chạm). Chọn "Ngành khác" ở màn làm quen sẽ vào thẳng bước này.
- Mọi lời nhắc AI dùng đúng nghề của bạn (không còn cố định "software developer").

**Khác**: game *Nói Nghề Quest* theo ngành (quái, câu Mochi nói, Boss AI); trang giới thiệu v3.0 với 34 ảnh mới, bản v2.0 lưu trữ ở `gioi-thieu-v2.html`; service worker cache sẵn cả 4 gói mới.

---

## v2.0.0 — 20/09/2026 · Nội dung ×2, theo vai, trang giới thiệu mới

**Nội dung**
- Hội thoại chọn đáp: 74 → **185 bài** (mỗi chặng thêm 3 tình huống công sở mới) — mỗi bài chỉ lặp tối đa 2 lần trong 370 ngày (trước ~5 lần).
- Sửa lỗi dữ liệu: đáp án đúng của 74 bài cũ **luôn nằm ở vị trí đầu** → nay được xáo vị trí khi sinh dữ liệu.
- Bài nghe: 148 → **222 bài**, trong đó **74 đoạn họp dài 2–3 câu** (standup, review, sprint planning, incident…).
  App hiện đoạn với nhiều ô điền cùng lúc, chấm từng từ; shadowing đoạn dài cho ghi âm tới 25 giây; game dùng đoạn họp cho câu hỏi nghe.
- Luyện theo vai: thêm **Designer 🎨** (bàn giao thiết kế, góp ý UI, nghiên cứu người dùng, design system) và **Data 📊** (nhận yêu cầu số liệu, giải thích dashboard, chất lượng dữ liệu, mô hình) → **7 vai**. Cá nhân hoá theo JD nhận diện được 2 vai mới.

**Trang giới thiệu v2.0**
- Chụp lại toàn bộ 25 ảnh màn hình (bản v1.22+).
- Mục mới: *Mới trong v2.0* — Standup 60 giây · Dịch ngược · Luyện theo vai + JD · Thuật ngữ tiếng Nhật · Đoạn họp dài.
- Mục **Lịch sử phiên bản**; trang cũ lưu trữ ở `gioi-thieu-v1.html`.

---

## v1.x — 09/2026

- **v1.22.0** — Nâng cấp UI/UX: bỏ nút AI nổi, Luyện 4 nhóm ô gọn, Lộ trình lưới 37 chặng, danh sách từ tải dần, chip tình huống lên đầu màn Giao tiếp, thanh ghim nền đặc, báo offline, khung chờ AI, rung phản hồi, vùng chạm 44px, bàn phím không che ô nhập.
- **v1.21.1** — Cập nhật tại chỗ mượt: không chạy lại hiệu ứng, không nhảy lên đầu trang khi bấm trong cùng màn.
- **v1.21.0 (Đợt C)** — Thuật ngữ tiếng Nhật, SRS cho câu, chọn đáp theo vai + cá nhân hoá JD, sự kiện, podcast, hỏi nhanh (nút ?), AI phân tích phát âm, ảnh chia sẻ PNG, cache AI + luật ngữ pháp offline, test tự động, CSP.
- **v1.20.0 (Đợt B)** — Standup 60 giây, Dịch ngược, biểu đồ tiến bộ, game ưu tiên từ hay sai + log đấu thoại, trang giới thiệu 1,6 MB → 44 KB.
- **v1.19.0 (Đợt A)** — Chống chèn HTML, sao lưu/khôi phục dữ liệu, script tự copy dữ liệu sang game, meta/OG.
- **v1.18.x** — Game *IT English Quest* (bản đồ ngày, quiz battle, boss, AFK Mochi, Shop, tab Nói 5 chế độ); màn "chào mừng trở lại".
- **v1.17.x** — "Nghe hết" hội thoại có xướng vai, video demo Giao tiếp AI, favicon, trang giới thiệu v1.
- **v1.0 – v1.16** — Lộ trình 370 ngày, từ vựng SRS, 1000 câu, nghe/shadowing, Giao tiếp AI (Gemini/Claude/Groq), PWA offline.
