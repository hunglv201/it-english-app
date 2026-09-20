# -*- coding: utf-8 -*-
# Gói "logistics" — Logistics · Xuất nhập khẩu: nhân viên chứng từ XNK, kho vận, forwarder / vận tải, mua hàng.
# Người học làm việc với nhà cung cấp, forwarder, hãng tàu và khách hàng nước ngoài. Tên công ty / cảng / tàu đều là tên tự đặt.
# Chặng lõi lấy từ office: 3 (Email công việc), 11 (Phỏng vấn & phát triển sự nghiệp).
# Schema: xem packs_src/README.md. Build: python3 packs_src/build.py logistics

PHASES = []

# ───────────────────────── 0. Báo giá cước & booking ─────────────────────────
PHASES.append({
 "title": "Báo giá cước & booking",
 "vocab": [
  ("freight", "/freɪt/", "n", "cước vận chuyển; hàng hoá vận chuyển", "The <b>freight</b> to Busan is 450 dollars per container.", "Cước đi Busan là 450 đô một container.", "運賃", "unchin"),
  ("booking", "/ˈbʊkɪŋ/", "n", "booking, đặt chỗ (trên tàu/máy bay)", "I've made a <b>booking</b> for two containers on next Friday's vessel.", "Tôi đã đặt booking hai container đi tàu thứ Sáu tuần sau."),
  ("forwarder", "/ˈfɔːwədə/", "n", "công ty giao nhận, forwarder", "Our <b>forwarder</b> will pick up the goods on Monday.", "Bên forwarder của mình sẽ lấy hàng vào thứ Hai.", "フォワーダー", "fowādā"),
  ("surcharge", "/ˈsɜːtʃɑːdʒ/", "n", "phụ phí", "The rate doesn't include the peak season <b>surcharge</b>.", "Giá cước này chưa gồm phụ phí mùa cao điểm.", "サーチャージ", "sāchāji"),
  ("container", "/kənˈteɪnə/", "n", "container, cont", "We need one 40-foot <b>container</b> for this order.", "Đơn này mình cần một container 40 feet.", "コンテナ", "kontena"),
  ("FCL", "/ˌef siː ˈel/", "n", "hàng nguyên container (FCL)", "This order is big enough to ship as <b>FCL</b>.", "Đơn này đủ lớn để đi hàng nguyên container."),
  ("LCL", "/ˌel siː ˈel/", "n", "hàng lẻ, hàng ghép container (LCL)", "Only three pallets? Then let's ship it <b>LCL</b>.", "Chỉ có ba pallet à? Vậy mình đi hàng lẻ nhé.", "混載貨物", "konsai kamotsu"),
  ("cut-off", "/ˈkʌt ɒf/", "n", "giờ cắt máng, hạn chót nhận hàng/chứng từ", "The <b>cut-off</b> for this vessel is Wednesday at noon.", "Giờ cắt máng của tàu này là trưa thứ Tư."),
  ("vessel", "/ˈvesl/", "n", "tàu (chở hàng)", "The <b>vessel</b> leaves Hai Phong on the 15th.", "Tàu rời Hải Phòng ngày 15.", "本船", "honsen"),
  ("space", "/speɪs/", "n", "chỗ (trên tàu), space", "There's no <b>space</b> left on this week's vessel.", "Tàu tuần này hết chỗ rồi."),
 ],
 "phrases": [
  ("Could you quote me a rate for one 40-foot container to Busan?", "Anh/chị báo giá giúp tôi cước một container 40 feet đi Busan được không?"),
  ("Does the rate include all local charges?", "Giá này đã gồm hết phí local chưa ạ?"),
  ("The rate is valid until the end of this month.", "Giá cước có hiệu lực đến cuối tháng này."),
  ("How long is the transit time to Tokyo?", "Thời gian vận chuyển đi Tokyo mất bao lâu ạ?"),
  ("I'd like to book space on the next vessel.", "Tôi muốn đặt chỗ trên chuyến tàu tới."),
  ("When is the cut-off for this vessel?", "Giờ cắt máng của tàu này là khi nào ạ?"),
  ("Please send me the booking confirmation today.", "Anh/chị gửi giúp tôi xác nhận booking trong hôm nay nhé."),
  ("It's only two pallets, so LCL is cheaper.", "Chỉ có hai pallet nên đi hàng lẻ sẽ rẻ hơn."),
  ("Is there a peak season surcharge this month?", "Tháng này có phụ phí mùa cao điểm không ạ?"),
  ("Can you give us a better rate for regular shipments?", "Nếu đi hàng đều thì bên anh/chị có giá tốt hơn không ạ?"),
 ],
 "dialogues": [
  ("Hi, what's your rate for a 20-foot container from Ho Chi Minh City to Singapore?", [
    ("It's 180 dollars, plus local charges. The rate is valid until the end of the month.", True, "Báo giá rõ + nói phí đi kèm + thời hạn hiệu lực."),
    ("Rate is cheap, 180.", False, "Thiếu mạo từ và đơn vị, câu cụt: 'The rate is 180 dollars.'"),
    ("You want go Singapore when?", False, "Trật tự câu kiểu tiếng Việt, lại chưa trả lời giá: 'When do you want to ship?'"),
  ]),
  ("Can you book two containers on Friday's vessel?", [
    ("Let me check the space with the carrier. I'll confirm within one hour.", True, "Không hứa bừa, kiểm tra với hãng tàu + hẹn thời gian cụ thể."),
    ("OK, I book already.", False, "Sai thì và nói chưa thật: 'I've booked it.' — chỉ nói khi đã có xác nhận."),
    ("Friday is full maybe, I don't sure.", False, "'I don't sure' sai: 'I'm not sure.' Nên nói sẽ kiểm tra và báo lại."),
  ]),
  ("When is the cut-off?", [
    ("The cargo cut-off is Wednesday at 5 p.m., and the SI cut-off is Tuesday at noon.", True, "Nêu rõ cả hạn hạ hàng và hạn nộp SI."),
    ("Cut-off Wednesday.", False, "Câu cụt, thiếu động từ và giờ cụ thể."),
    ("Don't worry, you can send any time.", False, "Sai thông tin — trễ cut-off là hàng bị rớt tàu."),
  ]),
  ("Should we ship this order FCL or LCL?", [
    ("It's only five cubic metres, so LCL is more cost-effective.", True, "Đưa lựa chọn + lý do bằng số liệu."),
    ("LCL more cheap.", False, "Thiếu động từ 'is'; so sánh hơn của 'cheap' là 'cheaper'."),
    ("Which one you like.", False, "Không tư vấn, lại thiếu trợ động từ: 'Which one do you prefer?'"),
  ]),
  ("Does this rate include the surcharges?", [
    ("No, it doesn't. The low sulphur surcharge is 30 dollars extra per container.", True, "Trả lời đúng câu hỏi + nói rõ phụ phí và số tiền."),
    ("No include.", False, "Dịch từng chữ 'không bao gồm': 'No, it doesn't include them.' — lại không nói phụ phí bao nhiêu."),
    ("Yes, all in, I think so.", False, "Mơ hồ ('I think so') khi báo giá — dễ phát sinh tranh cãi về sau."),
  ]),
 ],
 "listen": [
  ("The rate is valid until the end of the month", ["rate", "valid"], "hiệu lực giá cước"),
  ("We need one 40-foot container to Busan", ["container", "Busan"], "yêu cầu booking"),
  ("The cut-off for this vessel is Wednesday", ["cut-off", "Wednesday"], "giờ cắt máng"),
  ("There's no space left on this week's vessel", ["space", "vessel"], "hết chỗ"),
  ("Hi Lan, here's our rate for Tokyo. It's 350 dollars per container, plus local charges. Transit time is about seven days.", ["Tokyo", "local", "seven"], "forwarder báo giá cước"),
  ("I've booked two containers on the Pacific Star. The vessel leaves on Friday. Please deliver the goods to the port by Wednesday.", ["booked", "Friday", "port"], "xác nhận booking"),
 ],
})

# ───────────────────────── 1. Chứng từ xuất nhập khẩu ─────────────────────────
PHASES.append({
 "title": "Chứng từ xuất nhập khẩu",
 "vocab": [
  ("bill of lading", "/ˌbɪl əv ˈleɪdɪŋ/", "n", "vận đơn (B/L)", "Please check the draft <b>bill of lading</b> before Friday.", "Anh/chị kiểm tra giúp bản nháp vận đơn trước thứ Sáu nhé.", "船荷証券", "funani shōken"),
  ("commercial invoice", "/kəˌmɜːʃl ˈɪnvɔɪs/", "n", "hoá đơn thương mại", "The <b>commercial invoice</b> shows the unit price of each item.", "Hoá đơn thương mại ghi đơn giá của từng mặt hàng.", "インボイス", "inboisu"),
  ("packing list", "/ˈpækɪŋ lɪst/", "n", "phiếu chi tiết đóng gói, packing list", "The <b>packing list</b> says 120 cartons, not 125.", "Packing list ghi 120 thùng, không phải 125.", "パッキングリスト", "pakkingu risuto"),
  ("certificate of origin", "/səˌtɪfɪkət əv ˈɒrɪdʒɪn/", "n", "giấy chứng nhận xuất xứ (C/O)", "The buyer needs a <b>certificate of origin</b> to get a lower duty rate.", "Người mua cần C/O để được hưởng thuế suất thấp hơn.", "原産地証明書", "gensanchi shōmeisho"),
  ("original", "/əˈrɪdʒənl/", "n", "bản gốc", "We'll courier the three <b>originals</b> to you tomorrow.", "Mai bên tôi sẽ gửi chuyển phát ba bản gốc cho anh/chị.", "原本", "genpon"),
  ("telex release", "/ˈteleks rɪˌliːs/", "n", "điện giao hàng (không cần B/L gốc)", "The buyer has paid, so please arrange a <b>telex release</b>.", "Người mua đã thanh toán rồi, anh/chị làm điện giao hàng giúp nhé."),
  ("consignee", "/ˌkɒnsaɪˈniː/", "n", "người nhận hàng", "Please put the buyer's company as the <b>consignee</b>.", "Anh/chị ghi công ty người mua là người nhận hàng nhé.", "荷受人", "niukenin"),
  ("shipper", "/ˈʃɪpə/", "n", "người gửi hàng", "The <b>shipper</b>'s address on the B/L is wrong.", "Địa chỉ người gửi hàng trên B/L bị sai.", "荷送人", "niokurinin"),
  ("discrepancy", "/dɪˈskrepənsi/", "n", "điểm sai lệch, bất hợp lệ (giữa các chứng từ)", "There's a <b>discrepancy</b> between the invoice and the packing list.", "Có điểm lệch giữa hoá đơn và packing list."),
  ("amend", "/əˈmend/", "v", "sửa (chứng từ), tu chỉnh", "Can you <b>amend</b> the weight on the B/L before it's issued?", "Anh/chị sửa giúp trọng lượng trên B/L trước khi phát hành được không?"),
 ],
 "phrases": [
  ("Please find the draft B/L attached for your confirmation.", "Gửi anh/chị bản nháp B/L đính kèm để xác nhận."),
  ("Could you check the consignee name and address?", "Anh/chị kiểm tra giúp tên và địa chỉ người nhận hàng nhé."),
  ("The gross weight on the packing list doesn't match the B/L.", "Trọng lượng cả bì trên packing list không khớp với B/L."),
  ("We need the certificate of origin before the goods arrive.", "Chúng tôi cần C/O trước khi hàng về."),
  ("Could you send the scanned copies first?", "Anh/chị gửi bản scan trước giúp tôi được không?"),
  ("We'll courier the original documents tomorrow.", "Mai chúng tôi sẽ gửi chuyển phát bộ chứng từ gốc."),
  ("Please amend the invoice number on the C/O.", "Anh/chị sửa giúp số hoá đơn trên C/O nhé."),
  ("Is it an original B/L or a telex release?", "Lô này dùng B/L gốc hay điện giao hàng ạ?"),
  ("All the documents must show the same description.", "Tất cả chứng từ phải ghi cùng một mô tả hàng hoá."),
 ],
 "dialogues": [
  ("Have you checked the draft B/L?", [
    ("Yes, I have. The consignee address is correct, but the gross weight should be 12,500 kilos.", True, "Trả lời đúng thì + chỉ rõ chỗ cần sửa và con số đúng."),
    ("Yes, I check already. OK.", False, "Sai thì: 'I've checked it.' — và nên nói rõ có gì cần sửa không."),
    ("Draft is draft, no need check.", False, "Dịch từng chữ + sai quan điểm: B/L đã phát hành thì sửa rất tốn phí."),
  ]),
  ("The weight on the invoice is different from the packing list.", [
    ("Thanks for catching that. I'll correct the invoice and send you a new copy today.", True, "Cảm ơn + nhận sửa + hạn gửi lại."),
    ("Not my mistake, sales make it.", False, "Đổ lỗi, lại sai ngữ pháp ('sales made it'). Khách chỉ cần chứng từ đúng."),
    ("It's different a little, no problem.", False, "Coi nhẹ sai lệch — hải quan có thể giữ hàng vì chứng từ không khớp."),
  ]),
  ("When can you send the original documents?", [
    ("We'll courier them tomorrow morning. You should receive them in about three days.", True, "Nói ngày gửi + thời gian dự kiến nhận được."),
    ("Tomorrow I will sending.", False, "Sai dạng động từ: 'I'll send them tomorrow.'"),
    ("Soon, soon.", False, "Mơ hồ, không có thời gian cụ thể."),
  ]),
  ("The buyer has paid. Can we get a telex release?", [
    ("Sure. Please surrender the original B/Ls to the carrier, and they'll send the release to the destination office.", True, "Hướng dẫn đúng quy trình: nộp lại B/L gốc để hãng tàu điện giao hàng."),
    ("Telex release is free, OK no problem.", False, "Hứa sai — điện giao hàng thường có phí và cần thu hồi B/L gốc."),
    ("What is telex? I don't know.", False, "Thiếu chuyên môn; ít nhất nên nói 'Let me check the process with the carrier.'"),
  ]),
  ("Do you need a certificate of origin for this shipment?", [
    ("Yes, please. The buyer needs Form D to get the lower duty rate.", True, "Xác nhận + nêu loại C/O và lý do cần."),
    ("Yes, need.", False, "Thiếu chủ ngữ: 'Yes, we need one.'"),
    ("C/O is not important.", False, "Sai — không có C/O thì người mua mất ưu đãi thuế."),
  ]),
 ],
 "listen": [
  ("Please check the consignee name on the draft", ["consignee", "draft"], "kiểm tra nháp B/L"),
  ("The packing list shows one hundred cartons", ["packing", "cartons"], "số thùng trên packing list"),
  ("We'll send the original documents by courier", ["original", "courier"], "gửi chứng từ gốc"),
  ("There's a discrepancy in the gross weight", ["discrepancy", "weight"], "sai lệch chứng từ"),
  ("Hi Minh, I've attached the draft B/L. Please check the shipper and consignee details. We need your confirmation by Thursday.", ["attached", "shipper", "Thursday"], "email gửi nháp B/L"),
  ("The invoice and the packing list don't match. The invoice says 500 pieces, but the packing list says 480. Please amend it today.", ["match", "pieces", "amend"], "báo sai lệch chứng từ"),
 ],
})

