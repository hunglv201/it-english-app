# Rà soát nội dung gói `marketing` và `health` (2026-09-20)

Đã đọc hết từng dòng của `packs_src/marketing.py` và `packs_src/health.py`: từ vựng, IPA, từ loại, nghĩa tiếng Việt, thuật ngữ tiếng Nhật, câu mẫu, hội thoại, bài nghe, vai, prompt AI, câu dịch ngược, bài đọc, sự kiện và câu mẫu báo cáo.
Cấu trúc và số lượng mục giữ nguyên (mỗi gói vẫn 10 chặng × 10 từ, 5 hội thoại, 6 bài nghe; 4 vai; 5 bài đọc). `python3 packs_src/build.py marketing health` chạy qua. Không có từ vựng, câu mẫu, bài nghe hay hội thoại nào bị lặp trong gói, và không trùng từ với các chặng lõi lấy từ office.

Nhìn chung cả hai gói đã tốt. Tiếng Việt đủ dấu, đáp án bài đọc đều đúng, hầu hết câu đúng trong gói y tế đã làm đúng quy trình an toàn. Phần sửa chủ yếu gồm:
- **marketing**: định nghĩa các chỉ số chưa ghi công thức, vài cách nói chưa tự nhiên ("sold 2,000 orders"), dấu nhấn IPA.
- **health**: vài câu đúng mà nhân viên vẫn tự quyết việc dùng thuốc, cách đọc lại y lệnh chưa đúng kỹ thuật, gọi bệnh nhân bằng số giường, và trùng tên bệnh nhân giữa hai giường.

## Số chỗ sửa theo loại

| Loại | marketing | health |
|---|---|---|
| Tiếng Anh (ngữ pháp, độ tự nhiên, từ loại) | 8 | 4 |
| IPA (dấu nhấn) | 2 | 4 |
| Tiếng Việt (nghĩa, bản dịch) | 5 | 5 |
| Tiếng Nhật | 2 | 2 |
| Nhận xét hội thoại | 3 | 1 |
| Bài nghe | 3 | 2 |
| Độ chính xác của chỉ số marketing (CTR, CPC, ROAS, tỉ lệ chuyển đổi) | 4 | – |
| An toàn người bệnh (thuốc, y lệnh, chuyển bác sĩ hoặc dược sĩ) | – | 8 |
| Gọi bệnh nhân có tôn trọng, nhận dạng bằng tên kèm số giường | – | 5 |
| Nhất quán dữ liệu | – | 1 |
| **Tổng** | **27** | **32** |

## Các thay đổi chính

