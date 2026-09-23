# Rà soát nội dung `mail/templates.js` (2026-09-23)

Người soát là biên tập viên độc lập, không phải người viết. Đã soát **55/55 mẫu** (16 mẫu chung + 13 ngành × 3). Mỗi mẫu gồm subject, body và mọi bản tone (polite/short). Tổng cộng khoảng 125 đoạn văn.
Cách soát: điền ví dụ `ph` của từng field, lấy `{me}` = "Lan", in ra toàn bộ rồi đọc từng đoạn.
Cấu trúc, `id`, các `fields.k` và thứ tự giữ nguyên.

**Kiểm tra máy** (node, `new Function('window', src)(w)`):
- Có 55 mẫu, `id` không trùng.
- Mọi `{k}` trong subject/body/tone đều có trong `fields` hoặc là `{me}`.
- Mọi field đều được dùng trong `body`.

**Nội dung:** mẫu y tế chỉ có thông tin hành chính. "Làm theo chỉ định bác sĩ" nằm ở field do người dùng điền, còn câu "seek medical care right away" là lời khuyên an toàn chung. Mẫu luật chỉ nói về thủ tục, không tư vấn pháp lý. Label và vi đều là tiếng Việt có dấu.

## Danh sách sửa (14)

| Mẫu | Trước → Sau | Lý do |
|---|---|---|
| meeting_confirm body | "Thank you for your time. I'm happy to confirm…" → "I'm writing to confirm our meeting:" | Buổi họp chưa diễn ra nên cảm ơn "your time" là không hợp |
| meeting_confirm short | "…on {time} at {place}." → "…{topic}: {time}, {place}." | Khi điền vào ra "on Tuesday, May 14, 10:00 AM at Meeting Room 2". Nếu place là link thì câu còn vỡ hơn |
| office_interview_invite short | "…position on {time} at {place}." → "…position. Time: {time}. Place: {place}." | Khi điền vào ra "at 5th floor, 12 Le Loi Street", sai giới từ |
| thanks_meeting short | "Next step: {next}." → "As agreed, the next step is {next}." | ph là "to finalize…", nên dạng nhãn "Next step: to finalize" bị gượng |
| intro_team body + field before | "I worked {before}" (ph "as a tester…") → "I worked as {before}" (ph "a tester…", label "(công việc, nơi làm)") | Người dùng A2 dễ gõ thiếu "as" thành "I worked tester". Đưa "as" vào câu mẫu thì an toàn hơn |
| apology · label fix | "Đã khắc phục thế nào" → "… (dạng đã làm: sent…, fixed…)" | Câu mẫu là "I have already {fix}", nên người dùng cần gõ phân từ quá khứ |
| hotel_complaint_reply · label action | "Đã xử lý thế nào" → "… (dạng đã làm: shared…, fixed…)" | Câu mẫu là "We have {action}", lý do như trên |
| sales_quote body | "Thank you for your interest in 500 office chairs." → "Thank you for your request. Please find attached our quotation for {product}." | Khi field là số lượng + hàng thì "interest in 500 office chairs" không tự nhiên |
| fin_payment_reminder body | "…please send us the payment details, and kindly ignore this reminder." → "…please ignore this reminder, or send us the payment details so we can check." | Thứ tự ý cũ bị ngược (vừa bảo gửi vừa bảo bỏ qua) |
| con_inspection_request short | "{work} at {location}" → "{work} ({location})" | Khi điền vào ra "at Block B, grid lines 1–4", giới từ không hợp mọi vị trí |
| legal_translation_order short | "Document: {doc} ({lang})." → "Document: {doc}, {lang}." | ph doc đã có ngoặc "(2 pages)", nên cũ ra hai cặp ngoặc liền nhau |
| it_release_note · ph new | "export to Excel on the report page" → "CSV export on the report page" | Bỏ tên thương hiệu thật |
| mkt_content_approval · ph channel | "our Facebook page" → "our fan page" | Bỏ tên thương hiệu thật |
| edu_admissions_followup · ph program | "our IELTS preparation course" → "our English exam preparation course" | Bỏ tên thương hiệu thật (IELTS là nhãn hiệu) |

## Điều còn lo (không sửa)

- **sick**: câu "come to work {date}" chỉ đúng khi người dùng gõ "today"/"tomorrow". Nếu gõ "May 10" sẽ thiếu "on". ph "today (May 10)" đã gợi ý cách gõ, và mẫu vốn dành cho "hôm nay", nên giữ.
- Dạng của field chưa thống nhất: `reason` ở late là cụm danh từ ("because of {reason}"), còn ở deadline_delay/extension là mệnh đề ("because {reason}"). ph đã cho đúng dạng, nhưng người dùng vẫn có thể gõ nhầm. Có thể thêm gợi ý vào label nếu muốn.
- Một số field cần người dùng gõ cụm động từ ("Could you {ask}?", "will {solution}", "help you {benefit}"). ph đã đúng dạng, nhưng label chưa nói rõ.
- mkt_collab_invite: "the marketing team for {product}" chấp nhận được. Nếu người dùng điền tên thương hiệu thì câu còn tự nhiên hơn.
- Tên đường thật (Le Loi, Tran Phu) chỉ là địa chỉ ví dụ, không phải thương hiệu, nên giữ.
