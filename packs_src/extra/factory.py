# -*- coding: utf-8 -*-
# v4.1 — nội dung làm giàu cho gói factory (nối vào cuối gói, xem build.py)

PHASES = []

# ───────────────────────── A. Đọc bản vẽ & thông số kỹ thuật ─────────────────────────
PHASES.append({
 "title": "Đọc bản vẽ & thông số kỹ thuật",
 "vocab": [
  ("dimension", "/daɪˈmenʃn/", "n", "kích thước", "Please check every <b>dimension</b> on the drawing.", "Vui lòng kiểm tra mọi kích thước trên bản vẽ.", "寸法", "sunpō"),
  ("diameter", "/daɪˈæmɪtə/", "n", "đường kính", "The hole <b>diameter</b> is 8 millimetres.", "Đường kính lỗ là 8 mi-li-mét.", "直径", "chokkei"),
  ("revision", "/rɪˈvɪʒn/", "n", "phiên bản sửa đổi (của bản vẽ, tài liệu)", "Are you using drawing <b>revision</b> C?", "Anh đang dùng bản vẽ phiên bản C phải không?", "改訂", "kaitei"),
  ("scale", "/skeɪl/", "n", "tỉ lệ (bản vẽ)", "This drawing is at a <b>scale</b> of 1:2.", "Bản vẽ này theo tỉ lệ 1:2."),
  ("surface roughness", "/ˈsɜːfɪs ˈrʌfnəs/", "n", "độ nhám bề mặt", "The <b>surface roughness</b> must be Ra 1.6 or better.", "Độ nhám bề mặt phải đạt Ra 1,6 hoặc tốt hơn.", "面粗さ", "menarasa"),
  ("caliper", "/ˈkælɪpə/", "n", "thước cặp", "Measure the width with a <b>caliper</b>.", "Đo chiều rộng bằng thước cặp.", "ノギス", "nogisu"),
  ("micrometer", "/maɪˈkrɒmɪtə/", "n", "panme (dụng cụ đo chính xác)", "Use a <b>micrometer</b> for this thin part.", "Dùng panme để đo chi tiết mỏng này.", "マイクロメータ", "maikuromēta"),
  ("go/no-go gauge", "/ˌɡəʊ ˈnəʊ ɡəʊ ˌɡeɪdʒ/", "n", "dưỡng kiểm lọt/không lọt", "Check each hole with the <b>go/no-go gauge</b>.", "Kiểm tra từng lỗ bằng dưỡng lọt/không lọt.", "限界ゲージ", "genkai gēji"),
  ("upper limit", "/ˌʌpə ˈlɪmɪt/", "n", "giới hạn trên", "The <b>upper limit</b> is 10.05 millimetres.", "Giới hạn trên là 10,05 mi-li-mét.", "上限", "jōgen"),
  ("measurement", "/ˈmeʒəmənt/", "n", "phép đo, số đo", "Please write each <b>measurement</b> on the check sheet.", "Vui lòng ghi từng số đo vào phiếu kiểm tra.", "測定", "sokutei"),
 ],
 "phrases": [
  ("Which drawing revision are you using?", "Bạn đang dùng bản vẽ phiên bản nào?"),
  ("The latest revision is D, not C.", "Phiên bản mới nhất là D, không phải C."),
  ("All dimensions are in millimetres.", "Tất cả kích thước đều tính bằng mi-li-mét."),
  ("The tolerance for this hole is plus 0.1, minus 0.", "Dung sai của lỗ này là cộng 0,1, trừ 0."),
  ("This measurement is close to the upper limit.", "Số đo này sát giới hạn trên."),
  ("Please measure it three times and take the average.", "Đo ba lần rồi lấy giá trị trung bình nhé."),
  ("This drawing is not to scale, so don't measure from the paper.", "Bản vẽ này không theo tỉ lệ, đừng đo trực tiếp trên giấy."),
  ("What does this symbol mean?", "Ký hiệu này nghĩa là gì?"),
  ("The note says: remove all sharp edges.", "Phần ghi chú yêu cầu: làm tù hết các cạnh sắc."),
  ("Please remove the old revision from the line.", "Vui lòng thu hồi bản vẽ phiên bản cũ khỏi chuyền."),
 ],
 "dialogues": [
  ("What's the diameter of this hole?", [
    ("It's 8.2 millimetres, plus or minus 0.05. I checked it on revision D.", True, "Con số + dung sai + nói rõ dùng bản vẽ phiên bản nào."),
    ("Hole is 8.2.", False, "Thiếu 'The', thiếu đơn vị và dung sai: 'The hole is 8.2 millimetres.'"),
    ("It is very small hole.", False, "Thiếu 'a' và mơ hồ — kỹ thuật cần con số, không cần cảm nhận."),
  ]),
  ("This measurement is 10.08. Is it OK?", [
    ("No. The upper limit is 10.05, so it's 0.03 over. It's out of tolerance.", True, "So với giới hạn + vượt bao nhiêu + kết luận rõ."),
    ("Only 0.03 over, so it's OK.", False, "Sai về chất lượng: vượt dung sai dù ít vẫn là NG."),
    ("I think is OK.", False, "Thiếu chủ ngữ ('I think it's OK') và kết luận sai."),
  ]),
  ("Which revision is the line using?", [
    ("Revision C. But the customer sent revision D yesterday, so I'll replace it today.", True, "Trả lời + phát hiện chênh lệch + hành động ngay."),
    ("The line use old one.", False, "Thiếu 's' ('uses'), thiếu 'the' và không nói phiên bản cụ thể."),
    ("Revision is not important.", False, "Sai nghiêm trọng — dùng nhầm phiên bản bản vẽ dễ gây lỗi hàng loạt."),
  ]),
  ("How did you measure this width?", [
    ("With a digital caliper. I measured it three times and took the average.", True, "Nói rõ dụng cụ + cách đo."),
    ("I measure by eye.", False, "Sai thì ('measured') và đo bằng mắt thì không có giá trị."),
    ("By caliper maybe.", False, "Mơ hồ, thiếu chủ ngữ; nên nói 'I used a caliper.'"),
  ]),
  ("I don't understand this symbol on the drawing.", [
    ("That's the surface roughness symbol. Here it means Ra 1.6 or better.", True, "Giải thích ký hiệu + ý nghĩa cụ thể."),
    ("Me too. Just skip it.", False, "Bỏ qua yêu cầu trên bản vẽ là rủi ro — không hiểu thì hỏi kỹ sư."),
    ("It is symbol of Japan.", False, "Đoán mò, thiếu mạo từ và không giải thích được ý nghĩa."),
  ]),
 ],
 "listen": [
  ("All dimensions on this drawing are in millimetres", ["dimensions", "millimetres"], "đơn vị trên bản vẽ"),
  ("Please use drawing revision D from today", ["revision", "today"], "đổi phiên bản bản vẽ"),
  ("This measurement is close to the upper limit", ["measurement", "upper"], "số đo sát giới hạn"),
  ("Check each hole with the go/no-go gauge", ["hole", "gauge"], "dùng dưỡng kiểm"),
  ("The customer changed the drawing. The new diameter is eight point two millimetres. Please remove the old revision from the line.", ["customer", "diameter", "remove"], "thông báo đổi bản vẽ"),
  ("I measured ten parts with a micrometer. Two of them were over the upper limit. Please hold the lot.", ["micrometer", "over", "hold"], "báo kết quả đo"),
 ],
})

