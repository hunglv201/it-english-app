# Rà soát nội dung gói `office` và `hotel` (2026-09-20)

Đã đọc hết từng dòng của `packs_src/office.py` và `packs_src/hotel.py`: từ vựng, IPA, từ loại, nghĩa tiếng Việt, thuật ngữ tiếng Nhật, câu mẫu, hội thoại, bài nghe, vai, prompt AI, câu dịch ngược, bài đọc, sự kiện và câu mẫu báo cáo.
Cấu trúc và số lượng mục giữ nguyên. `python3 packs_src/build.py office hotel` chạy qua.

Nhìn chung cả hai gói đã tốt: không thấy lỗi dấu tiếng Việt, đáp án bài đọc đều đúng, bài nghe có đủ ô trống. Phần sửa chủ yếu là câu chưa tự nhiên, thuật ngữ tiếng Nhật, dấu nhấn IPA và các chi tiết về an toàn khi khách bị dị ứng.

## Số chỗ sửa theo loại

| Loại | office | hotel |
|---|---|---|
| Tiếng Anh (ngữ pháp, độ tự nhiên) | 4 | 6 |
| IPA | 0 | 3 |
| Từ loại | 1 | 0 |
| Tiếng Việt (nghĩa, nhận xét) | 4 | 1 |
| Tiếng Nhật | 2 | 2 |
| Thực tế nghề, an toàn (dị ứng) | 0 | 7 |
| Hội thoại (đáp án sai chưa đủ sai) | 0 | 1 |
| Bài đọc | 0 | 2 |
| **Tổng** | **11** | **22** |

## Các thay đổi chính

