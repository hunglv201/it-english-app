# Lịch sử phiên bản — Nói Nghề (trước đây IT English)

Ghi theo thứ tự mới → cũ. **Version lớn** (x.0.0) đi kèm một trang giới thiệu riêng; trang của version lớn cũ được giữ lại
làm bản lưu trữ (`gioi-thieu-v<N>.html`) để xem lại app từng trông thế nào.

| Version lớn | Trang giới thiệu | Ảnh chụp |
|---|---|---|
| **v3.0** (hiện tại) | [`gioi-thieu.html`](https://hunglv201.github.io/it-english-app/gioi-thieu.html) | `img/showcase/v3/` |
| v2.0 | [`gioi-thieu-v2.html`](https://hunglv201.github.io/it-english-app/gioi-thieu-v2.html) (lưu trữ) | `img/showcase/v2/` |
| v1.x | [`gioi-thieu-v1.html`](https://hunglv201.github.io/it-english-app/gioi-thieu-v1.html) (lưu trữ 13/09/2026) | `img/showcase/` |

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