# ───────────────────────── B. Nguyên vật liệu & nhà cung cấp ─────────────────────────
PHASES.append({
 "title": "Nguyên vật liệu & nhà cung cấp",
 "vocab": [
  ("incoming inspection", "/ˈɪnkʌmɪŋ ɪnˈspekʃn/", "n", "kiểm tra đầu vào (IQC)", "All materials must pass <b>incoming inspection</b>.", "Mọi nguyên vật liệu đều phải qua kiểm tra đầu vào.", "受入検査", "ukeire kensa"),
  ("material certificate", "/məˌtɪəriəl səˈtɪfɪkət/", "n", "chứng chỉ vật liệu (mill sheet)", "The <b>material certificate</b> is missing for this coil.", "Cuộn thép này thiếu chứng chỉ vật liệu.", "ミルシート", "mirushīto"),
  ("resin", "/ˈrezɪn/", "n", "hạt nhựa, nhựa nguyên liệu", "Dry the <b>resin</b> for four hours before molding.", "Sấy hạt nhựa bốn tiếng trước khi ép.", "樹脂", "jushi"),
  ("coil", "/kɔɪl/", "n", "cuộn (thép, tôn, dây)", "Each steel <b>coil</b> weighs about five tons.", "Mỗi cuộn thép nặng khoảng năm tấn.", "コイル", "koiru"),
  ("quotation", "/kwəʊˈteɪʃn/", "n", "bảng báo giá", "Please send us a <b>quotation</b> for 10,000 pieces.", "Vui lòng gửi chúng tôi báo giá cho 10.000 cái.", "見積書", "mitsumorisho"),
  ("unit price", "/ˌjuːnɪt ˈpraɪs/", "n", "đơn giá", "The <b>unit price</b> went up by 5 percent.", "Đơn giá đã tăng 5%.", "単価", "tanka"),
  ("minimum order quantity", "/ˌmɪnɪməm ˈɔːdə ˌkwɒntəti/", "n", "số lượng đặt hàng tối thiểu (MOQ)", "The <b>minimum order quantity</b> is 500 kilograms.", "Số lượng đặt hàng tối thiểu là 500 ki-lô-gam."),
  ("delivery date", "/dɪˈlɪvəri ˌdeɪt/", "n", "ngày giao hàng", "Can you confirm the <b>delivery date</b>?", "Anh xác nhận giúp ngày giao hàng được không?", "納期", "nōki"),
  ("substitute", "/ˈsʌbstɪtjuːt/", "n", "vật liệu/hàng thay thế", "We can't use a <b>substitute</b> without customer approval.", "Không được dùng vật liệu thay thế khi chưa được khách hàng duyệt."),
  ("expiry date", "/ɪkˈspaɪəri ˌdeɪt/", "n", "hạn sử dụng", "Check the <b>expiry date</b> on the glue before use.", "Kiểm tra hạn sử dụng của keo trước khi dùng.", "使用期限", "shiyō kigen"),
 ],
 "phrases": [
  ("The material arrived this morning. IQC is checking it now.", "Vật tư về sáng nay. IQC đang kiểm tra."),
  ("This lot failed incoming inspection.", "Lô này không đạt kiểm tra đầu vào."),
  ("Please send the material certificate with every delivery.", "Mỗi lần giao hàng vui lòng gửi kèm chứng chỉ vật liệu."),
  ("Could you send us a quotation by Friday?", "Anh gửi báo giá cho chúng tôi trước thứ Sáu được không?"),
  ("The unit price is higher than last time.", "Đơn giá cao hơn lần trước."),
  ("What's your minimum order quantity?", "Số lượng đặt hàng tối thiểu bên anh là bao nhiêu?"),
  ("Can you deliver two days earlier?", "Bên anh giao sớm hơn hai ngày được không?"),
  ("We can't accept a substitute without approval.", "Chúng tôi không nhận hàng thay thế khi chưa được duyệt."),
  ("This glue expires next month, so use it first.", "Keo này tháng sau hết hạn nên dùng trước."),
 ],
 "dialogues": [
  ("The resin from the supplier is wet. What should we do?", [
    ("Let's put it on hold and inform the supplier. We can't use it until QC checks it.", True, "Giữ hàng + báo nhà cung cấp + chờ QC đánh giá."),
    ("Just dry it longer and use.", False, "Thiếu 'it' ('use it') và tự ý xử lý khi QC chưa đánh giá."),
    ("Supplier always bad.", False, "Thiếu động từ ('is always bad') và chỉ than phiền, không xử lý."),
  ]),
  ("Did the steel coils arrive?", [
    ("Yes, ten coils arrived at nine. But one material certificate is missing, so I've asked the supplier to email it.", True, "Xác nhận + số lượng + vấn đề + đã làm gì."),
    ("Yes, arrive already.", False, "Thiếu chủ ngữ và sai thì: 'Yes, they arrived this morning.'"),
    ("Coils is heavy.", False, "Sai chia động từ ('are') và lạc đề."),
  ]),
  ("The supplier raised the unit price by 8 percent.", [
    ("Let's ask them for the reason and a cost breakdown. I'll also get quotations from two other suppliers.", True, "Hỏi lý do + so sánh báo giá — cách làm mua hàng chuyên nghiệp."),
    ("OK, we pay.", False, "Chấp nhận ngay, không đàm phán hay so sánh."),
    ("Too expensive, no buy.", False, "Cộc lốc, dịch từng chữ 'không mua'; nên nói 'We can't accept this price.'"),
  ]),
  ("Our supplier wants to send a substitute resin. Is that OK?", [
    ("Not yet. We need the data sheet and a trial run, and then the customer has to approve it.", True, "Nêu đúng quy trình duyệt thay đổi vật liệu."),
    ("Same color, so no problem.", False, "Cùng màu chưa chắc cùng tính chất — đổi vật liệu phải được duyệt."),
    ("I am not know.", False, "Sai ngữ pháp: 'I don't know' — và nên nói sẽ hỏi ai."),
  ]),
  ("What's the minimum order quantity for this part?", [
    ("It's 2,000 pieces. That's about one month of use for us.", True, "Con số + quy đổi ra mức sử dụng."),
    ("Minimum is little.", False, "Mơ hồ, không có con số."),
    ("We order minimum always.", False, "Không trả lời câu hỏi và sai trật tự từ."),
  ]),
 ],
 "listen": [
  ("The material arrived at nine this morning", ["material", "arrived"], "vật tư về"),
  ("This lot failed incoming inspection", ["failed", "incoming"], "không đạt IQC"),
  ("Please send the quotation by Friday", ["quotation", "Friday"], "hỏi báo giá"),
  ("Check the expiry date before you use the glue", ["expiry", "glue"], "kiểm tra hạn dùng"),
  ("The supplier called this morning. The resin will arrive two days late. Please change tomorrow's plan.", ["supplier", "late", "plan"], "báo vật tư về trễ"),
  ("IQC checked the steel coils. The thickness was OK, but one certificate was missing. We asked the supplier to send it today.", ["thickness", "certificate", "send"], "kết quả kiểm tra đầu vào"),
 ],
})

# ───────────────────────── C. Đóng gói, xuất hàng & kho thành phẩm ─────────────────────────
PHASES.append({
 "title": "Đóng gói, xuất hàng & kho thành phẩm",
 "vocab": [
  ("finished goods", "/ˌfɪnɪʃt ˈɡʊdz/", "n", "thành phẩm", "Move the <b>finished goods</b> to the shipping area.", "Chuyển thành phẩm ra khu vực xuất hàng.", "完成品", "kanseihin"),
  ("packing list", "/ˈpækɪŋ ˌlɪst/", "n", "phiếu đóng gói (packing list)", "The <b>packing list</b> must match the cartons.", "Phiếu đóng gói phải khớp với số thùng."),
  ("carton", "/ˈkɑːtn/", "n", "thùng các-tông", "Each <b>carton</b> holds 50 pieces.", "Mỗi thùng chứa 50 cái.", "段ボール", "danbōru"),
  ("pallet", "/ˈpælət/", "n", "pallet (tấm kê hàng)", "Put 20 cartons on each <b>pallet</b>.", "Mỗi pallet xếp 20 thùng.", "パレット", "paretto"),
  ("shipping label", "/ˈʃɪpɪŋ ˌleɪbl/", "n", "nhãn xuất hàng", "The <b>shipping label</b> shows the part number and quantity.", "Nhãn xuất hàng ghi mã hàng và số lượng.", "出荷ラベル", "shukka raberu"),
  ("FIFO", "/ˈfaɪfəʊ/", "n", "nhập trước xuất trước", "Always ship by <b>FIFO</b>: old stock goes first.", "Luôn xuất theo FIFO: hàng cũ xuất trước.", "先入れ先出し", "sakiire sakidashi"),
  ("forklift", "/ˈfɔːklɪft/", "n", "xe nâng", "Only licensed drivers can use the <b>forklift</b>.", "Chỉ người có chứng chỉ mới được lái xe nâng.", "フォークリフト", "fōkurifuto"),
  ("stack", "/stæk/", "v", "xếp chồng", "Don't <b>stack</b> more than five cartons.", "Không xếp chồng quá năm thùng."),
  ("loading dock", "/ˈləʊdɪŋ ˌdɒk/", "n", "cửa/bến bốc xếp hàng", "The truck is waiting at <b>loading dock</b> 2.", "Xe tải đang chờ ở cửa bốc xếp số 2."),
  ("outgoing inspection", "/ˈaʊtɡəʊɪŋ ɪnˈspekʃn/", "n", "kiểm tra xuất hàng (OQC)", "The lot passed <b>outgoing inspection</b> this morning.", "Lô hàng đã đạt kiểm tra xuất hàng sáng nay.", "出荷検査", "shukka kensa"),
 ],
 "phrases": [
  ("Please pack 50 pieces in each carton.", "Mỗi thùng đóng 50 cái nhé."),
  ("The label is missing on two cartons.", "Hai thùng bị thiếu nhãn."),
  ("Please check the quantity against the packing list.", "Kiểm tra số lượng so với phiếu đóng gói nhé."),
  ("Ship the old stock first — FIFO.", "Xuất hàng cũ trước — theo FIFO."),
  ("Don't stack the cartons too high.", "Đừng xếp thùng cao quá."),
  ("The truck will arrive at loading dock 2 at 3 p.m.", "Xe tải sẽ đến cửa bốc xếp số 2 lúc 3 giờ chiều."),
  ("This pallet is ready to ship.", "Pallet này đã sẵn sàng để xuất."),
  ("One carton is damaged. Please repack it.", "Một thùng bị móp. Đóng lại sang thùng mới nhé."),
  ("The finished goods area is full.", "Khu thành phẩm đã đầy."),
 ],
 "dialogues": [
  ("The packing list says 40 cartons, but I count 39.", [
    ("Thanks for checking. Let's stop loading and find the missing carton before the truck leaves.", True, "Cảm ơn + dừng lại + tìm cho khớp trước khi xe chạy."),
    ("It's OK, only one carton.", False, "Lệch số lượng sẽ bị khách khiếu nại — phải xử lý trước khi xuất."),
    ("Maybe you count wrong.", False, "Sai thì ('counted') và đổ lỗi thay vì đếm lại."),
  ]),
  ("Which pallet should we ship first?", [
    ("The one from May 2. We ship by FIFO, so the oldest stock goes first.", True, "Trả lời cụ thể + nêu nguyên tắc FIFO."),
    ("The nearest one. It's faster.", False, "Sai nguyên tắc FIFO — hàng cũ để lâu có thể quá hạn."),
    ("Any pallet also can.", False, "Dịch từng chữ 'cái nào cũng được' — sai cả ngữ pháp lẫn nguyên tắc."),
  ]),
  ("This carton is damaged. Can we still ship it?", [
    ("No. Let's repack the parts in a new carton and put a new label on it.", True, "Từ chối + cách xử lý cụ thể."),
    ("Customer will not see.", False, "Thiếu 'The' và tư duy giấu lỗi — rủi ro mất khách."),
    ("Yes, put tape more.", False, "Sai trật tự từ ('more tape') và vẫn xuất thùng hỏng."),
  ]),
  ("Has the lot for the Korean customer passed outgoing inspection?", [
    ("Yes, it passed at 10. The pallets are wrapped and waiting at loading dock 1.", True, "Xác nhận + giờ + tình trạng hàng."),
    ("Yes, it pass.", False, "Sai thì: 'Yes, it passed.'"),
    ("OQC is busy today.", False, "Không trả lời câu hỏi đã đạt hay chưa."),
  ]),
  ("The finished goods area is full. Where can I put these pallets?", [
    ("Put them in Area B for now. I'll ask logistics to move out today's shipment first.", True, "Chỗ để tạm + giải quyết gốc (cho hàng xuất đi)."),
    ("Put on the walkway.", False, "Thiếu 'them' và chắn lối đi — vi phạm an toàn."),
    ("Not my problem.", False, "Đùn đẩy trách nhiệm."),
  ]),
 ],
 "listen": [
  ("Please pack fifty pieces in each carton", ["pack", "carton"], "quy cách đóng gói"),
  ("Two cartons have no shipping label", ["cartons", "label"], "thiếu nhãn"),
  ("The truck is waiting at loading dock two", ["truck", "dock"], "xe chờ bốc hàng"),
  ("Always ship the old stock first", ["ship", "old"], "nguyên tắc FIFO"),
  ("The truck for Korea comes at three. We need twelve pallets. Please check each label against the packing list.", ["Korea", "pallets", "label"], "chuẩn bị xuất hàng"),
  ("One carton was damaged by the forklift. We repacked the parts. The shipment will leave on time.", ["damaged", "repacked", "time"], "báo hàng hư khi bốc xếp"),
 ],
})

