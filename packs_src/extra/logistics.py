# -*- coding: utf-8 -*-
# v4.1 — nội dung làm giàu cho gói logistics (nối vào cuối gói, xem build.py)
# Tên công ty / người / số hiệu đều là tên tự đặt.

PHASES = []

# ───────────────────────── 10. Vận tải hàng không ─────────────────────────
PHASES.append({
 "title": "Vận tải hàng không",
 "vocab": [
  ("air waybill", "/ˈeə ˌweɪbɪl/", "n", "vận đơn hàng không (AWB)", "Please send me the <b>air waybill</b> number so I can track the cargo.", "Anh/chị gửi tôi số vận đơn hàng không để tôi theo dõi hàng nhé.", "航空運送状", "kōkū unsōjō"),
  ("chargeable weight", "/ˌtʃɑːdʒəbl ˈweɪt/", "n", "trọng lượng tính cước", "The <b>chargeable weight</b> is 180 kilos, not 120.", "Trọng lượng tính cước là 180 ký, không phải 120."),
  ("volumetric weight", "/ˌvɒljʊˈmetrɪk ˈweɪt/", "n", "trọng lượng thể tích (quy đổi từ kích thước)", "These boxes are light but big, so the <b>volumetric weight</b> is higher.", "Mấy thùng này nhẹ nhưng cồng kềnh nên trọng lượng thể tích cao hơn."),
  ("airline", "/ˈeəlaɪn/", "n", "hãng hàng không, hãng bay", "The <b>airline</b> has confirmed space on Tuesday's flight.", "Hãng bay đã xác nhận chỗ trên chuyến thứ Ba."),
  ("direct flight", "/dəˌrekt ˈflaɪt/", "n", "chuyến bay thẳng", "A <b>direct flight</b> to Frankfurt costs more, but it's faster.", "Bay thẳng đi Frankfurt đắt hơn nhưng nhanh hơn."),
  ("offload", "/ˌɒfˈləʊd/", "v", "rút hàng xuống (không cho lên chuyến bay)", "Our cargo was <b>offloaded</b> because the flight was full.", "Hàng của mình bị rút xuống vì chuyến bay đầy tải."),
  ("cargo terminal", "/ˈkɑːɡəʊ ˌtɜːmɪnl/", "n", "ga hàng hoá, kho hàng sân bay", "Please deliver the goods to the <b>cargo terminal</b> by 6 p.m.", "Vui lòng giao hàng đến kho hàng sân bay trước 6 giờ chiều."),
  ("security screening", "/sɪˈkjʊərəti ˌskriːnɪŋ/", "n", "soi chiếu an ninh", "All air cargo must go through <b>security screening</b>.", "Mọi hàng đi máy bay đều phải qua soi chiếu an ninh."),
  ("courier", "/ˈkʊriə/", "n", "dịch vụ chuyển phát nhanh (quốc tế)", "Small samples are cheaper to send by <b>courier</b>.", "Hàng mẫu nhỏ gửi chuyển phát nhanh sẽ rẻ hơn."),
  ("dimensions", "/daɪˈmenʃnz/", "n", "kích thước (dài × rộng × cao)", "The <b>dimensions</b> of each carton are 60 by 40 by 50 centimetres.", "Kích thước mỗi thùng là 60 x 40 x 50 cm."),
 ],
 "phrases": [
  ("What's the chargeable weight for this shipment?", "Lô này trọng lượng tính cước là bao nhiêu?"),
  ("Air freight is charged on the higher of actual and volumetric weight.", "Cước hàng không tính theo số lớn hơn giữa trọng lượng thực và trọng lượng thể tích."),
  ("Could you send me the weight and dimensions of each carton?", "Anh/chị gửi giúp tôi trọng lượng và kích thước từng thùng nhé."),
  ("Can we get space on tomorrow's flight?", "Mình lấy được chỗ trên chuyến bay ngày mai không?"),
  ("Is it a direct flight or via Hong Kong?", "Chuyến này bay thẳng hay quá cảnh Hồng Kông?"),
  ("The cargo was offloaded, so it will fly on the next flight.", "Hàng bị rút xuống nên sẽ đi chuyến bay sau."),
  ("Here's the AWB number for tracking.", "Đây là số AWB để theo dõi hàng."),
  ("For samples under 20 kilos, courier is usually cheaper.", "Hàng mẫu dưới 20 ký thì đi chuyển phát nhanh thường rẻ hơn."),
  ("The goods must pass security screening before loading.", "Hàng phải qua soi chiếu an ninh trước khi xếp lên máy bay."),
 ],
 "dialogues": [
  ("Why is the chargeable weight 250 kilos? Our cargo is only 150.", [
    ("The cartons are large, so we charge by volumetric weight. It's higher than the actual weight.", True, "Giải thích đúng cách tính cước air: lấy số lớn hơn giữa trọng lượng thực và trọng lượng thể tích."),
    ("Because the airline want more money.", False, "Sai chia động từ ('wants') và giải thích sai — cước tính theo trọng lượng thể tích."),
    ("250 is correct, no need explain.", False, "Thiếu 'to' ('no need to explain') và không giải thích cho khách."),
  ]),
  ("Can we get this shipment to Tokyo by Friday?", [
    ("Yes, if we deliver it to the cargo terminal by Wednesday noon. There's a direct flight on Thursday.", True, "Đồng ý có điều kiện + hạn giao ra sân bay + chuyến bay cụ thể."),
    ("Yes, sure, tomorrow arrive.", False, "Trật tự từ kiểu Việt và hứa không có căn cứ: 'It will arrive tomorrow.'"),
    ("Friday is maybe difficult because flight.", False, "Câu lộn xộn, thiếu 'of the' ('because of the flight') và chưa kiểm tra chuyến bay."),
  ]),
  ("Our cargo didn't fly last night. What happened?", [
    ("I'm sorry. The airline offloaded it because the flight was full. It's booked on tonight's flight.", True, "Xin lỗi + nguyên nhân + chuyến bay mới đã đặt."),
    ("It no fly because full.", False, "Thiếu trợ động từ và chủ ngữ: 'It didn't fly because the flight was full.'"),
    ("Ask the airline, not me.", False, "Đẩy việc cho khách — forwarder phải tự làm việc với hãng bay."),
  ]),
  ("Should we send these samples by air freight or courier?", [
    ("They're only 8 kilos, so courier is cheaper and faster. It's door-to-door, too.", True, "Tư vấn bằng số liệu + lợi ích cụ thể."),
    ("Courier more fast.", False, "Thiếu động từ 'is'; so sánh hơn là 'faster'."),
    ("Both OK, you choose.", False, "Không tư vấn, đẩy quyết định cho khách."),
  ]),
  ("Could you send me the AWB number?", [
    ("Sure. I've just emailed it to you. You can track the cargo on the airline's website.", True, "Đã gửi + hướng dẫn cách theo dõi."),
    ("AWB not yet have.", False, "Dịch từng chữ 'chưa có': 'We don't have it yet.' — và nên nói khi nào có."),
    ("I send you later maybe.", False, "Thiếu 'will' và tân ngữ ('I'll send it'), lại mơ hồ về thời gian."),
  ]),
 ],
 "listen": [
  ("The chargeable weight is two hundred kilos", ["chargeable", "hundred"], "trọng lượng tính cước"),
  ("Our cargo was offloaded from the flight", ["offloaded", "flight"], "hàng bị rút xuống"),
  ("Please send the dimensions of each carton", ["dimensions", "carton"], "xin kích thước thùng"),
  ("The samples will go by courier tomorrow", ["samples", "courier"], "gửi mẫu chuyển phát nhanh"),
  ("Hi Mai, your cargo passed security screening this morning. It's on tonight's direct flight to Seoul. I'll send the AWB copy in an hour.", ["screening", "direct", "AWB"], "forwarder báo hàng air"),
  ("The boxes weigh 300 kilos in total. But the volumetric weight is 420 kilos, so the airline will charge for 420.", ["weigh", "volumetric", "charge"], "giải thích cước air"),
 ],
})

