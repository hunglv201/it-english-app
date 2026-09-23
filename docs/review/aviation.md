# Rà soát nội dung gói `aviation` và `ja/keigo.js` (2026-09-23)

Đã đọc hết từng dòng của `packs_src/aviation.py`: từ vựng, IPA, từ loại, nghĩa tiếng Việt, thuật ngữ tiếng Nhật, câu mẫu, hội thoại, bài nghe, vai, prompt AI, câu dịch ngược, bài đọc, sự kiện và câu mẫu báo cáo.
Cấu trúc và số lượng mục giữ nguyên. `python3 packs_src/build.py aviation` chạy qua.

Nhìn chung gói đã tốt: không thấy lỗi dấu tiếng Việt, IPA đúng kiểu Anh-Anh, thuật ngữ tiếng Nhật đều là từ chuẩn của ngành hàng không Nhật, đáp án bài đọc đều đúng. Không có tên hay mã hãng bay thật, số hiệu chuyến chỉ là số (215, 320, 680). Các câu về phí và hạn mức luôn nói chung chung ("shown on the screen", "according to our policy"). Phần sửa chủ yếu là câu chưa tự nhiên, chỉ sai quầy và vài nghĩa chưa chính xác.

## Số chỗ sửa theo loại

| Loại | aviation |
|---|---|
| Tiếng Anh (ngữ pháp, độ tự nhiên) | 7 |
| Tiếng Việt (nghĩa) | 3 |
| Tiếng Nhật | 1 |
| Thực tế nghề | 3 |
| Hội thoại (đáp án đúng chưa rõ) | 1 |
| Bài nghe | 1 |
| **Tổng** | **16** |

## Các thay đổi chính

| Mục | Trước | Sau | Lý do |
|---|---|---|---|
| Hội thoại ra cửa muộn (chặng 5) | "take you to the transfer desk" | "take you to the customer service desk" | Quầy nối chuyến (transfer desk) chỉ dành cho khách quá cảnh. Khách đi từ sân bay này bị lỡ chuyến thì ra quầy dịch vụ khách hàng |
| Bài đọc Departures | "Cancelled – please go to the transfer desk", đáp án "Go to the transfer desk" | "customer service desk" (cả bài và đáp án) | Cùng lý do trên, bảng khởi hành là cho khách xuất phát |
| no-show (tiếng Việt) | "đã làm thủ tục nhưng không lên máy bay" | "có vé/đã làm thủ tục nhưng không đến lên máy bay" | *No-show* gồm cả khách không đến làm thủ tục. Loại đã làm thủ tục mà không lên là *gate no-show* |
| Ví dụ pregnant | "Are you <b>pregnant</b>? Let me check…" | "Since you are <b>pregnant</b>, let me check…" | Hỏi thẳng khách "Chị có thai không?" là thiếu tế nhị. Chỉ nói khi khách đã cho biết |
| Hội thoại cởi giày (chặng 4) | "Not today." | "No, you don't need to." | "Not today" nghe như quy định đổi theo ngày, dễ làm khách khó hiểu |
| Hội thoại tờ khai nhập cảnh | "Yes, please." | "Yes, you do." | Khách hỏi "Do I need to…?" nên đáp "Yes, you do". "Yes, please" không khớp câu hỏi |
| Vai check-in, hỏi số kiện xách tay | "It depends on your ticket. For your ticket, it's one carry-on…" | "Let me check your ticket. You can take one carry-on…" | Câu cũ lặp và gượng. Câu mới vẫn giữ ý kiểm tra theo vé |
| Câu mẫu nâng hạng | "There is a paid upgrade to business class. Would you like to hear the price?" | "You can upgrade to business class for an extra charge. Would you like to know the price?" | Câu cũ không tự nhiên. Tiếng Việt viết lại cho khớp |
| priority boarding (ví dụ) | "Families with small children are welcome for priority boarding." | "Families with small children can use priority boarding." | "welcome for" sai kết hợp từ |
| Câu mẫu gọi lần cuối | "final call for passenger Mr. David Lee" | "final call for passenger David Lee" | Đã có "passenger" thì bỏ "Mr.", đúng kiểu thông báo sân bay |
| stroller (ví dụ) | "until the aircraft door" | "up to the aircraft door" | "until" dùng cho thời gian. Nói nơi chốn thì dùng "up to" |
| Bài nghe giờ lên máy bay | "Boarding starts at Gate twelve at nine fifteen" | "Boarding starts at nine fifteen at Gate twelve" | Cho khớp thứ tự trong câu mẫu (giờ trước, cửa sau) và nghe tự nhiên hơn |
| Bài nghe đồ dễ vỡ | "Here is your claim tag, so please keep it safe." | "Here is your claim tag. Please keep it safe." | Dùng "so" ở đây không hợp lý |
| Câu mẫu Boarding (tiếng Việt) | "Giờ lên máy bay bắt đầu lúc 9 giờ 15" | "Bắt đầu lên máy bay lúc 9 giờ 15" | Câu cũ thừa và lủng củng ("giờ… bắt đầu") |
| Dịch ngược | "Tôi sẽ đặt cho anh/chị chuyến bay kế tiếp." | "Tôi sẽ đặt chỗ cho anh/chị trên chuyến bay kế tiếp." | Đặt chỗ trên chuyến bay, không phải "đặt chuyến bay" cho khách |
| Tiếng Nhật duty-free | 免税品 (menzeihin) | 免税 (menzei) | Từ gốc là tính từ ("duty-free perfume"). 免税品 nghĩa là "hàng miễn thuế" |