# ───────────────────────── D. Môi trường, hoá chất & chất thải ─────────────────────────
PHASES.append({
 "title": "Môi trường, hoá chất & chất thải",
 "vocab": [
  ("chemical", "/ˈkemɪkl/", "n", "hoá chất", "Keep all <b>chemicals</b> in the locked cabinet.", "Cất tất cả hoá chất trong tủ có khoá.", "化学物質", "kagaku busshitsu"),
  ("safety data sheet", "/ˌseɪfti ˈdeɪtə ˌʃiːt/", "n", "phiếu an toàn hoá chất (SDS)", "Read the <b>safety data sheet</b> before you use a new chemical.", "Đọc phiếu an toàn hoá chất trước khi dùng một hoá chất mới.", "安全データシート", "anzen dēta shīto"),
  ("hazardous waste", "/ˌhæzədəs ˈweɪst/", "n", "chất thải nguy hại", "Oily rags are <b>hazardous waste</b>.", "Giẻ dính dầu là chất thải nguy hại."),
  ("spill", "/spɪl/", "n/v", "sự tràn đổ; làm đổ", "Clean up the oil <b>spill</b> with the spill kit.", "Dùng bộ dụng cụ xử lý tràn đổ để làm sạch chỗ dầu bị đổ."),
  ("ventilation", "/ˌventɪˈleɪʃn/", "n", "sự thông gió", "The paint room needs good <b>ventilation</b>.", "Phòng sơn cần thông gió tốt.", "換気", "kanki"),
  ("solvent", "/ˈsɒlvənt/", "n", "dung môi", "Close the <b>solvent</b> can after use.", "Dùng xong phải đậy nắp can dung môi.", "溶剤", "yōzai"),
  ("respirator", "/ˈrespəreɪtə/", "n", "mặt nạ phòng độc", "Wear a <b>respirator</b> when you mix the paint.", "Đeo mặt nạ phòng độc khi pha sơn.", "防毒マスク", "bōdoku masuku"),
  ("flammable", "/ˈflæməbl/", "adj", "dễ cháy", "Keep <b>flammable</b> liquids away from heat.", "Để chất lỏng dễ cháy tránh xa nguồn nhiệt."),
  ("wastewater", "/ˈweɪstwɔːtə/", "n", "nước thải", "Never pour chemicals into the <b>wastewater</b> drain.", "Không bao giờ đổ hoá chất xuống cống nước thải.", "排水", "haisui"),
  ("recycle", "/ˌriːˈsaɪkl/", "v", "tái chế", "We <b>recycle</b> all plastic trays.", "Nhà máy mình tái chế toàn bộ khay nhựa.", "リサイクルする", "risaikuru suru"),
 ],
 "phrases": [
  ("Please label every chemical container.", "Mọi bình chứa hoá chất đều phải dán nhãn."),
  ("Where is the safety data sheet for this solvent?", "Phiếu an toàn của dung môi này để ở đâu?"),
  ("Put oily rags in the red bin, not the normal trash.", "Giẻ dính dầu bỏ vào thùng đỏ, không bỏ vào thùng rác thường."),
  ("There's a small spill near the paint room.", "Có chỗ tràn đổ nhỏ gần phòng sơn."),
  ("Turn on the fan before you open the solvent.", "Bật quạt hút trước khi mở dung môi."),
  ("Keep the lid closed when you're not using it.", "Không dùng thì đậy nắp lại."),
  ("Don't pour anything into the drain.", "Không đổ bất cứ thứ gì xuống cống."),
  ("We separate waste into three types.", "Mình phân loại rác thành ba loại."),
  ("If a chemical gets in your eyes, rinse them with water for 15 minutes and see the nurse.", "Nếu hoá chất bắn vào mắt, rửa mắt bằng nước sạch 15 phút rồi đến gặp y tá."),
 ],
 "dialogues": [
  ("There's some solvent on the floor near Station 6.", [
    ("Thanks. Let's keep people away, open the windows and use the spill kit. I'll tell the EHS team.", True, "Cách ly khu vực + thông gió + dùng đúng dụng cụ + báo bộ phận EHS."),
    ("Use water wash it away.", False, "Thiếu 'to' ('use water to wash') và sai cách: dội nước làm dung môi lan xuống cống."),
    ("Small only, no need.", False, "Coi nhẹ — dung môi vừa dễ cháy vừa độc, tràn ít cũng phải xử lý."),
  ]),
  ("Where should I throw these oily gloves?", [
    ("In the red bin for hazardous waste. Don't put them in the normal trash.", True, "Chỉ đúng thùng + nhắc phân loại."),
    ("Throw anywhere.", False, "Sai quy định phân loại chất thải nguy hại."),
    ("In trash normal.", False, "Sai trật tự từ kiểu tiếng Việt ('normal trash') và sai quy định."),
  ]),
  ("Do I need a respirator to mix this paint?", [
    ("Yes. The safety data sheet says so. Please also turn on the ventilation fan.", True, "Trả lời + căn cứ SDS + nhắc thông gió."),
    ("No need. The smell is not strong.", False, "Nguy hiểm — không đánh giá độ độc bằng mùi, phải theo SDS."),
    ("Yes, you must wearing.", False, "Sau 'must' dùng động từ nguyên mẫu: 'You must wear one.'"),
  ]),
  ("Why can't we keep the solvent next to the oven?", [
    ("Because it's flammable. The heat from the oven can start a fire.", True, "Lý do rõ ràng, đúng thực tế."),
    ("Because the rule say.", False, "Sai chia động từ ('says') và không giải thích lý do."),
    ("The oven is expensive.", False, "Lạc đề — lý do thật là nguy cơ cháy."),
  ]),
  ("The environmental inspectors are coming next week. Are we ready?", [
    ("Mostly. The waste records are up to date, but I still need to relabel two chemical cabinets by Friday.", True, "Tình trạng + việc còn tồn + hạn chót."),
    ("Yes, 100 percent, no problem.", False, "Hứa suông khi chưa rà soát."),
    ("We will ready.", False, "Thiếu 'be' ('We will be ready') và không nói còn việc gì."),
  ]),
 ],
 "listen": [
  ("Please label every chemical container", ["label", "chemical"], "dán nhãn hoá chất"),
  ("Put oily rags in the red bin", ["oily", "red"], "phân loại rác nguy hại"),
  ("Turn on the fan before you open the solvent", ["fan", "solvent"], "thông gió"),
  ("Keep flammable liquids away from heat", ["flammable", "heat"], "chất dễ cháy"),
  ("There is a solvent spill near the paint room. Please keep away from the area. The EHS team is coming with a spill kit.", ["spill", "away", "kit"], "báo tràn đổ hoá chất"),
  ("From Monday, we will separate waste into three bins. Red is for hazardous waste. Blue is for plastic.", ["separate", "hazardous", "plastic"], "thông báo phân loại rác"),
 ],
})