# ───────────────────────── 11. Hàng lạnh & hàng nguy hiểm ─────────────────────────
PHASES.append({
 "title": "Hàng lạnh & hàng nguy hiểm",
 "vocab": [
  ("reefer", "/ˈriːfə/", "n", "container lạnh (reefer)", "We need a 40-foot <b>reefer</b> for the frozen shrimp.", "Mình cần một container lạnh 40 feet cho lô tôm đông lạnh.", "リーファーコンテナ", "rīfā kontena"),
  ("cold chain", "/ˌkəʊld ˈtʃeɪn/", "n", "chuỗi lạnh", "If the <b>cold chain</b> breaks, the fruit will go bad.", "Nếu đứt chuỗi lạnh thì trái cây sẽ hỏng.", "コールドチェーン", "kōrudo chēn"),
  ("set point", "/ˈset pɔɪnt/", "n", "nhiệt độ cài đặt (của container lạnh)", "The <b>set point</b> for this cargo is minus 18 degrees.", "Nhiệt độ cài đặt cho lô này là âm 18 độ."),
  ("perishable", "/ˈperɪʃəbl/", "adj", "dễ hỏng, mau hư (hàng tươi sống)", "<b>Perishable</b> goods must be cleared quickly.", "Hàng dễ hỏng phải được thông quan nhanh."),
  ("pre-cool", "/ˌpriː ˈkuːl/", "v", "làm lạnh trước (hàng, trước khi đóng vào container)", "The fruit must be <b>pre-cooled</b> before it goes into the reefer.", "Trái cây phải được làm lạnh trước khi đóng vào container lạnh."),
  ("dangerous goods", "/ˌdeɪndʒərəs ˈɡʊdz/", "n", "hàng nguy hiểm (DG)", "Lithium batteries are <b>dangerous goods</b>, so we need extra documents.", "Pin lithium là hàng nguy hiểm nên cần thêm chứng từ.", "危険物", "kikenbutsu"),
  ("safety data sheet", "/ˌseɪfti ˈdeɪtə ʃiːt/", "n", "bảng dữ liệu an toàn hoá chất (SDS/MSDS)", "The carrier asked for the <b>safety data sheet</b> of this chemical.", "Hãng tàu yêu cầu bảng dữ liệu an toàn của hoá chất này.", "安全データシート", "anzen dēta shīto"),
  ("UN number", "/ˌjuː ˈen ˌnʌmbə/", "n", "số UN (mã nhận dạng hàng nguy hiểm)", "Please write the <b>UN number</b> on the booking request.", "Anh/chị ghi số UN vào yêu cầu booking nhé.", "国連番号", "kokuren bangō"),
  ("hazard label", "/ˈhæzəd ˌleɪbl/", "n", "nhãn cảnh báo nguy hiểm", "Each carton must have the correct <b>hazard label</b>.", "Mỗi thùng phải dán đúng nhãn cảnh báo nguy hiểm."),
  ("flammable", "/ˈflæməbl/", "adj", "dễ cháy", "This paint is <b>flammable</b>, so keep it away from heat.", "Sơn này dễ cháy nên để xa nguồn nhiệt."),
 ],
 "phrases": [
  ("Please set the reefer to minus 18 degrees.", "Anh/chị cài container lạnh ở âm 18 độ giúp nhé."),
  ("Could you send me the temperature record for the whole voyage?", "Anh/chị gửi giúp tôi bản ghi nhiệt độ cả hành trình nhé."),
  ("The reefer needs power at the port, so there's a plug-in charge.", "Container lạnh cần cắm điện ở cảng nên có phí cắm điện."),
  ("Frozen goods must stay at minus 18 or colder.", "Hàng đông lạnh phải giữ ở âm 18 độ hoặc lạnh hơn."),
  ("Is this cargo classified as dangerous goods?", "Hàng này có được xếp vào hàng nguy hiểm không?"),
  ("Please send us the SDS before we book.", "Anh/chị gửi bên tôi SDS trước khi đặt chỗ nhé."),
  ("Not every vessel accepts dangerous goods.", "Không phải tàu nào cũng nhận hàng nguy hiểm."),
  ("DG cargo needs special approval from the carrier.", "Hàng DG cần hãng tàu duyệt riêng."),
  ("Keep flammable goods away from the office area.", "Để hàng dễ cháy tránh xa khu văn phòng."),
 ],
 "dialogues": [
  ("What temperature should we set for the frozen fish?", [
    ("Minus 18 degrees, as the buyer's instructions say. I'll put it on the booking request.", True, "Nêu nhiệt độ cụ thể theo chỉ dẫn của người mua + ghi vào booking."),
    ("Very cold is OK.", False, "Mơ hồ — container lạnh phải cài đúng số độ."),
    ("I think minus 5, same same.", False, "Sai chuyên môn: hàng đông lạnh thường cần -18°C trở xuống; 'same same' là lối nói kiểu Việt."),
  ]),
  ("The reefer was unplugged for six hours at the port.", [
    ("That could be a problem. Let's ask the carrier for the temperature record and inform the insurer today.", True, "Nhận định đúng rủi ro + hành động: xin bản ghi nhiệt độ, báo bảo hiểm."),
    ("No problem, inside is still cold.", False, "Đoán mò — cần dữ liệu nhiệt độ mới biết hàng có hỏng không; trật tự câu kiểu Việt ('It's still cold inside')."),
    ("Six hours only, not serious.", False, "Xem nhẹ — mất điện lâu có thể làm hỏng cả lô hàng lạnh."),
  ]),
  ("Can we ship these lithium batteries as normal cargo?", [
    ("No, we can't. They're dangerous goods, so we need the SDS, the UN number and approval from the carrier.", True, "Trả lời rõ + liệt kê giấy tờ cần cho hàng DG."),
    ("Yes, can. Normal cargo cheaper.", False, "Thiếu chủ ngữ và động từ, lại sai chuyên môn — pin lithium là hàng nguy hiểm."),
    ("Battery is small, no problem.", False, "Sai — pin lithium vẫn là hàng nguy hiểm dù nhỏ; thiếu mạo từ/số nhiều ('The batteries are small')."),
  ]),
  ("Why is the DG booking taking so long?", [
    ("The carrier has to check the documents and find a safe place on the vessel. It usually takes two or three days.", True, "Giải thích quy trình duyệt hàng DG + thời gian thường mất."),
    ("Because DG is dangerous, you know.", False, "Giải thích vòng vo, không có thông tin cụ thể."),
    ("Carrier slow, not my problem.", False, "Thiếu mạo từ và động từ ('The carrier is slow'), lại đổ lỗi."),
  ]),
  ("The fruit arrived soft. Was the cold chain broken?", [
    ("We're checking the temperature log now. I'll send you the data and our findings by tomorrow.", True, "Không kết luận vội + kiểm tra dữ liệu + hẹn thời gian."),
    ("No, no broken. The fruit is bad from start.", False, "Sai ngữ pháp ('It wasn't broken') và đổ lỗi khi chưa kiểm tra."),
    ("Maybe yes. Sorry, bye.", False, "Cộc lốc, không đưa hướng xử lý."),
  ]),
 ],
 "listen": [
  ("Please set the reefer to minus eighteen", ["reefer", "eighteen"], "cài nhiệt độ container lạnh"),
  ("This paint is flammable and needs a label", ["flammable", "label"], "hàng dễ cháy"),
  ("We need the safety data sheet first", ["safety", "sheet"], "xin SDS"),
  ("Perishable goods must be cleared quickly", ["Perishable", "quickly"], "hàng dễ hỏng"),
  ("The reefer arrived at Cat Lai this morning. Please plug it in as soon as possible. The frozen shrimp must stay at minus eighteen.", ["plug", "frozen", "shrimp"], "nhận container lạnh ở cảng"),
  ("This shipment contains dangerous goods. The UN number is 1263. Please attach the SDS to the booking request.", ["contains", "number", "attach"], "booking hàng nguy hiểm"),
 ],
})