## Đã kiểm tra, không cần sửa
- Mỗi hội thoại có đúng một đáp án đúng, và đáp án sai đều sai rõ ràng (sai ngữ pháp, thô lỗ, sai an toàn hoặc hứa bừa). Nhận xét khớp với lỗi.
- 5 bài đọc: đáp án (`a`) đều đúng (12:20; customer service desk; Two; A technical issue / A meal voucher; In Bangkok / green ribbon).
- Bài nghe: ô trống đều là từ nội dung. Đoạn dài có 2–3 câu và đúng 3 ô trống.
- An toàn bay: sạc dự phòng không được ký gửi, không cho khách đứng dậy khi đèn thắt dây còn bật, không cho đổi ghế trước khi cất cánh, đeo mặt nạ cho mình trước. Tất cả đều đúng quy tắc chung của ngành.
- Thuật ngữ Nhật (受託手荷物, 無料手荷物許容量, 非常口座席, バシネット, 手荷物引換証, 遺失物取扱所…) đều là từ các hãng Nhật đang dùng. Romaji viết theo Hepburn và dùng dấu ō/ū nhất quán.

---

# `ja/keigo.js` — câu cố định & keigo công sở

Đã đọc 7 nhóm, 51 câu. Kiểm tra độ tự nhiên, nhãn keigo, furigana, `kana`, romaji Hepburn (ā/ō/ū), nghĩa và cách dùng tiếng Việt, câu tiếng Anh tương đương.
Kết quả kiểm tra ruby: `7 0` (7 nhóm, không có câu nào mà ruby bỏ phần đọc ra lại khác `ja`).

Chất lượng đã cao: furigana chỉ đặt trên kanji và đọc đúng, `kana` và romaji khớp với câu, nhãn 尊敬語/謙譲語/丁寧語 hợp lý với mức keigo chủ đạo của từng câu. Các ghi chú văn hoá đều đúng: ご苦労様 là câu người trên nói với người dưới; nói với khách về người trong công ty mình thì bỏ さん; お名前をいただけますか là cách nói sai.

**Sửa 3 chỗ:**

| Câu | Trước | Sau | Lý do |
|---|---|---|---|
| かしこまりました (vi) | "Vâng, tôi xin làm ngay ạ" | "Vâng, tôi đã rõ ạ … (lễ phép hơn 承知しました)" | Câu này nghĩa là "đã rõ, xin vâng", không có nghĩa "làm ngay" |
| お手数ですが、よろしくお願いいたします (when) | "Không cần dùng khi người kia làm việc vốn là nhiệm vụ của mình" | "…kể cả khi việc đó thuộc nhiệm vụ của người kia. Trang trọng hơn: お手数をおかけしますが…" | Ghi chú cũ sai: câu này vẫn được dùng rộng rãi cả với việc thuộc phận sự của người nhận (vd. nhờ khách điền form) |
| 少々お待ちください (when) | "Với khách hàng nên nói đầy đủ hơn: 少々お待ちいただけますか" | "Với khách hàng có thể nói mềm hơn: 少々お待ちいただけますでしょうか" | Bản thân 少々お待ちください đã là cách nói chuẩn với khách hàng. Câu gợi ý cũ không lịch sự hơn câu gốc |

Giữ nguyên, dù có thể bàn thêm: ご返信が遅くなり (chữ ご là cách nói khiêm nhường và thường gặp trong email công việc), `tenpu` (kiểu Hepburn sửa đổi, n đứng trước p).
