# Rà soát nội dung gói `education` (2026-09-23)

Gói mới nên soát cả 2 file: `packs_src/education.py` (gói gốc, 10 chặng) và `packs_src/extra/education.py` (EXTRA, 8 chặng).
Đã đọc hết từng dòng, khoảng 700 mục: 395 mục ở file gốc, 306 mục ở EXTRA. Soát từ vựng, IPA, nghĩa, câu mẫu, hội thoại, bài nghe, vai, prompt AI, dịch ngược, bài đọc, sự kiện, quips và báo cáo 60 giây.
Cấu trúc, số lượng và key giữ nguyên. `python3 packs_src/build.py education legal` chạy qua (20 chặng · 200 ngày).

Nhìn chung gói đã tốt. IPA chuẩn Anh-Anh, có dấu nhấn. Mỗi hội thoại có đúng một đáp án đúng, 2 đáp án sai đều sai rõ (sai ngữ pháp, gắn nhãn học sinh, hứa bừa, sai nguyên tắc an toàn). Không có tên thương hiệu thật.
Phần bảo vệ học sinh đúng thực tế: không giao trẻ cho người không có trong danh sách đón, không hứa giữ bí mật, báo cho người phụ trách bảo vệ học sinh, giáo viên không tự chẩn đoán chứng khó đọc. Có nhắc thuốc dị ứng để ở phòng y tế nhưng không có liều thuốc. Gói không có từ tiếng Nhật nào (tuple 6 phần tử), nên không có gì để bỏ.

## Số chỗ sửa theo loại

| Loại | gốc | extra |
|---|---|---|
| Tiếng Anh (ngữ pháp, độ tự nhiên) | 5 | 3 |
| Tiếng Việt | 1 | 1 |
| **Tổng** | **6** | **4** |

## Các thay đổi

| File · mục | Trước | Sau | Lý do |
|---|---|---|---|
| gốc · grade (ví dụ) | "She got a <b>grade</b> A for her project." | "She got a good <b>grade</b> for her project." (VN: "được điểm cao") | Người bản xứ không nói "a grade A" mà nói "an A" |
| gốc · bài nghe chặng 2 | "This week we are one week behind." | "We are one week behind the plan." | Lặp "week" và vô nghĩa ("tuần này chậm một tuần") |
| gốc · câu mẫu chấm chéo (VN) | "Mình chấm chéo kiểm tra cho nhau được không?" | "Mình kiểm tra chéo phần chấm bài của nhau được không?" | Câu cũ lủng củng |
| gốc · câu mẫu hẹn lịch | "book another appointment next month" | "book another appointment for next month" | Thiếu giới từ |
| gốc · hội thoại nhận xét cuối kỳ | "I've finished 20 of 25." | "I've finished 20 out of 25." | Tự nhiên hơn khi nói |
| gốc · dịch ngược | "You need more practice with writing." | "You need more writing practice." | Cách nói tự nhiên hơn |
| extra · recommendation letter (ví dụ) | "Two teachers will write a recommendation letter for you." | "Your class teacher will write a recommendation letter for you." (VN khớp lại) | Hai người mà viết "a letter" (một thư) là không khớp số |
| extra · hội thoại câu lạc bộ | "Really well. 18 students joined…" | "Really well. Eighteen students joined…" | Không bắt đầu câu bằng chữ số |
| extra · silence (ví dụ) | "Please keep <b>silence</b> until everyone has left the room." | "Please work in <b>silence</b> until the end of the exam." (VN khớp lại) | "keep silence" không tự nhiên. Người bản xứ nói "work in silence" |
| extra · câu mẫu coi thi (VN) | "Để điện thoại và cặp ở phía trên nhé." | "…ở đầu phòng nhé." | "phía trên" dễ hiểu thành "trên bàn". Ý đúng là "at the front" |

## Tiếng Nhật đã bỏ
Không có (gói không dùng tiếng Nhật).

## Đã kiểm tra, không cần sửa
- 10 bài đọc (5 gốc + 5 extra): đáp án `a` đều đúng theo văn bản. Số liệu khớp nhau: giáo án 5 + 25 + 10 phút, ưu đãi anh chị em 10%, cộng thêm 25% thời gian, 16/10 là thứ Sáu.
- Bài nghe: ô trống đều là từ nội dung có trong câu. Mỗi đoạn có 2–3 câu và đúng 3 ô trống.
- Chuyên môn: dạy thêm học sinh lớp mình được đánh dấu là xung đột lợi ích. Thiếu giấy đồng ý thì không cho đi dã ngoại. Đếm thiếu sĩ số thì phải dừng lại. Trợ giảng đọc đề giúp nhưng không làm hộ. Có giám thị đi cùng khi thí sinh ra ngoài.

## Còn đáng lo
- Học phí ví dụ "about 250 million dong a year" và các giờ, ngày trong bài chỉ là số minh hoạ của một trường tự đặt. Nên giữ như vậy, không biến thành "mức chuẩn".
- Gói dùng từ và cách viết Anh-Anh (Year 3, plenary, invigilator, register), nhưng chỗ khác lại dùng "Grade 3". Hai cách này đều đúng ở trường quốc tế tại Việt Nam, nên không sửa.