# ───────────────────────── 2. Hải quan & thông quan ─────────────────────────
PHASES.append({
 "title": "Hải quan & thông quan",
 "vocab": [
  ("customs clearance", "/ˌkʌstəmz ˈklɪərəns/", "n", "thông quan, làm thủ tục hải quan", "<b>Customs clearance</b> usually takes one or two days.", "Thông quan thường mất một đến hai ngày.", "通関", "tsūkan"),
  ("customs declaration", "/ˌkʌstəmz ˌdekləˈreɪʃn/", "n", "tờ khai hải quan", "We submitted the <b>customs declaration</b> this morning.", "Sáng nay bên mình đã truyền tờ khai hải quan."),
  ("HS code", "/ˌeɪtʃ ˈes kəʊd/", "n", "mã HS (mã phân loại hàng hoá)", "The <b>HS code</b> determines the import duty rate.", "Mã HS quyết định thuế suất nhập khẩu.", "HSコード", "eichi esu kōdo"),
  ("import duty", "/ˈɪmpɔːt ˌdjuːti/", "n", "thuế nhập khẩu", "With a valid C/O, the <b>import duty</b> can be lower.", "Có C/O hợp lệ thì thuế nhập khẩu có thể thấp hơn.", "輸入関税", "yunyū kanzei"),
  ("physical inspection", "/ˌfɪzɪkl ɪnˈspekʃn/", "n", "kiểm hoá (kiểm tra thực tế hàng)", "The shipment was sent for <b>physical inspection</b>.", "Lô hàng bị phân đi kiểm hoá."),
  ("customs broker", "/ˈkʌstəmz ˌbrəʊkə/", "n", "đại lý làm thủ tục hải quan", "Our <b>customs broker</b> will handle the paperwork.", "Đại lý hải quan của mình sẽ lo giấy tờ.", "通関業者", "tsūkan gyōsha"),
  ("green channel", "/ˌɡriːn ˈtʃænl/", "n", "luồng xanh", "Good news: the declaration went through the <b>green channel</b>.", "Tin vui: tờ khai được phân luồng xanh."),
  ("classify", "/ˈklæsɪfaɪ/", "v", "phân loại, áp mã (hàng hoá)", "How should we <b>classify</b> these spare parts?", "Mấy phụ tùng này mình nên áp mã thế nào?"),
  ("import permit", "/ˈɪmpɔːt ˌpɜːmɪt/", "n", "giấy phép nhập khẩu", "Some medical equipment needs an <b>import permit</b>.", "Một số thiết bị y tế cần có giấy phép nhập khẩu."),
  ("customs officer", "/ˈkʌstəmz ˌɒfɪsə/", "n", "cán bộ hải quan", "The <b>customs officer</b> asked for the product catalogue.", "Cán bộ hải quan yêu cầu nộp catalogue sản phẩm.", "税関職員", "zeikan shokuin"),
 ],
 "phrases": [
  ("The shipment has cleared customs.", "Lô hàng đã thông quan."),
  ("The declaration went into the yellow channel, so they need to check the documents.", "Tờ khai bị luồng vàng nên hải quan cần kiểm tra hồ sơ."),
  ("Customs has selected the container for physical inspection.", "Hải quan đã chọn container đi kiểm hoá."),
  ("Could you confirm the HS code for this item?", "Anh/chị xác nhận giúp mã HS của mặt hàng này nhé."),
  ("We need the catalogue to explain the product to customs.", "Mình cần catalogue để giải trình sản phẩm với hải quan."),
  ("How much import duty and VAT do we need to pay?", "Mình phải nộp bao nhiêu thuế nhập khẩu và VAT?"),
  ("Our customs broker will submit the declaration tomorrow.", "Ngày mai đại lý hải quan bên mình sẽ truyền tờ khai."),
  ("This product needs an import permit before clearance.", "Mặt hàng này cần giấy phép nhập khẩu trước khi thông quan."),
  ("We expect to clear the goods by Thursday.", "Dự kiến bên mình thông quan xong trước thứ Năm."),
 ],
 "dialogues": [
  ("Has the shipment cleared customs yet?", [
    ("Not yet. It's in the yellow channel, so customs is checking the documents. We expect clearance tomorrow.", True, "Trả lời 'chưa' + lý do + thời gian dự kiến."),
    ("Not yet clear.", False, "Thiếu chủ ngữ/động từ và không nói lý do: 'It hasn't cleared yet because…'"),
    ("Customs is very slow, I can't do anything.", False, "Than phiền, không cung cấp thông tin hay hướng xử lý."),
  ]),
  ("Why was the container sent for inspection?", [
    ("It may be a random check, and it's the first time we're importing this product. The inspection is on Monday.", True, "Giải thích lý do khách quan (không khẳng định thay hải quan) + lịch kiểm hoá."),
    ("Because customs don't like us.", False, "Suy đoán thiếu chuyên nghiệp, không đưa thông tin thật."),
    ("Because inspection.", False, "Câu cụt, không giải thích gì."),
  ]),
  ("What HS code are you using for these items?", [
    ("We're using 8471.30. I'll send you the classification details so you can double-check.", True, "Nêu mã cụ thể + chủ động gửi căn cứ để đối chiếu."),
    ("Any code is OK, same tax.", False, "Sai hoàn toàn — áp sai mã HS có thể bị truy thu và phạt."),
    ("Code is, uh, I forget.", False, "Thiếu chuẩn bị; nên nói 'Let me check and get back to you.'"),
  ]),
  ("Customs is asking for more documents.", [
    ("OK. Could you tell me exactly which documents they need? I'll send them this afternoon.", True, "Hỏi rõ yêu cầu + cam kết thời gian."),
    ("Why they need more?", False, "Thiếu trợ động từ: 'Why do they need more?' — và nghe như phàn nàn."),
    ("We already gave everything.", False, "Cãi lại thay vì hỏi rõ hải quan còn thiếu gì."),
  ]),
  ("How much duty will we pay?", [
    ("With Form D, the import duty for this item is zero, but we still have to pay import VAT.", True, "Trả lời đúng câu hỏi, nêu điều kiện ưu đãi và nhắc vẫn phải nộp VAT hàng nhập khẩu."),
    ("Duty is zero, no pay anything.", False, "Sai thông tin: miễn thuế nhập khẩu vẫn phải nộp VAT; 'no pay' sai ngữ pháp."),
    ("I don't know, customs will tell.", False, "Né tránh — người làm XNK cần ước tính được thuế cho khách."),
  ]),
 ],
 "listen": [
  ("The shipment cleared customs this morning", ["cleared", "customs"], "thông quan xong"),
  ("Customs has selected our container for inspection", ["selected", "inspection"], "bị kiểm hoá"),
  ("Please confirm the HS code for these parts", ["confirm", "parts"], "xác nhận mã HS"),
  ("The declaration went through the green channel", ["declaration", "green"], "phân luồng xanh"),
  ("Hi Tom, the declaration is in the yellow channel. Customs wants the product catalogue. We'll send it today and hope to clear the goods tomorrow.", ["yellow", "catalogue", "tomorrow"], "báo tình trạng tờ khai"),
  ("The inspection is on Monday morning. Our customs broker will be at the port. If everything is fine, we can deliver on Tuesday.", ["Monday", "broker", "Tuesday"], "lịch kiểm hoá"),
 ],
})