# ───────────────────────── 12. Thương mại điện tử & giao chặng cuối ─────────────────────────
PHASES.append({
 "title": "Thương mại điện tử & giao chặng cuối",
 "vocab": [
  ("last mile", "/ˌlɑːst ˈmaɪl/", "n", "chặng giao cuối (đến tay người mua)", "The <b>last mile</b> is often the most expensive part of delivery.", "Chặng cuối thường là phần tốn kém nhất của khâu giao hàng."),
  ("fulfilment", "/fʊlˈfɪlmənt/", "n", "xử lý đơn hàng (nhận, soạn, đóng gói, giao)", "Our <b>fulfilment</b> centre ships 5,000 orders a day.", "Trung tâm xử lý đơn hàng của mình xuất 5.000 đơn mỗi ngày."),
  ("parcel", "/ˈpɑːsl/", "n", "bưu kiện, gói hàng", "The driver delivered 120 <b>parcels</b> today.", "Hôm nay tài xế giao được 120 gói hàng."),
  ("tracking number", "/ˈtrækɪŋ ˌnʌmbə/", "n", "mã vận đơn, mã theo dõi", "The customer can check the status with the <b>tracking number</b>.", "Khách có thể xem tình trạng đơn bằng mã vận đơn.", "追跡番号", "tsuiseki bangō"),
  ("cash on delivery", "/ˌkæʃ ɒn dɪˈlɪvəri/", "n", "thu tiền khi giao hàng (COD)", "Most of our online orders are <b>cash on delivery</b>.", "Phần lớn đơn online của bên mình là thu tiền khi giao.", "代金引換", "daikin hikikae"),
  ("failed delivery", "/ˌfeɪld dɪˈlɪvəri/", "n", "giao hàng không thành công", "A wrong phone number is a common reason for a <b>failed delivery</b>.", "Sai số điện thoại là lý do hay gặp khiến giao hàng không thành."),
  ("reverse logistics", "/rɪˌvɜːs ləˈdʒɪstɪks/", "n", "logistics ngược (thu hồi hàng hoàn, hàng trả)", "<b>Reverse logistics</b> is getting more important as returns grow.", "Logistics ngược ngày càng quan trọng khi lượng hàng hoàn tăng."),
  ("same-day delivery", "/ˌseɪm deɪ dɪˈlɪvəri/", "n", "giao trong ngày", "We offer <b>same-day delivery</b> for orders placed before 11 a.m.", "Bên mình giao trong ngày cho đơn đặt trước 11 giờ sáng."),
  ("sorting centre", "/ˈsɔːtɪŋ ˌsentə/", "n", "trung tâm phân loại (bưu kiện)", "All parcels go through the <b>sorting centre</b> at night.", "Tất cả bưu kiện đi qua trung tâm phân loại vào ban đêm."),
  ("shipping label", "/ˈʃɪpɪŋ ˌleɪbl/", "n", "nhãn vận chuyển (dán lên gói hàng)", "The <b>shipping label</b> is missing the customer's phone number.", "Nhãn vận chuyển bị thiếu số điện thoại của khách."),
 ],
 "phrases": [
  ("Your parcel is out for delivery today.", "Gói hàng của anh/chị đang được giao trong hôm nay."),
  ("The driver couldn't reach the customer by phone.", "Tài xế không liên lạc được với khách qua điện thoại."),
  ("We'll try to deliver again tomorrow.", "Ngày mai bên mình sẽ giao lại."),
  ("The customer refused the parcel, so it's coming back to the warehouse.", "Khách từ chối nhận nên gói hàng đang được hoàn về kho."),
  ("Orders placed before noon ship the same day.", "Đơn đặt trước 12 giờ trưa sẽ được xuất trong ngày."),
  ("Please print the shipping labels for today's orders.", "In giúp nhãn vận chuyển cho các đơn hôm nay nhé."),
  ("The COD money will be transferred to your account every Friday.", "Tiền COD sẽ được chuyển vào tài khoản của anh/chị mỗi thứ Sáu."),
  ("Our return rate is about 8% during big sales.", "Tỷ lệ hoàn hàng của bên mình khoảng 8% vào các đợt sale lớn."),
  ("Please check the address and phone number before packing.", "Kiểm tra địa chỉ và số điện thoại trước khi đóng gói nhé."),
 ],
 "dialogues": [
  ("Where's my parcel? The app says 'failed delivery'.", [
    ("I'm sorry. The driver couldn't reach you by phone. We'll deliver again tomorrow morning. Is that OK?", True, "Xin lỗi + lý do + hẹn giao lại + hỏi khách có tiện không."),
    ("Driver call you but you not answer.", False, "Sai thì và thiếu trợ động từ ('The driver called, but you didn't answer') — lại nghe như trách khách."),
    ("Please check the app again.", False, "Không giải thích, đẩy lại cho khách."),
  ]),
  ("Can you deliver this order today?", [
    ("Yes. You ordered before 11 a.m., so we can deliver it today, by 6 p.m.", True, "Xác nhận + điều kiện được giao trong ngày + giờ đến dự kiến."),
    ("Today can.", False, "Thiếu chủ ngữ, trật tự kiểu Việt: 'Yes, we can deliver it today.'"),
    ("Maybe today, maybe not, depends driver.", False, "Mơ hồ, thiếu 'It' và 'on': 'It depends on the driver.'"),
  ]),
  ("Why is the COD payment for last week late?", [
    ("Let me check with our finance team. The transfer is usually on Friday, so I'll update you by this afternoon.", True, "Kiểm tra + lịch chuyển tiền thông thường + hẹn giờ phản hồi."),
    ("Finance slow, I don't know.", False, "Thiếu động từ ('Finance is slow'), đổ lỗi, không hỗ trợ."),
    ("Money will come, don't worry.", False, "Hứa suông, không có ngày cụ thể."),
  ]),
  ("The customer wants to return this item. What should I do?", [
    ("Please create a return request in the system. The driver will pick it up within two days.", True, "Hướng dẫn quy trình hoàn hàng cụ thể."),
    ("Return is trouble, tell him no.", False, "Từ chối trái chính sách, cộc lốc."),
    ("You take and bring back.", False, "Thiếu tân ngữ, chỉ dẫn mơ hồ: 'Please pick it up and bring it back.'"),
  ]),
  ("How can we reduce failed deliveries?", [
    ("We could send an SMS before the driver leaves and ask customers to confirm a time.", True, "Đề xuất cụ thể, dùng 'could' lịch sự."),
    ("Customers must answer phone always.", False, "Đổ trách nhiệm cho khách; thiếu mạo từ và sai vị trí trạng từ: 'must always answer the phone'."),
    ("Failed delivery is normal, cannot reduce.", False, "Bi quan, thiếu chủ ngữ ('we can't reduce it')."),
  ]),
 ],
 "listen": [
  ("Your parcel is out for delivery today", ["parcel", "delivery"], "gói hàng đang giao"),
  ("Please print the shipping labels now", ["print", "labels"], "in nhãn vận chuyển"),
  ("The customer refused the parcel at the door", ["refused", "door"], "khách từ chối nhận"),
  ("We offer same-day delivery in the city", ["same-day", "city"], "giao trong ngày"),
  ("Hi, this is your delivery driver. I'm outside your building now. Could you come down and pay 350,000 dong?", ["driver", "building", "pay"], "tài xế gọi khách"),
  ("We shipped 4,000 orders during the sale. About 5% were failed deliveries. Most customers gave the wrong phone number.", ["sale", "failed", "wrong"], "báo cáo sau đợt sale"),
 ],
})

# ───────────────────────── 13. Bảo hiểm hàng hoá ─────────────────────────
PHASES.append({
 "title": "Bảo hiểm hàng hoá",
 "vocab": [
  ("insurance policy", "/ɪnˈʃʊərəns ˌpɒləsi/", "n", "hợp đồng / đơn bảo hiểm", "Please check what our <b>insurance policy</b> covers.", "Anh/chị kiểm tra giúp hợp đồng bảo hiểm của mình bảo hiểm những gì nhé.", "保険証券", "hoken shōken"),
  ("premium", "/ˈpriːmiəm/", "n", "phí bảo hiểm", "The <b>premium</b> is 0.1% of the insured value.", "Phí bảo hiểm là 0,1% giá trị được bảo hiểm.", "保険料", "hokenryō"),
  ("insured value", "/ɪnˌʃʊəd ˈvæljuː/", "n", "giá trị được bảo hiểm", "The <b>insured value</b> is usually the CIF value plus 10%.", "Giá trị bảo hiểm thường là trị giá CIF cộng 10%."),
  ("all risks", "/ˌɔːl ˈrɪsks/", "n", "điều kiện bảo hiểm mọi rủi ro (ICC A)", "For fragile goods, we always buy <b>all risks</b> cover.", "Hàng dễ vỡ thì bên mình luôn mua bảo hiểm mọi rủi ro."),
  ("deductible", "/dɪˈdʌktəbl/", "n", "mức khấu trừ (khoản tự chịu mỗi vụ tổn thất)", "The policy has a <b>deductible</b> of 200 dollars per claim.", "Hợp đồng có mức khấu trừ 200 đô cho mỗi vụ bồi thường."),
  ("insurer", "/ɪnˈʃʊərə/", "n", "công ty bảo hiểm, bên bảo hiểm", "We must inform the <b>insurer</b> as soon as we find the damage.", "Phát hiện hư hỏng là phải báo ngay cho bên bảo hiểm."),
  ("general average", "/ˌdʒenrəl ˈævərɪdʒ/", "n", "tổn thất chung (các chủ hàng cùng chia chi phí cứu tàu)", "After the fire on the ship, the owner declared <b>general average</b>.", "Sau vụ cháy trên tàu, chủ tàu đã tuyên bố tổn thất chung.", "共同海損", "kyōdō kaison"),
  ("exclusion", "/ɪkˈskluːʒn/", "n", "điều khoản loại trừ (trường hợp không được bảo hiểm)", "Poor packing is a common <b>exclusion</b> in cargo policies.", "Đóng gói kém là điều khoản loại trừ phổ biến trong hợp đồng bảo hiểm hàng hoá."),
  ("compensation", "/ˌkɒmpenˈseɪʃn/", "n", "tiền bồi thường", "We received <b>compensation</b> for the damaged cartons last week.", "Tuần trước bên mình đã nhận tiền bồi thường cho số thùng hư."),
  ("coverage", "/ˈkʌvərɪdʒ/", "n", "phạm vi bảo hiểm", "Does our <b>coverage</b> include theft during trucking?", "Phạm vi bảo hiểm của mình có gồm mất cắp khi chở bằng xe tải không?"),
 ],
 "phrases": [
  ("Do we need insurance for this shipment?", "Lô này mình có cần mua bảo hiểm không?"),
  ("How much is the premium for this shipment?", "Phí bảo hiểm cho lô này là bao nhiêu?"),
  ("We usually insure the goods for 110% of the CIF value.", "Bên mình thường mua bảo hiểm cho hàng ở mức 110% trị giá CIF."),
  ("Does the policy cover theft?", "Hợp đồng bảo hiểm có bảo hiểm mất cắp không?"),
  ("Please send me the insurance certificate before shipment.", "Anh/chị gửi giúp giấy chứng nhận bảo hiểm trước khi giao hàng nhé."),
  ("The insurer needs photos, the survey report and the invoice.", "Bên bảo hiểm cần ảnh, biên bản giám định và hoá đơn."),
  ("Poor packing is not covered.", "Đóng gói kém thì không được bảo hiểm."),
  ("When will we receive the compensation?", "Khi nào bên mình nhận được tiền bồi thường?"),
  ("Without insurance, we'd have to pay for the loss ourselves.", "Không có bảo hiểm thì mình phải tự chịu tổn thất."),
 ],
 "dialogues": [
  ("Do we really need cargo insurance? It's an extra cost.", [
    ("I'd recommend it. The premium is small, and the carrier's liability is very limited if something goes wrong.", True, "Khuyên kèm lý do: phí nhỏ, trách nhiệm của hãng tàu có giới hạn."),
    ("No need, carrier pay all.", False, "Sai chuyên môn (trách nhiệm hãng tàu có giới hạn) và thiếu 's' ('the carrier pays')."),
    ("Insurance is waste money.", False, "Thiếu 'a … of' ('a waste of money') và tư vấn sai."),
  ]),
  ("What does 'all risks' cover?", [
    ("It covers most physical loss or damage, but not things like poor packing or delay.", True, "Giải thích đúng phạm vi + nêu các điều khoản loại trừ phổ biến."),
    ("All risks is cover everything.", False, "Thừa 'is' ('it covers') và sai — 'all risks' vẫn có điều khoản loại trừ."),
    ("It is very good, don't worry.", False, "Không trả lời câu hỏi."),
  ]),
  ("How much is the insurance for this shipment?", [
    ("The insured value is 55,000 dollars, and the rate is 0.1%, so the premium is 55 dollars.", True, "Tính minh bạch: giá trị bảo hiểm × tỷ lệ phí."),
    ("Very cheap, only little money.", False, "Không có con số cụ thể; 'only a little money'."),
    ("Premium 0.1.", False, "Câu cụt, thiếu động từ, đơn vị (%) và số tiền."),
  ]),
  ("The insurer rejected our claim. Why?", [
    ("They said the damage was caused by poor packing, which is an exclusion in our policy.", True, "Nêu lý do cụ thể gắn với điều khoản loại trừ."),
    ("Because they don't want pay.", False, "Thiếu 'to' ('want to pay') và suy đoán thiếu cơ sở."),
    ("I don't know, they reject only.", False, "Không tìm hiểu lý do; câu dịch từng chữ, sai thì."),
  ]),
  ("What documents do we need for the insurance claim?", [
    ("We need the policy, the invoice, the B/L, photos, the survey report and a claim letter.", True, "Liệt kê đủ bộ hồ sơ đòi bồi thường."),
    ("Only photos is enough.", False, "Sai chia động từ ('are') và thiếu hồ sơ — bảo hiểm cần nhiều chứng từ hơn."),
    ("Many papers, I send you later.", False, "Mơ hồ, không trả lời câu hỏi, thiếu 'will'."),
  ]),
 ],
 "listen": [
  ("The premium is point one percent", ["premium", "percent"], "phí bảo hiểm"),
  ("Our policy does not cover poor packing", ["policy", "packing"], "điều khoản loại trừ"),
  ("Please inform the insurer this afternoon", ["inform", "insurer"], "báo cho bảo hiểm"),
  ("We received the compensation last Friday", ["compensation", "Friday"], "nhận tiền bồi thường"),
  ("Hi Linh, the goods are insured for 110% of the CIF value. The premium is 60 dollars. I'll email the certificate today.", ["insured", "premium", "certificate"], "xác nhận mua bảo hiểm"),
  ("We've filed the claim with the insurer. They need the survey report by Friday. The compensation should come within a month.", ["filed", "survey", "month"], "tiến độ hồ sơ bồi thường"),
 ],
})

