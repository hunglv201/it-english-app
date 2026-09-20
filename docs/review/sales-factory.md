# Rà soát nội dung gói `sales` và `factory` (2026-09-20)

Đã rà từng dòng của `packs_src/sales.py` và `packs_src/factory.py`: từ vựng, IPA, từ loại, nghĩa tiếng Việt, thuật ngữ Nhật, hội thoại, bài nghe, vai, bài đọc, dịch ngược, sự kiện và câu mẫu báo cáo. Cấu trúc và số lượng giữ nguyên. `python3 packs_src/build.py sales factory` chạy qua.

## Số chỗ đã sửa

| Nhóm | sales | factory |
|---|---|---|
| Tiếng Anh (ngữ pháp, độ tự nhiên, ngữ cảnh) | 7 | 7 |
| IPA (dấu nhấn phụ ˌ trong danh từ ghép) | 0 | 7 |
| Tiếng Việt (nghĩa, độ tự nhiên, thuật ngữ) | 7 | 5 |
| Tiếng Nhật (sửa, thêm, bỏ) | 6 | 5 |
| Hội thoại (câu "sai" thực ra vẫn đúng, câu đúng sai quy trình, nhận xét) | 8 | 4 |
| Bài nghe (ô trống, câu) | (tính vào mục Tiếng Anh) | 2 |
| **Tổng** | **28** | **30** (29 lần sửa; `key point` sửa cả IPA lẫn tiếng Nhật) |

Không thấy lỗi ở những phần sau: đáp án bài đọc (`a`), số ô trống của bài nghe, từ vựng trùng trong cùng gói, 5S (Sàng lọc/Sắp xếp/Sạch sẽ/Săn sóc/Sẵn sàng ↔ 整理/整頓/清掃/清潔/躾), các cặp 歩留まり, 是正処置, ポカヨケ, 星取表, なぜなぜ分析, 特性要因図, 段取り替え, 多能工, 見える化.

## Những thay đổi quan trọng