# ───────────────────────── 3. Kho bãi & nhập xuất kho ─────────────────────────
PHASES.append({
 "title": "Kho bãi & nhập xuất kho",
 "vocab": [
  ("pallet", "/ˈpælət/", "n", "pallet (tấm kê hàng)", "Each <b>pallet</b> holds 40 cartons.", "Mỗi pallet xếp được 40 thùng.", "パレット", "paretto"),
  ("stock count", "/ˈstɒk kaʊnt/", "n", "kiểm kê kho", "We do a full <b>stock count</b> at the end of each quarter.", "Cuối mỗi quý bên mình kiểm kê toàn bộ kho.", "棚卸", "tanaoroshi"),
  ("receiving", "/rɪˈsiːvɪŋ/", "n", "khâu nhận hàng, nhập kho", "<b>Receiving</b> starts at 7 a.m. at dock 2.", "Nhận hàng bắt đầu lúc 7 giờ sáng ở cửa số 2.", "入荷", "nyūka"),
  ("picking", "/ˈpɪkɪŋ/", "n", "soạn hàng, lấy hàng theo đơn", "<b>Picking</b> for today's orders must finish by 2 p.m.", "Soạn hàng cho các đơn hôm nay phải xong trước 2 giờ chiều.", "ピッキング", "pikkingu"),
  ("SKU", "/ˌes keɪ ˈjuː/", "n", "mã hàng (SKU)", "We store more than 3,000 <b>SKUs</b> in this warehouse.", "Kho này chứa hơn 3.000 mã hàng."),
  ("location", "/ləʊˈkeɪʃn/", "n", "vị trí (ô kệ) trong kho", "The system shows the wrong <b>location</b> for this item.", "Hệ thống báo sai vị trí của mã hàng này.", "ロケーション", "rokēshon"),
  ("forklift", "/ˈfɔːklɪft/", "n", "xe nâng", "Only trained staff can drive the <b>forklift</b>.", "Chỉ nhân viên đã qua đào tạo mới được lái xe nâng.", "フォークリフト", "fōkurifuto"),
  ("FIFO", "/ˈfaɪfəʊ/", "n", "nhập trước xuất trước (FIFO)", "Please follow <b>FIFO</b> and ship the oldest stock first.", "Nhớ theo FIFO, xuất hàng cũ trước nhé.", "先入れ先出し", "sakiire sakidashi"),
  ("stock level", "/ˈstɒk ˌlevl/", "n", "mức tồn kho", "The <b>stock level</b> of item A12 is below the minimum.", "Tồn kho mã A12 đang dưới mức tối thiểu."),
  ("loading dock", "/ˈləʊdɪŋ dɒk/", "n", "cửa/bến bốc xếp hàng", "The truck is waiting at <b>loading dock</b> 3.", "Xe tải đang chờ ở cửa xuất hàng số 3."),
 ],
 "phrases": [
  ("The goods arrived at the warehouse this morning.", "Hàng đã về kho sáng nay."),
  ("We received 18 pallets, but the packing list says 20.", "Bên mình nhận 18 pallet, nhưng packing list ghi 20."),
  ("Please put these pallets in location B-05.", "Xếp mấy pallet này vào vị trí B-05 nhé."),
  ("The stock in the system doesn't match the physical stock.", "Tồn kho trên hệ thống không khớp với tồn thực tế."),
  ("We're doing a stock count this Saturday.", "Thứ Bảy này bên mình kiểm kê kho."),
  ("This item is running low. We need to reorder.", "Mã hàng này sắp hết rồi, cần đặt thêm."),
  ("The order is picked and packed, ready to ship.", "Đơn đã soạn và đóng gói xong, sẵn sàng xuất."),
  ("Please scan every carton before loading.", "Quét mã từng thùng trước khi bốc lên xe nhé."),
  ("We have space for about 200 more pallets.", "Kho còn chỗ cho khoảng 200 pallet nữa."),
  ("Always use FIFO for food products.", "Hàng thực phẩm thì luôn nhập trước xuất trước (FIFO)."),
 ],
 "dialogues": [
  ("How many pallets did you receive?", [
    ("We received 18 pallets, but the packing list says 20. I've taken photos and informed the supplier.", True, "Báo số thực nhận + chênh lệch + việc đã làm."),
    ("We receive 18.", False, "Sai thì: 'We received 18.' — và chưa nói chênh lệch với chứng từ."),
    ("Around 20, I think.", False, "Nhận hàng phải đếm chính xác, không dùng 'around… I think'."),
  ]),
  ("Can you ship this order today?", [
    ("Yes. Picking is finished, and the truck will leave at 3 p.m.", True, "Xác nhận + tình trạng soạn hàng + giờ xe chạy."),
    ("Yes, can.", False, "Thiếu chủ ngữ: 'Yes, we can.'"),
    ("Today maybe, tomorrow maybe.", False, "Mơ hồ — khách cần thời gian chắc chắn."),
  ]),
  ("The system shows 50 units, but I can only find 42.", [
    ("Let's check the other locations first. If we still can't find them, I'll report it to the manager.", True, "Đề xuất bước kiểm tra + báo cáo nếu vẫn thiếu."),
    ("Maybe somebody take it.", False, "Sai thì ('took') và buộc tội vô căn cứ."),
    ("Just change the system to 42.", False, "Sửa số liệu khi chưa điều tra — vi phạm quy trình kiểm soát tồn kho."),
  ]),
  ("When is the next stock count?", [
    ("It's this Saturday, from 8 a.m. We'll stop all receiving and picking during the count.", True, "Trả lời ngày giờ + lưu ý vận hành trong lúc kiểm kê."),
    ("Saturday have stock count.", False, "Dịch từng chữ 'thứ Bảy có kiểm kê': 'There's a stock count on Saturday.'"),
    ("I don't know, ask other people.", False, "Đẩy việc, thiếu hợp tác."),
  ]),
  ("Where should I put these new pallets?", [
    ("Please put them in aisle C, locations C-10 to C-14, and update the system.", True, "Chỉ dẫn vị trí cụ thể + nhắc cập nhật hệ thống."),
    ("Put anywhere.", False, "Cộc và sai nghiệp vụ — hàng không đúng vị trí sẽ khó tìm."),
    ("You put in there.", False, "Thiếu tân ngữ và chỉ dẫn mơ hồ: 'Please put them in…'"),
  ]),
 ],
 "listen": [
  ("We received eighteen pallets this morning", ["eighteen", "pallets"], "số pallet nhận"),
  ("Please put the cartons in location B-05", ["cartons", "location"], "xếp hàng vào vị trí"),
  ("The stock count starts at eight on Saturday", ["count", "Saturday"], "lịch kiểm kê"),
  ("This item is running low in the warehouse", ["running", "warehouse"], "sắp hết hàng"),
  ("The truck from the supplier is at dock two. Please unload it first. Then scan each pallet and check the packing list.", ["truck", "unload", "scan"], "hướng dẫn nhận hàng"),
  ("After the stock count, we found three differences. Two items were in the wrong location. One carton is still missing.", ["differences", "wrong", "missing"], "kết quả kiểm kê"),
 ],
})

# ───────────────────────── 4. Vận tải & giao hàng ─────────────────────────
PHASES.append({
 "title": "Vận tải & giao hàng",
 "vocab": [
  ("trucking", "/ˈtrʌkɪŋ/", "n", "vận tải đường bộ (bằng xe tải), trucking", "The <b>trucking</b> cost from the port is 2 million dong.", "Phí trucking từ cảng về là 2 triệu đồng."),
  ("delivery note", "/dɪˈlɪvəri nəʊt/", "n", "phiếu giao hàng", "Please ask the customer to sign the <b>delivery note</b>.", "Nhớ nhờ khách ký phiếu giao hàng nhé.", "納品書", "nōhinsho"),
  ("proof of delivery", "/ˌpruːf əv dɪˈlɪvəri/", "n", "chứng từ xác nhận đã giao hàng (POD)", "Send me the <b>proof of delivery</b> after unloading.", "Dỡ hàng xong thì gửi tôi POD nhé.", "受領書", "juryōsho"),
  ("route", "/ruːt/", "n", "tuyến đường", "The driver will take a different <b>route</b> to avoid traffic.", "Tài xế sẽ đi tuyến khác để tránh kẹt xe."),
  ("pick up", "/ˌpɪk ˈʌp/", "phr v", "đến lấy hàng", "The truck will <b>pick up</b> the goods at 9 a.m.", "Xe sẽ đến lấy hàng lúc 9 giờ sáng."),
  ("unload", "/ʌnˈləʊd/", "v", "dỡ hàng (xuống xe/khỏi container)", "It takes about an hour to <b>unload</b> a container.", "Dỡ một container mất khoảng một tiếng.", "荷降ろし", "nioroshi"),
  ("transit time", "/ˈtrænzɪt taɪm/", "n", "thời gian vận chuyển", "The <b>transit time</b> by road to Hanoi is two days.", "Đi đường bộ ra Hà Nội mất hai ngày."),
  ("door-to-door", "/ˌdɔː tə ˈdɔː/", "adj", "giao tận nơi (từ kho người bán đến kho người mua)", "We offer a <b>door-to-door</b> service from Shenzhen to Bac Ninh.", "Bên em có dịch vụ door-to-door từ Thâm Quyến về Bắc Ninh."),
  ("consolidate", "/kənˈsɒlɪdeɪt/", "v", "gom (nhiều lô) hàng", "Let's <b>consolidate</b> the three orders into one truck.", "Mình gom ba đơn lên một xe nhé."),
  ("seal", "/siːl/", "n", "seal niêm phong (container)", "Please check the <b>seal</b> number before opening the container.", "Kiểm tra số seal trước khi mở container nhé."),
 ],
 "phrases": [
  ("The truck will pick up the container at 8 a.m.", "Xe sẽ đến lấy container lúc 8 giờ sáng."),
  ("The goods are on the way to your warehouse.", "Hàng đang trên đường đến kho của anh/chị."),
  ("The driver is stuck in traffic and will be about an hour late.", "Tài xế bị kẹt xe, sẽ đến trễ khoảng một tiếng."),
  ("Could you send me the driver's name and phone number?", "Anh/chị gửi giúp tôi tên và số điện thoại tài xế nhé."),
  ("What time can your warehouse receive the goods?", "Kho bên anh/chị nhận hàng được lúc mấy giờ ạ?"),
  ("Please sign the delivery note and write the date.", "Anh/chị ký phiếu giao hàng và ghi ngày giúp nhé."),
  ("The seal number matches the B/L.", "Số seal khớp với B/L."),
  ("We can consolidate both orders into one shipment.", "Mình có thể gom hai đơn thành một lô."),
  ("Please return the empty container by Friday.", "Vui lòng trả vỏ container trước thứ Sáu."),
 ],
 "dialogues": [
  ("Where's the truck now? We've been waiting for an hour.", [
    ("I'm sorry. The driver is stuck in traffic near the port. He'll arrive in about 30 minutes.", True, "Xin lỗi + lý do + thời gian đến cụ thể."),
    ("Traffic jam, not my fault.", False, "Thiếu động từ và đổ lỗi, không xin lỗi."),
    ("He come soon.", False, "Sai chia động từ ('He'll come') và mơ hồ."),
  ]),
  ("Can you deliver on Saturday?", [
    ("Yes, we can. Could you confirm that someone will be at the warehouse to receive the goods?", True, "Xác nhận + hỏi lại điều kiện nhận hàng."),
    ("Saturday is OK but no people receive.", False, "Câu lộn xộn; cần hỏi 'Will someone be there to receive it?'"),
    ("Yes, of course, any time!", False, "Hứa suông, không xác nhận giờ nhận hàng."),
  ]),
  ("The customer says two cartons are missing.", [
    ("Let me check the delivery note and the POD. Did the customer write any remarks when signing?", True, "Kiểm tra chứng từ + hỏi đúng thông tin cần để xử lý."),
    ("Impossible, we deliver full.", False, "Phủ nhận ngay, sai thì ('delivered')."),
    ("The customer lie.", False, "Buộc tội khách và sai ngữ pháp ('is lying')."),
  ]),
  ("How long is the transit time to Da Nang?", [
    ("By truck, it's about two days. If it's urgent, we can arrange an express service.", True, "Trả lời thời gian + phương án nhanh hơn."),
    ("Two days maybe three maybe.", False, "Mơ hồ, không có câu hoàn chỉnh."),
    ("It is take two days.", False, "Thừa 'is': 'It takes two days.'"),
  ]),
  ("Can you combine these orders into one truck?", [
    ("Yes. The total is 14 pallets, so they'll fit in one 10-ton truck.", True, "Đồng ý + căn cứ tính toán cụ thể."),
    ("Yes, combine is cheaper.", False, "Sai dạng từ: động từ 'combine' không làm chủ ngữ được — 'Combining them is cheaper.' Lại chưa kiểm tra tải trọng."),
    ("No, cannot.", False, "Thiếu chủ ngữ, không có lý do: 'No, we can't because…'"),
  ]),
 ],
 "listen": [
  ("The truck will pick up the goods at nine", ["truck", "nine"], "giờ lấy hàng"),
  ("Please sign the delivery note at the bottom", ["sign", "note"], "ký phiếu giao hàng"),
  ("The driver is stuck in traffic near the port", ["driver", "traffic"], "xe bị kẹt"),
  ("Please check the seal number before unloading", ["seal", "unloading"], "kiểm tra seal"),
  ("Hi, this is Tuan from Delta Trucking. Our driver is ten minutes away. Please open dock three for him.", ["driver", "minutes", "dock"], "báo xe sắp đến"),
  ("The goods were delivered at two o'clock. The customer signed the delivery note. I'll send you the photos and the POD tonight.", ["delivered", "signed", "photos"], "xác nhận đã giao"),
 ],
})