# ───────────────────────── 14. Thanh toán quốc tế & L/C ─────────────────────────
PHASES.append({
 "title": "Thanh toán quốc tế & L/C",
 "vocab": [
  ("telegraphic transfer", "/ˌtelɪˈɡræfɪk ˈtrænsfɜː/", "n", "chuyển tiền bằng điện (T/T)", "The buyer will pay by <b>telegraphic transfer</b> within 30 days.", "Người mua sẽ thanh toán bằng T/T trong vòng 30 ngày.", "電信送金", "denshin sōkin"),
  ("deposit", "/dɪˈpɒzɪt/", "n", "tiền đặt cọc", "We'll start production after we receive the <b>deposit</b>.", "Bên tôi sẽ sản xuất sau khi nhận tiền cọc."),
  ("balance", "/ˈbæləns/", "n", "số tiền còn lại (phải trả)", "Please pay the <b>balance</b> before we release the B/L.", "Vui lòng thanh toán phần còn lại trước khi bên tôi giao B/L."),
  ("proforma invoice", "/ˌprəʊ ˌfɔːmə ˈɪnvɔɪs/", "n", "hoá đơn chiếu lệ (PI)", "Please send the <b>proforma invoice</b> so we can open the L/C.", "Anh/chị gửi PI để bên tôi mở L/C nhé."),
  ("issuing bank", "/ˈɪʃuːɪŋ bæŋk/", "n", "ngân hàng phát hành (L/C)", "The <b>issuing bank</b> is in Singapore.", "Ngân hàng phát hành L/C ở Singapore.", "発行銀行", "hakkō ginkō"),
  ("beneficiary", "/ˌbenɪˈfɪʃəri/", "n", "người thụ hưởng", "Our company is the <b>beneficiary</b> of this L/C.", "Công ty mình là người thụ hưởng của L/C này.", "受益者", "juekisha"),
  ("expiry date", "/ɪkˈspaɪəri deɪt/", "n", "ngày hết hạn", "The <b>expiry date</b> of the L/C is 30 June.", "L/C hết hạn ngày 30 tháng 6."),
  ("latest shipment date", "/ˌleɪtɪst ˈʃɪpmənt deɪt/", "n", "ngày giao hàng chậm nhất (theo L/C)", "The <b>latest shipment date</b> is 15 June, so we can't miss this vessel.", "Ngày giao hàng chậm nhất là 15/6 nên mình không được lỡ chuyến tàu này."),
  ("remittance", "/rɪˈmɪtns/", "n", "khoản chuyển tiền; chứng từ chuyển tiền", "Could you send us a copy of the <b>remittance</b>?", "Anh/chị gửi giúp bên tôi bản sao chứng từ chuyển tiền nhé."),
  ("bank charges", "/ˈbæŋk ˌtʃɑːdʒɪz/", "n", "phí ngân hàng", "Each side pays its own <b>bank charges</b>.", "Mỗi bên tự trả phí ngân hàng của mình."),
 ],
 "phrases": [
  ("We've received your deposit, thank you.", "Bên tôi đã nhận tiền cọc, cảm ơn anh/chị."),
  ("Could you send us the bank slip after the transfer?", "Chuyển tiền xong anh/chị gửi giúp bên tôi phiếu chuyển tiền nhé."),
  ("The payment hasn't arrived in our account yet.", "Tiền chưa về tài khoản bên tôi."),
  ("An international transfer usually takes two to three working days.", "Chuyển tiền quốc tế thường mất hai đến ba ngày làm việc."),
  ("Please check the L/C terms carefully before shipment.", "Kiểm tra kỹ các điều khoản L/C trước khi giao hàng nhé."),
  ("The bank found a discrepancy, so payment is delayed.", "Ngân hàng phát hiện bất hợp lệ nên thanh toán bị chậm."),
  ("Could you amend the latest shipment date to 30 June?", "Anh/chị tu chỉnh ngày giao hàng chậm nhất thành 30/6 được không?"),
  ("We received 20 dollars less because of bank charges.", "Bên tôi nhận thiếu 20 đô do phí ngân hàng."),
  ("Your payment is ten days overdue.", "Khoản thanh toán của anh/chị đã quá hạn mười ngày."),
 ],
 "dialogues": [
  ("We sent the balance yesterday. Did you receive it?", [
    ("Not yet. International transfers usually take two or three days. Could you send me the bank slip?", True, "Trả lời + giải thích thời gian + xin chứng từ để kiểm tra."),
    ("No receive.", False, "Dịch từng chữ 'chưa nhận': 'We haven't received it yet.'"),
    ("You don't send, I think.", False, "Sai thì ('You didn't send it') và nghi ngờ khách, thiếu lịch sự."),
  ]),
  ("The buyer paid 10,000 dollars, but we only received 9,970. Why?", [
    ("The missing 30 dollars is probably a charge from an intermediary bank. I'll ask our bank to confirm.", True, "Giải thích nguyên nhân hợp lý + kiểm tra lại với ngân hàng."),
    ("Buyer cheat us 30 dollars.", False, "Buộc tội vô căn cứ, sai thì và thiếu mạo từ ('The buyer cheated us')."),
    ("30 dollars small, forget it.", False, "Thiếu động từ 'is' và bỏ qua vấn đề."),
  ]),
  ("When will you open the L/C?", [
    ("We'll open it this week, once you send us the final proforma invoice.", True, "Mốc thời gian + điều kiện cần từ phía bên kia."),
    ("L/C open soon.", False, "Thiếu chủ ngữ và trợ động từ, mơ hồ: 'We'll open it this week.'"),
    ("Why you need L/C so fast?", False, "Sai trật tự câu hỏi ('Why do you need…') và nghe khó chịu."),
  ]),
  ("We can't ship before the latest shipment date. What should we do?", [
    ("Let's ask the buyer to amend the L/C and extend both the shipment date and the expiry date.", True, "Giải pháp đúng: tu chỉnh L/C, gia hạn cả ngày giao hàng và ngày hết hạn."),
    ("We ship late, bank still pay.", False, "Sai ngữ pháp ('the bank will still pay') và sai nghiệp vụ: giao trễ so với L/C là bất hợp lệ, có thể bị từ chối thanh toán."),
    ("Just change the date on the B/L.", False, "Nguy hiểm: sửa ngày B/L là gian lận chứng từ."),
  ]),
  ("Your payment is two weeks overdue.", [
    ("I'm sorry about that. Our finance team will send it on Friday, and I'll email you the bank slip.", True, "Xin lỗi + ngày chuyển tiền + cam kết gửi chứng từ."),
    ("Sorry, finance forget.", False, "Sai thì ('forgot') và đổ lỗi cho bộ phận khác."),
    ("Only two weeks, not long.", False, "Xem nhẹ việc trễ hạn thanh toán, làm mất lòng tin."),
  ]),
 ],
 "listen": [
  ("We received your deposit this morning", ["deposit", "morning"], "nhận tiền cọc"),
  ("Please pay the balance before shipment", ["balance", "shipment"], "thanh toán phần còn lại"),
  ("The L/C expires at the end of June", ["expires", "June"], "hạn L/C"),
  ("Could you send me the bank slip", ["bank", "slip"], "xin phiếu chuyển tiền"),
  ("Hi Tuan, we've received the L/C. The latest shipment date is 20 May. Please book the vessel early.", ["received", "latest", "early"], "báo đã nhận L/C"),
  ("The bank found two discrepancies in our documents. The weight on the invoice doesn't match the B/L. Payment will be delayed.", ["bank", "weight", "delayed"], "ngân hàng báo bất hợp lệ"),
 ],
})