# ───────────────────────── E. Tự động hoá, robot & PLC ─────────────────────────
PHASES.append({
 "title": "Tự động hoá, robot & PLC",
 "vocab": [
  ("PLC", "/ˌpiː el ˈsiː/", "n", "bộ điều khiển lập trình (PLC)", "The <b>PLC</b> controls the whole line.", "PLC điều khiển cả chuyền."),
  ("robot arm", "/ˈrəʊbɒt ˌɑːm/", "n", "cánh tay robot", "The <b>robot arm</b> picks up the part and puts it on the conveyor.", "Cánh tay robot gắp linh kiện và đặt lên băng tải."),
  ("conveyor", "/kənˈveɪə/", "n", "băng tải", "The <b>conveyor</b> stopped because a box got stuck.", "Băng tải dừng vì một thùng bị kẹt.", "コンベア", "konbea"),
  ("emergency stop", "/ɪˌmɜːdʒənsi ˈstɒp/", "n", "nút dừng khẩn cấp (E-stop)", "Press the <b>emergency stop</b> if anything goes wrong.", "Có gì bất thường thì nhấn nút dừng khẩn cấp.", "非常停止", "hijō teishi"),
  ("teach pendant", "/ˈtiːtʃ ˌpendənt/", "n", "tay dạy robot (teach pendant)", "Only trained staff can use the <b>teach pendant</b>.", "Chỉ người đã được đào tạo mới được dùng tay dạy robot.", "ティーチングペンダント", "tīchingu pendanto"),
  ("parameter", "/pəˈræmɪtə/", "n", "thông số cài đặt", "Don't change any <b>parameter</b> without approval.", "Không được đổi thông số nào khi chưa được duyệt.", "パラメータ", "paramēta"),
  ("manual mode", "/ˈmænjuəl ˌməʊd/", "n", "chế độ chạy tay", "Switch to <b>manual mode</b> before you move the robot.", "Chuyển sang chế độ tay trước khi di chuyển robot.", "手動モード", "shudō mōdo"),
  ("reset", "/ˌriːˈset/", "v", "đặt lại, xoá báo lỗi (reset)", "Find the cause before you <b>reset</b> the alarm.", "Tìm ra nguyên nhân rồi mới reset báo lỗi."),
  ("light curtain", "/ˈlaɪt ˌkɜːtn/", "n", "màn chắn sáng an toàn", "The robot stops when someone breaks the <b>light curtain</b>.", "Robot dừng khi có người cắt qua màn chắn sáng.", "ライトカーテン", "raito kāten"),
  ("interlock", "/ˈɪntəlɒk/", "n", "khoá liên động (an toàn)", "Never bypass the door <b>interlock</b>.", "Không bao giờ được vô hiệu hoá khoá liên động của cửa.", "インターロック", "intārokku"),
 ],
 "phrases": [
  ("The robot stopped with an error on the screen.", "Robot dừng và báo lỗi trên màn hình."),
  ("Please switch to manual mode first.", "Chuyển sang chế độ tay trước nhé."),
  ("Press the emergency stop if you see a problem.", "Thấy có vấn đề thì nhấn nút dừng khẩn cấp."),
  ("Don't enter the robot cell while it's in auto mode.", "Không vào vùng làm việc của robot khi robot đang chạy tự động."),
  ("Who changed the parameters on Machine 7?", "Ai đã đổi thông số ở máy 7?"),
  ("Please write down the error code before you reset.", "Ghi lại mã lỗi trước khi reset nhé."),
  ("The conveyor is running too fast for Station 2.", "Băng tải chạy nhanh quá so với công đoạn 2."),
  ("The light curtain is dirty, so the robot keeps stopping.", "Màn chắn sáng bị bẩn nên robot cứ dừng liên tục."),
  ("We need to back up the PLC program first.", "Cần sao lưu chương trình PLC trước."),
 ],
 "dialogues": [
  ("The robot keeps stopping. Can we turn off the light curtain?", [
    ("No, we can't. It protects people. Let's clean it and check the alignment instead.", True, "Từ chối dứt khoát + lý do an toàn + cách xử lý đúng."),
    ("OK, turn off for one hour only.", False, "Tắt thiết bị an toàn dù chỉ một giờ cũng cực kỳ nguy hiểm."),
    ("Robot is stupid.", False, "Thiếu 'The', chỉ than phiền mà không xử lý."),
  ]),
  ("The conveyor stopped. What happened?", [
    ("A carton got stuck at the end. I pressed the emergency stop and removed it. We're restarting now.", True, "Nguyên nhân + đã làm gì + tình trạng hiện tại."),
    ("It stop, I don't know.", False, "Sai thì ('stopped') và không tìm hiểu nguyên nhân."),
    ("Conveyor is old machine.", False, "Thiếu mạo từ và đoán nguyên nhân khi chưa kiểm tra."),
  ]),
  ("Can I reset the alarm now?", [
    ("Please write down the error code first and tell me what you saw. Then we can reset it.", True, "Ghi mã lỗi + tìm hiểu trước khi reset."),
    ("Yes, reset many times until it runs.", False, "Reset liên tục che mất nguyên nhân, có thể làm hỏng máy."),
    ("You can resetting.", False, "Sau 'can' dùng động từ nguyên mẫu: 'You can reset it.'"),
  ]),
  ("Who changed the speed parameter on Line 5?", [
    ("I did, yesterday afternoon. The engineer approved it, and it's in the change record.", True, "Nhận trách nhiệm + đã được duyệt + có hồ sơ."),
    ("Not me, maybe the night shift.", False, "Né tránh, đổ cho ca khác mà không kiểm tra hồ sơ."),
    ("I change for faster.", False, "Sai thì ('changed') và thiếu ý ('to make it faster'); đổi thông số phải được duyệt."),
  ]),
  ("I need to go inside the robot cell to fix a part.", [
    ("OK. First switch to manual mode, lock out the power and take the key with you.", True, "Đúng trình tự an toàn trước khi vào vùng robot."),
    ("Go fast. The robot is slow.", False, "Nguy hiểm — không bao giờ vào vùng robot khi đang chạy tự động."),
    ("Robot cell is danger.", False, "Dùng sai từ ('dangerous') và không hướng dẫn gì cụ thể."),
  ]),
 ],
 "listen": [
  ("Please switch the robot to manual mode", ["switch", "manual"], "chuyển chế độ tay"),
  ("Press the emergency stop if you see a problem", ["emergency", "problem"], "nút dừng khẩn cấp"),
  ("Write down the error code before you reset", ["error", "reset"], "ghi mã lỗi"),
  ("Never bypass the door interlock", ["bypass", "interlock"], "khoá liên động"),
  ("The robot on Line four stopped again. The light curtain was dirty. We cleaned it, and the robot is running now.", ["again", "dirty", "running"], "báo robot dừng"),
  ("We will update the PLC program on Saturday. Please do not change any parameters this week. Call me if you see an alarm.", ["update", "parameters", "alarm"], "thông báo cập nhật PLC"),
 ],
})