| Gói | Mục | Trước | Sau | Lý do |
|---|---|---|---|---|
| health | Hội thoại "Give him the new medicine now." (chặng 9) | "Just to check: which medicine and what dose?" | "Just to confirm: which medicine, what dose, and how should I give it? I'll read it back to you." | Khi nhận y lệnh miệng phải hỏi đủ tên thuốc, liều và đường dùng rồi đọc lại |
| health | Câu mẫu đọc lại y lệnh | "Could you repeat the order, please? I want to read it back." | "Let me read the order back to you to make sure it's correct." | Đọc lại y lệnh (read-back) là điều dưỡng tự đọc lại cho bác sĩ xác nhận, không phải nhờ bác sĩ nhắc lại |
| health | Hội thoại tác dụng phụ (chặng 4) | "Please don't take the next dose until you speak to her." | "I'll let the doctor know right away and ask her about your next dose." | Nhân viên không tự quyết cho người bệnh ngừng thuốc. Bác sĩ quyết định liều tiếp theo |
| health | Câu mẫu thuốc | "This one should be taken after meals." | "The label says to take this one after meals." | Nhân viên chỉ nhắc lại hướng dẫn trên nhãn, không tự đưa ra cách dùng |
| health | Nhà thuốc, hỏi uống rượu bia | "It's best to avoid alcohol with this medicine." | "Let me check that with the pharmacist for you. Some medicines don't mix well with alcohol." | Chưa biết là thuốc gì thì nhân viên không nên khẳng định. Phải hỏi dược sĩ |
| health | Nhà thuốc, mua thuốc đau đầu | "Yes. Do you have any allergies or other medical conditions?…" | "Before I suggest anything, do you have any allergies, or are you taking any other medicine?" | Hỏi thêm thuốc đang dùng để tránh tương tác, và chưa hứa bán thuốc ngay |
| health | Hội thoại chóng mặt (chặng 1) | "I'll tell the doctor, and I'll stay with you." | "Please sit down and don't stand up on your own. I'll call the doctor and stay with you." | Câu cũ mâu thuẫn: đi báo bác sĩ thì không thể ở cạnh người bệnh. Câu mới dặn thêm để phòng ngã |
| health | specialist (ví dụ) | "You need to see a skin specialist." | "Would you like to see a skin specialist?" | Lễ tân không quyết định người bệnh cần khám chuyên khoa nào |
| health | Tên bệnh nhân | Ông Kim ở giường 4 (báo cáo, bài đọc) và cũng ở giường 7 (hội thoại gọi bác sĩ) | Giường 7 đổi thành Mr Wilson | Một tên ở hai giường là đúng kiểu nhầm lẫn bệnh nhân cần tránh |
| health | Giao ban (câu mẫu, hội thoại, bài nghe, dịch ngược, ví dụ stable) | "Bed 4 had a fever…", "Bed 3 is stable…" | "Mr Kim in bed 4…", "The patient in bed 3/4…" | Gọi người bệnh bằng số giường thiếu tôn trọng. Giao ban nên dùng tên kèm số giường để nhận dạng đúng |
| health | observation (tiếng Nhật) | 経過観察 (keika kansatsu) | bỏ (tuple 6 phần tử) | 経過観察 là "theo dõi diễn biến, chưa can thiệp", không phải đo sinh hiệu định kỳ |
| health | bed rest (tiếng Nhật) | 安静 (ansei) | ベッド上安静 (beddojō ansei) | Thuật ngữ điều dưỡng Nhật cho "nằm nghỉ tại giường". 安静 chỉ có nghĩa là nghỉ ngơi, giữ yên |
| health | medical certificate (tiếng Việt) | "giấy chứng nhận y tế, giấy khám sức khỏe" | "giấy xác nhận của bác sĩ (giấy nghỉ ốm, chứng nhận tình trạng bệnh)" | Giấy khám sức khỏe là một loại giấy khác. Công ty cần giấy nghỉ ốm hoặc giấy xác nhận của bác sĩ |
| health | over-the-counter (ví dụ) | "You can buy this over-the-counter…" | "This is an over-the-counter medicine…" | Từ được ghi là tính từ (adj). Viết có gạch nối thì chỉ đứng trước danh từ |
| health | nausea (ví dụ) | "The medicine may cause mild nausea." | "Do you have any nausea or vomiting?" | Chặng này dạy hỏi triệu chứng. Nhân viên không nên tự nói trước tác dụng phụ của thuốc |
| health | IPA medical history / fees / certificate / record | /ˈmedɪkl …/ | /ˌmedɪkl ˈ…/ | Theo Cambridge/Oxford, nhấn chính rơi vào từ thứ hai |
| health | Câu mẫu thanh toán | "Will you pay with insurance or by yourself?" | "Will you use your insurance, or pay yourself?" | "pay by yourself" nghĩa là tự đi trả một mình, không phải tự chi trả |
| health | Bài nghe biên lai | "Here is your receipt" (ô trống "Here") | "Here is your receipt for the insurance claim" (ô trống "receipt", "claim") | "Here" gần như là từ chức năng nên không nên làm ô trống |
| health | Bài nghe đón bệnh nhân | "Please show me your passport." | "May I see your passport, please?" | Nói với bệnh nhân thì câu mới lịch sự hơn, đúng như câu mẫu của chặng |
| health | faint (tiếng Việt) | "Một người nhà bị ngất" | "Một người đến thăm bị ngất" | Bản dịch phải sát câu gốc: visitor là người đến thăm |
| marketing | ROAS (nghĩa và ví dụ) | "doanh thu trên chi phí quảng cáo"; "we earn 4 dong for every 1 dong" | "= doanh thu từ quảng cáo ÷ chi phí quảng cáo"; "4 dong in revenue for every 1 dong we spend on ads" (+ "chưa phải lợi nhuận") | Câu cũ dùng "earn" nên dễ hiểu nhầm ROAS là lợi nhuận |
| marketing | CTR, CPC, conversion rate (nghĩa) | chỉ có tên tiếng Việt | thêm công thức: lượt nhấp ÷ lượt hiển thị; chi phí ÷ lượt nhấp; số đơn ÷ lượt truy cập | Người học cần hiểu đúng định nghĩa để báo cáo với sếp |
| marketing | "sold … orders" (câu mẫu, hội thoại, bài nghe) | "We sold 2,000 orders" | "We got 2,000 orders" | Người ta bán hàng chứ không "bán đơn". "Get/receive orders" mới là cách nói tự nhiên |
| marketing | objective (ví dụ) | "Our main objective is 2,000 new customers." | "…is to get 2,000 new customers." | Mục tiêu là một hành động, không phải con số đứng một mình |
| marketing | Câu mẫu giảm giá | "The discount must not make us lose money." | "We shouldn't lose money on this discount." | Câu cũ bị dịch từng chữ từ tiếng Việt |
| marketing | add to cart (ví dụ) | "…but don't pay." | "Many shoppers add to cart but never check out." | Dùng đúng thuật ngữ TMĐT "check out" |
| marketing | Hội thoại KPI | "We reached 92% of the target, mainly because of a slow first week." | "…We missed it mainly because the first week was slow." | Câu cũ nghe như tuần đầu chậm là lý do *đạt được* 92% |
| marketing | Bài nghe voucher / free shipping | "add our voucher"; "over three hundred thousand" | "use our voucher"; "…three hundred thousand dong" | Voucher thì "dùng", không phải "thêm". Số tiền phải có đơn vị |
| marketing | Bài nghe mở đầu pitch | ô trống "having" | ô trống "today" | "having" (trong "for having us") là từ nghĩa yếu, không nên làm ô trống |
| marketing | IPA product description, call to action | /ˈprɒdʌkt dɪˌskrɪpʃn/, /ˌkɔːl tu ˈækʃn/ | /ˌprɒdʌkt dɪˈskrɪpʃn/, /ˌkɔːl tə ˈækʃn/ | Sửa dấu nhấn chính, và "to" ở đây đọc dạng yếu /tə/ |
| marketing | Tiếng Việt "ship the same day", "20 đơn chờ giao" | "được giao ngay trong ngày", "chờ giao" | "được gửi đi ngay trong ngày", "chờ gửi đi" | "ship" là gửi hàng đi, không có nghĩa là khách nhận được trong ngày |
| marketing | Tiếng Việt "by Thursday noon", "instead" | "trước trưa thứ Năm", "…thay vào đó được không?" | "chậm nhất trưa thứ Năm", "đổi sang đăng vào tối thứ Bảy…" | "by" nghĩa là hạn chót. "thay vào đó" là dịch từng chữ |
| marketing | USP (tiếng Việt) | "điểm bán hàng độc nhất" | "điểm khác biệt độc nhất, lợi điểm bán hàng (USP)" | Dùng thuật ngữ quen thuộc với dân marketing Việt Nam, khớp với câu ví dụ |
| marketing | Nhận xét "OK, I fix it after." | "'later' mơ hồ" (trong câu không có chữ "later") | "'after' đứng cuối câu vừa sai vừa mơ hồ" | Nhận xét phải nói đúng chữ có trong câu |
| marketing | Nhận xét "Customer can ask in chat." | "bỏ qua nguyên nhân gây trả hàng" | "Thiếu mạo từ ('The customer') và đẩy việc cho khách…" | Nêu đủ lỗi ngữ pháp và lỗi xử lý |
| marketing | Romaji | kurikku-ritsu, konbājon-ritsu | kurikkuritsu, konbājonritsu | Viết liền theo Hepburn, cho thống nhất với chokkiritsu |

## Đã kiểm tra, không cần sửa
- Đáp án (`a`) của 10 bài đọc đều đúng. Số liệu trong bài đọc khớp nhau (52 triệu × ROAS 4.0 = 208 triệu; đồng chi trả 20% ↔ bảo hiểm trả 80%).
- Mỗi hội thoại có đúng một đáp án đúng, và đáp án đúng đứng ở vị trí đầu. Đáp án sai đều sai rõ, về ngữ pháp hoặc về thực hành an toàn.
- Gói health: không có câu nào đưa ra liều thuốc hay chẩn đoán bệnh. Các bước an toàn đều có: hỏi dị ứng, xác nhận họ tên và ngày sinh, bảo mật kết quả xét nghiệm, phòng té ngã, báo bác sĩ khi người bệnh diễn biến xấu (SBAR), không hứa trước kết quả.
- Viết tắt đọc từng chữ cái: CTR, CPC, KPI, SKU, KOL, IV, ID. **ROAS được giữ /ˈrəʊæs/**, đọc như một từ, vì dân quảng cáo thường đọc như vậy.
- Thuật ngữ tiếng Nhật còn lại đều chuẩn (クリック率, 直帰率, 前月比, 既往歴, 紹介状, ナースコール, 回診, 自己負担…).