# ───────────────────────── 15. Đóng gói, pallet & đóng container ─────────────────────────
PHASES.append({
 "title": "Đóng gói, pallet & đóng container",
 "vocab": [
  ("stuffing", "/ˈstʌfɪŋ/", "n", "đóng hàng vào container", "Container <b>stuffing</b> starts at 8 a.m. at our factory.", "8 giờ sáng bắt đầu đóng hàng vào container ở xưởng mình.", "バンニング", "banningu"),
  ("carton", "/ˈkɑːtn/", "n", "thùng carton", "Each <b>carton</b> holds 24 bottles.", "Mỗi thùng chứa 24 chai.", "段ボール", "danbōru"),
  ("stretch wrap", "/ˈstretʃ ræp/", "n", "màng quấn pallet (màng PE căng)", "Use two layers of <b>stretch wrap</b> on each pallet.", "Quấn hai lớp màng PE cho mỗi pallet."),
  ("shipping mark", "/ˈʃɪpɪŋ mɑːk/", "n", "ký mã hiệu (trên thùng hàng)", "The <b>shipping mark</b> must show the PO number and the carton number.", "Ký mã hiệu phải có số PO và số thứ tự thùng."),
  ("fumigation", "/ˌfjuːmɪˈɡeɪʃn/", "n", "hun trùng", "Wooden pallets need heat treatment or <b>fumigation</b> before export.", "Pallet gỗ cần xử lý nhiệt hoặc hun trùng trước khi xuất khẩu.", "燻蒸", "kunjō"),
  ("dunnage", "/ˈdʌnɪdʒ/", "n", "vật chèn lót (chống xê dịch hàng)", "Put <b>dunnage</b> bags in the gaps so the cargo can't move.", "Chèn túi khí vào các khoảng trống để hàng không xê dịch."),
  ("lashing", "/ˈlæʃɪŋ/", "n", "chằng buộc (hàng trong container)", "Heavy machines need strong <b>lashing</b> inside the container.", "Máy móc nặng cần chằng buộc chắc chắn trong container."),
  ("gross weight", "/ˌɡrəʊs ˈweɪt/", "n", "trọng lượng cả bì", "The <b>gross weight</b> includes the cartons and the pallet.", "Trọng lượng cả bì gồm cả thùng và pallet.", "総重量", "sō jūryō"),
  ("net weight", "/ˌnet ˈweɪt/", "n", "trọng lượng tịnh", "The <b>net weight</b> of each bag is 25 kilos.", "Trọng lượng tịnh mỗi bao là 25 ký.", "正味重量", "shōmi jūryō"),
  ("VGM", "/ˌviː dʒiː ˈem/", "n", "khối lượng toàn bộ container đã xác minh (VGM)", "Please submit the <b>VGM</b> to the carrier before the cut-off.", "Nhớ khai VGM cho hãng tàu trước giờ cắt máng nhé."),
 ],
 "phrases": [
  ("How many cartons can we fit in a 20-foot container?", "Một container 20 feet đóng được bao nhiêu thùng?"),
  ("Put the heavy cartons at the bottom.", "Xếp thùng nặng ở dưới."),
  ("Please don't stack more than four cartons high.", "Đừng xếp chồng quá bốn thùng nhé."),
  ("Check the container for holes and bad smells before loading.", "Kiểm tra container xem có lỗ thủng hay mùi lạ không trước khi đóng hàng."),
  ("Take photos of the container before and after stuffing.", "Chụp ảnh container trước và sau khi đóng hàng."),
  ("The wooden pallets must have the ISPM 15 mark.", "Pallet gỗ phải có dấu ISPM 15."),
  ("Please mark the cartons 'Fragile' and 'This Side Up'.", "Nhớ ghi 'Hàng dễ vỡ' và 'Mặt này hướng lên' trên thùng nhé."),
  ("Use dunnage bags to fill the empty space.", "Dùng túi khí chèn để lấp khoảng trống."),
  ("We need the VGM before the cut-off tomorrow.", "Mình cần VGM trước giờ cắt máng ngày mai."),
 ],
 "dialogues": [
  ("How should we load these cartons?", [
    ("Please put the heavy cartons at the bottom and the light ones on top. Don't stack them more than five high.", True, "Chỉ dẫn cụ thể: nặng dưới, nhẹ trên, giới hạn số lớp."),
    ("Load any way, fast fast.", False, "Chỉ dẫn cẩu thả, lặp từ kiểu Việt — xếp sai dễ đè bẹp hàng."),
    ("You load how you like.", False, "Sai cấu trúc ('however you like') và không hướng dẫn gì."),
  ]),
  ("The buyer wants wooden pallets. Is there anything special?", [
    ("Yes. They must be heat-treated or fumigated and have the ISPM 15 mark.", True, "Nêu đúng yêu cầu ISPM 15 cho pallet gỗ xuất khẩu."),
    ("No special, wood is wood.", False, "Sai chuyên môn — pallet gỗ chưa xử lý có thể bị giữ hoặc buộc tiêu huỷ ở nước đến."),
    ("Yes, must fumigation.", False, "Thiếu chủ ngữ và dùng danh từ thay động từ: 'They must be fumigated.'"),
  ]),
  ("Have you submitted the VGM?", [
    ("Yes, I sent it to the carrier this morning. It's 24,300 kilos.", True, "Trả lời đúng thì + thời điểm + con số."),
    ("Yes, I submit already.", False, "Sai thì: 'Yes, I've submitted it.'"),
    ("VGM is not important.", False, "Sai — không có VGM thì container không được xếp lên tàu (quy định SOLAS)."),
  ]),
  ("There's a gap at the back of the container. Is that OK?", [
    ("No, the cargo could move. Please fill it with dunnage bags and add some lashing.", True, "Nhận ra rủi ro + cách xử lý cụ thể."),
    ("Is OK, container is strong.", False, "Thiếu chủ ngữ ('It's OK') và sai — hàng xê dịch sẽ đổ vỡ."),
    ("Just close the door quickly.", False, "Bỏ qua rủi ro, không xử lý khoảng trống."),
  ]),
  ("What's the difference between gross weight and net weight?", [
    ("Net weight is the product only. Gross weight includes the packing, like cartons and pallets.", True, "Giải thích đúng, có ví dụ."),
    ("Same thing, no different.", False, "Sai kiến thức; 'no different' phải là 'no difference'."),
    ("Gross is more heavy.", False, "Chưa giải thích và sai so sánh hơn ('heavier')."),
  ]),
 ],
 "listen": [
  ("Put the heavy cartons at the bottom", ["heavy", "bottom"], "xếp hàng nặng"),
  ("Stuffing starts at eight at the factory", ["Stuffing", "factory"], "giờ đóng hàng"),
  ("Please wrap each pallet with stretch film", ["wrap", "film"], "quấn màng pallet"),
  ("The net weight of each bag is fifty kilos", ["net", "fifty"], "trọng lượng tịnh"),
  ("The container is clean and dry. We've loaded 960 cartons. Please send the seal number and the VGM to the carrier.", ["clean", "loaded", "VGM"], "báo đóng hàng xong"),
  ("These pallets are made of wood. They need heat treatment and the ISPM 15 mark. Otherwise, the destination country may reject them.", ["wood", "treatment", "reject"], "yêu cầu với pallet gỗ"),
 ],
})