# ───────────────────────── 5. Theo dõi lô hàng & chậm trễ ─────────────────────────
PHASES.append({
 "title": "Theo dõi lô hàng & chậm trễ",
 "vocab": [
  ("ETA", "/ˌiː tiː ˈeɪ/", "n", "thời gian dự kiến tàu/hàng đến (ETA)", "The <b>ETA</b> at Cat Lai port is next Monday.", "ETA về cảng Cát Lái là thứ Hai tuần sau.", "到着予定日", "tōchaku yoteibi"),
  ("ETD", "/ˌiː tiː ˈdiː/", "n", "thời gian dự kiến tàu khởi hành (ETD)", "The <b>ETD</b> from Shanghai is the 12th.", "ETD từ Thượng Hải là ngày 12.", "出港予定日", "shukkō yoteibi"),
  ("track", "/træk/", "v", "theo dõi (hành trình lô hàng)", "You can <b>track</b> the container on the carrier's website.", "Anh/chị có thể theo dõi container trên website hãng tàu."),
  ("transshipment", "/trænsˈʃɪpmənt/", "n", "chuyển tải (qua cảng trung chuyển)", "There's a <b>transshipment</b> in Singapore.", "Lô này có chuyển tải ở Singapore.", "積み替え", "tsumikae"),
  ("port congestion", "/ˌpɔːt kənˈdʒestʃən/", "n", "ùn tắc cảng", "<b>Port congestion</b> has caused a three-day delay.", "Ùn tắc cảng khiến lô hàng trễ ba ngày."),
  ("roll over", "/ˌrəʊl ˈəʊvə/", "phr v", "bị rớt tàu (đẩy sang chuyến sau)", "Our container was <b>rolled over</b> to next week's vessel.", "Container của mình bị rớt sang tàu tuần sau."),
  ("demurrage", "/dɪˈmʌrɪdʒ/", "n", "phí lưu container tại bãi cảng (DEM)", "Pick up the container soon, or we'll pay <b>demurrage</b>.", "Lấy container sớm đi, không là phải trả phí lưu bãi.", "デマレージ", "demarēji"),
  ("detention", "/dɪˈtenʃn/", "n", "phí lưu vỏ container ngoài cảng (DET)", "Return the empty container on time to avoid <b>detention</b>.", "Trả vỏ đúng hạn để tránh phí lưu vỏ."),
  ("status", "/ˈsteɪtəs/", "n", "tình trạng", "Could you give me a <b>status</b> update on PO 4521?", "Anh/chị cập nhật giúp tình trạng PO 4521 nhé."),
  ("revised", "/rɪˈvaɪzd/", "adj", "đã điều chỉnh, (lịch) mới", "The <b>revised</b> ETA is Thursday.", "ETA mới là thứ Năm."),
 ],
 "phrases": [
  ("Could you give me an update on this shipment?", "Anh/chị cập nhật giúp tôi tình hình lô hàng này nhé."),
  ("The vessel is running two days late.", "Tàu đang trễ hai ngày."),
  ("The new ETA is Thursday morning.", "ETA mới là sáng thứ Năm."),
  ("Our container was rolled over to the next vessel.", "Container của mình bị rớt sang tàu sau."),
  ("The delay is due to port congestion in Singapore.", "Chậm trễ là do ùn tắc cảng ở Singapore."),
  ("I'll keep you updated every day until it arrives.", "Tôi sẽ cập nhật cho anh/chị hằng ngày đến khi hàng về."),
  ("How many free days do we have at the port?", "Mình được bao nhiêu ngày miễn phí lưu bãi ở cảng?"),
  ("We need to pick up the container before demurrage starts.", "Mình cần lấy container trước khi bắt đầu tính phí lưu bãi."),
  ("Is there any way to speed it up?", "Có cách nào đẩy nhanh hơn không ạ?"),
 ],
 "dialogues": [
  ("Where's our shipment? It should be here by now.", [
    ("I'm sorry. The vessel was delayed by port congestion in Singapore. The revised ETA is Thursday.", True, "Xin lỗi + nguyên nhân + ETA mới."),
    ("It is late because congestion.", False, "Thiếu 'of': 'because of congestion' — và chưa có ETA mới."),
    ("I don't know, the carrier don't tell me.", False, "Sai chia động từ ('doesn't') và nghe bị động, thiếu trách nhiệm."),
  ]),
  ("Why was our container rolled over?", [
    ("The vessel was overbooked. We've secured space on the next one, which leaves on Monday.", True, "Nguyên nhân + giải pháp đã làm + ngày đi mới."),
    ("Rolled over is normal, don't worry.", False, "Coi nhẹ vấn đề của khách; câu sai ('rolled over' không làm chủ ngữ): 'Rollovers happen, but…'"),
    ("Because vessel full.", False, "Câu cụt, thiếu mạo từ và động từ: 'Because the vessel was full.'"),
  ]),
  ("Will we have to pay demurrage?", [
    ("We have five free days. If we pick up the container by Friday, there will be no demurrage.", True, "Nêu số ngày miễn phí + hạn cần lấy để không mất phí."),
    ("Maybe yes, maybe no.", False, "Né câu hỏi; hãy tính theo số ngày free time."),
    ("Demurrage is not my business.", False, "Thiếu hợp tác — chi phí này ảnh hưởng trực tiếp đến khách."),
  ]),
  ("Can you send me a status update every day?", [
    ("Of course. I'll email you every morning until the goods arrive.", True, "Đồng ý + tần suất + thời điểm kết thúc."),
    ("OK, I update you when I free.", False, "Thiếu 'am' ('when I'm free') và nghe không ưu tiên khách."),
    ("Every day is too much.", False, "Từ chối thẳng, nên đề xuất tần suất khác nếu không làm được."),
  ]),
  ("Is there a transshipment on this route?", [
    ("Yes, there's a transshipment in Kaohsiung, so the transit time is about 12 days.", True, "Xác nhận + cảng chuyển tải + ảnh hưởng đến thời gian."),
    ("Yes, it have.", False, "Sai cấu trúc: 'Yes, there is.'"),
    ("No problem.", False, "Không trả lời đúng câu hỏi có/không."),
  ]),
 ],
 "listen": [
  ("The new ETA is Thursday morning", ["ETA", "Thursday"], "ETA mới"),
  ("Our container was rolled over to next week", ["container", "week"], "rớt tàu"),
  ("The delay is due to port congestion", ["due", "congestion"], "nguyên nhân chậm"),
  ("We have five free days at the port", ["five", "free"], "số ngày miễn phí lưu bãi"),
  ("Hi Anna, quick update on your shipment. The vessel left Shanghai two days late. The revised ETA in Hai Phong is the 20th.", ["update", "Shanghai", "revised"], "cập nhật ETA cho khách"),
  ("The container is still at the port. We must pick it up by Friday. After that, demurrage is 40 dollars a day.", ["still", "Friday", "demurrage"], "cảnh báo phí lưu bãi"),
 ],
})

# ───────────────────────── 6. Làm việc với nhà cung cấp ─────────────────────────
PHASES.append({
 "title": "Làm việc với nhà cung cấp",
 "vocab": [
  ("purchase order", "/ˈpɜːtʃəs ˌɔːdə/", "n", "đơn đặt hàng (PO)", "I've sent you the <b>purchase order</b> for 2,000 units.", "Tôi đã gửi anh/chị PO cho 2.000 cái.", "発注書", "hacchūsho"),
  ("lead time", "/ˈliːd taɪm/", "n", "thời gian chờ hàng (từ lúc đặt đến lúc có hàng)", "The <b>lead time</b> for this part is six weeks.", "Linh kiện này mất sáu tuần từ lúc đặt hàng.", "リードタイム", "rīdo taimu"),
  ("MOQ", "/ˌem əʊ ˈkjuː/", "n", "số lượng đặt hàng tối thiểu (MOQ)", "The <b>MOQ</b> is 500 pieces per colour.", "MOQ là 500 cái mỗi màu."),
  ("unit price", "/ˌjuːnɪt ˈpraɪs/", "n", "đơn giá", "The <b>unit price</b> is 2.40 dollars.", "Đơn giá là 2,40 đô.", "単価", "tanka"),
  ("order confirmation", "/ˈɔːdə ˌkɒnfəˈmeɪʃn/", "n", "xác nhận đơn hàng", "Please send the <b>order confirmation</b> with the ship date.", "Anh/chị gửi xác nhận đơn hàng kèm ngày giao nhé.", "注文請書", "chūmon ukesho"),
  ("vendor", "/ˈvendə/", "n", "nhà cung cấp, vendor", "We need to compare quotes from three <b>vendors</b>.", "Mình cần so sánh báo giá của ba nhà cung cấp.", "仕入先", "shiiresaki"),
  ("sourcing", "/ˈsɔːsɪŋ/", "n", "tìm nguồn hàng, sourcing", "Our <b>sourcing</b> team is looking for a new supplier in Thailand.", "Nhóm sourcing đang tìm nhà cung cấp mới ở Thái Lan."),
  ("negotiate", "/nɪˈɡəʊʃieɪt/", "v", "đàm phán", "We're trying to <b>negotiate</b> a lower price for next year.", "Bên mình đang đàm phán giá thấp hơn cho năm sau.", "交渉する", "kōshō suru"),
  ("partial shipment", "/ˌpɑːʃl ˈʃɪpmənt/", "n", "giao hàng từng phần", "Can we accept a <b>partial shipment</b> this week?", "Tuần này mình nhận giao từng phần được không?", "分割出荷", "bunkatsu shukka"),
  ("backorder", "/ˈbækˌɔːdə/", "n", "hàng nợ lại, chưa giao đủ", "The other 300 units are on <b>backorder</b>.", "300 cái còn lại đang nợ, chưa giao."),
 ],
 "phrases": [
  ("Please confirm the price and the ship date for this PO.", "Anh/chị xác nhận giúp giá và ngày giao cho PO này nhé."),
  ("What's your current lead time?", "Hiện tại bên anh/chị cần bao lâu để giao hàng?"),
  ("Could you lower the MOQ for our first order?", "Đơn đầu tiên, bên anh/chị giảm MOQ được không?"),
  ("We need the goods by the 15th at the latest.", "Chậm nhất ngày 15 bên tôi phải có hàng."),
  ("Can you ship part of the order first?", "Bên anh/chị giao trước một phần đơn được không?"),
  ("Your price is higher than other vendors' prices.", "Giá bên anh/chị cao hơn giá của các nhà cung cấp khác."),
  ("If we order 5,000 units, can you give us a better price?", "Nếu đặt 5.000 cái thì anh/chị có giá tốt hơn không?"),
  ("Please let us know as soon as possible if there's any delay.", "Nếu có chậm trễ gì anh/chị báo sớm giúp nhé."),
  ("We'd like to receive samples before we place the order.", "Chúng tôi muốn nhận mẫu trước khi đặt hàng."),
 ],
 "dialogues": [
  ("Hi, we've received your PO. The lead time is six weeks.", [
    ("Thanks. Six weeks is too long for us. Could you ship half of the order in four weeks?", True, "Cảm ơn + nêu vấn đề + đề xuất cụ thể (giao từng phần)."),
    ("Six weeks? Too long, you must faster.", False, "Sai ngữ pháp ('be faster') và giọng ra lệnh."),
    ("OK, no problem.", False, "Chấp nhận ngay dù không đáp ứng tiến độ — nên thương lượng."),
  ]),
  ("Our MOQ is 1,000 pieces.", [
    ("I see. This is a trial order, so could you accept 500 pieces this time?", True, "Ghi nhận + lý do + đề xuất số lượng thấp hơn."),
    ("1,000 is too many, we no need.", False, "Sai ngữ pháp ('we don't need that many') và nói cụt."),
    ("Why MOQ so high?", False, "Thiếu động từ: 'Why is the MOQ so high?' — nghe như trách."),
  ]),
  ("We can't ship on the 10th. The raw material is late.", [
    ("I understand. What's the earliest date you can ship? And can you send part of the order first?", True, "Thông cảm + hỏi ngày sớm nhất + phương án giao từng phần."),
    ("You promised! This is very bad.", False, "Cảm xúc, không giải quyết vấn đề."),
    ("OK, when you can, you ship.", False, "Buông xuôi, không hỏi mốc thời gian mới."),
  ]),
  ("Can you send us the purchase order today?", [
    ("Yes. I'm waiting for my manager's signature, so you'll get it by 4 p.m.", True, "Xác nhận + lý do + giờ gửi cụ thể."),
    ("Yes, I send.", False, "Thiếu 'will' và tân ngữ: 'Yes, I'll send it today.'"),
    ("Maybe. PO is not ready, I don't know.", False, "Mơ hồ, không nói khi nào sẵn sàng."),
  ]),
  ("The price will go up by 5% next month.", [
    ("That's a big increase for us. Could we keep the current price for orders placed this month?", True, "Phản hồi lịch sự + thương lượng giữ giá cho đơn đặt trong tháng."),
    ("We don't accept. Price go up is not fair.", False, "Sai ngữ pháp ('The price increase isn't fair') và cứng nhắc."),
    ("Why? You want more money?", False, "Nghe khiêu khích, không chuyên nghiệp."),
  ]),
 ],
 "listen": [
  ("Please confirm the ship date for this order", ["confirm", "ship"], "xác nhận ngày giao"),
  ("The lead time for this part is six weeks", ["lead", "six"], "thời gian giao hàng"),
  ("Our minimum order is five hundred pieces", ["minimum", "pieces"], "số lượng tối thiểu"),
  ("The rest of the order is on backorder", ["rest", "backorder"], "hàng nợ"),
  ("Hi Kenji, thanks for the order confirmation. The unit price is correct. However, we need the goods one week earlier, by May 10.", ["confirmation", "correct", "earlier"], "phản hồi xác nhận đơn"),
  ("We can ship 600 units on Friday. The other 400 will follow in two weeks. Is a partial shipment OK for you?", ["Friday", "follow", "partial"], "nhà cung cấp đề nghị giao từng phần"),
 ],
})

