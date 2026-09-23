# Việc để sau (backlog)

> 23/09/2026: nghiên cứu mới + lộ trình đợt A–D (giữ chân, nói tốt hơn, lớp học, nội dung) — xem [`TINH-NANG-MOI-2026-09-23.md`](TINH-NANG-MOI-2026-09-23.md).

Ghi lại các ý tưởng đã bàn nhưng **chưa làm** (cập nhật 20/09/2026, sau v3.1.0). Thứ tự ≈ độ ưu tiên đề xuất.

| # | Việc | Ước lượng | Ghi chú |
|---|---|---|---|
| 1 | **Kiểm tra trình độ đầu vào 3 phút** — nghe 3 câu + nói 2 câu, AI chấm và xếp đúng ngày bắt đầu (thay cho tự chọn Mới/Cơ bản/Khá ở bước 3 làm quen) | 0,5 phiên | Dùng `micLong` + `wordMatch` cho nghe/nói; AI chấm tổng. Bỏ qua được như các bước khác |
| 2 | **Tiếng Nhật công sở làm ngôn ngữ học chính** (không chỉ nghĩa phụ) — lộ trình, hội thoại, TTS `ja-JP`, nhận giọng `ja-JP` | 2–3 phiên | Người Việt làm cho công ty Nhật rất đông; cần schema gói có `lang` đích, đổi `lNorm`/`wordMatch` cho tiếng Nhật (tách theo ký tự) |
| 2b | **Backend Supabase (server-first, offline, khách + đăng nhập Google, AI qua server)** — kế hoạch chi tiết: [`BACKEND-PLAN.md`](BACKEND-PLAN.md) | ≈ 15 ngày công (≈ 7 phiên), chia v4.0 + v4.1 | FE vẫn trên GitHub Pages |
| 3 | **Lớp học / nhóm doanh nghiệp** — mã lớp, cả nhóm cùng ngành, bảng xếp hạng streak | 1–2 phiên | Không cần server nếu chạy bản claude.ai (capability `db`/`room`); bản Pages cần backend nhẹ |
| 4 | Ngành tiếp theo: Xây dựng · Kỹ thuật, Giáo dục, Luật · Hành chính công, Hàng không | 0,5–1 phiên/gói | Quy trình sẵn: `packs_src/README.md` → agent viết → agent kiểm duyệt → build |
| 5 | Nhờ **người làm thật trong từng ngành** đọc duyệt 1–2 chặng mỗi gói; gom báo lỗi từ GitHub issues (nhãn `content`) để sửa theo đợt | liên tục | Nút ⚑ đã có từ v3.1 |
| 6 | Rảnh tay: lệnh giọng nói ("next", "again", "stop"), chạy nền khi khoá màn hình (iOS dừng SpeechSynthesis) — cân nhắc audio ghi sẵn | 1 phiên | |
| 7 | Ảnh → bài học: lưu bài học từ ảnh thành "bộ" để ôn lại; OCR offline (Tesseract.js) khi không có AI đọc ảnh | 0,5–1 phiên | |
| 8 | Còn từ trước: G3 thêm boss/kết cục game; E7 đọc ký hiệu kỹ thuật; K4/E16 backend giữ key + đồng bộ đa thiết bị | — | Xem `docs/REVIEW-2026-09-20.md` |