# ───────────────────────── 16. Tối ưu tuyến & chi phí vận chuyển ─────────────────────────
PHASES.append({
 "title": "Tối ưu tuyến & chi phí vận chuyển",
 "vocab": [
  ("backhaul", "/ˈbækhɔːl/", "n", "hàng chiều về (chở hàng khi xe quay về)", "We found a <b>backhaul</b> load, so the truck won't come back empty.", "Bên mình tìm được hàng chiều về nên xe không phải chạy rỗng."),
  ("utilisation", "/ˌjuːtəlaɪˈzeɪʃn/", "n", "mức sử dụng (tải trọng, không gian của xe/container)", "Truck <b>utilisation</b> was only 60% last month.", "Tháng trước xe chỉ chạy được 60% tải."),
  ("milk run", "/ˈmɪlk rʌn/", "n", "tuyến gom hàng vòng (lấy hàng nhiều điểm theo lịch cố định)", "One truck does a <b>milk run</b> to five suppliers every morning.", "Mỗi sáng một xe chạy vòng lấy hàng ở năm nhà cung cấp.", "ミルクラン", "mirukuran"),
  ("toll", "/təʊl/", "n", "phí cầu đường", "The expressway is faster, but the <b>tolls</b> are high.", "Đi cao tốc nhanh hơn nhưng phí cầu đường cao."),
  ("multimodal", "/ˌmʌltiˈməʊdl/", "adj", "đa phương thức", "A <b>multimodal</b> route by sea and rail is cheaper than air.", "Tuyến đa phương thức biển kết hợp đường sắt rẻ hơn đường hàng không."),
  ("rail freight", "/ˈreɪl freɪt/", "n", "vận tải đường sắt", "<b>Rail freight</b> from Hanoi to Europe takes about 25 days.", "Đi đường sắt từ Hà Nội sang châu Âu mất khoảng 25 ngày."),
  ("barge", "/bɑːdʒ/", "n", "sà lan", "We move containers from Can Tho to Cat Lai by <b>barge</b>.", "Bên mình chuyển container từ Cần Thơ lên Cát Lái bằng sà lan."),
  ("spot rate", "/ˈspɒt reɪt/", "n", "giá cước thị trường (giá giao ngay)", "The <b>spot rate</b> is higher than our contract rate this month.", "Tháng này giá cước thị trường cao hơn giá hợp đồng của mình."),
  ("optimise", "/ˈɒptɪmaɪz/", "v", "tối ưu", "The new software helps us <b>optimise</b> delivery routes.", "Phần mềm mới giúp bên mình tối ưu tuyến giao hàng."),
  ("full truckload", "/ˌfʊl ˈtrʌkləʊd/", "n", "hàng nguyên xe (FTL)", "It's cheaper per kilo to ship a <b>full truckload</b>.", "Đi nguyên xe thì tính ra mỗi ký rẻ hơn."),
 ],
 "phrases": [
  ("Too many trucks are coming back empty.", "Có quá nhiều xe chạy chiều về rỗng."),
  ("If we combine these two routes, we can save one truck.", "Nếu gộp hai tuyến này, mình bớt được một xe."),
  ("Barge is cheaper than trucking, but it's slower.", "Đi sà lan rẻ hơn xe tải nhưng chậm hơn."),
  ("Let's compare the cost per kilo for each option.", "Mình so sánh chi phí trên mỗi ký của từng phương án nhé."),
  ("Should we lock in a contract rate or use spot rates?", "Mình nên chốt giá hợp đồng hay đi theo giá thị trường?"),
  ("Delivering at night avoids traffic and the truck ban.", "Giao ban đêm tránh được kẹt xe và giờ cấm tải."),
  ("The expressway saves two hours but adds 500,000 dong in tolls.", "Đi cao tốc tiết kiệm hai tiếng nhưng tốn thêm 500.000 đồng phí cầu đường."),
  ("Our target is to cut transport costs by 10% this year.", "Mục tiêu năm nay là giảm 10% chi phí vận tải."),
  ("Fuller trucks mean a lower cost per order.", "Xe chở đầy hơn thì chi phí mỗi đơn thấp hơn."),
 ],
 "dialogues": [
  ("Our trucking cost went up 15% this quarter. Why?", [
    ("Fuel prices went up, and many trucks were only half full. We need to improve utilisation.", True, "Nêu nguyên nhân + hướng cải thiện."),
    ("Because everything expensive now.", False, "Thiếu động từ 'is' và giải thích chung chung."),
    ("Cost go up, cannot control.", False, "Sai thì ('went up'), thiếu chủ ngữ ('we can't'), bi quan."),
  ]),
  ("Should we use barges or trucks from Can Tho to Cat Lai?", [
    ("Barge is about 30% cheaper. If the goods aren't urgent, I'd go by barge.", True, "So sánh bằng số + điều kiện + đề xuất rõ ràng."),
    ("Barge more cheap but more slow.", False, "Thiếu 'is'; phải dùng 'cheaper' và 'slower'."),
    ("Truck, because I like truck.", False, "Lý do cảm tính, không dựa trên chi phí hay thời gian."),
  ]),
  ("Can we reduce the number of trucks for supplier pickups?", [
    ("Yes. We could set up a milk run, so one truck picks up from all five suppliers each morning.", True, "Giải pháp cụ thể (milk run) + cách vận hành."),
    ("Yes, we can reduce trucks maybe.", False, "Mơ hồ, không nói cách làm."),
    ("Suppliers bring by themselves.", False, "Thiếu tân ngữ ('bring the goods themselves') và chưa bàn với nhà cung cấp."),
  ]),
  ("The spot rate is lower than our contract rate. Should we switch?", [
    ("Not completely. Spot rates can go up quickly in peak season. Let's keep the contract and use spot rates for extra volume.", True, "Cân nhắc rủi ro + phương án kết hợp hợp lý."),
    ("Yes, switch all now, cheap is good.", False, "Quyết vội — giá thị trường biến động, dễ mất chỗ khi cao điểm."),
    ("Spot rate I don't understand.", False, "Trật tự từ kiểu Việt và thiếu chuyên môn."),
  ]),
  ("Why don't the drivers use the expressway?", [
    ("The tolls are high, and the old road is only 30 minutes slower. For urgent orders, they do use it.", True, "Giải thích bằng chi phí/thời gian + nêu ngoại lệ."),
    ("Because expressway expensive.", False, "Thiếu mạo từ và động từ: 'Because the expressway is expensive.'"),
    ("Drivers like old road.", False, "Lý do chủ quan, thiếu mạo từ ('the old road')."),
  ]),
 ],
 "listen": [
  ("The truck came back empty again", ["truck", "empty"], "xe chạy rỗng"),
  ("We move the containers by barge", ["move", "barge"], "đi sà lan"),
  ("Truck utilisation was only sixty percent", ["utilisation", "sixty"], "hiệu suất sử dụng xe"),
  ("The spot rate went up this week", ["spot", "week"], "giá thị trường tăng"),
  ("We looked at the routes last month. Two trucks were only half full every day. If we combine them, we can save about 20 million dong a month.", ["routes", "half", "combine"], "đề xuất gộp tuyến"),
  ("Every morning, one truck visits five suppliers. It collects all the parts and brings them to our factory by ten.", ["morning", "suppliers", "parts"], "mô tả tuyến milk run"),
 ],
})

# ───────────────────────── 17. Hệ thống WMS/TMS & dữ liệu ─────────────────────────
PHASES.append({
 "title": "Hệ thống WMS/TMS & dữ liệu",
 "vocab": [
  ("WMS", "/ˌdʌbljuː em ˈes/", "n", "hệ thống quản lý kho (WMS)", "Every pallet movement is recorded in the <b>WMS</b>.", "Mọi lần di chuyển pallet đều được ghi vào WMS."),
  ("TMS", "/ˌtiː em ˈes/", "n", "hệ thống quản lý vận tải (TMS)", "The <b>TMS</b> shows where every truck is right now.", "TMS cho biết ngay lúc này từng xe đang ở đâu."),
  ("barcode", "/ˈbɑːkəʊd/", "n", "mã vạch", "The <b>barcode</b> on this carton won't scan.", "Mã vạch trên thùng này quét không được.", "バーコード", "bākōdo"),
  ("handheld scanner", "/ˌhændheld ˈskænə/", "n", "máy quét cầm tay", "Please charge your <b>handheld scanner</b> before the shift.", "Nhớ sạc máy quét cầm tay trước ca nhé."),
  ("real-time", "/ˈrɪəl taɪm/", "adj", "theo thời gian thực", "Customers can see <b>real-time</b> tracking on our portal.", "Khách có thể theo dõi đơn theo thời gian thực trên cổng thông tin của mình."),
  ("dashboard", "/ˈdæʃbɔːd/", "n", "bảng số liệu tổng quan (dashboard)", "The <b>dashboard</b> shows today's orders and late deliveries.", "Dashboard hiển thị đơn hôm nay và các đơn giao trễ."),
  ("EDI", "/ˌiː diː ˈaɪ/", "n", "trao đổi dữ liệu điện tử (EDI)", "The customer sends us orders by <b>EDI</b>, not by email.", "Khách gửi đơn cho bên mình qua EDI chứ không qua email."),
  ("master data", "/ˈmɑːstə ˌdeɪtə/", "n", "dữ liệu gốc (mã hàng, kích thước, trọng lượng…)", "Wrong <b>master data</b> means wrong weights on every order.", "Dữ liệu gốc sai thì đơn nào cũng sai trọng lượng.", "マスターデータ", "masutā dēta"),
  ("KPI", "/ˌkeɪ piː ˈaɪ/", "n", "chỉ số đánh giá hiệu quả (KPI)", "Picking accuracy is our most important <b>KPI</b>.", "Độ chính xác soạn hàng là KPI quan trọng nhất của bên mình."),
  ("data entry", "/ˈdeɪtə ˌentri/", "n", "nhập liệu", "Most errors come from manual <b>data entry</b>.", "Hầu hết lỗi đến từ khâu nhập liệu thủ công."),
 ],
 "phrases": [
  ("Please scan the barcode instead of typing the code.", "Quét mã vạch nhé, đừng gõ mã bằng tay."),
  ("The scanner isn't connecting to the system.", "Máy quét không kết nối được với hệ thống."),
  ("The system is down, so we're recording orders on paper.", "Hệ thống bị sập nên bên mình đang ghi đơn ra giấy."),
  ("Can you export this report as a spreadsheet?", "Anh/chị xuất báo cáo này ra file bảng tính được không?"),
  ("The dashboard updates every 15 minutes.", "Dashboard cập nhật 15 phút một lần."),
  ("We need to update the master data for the new items.", "Mình cần cập nhật dữ liệu gốc cho các mã hàng mới."),
  ("Our picking accuracy is 99.8% this month.", "Tháng này độ chính xác soạn hàng của mình là 99,8%."),
  ("The EDI order didn't come through this morning.", "Sáng nay đơn EDI không về hệ thống."),
  ("Who has access to change the data?", "Ai có quyền sửa dữ liệu?"),
 ],
 "dialogues": [
  ("The scanner says 'item not found'. What should I do?", [
    ("Check if the item is in the master data. If it isn't, ask the admin team to add it.", True, "Chỉ ra nguyên nhân khả dĩ + bước xử lý + người phụ trách."),
    ("Scanner broken, throw away.", False, "Kết luận vội; câu cụt, thiếu động từ và tân ngữ."),
    ("Just type any code.", False, "Sai quy trình — nhập mã bừa làm sai tồn kho."),
  ]),
  ("The WMS is down. Can we still ship today?", [
    ("Yes. We'll use the paper backup process and enter the data when the system is back.", True, "Có phương án dự phòng + nhắc nhập liệu bù."),
    ("No system, no ship.", False, "Cộc lốc, dịch từng chữ; không nghĩ tới phương án dự phòng."),
    ("We wait IT fix.", False, "Thiếu 'for' và 'to': 'We'll wait for IT to fix it.' — lại thụ động, không có phương án."),
  ]),
  ("Can the customer see where the truck is?", [
    ("Yes. The TMS gives real-time tracking, so the customer can see it on our portal.", True, "Xác nhận + tính năng + khách xem ở đâu."),
    ("Yes, can see.", False, "Thiếu chủ ngữ và tân ngữ: 'Yes, they can see it.'"),
    ("Customer call driver is faster.", False, "Sai cấu trúc câu và không trả lời câu hỏi về hệ thống."),
  ]),
  ("Why are the weights on these orders wrong?", [
    ("The master data for three new items was entered incorrectly. I've corrected it, so the next orders will be fine.", True, "Nguyên nhân gốc + đã sửa + tác động."),
    ("System make mistake.", False, "Sai chia động từ ('made'), thiếu mạo từ, đổ cho hệ thống — lỗi thường do dữ liệu nhập vào."),
    ("Weights not important.", False, "Sai — trọng lượng ảnh hưởng đến cước và chứng từ."),
  ]),
  ("What KPIs do you report every month?", [
    ("On-time delivery, picking accuracy and cost per order. I'll share the dashboard with you.", True, "Liệt kê KPI cụ thể + chủ động chia sẻ."),
    ("Many KPI, very good.", False, "Thiếu số nhiều ('KPIs') và không nêu cụ thể."),
    ("I report when boss ask.", False, "Sai chia động từ ('asks'), thiếu mạo từ, nghe thiếu chủ động."),
  ]),
 ],
 "listen": [
  ("Please scan the barcode on each carton", ["scan", "barcode"], "quét mã vạch"),
  ("The system is down this morning", ["system", "down"], "hệ thống sập"),
  ("The dashboard shows all late deliveries", ["dashboard", "late"], "xem dashboard"),
  ("Please update the master data today", ["update", "master"], "cập nhật dữ liệu gốc"),
  ("From Monday, we'll use the new WMS. Every pallet must be scanned in and out. Please collect your handheld scanner at the office.", ["Monday", "scanned", "handheld"], "thông báo dùng WMS mới"),
  ("Our picking accuracy was 99.5% last month. Most errors came from manual data entry. Next month, we'll use more barcodes.", ["accuracy", "manual", "barcodes"], "báo cáo KPI kho"),
 ],
})