# ───────────────────────── F. Năng suất, OEE & KPI ca ─────────────────────────
PHASES.append({
 "title": "Năng suất, OEE & KPI ca",
 "vocab": [
  ("OEE", "/ˌəʊ iː ˈiː/", "n", "hiệu suất thiết bị tổng thể (OEE)", "Our <b>OEE</b> this month is 78 percent.", "OEE tháng này của mình là 78%.", "設備総合効率", "setsubi sōgō kōritsu"),
  ("availability", "/əˌveɪləˈbɪləti/", "n", "tỉ lệ thời gian máy chạy (một thành phần của OEE)", "Long changeovers lower our <b>availability</b>.", "Chuyển đổi mã hàng lâu làm giảm tỉ lệ thời gian máy chạy.", "時間稼働率", "jikan kadōritsu"),
  ("performance", "/pəˈfɔːməns/", "n", "hiệu suất tốc độ (một thành phần của OEE)", "Small stops hurt our <b>performance</b>.", "Những lần dừng ngắn làm giảm hiệu suất tốc độ.", "性能稼働率", "seinō kadōritsu"),
  ("productivity", "/ˌprɒdʌkˈtɪvəti/", "n", "năng suất lao động", "<b>Productivity</b> went up 6 percent after the kaizen.", "Năng suất tăng 6% sau cải tiến.", "生産性", "seisansei"),
  ("KPI", "/ˌkeɪ piː ˈaɪ/", "n", "chỉ số đánh giá hiệu quả (KPI)", "Our main <b>KPIs</b> are output, yield and OEE.", "Các KPI chính của tổ là sản lượng, tỉ lệ đạt và OEE."),
  ("takt time", "/ˈtɑːkt ˌtaɪm/", "n", "nhịp sản xuất theo nhu cầu khách hàng (takt time)", "The <b>takt time</b> is 50 seconds, but our cycle time is 55.", "Takt time là 50 giây, nhưng thời gian chu kỳ của mình là 55 giây.", "タクトタイム", "takuto taimu"),
  ("scrap", "/skræp/", "n", "phế phẩm (hàng phải huỷ)", "We had 30 kilograms of <b>scrap</b> today.", "Hôm nay có 30 ký phế phẩm."),
  ("rework", "/ˌriːˈwɜːk/", "n/v", "sửa lại hàng lỗi; làm lại", "These ten pieces need <b>rework</b>.", "Mười cái này cần sửa lại.", "手直し", "tenaoshi"),
  ("man-hour", "/ˈmæn ˌaʊə/", "n", "giờ công", "This job takes 12 <b>man-hours</b>.", "Việc này mất 12 giờ công.", "工数", "kōsū"),
  ("trend", "/trend/", "n", "xu hướng", "The <b>trend</b> is getting better every week.", "Xu hướng đang tốt lên từng tuần."),
 ],
 "phrases": [
  ("Our OEE today is 81 percent, up from 76.", "OEE hôm nay là 81%, tăng từ 76%."),
  ("Availability is low because of the long changeover.", "Tỉ lệ máy chạy thấp do chuyển đổi mã hàng lâu."),
  ("We had many small stops on Machine 2.", "Máy 2 bị dừng ngắn nhiều lần."),
  ("Our cycle time is longer than the takt time.", "Thời gian chu kỳ đang dài hơn takt time."),
  ("Scrap went down to 0.5 percent this week.", "Tuần này phế phẩm giảm xuống 0,5%."),
  ("Twenty pieces are waiting for rework.", "Hai mươi cái đang chờ sửa lại."),
  ("Let's look at the trend for the last four weeks.", "Mình xem xu hướng bốn tuần qua nhé."),
  ("We met three out of four KPIs this month.", "Tháng này mình đạt ba trên bốn KPI."),
  ("Units per man-hour went up from 12 to 14.", "Số sản phẩm trên mỗi giờ công tăng từ 12 lên 14."),
 ],
 "dialogues": [
  ("Why is the OEE so low today?", [
    ("Mainly availability. We lost 50 minutes on a changeover and 20 minutes on a sensor alarm.", True, "Chỉ ra thành phần OEE bị thấp + số phút mất cụ thể."),
    ("Because workers not hard working.", False, "Thiếu 'are' và đổ lỗi cho người thay vì phân tích tổn thất."),
    ("OEE is low, yes.", False, "Chỉ lặp lại, không giải thích nguyên nhân."),
  ]),
  ("What's the difference between cycle time and takt time?", [
    ("Takt time is the pace the customer needs. Cycle time is how long we actually take to make one piece.", True, "Giải thích đúng và gọn hai khái niệm."),
    ("They are same thing.", False, "Sai khái niệm và thiếu 'the' ('the same')."),
    ("Takt time is Japanese word.", False, "Không giải thích nội dung, thiếu mạo từ (thực ra 'takt' gốc tiếng Đức)."),
  ]),
  ("How much scrap did we have this week?", [
    ("About 45 kilograms, or 0.8 percent. Most of it came from the Monday start-up.", True, "Con số + tỉ lệ + nguồn phát sinh chính."),
    ("Scrap have a lot.", False, "Sai ngữ pháp ('There was a lot of scrap') và không có số."),
    ("I throw it already.", False, "Sai thì ('I've thrown it away') và lạc đề — người hỏi cần số liệu."),
  ]),
  ("Can we rework these parts, or should we scrap them?", [
    ("We can rework them. It's only a label problem, and QC has agreed.", True, "Quyết định + lý do + đã có QC đồng ý."),
    ("Scrap all, faster.", False, "Cộc lốc và lãng phí — huỷ hàng còn sửa được làm tăng chi phí."),
    ("Rework is can.", False, "Dịch từng chữ 'sửa được': 'We can rework them.'"),
  ]),
  ("Did your line meet its KPIs this month?", [
    ("Three out of four. Output and yield were on target, but OEE was 3 points below.", True, "Tổng kết + chỉ rõ KPI nào chưa đạt và thiếu bao nhiêu."),
    ("Almost meet.", False, "Thiếu chủ ngữ và sai thì ('We almost met them'), lại không có số."),
    ("KPI is not fair.", False, "Than phiền thay vì báo cáo kết quả."),
  ]),
 ],
 "listen": [
  ("Our OEE today is eighty-one percent", ["OEE", "percent"], "báo OEE"),
  ("Availability is low because of the changeover", ["Availability", "changeover"], "nguyên nhân OEE thấp"),
  ("Twenty pieces are waiting for rework", ["Twenty", "rework"], "hàng chờ sửa"),
  ("Our cycle time is longer than the takt time", ["longer", "takt"], "so sánh nhịp"),
  ("This week our OEE went up to eighty percent. Scrap went down by half. Great job, everyone.", ["week", "Scrap", "half"], "tổng kết tuần"),
  ("Machine two had many small stops. Each stop was short, but together we lost forty minutes. Please clean the feeder every hour.", ["small", "together", "feeder"], "phân tích dừng ngắn"),
 ],
})