# ───────────────────────── 7. Incoterms & điều kiện thương mại ─────────────────────────
PHASES.append({
 "title": "Incoterms & điều kiện thương mại",
 "vocab": [
  ("Incoterms", "/ˈɪŋkəʊtɜːmz/", "n", "điều kiện giao hàng Incoterms", "Which <b>Incoterms</b> are we using for this contract?", "Hợp đồng này mình dùng điều kiện Incoterms nào?", "インコタームズ", "inkotāmuzu"),
  ("FOB", "/ˌef əʊ ˈbiː/", "n", "giao hàng lên tàu (FOB)", "Under <b>FOB</b>, the buyer pays the sea freight.", "Theo FOB, người mua trả cước biển.", "本船渡し", "honsen watashi"),
  ("CIF", "/ˌsiː aɪ ˈef/", "n", "giá gồm tiền hàng, bảo hiểm và cước (CIF)", "Under <b>CIF</b>, the seller pays freight and insurance.", "Theo CIF, người bán trả cước và bảo hiểm.", "運賃保険料込み", "unchin hokenryō komi"),
  ("EXW", "/ˌeks ˈwɜːks/", "n", "giao tại xưởng (EXW)", "With <b>EXW</b>, we collect the goods from the supplier's factory.", "Với EXW, bên mình tự đến xưởng nhà cung cấp lấy hàng.", "工場渡し", "kōjō watashi"),
  ("DAP", "/ˌdiː eɪ ˈpiː/", "n", "giao tại nơi đến (DAP)", "Under <b>DAP</b>, the buyer still pays the import duty.", "Theo DAP, người mua vẫn phải trả thuế nhập khẩu."),
  ("risk", "/rɪsk/", "n", "rủi ro", "Under FOB, the <b>risk</b> passes to the buyer when the goods are on board.", "Theo FOB, rủi ro chuyển sang người mua khi hàng đã lên tàu."),
  ("cargo insurance", "/ˈkɑːɡəʊ ɪnˌʃʊərəns/", "n", "bảo hiểm hàng hoá", "Who is buying the <b>cargo insurance</b>?", "Bên nào mua bảo hiểm hàng hoá?", "貨物保険", "kamotsu hoken"),
  ("letter of credit", "/ˌletər əv ˈkredɪt/", "n", "thư tín dụng (L/C)", "Payment is by <b>letter of credit</b> at sight.", "Thanh toán bằng L/C trả ngay.", "信用状", "shin'yōjō"),
  ("payment terms", "/ˈpeɪmənt tɜːmz/", "n", "điều khoản thanh toán", "Our <b>payment terms</b> are 30% deposit and 70% before shipment.", "Điều khoản thanh toán: cọc 30%, 70% trước khi giao hàng.", "支払条件", "shiharai jōken"),
  ("port of loading", "/ˌpɔːt əv ˈləʊdɪŋ/", "n", "cảng xếp hàng (POL)", "The <b>port of loading</b> is Cat Lai, Ho Chi Minh City.", "Cảng xếp hàng là Cát Lái, TP.HCM.", "船積港", "funazumikō"),
 ],
 "phrases": [
  ("Is the price FOB or CIF?", "Giá này là FOB hay CIF ạ?"),
  ("Under FOB, the buyer arranges the sea freight.", "Theo FOB, người mua lo cước biển."),
  ("Under CIF, we pay the freight and insurance to the port of destination.", "Theo CIF, bên tôi trả cước và bảo hiểm đến cảng đích."),
  ("With EXW, the buyer handles export clearance too.", "Với EXW, người mua lo cả thủ tục hải quan xuất khẩu."),
  ("Who pays the local charges at the port of loading?", "Ai trả phí local ở cảng xếp hàng?"),
  ("When does the risk pass to the buyer?", "Khi nào rủi ro chuyển sang người mua?"),
  ("Our payment terms are 30% deposit, 70% against copy B/L.", "Điều khoản thanh toán: cọc 30%, 70% khi nhận bản sao B/L."),
  ("We'd prefer to pay by T/T rather than L/C.", "Bên tôi muốn thanh toán bằng T/T hơn là L/C."),
  ("Please add the Incoterms and the named port to the contract.", "Anh/chị ghi rõ điều kiện Incoterms và tên cảng vào hợp đồng nhé."),
 ],
 "dialogues": [
  ("Is your price FOB or CIF?", [
    ("It's FOB Hai Phong. If you'd like CIF Osaka, I can send you a new quote.", True, "Trả lời rõ điều kiện + cảng + đề xuất báo giá theo điều kiện khác."),
    ("FOB. Same same CIF.", False, "Sai kiến thức: FOB và CIF khác nhau về cước, bảo hiểm và chi phí."),
    ("Price is good, no matter.", False, "Né câu hỏi — điều kiện Incoterms ảnh hưởng lớn đến giá."),
  ]),
  ("Under FOB, who pays the sea freight?", [
    ("The buyer does. The seller pays the costs until the goods are loaded on the vessel.", True, "Trả lời đúng + giải thích phạm vi chi phí của người bán."),
    ("Seller pay all.", False, "Sai kiến thức và thiếu 's' ('pays')."),
    ("I think the forwarder.", False, "Sai — forwarder chỉ là bên cung cấp dịch vụ, người trả là người mua."),
  ]),
  ("If we buy EXW, what do we need to arrange?", [
    ("You'll need to arrange everything: pickup at our factory, export clearance, freight and import clearance.", True, "Liệt kê đủ trách nhiệm của người mua theo EXW."),
    ("Only freight, we do the rest.", False, "Sai — theo EXW người bán gần như không làm gì, kể cả thông quan xuất."),
    ("EXW is easy, don't worry.", False, "Không trả lời câu hỏi, dễ gây hiểu lầm về trách nhiệm."),
  ]),
  ("Can we change the payment terms to 60 days after the B/L date?", [
    ("I'll need to check with our finance team. Could we discuss it on our call tomorrow?", True, "Không hứa vượt quyền + hẹn trao đổi tiếp."),
    ("OK, 60 days no problem.", False, "Đồng ý ngay khi chưa hỏi bộ phận tài chính — rủi ro cho công ty."),
    ("No. L/C only.", False, "Cứng nhắc, cộc lốc, dễ mất khách."),
  ]),
  ("Who's responsible if the goods are damaged at sea?", [
    ("Under CIF, the risk is the buyer's after loading, but the seller's insurance covers the goods, so you can claim on it.", True, "Giải thích đúng: rủi ro chuyển khi xếp hàng, nhưng người mua được bồi thường qua bảo hiểm do người bán mua."),
    ("The seller, always.", False, "Sai kiến thức: tuỳ điều kiện Incoterms."),
    ("The shipping line, 100%.", False, "Sai — hãng tàu chỉ chịu trách nhiệm có giới hạn, cần xem điều kiện và bảo hiểm."),
  ]),
 ],
 "listen": [
  ("Our price is FOB Hai Phong", ["price", "FOB"], "điều kiện giá"),
  ("Under CIF the seller pays the insurance", ["seller", "insurance"], "trách nhiệm theo CIF"),
  ("Payment is by letter of credit at sight", ["letter", "sight"], "phương thức thanh toán"),
  ("Please add the port of loading to the contract", ["loading", "contract"], "bổ sung hợp đồng"),
  ("We usually sell FOB. The buyer books the vessel and pays the sea freight. We only pay the costs in Vietnam.", ["sell", "freight", "costs"], "giải thích điều kiện FOB"),
  ("Our payment terms are simple. You pay a 30% deposit with the order. The balance is due before shipment.", ["simple", "deposit", "balance"], "điều khoản thanh toán"),
 ],
})