# ───────────────────────── Vai trò: bổ sung ─────────────────────────
ROLES_X = {
 "docs": {
  "scenarios": [
   ("dc_lcdisc", "L/C bị bất hợp lệ", "You are a bank officer handling our export L/C. Tell me there are two discrepancies in our documents: late shipment and a wrong invoice amount. Ask how we want to solve them."),
   ("dc_ins", "Xin chứng từ bảo hiểm", "You are a foreign buyer on CIF terms. Ask me for the insurance certificate, the insured value and what the cover includes."),
  ],
  "dialogues": [
   ("The bank says our documents have a discrepancy.", [
     ("Could you tell me exactly what it is? If it's a typing error, I'll correct the document and send it back today.", True, "Hỏi rõ lỗi + phương án sửa nhanh."),
     ("Discrepancy where? We check carefully already.", False, "Câu hỏi cụt, sai thì ('We checked carefully') và nghe như cãi."),
     ("Bank always find problems.", False, "Sai chia động từ ('finds'), thiếu mạo từ, than phiền thay vì xử lý.")]),
   ("Can you send us the insurance certificate?", [
     ("Sure. The goods are insured for 110% of the CIF value. I'll email the certificate this afternoon.", True, "Xác nhận + mức bảo hiểm + thời gian gửi."),
     ("Insurance I buy already, no need paper.", False, "Trật tự từ kiểu Việt, sai thì; người mua CIF cần chứng từ bảo hiểm để đòi bồi thường."),
     ("Yes, later.", False, "Quá ngắn, không có thời gian cụ thể.")]),
   ("Why is the net weight on the packing list higher than the gross weight?", [
     ("That's my mistake. I swapped the two numbers. I'll send you a corrected packing list right away.", True, "Nhận lỗi rõ + nguyên nhân + gửi bản sửa ngay."),
     ("Net and gross same meaning.", False, "Sai kiến thức và thiếu động từ: trọng lượng tịnh luôn nhỏ hơn trọng lượng cả bì."),
     ("Maybe the scale is wrong.", False, "Đoán mò — tịnh lớn hơn cả bì là lỗi ghi số, không phải do cân.")]),
   ("Please send us the proforma invoice so we can open the L/C.", [
     ("Of course. I'll send it today. Please check the unit price, the quantity and the latest shipment date.", True, "Đồng ý + thời gian + nhắc các điểm cần kiểm tra."),
     ("OK, I send PI now now.", False, "Thiếu 'will', lặp 'now now' kiểu tiếng Việt."),
     ("Why you need PI?", False, "Sai trật tự câu hỏi; PI là căn cứ để mở L/C.")]),
  ]},
 "warehouse": {
  "scenarios": [
   ("wh_wms", "Chuyển sang WMS mới", "You are my foreign warehouse manager. We start using a new WMS next week. Ask me how I will train the team, what could go wrong and what our backup plan is."),
   ("wh_cold", "Khách xem kho lạnh", "You are a foreign food client visiting our cold storage. Ask about the temperature, how we record it and what happens if the power goes off."),
  ],
  "dialogues": [
   ("The new WMS starts on Monday. Is the team ready?", [
     ("Almost. Everyone has had two training sessions, and we'll do a test run on Saturday.", True, "Trả lời trung thực + việc đã làm + bước tiếp theo."),
     ("Ready, ready, no problem.", False, "Lặp từ, hứa suông, không có bằng chứng."),
     ("The team is learn now.", False, "Sai thì: 'The team is learning now.'")]),
   ("What temperature is the cold room?", [
     ("It's kept between 2 and 8 degrees. The sensors record it every 10 minutes.", True, "Con số cụ thể + cách ghi nhận nhiệt độ."),
     ("Very cold, don't worry.", False, "Không có số liệu."),
     ("Temperature is 2 to 8 degree.", False, "Thiếu 's' số nhiều ('degrees') và chưa nói cách theo dõi.")]),
   ("This barcode won't scan. Can I type the code?", [
     ("Yes, but please check it twice and tell the supervisor, so we can print a new label.", True, "Cho phép có kiểm soát + báo để in lại nhãn."),
     ("Type anything, it's OK.", False, "Sai quy trình — nhập sai mã làm lệch tồn kho."),
     ("Scanner is broken, stop working.", False, "Kết luận vội, sai ngữ pháp ('It has stopped working').")]),
   ("Where should we store the flammable paint?", [
     ("In the DG area, away from heat, with the SDS on the wall. Don't store it next to food.", True, "Chỉ dẫn đúng an toàn: khu riêng, xa nguồn nhiệt, có SDS, không để cạnh thực phẩm."),
     ("Anywhere is OK, it's closed.", False, "Nguy hiểm — hàng dễ cháy phải để ở khu riêng."),
     ("Put near the office, easy find.", False, "Thiếu tân ngữ ('Put it…', 'easy to find') và sai an toàn: không để hàng dễ cháy gần văn phòng.")]),
  ]},
 "forwarding": {
  "scenarios": [
   ("fw_reefer", "Container lạnh báo động", "You are a customer whose reefer container showed a temperature alarm at the port. Ask me what happened, whether the cargo is safe and what we are doing about it."),
   ("fw_multi", "Tuyến đa phương thức", "You are a customer who wants a cheaper option than air from Hanoi to Europe. Ask me about rail and sea-air options, costs and transit times."),
  ],
  "dialogues": [
   ("Our reefer had a temperature alarm at the port. Is the cargo OK?", [
     ("We're checking the temperature record now. The alarm lasted 40 minutes, and the cargo stayed below minus 15. I'll send you the report in an hour.", True, "Dữ liệu cụ thể + hẹn giờ gửi báo cáo."),
     ("Alarm is normal, don't care.", False, "Xem nhẹ vấn đề; 'don't care' nghe rất thô."),
     ("I think OK, maybe.", False, "Mơ hồ, không có dữ liệu.")]),
   ("Is there a cheaper option than air to Europe?", [
     ("Yes. Rail takes about 25 days and costs much less than air. Sea-air is another option, at around 20 days.", True, "Đưa hai phương án kèm thời gian để khách so sánh."),
     ("Cheaper is sea, slow slow.", False, "Trật tự từ, lặp từ kiểu Việt; chưa nói thời gian cụ thể."),
     ("No, air is only way.", False, "Sai thông tin, thiếu mạo từ ('the only way').")]),
   ("Can you ship these lithium batteries on Friday's vessel?", [
     ("Only if the carrier approves the DG booking in time. Please send the SDS and the UN number today.", True, "Nói rõ điều kiện + tài liệu cần gửi ngay."),
     ("Yes, sure, battery is normal.", False, "Sai chuyên môn — pin lithium là hàng nguy hiểm."),
     ("Friday no, because DG.", False, "Câu cụt, không giải thích quy trình hay phương án.")]),
   ("An online seller wants us to deliver 3,000 parcels a day. Can we handle it?", [
     ("We can handle about 2,000 now. For 3,000, we'd need two more trucks and an evening shift.", True, "Năng lực hiện tại + điều kiện để đáp ứng."),
     ("Yes, no problem, we can everything.", False, "Hứa suông; 'can everything' sai: 'we can do everything'."),
     ("3,000 is too much, say no.", False, "Từ chối ngay, không phân tích phương án.")]),
  ]},
 "purchasing": {
  "scenarios": [
   ("pu_pi", "PI & tiền cọc", "You are a foreign supplier. Send me your proforma invoice and ask for a 30% deposit by T/T. Answer my questions about bank charges and when production starts."),
   ("pu_pack", "Thay đổi quy cách đóng gói", "You are a foreign supplier. I am the buyer and I want to change the packing: stronger cartons, new shipping marks and heat-treated pallets. Discuss the extra cost and whether the lead time changes."),
  ],
  "dialogues": [
   ("Please pay a 30% deposit so we can start production.", [
     ("Sure. We'll send it by T/T on Wednesday, and I'll email you the bank slip.", True, "Đồng ý + phương thức + ngày + chứng từ."),
     ("OK, deposit I pay tomorrow.", False, "Trật tự từ kiểu Việt và thiếu 'will': 'I'll pay the deposit tomorrow.'"),
     ("Why deposit? We are big company.", False, "Thiếu mạo từ ('a big company') và thái độ khó chịu.")]),
   ("Who pays the bank charges?", [
     ("Each side pays its own bank charges. That's what the contract says.", True, "Trả lời đúng + căn cứ hợp đồng."),
     ("You pay all, you are seller.", False, "Áp đặt, thiếu mạo từ ('the seller')."),
     ("Bank charges small, no matter.", False, "Né câu hỏi, thiếu động từ ('are small').")]),
   ("Stronger cartons will cost 3% more.", [
     ("I see. Could you do 2%? And will the lead time stay the same?", True, "Thương lượng con số + hỏi tác động đến tiến độ."),
     ("3% is too much, no.", False, "Cộc lốc, không đề xuất gì."),
     ("Why carton so expensive?", False, "Thiếu động từ: 'Why are the cartons so expensive?'")]),
   ("What shipping marks do you need on the cartons?", [
     ("Please show our company name, the PO number, the carton number, like '1 of 50', and the country of origin.", True, "Liệt kê cụ thể nội dung ký mã hiệu."),
     ("Any mark is OK.", False, "Mơ hồ — ký mã hiệu sai làm khó nhận hàng và khó khớp chứng từ."),
     ("Mark like last time, you remember.", False, "Không rõ ràng, dễ sai; nên gửi yêu cầu cụ thể bằng văn bản.")]),
  ]},
}