# ───────────────────────── G. Giao ca & quản lý tổ ─────────────────────────
PHASES.append({
 "title": "Giao ca & quản lý tổ",
 "vocab": [
  ("handover", "/ˈhændəʊvə/", "n", "sự bàn giao (ca, công việc)", "The shift <b>handover</b> takes ten minutes.", "Giao ca mất mười phút.", "引き継ぎ", "hikitsugi"),
  ("attendance", "/əˈtendəns/", "n", "sự có mặt, chấm công", "Please check <b>attendance</b> before we start.", "Kiểm tra quân số trước khi bắt đầu nhé.", "勤怠", "kintai"),
  ("overtime", "/ˈəʊvətaɪm/", "n", "tăng ca, làm thêm giờ", "We need two hours of <b>overtime</b> on Friday.", "Thứ Sáu cần tăng ca hai tiếng.", "残業", "zangyō"),
  ("absent", "/ˈæbsənt/", "adj", "vắng mặt", "Three workers are <b>absent</b> today.", "Hôm nay ba công nhân vắng mặt."),
  ("assign", "/əˈsaɪn/", "v", "phân công", "I'll <b>assign</b> Mai to Station 4 today.", "Hôm nay tôi phân công Mai sang công đoạn 4."),
  ("morning meeting", "/ˌmɔːnɪŋ ˈmiːtɪŋ/", "n", "họp đầu ca (chào ca buổi sáng)", "At the <b>morning meeting</b>, we share the target and a safety point.", "Trong buổi họp đầu ca, tổ chia sẻ chỉ tiêu và một điểm an toàn.", "朝礼", "chōrei"),
  ("logbook", "/ˈlɒɡbʊk/", "n", "sổ nhật ký, sổ giao ca", "Write every problem in the <b>logbook</b>.", "Ghi mọi vấn đề vào sổ giao ca."),
  ("rotation", "/rəʊˈteɪʃn/", "n", "luân chuyển vị trí làm việc", "Job <b>rotation</b> helps workers learn more stations.", "Luân chuyển vị trí giúp công nhân làm được nhiều công đoạn hơn.", "ローテーション", "rōtēshon"),
  ("motivate", "/ˈməʊtɪveɪt/", "v", "tạo động lực", "Small rewards can <b>motivate</b> the team.", "Những phần thưởng nhỏ có thể tạo động lực cho cả tổ."),
  ("escalate", "/ˈeskəleɪt/", "v", "báo lên cấp trên (khi vượt khả năng xử lý)", "If you can't fix it in 30 minutes, <b>escalate</b> it to the supervisor.", "Nếu 30 phút không xử lý được thì báo lên giám sát."),
 ],
 "phrases": [
  ("Here's the handover for Line 2.", "Đây là nội dung giao ca của chuyền 2."),
  ("Everything is normal, except Machine 5.", "Mọi thứ bình thường, trừ máy 5."),
  ("Please read the logbook before you start.", "Đọc sổ giao ca trước khi bắt đầu nhé."),
  ("Two people are absent, so I moved Lan to Station 3.", "Hai người vắng nên tôi đã chuyển Lan sang công đoạn 3."),
  ("Can you stay for two hours of overtime tonight?", "Tối nay bạn ở lại tăng ca hai tiếng được không?"),
  ("Let's start the morning meeting.", "Mình bắt đầu họp đầu ca nhé."),
  ("Thanks for your hard work today, everyone.", "Cảm ơn mọi người hôm nay đã vất vả."),
  ("If it's not fixed in 30 minutes, please call me.", "Nếu 30 phút chưa xong thì gọi tôi."),
  ("Next week we'll rotate people between Stations 1 and 2.", "Tuần sau mình luân chuyển người giữa công đoạn 1 và 2."),
 ],
 "dialogues": [
  ("Anything I should know before I take over?", [
    ("Yes, two things. Machine 5 had a sensor alarm at four, and Lot 88 is on hold. It's all in the logbook.", True, "Giao ca gọn: nói có mấy việc + từng việc + chỉ chỗ đã ghi."),
    ("No, everything OK.", False, "Thiếu 'is' và giấu thông tin — ca sau dễ gặp lại sự cố."),
    ("Machine 5 is problem.", False, "Dùng sai ('has a problem') và không nói rõ chuyện gì."),
  ]),
  ("Three people are absent today. What's your plan?", [
    ("I'll move two multi-skilled workers from Line 4 and do 30 minutes of overtime to hit the target.", True, "Phương án cụ thể + gắn với chỉ tiêu."),
    ("We will try, no plan.", False, "Không có phương án — tổ trưởng phải chủ động."),
    ("Three people absent, very tired.", False, "Thiếu động từ, chỉ than phiền."),
  ]),
  ("I can't do overtime tonight. My child is sick.", [
    ("I understand. Please take care of your child. I'll ask someone else.", True, "Thông cảm + tự tìm người khác, không gây áp lực."),
    ("You must stay. No excuse.", False, "Ép buộc — tăng ca phải có sự đồng ý của người lao động."),
    ("Why you not tell me before?", False, "Sai trật tự câu hỏi ('Why didn't you tell me earlier?') và trách móc."),
  ]),
  ("The machine is still down after an hour. What should I do?", [
    ("Please escalate it to the supervisor now, and tell planning we'll be behind.", True, "Báo lên đúng lúc + báo bộ phận liên quan."),
    ("Wait more, maybe it runs.", False, "Chờ thụ động — quá thời gian quy định thì phải báo cấp trên."),
    ("I will fixing it myself.", False, "Sai ngữ pháp ('I'll fix it') và tự sửa khi không có chuyên môn là nguy hiểm."),
  ]),
  ("The team looks tired this week.", [
    ("You're right. We've had a lot of overtime. I'll give them a longer break and thank them at the morning meeting.", True, "Đồng cảm + hành động cụ thể để động viên."),
    ("Tired is normal in factory.", False, "Thiếu chủ ngữ/mạo từ và bỏ qua sức khoẻ người lao động."),
    ("They are lazy.", False, "Quy chụp, không tìm hiểu nguyên nhân."),
  ]),
 ],
 "listen": [
  ("Please read the logbook before you start", ["logbook", "start"], "đọc sổ giao ca"),
  ("Two people are absent today", ["Two", "absent"], "báo quân số"),
  ("Can you stay for two hours of overtime", ["stay", "overtime"], "hỏi tăng ca"),
  ("Let's start the morning meeting now", ["start", "meeting"], "bắt đầu họp đầu ca"),
  ("Here is my handover. Machine five had an alarm at four o'clock. Lot eighty-eight is still on hold.", ["handover", "alarm", "hold"], "giao ca cuối ngày"),
  ("Good morning, everyone. Our target today is nine hundred pieces. Mai will work at Station three because Tú is absent.", ["morning", "target", "absent"], "họp đầu ca"),
 ],
})

# ───────────────────────── H. Sự cố khẩn cấp: cháy, rò rỉ, sơ tán ─────────────────────────
PHASES.append({
 "title": "Sự cố khẩn cấp: cháy, rò rỉ, sơ tán",
 "vocab": [
  ("evacuate", "/ɪˈvækjueɪt/", "v", "sơ tán", "Everyone must <b>evacuate</b> when the alarm rings.", "Khi chuông báo vang, mọi người phải sơ tán.", "避難する", "hinan suru"),
  ("assembly point", "/əˈsembli ˌpɔɪnt/", "n", "điểm tập trung (khi sơ tán)", "Our <b>assembly point</b> is the parking area.", "Điểm tập trung của mình là bãi xe.", "集合場所", "shūgō basho"),
  ("fire alarm", "/ˈfaɪər əˌlɑːm/", "n", "chuông/nút báo cháy", "If you see a fire, push the <b>fire alarm</b> button.", "Nếu thấy cháy, nhấn nút báo cháy.", "火災報知器", "kasai hōchiki"),
  ("smoke", "/sməʊk/", "n", "khói", "There's <b>smoke</b> coming from the panel.", "Có khói bốc ra từ tủ điện.", "煙", "kemuri"),
  ("gas leak", "/ˈɡæs ˌliːk/", "n", "rò rỉ khí gas", "If you smell a <b>gas leak</b>, leave the area and call security.", "Nếu ngửi thấy mùi gas rò rỉ, rời khỏi khu vực và gọi bảo vệ.", "ガス漏れ", "gasu more"),
  ("headcount", "/ˈhedkaʊnt/", "n", "điểm danh quân số", "Leaders do a <b>headcount</b> at the assembly point.", "Tổ trưởng điểm danh quân số tại điểm tập trung.", "点呼", "tenko"),
  ("power outage", "/ˈpaʊər ˌaʊtɪdʒ/", "n", "sự cố mất điện", "The <b>power outage</b> stopped all lines for 20 minutes.", "Mất điện làm tất cả các chuyền dừng 20 phút.", "停電", "teiden"),
  ("stairs", "/steəz/", "n", "cầu thang bộ", "Use the <b>stairs</b>, not the lift, during a fire.", "Khi có cháy, đi cầu thang bộ, không đi thang máy.", "階段", "kaidan"),
  ("fire drill", "/ˈfaɪə ˌdrɪl/", "n", "buổi diễn tập phòng cháy chữa cháy", "We have a <b>fire drill</b> twice a year.", "Mỗi năm mình diễn tập PCCC hai lần.", "消防訓練", "shōbō kunren"),
  ("fire warden", "/ˈfaɪə ˌwɔːdn/", "n", "người phụ trách PCCC và sơ tán của khu vực", "The <b>fire warden</b> checks that nobody is left inside.", "Người phụ trách PCCC khu vực kiểm tra để chắc không còn ai bên trong."),
 ],
 "phrases": [
  ("Fire! Stop work and leave the building now.", "Cháy! Dừng việc và ra khỏi toà nhà ngay."),
  ("Don't run. Walk quickly to the nearest exit.", "Đừng chạy. Đi nhanh tới lối thoát gần nhất."),
  ("Use the stairs. Don't use the lift.", "Đi cầu thang bộ. Không dùng thang máy."),
  ("Go to the assembly point in the parking area.", "Đến điểm tập trung ở bãi xe."),
  ("Is everyone here? Let's do a headcount.", "Đủ người chưa? Mình điểm danh nhé."),
  ("Two people are missing from Line 3.", "Chuyền 3 còn thiếu hai người."),
  ("I smell gas near the kitchen.", "Tôi ngửi thấy mùi gas gần bếp."),
  ("Don't go back inside until the fire warden says it's safe.", "Không quay lại bên trong cho đến khi người phụ trách PCCC báo an toàn."),
  ("There's a power outage. Please stay at your station.", "Đang mất điện. Mọi người ở yên tại vị trí."),
  ("Please call 114 and tell security.", "Gọi 114 và báo cho bảo vệ."),
 ],
 "dialogues": [
  ("I see smoke coming from the electrical panel!", [
    ("Push the fire alarm and move away. I'll call security and 114.", True, "Báo động + tránh xa + gọi hỗ trợ — đúng thứ tự ưu tiên."),
    ("Throw water on it quickly.", False, "Rất nguy hiểm — không dùng nước dập đám cháy điện."),
    ("Smoke from where?", False, "Hỏi lại khi thông tin đã rõ — lúc khẩn cấp phải hành động ngay."),
  ]),
  ("The fire alarm is ringing. Should I finish this box first?", [
    ("No. Stop now and go to the assembly point. Leave the box.", True, "Dứt khoát: bỏ việc, sơ tán ngay."),
    ("Yes, finish quick then go.", False, "Sai về an toàn — có báo cháy thì không được làm tiếp."),
    ("Maybe is only drill.", False, "Thiếu chủ ngữ và mạo từ ('Maybe it's only a drill'), lại coi nhẹ — luôn sơ tán như thật."),
  ]),
  ("Is everyone from Line 3 here?", [
    ("No, two are missing: Hoà and Bình. I've told the fire warden.", True, "Trả lời + tên người thiếu + đã báo người phụ trách."),
    ("I think all here.", False, "Thiếu động từ ('everyone is here') và không điểm danh thật."),
    ("I will go inside and find them.", False, "Tự quay vào là nguy hiểm — báo người phụ trách để đội cứu hộ xử lý."),
  ]),
  ("I smell gas near the canteen kitchen.", [
    ("Don't switch anything on or off. Let's move everyone out and call security now.", True, "Không tạo tia lửa + sơ tán + báo bảo vệ — đúng quy tắc khi rò gas."),
    ("Turn on the light and check.", False, "Nguy hiểm — bật công tắc điện khi rò gas có thể gây nổ."),
    ("Smell is normal, cooking time.", False, "Chủ quan và thiếu động từ — có mùi gas phải xử lý ngay."),
  ]),
  ("There's a power outage. What should the operators do?", [
    ("Stay at their stations, turn their machine switches off and wait for instructions.", True, "Hướng dẫn rõ: ở yên, tắt công tắc máy để máy không tự chạy lại, chờ chỉ thị."),
    ("They go home.", False, "Sai quy trình — bỏ vị trí khi chưa có chỉ thị."),
    ("Electricity no have.", False, "Dịch từng chữ 'không có điện' và không trả lời cần làm gì."),
  ]),
 ],
 "listen": [
  ("Stop work and leave the building now", ["leave", "building"], "lệnh sơ tán"),
  ("Use the stairs and do not use the lift", ["stairs", "lift"], "cách sơ tán"),
  ("Please go to the assembly point", ["assembly", "point"], "điểm tập trung"),
  ("Two people from Line three are missing", ["people", "missing"], "báo thiếu người"),
  ("There is smoke in the paint room. Everyone in Building B, please evacuate now. Use the stairs on the east side.", ["smoke", "evacuate", "east"], "thông báo sơ tán thật"),
  ("All workers are at the assembly point. The fire warden checked the building. Nobody is inside.", ["workers", "checked", "inside"], "báo cáo sau sơ tán"),
 ],
})