| Gói | Mục | Trước | Sau | Lý do |
|---|---|---|---|---|
| hotel | Hội thoại dị ứng (chặng 7) | "It has peanuts, but I'll ask the chef to make it without them." | "The salad has peanuts, so let me check with the chef and find a safe dish for you." | Chỉ bỏ đậu phộng ra khỏi món chưa chắc an toàn (còn nguy cơ lây nhiễm chéo), nên đáp án mẫu phải là hỏi bếp và chọn món an toàn |
| hotel | Bài đọc thực đơn | "green papaya salad" (không ghi chú), lựa chọn "Fresh fruit" | "green papaya salad (no peanuts)", lựa chọn "Green papaya salad / Neither of them" | Gỏi đu đủ ở Việt Nam thường có đậu phộng, nên thực đơn phải ghi rõ. "Fresh fruit" là món tráng miệng, không phải món khai vị |
| hotel | Bài nghe báo dị ứng hải sản | "don't use fish sauce in her soup" | "don't use any seafood or fish sauce in her soup" | Khách dị ứng hải sản thì phải bỏ hết hải sản, không chỉ bỏ nước mắm |
| hotel | gluten-free | "Rice noodles are gluten-free." | "Our rice noodles are gluten-free, but let me check the sauce." | Bánh phở không có gluten nhưng nước sốt (xì dầu…) có thể có, nên phải kiểm tra |
| hotel | adjoining rooms | adjoining rooms = "phòng thông nhau" | **connecting rooms** /kəˌnektɪŋ ˈruːmz/ | Trong nghề khách sạn, *adjoining* là hai phòng sát nhau (có thể không có cửa nối). Phòng thông nhau có cửa nối là *connecting* (khớp với コネクティングルーム) |
| hotel | Bài nghe buồng phòng | "Room 305 has a Do Not Disturb sign. Please clean it after two o'clock." | "… Please go back after two o'clock." | Khách treo biển DND thì không được hẹn giờ dọn, chỉ quay lại kiểm tra sau |
| hotel | Tỷ giá (từ vựng và hội thoại) | 25,400 dong to the dollar | 26,300 | Cập nhật theo tỷ giá thực tế năm 2025–2026 |
| hotel | IPA twin room / double room / main course | /ˈtwɪn ruːm/, /ˈdʌbl ruːm/, /ˈmeɪn kɔːs/ | /ˌtwɪn ˈruːm/, /ˌdʌbl ˈruːm/, /ˌmeɪn ˈkɔːs/ | Theo Cambridge/Oxford, nhấn chính rơi vào từ thứ hai |
| hotel | Bài nghe giao phòng | "Here is your key card and the Wi-Fi password." | "Here is your key card, and the Wi-Fi password is on the holder." | Chủ ngữ số nhiều đi với "Here is" không chuẩn. Câu mới cũng khớp với câu mẫu "mật khẩu ghi trên bìa thẻ" |
| hotel | Câu mẫu đặt phòng | "Which dates would you like to stay?" | "Which dates would you like to book?" | "stay" cần giới từ ("stay on which dates"), còn "book" dùng được ngay |
| hotel | Bài nghe khai vị | "Would you like a starter or a salad" | "Would you like a starter before your main course" | Salad thường chính là món khai vị, nên câu cũ phi lý |
| hotel | takeaway | "We can pack the rest as a takeaway." | "Would you like a takeaway box for the rest?" | Câu cũ không tự nhiên. Người phục vụ thường nói "takeaway box" |
| hotel | Hội thoại khách chưa gọi món | "Just wave when you're ready." | "Just let me know when you're ready." | Bảo khách "vẫy tay" là thiếu lịch sự trong nhà hàng khách sạn |
| hotel | Vai lễ tân, gửi hành lý | "Here's your ticket." | "Here's your luggage tag." | Dùng đúng thuật ngữ "phiếu gửi hành lý" |
| hotel | Vai F&B, đáp án sai | "Yes, room number?" | "Yes. What your room?" | Câu cũ vẫn chấp nhận được trong giao tiếp. Câu mới sai hẳn về ngữ pháp, và nhận xét đã được viết lại cho khớp |
| hotel | Tiếng Nhật bill | お会計 (okaikei) | 請求書 (seikyūsho) | お会計 là từ ở nhà hàng. Hoá đơn khi trả phòng khách sạn là 請求書 |
| hotel | Tiếng Nhật itinerary | 旅程 (ryotei) | 行程表 (kōteihyō) | Công ty du lịch Nhật gọi lịch trình tour là 行程表 |
| hotel | Tiếng Việt starter | "Chả giò bên em được khách rất thích." | "Món chả giò được khách rất thích." | Câu cũ lẫn cách xưng "em" trong khi cả gói xưng "tôi" với "anh/chị" |
| office | welcome (từ loại) | v/n | excl/v | Câu ví dụ "Welcome to the team!" dùng như thán từ |
| office | Tiếng Nhật position | 役職 (yakushoku) | ポジション (pojishon) | 役職 là chức danh quản lý (課長, 部長…). Hỏi "làm vị trí gì" thì dùng ポジション |
| office | Tiếng Nhật priority | 優先順位 (yūsen jun'i) | 優先事項 (yūsen jikō) | Ví dụ là "top priority" (một việc ưu tiên), không phải thứ tự ưu tiên |
| office | progress (ví dụ) | "Let me share my progress this week." | "Here's my progress for this week." | Câu mới tự nhiên hơn |
| office | on track (tiếng Việt, 2 chỗ) | "sẽ xong trước thứ Sáu" | "kịp xong vào thứ Sáu" | "by Friday" nghĩa là muộn nhất thứ Sáu, không phải trước thứ Sáu |
| office | Bài nghe email | "the training is moved to Wednesday" | "the training has been moved to Wednesday" | Thông báo đổi lịch thì dùng hiện tại hoàn thành bị động |
| office | Hội thoại thuyết trình | "we can grow 10 percent next year" | "we expect to grow 10 percent next year" | Nói về dự báo thì dùng "expect", nghe đúng kiểu thuyết trình hơn |
| office | Vai trưởng nhóm | "We're on track. We finished three…" | "We've finished three…" | Báo cáo kết quả tính đến hiện tại thì dùng hiện tại hoàn thành |
| office | claim expenses (tiếng Việt) | "thanh toán chi phí đi lại" | "làm thủ tục hoàn lại chi phí đi lại" | "claim" là xin công ty hoàn lại tiền, không phải trả tiền |
| office | Nhận xét "Sales file is in there." | chỉ nói "mơ hồ" | thêm lỗi thiếu "The" | Nhận xét phải nêu đủ các lỗi |

## Đã kiểm tra, không cần sửa
- Đáp án (`a`) của cả 10 bài đọc đều đúng. Ngày trong tuần khớp với ngày tháng (14/3 là thứ Sáu, 5/6 là thứ Tư, 2/9 là thứ Hai).
- Mỗi hội thoại có đúng một đáp án đúng, và đáp án đúng đứng ở vị trí đầu.
- Bài nghe: đoạn dài có 2–3 câu và đúng 3 ô trống, không có ô trống nào là từ chức năng.
- IPA của office dùng thống nhất kiểu Anh-Anh. Romaji viết theo Hepburn và dùng dấu ō/ū nhất quán.