# ───────────────────────── 8. Hàng hư hỏng & khiếu nại ─────────────────────────
PHASES.append({
 "title": "Hàng hư hỏng & khiếu nại",
 "vocab": [
  ("claim", "/kleɪm/", "n", "yêu cầu bồi thường, khiếu nại", "We'll file a <b>claim</b> with the insurance company.", "Bên mình sẽ làm hồ sơ đòi bồi thường với công ty bảo hiểm.", "クレーム", "kurēmu"),
  ("short-shipped", "/ˌʃɔːt ˈʃɪpt/", "adj", "(hàng) giao thiếu so với chứng từ", "Two cartons were <b>short-shipped</b>.", "Lô hàng bị giao thiếu hai thùng."),
  ("dent", "/dent/", "n", "vết móp", "There's a big <b>dent</b> on the side of the container.", "Có một vết móp lớn ở hông container."),
  ("wet damage", "/ˌwet ˈdæmɪdʒ/", "n", "hư hỏng do ướt, ngấm nước", "Ten cartons have <b>wet damage</b> from the rain.", "Mười thùng bị ướt do mưa."),
  ("survey report", "/ˈsɜːveɪ rɪˌpɔːt/", "n", "biên bản giám định", "The insurer needs the <b>survey report</b> to process our claim.", "Bên bảo hiểm cần biên bản giám định để xử lý hồ sơ bồi thường."),
  ("liable", "/ˈlaɪəbl/", "adj", "chịu trách nhiệm (pháp lý)", "The carrier may be <b>liable</b> for damage during the voyage.", "Hãng tàu có thể phải chịu trách nhiệm với hư hỏng trong hành trình."),
  ("mishandling", "/ˌmɪsˈhændlɪŋ/", "n", "xếp dỡ, vận chuyển sai cách", "The damage was caused by <b>mishandling</b> at the port.", "Hư hỏng là do xếp dỡ không đúng cách ở cảng."),
  ("crushed", "/krʌʃt/", "adj", "bị đè bẹp", "The bottom cartons were <b>crushed</b>.", "Mấy thùng ở dưới bị đè bẹp."),
  ("notify", "/ˈnəʊtɪfaɪ/", "v", "thông báo (chính thức)", "Please <b>notify</b> the carrier within three days.", "Nhớ thông báo cho hãng tàu trong vòng ba ngày."),
  ("replacement", "/rɪˈpleɪsmənt/", "n", "hàng thay thế", "The supplier will send a <b>replacement</b> next week.", "Nhà cung cấp sẽ gửi hàng thay thế vào tuần sau."),
 ],
 "phrases": [
  ("Some cartons arrived damaged.", "Một số thùng về đến nơi bị hư hỏng."),
  ("Please take photos before you unload anything.", "Chụp ảnh trước khi dỡ bất cứ thứ gì nhé."),
  ("Write the damage on the delivery note before you sign.", "Ghi chú hư hỏng lên phiếu giao hàng trước khi ký."),
  ("We've notified the carrier and the insurer.", "Bên mình đã thông báo cho hãng tàu và công ty bảo hiểm."),
  ("A surveyor will inspect the goods tomorrow.", "Ngày mai giám định viên sẽ kiểm tra hàng."),
  ("We'd like to file a claim for the damaged goods.", "Chúng tôi muốn làm hồ sơ đòi bồi thường cho số hàng hư hỏng."),
  ("Could you send a replacement with the next shipment?", "Anh/chị gửi hàng thay thế kèm lô sau được không?"),
  ("Please issue a credit note for the missing items.", "Anh/chị xuất credit note cho số hàng bị thiếu giúp nhé."),
  ("We'll send you the photos and the survey report today.", "Hôm nay bên mình sẽ gửi ảnh và biên bản giám định."),
 ],
 "dialogues": [
  ("We received the goods, but 20 cartons are damaged.", [
    ("I'm very sorry. Could you send me photos of the cartons and the signed delivery note?", True, "Xin lỗi + xin bằng chứng cần thiết để xử lý khiếu nại."),
    ("Not possible. We pack very good.", False, "Phủ nhận khi chưa kiểm tra; 'very good' phải là 'very well'."),
    ("Damaged is not my department.", False, "Né trách nhiệm, sai ngữ pháp."),
  ]),
  ("Who will pay for the damage?", [
    ("It depends on the cause. We'll notify the insurer, and a surveyor will check the goods first.", True, "Trả lời trung thực + quy trình xác định trách nhiệm."),
    ("You pay, because you signed.", False, "Đổ lỗi vội vàng, không theo quy trình giám định."),
    ("Insurance pay all, easy.", False, "Hứa sai — chưa chắc bảo hiểm bồi thường toàn bộ; thiếu 's' ('pays')."),
  ]),
  ("The shipment is short by two cartons.", [
    ("Thanks for letting us know. I'll check our loading records and get back to you by tomorrow.", True, "Cảm ơn + kiểm tra hồ sơ xếp hàng + hẹn thời gian."),
    ("Impossible, we count already.", False, "Phủ nhận ngay, sai thì ('We counted them')."),
    ("Two cartons only, small problem.", False, "Xem nhẹ vấn đề của khách."),
  ]),
  ("Should I sign the delivery note? Some boxes are wet.", [
    ("Yes, but please write 'ten cartons wet' on it before you sign, and take photos.", True, "Hướng dẫn đúng nghiệp vụ: ghi chú bảo lưu trước khi ký + chụp ảnh."),
    ("No, don't sign. Send the truck back.", False, "Quá cứng — trả cả xe gây thêm chi phí; nên nhận và ghi chú hư hỏng."),
    ("Sign first, talk later.", False, "Sai nghiệp vụ — ký sạch sẽ khó đòi bồi thường về sau."),
  ]),
  ("Can you send a replacement quickly?", [
    ("Yes. We'll ship the replacement by air on Monday at our cost.", True, "Đồng ý + phương thức + thời gian + ai chịu phí."),
    ("Yes, I send quickly quickly.", False, "Lặp từ kiểu tiếng Việt và thiếu 'will'."),
    ("Replacement needs three months.", False, "Không đưa phương án khả thi, thiếu thiện chí."),
  ]),
 ],
 "listen": [
  ("Twenty cartons arrived with wet damage", ["cartons", "wet"], "hàng bị ướt"),
  ("Please take photos before you sign", ["photos", "sign"], "chụp ảnh trước khi ký"),
  ("The surveyor will come tomorrow morning", ["surveyor", "morning"], "lịch giám định"),
  ("We'll send a replacement next week", ["replacement", "week"], "hàng thay thế"),
  ("When we opened the container, the bottom cartons were crushed. We took photos and notified the carrier. The surveyor is coming at ten.", ["opened", "crushed", "surveyor"], "báo hàng bị bẹp"),
  ("We're sorry about the missing items. We'll issue a credit note today. The replacement will be on the next vessel.", ["missing", "credit", "vessel"], "nhà cung cấp phản hồi khiếu nại"),
 ],
})

# ───────────────────────── 9. Họp vận hành & báo cáo ─────────────────────────
PHASES.append({
 "title": "Họp vận hành & báo cáo",
 "vocab": [
  ("on-time delivery", "/ˌɒn ˌtaɪm dɪˈlɪvəri/", "n", "(tỷ lệ) giao hàng đúng hạn", "Our <b>on-time delivery</b> rate was 96% last month.", "Tỷ lệ giao hàng đúng hạn tháng trước là 96%.", "納期遵守率", "nōki junshuritsu"),
  ("backlog", "/ˈbæklɒɡ/", "n", "lượng đơn/hàng tồn đọng", "We have a <b>backlog</b> of 30 orders after the holiday.", "Sau kỳ nghỉ, bên mình tồn 30 đơn chưa xử lý."),
  ("volume", "/ˈvɒljuːm/", "n", "khối lượng hàng, sản lượng", "Import <b>volume</b> went up by 15% this quarter.", "Sản lượng nhập khẩu quý này tăng 15%.", "物量", "butsuryō"),
  ("peak season", "/ˌpiːk ˈsiːzn/", "n", "mùa cao điểm", "Rates always go up in <b>peak season</b>.", "Mùa cao điểm giá cước lúc nào cũng tăng.", "繁忙期", "hanbōki"),
  ("carrier", "/ˈkæriə/", "n", "hãng vận chuyển (hãng tàu, hãng bay…)", "We're using two <b>carriers</b> on the Japan route.", "Tuyến Nhật bên mình đang dùng hai hãng tàu.", "運送会社", "unsō gaisha"),
  ("logistics cost", "/ləˈdʒɪstɪks kɒst/", "n", "chi phí logistics", "<b>Logistics cost</b> is 8% of our sales.", "Chi phí logistics chiếm 8% doanh thu.", "物流コスト", "butsuryū kosuto"),
  ("turnaround time", "/ˈtɜːnəraʊnd taɪm/", "n", "thời gian xử lý (một vòng)", "Our <b>turnaround time</b> for documents is one day.", "Thời gian xử lý chứng từ của bên mình là một ngày."),
  ("workaround", "/ˈwɜːkəraʊnd/", "n", "giải pháp tạm thời", "As a <b>workaround</b>, we'll ship the urgent items by air.", "Tạm thời bên mình sẽ gửi hàng gấp bằng đường hàng không."),
  ("flag", "/flæɡ/", "v", "nêu lên, cảnh báo (vấn đề)", "I want to <b>flag</b> a risk for next week's shipments.", "Tôi muốn nêu một rủi ro cho các lô tuần sau."),
  ("contingency plan", "/kənˈtɪndʒənsi plæn/", "n", "phương án dự phòng", "We need a <b>contingency plan</b> for the typhoon season.", "Mình cần phương án dự phòng cho mùa bão."),
 ],
 "phrases": [
  ("This week we shipped 25 containers.", "Tuần này bên mình đã xuất 25 container."),
  ("Our on-time delivery rate is 94%, down from 97%.", "Tỷ lệ giao đúng hạn là 94%, giảm từ 97%."),
  ("Three shipments are delayed because of port congestion.", "Ba lô bị chậm do ùn tắc cảng."),
  ("I'd like to flag a risk for next week.", "Tôi muốn nêu một rủi ro cho tuần sau."),
  ("Freight rates are going up because of the peak season.", "Giá cước đang tăng do mùa cao điểm."),
  ("As a workaround, we can ship the urgent parts by air.", "Tạm thời mình có thể gửi phụ tùng gấp bằng đường hàng không."),
  ("We need a backup carrier on this route.", "Tuyến này mình cần một hãng tàu dự phòng."),
  ("The next step is to confirm space with the carrier.", "Bước tiếp theo là xác nhận chỗ với hãng tàu."),
  ("I'll share the updated report after the meeting.", "Tôi sẽ gửi báo cáo cập nhật sau cuộc họp."),
 ],
 "dialogues": [
  ("Can you give us a quick update on this week's shipments?", [
    ("Sure. We shipped 25 containers. Two are delayed at Singapore, and the new ETA is Monday.", True, "Báo cáo ngắn gọn: số liệu + vấn đề + ETA mới."),
    ("This week many containers, OK all.", False, "Không có số liệu, câu lộn xộn."),
    ("We ship 25 containers.", False, "Sai thì: 'We shipped' (đã xảy ra)."),
  ]),
  ("Why did on-time delivery go down this month?", [
    ("Mainly because of port congestion. Four of the six late shipments were stuck at the same port.", True, "Nêu nguyên nhân chính + số liệu chứng minh."),
    ("Because many problems.", False, "Mơ hồ, thiếu 'there were': 'Because there were many problems.'"),
    ("It's not our fault, it's the carrier.", False, "Đổ lỗi, không phân tích nguyên nhân."),
  ]),
  ("What's your plan for the peak season?", [
    ("We'll book space two weeks earlier and add a backup carrier on the Japan route.", True, "Kế hoạch cụ thể, dùng 'will' cho dự định."),
    ("Peak season we will try our best.", False, "Nói chung chung, không có hành động cụ thể."),
    ("We book early.", False, "Thiếu 'will' và quá ngắn, chưa rõ kế hoạch."),
  ]),
  ("Is there anything you'd like to flag?", [
    ("Yes. A typhoon may close Hai Phong port next week, so some shipments could be delayed.", True, "Nêu rủi ro + ảnh hưởng dự kiến."),
    ("No flag.", False, "Dịch sát chữ 'flag', nghe kỳ: 'Nothing from me.' / 'No, nothing to flag.'"),
    ("Typhoon come, maybe delay.", False, "Thiếu mạo từ, chia động từ sai: 'A typhoon is coming, so there may be delays.'"),
  ]),
  ("How can we reduce our logistics cost?", [
    ("We could consolidate small orders into FCL shipments and negotiate yearly rates with carriers.", True, "Đề xuất cụ thể bằng 'could' — lịch sự, thuyết phục."),
    ("Cost reduce is difficult.", False, "Sai trật tự ('Reducing cost is difficult') và không đề xuất."),
    ("Use the cheapest carrier always.", False, "Đơn giản hoá quá mức — giá rẻ có thể làm giảm tỷ lệ đúng hạn."),
  ]),
 ],
 "listen": [
  ("Our on-time delivery rate was ninety-four percent", ["on-time", "ninety-four"], "tỷ lệ đúng hạn"),
  ("I'd like to flag a risk for next week", ["flag", "risk"], "nêu rủi ro"),
  ("Freight rates are going up in peak season", ["rates", "peak"], "giá cước tăng"),
  ("As a workaround we'll ship by air", ["workaround", "air"], "giải pháp tạm"),
  ("This week we shipped 25 containers and received 12. Two shipments are delayed because of bad weather. The next step is to update the customers.", ["shipped", "weather", "customers"], "báo cáo tuần"),
  ("Volume is up 20% this month. We have a backlog of 15 orders in the warehouse. I suggest we add a Saturday shift.", ["Volume", "backlog", "Saturday"], "đề xuất trong họp vận hành"),
 ],
})