EXTRA = {
 "phases": PHASES,
 "rev": [
  ("Bản vẽ này là phiên bản cũ.", "This drawing is an old revision."),
  ("Số đo này vượt giới hạn trên.", "This measurement is over the upper limit."),
  ("Vật tư sẽ về trễ hai ngày.", "The material will arrive two days late."),
  ("Lô thép này không có chứng chỉ vật liệu.", "This steel lot has no material certificate."),
  ("Mỗi thùng đóng năm mươi cái.", "Pack fifty pieces in each carton."),
  ("Xuất hàng cũ trước nhé.", "Please ship the old stock first."),
  ("Hai thùng bị thiếu nhãn.", "Two cartons are missing labels."),
  ("Giẻ dính dầu bỏ vào thùng đỏ.", "Put oily rags in the red bin."),
  ("Đậy nắp can dung môi lại.", "Please close the solvent can."),
  ("Chuyển robot sang chế độ tay trước.", "Switch the robot to manual mode first."),
  ("Ghi lại mã lỗi trước khi reset.", "Write down the error code before you reset."),
  ("OEE hôm nay là 80%.", "Today's OEE is 80 percent."),
  ("Hai mươi cái đang chờ sửa lại.", "Twenty pieces are waiting for rework."),
  ("Hôm nay ba người vắng mặt.", "Three people are absent today."),
  ("Đọc sổ giao ca trước khi bắt đầu.", "Read the logbook before you start."),
  ("Đi cầu thang bộ, không đi thang máy.", "Use the stairs, not the lift."),
 ],
 "reading": [
  {"t": "Drawing change notice", "text": "DRAWING CHANGE NOTICE\nPart: Bracket B-210\nOld: Rev. C – hole diameter 8.0 mm\nNew: Rev. D – hole diameter 8.2 mm (±0.05)\nEffective: from Lot 2410 (Oct 3)\nPlease remove all Rev. C drawings from the line and return them to Engineering.", "q": [
    {"q": "What changed in Rev. D?", "o": ["The hole diameter", "The part name", "The material"], "a": 0},
    {"q": "What should the line do with the Rev. C drawings?", "o": ["Keep them for reference", "Return them to Engineering", "Send them to the customer"], "a": 1}]},
  {"t": "Supplier quotation", "text": "Dear Purchasing team,\nThank you for your request. Our price for PP resin (grade H-30) is USD 1.45/kg.\nMinimum order quantity: 1,000 kg\nDelivery: 3 weeks after PO\nThis quotation is valid until 31 October.\nBest regards,\nSales Department", "q": [
    {"q": "What is the minimum order?", "o": ["3 tons", "145 kg", "1,000 kg"], "a": 2},
    {"q": "When will the resin arrive after the PO?", "o": ["In 3 weeks", "On 31 October", "In 3 days"], "a": 0}]},
  {"t": "Shift handover log", "text": "Line 4 – Night → Day, 6:00\n• Output: 870 / 900\n• Machine 5: sensor alarm at 3:10, cleaned, OK now\n• Lot 88: on hold (QC to check the label printing)\n• Absent: 1 (Tú)\nDay shift: please watch Machine 5 and ask QC about Lot 88 before 9:00.", "q": [
    {"q": "Why is Lot 88 on hold?", "o": ["A label printing problem", "A sensor alarm", "It is 30 units short"], "a": 0},
    {"q": "What should the day shift do before 9:00?", "o": ["Ship Lot 88", "Replace the sensor", "Ask QC about Lot 88"], "a": 2}]},
  {"t": "Chemical storage rules", "text": "CHEMICAL STORAGE – PAINT ROOM\n1. Keep flammable liquids in the yellow cabinet only.\n2. Close every container after use.\n3. Every container must have a label and an SDS.\n4. Put oily rags and empty cans in the red hazardous waste bin.\nSpill? Use the spill kit and call EHS (ext. 205).", "q": [
    {"q": "Where should flammable liquids be kept?", "o": ["Next to the oven", "In the red bin", "In the yellow cabinet"], "a": 2},
    {"q": "What should you do after a spill?", "o": ["Wash it into the drain", "Use the spill kit and call EHS", "Open a new container"], "a": 1}]},
  {"t": "Fire drill notice", "text": "FIRE DRILL – Thursday, 14:00\nWhen the alarm rings, stop work and switch off your machine if it is safe to do so. Leave by the nearest exit — do not use the lift.\nAssembly point: Parking Area C\nLeaders must report a headcount to the fire warden within 5 minutes.", "q": [
    {"q": "Where is the assembly point?", "o": ["Parking Area C", "The canteen", "The main gate"], "a": 0},
    {"q": "What must leaders do?", "o": ["Call the fire station", "Report a headcount to the fire warden", "Turn off the fire alarm"], "a": 1}]},
 ],
 "ai": [
  ("drawing", "Hỏi về bản vẽ mới", "You are a Japanese design engineer. You sent a new drawing revision to our factory. I am the production engineer and I have questions. Explain the changes simply and answer my questions about dimensions and tolerances."),
  ("iqc", "Báo nhà cung cấp hàng không đạt", "You are a salesperson from a material supplier. I call because your resin failed our incoming inspection. Apologize, ask for the details and agree with me on what to do with the lot."),
  ("handover", "Giao ca cho ca sau", "You are the leader of the next shift. I am giving you my shift handover. Ask about output, machine problems, lots on hold and anything you need to watch."),
  ("robot", "Robot dừng liên tục", "You are a service engineer from a foreign robot maker. Our robot keeps stopping with an alarm. Ask me for the error code, what the operator saw and what we have checked. Remind me about safety."),
 ],
 "events": [
  ("drill", "Diễn tập PCCC toàn nhà máy", "You are the factory's safety manager. We have a big fire drill next week. Ask me about my team's evacuation route, the assembly point and how I will do the headcount."),
  ("newline", "Lắp đặt dây chuyền/robot mới", "You are a foreign engineer coming to install a new automated line next month. Ask me about the space, the power supply, the team for training and the safety rules."),
  ("kpi_review", "Họp đánh giá KPI tháng", "You are the plant manager at the monthly KPI review. Ask me about my line's OEE, scrap and overtime, and ask for one action to improve next month."),
 ],
 "quips": [
  "Rev. D only, please!",
  "Measure twice, cut once!",
  "FIFO: old stock first!",
  "E-stop? I know where it is!",
  "OEE up, scrap down!",
  "Handover done, see you tomorrow!",
 ],
 "roles": {
  "qc": {
   "scenarios": [
    ("qc_iqc", "Từ chối lô vật tư", "You are a supplier's quality engineer. I am from IQC, and our incoming inspection rejected your lot. Ask what we found, how many samples failed and what we need from you."),
    ("qc_drawing", "Hỏi khách về bản vẽ", "You are the customer's design engineer. I am QC, and one tolerance on your new drawing is not clear. Answer my questions and confirm the correct value."),
   ],
   "dialogues": [
    ("Why did IQC reject our resin?", [
      ("The moisture was 0.35 percent, and our limit is 0.2. All five samples failed.", True, "Số đo + giới hạn + số mẫu không đạt — nói bằng dữ liệu."),
      ("Because it is not good quality.", False, "Mơ hồ — nhà cung cấp cần số đo cụ thể để xử lý."),
      ("Your resin is wet, you know that.", False, "Giọng trách móc, không đưa dữ liệu.")]),
    ("Is this drawing the latest revision?", [
      ("No, this is Rev. C. The latest is Rev. D from last week. I'll give you a new copy.", True, "Trả lời + thông tin đúng + đưa bản mới."),
      ("I think latest, maybe.", False, "Thiếu chủ ngữ/động từ và không chắc — phải tra danh mục bản vẽ rồi mới trả lời."),
      ("Drawing is drawing, same.", False, "Coi nhẹ phiên bản bản vẽ — nguồn gây lỗi hàng loạt.")]),
    ("Can we use this caliper? It's the only one left.", [
      ("Only if its calibration is still valid. Let me check the label and the record first.", True, "Điều kiện rõ + kiểm tra hồ sơ trước khi dùng."),
      ("Yes, use it. No time.", False, "Bỏ qua hiệu chuẩn vì vội — kết quả đo có thể sai."),
      ("It is only caliper, OK.", False, "Thiếu 'the' ('the only one') và không kiểm tra hiệu chuẩn.")]),
    ("The customer wants outgoing inspection data with every shipment. Can we do that?", [
      ("Yes. We'll attach the OQC report with the measurements to each packing list, starting next week.", True, "Đồng ý + cách làm + thời điểm bắt đầu."),
      ("Very difficult, too much work.", False, "Từ chối kiểu than phiền, không đưa phương án."),
      ("Yes, we do from before.", False, "Sai ngữ pháp ('We already do that') và không rõ ràng.")]),
   ]},
  "engineer": {
   "scenarios": [
    ("en_robot", "Hướng dẫn vận hành robot", "You are a new operator on a robot line. I am the engineer training you. Ask me what to do when the robot stops, when to press the emergency stop and whether you can enter the robot cell."),
    ("en_oee", "Giải thích OEE giảm", "You are the production manager. The OEE on my machines dropped from 82 to 70 percent. Ask me which part of OEE dropped, why, and what I will do."),
   ],
   "dialogues": [
    ("The robot program is gone after the power outage. Do we have a backup?", [
      ("Yes. I backed it up last Friday. I'll load it now and do a trial run before production.", True, "Có bản sao lưu + khôi phục + chạy thử trước khi sản xuất."),
      ("I think the PLC keeps it.", False, "Đoán mò — cần kiểm tra thực tế và dùng bản sao lưu."),
      ("No backup, program again.", False, "Thiếu chủ ngữ và cho thấy không có quy trình sao lưu.")]),
    ("Can you make the conveyor faster to increase output?", [
      ("We can, but Station 3 can't keep up. Let's balance Station 3 first, then increase the speed.", True, "Chỉ ra điểm nghẽn + đề xuất thứ tự hợp lý."),
      ("Yes, faster is better.", False, "Tăng tốc mà không xử lý điểm nghẽn chỉ gây ùn hàng và lỗi."),
      ("Conveyor cannot fast.", False, "Thiếu 'The' và động từ ('can't go faster'), lại không giải thích.")]),
    ("Why is the performance rate only 85 percent?", [
      ("We have many small stops at the feeder, about 40 a shift. I'm checking the part guide now.", True, "Nguyên nhân cụ thể + số lần + đang làm gì."),
      ("Because machine is slow.", False, "Thiếu 'the' và chưa phân tích nguyên nhân."),
      ("85 is good enough, I think.", False, "Né câu hỏi 'tại sao' — người hỏi cần nguyên nhân.")]),
    ("A worker says the light curtain doesn't stop the robot.", [
      ("Then stop the robot now and lock it out. Nobody can use it until I test the light curtain.", True, "Dừng ngay + khoá máy + kiểm tra — lỗi an toàn phải xử lý trước tiên."),
      ("Tell him be careful.", False, "Thiếu 'to' ('tell him to be careful') và coi nhẹ lỗi an toàn nghiêm trọng."),
      ("Maybe he test wrong.", False, "Sai thì ('tested') và nghi ngờ người báo thay vì kiểm tra.")]),
   ]},
  "leader": {
   "scenarios": [
    ("ld_handover", "Giao ca cho tổ trưởng ca sau", "You are the leader of the next shift. I am handing over my line to you. Ask about output, machine problems, absent workers and anything on hold."),
    ("ld_evac", "Báo cáo sau sơ tán", "You are the fire warden at the assembly point after a fire alarm. I am a line leader. Ask me for my headcount, who is missing and where they were working."),
   ],
   "dialogues": [
    ("How many people from your line are at the assembly point?", [
      ("Twenty-six out of twenty-seven. Tú is missing — he was at Station 5.", True, "Con số + người thiếu + vị trí cuối cùng để đội cứu hộ tìm."),
      ("Almost all, I think.", False, "Mơ hồ — khi sơ tán cần con số chính xác."),
      ("I don't count yet.", False, "Sai thì ('I haven't counted yet') và chậm trễ trong tình huống khẩn cấp.")]),
    ("Why didn't you write the alarm in the logbook?", [
      ("Sorry, I forgot. I'll add it now and remind the team at the morning meeting.", True, "Nhận lỗi + sửa ngay + phòng ngừa."),
      ("The alarm is small, not need.", False, "Sai ngữ pháp ('no need') và coi nhẹ việc ghi sổ giao ca."),
      ("I tell by mouth already.", False, "Sai thì ('I already told them') — nói miệng không thay được ghi sổ.")]),
    ("Can your team do overtime every day next week?", [
      ("Maybe three days, not every day. The team is tired. Could we get two temporary workers?", True, "Đưa giới hạn hợp lý + lý do + đề xuất phương án."),
      ("Yes, every day, no problem.", False, "Hứa ngay, không nghĩ đến sức khoẻ và giới hạn giờ tăng ca."),
      ("Team no want.", False, "Thiếu động từ ('The team doesn't want to') và cộc lốc.")]),
    ("Our scrap is up this week. What's happening?", [
      ("Most of it is from the new operator at Station 2. I'm retraining her today and checking her first ten pieces.", True, "Nguyên nhân + hành động cụ thể."),
      ("Scrap up because material bad.", False, "Thiếu động từ ('is up', 'is bad') và đoán nguyên nhân không có dữ liệu."),
      ("Not my line's fault.", False, "Đùn đẩy trách nhiệm.")]),
   ]},
  "planner": {
   "scenarios": [
    ("pl_quote", "Đàm phán báo giá", "You are a salesperson from a material supplier. You sent a quotation with a 7 percent price increase. I am the buyer. Explain the reason and negotiate the price, the MOQ and the delivery date."),
    ("pl_pack", "Khách đổi quy cách đóng gói", "You are a foreign customer's logistics manager. You want us to change the packing: fewer pieces per carton and a new label. Ask when we can start and if the cost will change."),
   ],
   "dialogues": [
    ("The supplier's new quotation is 7 percent higher. What do you think?", [
      ("It's too high. I'll ask them for a cost breakdown and compare it with two other quotations.", True, "Nhận định + đòi căn cứ + so sánh báo giá."),
      ("Price up is normal, accept.", False, "Chấp nhận ngay, không đàm phán."),
      ("Supplier is greedy.", False, "Cảm tính, thiếu mạo từ và không đưa hành động.")]),
    ("The MOQ is 2,000 kilograms, but we only need 800. What should we do?", [
      ("Let's ask if they can supply 1,000 this time, or combine it with next month's order.", True, "Đưa hai phương án thực tế."),
      ("Buy 2,000, keep in warehouse.", False, "Tồn kho thừa tốn chi phí, vật liệu có thể hết hạn."),
      ("We need 800 only, cannot.", False, "Cộc lốc, không có hướng xử lý.")]),
    ("Where should we put the finished goods for Friday's shipment?", [
      ("In Area B, near loading dock 2. I'll label the pallets by customer so loading is faster.", True, "Vị trí cụ thể + cách sắp xếp giúp bốc hàng nhanh."),
      ("Anywhere free.", False, "Mơ hồ — dễ lẫn hàng, xuất nhầm."),
      ("Put near door is OK.", False, "Thiếu 'them' và 'the', không chỉ rõ chỗ nào.")]),
    ("The customer wants 40 pieces per carton instead of 50. When can we start?", [
      ("From next Monday. We need three days to get the new cartons and print the new labels.", True, "Ngày bắt đầu + lý do cần thời gian chuẩn bị."),
      ("Start now, easy.", False, "Chưa có thùng, nhãn mới mà đã hứa ngay."),
      ("Why customer change?", False, "Sai trật tự câu hỏi ('Why did the customer change it?') và không trả lời.")]),
   ]},
 },
}