| # | Gói | Trước | Sau | Lý do |
|---|---|---|---|---|
| 1 | sales | Câu đúng: "Since the item is faulty, we can give you a full refund." (khách chỉ nói "I want my money back") | "Could you tell me what's wrong with it? If it's faulty, we can give you a full refund within five working days." | Câu cũ tự cho là hàng lỗi rồi hoàn tiền luôn. Đúng quy trình là hỏi rõ vấn đề trước |
| 2 | sales | Hàng giao bị hư: "We'll send you a new one today, and you don't need to return the damaged one." | "Could you send me a photo of the damage? Then we'll send you a new one right away." | Quy trình thật: xin ảnh làm bằng chứng rồi mới gửi hàng thay (khớp với câu mẫu và bài nghe cùng chặng) |
| 3 | sales | receipt → 領収書 | レシート (reshīto) | Cửa hàng đưa cho khách レシート; 領収書 là biên nhận chính thức, ghi tên người nhận |
| 4 | sales | target → ノルマ | 売上目標 (uriage mokuhyō) | ノルマ mang nghĩa "chỉ tiêu ép" (tiêu cực), công ty Nhật không dùng làm thuật ngữ chính thức |
| 5 | sales | dispatch → 出荷 | 発送 (hassō) | Gửi đơn cho khách lẻ là 発送; 出荷 là xuất hàng ở nhà máy/kho |
| 6 | sales | product → 製品 | 商品 (shōhin) | Ở bán lẻ, món hàng bán cho khách là 商品 |
| 7 | sales | quotation → 見積もり | 見積書 (mitsumorisho) | Câu ví dụ nói tới tài liệu báo giá gửi qua email |
| 8 | sales | satisfaction → 満足度 | 満足 (manzoku) | 満足度 là "mức độ hài lòng", không phải "sự hài lòng" |
| 9 | sales | "How often will you use it?" = "Anh/chị sẽ dùng nó thường xuyên không ạ?" | "…định dùng nó bao lâu một lần ạ?" | Dịch sai: câu gốc hỏi tần suất, không phải hỏi có/không |
| 10 | sales | "May I put you on hold…" = "Em xin phép giữ máy…" | "Anh/chị vui lòng giữ máy…" (cả phần câu mẫu lẫn dịch ngược) | Người giữ máy là khách, không phải nhân viên. Câu cũ hiểu sai nghĩa |
| 11 | sales | Bài nghe: "…It's about two million more. But you can upgrade later if you prefer." | "…It costs about two million more. If you choose the basic one, you can upgrade it later." | Câu cũ không hợp lý (đã mua Pro thì nâng cấp cái gì) |
| 12 | sales | "…made in Việt Nam", "…in Hà Nội" (trong câu tiếng Anh) | "Vietnam", "Hanoi" | Viết đúng kiểu tiếng Anh, và TTS tiếng Anh đọc đúng |
| 13 | sales | Nhận xét "Your mother how old?" gợi ý "Does she use a smartphone much?" | "Thiếu động từ ('How old is she?')… nên hỏi về sở thích, thói quen" | Ngữ cảnh là mua quà, không phải mua điện thoại. Bổ sung cách sửa ngữ pháp |
| 14 | sales | "I'll resolve it for you now" (it = email) | "I'll help you with it right now." | Không ai "resolve" một email. Câu mới tự nhiên hơn |
| 15 | sales | "Great choice!" = "Anh/chị chọn chuẩn quá!" | "Anh/chị chọn rất hợp ạ!" | Câu cũ quá suồng sã với khách |
| 16 | sales | "pay by foreign card" (prompt vai) | "pay by a foreign card" | Thiếu mạo từ |
| 17 | sales | "With your usage, …" | "For your usage, …" | Tự nhiên hơn |
| 18 | sales | Nhận xét "I discount for you 20%" / "I recommend you to buy S3" | Nói rõ cấu trúc đúng và lỗi nghiệp vụ | Nhận xét cũ đưa cách sửa lệch con số, chưa nêu lỗi 'recommend sb to do' |
| 19 | factory | Câu "sai": "Yes, very much faster." (lỗi: 'much faster') | "Yes, it very fast." (thiếu động từ, không có số liệu) | "very much faster" là tiếng Anh đúng, nên câu sai cũ không sai thật |
| 20 | factory | Câu "sai": "Depends on the person maybe." | "Depends person maybe." + nhận xét 'It depends on the person' | Câu cũ gần như chấp nhận được, nhận xét không chỉ ra lỗi ngôn ngữ |
| 21 | factory | hazard → 危険 | 危険源 (kikengen) | Thuật ngữ chuẩn trong đánh giá rủi ro an toàn ở nhà máy Nhật |
| 22 | factory | trial run → 試運転 | bỏ tiếng Nhật (tuple 6 phần tử) | 試運転 là chạy thử máy. Còn "chạy thử 50 sản phẩm" thì cách gọi khác nhau tùy công ty (試作, トライ…), không chắc nên bỏ |
| 23 | factory | forecast (không có tiếng Nhật) | 内示 (naiji) | Dự báo đơn hàng khách gửi, ở nhà máy Nhật gọi là 内示 |
| 24 | factory | lead time (không có tiếng Nhật) | リードタイム (rīdo taimu) | Thuật ngữ chuẩn |
| 25 | factory | key point: /ˈkiː pɔɪnt/, không có tiếng Nhật | /ˌkiː ˈpɔɪnt/ + 急所 (kyūsho) | Sửa dấu nhấn theo Cambridge. 急所 là thuật ngữ TWI (作業の急所) trong đào tạo công nhân |
| 26 | factory | IPA production line, cycle time, lead time, customer claim, visitor badge, factory tour | Thêm dấu nhấn phụ ˌ cho từ thứ hai | Danh từ ghép phải ghi đủ nhấn chính và nhấn phụ, giống các mục khác |
| 27 | factory | first article = "hàng đầu" | "sản phẩm đầu tiên (hàng đầu lô/đầu ca…)" | "hàng đầu" dễ hiểu nhầm thành "tốt nhất" |
| 28 | factory | Bài nghe an toàn: ô trống "Line" | "slipped on oil…If you see oil on the floor, please clean it up" → ô trống slipped/floor/clean | Ô trống "Line" ít giá trị. Câu mới rõ hành động hơn |
| 29 | factory | Bài nghe "This size is out of spec" (ô trống size) | "This part is out of spec" (ô trống part) | "This size is out of spec" không tự nhiên |
| 30 | factory | "We will do full inspection" | "…do a full inspection" | Thiếu mạo từ |
| 31 | factory | "send you the corrective action" (câu mẫu, bài nghe) | "…corrective action report / plan" | Thứ được gửi là báo cáo/kế hoạch, không phải "hành động" |
| 32 | factory | "wear your PPE before you enter the line" | "…before you enter the production area" | "enter the line" không tự nhiên |
| 33 | factory | "There's strange vibration in the motor." | "There's a strange vibration…" | Tự nhiên hơn |
| 34 | factory | "move this order up to next week" = "đẩy đơn này lên tuần sau" | "đưa đơn này lên sớm hơn, làm vào tuần sau" | Câu cũ dễ hiểu nhầm thành lùi lịch; "move up" nghĩa là làm sớm hơn |
| 35 | factory | countermeasure = "biện pháp đối sách" | "đối sách, biện pháp xử lý" | Câu cũ lặp nghĩa |
| 36 | factory | certified for soldering = "tay nghề hàn" | "tay nghề hàn thiếc" | soldering (hàn thiếc) khác welding (hàn) |
| 37 | factory | "Today you will learn Station two." | "…learn the job at Station two." | Câu cũ không tự nhiên |
| 38 | factory | "a supplier's sales person" | "salesperson" | Viết đúng chính tả |