EXTRA = {
 "phases": PHASES,
 "rev": [
  ("Trọng lượng tính cước là 150 ký.", "The chargeable weight is 150 kilos."),
  ("Hàng bị rút xuống khỏi chuyến bay tối qua.", "The cargo was offloaded from last night's flight."),
  ("Container lạnh phải cắm điện ngay.", "The reefer must be plugged in right away."),
  ("Lô này có hàng nguy hiểm.", "This shipment contains dangerous goods."),
  ("Anh/chị gửi giúp tôi SDS nhé.", "Could you send me the SDS, please?"),
  ("Gói hàng đang được giao hôm nay.", "The parcel is out for delivery today."),
  ("Khách từ chối nhận hàng.", "The customer refused the parcel."),
  ("Phí bảo hiểm là 50 đô.", "The premium is 50 dollars."),
  ("Hợp đồng bảo hiểm không bảo hiểm lỗi đóng gói.", "The policy doesn't cover poor packing."),
  ("Bên tôi đã nhận tiền cọc.", "We've received the deposit."),
  ("Tiền chưa về tài khoản bên tôi.", "The money hasn't arrived in our account yet."),
  ("L/C hết hạn vào cuối tháng này.", "The L/C expires at the end of this month."),
  ("Xếp thùng nặng ở dưới.", "Put the heavy cartons at the bottom."),
  ("Nhớ khai VGM trước giờ cắt máng.", "Please submit the VGM before the cut-off."),
  ("Đi sà lan rẻ hơn nhưng chậm hơn.", "Barge is cheaper, but it's slower."),
  ("Hệ thống bị sập từ sáng.", "The system has been down since this morning."),
 ],
 "reading": [
  {"t": "Air freight quote", "text": "Subject: Air quote – Hanoi to Frankfurt\nHi Ms Thu,\nThanks for your enquiry. For 5 cartons (300 kg, 2.4 cbm):\nChargeable weight: 400 kg (volumetric)\nRate: USD 3.20/kg, all-in\nFlights: direct, every Tuesday and Friday\nPlease deliver the cargo to the cargo terminal one day before the flight.\nBest regards,\nDaniel", "q": [
    {"q": "Why is the chargeable weight 400 kg?", "o": ["The rate is all-in", "It's based on the volumetric weight", "There are five cartons"], "a": 1},
    {"q": "When should the cargo reach the terminal?", "o": ["On the day of the flight", "One day before the flight", "Every Tuesday"], "a": 1}]},
  {"t": "Reefer booking remarks", "text": "REEFER BOOKING – REMARKS\nCommodity: Frozen shrimp\nSet point: -20°C  |  Vents: closed\nPower: plug in within 2 hours of gate-in\nA temperature record is required for the whole voyage.\nIf an alarm appears, contact the reefer desk at once.", "q": [
    {"q": "What is the set point?", "o": ["-2°C", "-18°C", "-20°C"], "a": 2},
    {"q": "What must happen within 2 hours of gate-in?", "o": ["The container must be plugged in", "The vents must be opened", "The record must be sent"], "a": 0}]},
  {"t": "Delivery app message", "text": "Delivery update – Order #58214\nWe tried to deliver your parcel today at 14:20, but we couldn't reach you by phone.\nNext attempt: tomorrow, 9:00–12:00\nCOD amount: 420,000 VND\nAfter 3 failed attempts, the parcel will be returned to the seller.\nReply 1 to confirm, or 2 to change the address.", "q": [
    {"q": "How much must the customer pay?", "o": ["420,000 VND", "58,214 VND", "Nothing"], "a": 0},
    {"q": "What happens after three failed attempts?", "o": ["The driver calls again", "The parcel goes back to the seller", "The address is changed"], "a": 1}]},
  {"t": "Bank discrepancy notice", "text": "NOTICE OF DISCREPANCY\nL/C No.: 0425-778\nBeneficiary: An Khang Seafood Co.\nDiscrepancies:\n1. Late shipment: B/L dated 18 May, latest shipment date 15 May.\n2. Invoice amount exceeds the L/C amount by USD 350.\nWe are holding the documents and will ask the applicant whether they accept the discrepancies.", "q": [
    {"q": "How many days late was the shipment?", "o": ["Two", "Three", "Five"], "a": 1},
    {"q": "What will the bank do next?", "o": ["Pay the beneficiary now", "Return the goods", "Ask the applicant to accept the discrepancies"], "a": 2}]},
  {"t": "Loading instructions", "text": "LOADING INSTRUCTIONS – PO 3390\nContainer: 1 x 40' HC\nCargo: 22 pallets, max. 2 pallets high\nPallets: heat-treated, ISPM 15 mark required\nStretch-wrap each pallet with 3 layers.\nPhotos: empty container, half-loaded, fully loaded, sealed.\nSend the VGM to the carrier by Thursday 12:00.", "q": [
    {"q": "How many layers of stretch wrap are needed?", "o": ["Two", "Three", "Twenty-two"], "a": 1},
    {"q": "When is the VGM due?", "o": ["Thursday 12:00", "After sealing", "Friday 12:00"], "a": 0}]},
 ],
 "ai": [
  ("air", "Báo giá hàng air", "You are a foreign customer who needs to send 250 kilos of spare parts by air to Germany. Ask me, a forwarder, about the chargeable weight, the rate, the flight and the transit time."),
  ("dg", "Booking hàng nguy hiểm", "You are a carrier's booking officer. I want to book a container of paint, which is dangerous goods. Ask me for the UN number, the SDS and the packing details, and explain the extra checks."),
  ("lc", "Kiểm tra điều khoản L/C", "You are a foreign buyer who has just opened an L/C for my company. Ask me whether the latest shipment date, the expiry date and the required documents are OK. Agree to amend one date if I explain why."),
  ("lastmile", "Giao hàng chặng cuối", "You are an online shopper whose parcel had a failed delivery. Call me at the delivery company's customer service. Sound a little annoyed and ask when it will arrive and whether you can change the address."),
 ],
 "events": [
  ("wms_golive", "Chạy hệ thống kho mới", "You are my foreign project manager. Our new WMS goes live next Monday. Ask me about training, data migration, scanners and what we will do if the system goes down."),
  ("mega_sale", "Đợt sale lớn thương mại điện tử", "You are the foreign operations director of an online shop. Our biggest sale of the year is next week. Ask me about warehouse staff, delivery capacity, failed deliveries and returns."),
  ("dg_audit", "Kiểm tra an toàn hàng nguy hiểm", "You are a foreign safety auditor checking how we store and ship dangerous goods. Ask about labels, SDS files, storage areas, staff training and what we do in case of a spill."),
 ],
 "quips": [
  "Chargeable weight: checked!",
  "Keep calm and stay cold!",
  "Parcel out for delivery!",
  "L/C documents all match!",
  "Pallet wrapped, three layers!",
  "Beep! Barcode scanned!",
 ],
 "roles": ROLES_X,
}