# ───────────────────────── Vai trò (roles) ─────────────────────────
ROLES = {
 "docs": {"label": "Chứng từ XNK", "emoji": "📄",
  "scenarios": [
   ("dc_draft", "Xác nhận nháp B/L", "You are a foreign buyer's import coordinator. I send you a draft B/L. Point out that the consignee address is wrong and ask when the final B/L will be issued."),
   ("dc_co", "Hỏi về C/O", "You are a foreign buyer. Ask me which certificate of origin I can provide, when you will get the original and whether you will get the lower duty rate."),
   ("dc_mismatch", "Chứng từ không khớp", "You are a customs broker abroad. The weight on the commercial invoice does not match the packing list. Ask me to explain and send corrected documents."),
   ("dc_release", "Điện giao hàng", "You are a buyer whose goods have arrived at the port, but you have not received the original B/L. Ask me about a telex release and what you need to do."),
  ],
  "dialogues": [
   ("The consignee address on the draft B/L is wrong.", [
     ("Thanks for pointing that out. Could you send me the correct address? I'll ask the carrier to amend it today.", True, "Cảm ơn + xin thông tin đúng + hành động cụ thể."),
     ("Not my mistake, the carrier type.", False, "Đổ lỗi và sai thì ('typed'). Khách chỉ cần sửa kịp."),
     ("OK, B/L already issue, cannot change.", False, "Sai ngữ pháp ('has been issued') và từ chối khi chưa hỏi hãng tàu.")]),
   ("When will we get the original documents?", [
     ("We'll courier them on Friday. I'll send you the tracking number once they're picked up.", True, "Ngày gửi + cam kết gửi mã vận đơn."),
     ("Friday I send, maybe.", False, "Trật tự từ kiểu Việt, thiếu 'will', thêm 'maybe' làm mất tin tưởng."),
     ("Original not needed, use copy.", False, "Sai — nhiều trường hợp cần bộ gốc để nhận hàng/thông quan.")]),
   ("Can you provide a certificate of origin?", [
     ("Yes. We can apply for Form D, and I'll send you a copy as soon as it's issued.", True, "Xác nhận + loại C/O + khi nào gửi. C/O do cơ quan có thẩm quyền cấp, người xuất khẩu chỉ xin cấp."),
     ("Yes, have.", False, "Thiếu chủ ngữ và động từ: 'Yes, we can provide one.'"),
     ("C/O is expensive, you really need?", False, "Sai cấu trúc câu hỏi và làm khó khách.")]),
   ("The invoice value and the L/C amount are different.", [
     ("You're right. The invoice should be 45,200 dollars. I'll reissue it so it matches the L/C.", True, "Thừa nhận + con số đúng + xử lý để khớp L/C."),
     ("Different a little is OK.", False, "Sai nghiệp vụ — ngân hàng từ chối thanh toán nếu chứng từ không khớp L/C."),
     ("Bank will fix it.", False, "Đẩy việc sai chỗ; người xuất khẩu phải sửa chứng từ.")]),
   ("Our goods are at the port, but we don't have the B/L.", [
     ("We've received your payment, so I'll ask the carrier for a telex release. Then you can get the goods without the original B/L.", True, "Giải pháp đúng: điện giao hàng sau khi đã thanh toán."),
     ("Wait for the original, maybe one week.", False, "Không đưa giải pháp, khách sẽ bị tính phí lưu bãi."),
     ("Why you don't have?", False, "Sai trật tự câu hỏi và nghe như trách khách.")]),
   ("Please send all the documents by email first.", [
     ("Sure. I'll send the invoice, packing list, B/L copy and C/O in one email this afternoon.", True, "Liệt kê bộ chứng từ + thời gian gửi."),
     ("OK, I send all.", False, "Thiếu 'will' và không nói thời gian."),
     ("Email is not safe.", False, "Từ chối không cần thiết, không đưa phương án khác.")]),
  ]},
 "warehouse": {"label": "Kho vận", "emoji": "🏬",
  "scenarios": [
   ("wh_receive", "Nhận hàng thiếu", "You are a supplier's sales coordinator. I work in the warehouse and I call to say we received fewer cartons than the packing list. Ask for details and evidence."),
   ("wh_visit", "Khách tham quan kho", "You are a foreign client visiting our warehouse for the first time. Ask about the storage capacity, the picking process and how we control stock accuracy."),
   ("wh_urgent", "Đơn gấp trong ngày", "You are a customer with an urgent order. Ask if we can pick, pack and ship 200 cartons today, and what time the truck can leave."),
   ("wh_count", "Chênh lệch kiểm kê", "You are my foreign manager. After the stock count, 15 units of an expensive item are missing. Ask me what happened and what we will do next."),
  ],
  "dialogues": [
   ("How many pallets can this warehouse hold?", [
     ("About 5,000 pallets. We're at 80% capacity at the moment.", True, "Con số cụ thể + tình trạng hiện tại."),
     ("Very big, a lot of pallets.", False, "Không có số liệu, khách không đánh giá được."),
     ("It can hold 5,000 pallet.", False, "Thiếu 's' số nhiều: '5,000 pallets'.")]),
   ("How do you make sure the stock is accurate?", [
     ("We scan every pallet in and out, and we do cycle counts every week.", True, "Mô tả quy trình kiểm soát cụ thể."),
     ("Our staff is very careful.", False, "Chung chung, không nói quy trình."),
     ("We count when have time.", False, "Thiếu chủ ngữ và nghe thiếu kiểm soát.")]),
   ("Can you ship 200 cartons today?", [
     ("Yes, if we get the order by 11 a.m. The truck can leave at 4 p.m.", True, "Đồng ý có điều kiện + giờ chốt + giờ xe chạy."),
     ("Yes, easy!", False, "Hứa suông, không có mốc thời gian."),
     ("200 is too many today, no can.", False, "Sai ngữ pháp ('we can't') và từ chối không đề xuất phương án.")]),
   ("Why are 15 units missing after the stock count?", [
     ("We're still checking. Some may be in the wrong location. I'll report the result by tomorrow noon.", True, "Trung thực + giả thuyết + hạn báo cáo."),
     ("Maybe the night shift take.", False, "Buộc tội vô căn cứ, sai thì ('took')."),
     ("15 is small, not important.", False, "Xem nhẹ thất thoát, không chuyên nghiệp.")]),
   ("Do you use FIFO?", [
     ("Yes, we do. For food items we use FEFO, so products that expire first are shipped first.", True, "Trả lời đúng + thêm thông tin chuyên môn phù hợp."),
     ("Yes, FIFO have.", False, "Dịch từng chữ: 'Yes, we use FIFO.'"),
     ("FIFO? Maybe.", False, "Mơ hồ, thiếu hiểu biết cơ bản về kho.")]),
   ("The truck is here, but the goods aren't ready.", [
     ("I'm sorry. We need 30 more minutes to finish packing. Could the driver wait at dock 2?", True, "Xin lỗi + thời gian cần thêm + đề nghị cụ thể."),
     ("Truck come too early.", False, "Đổ lỗi, sai chia động từ ('came')."),
     ("Tell driver go back.", False, "Cộc lốc, gây thêm chi phí và trễ hàng.")]),
  ]},
 "forwarding": {"label": "Forwarder · Vận tải", "emoji": "🚢",
  "scenarios": [
   ("fw_quote", "Báo giá cước cho khách", "You are a foreign customer asking me, a freight forwarder, for a sea freight rate from Vietnam to Los Angeles. Ask about the transit time, surcharges and validity."),
   ("fw_rollover", "Báo rớt tàu", "You are a customer. I call to tell you your container was rolled over. Be unhappy, ask why, and ask what I can do to limit the delay."),
   ("fw_dem", "Phí lưu bãi", "You are a customer who received a big demurrage invoice. Ask me why you have to pay it and whether we can reduce it."),
   ("fw_air", "Chuyển sang hàng air", "You are a customer who needs part of an order urgently. Ask me about the cost and time of shipping 300 kilos by air instead of by sea."),
  ],
  "dialogues": [
   ("What's your best rate to Los Angeles?", [
     ("For a 40-foot container, it's 2,100 dollars, valid until the 30th. Transit time is about 22 days.", True, "Giá + thời hạn + thời gian vận chuyển."),
     ("Best rate is very cheap, trust me.", False, "Không có con số, thiếu chuyên nghiệp."),
     ("Rate 2,100.", False, "Câu cụt, thiếu loại container và thời hạn.")]),
   ("Why was my container rolled over?", [
     ("The vessel was overbooked. I'm sorry. I've already booked you on the next vessel, which leaves in three days.", True, "Nguyên nhân + xin lỗi + giải pháp đã làm."),
     ("It is not me, it is the shipping line.", False, "Đổ lỗi, chưa xin lỗi hay đưa giải pháp."),
     ("Roll over happen always.", False, "Sai ngữ pháp và coi thường vấn đề của khách.")]),
   ("Why do I have to pay demurrage?", [
     ("The container stayed at the port for nine days, and you had five free days. I'll ask the carrier if they can waive part of it.", True, "Giải thích bằng số liệu + chủ động hỗ trợ giảm phí."),
     ("Because you pick up late.", False, "Sai thì ('picked') và nghe như trách khách."),
     ("I don't know, just pay.", False, "Thiếu giải thích, thiếu tôn trọng.")]),
   ("How much would it cost to send 300 kilos by air?", [
     ("About 4.5 dollars per kilo, so around 1,350 dollars. It can arrive in three days.", True, "Đơn giá + tổng tiền ước tính + thời gian."),
     ("Air is very expensive, don't do.", False, "Quyết định thay khách, không báo giá."),
     ("It cost 4.5 per kilo.", False, "Thiếu 's' ('costs') và thiếu tổng tiền, thời gian.")]),
   ("Can you track my container for me?", [
     ("Sure. It's on the vessel near Hong Kong now. The ETA in Hai Phong is still Tuesday.", True, "Vị trí hiện tại + ETA."),
     ("You can check website yourself.", False, "Đẩy việc lại cho khách, thiếu mạo từ ('the website')."),
     ("Container is fine, don't worry.", False, "Không có thông tin cụ thể.")]),
   ("Can you arrange door-to-door delivery?", [
     ("Yes. We'll handle export clearance, sea freight, import clearance and trucking to your warehouse.", True, "Liệt kê rõ các khâu trong dịch vụ door-to-door."),
     ("Yes, we can do all thing.", False, "Sai số nhiều ('everything') và mơ hồ."),
     ("Door-to-door is difficult, maybe no.", False, "Không rõ ràng, không giải thích lý do.")]),
  ]},
 "purchasing": {"label": "Mua hàng · Nhà cung cấp", "emoji": "🛒",
  "scenarios": [
   ("pu_new", "Tìm nhà cung cấp mới", "You are a sales manager at a foreign supplier. I am a buyer looking for a new vendor. Answer my questions about MOQ, lead time, prices and samples."),
   ("pu_late", "Nhà cung cấp giao trễ", "You are a supplier who has to delay a shipment by two weeks because of a raw material shortage. I am the buyer. Explain the delay and respond to my requests."),
   ("pu_price", "Thương lượng tăng giá", "You are a supplier who wants to raise prices by 8% next quarter. I am the buyer. Explain why, and agree to a smaller increase only if I negotiate well."),
   ("pu_quality", "Phàn nàn chất lượng", "You are a supplier's account manager. I call to complain that 5% of the last shipment was defective. Ask for details and discuss a solution."),
  ],
  "dialogues": [
   ("What quantity are you looking for?", [
     ("About 3,000 units per month. We'd like to start with a trial order of 500.", True, "Số lượng dự kiến + đề xuất đơn thử."),
     ("Many, many units.", False, "Không có số liệu, không chuyên nghiệp."),
     ("We are want 3,000.", False, "Thừa 'are': 'We want 3,000.'")]),
   ("We need to delay your shipment by two weeks.", [
     ("That's a serious problem for our production. Can you ship at least half of the order on the original date?", True, "Nêu tác động + đề xuất giao từng phần."),
     ("Two weeks? You crazy!", False, "Thô lỗ, thiếu động từ."),
     ("OK, no problem.", False, "Chấp nhận ngay, không bảo vệ lợi ích công ty.")]),
   ("Our prices will increase by 8% next quarter.", [
     ("I understand costs are rising, but 8% is too high for us. Could we agree on 3%?", True, "Thông cảm + nêu quan điểm + đề xuất con số."),
     ("No increase. We change supplier.", False, "Đe doạ cộc lốc, dễ làm hỏng quan hệ."),
     ("Why price increase so much?", False, "Thiếu trợ động từ: 'Why are prices increasing so much?'")]),
   ("Can you send us your forecast for next quarter?", [
     ("Sure. I'll send the forecast by Friday. It's about 9,000 units in total.", True, "Đồng ý + hạn gửi + con số ước lượng."),
     ("Forecast is difficult, I don't know.", False, "Né yêu cầu; có thể gửi số ước tính và cập nhật sau."),
     ("Yes, I send you next week maybe.", False, "Thiếu 'will', 'maybe' làm nhà cung cấp khó lập kế hoạch.")]),
   ("Can you issue the PO today?", [
     ("Yes. Once you confirm the unit price and lead time, I'll send the PO within an hour.", True, "Đồng ý có điều kiện rõ ràng + thời gian."),
     ("PO need approve first.", False, "Sai ngữ pháp: 'The PO needs approval first.' — cũng chưa nói khi nào."),
     ("Why so hurry?", False, "Sai ngữ pháp ('Why the hurry?') và nghe khó chịu.")]),
   ("5% of our last shipment was defective? Can you send photos?", [
     ("Of course. I'll email the photos and the inspection report today. We'd like replacements with the next order.", True, "Đồng ý + bằng chứng + yêu cầu giải pháp cụ thể."),
     ("You don't believe me?", False, "Tự ái; nhà cung cấp xin ảnh là yêu cầu bình thường."),
     ("Photos is many, I send later.", False, "Sai chia động từ ('are') và trì hoãn.")]),
  ]},
}

