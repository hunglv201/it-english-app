# Rà soát nội dung gói `legal` (2026-09-23)

Gói mới nên soát cả 2 file: `packs_src/legal.py` (gói gốc, 10 chặng) và `packs_src/extra/legal.py` (EXTRA, 8 chặng).
Đã đọc hết từng dòng, khoảng 700 mục: 394 mục ở file gốc, 306 mục ở EXTRA. Trong đó có 119 từ có tiếng Nhật.
Cấu trúc, số lượng và key giữ nguyên. `python3 packs_src/build.py education legal` chạy qua (20 chặng · 200 ngày).

**Kiểm tra khẳng định pháp lý:** đã rà từng câu tìm số điều luật, mức phí, mức phạt, thời hạn luật định và thời gian xử lý hồ sơ. Gói không nêu điều luật, nghị định hay lệ phí nào của Nhà nước. Các chỗ về thời hạn đều nói chung chung: "current regulations", "the date on your receipt", "I'll check the exact rule". Còn các con số như "Clause 9", "30 days' notice", "10 working days from the letter", "within 3 days" đều thuộc hợp đồng, công văn hay chính sách nội bộ tự đặt trong tình huống, không phải quy định của luật.
Có 3 chỗ ngầm khẳng định sai hoặc rủi ro, đã sửa cho chung chung hơn (xem 3 dòng đầu bảng dưới).
Các nguyên tắc chung khác vẫn giữ vì đúng ở mức khái quát: giấy tờ nước ngoài "usually" cần hợp pháp hoá lãnh sự, chứng thực bản sao phải đối chiếu bản gốc, thẻ tạm trú "usually" không dài hơn giấy phép lao động, nhãn hiệu bảo hộ theo từng nước, người nước ngoài cần quyết toán thuế trước khi rời Việt Nam ("probably"), công ty có thể đăng ký mã số thuế thay nhân viên ("in most cases").

## Số chỗ sửa theo loại

| Loại | gốc | extra |
|---|---|---|
| Khẳng định pháp lý / thực tế nghề | 3 | 1 |
| Tiếng Anh (độ tự nhiên) | 4 | 0 |
| Tiếng Nhật | 1 | 1 |
| **Tổng** | **8** | **2** |

## Các thay đổi

| File · mục | Trước | Sau | Lý do |
|---|---|---|---|
| gốc · hội thoại hạn gia hạn GPLĐ (chặng 9) | "We should submit it some weeks before it expires." | "It must be submitted within a set period before it expires." (+ nhận xét VN) | Luật quy định một khoảng thời gian được nộp trước khi hết hạn (có mốc sớm nhất và muộn nhất). "Vài tuần trước" có thể sai. Câu mới nói chung chung và đúng |
| gốc · câu mẫu GPLĐ (chặng 3) | "Your permit expires in three months, so let's renew it." | "…so let's prepare the renewal." (VN: "chuẩn bị hồ sơ gia hạn") | Còn 3 tháng thường chưa nộp gia hạn được. Chỉ nên nói chuẩn bị hồ sơ |
| gốc · hội thoại luật sư nước ngoài (chặng 8) | "the investment approval" | "the investment registration" | Nhà đầu tư nước ngoài làm thủ tục *đăng ký* đầu tư (IRC), không phải "phê duyệt" chung chung |
| extra · bài nghe sửa hoá đơn | "We will cancel it and issue a new one." (ô trống "cancel") | "We will issue a replacement invoice." (ô trống "replacement") | Hoá đơn điện tử sai tên thì xử lý bằng điều chỉnh hoặc thay thế, không tự huỷ. Nay khớp với hội thoại "corrected e-invoice" |
| gốc · criminal record check (ví dụ) | "Ask your home country for a criminal record check early." | "Apply for a criminal record check in your home country early." | "ask your home country for" không tự nhiên |
| gốc · bài nghe lý lịch tư pháp | "Please ask your home country for it now." | "Please apply for it in your home country now." | Như trên. Ô trống "country" vẫn giữ |
| gốc · working day (ví dụ) | "The result comes in five working days" | "The result will be ready in five working days" | Tự nhiên hơn, khớp với câu dịch ngược |
| gốc · câu mẫu hợp đồng song ngữ | "Which version wins if the two languages are different?" | "Which language prevails if the two versions are different?" | "wins" là khẩu ngữ. "prevails" là từ chuẩn và đã dùng ở hội thoại, bài nghe cùng chặng |
| gốc · compensation (tiếng Nhật) | 補償 (hoshō) | 損害賠償 (songai baishō) | Bồi thường thiệt hại hàng hỏng trong hợp đồng thì dùng 損害賠償. 補償 là đền bù (thường cho tổn thất không do lỗi) |
| extra · consecutive (tiếng Nhật) | 逐次 (chikuji) | 逐次通訳 (chikuji tsūyaku) | 逐次 đứng một mình chỉ là "lần lượt". Thuật ngữ phiên dịch là 逐次通訳 |

## Tiếng Nhật đã bỏ
Không bỏ từ nào. Có 2 từ đã được thay bằng từ đúng hơn (xem bảng). Còn lại 117 từ đều là thuật ngữ công ty, văn phòng luật Nhật dùng thật, và romaji khớp Hepburn có ā/ō/ū. Ví dụ: 定款, 委任状, 準拠法, 違約金, 秘密保持契約, 就業規則, 源泉徴収, 利益相反, 内部通報, ビザ, パスポート.

## Đã kiểm tra, không cần sửa
- 10 bài đọc: đáp án `a` đều đúng. Số liệu khớp nhau: 7/8 giấy tờ; 700 triệu = 70% yêu cầu; 3 đợt trả; hạn 10/6 trước khi giữ hộ chiếu 12–25/6.
- Hội thoại: đáp án đúng luôn là "không khẳng định vội, kiểm tra quy định hiện hành hoặc hỏi luật sư". Đáp án sai là hứa bừa, đoán, che giấu, hối lộ hoặc cộc lốc. Nhận xét tiếng Việt đúng lỗi.
- Đạo đức nghề: phiên dịch giữ trung lập và không lược bỏ nội dung, không hứa thắng kiện, kiểm tra xung đột lợi ích trước khi báo phí, bảo vệ người tố giác, từ chối "tiền cà phê".
- Tên công ty và người đều tự đặt (Blue River Trading, Green Valley Foods, Sunrise Packaging…), không có thương hiệu thật.

## Còn đáng lo
- Pháp luật Việt Nam về giấy phép lao động, dữ liệu cá nhân và hoá đơn điện tử thay đổi nhanh. Nội dung hiện đã chung chung. Nếu sau này có người viết thêm mốc cụ thể (số ngày, mức phạt 8%…), cần người trong nghề duyệt lại.
- "Working days are usually Monday to Friday": một số bộ phận một cửa làm cả sáng thứ Bảy. Câu đã có "usually" nên giữ.