# ───────────────────────── Gói ─────────────────────────
PACK = {
 "id": "logistics",
 "label": "Logistics · Xuất nhập khẩu",
 "short": "Logistics",
 "emoji": "🚚",
 "desc": "Chứng từ · kho · vận tải · mua hàng",
 "persona": "a Vietnamese logistics and import-export worker",
 "counterpart": "a foreign supplier, forwarder or customer",
 "context": "logistics and import-export",
 "core": [3, 11],
 "report": {
  "title": "Báo cáo lô hàng 60 giây", "short": "Báo cáo lô hàng", "sub": "Nói như họp vận hành 🎙️",
  "steps": [["Shipments", "This week we shipped … containers …"], ["Issues", "One shipment is delayed because … / No issues."], ["Next steps", "Next, we will …"]],
  "kind": "shipment status update",
  "structure": "shipment status / delays or issues / next steps",
  "sample": "This week we shipped 18 containers to Japan and received six from China. One container to Osaka was rolled over, so the new ETA is next Tuesday. Next, we will inform the customer today and book space two weeks earlier for the peak season.",
 },
 "podcast": "Podcast logistics",
 "game_tag": "Game anime: đánh quái chứng từ sai, hạ boss rớt tàu",
 "reverse_tag": "kiểu logistics",
 "jd_placeholder": "VD: Nhân viên chứng từ XNK ở Hải Phòng, làm với nhà cung cấp Nhật/Hàn, booking tàu, B/L, C/O, thông quan…",
 "rw_placeholder": "VD: container bị rớt tàu, khách Nhật hỏi ETA mới",
 "quips": [
  "Container loaded!",
  "Where's my B/L?",
  "Customs cleared!",
  "ETA confirmed!",
  "Cut-off in one hour!",
  "Space booked!",
  "One more pallet…",
  "Tracking, tracking, tracking…",
  "Delivered on time!",
  "Stock count done!",
 ],
 "ai": [
  ("rate", "Hỏi giá cước & booking", "You are a freight forwarder. I am a Vietnamese shipper asking for a rate for one 40-foot container to Busan. Give a rate, mention surcharges and the cut-off, and ask for the cargo details."),
  ("docs", "Kiểm tra chứng từ", "You are a foreign buyer checking my draft B/L, commercial invoice and packing list. Find one mismatch in the weight and ask me to amend it."),
  ("customs", "Thông quan bị kiểm hoá", "You are my foreign customer. Your imported goods are in customs and were selected for physical inspection. Ask me why, when the goods will be cleared and how much duty you will pay."),
  ("delay", "Báo lô hàng chậm", "You are a foreign customer whose shipment is late. Ask me for a status update, the reason and the new ETA. Be a little impatient until I give a clear plan."),
  ("supplier", "Làm việc với nhà cung cấp", "You are a foreign supplier. I am the buyer. Tell me the lead time is eight weeks and the MOQ is 1,000 pieces. Negotiate with me if I ask politely."),
  ("incoterms", "Thương lượng điều kiện giao hàng", "You are a foreign buyer negotiating a new contract with me. Ask whether my price is FOB or CIF, who pays insurance and what the payment terms are."),
  ("claim", "Khiếu nại hàng hư hỏng", "You are a foreign customer. Ten cartons of your shipment arrived crushed. Complain politely but firmly and ask what we will do, including a replacement or credit note."),
  ("ops", "Họp vận hành với sếp", "You are my foreign logistics manager. Ask me for a quick update on this week's shipments, any delays, and my plan for the peak season. Ask one follow-up question."),
 ],
 "rev": [
  ("Lô hàng đã thông quan sáng nay.", "The shipment cleared customs this morning."),
  ("ETA mới là thứ Năm.", "The new ETA is Thursday."),
  ("Container của mình bị rớt tàu.", "Our container was rolled over."),
  ("Anh/chị kiểm tra giúp bản nháp B/L nhé.", "Please check the draft B/L."),
  ("Giờ cắt máng là trưa thứ Tư.", "The cut-off is Wednesday at noon."),
  ("Packing list không khớp với hoá đơn.", "The packing list doesn't match the invoice."),
  ("Hàng đã về kho lúc 10 giờ.", "The goods arrived at the warehouse at 10."),
  ("Mình cần lấy container trước thứ Sáu.", "We need to pick up the container by Friday."),
  ("Giá này là FOB Hải Phòng.", "This price is FOB Hai Phong."),
  ("Tuần này tàu hết chỗ rồi.", "There's no space on this week's vessel."),
  ("Nhà cung cấp sẽ giao từng phần.", "The supplier will make a partial shipment."),
  ("Mười thùng bị ướt do mưa.", "Ten cartons were damaged by rain."),
  ("Thứ Bảy này bên mình kiểm kê kho.", "We're doing a stock count this Saturday."),
  ("Tôi sẽ gửi bộ chứng từ gốc vào ngày mai.", "I'll send the original documents tomorrow."),
 ],
 "reading": [
  {"t": "Booking confirmation", "text": "BOOKING CONFIRMATION – No. HPH240518\nShipper: Minh Phat Furniture Co.\nPort of loading: Hai Phong  →  Port of discharge: Busan\nEquipment: 2 x 40' HC\nVessel: Pacific Star V.215  ETD: 18 May\nCargo cut-off: 16 May, 17:00  |  SI cut-off: 15 May, 12:00\nEmpty containers available from 12 May at Depot 3.", "q": [
    {"q": "When must the shipping instructions be sent?", "o": ["15 May, 12:00", "16 May, 17:00", "18 May"], "a": 0},
    {"q": "Where can the shipper get the empty containers?", "o": ["At Busan port", "At Depot 3", "At the factory"], "a": 1}]},
  {"t": "Email from buyer", "text": "Subject: Draft B/L – PO 7731\nHi Hoa,\nThanks for the draft B/L. Two changes, please:\n1. Consignee: our new address is 22 Harbour Road, Osaka.\n2. Gross weight should be 11,850 kg, as on the packing list.\nEverything else is fine. Please confirm before the vessel leaves on Friday.\nBest regards,\nYuki", "q": [
    {"q": "How many changes does Yuki ask for?", "o": ["One", "Two", "Three"], "a": 1},
    {"q": "Where is the correct weight?", "o": ["On the invoice", "On the packing list", "On the C/O"], "a": 1}]},
  {"t": "Delay notice", "text": "SCHEDULE UPDATE\nDue to port congestion in Singapore, vessel Ocean Bay V.88 is delayed.\nOld ETA Cat Lai: 3 June  →  Revised ETA: 6 June.\nContainers for transshipment will connect to the next available vessel. We apologise for the inconvenience and will send another update on 4 June.", "q": [
    {"q": "Why is the vessel late?", "o": ["Bad weather", "Port congestion", "A customs inspection"], "a": 1},
    {"q": "How many days late is the vessel?", "o": ["Two", "Three", "Six"], "a": 1}]},
  {"t": "Warehouse notice", "text": "WAREHOUSE NOTICE\nQuarterly stock count: Saturday 29 June, 7:00–15:00.\n- No receiving or picking during the count.\n- Urgent orders must be shipped by Friday 16:00.\n- Team leaders: collect scanners at the office at 6:45.\nThank you for your cooperation.", "q": [
    {"q": "When must urgent orders be shipped?", "o": ["Saturday 7:00", "Friday 16:00", "Saturday 15:00"], "a": 1},
    {"q": "What will team leaders collect?", "o": ["Scanners", "Keys", "Forklifts"], "a": 0}]},
  {"t": "Supplier message", "text": "Hi Nam, sorry for the bad news. Our raw material arrived late, so we can't ship all 2,000 units on 10 July. We can ship 1,200 on 10 July and the other 800 on 24 July. Please let me know if a partial shipment is OK. – Lisa, Sales", "q": [
    {"q": "How many units can ship on 10 July?", "o": ["800", "1,200", "2,000"], "a": 1},
    {"q": "What does Lisa need from Nam?", "o": ["A new PO", "Payment", "Approval for a partial shipment"], "a": 2}]},
 ],
 "events": [
  ("audit", "Khách hàng đánh giá kho", "You are a foreign client auditing our warehouse before signing a contract. Ask about storage conditions, safety, stock accuracy and how we handle damaged goods."),
  ("tender", "Đấu thầu cước năm", "You are the logistics manager of a foreign company choosing a forwarder for next year. Ask about our rates, carriers, transit times and how we handle delays."),
  ("supplier_visit", "Thăm nhà cung cấp", "You are a foreign supplier visiting our office. Discuss lead times, the next quarter's forecast, packaging and a small price increase."),
  ("peak", "Chuẩn bị mùa cao điểm", "You are my foreign manager. Ask me how we will prepare for the peak season: space bookings, warehouse capacity and backup plans."),
  ("claim_meeting", "Họp xử lý khiếu nại", "You are an unhappy customer whose shipment arrived with wet damage. In a meeting, ask for the survey result, who is liable and what compensation we offer."),
  ("interview", "Phỏng vấn vị trí XNK", "You are a hiring manager at a foreign logistics company. Interview me for an import-export coordinator job. Ask about Incoterms, documents and a problem I solved."),
  ("other", "Khác", ""),
 ],
 "roles": ROLES,
 "phases": PHASES,
}
