# -*- coding: utf-8 -*-
# v4.1 — nội dung làm giàu cho gói hotel (nối vào cuối gói, xem build.py)

PHASES = []

# ───────────────────────── 11. Concierge & đặt dịch vụ hộ khách ─────────────────────────
PHASES.append({
 "title": "Concierge & đặt dịch vụ hộ khách",
 "vocab": [
  ("concierge", "/ˌkɒnsiˈeəʒ/", "n", "nhân viên/quầy hỗ trợ khách (đặt vé, đặt bàn, tư vấn)", "Please ask the <b>concierge</b> about tickets for the show.", "Anh/chị hỏi quầy concierge về vé xem biểu diễn nhé.", "コンシェルジュ", "konsheruju"),
  ("on behalf of", "/ɒn bɪˈhɑːf əv/", "phr", "thay mặt, thay cho (ai)", "I called the restaurant <b>on behalf of</b> Mr. Hill.", "Tôi đã thay mặt ông Hill gọi cho nhà hàng."),
  ("voucher", "/ˈvaʊtʃə/", "n", "phiếu dịch vụ, phiếu xác nhận (tour, spa…)", "Please show this <b>voucher</b> to the driver.", "Anh/chị đưa phiếu này cho tài xế nhé.", "バウチャー", "bauchā"),
  ("confirmation number", "/ˌkɒnfəˈmeɪʃn ˌnʌmbə/", "n", "mã xác nhận (đặt chỗ)", "Your <b>confirmation number</b> is in the email.", "Mã xác nhận của anh/chị có trong email.", "予約番号", "yoyaku bangō"),
  ("cooking class", "/ˈkʊkɪŋ klɑːs/", "n", "lớp học nấu ăn", "The <b>cooking class</b> starts with a trip to the market.", "Lớp học nấu ăn bắt đầu bằng một chuyến đi chợ."),
  ("tailor", "/ˈteɪlə/", "n", "thợ may (may đo)", "A good <b>tailor</b> can make a suit in two days.", "Một thợ may giỏi có thể may xong bộ vest trong hai ngày."),
  ("dress code", "/ˈdres kəʊd/", "n", "quy định trang phục", "The restaurant has a <b>dress code</b>: no shorts or flip-flops.", "Nhà hàng có quy định trang phục: không mặc quần short, không đi dép tông.", "ドレスコード", "doresu kōdo"),
  ("day trip", "/ˈdeɪ trɪp/", "n", "chuyến đi trong ngày", "Mỹ Sơn is an easy <b>day trip</b> from Hội An.", "Từ Hội An đi Mỹ Sơn về trong ngày rất tiện."),
  ("opening hours", "/ˈəʊpənɪŋ ˌaʊəz/", "n", "giờ mở cửa", "Let me check the museum's <b>opening hours</b>.", "Để tôi kiểm tra giờ mở cửa của bảo tàng.", "営業時間", "eigyō jikan"),
  ("in advance", "/ɪn ədˈvɑːns/", "phr", "trước (đặt trước, báo trước)", "Please book the show two days <b>in advance</b>.", "Anh/chị nên đặt vé xem biểu diễn trước hai ngày."),
 ],
 "phrases": [
  ("Good morning. What can I arrange for you today?", "Chào buổi sáng. Hôm nay tôi có thể sắp xếp gì cho anh/chị ạ?"),
  ("I'd be happy to book that for you.", "Tôi rất sẵn lòng đặt giúp anh/chị."),
  ("For how many people, and at what time?", "Cho mấy người và lúc mấy giờ ạ?"),
  ("I've booked a table for two at 7:30 under your name.", "Tôi đã đặt bàn cho hai người lúc 7 giờ 30 theo tên anh/chị."),
  ("Here's your voucher. Please show it at the entrance.", "Đây là phiếu dịch vụ. Anh/chị xuất trình ở lối vào nhé."),
  ("The show is very popular, so it's best to book in advance.", "Buổi biểu diễn rất đông khách nên tốt nhất là đặt trước."),
  ("There's a small booking fee of 50,000 dong.", "Có một khoản phí đặt chỗ nhỏ là 50.000 đồng."),
  ("Just so you know, the restaurant has a dress code.", "Anh/chị lưu ý giúp, nhà hàng có quy định về trang phục."),
  ("I'll call your room when it's confirmed.", "Khi có xác nhận, tôi sẽ gọi lên phòng cho anh/chị."),
  ("I'm afraid it's sold out tonight. Would tomorrow work for you?", "Tôi e là tối nay đã hết vé. Ngày mai có được không ạ?"),
 ],
 "dialogues": [
  ("Could you book us a table somewhere nice for dinner tonight?", [
    ("Of course. What kind of food would you like, and what time?", True, "Nhận lời + hỏi khẩu vị và giờ trước khi đặt."),
    ("You search on internet, many restaurants.", False, "Đẩy việc cho khách, thiếu 'the' — concierge phải đặt giúp."),
    ("OK, I book restaurant for you.", False, "Thiếu 'will' và mạo từ, chưa hỏi giờ, số người: 'I'll book it for you. What time?'"),
  ]),
  ("Can you get us two tickets for the water puppet show tomorrow?", [
    ("Let me check. Yes, there are seats at 6 p.m. They're 200,000 dong each. Shall I book them?", True, "Kiểm tra + giờ + giá + hỏi khách xác nhận trước khi đặt."),
    ("Tickets have, 6 p.m.", False, "Dịch từng chữ 'vé thì có': 'There are tickets for 6 p.m.'"),
    ("Yes, sure, no problem, I get.", False, "Hứa ngay khi chưa kiểm tra, thiếu 'will' và tân ngữ ('I'll get them')."),
  ]),
  ("I'd like to have a suit made while I'm here. Do you know a good tailor?", [
    ("Yes, we work with a tailor in the old town. How long are you staying? A suit usually takes two or three days.", True, "Giới thiệu + hỏi thời gian lưu trú + báo thời gian may."),
    ("Tailor very many in Hội An.", False, "Thiếu động từ ('There are many tailors') và không giới thiệu chỗ cụ thể."),
    ("You go old town, find yourself.", False, "Cộc, thiếu 'to the', bỏ mặc khách tự tìm."),
  ]),
  ("Is there a dress code at that restaurant?", [
    ("Yes, it's smart casual. Shorts and flip-flops aren't allowed.", True, "Trả lời + nói rõ nên mặc gì, không được mặc gì."),
    ("Yes, have dress code.", False, "Thiếu chủ ngữ: 'Yes, there is.' — và nên nói cụ thể."),
    ("You can wear anything you like.", False, "Nói sai quy định — khách có thể bị từ chối ở cửa."),
  ]),
  ("The cooking class is full? That's a shame. We really wanted to do it.", [
    ("I'm sorry. I can put you on the waiting list, or book you for Thursday. Which would you prefer?", True, "Xin lỗi + hai phương án + để khách chọn."),
    ("Full is full, sorry.", False, "Cứng nhắc, không đưa lựa chọn nào."),
    ("Next time you book early.", False, "Trách khách — nên đưa phương án khác thay vì dạy khách."),
  ]),
 ],
 "listen": [
  ("I booked a table for two at seven", ["booked", "two"], "đặt bàn hộ khách"),
  ("Please show this voucher at the entrance", ["voucher", "entrance"], "đưa phiếu dịch vụ"),
  ("The museum is closed on Mondays", ["museum", "Mondays"], "giờ mở cửa bảo tàng"),
  ("It's best to book the show in advance", ["show", "advance"], "đặt vé trước"),
  ("Good news, Mr. Hill. I've booked the cooking class for tomorrow morning. The driver will pick you up at eight.", ["cooking", "tomorrow", "driver"], "báo đặt dịch vụ thành công"),
  ("The restaurant is fully booked at seven, but they have a table at eight thirty. Would that work for you? Please note there is a dress code.", ["seven", "table", "dress"], "báo phương án khác cho khách"),
 ],
})

# ───────────────────────── 12. Đưa đón sân bay & vận chuyển ─────────────────────────
PHASES.append({
 "title": "Đưa đón sân bay & vận chuyển",
 "vocab": [
  ("pick-up", "/ˈpɪk ʌp/", "n", "việc đón (khách)", "Your <b>pick-up</b> is at 9:15 from the lobby.", "Xe đón anh/chị lúc 9 giờ 15 ở sảnh."),
  ("flight number", "/ˈflaɪt ˌnʌmbə/", "n", "số hiệu chuyến bay", "Could you tell me your <b>flight number</b>, please?", "Anh/chị cho tôi biết số hiệu chuyến bay được không ạ?", "便名", "binmei"),
  ("arrivals hall", "/əˈraɪvlz hɔːl/", "n", "sảnh đến (sân bay)", "Our driver will wait for you in the <b>arrivals hall</b>.", "Tài xế của chúng tôi sẽ đợi anh/chị ở sảnh đến.", "到着ロビー", "tōchaku robī"),
  ("name sign", "/ˈneɪm saɪn/", "n", "bảng tên (tài xế cầm khi đón khách)", "Look for a driver with a <b>name sign</b> that says 'Hoa Sen Hotel'.", "Anh/chị tìm tài xế cầm bảng tên ghi 'Hoa Sen Hotel' nhé."),
  ("delayed", "/dɪˈleɪd/", "adj", "bị trễ, bị hoãn", "My flight is <b>delayed</b> by two hours.", "Chuyến bay của tôi bị trễ hai tiếng."),
  ("baggage claim", "/ˈbæɡɪdʒ kleɪm/", "n", "khu nhận hành lý (băng chuyền)", "The driver will meet you after <b>baggage claim</b>.", "Tài xế sẽ gặp anh/chị sau khu nhận hành lý."),
  ("seven-seater", "/ˌsevn ˈsiːtə/", "n", "xe bảy chỗ", "For five people with big bags, we'll send a <b>seven-seater</b>.", "Năm người mang vali lớn thì chúng tôi sẽ cho xe bảy chỗ."),
  ("fare", "/feə/", "n", "giá cước, tiền xe", "The taxi <b>fare</b> to the airport is about 200,000 dong.", "Tiền taxi ra sân bay khoảng 200.000 đồng.", "運賃", "unchin"),
  ("traffic jam", "/ˈtræfɪk dʒæm/", "n", "tắc đường, kẹt xe", "Please leave early. There's often a <b>traffic jam</b> at 5 p.m.", "Anh/chị nên đi sớm. Tầm 5 giờ chiều hay bị kẹt xe.", "渋滞", "jūtai"),
  ("drop-off", "/ˈdrɒp ɒf/", "n", "việc đưa khách đến nơi; điểm trả khách", "The <b>drop-off</b> point is Terminal 2.", "Điểm trả khách là nhà ga số 2."),
 ],
 "phrases": [
  ("Could you send me your flight number and arrival time?", "Anh/chị gửi tôi số hiệu chuyến bay và giờ đến được không ạ?"),
  ("Our driver will be waiting in the arrivals hall with a name sign.", "Tài xế của chúng tôi sẽ đợi ở sảnh đến với bảng tên."),
  ("It takes about 30 minutes to get to the hotel.", "Về đến khách sạn mất khoảng 30 phút."),
  ("The transfer costs 300,000 dong one way.", "Xe đưa đón giá 300.000 đồng một chiều."),
  ("We track your flight, so don't worry if it's delayed.", "Chúng tôi theo dõi chuyến bay, nên nếu bị trễ anh/chị đừng lo."),
  ("How many pieces of luggage do you have?", "Anh/chị có bao nhiêu kiện hành lý ạ?"),
  ("I'd suggest leaving at three because of the traffic.", "Tôi nghĩ anh/chị nên đi lúc 3 giờ vì đường hay kẹt."),
  ("Your driver's name is Tuấn, and here's his phone number.", "Tài xế của anh/chị tên là Tuấn, và đây là số điện thoại của anh ấy."),
  ("Is it a domestic or an international flight?", "Chuyến bay nội địa hay quốc tế ạ?"),
 ],
 "dialogues": [
  ("I'd like to book an airport pick-up for Friday.", [
    ("Certainly. Could I have your flight number and arrival time, please?", True, "Nhận lời + xin đúng hai thông tin cần để đón."),
    ("OK. What time you come?", False, "Thiếu trợ động từ: 'What time do you arrive?' — và nên xin số hiệu chuyến bay."),
    ("Friday OK. Driver go.", False, "Cộc lốc, động từ không chia, chưa hỏi chuyến bay."),
  ]),
  ("My flight is delayed by two hours. Will the driver still be there?", [
    ("Yes, don't worry. We track your flight, and the driver will wait for you in the arrivals hall.", True, "Trấn an + giải thích + nơi tài xế đợi."),
    ("Driver waiting long, you pay more.", False, "Thiếu 'is' và đòi tiền ngay khi khách đang lo — nên trấn an trước."),
    ("I don't know. Maybe he go home.", False, "Mơ hồ, sai ngôi ('goes') — nên kiểm tra rồi xác nhận cho khách."),
  ]),
  ("There are six of us with a lot of bags. Will one car be enough?", [
    ("I'd suggest a sixteen-seat van. A seven-seater would be too small with all your bags.", True, "Đề xuất xe phù hợp + lý do rõ ràng."),
    ("Yes, one car can.", False, "Câu cụt, thiếu động từ chính — lại chưa tính đến hành lý."),
    ("Six people is many.", False, "Nhận xét thừa, sai chia động từ ('are'), không đưa giải pháp."),
  ]),
  ("How long does it take to get to the airport?", [
    ("Usually about 40 minutes, but it can take an hour at rush hour. I'd suggest leaving by three.", True, "Thời gian + lưu ý giờ cao điểm + gợi ý giờ đi."),
    ("Not far, fast.", False, "Mơ hồ, không có con số."),
    ("It take 40 minutes.", False, "Thiếu 's': 'It takes about 40 minutes.'"),
  ]),
  ("I can't find the driver. I'm outside the arrivals hall.", [
    ("I'm sorry. Let me call him now. Could you wait near Exit B? He'll be there in two minutes.", True, "Xin lỗi + gọi tài xế + dặn khách đứng ở đâu."),
    ("You find again, he is there.", False, "Đẩy việc cho khách, câu thiếu chuẩn ('Please look again')."),
    ("Driver is busy, wait.", False, "Cộc và làm khách lo thêm — cần liên hệ tài xế ngay."),
  ]),
 ],
 "listen": [
  ("Could I have your flight number, please", ["flight", "number"], "hỏi số hiệu chuyến bay"),
  ("The driver will wait in the arrivals hall", ["driver", "arrivals"], "tài xế đợi ở đâu"),
  ("There is often a traffic jam after five", ["traffic", "five"], "giờ kẹt xe"),
  ("The taxi fare is about two hundred thousand dong", ["fare", "hundred"], "giá taxi"),
  ("Welcome to Đà Nẵng, Ms. Park. My name is Tuấn, from Hoa Sen Hotel. The car is just outside, and the trip takes twenty minutes.", ["Welcome", "outside", "twenty"], "tài xế đón khách"),
  ("Your flight leaves at nine tonight. Because of the traffic, I suggest leaving the hotel at six. Our car will be ready in front of the lobby.", ["leaves", "traffic", "ready"], "dặn giờ ra sân bay"),
 ],
})

# ───────────────────────── 13. Spa, hồ bơi & tiện ích ─────────────────────────
PHASES.append({
 "title": "Spa, hồ bơi & tiện ích",
 "vocab": [
  ("spa", "/spɑː/", "n", "spa, khu chăm sóc sức khoẻ và làm đẹp", "The <b>spa</b> is on the fourth floor, next to the gym.", "Spa ở tầng bốn, cạnh phòng gym.", "スパ", "supa"),
  ("massage", "/ˈmæsɑːʒ/", "n", "mát-xa", "A 60-minute <b>massage</b> costs 600,000 dong.", "Mát-xa 60 phút giá 600.000 đồng.", "マッサージ", "massāji"),
  ("treatment", "/ˈtriːtmənt/", "n", "liệu trình (spa)", "Please arrive ten minutes before your <b>treatment</b>.", "Anh/chị vui lòng đến trước giờ làm liệu trình mười phút."),
  ("therapist", "/ˈθerəpɪst/", "n", "kỹ thuật viên trị liệu (spa)", "Would you prefer a male or a female <b>therapist</b>?", "Anh/chị muốn kỹ thuật viên nam hay nữ ạ?", "セラピスト", "serapisuto"),
  ("sauna", "/ˈsɔːnə/", "n", "phòng xông hơi khô", "The <b>sauna</b> is free for hotel guests.", "Khách lưu trú được dùng phòng xông hơi miễn phí.", "サウナ", "sauna"),
  ("lifeguard", "/ˈlaɪfɡɑːd/", "n", "nhân viên cứu hộ", "There's a <b>lifeguard</b> at the pool from 8 a.m. to 6 p.m.", "Hồ bơi có nhân viên cứu hộ từ 8 giờ sáng đến 6 giờ chiều."),
  ("sun lounger", "/ˈsʌn ˌlaʊndʒə/", "n", "ghế nằm tắm nắng", "Shall I bring a towel to your <b>sun lounger</b>?", "Tôi mang khăn ra ghế nằm cho anh/chị nhé?"),
  ("pool towel", "/ˈpuːl ˌtaʊəl/", "n", "khăn hồ bơi", "Please return your <b>pool towel</b> when you leave.", "Khi về, anh/chị vui lòng trả lại khăn hồ bơi."),
  ("facilities", "/fəˈsɪlətiz/", "n", "các tiện ích, cơ sở vật chất", "Our <b>facilities</b> include a pool, a gym and a spa.", "Tiện ích của khách sạn gồm hồ bơi, phòng gym và spa.", "施設", "shisetsu"),
  ("pressure", "/ˈpreʃə/", "n", "lực (khi mát-xa)", "Is the <b>pressure</b> OK, or would you like it lighter?", "Lực như vậy được chưa, hay anh/chị muốn nhẹ hơn ạ?"),
 ],
 "phrases": [
  ("Would you like to book a massage for this afternoon?", "Anh/chị có muốn đặt mát-xa chiều nay không ạ?"),
  ("We have a 60-minute and a 90-minute option.", "Chúng tôi có gói 60 phút và 90 phút ạ."),
  ("Do you have any health problems or injuries we should know about?", "Anh/chị có vấn đề sức khoẻ hay chấn thương nào chúng tôi cần biết không ạ?"),
  ("Please tell me if the pressure is too strong.", "Nếu lực mạnh quá anh/chị cứ báo tôi nhé."),
  ("Please take a shower before using the pool.", "Anh/chị vui lòng tắm tráng trước khi xuống hồ bơi."),
  ("The pool is open from 6 a.m. to 8 p.m.", "Hồ bơi mở cửa từ 6 giờ sáng đến 8 giờ tối."),
  ("No glass is allowed near the pool.", "Không được mang đồ thuỷ tinh ra khu hồ bơi."),
  ("You can pick up a pool towel here.", "Anh/chị có thể lấy khăn hồ bơi ở đây."),
  ("How was your treatment? Would you like some ginger tea?", "Liệu trình thế nào ạ? Anh/chị dùng chút trà gừng nhé?"),
  ("The treatment can be charged to your room.", "Phí liệu trình có thể tính vào tiền phòng ạ."),
 ],
 "dialogues": [
  ("I'd like a massage this afternoon. Do you have any free times?", [
    ("Let me check. We have 2 p.m. or 4:30. Would you like 60 or 90 minutes?", True, "Kiểm tra + đưa giờ trống + hỏi gói."),
    ("Afternoon have, 2 and 4:30.", False, "Dịch từng chữ 'chiều thì có': 'We have free times at 2 and 4:30.'"),
    ("Yes, you come anytime.", False, "Hứa bừa khi chưa xem lịch — spa cần đặt giờ và xếp kỹ thuật viên."),
  ]),
  ("That's a bit too strong for me.", [
    ("I'm sorry. I'll make it lighter. Please tell me if it's still too strong.", True, "Xin lỗi + chỉnh lực ngay + mời khách báo tiếp."),
    ("Strong is good for you.", False, "Áp ý mình lên khách — khách thấy mạnh thì phải giảm lực."),
    ("OK, I do soft.", False, "Thiếu 'will', sai từ: 'I'll make it lighter.'"),
  ]),
  ("Is there a lifeguard at the pool? My kids want to swim.", [
    ("Yes, from 8 a.m. to 6 p.m. But children under 12 must be with an adult at all times.", True, "Trả lời + giờ có cứu hộ + nhắc quy định an toàn cho trẻ."),
    ("Yes, so kids can swim alone.", False, "Nguy hiểm — dù có cứu hộ, trẻ vẫn phải có người lớn trông."),
    ("Lifeguard have, no worry.", False, "Dịch từng chữ, thiếu chủ ngữ và chủ quan về an toàn."),
  ]),
  ("Can I use the sauna? I'm not staying at the hotel.", [
    ("Yes, you can buy a day pass for 250,000 dong. It includes the pool, the sauna and the gym.", True, "Trả lời + phương án (vé ngày) + những gì bao gồm."),
    ("No guest, no sauna.", False, "Cộc lốc, lại bỏ lỡ cơ hội bán vé ngày."),
    ("You can, but you must to pay.", False, "Sau 'must' không có 'to': 'You need to buy a day pass.'"),
  ]),
  ("I'm pregnant. Can I still have a massage?", [
    ("Yes, we have a special pregnancy massage. Could you fill in this health form first, please?", True, "Có liệu trình phù hợp + làm phiếu sức khoẻ trước — đúng quy trình an toàn."),
    ("Yes, any massage is OK.", False, "Không an toàn — bà bầu cần liệu trình và kỹ thuật riêng."),
    ("Pregnant cannot massage.", False, "Thiếu chủ ngữ và không đúng — nhiều spa có mát-xa riêng cho bà bầu."),
  ]),
 ],
 "listen": [
  ("Would you like a massage this afternoon", ["massage", "afternoon"], "mời đặt mát-xa"),
  ("Please take a shower before you swim", ["shower", "swim"], "quy định hồ bơi"),
  ("The sauna is next to the gym", ["sauna", "gym"], "vị trí phòng xông hơi"),
  ("Is the pressure OK for you", ["pressure", "OK"], "hỏi lực mát-xa"),
  ("Welcome to the spa. Please fill in this short health form. Your therapist will be ready in five minutes.", ["health", "therapist", "five"], "đón khách ở spa"),
  ("The pool is open until eight tonight. You can get a pool towel at the bar. Please don't bring glass near the water.", ["eight", "towel", "glass"], "dặn quy định hồ bơi"),
 ],
})

# ───────────────────────── 14. Bar & đồ uống ─────────────────────────
PHASES.append({
 "title": "Bar & đồ uống",
 "vocab": [
  ("cocktail", "/ˈkɒkteɪl/", "n", "cốc-tai", "Our signature <b>cocktail</b> is made with passion fruit.", "Cốc-tai đặc trưng của quán làm từ chanh dây.", "カクテル", "kakuteru"),
  ("draught beer", "/ˌdrɑːft ˈbɪə/", "n", "bia tươi (bia rót vòi)", "A glass of <b>draught beer</b> is 60,000 dong.", "Một ly bia tươi giá 60.000 đồng.", "生ビール", "nama bīru"),
  ("happy hour", "/ˌhæpi ˈaʊə/", "n", "giờ vàng (giảm giá đồ uống)", "<b>Happy hour</b> is from 5 to 7: buy one, get one free.", "Giờ vàng từ 5 đến 7 giờ: mua một tặng một.", "ハッピーアワー", "happī awā"),
  ("on the rocks", "/ɒn ðə ˈrɒks/", "phr", "(rượu) uống với đá", "I'll have a whisky <b>on the rocks</b>, please.", "Cho tôi một ly whisky với đá.", "ロック", "rokku"),
  ("non-alcoholic", "/ˌnɒn ælkəˈhɒlɪk/", "adj", "không cồn", "We have three <b>non-alcoholic</b> cocktails.", "Quán có ba loại cốc-tai không cồn.", "ノンアルコール", "non'arukōru"),
  ("bartender", "/ˈbɑːtendə/", "n", "nhân viên pha chế (bartender)", "Our <b>bartender</b> can make it less sweet for you.", "Nhân viên pha chế có thể làm bớt ngọt cho anh/chị.", "バーテンダー", "bātendā"),
  ("last orders", "/ˌlɑːst ˈɔːdəz/", "n", "lượt gọi đồ cuối cùng (trước khi đóng cửa)", "<b>Last orders</b> at the bar are at 11:30.", "Quầy bar nhận gọi đồ lần cuối lúc 11 giờ 30.", "ラストオーダー", "rasuto ōdā"),
  ("by the glass", "/baɪ ðə ˈɡlɑːs/", "phr", "(bán) theo ly", "We sell red and white wine <b>by the glass</b>.", "Quán bán rượu vang đỏ và trắng theo ly."),
  ("tab", "/tæb/", "n", "hoá đơn ghi dồn (trả một lần lúc cuối)", "Would you like to open a <b>tab</b>?", "Anh/chị có muốn ghi dồn rồi thanh toán một lần không ạ?"),
  ("house wine", "/ˌhaʊs ˈwaɪn/", "n", "vang của nhà hàng (loại phổ thông, giá mềm)", "Our <b>house wine</b> is from Chile.", "Vang nhà (house wine) của chúng tôi là vang Chile.", "ハウスワイン", "hausu wain"),
 ],
 "phrases": [
  ("Good evening. What can I get you?", "Chào buổi tối. Anh/chị dùng gì ạ?"),
  ("Would you like to see the cocktail menu?", "Anh/chị có muốn xem thực đơn cốc-tai không ạ?"),
  ("It's happy hour, so all cocktails are half price.", "Đang giờ vàng nên tất cả cốc-tai giảm nửa giá."),
  ("Would you like that with ice?", "Anh/chị có dùng đá không ạ?"),
  ("We have a local craft beer on tap.", "Quán có bia thủ công địa phương rót vòi ạ."),
  ("Could I see some ID, please?", "Cho tôi xem giấy tờ tuỳ thân được không ạ?"),
  ("It's last orders. Can I get you anything else?", "Đây là lượt gọi cuối. Anh/chị dùng thêm gì không ạ?"),
  ("Would you like to pay now or open a tab?", "Anh/chị muốn thanh toán luôn hay ghi dồn trả sau ạ?"),
  ("Let me get you some water and call you a taxi.", "Để tôi lấy cho anh/chị ít nước và gọi taxi nhé."),
  ("Here you are. Enjoy your drink!", "Của anh/chị đây. Chúc anh/chị thưởng thức vui vẻ!"),
 ],
 "dialogues": [
  ("What local beer do you have?", [
    ("We have two local beers on tap and a craft beer in bottles. Would you like to try a little first?", True, "Liệt kê cụ thể + mời khách nếm thử."),
    ("Beer is many kind.", False, "Sai số nhiều và không nói loại nào: 'We have several kinds.'"),
    ("Local beer is cheap.", False, "Không trả lời quán có loại bia nào."),
  ]),
  ("Can I get a mojito without alcohol?", [
    ("Of course. Our bartender can make a non-alcoholic mojito. Would you like it less sweet?", True, "Đồng ý + gọi đúng tên đồ uống + hỏi khẩu vị."),
    ("Mojito no alcohol is not mojito.", False, "Cãi khách, thiếu thiện chí — quầy bar thường pha được bản không cồn."),
    ("Yes, I make no alcohol.", False, "Thiếu 'will' và dịch từng chữ: 'Sure, I'll make it without alcohol.'"),
  ]),
  ("Is it still happy hour?", [
    ("I'm sorry, happy hour finished at seven. But our house wine is still a good price.", True, "Trả lời thật + gợi ý lựa chọn giá tốt."),
    ("Happy hour finish already.", False, "Sai thì: 'Happy hour finished at seven.'"),
    ("No. Normal price.", False, "Cộc, không gợi ý gì thêm."),
  ]),
  ("The guest at the end of the bar is very drunk, and he wants another whisky.", [
    ("Let's stop serving him alcohol. I'll offer him some water and ask security to help him back to his room.", True, "Ngừng bán rượu + chăm sóc + nhờ an ninh hỗ trợ — đúng quy trình phục vụ có trách nhiệm."),
    ("He pays, so we give more.", False, "Bán tiếp cho khách say là nguy hiểm và sai quy trình."),
    ("Drunk guest, not my problem.", False, "Thiếu động từ và đẩy trách nhiệm — cả ca phải cùng xử lý."),
  ]),
  ("Can I pay for all the drinks at the end?", [
    ("Of course. I'll open a tab for you. Could I have your room number, please?", True, "Đồng ý + mở tab + xin số phòng."),
    ("Yes, end pay.", False, "Dịch từng chữ 'cuối trả': 'Sure, you can pay at the end.'"),
    ("No, pay each drink.", False, "Cứng nhắc và thiếu 'for' — khách lưu trú thường được ghi dồn."),
  ]),
 ],
 "listen": [
  ("Happy hour is from five to seven", ["Happy", "seven"], "giờ vàng"),
  ("Would you like your whisky on the rocks", ["whisky", "rocks"], "hỏi uống với đá"),
  ("We sell house wine by the glass", ["wine", "glass"], "bán vang theo ly"),
  ("Last orders at the bar are at eleven thirty", ["Last", "eleven"], "giờ gọi đồ cuối"),
  ("Good evening. Here's our cocktail menu. It's happy hour now, so all cocktails are half price.", ["cocktail", "happy", "half"], "mời khách ở quầy bar"),
  ("The guest at table four has had a lot to drink. Please don't serve him any more alcohol. Bring him some water and call a taxi.", ["four", "alcohol", "water"], "dặn đồng nghiệp ở quầy bar"),
 ],
})

# ───────────────────────── 15. Tiệc, hội nghị & sự kiện ─────────────────────────
PHASES.append({
 "title": "Tiệc, hội nghị & sự kiện",
 "vocab": [
  ("banquet", "/ˈbæŋkwɪt/", "n", "tiệc lớn (tiệc chiêu đãi, tiệc cưới)", "The <b>banquet</b> hall can seat 300 guests.", "Sảnh tiệc có thể xếp chỗ cho 300 khách.", "宴会", "enkai"),
  ("conference room", "/ˈkɒnfərəns ruːm/", "n", "phòng hội nghị, phòng họp", "The <b>conference room</b> is ready for your nine o'clock meeting.", "Phòng hội nghị đã sẵn sàng cho cuộc họp 9 giờ của anh/chị.", "会議室", "kaigishitsu"),
  ("projector", "/prəˈdʒektə/", "n", "máy chiếu", "The <b>projector</b> and screen are included in the price.", "Máy chiếu và màn chiếu đã gồm trong giá.", "プロジェクター", "purojekutā"),
  ("seating plan", "/ˈsiːtɪŋ plæn/", "n", "sơ đồ chỗ ngồi", "Could you send us the <b>seating plan</b> by Friday?", "Anh/chị gửi sơ đồ chỗ ngồi cho chúng tôi trước thứ Sáu nhé."),
  ("coffee break", "/ˈkɒfi breɪk/", "n", "giờ giải lao (tiệc trà giữa giờ)", "The <b>coffee break</b> is at 10:30, just outside the room.", "Giờ giải lao lúc 10 giờ 30, ngay bên ngoài phòng.", "コーヒーブレイク", "kōhī bureiku"),
  ("headcount", "/ˈhedkaʊnt/", "n", "số lượng khách (để chốt suất)", "We need the final <b>headcount</b> three days before the event.", "Chúng tôi cần chốt số lượng khách ba ngày trước sự kiện."),
  ("attendee", "/əˌtenˈdiː/", "n", "người tham dự", "Each <b>attendee</b> gets a name badge at the door.", "Mỗi người tham dự được phát thẻ tên ở cửa."),
  ("microphone", "/ˈmaɪkrəfəʊn/", "n", "micrô", "We'll put a wireless <b>microphone</b> on the stage.", "Chúng tôi sẽ đặt một micrô không dây trên sân khấu.", "マイク", "maiku"),
  ("venue", "/ˈvenjuː/", "n", "địa điểm tổ chức", "The garden is a beautiful <b>venue</b> for a wedding.", "Khu vườn là địa điểm tổ chức tiệc cưới rất đẹp.", "会場", "kaijō"),
  ("registration desk", "/ˌredʒɪˈstreɪʃn desk/", "n", "bàn đón tiếp, bàn đăng ký", "The <b>registration desk</b> opens at 8 a.m.", "Bàn đăng ký mở lúc 8 giờ sáng.", "受付", "uketsuke"),
 ],
 "phrases": [
  ("How many guests are you expecting?", "Anh/chị dự kiến bao nhiêu khách ạ?"),
  ("Would you like a theatre or a classroom layout?", "Anh/chị muốn xếp ghế kiểu rạp hát hay kiểu lớp học ạ?"),
  ("The package includes a projector, two microphones and water.", "Gói này gồm máy chiếu, hai micrô và nước uống."),
  ("We need the final headcount by Wednesday.", "Chúng tôi cần chốt số lượng khách trước thứ Tư."),
  ("Coffee breaks will be at 10:30 and 3 p.m.", "Tiệc trà giữa giờ sẽ vào lúc 10 giờ 30 và 3 giờ chiều."),
  ("Let me show you the banquet hall.", "Để tôi dẫn anh/chị đi xem sảnh tiệc."),
  ("Our technician will test the sound before you start.", "Kỹ thuật viên sẽ kiểm tra âm thanh trước khi anh/chị bắt đầu."),
  ("We'll need a 30 percent deposit to confirm the date.", "Chúng tôi cần đặt cọc 30% để giữ ngày."),
  ("The registration desk will be right outside the ballroom.", "Bàn đăng ký sẽ đặt ngay bên ngoài phòng tiệc lớn."),
  ("Is there anything else you need for tomorrow's event?", "Anh/chị có cần gì thêm cho sự kiện ngày mai không ạ?"),
 ],
 "dialogues": [
  ("We're planning a conference for 80 people next month.", [
    ("Great. Which dates are you thinking of, and do you need rooms for the attendees too?", True, "Hỏi ngày + gợi ý thêm phòng nghỉ cho khách dự."),
    ("80 people is OK, have room.", False, "Thiếu chủ ngữ ('We have a room for 80') và chưa hỏi ngày."),
    ("Conference is expensive, you know?", False, "Nói giá kiểu doạ khách, không hỏi thông tin cần thiết."),
  ]),
  ("The projector isn't working, and I'm speaking in ten minutes!", [
    ("I'm so sorry. I'll call our technician right now and bring a spare projector just in case.", True, "Xin lỗi + gọi kỹ thuật + có phương án dự phòng."),
    ("Maybe you connect wrong cable.", False, "Đổ lỗi cho khách lúc đang gấp, sai thì và thiếu 'the'."),
    ("Wait, technician coming.", False, "Thiếu 'is' và không nói bao lâu — khách đang rất gấp."),
  ]),
  ("Can we change the headcount from 120 to 135?", [
    ("Yes, that's fine. Could you confirm it by email today, please? The kitchen needs it for the menu.", True, "Đồng ý + xin xác nhận bằng văn bản + nêu lý do."),
    ("OK, 135. No problem.", False, "Chỉ nói miệng — đổi số suất nên có email xác nhận."),
    ("Too late, cannot change.", False, "Thiếu chủ ngữ, chưa kiểm tra đã từ chối."),
  ]),
  ("Where should the attendees go when they arrive?", [
    ("The registration desk is right outside the ballroom on the second floor. We'll put signs in the lobby.", True, "Vị trí cụ thể + có biển chỉ dẫn."),
    ("They go second floor.", False, "Thiếu 'to the' và chưa nói chỗ đăng ký."),
    ("Anywhere is OK.", False, "Không hướng dẫn gì, khách sẽ bị lạc."),
  ]),
  ("Some of our guests are vegetarian. Is that a problem?", [
    ("Not at all. How many vegetarian guests will there be? We'll prepare a separate menu for them.", True, "Trấn an + hỏi số lượng + phương án cụ thể."),
    ("Vegetarian eat salad.", False, "Thiếu mạo từ, qua loa — nên chuẩn bị thực đơn chay riêng."),
    ("No problem, no problem.", False, "Chỉ nói suông, chưa hỏi số lượng để chuẩn bị."),
  ]),
 ],
 "listen": [
  ("We need the final headcount by Friday", ["final", "headcount"], "chốt số khách"),
  ("The coffee break starts at ten thirty", ["coffee", "thirty"], "giờ giải lao"),
  ("The projector is ready in the conference room", ["projector", "conference"], "máy chiếu"),
  ("The banquet hall can seat three hundred guests", ["banquet", "hundred"], "sức chứa sảnh tiệc"),
  ("Good morning, team. The registration desk opens at eight. Please give each attendee a name badge and a bottle of water.", ["registration", "badge", "water"], "dặn việc trước hội nghị"),
  ("The speaker needs two microphones on the stage. Please test the sound at seven. Lunch for all guests is at twelve in the garden.", ["microphones", "sound", "garden"], "chuẩn bị sự kiện"),
 ],
})

# ───────────────────────── 16. Phục vụ tại phòng & minibar ─────────────────────────
PHASES.append({
 "title": "Phục vụ tại phòng & minibar",
 "vocab": [
  ("room service", "/ˈruːm ˌsɜːvɪs/", "n", "dịch vụ ăn uống tại phòng", "<b>Room service</b> is available 24 hours a day.", "Dịch vụ ăn uống tại phòng phục vụ 24/24.", "ルームサービス", "rūmu sābisu"),
  ("in-room dining", "/ˌɪn ruːm ˈdaɪnɪŋ/", "n", "ăn uống tại phòng (tên gọi khác của room service)", "Please press 6 for <b>in-room dining</b>.", "Anh/chị bấm số 6 để gọi đồ ăn lên phòng."),
  ("tray", "/treɪ/", "n", "cái khay", "Please leave the <b>tray</b> outside your door when you finish.", "Dùng xong anh/chị để khay ra ngoài cửa giúp nhé.", "トレー", "torē"),
  ("cutlery", "/ˈkʌtləri/", "n", "bộ dao, dĩa, thìa", "I'm sorry. I'll bring the <b>cutlery</b> right away.", "Xin lỗi anh/chị. Tôi sẽ mang dao dĩa lên ngay.", "カトラリー", "katorarī"),
  ("restock", "/ˌriːˈstɒk/", "v", "bổ sung lại (hàng, đồ uống)", "We <b>restock</b> the minibar every morning.", "Chúng tôi bổ sung minibar mỗi sáng.", "補充する", "hojū suru"),
  ("kettle", "/ˈketl/", "n", "ấm đun nước", "There's a <b>kettle</b> and some tea bags on the desk.", "Trên bàn có ấm đun nước và mấy gói trà."),
  ("snack", "/snæk/", "n", "đồ ăn vặt, đồ ăn nhẹ", "The <b>snacks</b> in the minibar are not free.", "Đồ ăn vặt trong minibar không miễn phí."),
  ("bottled water", "/ˌbɒtld ˈwɔːtə/", "n", "nước đóng chai", "Please drink <b>bottled water</b>, not tap water.", "Anh/chị nên uống nước đóng chai, đừng uống nước máy."),
  ("surcharge", "/ˈsɜːtʃɑːdʒ/", "n", "phụ phí", "There's a 50,000 dong <b>surcharge</b> for orders after 11 p.m.", "Gọi món sau 11 giờ đêm có phụ phí 50.000 đồng."),
  ("napkin", "/ˈnæpkɪn/", "n", "khăn ăn", "Could you bring some extra <b>napkins</b>, please?", "Anh/chị mang thêm khăn ăn giúp tôi được không?", "ナプキン", "napukin"),
 ],
 "phrases": [
  ("Room service. How may I help you?", "Bộ phận phục vụ tại phòng xin nghe. Tôi có thể giúp gì ạ?"),
  ("Could I have your room number, please?", "Cho tôi xin số phòng ạ."),
  ("Your order will arrive in about 30 minutes.", "Món của anh/chị sẽ được mang lên trong khoảng 30 phút."),
  ("Just to confirm, that's one club sandwich and a pot of tea.", "Tôi xin nhắc lại: một bánh mì kẹp club và một ấm trà ạ."),
  ("There's a small surcharge for orders after 11 p.m.", "Gọi món sau 11 giờ đêm có phụ phí nhỏ ạ."),
  ("Where would you like me to put the tray?", "Anh/chị muốn tôi đặt khay ở đâu ạ?"),
  ("Could you sign here, please? It'll be charged to your room.", "Anh/chị ký vào đây giúp tôi. Khoản này sẽ tính vào tiền phòng ạ."),
  ("When you finish, just call us and we'll collect the tray.", "Dùng xong anh/chị gọi, chúng tôi sẽ lên lấy khay ạ."),
  ("The water on the desk is free, but the minibar drinks are not.", "Nước trên bàn miễn phí, còn đồ uống trong minibar thì tính tiền."),
  ("I'm here to restock your minibar. It'll only take a minute.", "Tôi đến bổ sung minibar. Chỉ mất một phút thôi ạ."),
 ],
 "dialogues": [
  ("Hi, I'd like to order some food to my room.", [
    ("Of course. May I have your room number, please? And what would you like to order?", True, "Xin số phòng + hỏi món."),
    ("OK, you want eat what?", False, "Dịch từng chữ, sai trật tự: 'What would you like to order?'"),
    ("Kitchen close already.", False, "Sai thì, cộc — nếu bếp đã đóng cũng phải xin lỗi và đưa phương án."),
  ]),
  ("How long will it take?", [
    ("About 30 minutes. I'll call you if there's any delay.", True, "Thời gian cụ thể + hứa báo nếu bị trễ."),
    ("Fast, fast.", False, "Lặp từ kiểu tiếng Việt, không có con số."),
    ("It depend on the kitchen.", False, "Thiếu 's' ('depends') và không cho khách con số nào."),
  ]),
  ("There's no knife or fork on the tray.", [
    ("I'm so sorry. I'll bring the cutlery right away.", True, "Xin lỗi + mang lên ngay."),
    ("You can eat with chopsticks.", False, "Bắt khách tự xoay xở — lỗi của mình thì phải sửa ngay."),
    ("Sorry, I forget.", False, "Sai thì: 'I forgot' — và chưa nói sẽ mang lên."),
  ]),
  ("Why is there a surcharge on my bill?", [
    ("That's the late-night surcharge for orders after 11 p.m. It's on the menu. Would you like me to show you?", True, "Giải thích + chỉ căn cứ + đề nghị cho khách xem."),
    ("Because late.", False, "Thiếu chủ ngữ và động từ: 'Because you ordered after 11 p.m.'"),
    ("All hotels have it.", False, "Không giải thích khoản phí của chính khách sạn mình."),
  ]),
  ("I didn't drink anything from the minibar, but it's on my bill.", [
    ("I'm sorry about that. Let me ask housekeeping to check, and I'll remove it if it's a mistake.", True, "Xin lỗi + kiểm tra + cam kết xoá nếu sai."),
    ("The list says you drank it, so you did.", False, "Cãi khách dựa vào giấy tờ, không kiểm tra lại."),
    ("OK, I delete, no problem.", False, "Thiếu 'will', nên dùng 'remove' thay cho 'delete', lại xoá khi chưa kiểm tra."),
  ]),
 ],
 "listen": [
  ("Room service is open twenty-four hours", ["service", "twenty-four"], "giờ phục vụ tại phòng"),
  ("Please leave the tray outside your door", ["tray", "door"], "để khay ngoài cửa"),
  ("Your order will arrive in thirty minutes", ["order", "thirty"], "thời gian mang món lên"),
  ("I'm here to restock your minibar", ["restock", "minibar"], "bổ sung minibar"),
  ("Good evening, room 608. That's one chicken curry and two bottles of water. There's a small surcharge after eleven, and the food will be there in twenty minutes.", ["curry", "surcharge", "twenty"], "xác nhận món gọi lên phòng"),
  ("Here is your dinner, sir. Where would you like the tray? Please call us when you finish.", ["dinner", "tray", "finish"], "mang món lên phòng"),
 ],
})

# ───────────────────────── 17. Đánh giá online & khách quay lại ─────────────────────────
PHASES.append({
 "title": "Đánh giá online & khách quay lại",
 "vocab": [
  ("review", "/rɪˈvjuː/", "n", "bài đánh giá (của khách)", "The guest wrote a great <b>review</b> about our staff.", "Vị khách viết một bài đánh giá rất tốt về nhân viên mình.", "口コミ", "kuchikomi"),
  ("rating", "/ˈreɪtɪŋ/", "n", "điểm đánh giá, số sao", "Our <b>rating</b> went up to 9.1 this month.", "Tháng này điểm đánh giá của khách sạn lên 9,1.", "評価", "hyōka"),
  ("feedback", "/ˈfiːdbæk/", "n", "ý kiến phản hồi, góp ý", "Thank you for your <b>feedback</b>. We'll share it with the team.", "Cảm ơn góp ý của anh/chị. Chúng tôi sẽ chia sẻ với cả đội.", "フィードバック", "fīdobakku"),
  ("repeat guest", "/rɪˌpiːt ˈɡest/", "n", "khách quay lại, khách quen", "Mr. Tanaka is a <b>repeat guest</b>. It's his fifth stay.", "Ông Tanaka là khách quen. Đây là lần thứ năm ông ở đây.", "リピーター", "ripītā"),
  ("loyalty programme", "/ˈlɔɪəlti ˌprəʊɡræm/", "n", "chương trình khách hàng thân thiết", "Members of our <b>loyalty programme</b> get a free late check-out.", "Thành viên chương trình khách hàng thân thiết được trả phòng muộn miễn phí."),
  ("guest satisfaction", "/ˌɡest ˌsætɪsˈfækʃn/", "n", "mức độ hài lòng của khách", "<b>Guest satisfaction</b> is our number one goal.", "Sự hài lòng của khách là mục tiêu số một của chúng tôi."),
  ("respond", "/rɪˈspɒnd/", "v", "phản hồi, trả lời", "We <b>respond</b> to every online review within 24 hours.", "Chúng tôi trả lời mọi đánh giá online trong vòng 24 giờ."),
  ("exceed", "/ɪkˈsiːd/", "v", "vượt quá (mong đợi)", "The service <b>exceeded</b> our expectations.", "Dịch vụ vượt ngoài mong đợi của chúng tôi."),
  ("personalised", "/ˈpɜːsənəlaɪzd/", "adj", "dành riêng cho từng khách", "We left a <b>personalised</b> welcome card in her room.", "Chúng tôi để trong phòng chị ấy một tấm thiệp chào mừng ghi riêng tên chị."),
  ("survey", "/ˈsɜːveɪ/", "n", "phiếu khảo sát", "Could you spend two minutes on our guest <b>survey</b>?", "Anh/chị dành hai phút làm phiếu khảo sát giúp chúng tôi được không?", "アンケート", "ankēto"),
 ],
 "phrases": [
  ("Welcome back, Mr. Tanaka! It's great to see you again.", "Chào mừng ông Tanaka quay lại! Rất vui được gặp lại ông."),
  ("Would you like the same room as last time?", "Ông có muốn ở phòng giống lần trước không ạ?"),
  ("We remember you like a quiet room on a high floor.", "Chúng tôi nhớ ông thích phòng yên tĩnh ở tầng cao."),
  ("How was everything during your stay?", "Mọi thứ trong thời gian anh/chị ở đây thế nào ạ?"),
  ("If you enjoyed your stay, we'd love a review online.", "Nếu anh/chị hài lòng, chúng tôi rất mong được anh/chị đánh giá online."),
  ("Thank you for your feedback. I'll pass it on to our manager.", "Cảm ơn góp ý của anh/chị. Tôi sẽ chuyển lại cho quản lý."),
  ("As a member, you get a free upgrade when rooms are available.", "Là thành viên, anh/chị được nâng hạng phòng miễn phí khi còn phòng."),
  ("We're sorry your stay wasn't perfect. What could we do better?", "Chúng tôi rất tiếc kỳ nghỉ chưa được trọn vẹn. Chúng tôi nên cải thiện điều gì ạ?"),
  ("We reply to every review, good or bad.", "Chúng tôi trả lời mọi bài đánh giá, dù khen hay chê."),
  ("We hope to welcome you back soon.", "Hy vọng sớm được đón anh/chị quay lại."),
 ],
 "dialogues": [
  ("Hello again! I stayed here last year.", [
    ("Welcome back! It's lovely to see you again. Would you like the same room with the garden view?", True, "Chào mừng quay lại + nhớ sở thích của khách."),
    ("Oh, I don't remember you.", False, "Thật thà quá mức làm khách cụt hứng — nên chào đón nồng nhiệt."),
    ("Yes, last year you come.", False, "Sai thì: 'You stayed with us last year' — và chưa chào đón."),
  ]),
  ("The room was nice, but breakfast was a bit disappointing.", [
    ("Thank you for telling us. What didn't you like about it? I'll pass your feedback on to the chef.", True, "Cảm ơn + hỏi cụ thể + chuyển góp ý."),
    ("Breakfast is same every hotel.", False, "Thiếu 'the' và bào chữa, không nhận góp ý."),
    ("Other guests say it's delicious.", False, "Phủ nhận cảm nhận của khách."),
  ]),
  ("Do you have a loyalty programme?", [
    ("Yes, we do. It's free to join, and members get 10 percent off and a late check-out. Shall I sign you up?", True, "Trả lời + nêu quyền lợi + mời đăng ký."),
    ("Yes, have. Free.", False, "Thiếu chủ ngữ, quá cụt — nên nói quyền lợi."),
    ("Loyalty programme is for VIP only.", False, "Nói sai và làm khách mất hứng."),
  ]),
  ("A guest gave us one star online and said the room was dirty. What should we do?", [
    ("Let's reply politely today, say sorry, and ask housekeeping to check what happened.", True, "Trả lời lịch sự, sớm + xin lỗi + tìm nguyên nhân."),
    ("Just delete it. Nobody will see.", False, "Không xoá được và thiếu trung thực — phải phản hồi công khai."),
    ("We write he is lying.", False, "Sai thì ('We'll say he's lying') và cãi khách công khai rất phản tác dụng."),
  ]),
  ("I had a wonderful stay. Everyone was so kind!", [
    ("Thank you so much! If you have time, we'd love it if you could write a short review online.", True, "Cảm ơn + khéo léo mời viết đánh giá."),
    ("You must write five stars for us.", False, "Ép khách chấm điểm — không được làm vậy."),
    ("Yes, we are very kind.", False, "Nhận lời khen thiếu khiêm tốn, bỏ lỡ lời mời đánh giá."),
  ]),
 ],
 "listen": [
  ("Welcome back, it's great to see you again", ["back", "again"], "chào khách quen"),
  ("Thank you for your feedback", ["Thank", "feedback"], "cảm ơn góp ý"),
  ("We reply to every review within a day", ["reply", "review"], "phản hồi đánh giá"),
  ("Our rating went up to nine this month", ["rating", "month"], "điểm đánh giá"),
  ("Mr. Tanaka is a repeat guest. He likes a quiet room on a high floor. Please put a welcome card in his room.", ["repeat", "quiet", "card"], "chuẩn bị đón khách quen"),
  ("Thank you for staying with us. Before you go, could you fill in this short survey? It only takes two minutes.", ["staying", "survey", "minutes"], "mời khách làm khảo sát"),
 ],
})

# ───────────────────────── 18. An ninh, đồ thất lạc & khẩn cấp ─────────────────────────
PHASES.append({
 "title": "An ninh, đồ thất lạc & khẩn cấp",
 "vocab": [
  ("security", "/sɪˈkjʊərəti/", "n", "bộ phận an ninh; sự an ninh", "Please call <b>security</b> if you see anything strange.", "Nếu thấy điều gì bất thường, hãy gọi bộ phận an ninh.", "警備", "keibi"),
  ("CCTV", "/ˌsiː siː tiː ˈviː/", "n", "camera giám sát", "The <b>CCTV</b> shows he left the lobby at 9 p.m.", "Camera giám sát cho thấy anh ấy rời sảnh lúc 9 giờ tối.", "防犯カメラ", "bōhan kamera"),
  ("fire alarm", "/ˈfaɪər əˌlɑːm/", "n", "chuông báo cháy", "If the <b>fire alarm</b> rings, leave by the stairs.", "Nếu chuông báo cháy kêu, hãy thoát ra bằng cầu thang bộ.", "火災報知器", "kasai hōchiki"),
  ("emergency exit", "/ɪˈmɜːdʒənsi ˌeksɪt/", "n", "lối thoát hiểm", "The <b>emergency exit</b> is at the end of the corridor.", "Lối thoát hiểm ở cuối hành lang.", "非常口", "hijōguchi"),
  ("evacuate", "/ɪˈvækjueɪt/", "v", "sơ tán", "We need to <b>evacuate</b> the building now.", "Chúng ta cần sơ tán khỏi toà nhà ngay.", "避難する", "hinan suru"),
  ("assembly point", "/əˈsembli pɔɪnt/", "n", "điểm tập kết (khi sơ tán)", "The <b>assembly point</b> is the car park in front of the hotel.", "Điểm tập kết là bãi đỗ xe trước khách sạn."),
  ("first aid", "/ˌfɜːst ˈeɪd/", "n", "sơ cứu", "Two staff on every shift are trained in <b>first aid</b>.", "Mỗi ca có hai nhân viên được đào tạo sơ cứu.", "応急処置", "ōkyū shochi"),
  ("ambulance", "/ˈæmbjələns/", "n", "xe cứu thương", "I've called an <b>ambulance</b>. It'll be here in ten minutes.", "Tôi đã gọi xe cứu thương. Mười phút nữa xe sẽ tới.", "救急車", "kyūkyūsha"),
  ("belongings", "/bɪˈlɒŋɪŋz/", "n", "đồ đạc, tư trang", "Please don't leave your <b>belongings</b> by the pool.", "Anh/chị đừng để đồ đạc cá nhân ở cạnh hồ bơi nhé.", "所持品", "shojihin"),
  ("power cut", "/ˈpaʊə kʌt/", "n", "mất điện, cúp điện", "Sorry, there's a <b>power cut</b>. The generator will start in a minute.", "Xin lỗi, đang mất điện. Một phút nữa máy phát sẽ chạy.", "停電", "teiden"),
 ],
 "phrases": [
  ("Please stay calm and follow me to the emergency exit.", "Mọi người bình tĩnh và đi theo tôi đến lối thoát hiểm."),
  ("Please use the stairs. Don't use the lift.", "Vui lòng đi cầu thang bộ. Không dùng thang máy."),
  ("Please go to the assembly point in front of the hotel.", "Vui lòng đến điểm tập kết trước khách sạn."),
  ("Is anyone hurt?", "Có ai bị thương không?"),
  ("I'll call an ambulance right now.", "Tôi sẽ gọi xe cứu thương ngay."),
  ("Our first aider is on the way.", "Nhân viên sơ cứu đang tới."),
  ("Could you describe the bag? What colour is it?", "Anh/chị mô tả chiếc túi giúp tôi. Nó màu gì ạ?"),
  ("We'll check the CCTV and call you back within an hour.", "Chúng tôi sẽ kiểm tra camera và gọi lại cho anh/chị trong vòng một giờ."),
  ("If you need a police report for your insurance, I can help you.", "Nếu anh/chị cần biên bản của công an để làm bảo hiểm, tôi có thể hỗ trợ."),
  ("For your safety, please don't open the door to strangers.", "Vì an toàn, anh/chị đừng mở cửa cho người lạ."),
 ],
 "dialogues": [
  ("I can't find my wallet. I think someone took it from my room!", [
    ("I'm sorry to hear that. Let's check your room together first, and then I'll call our security manager.", True, "Cảm thông + cùng khách kiểm tra + báo an ninh — không kết luận vội."),
    ("Our staff never steal.", False, "Phủ nhận ngay khiến khách nghĩ khách sạn bao che."),
    ("Maybe you lose it outside.", False, "Sai thì ('lost') và đổ cho khách khi chưa kiểm tra."),
  ]),
  ("What's that noise? Is it the fire alarm?", [
    ("Yes, it is. Please leave your room now, take the stairs and go to the assembly point in front of the hotel.", True, "Xác nhận + hướng dẫn rõ: rời phòng, đi thang bộ, đến điểm tập kết."),
    ("Don't worry, it's probably nothing. Stay in your room.", False, "Rất nguy hiểm — chuông báo cháy kêu là phải sơ tán theo quy trình."),
    ("Yes, fire. Run, run!", False, "Gây hoảng loạn, không chỉ hướng — cần bình tĩnh và nói rõ lối thoát."),
  ]),
  ("My husband fell by the pool and hurt his head.", [
    ("I'm sending our first aider now. Please don't move him. I'll call an ambulance too.", True, "Cử người sơ cứu + dặn không di chuyển + chủ động gọi cấp cứu (chấn thương đầu không nên chờ)."),
    ("Please take him to his room.", False, "Nguy hiểm — chấn thương đầu thì không nên tự di chuyển người bị nạn."),
    ("Pool floor is wet, you must careful.", False, "Trách khách lúc khẩn cấp, thiếu 'be' ('must be careful')."),
  ]),
  ("Why is everything dark? Is it a power cut?", [
    ("Yes, I'm sorry. The generator will start in a minute. Please stay where you are, and I'll bring you a torch.", True, "Xác nhận + thời gian + dặn an toàn + hỗ trợ."),
    ("Electric is die.", False, "Dịch từng chữ 'điện chết' — nói 'There's a power cut.'"),
    ("I don't know. Wait.", False, "Không trấn an, không có thông tin."),
  ]),
  ("I left my laptop in the taxi from the airport.", [
    ("Oh no. Do you have the receipt, or do you remember the taxi company? I'll call them for you right away.", True, "Cảm thông + hỏi thông tin để tìm + gọi giúp ngay."),
    ("Taxi is gone, cannot find.", False, "Bỏ cuộc ngay, thiếu chủ ngữ — nên hỏi hoá đơn/hãng xe để tìm."),
    ("Why you don't check before?", False, "Sai thì và trật tự ('Why didn't you check?') — lại trách khách."),
  ]),
 ],
 "listen": [
  ("Please use the stairs, not the lift", ["stairs", "lift"], "thoát hiểm bằng thang bộ"),
  ("The emergency exit is at the end of the corridor", ["emergency", "corridor"], "lối thoát hiểm"),
  ("I'll call an ambulance right now", ["ambulance", "now"], "gọi cấp cứu"),
  ("We will check the CCTV this afternoon", ["check", "CCTV"], "kiểm tra camera"),
  ("Attention, please. This is not a drill. Please leave the building by the stairs and go to the assembly point in the car park.", ["drill", "stairs", "assembly"], "thông báo sơ tán"),
  ("A guest lost a black backpack in the lobby this morning. Please check the cameras. Call me if you find anything.", ["backpack", "cameras", "find"], "báo đồ thất lạc cho an ninh"),
 ],
})

EXTRA = {
 "phases": PHASES,
 "rev": [
  ("Tôi đã đặt bàn lúc bảy giờ cho anh/chị.", "I've booked a table for you at seven."),
  ("Tài xế sẽ đợi anh/chị ở sảnh đến.", "The driver will wait for you in the arrivals hall."),
  ("Chuyến bay của anh/chị số hiệu gì ạ?", "What's your flight number?"),
  ("Giờ này đường hay kẹt, anh/chị nên đi sớm.", "The traffic is usually bad now, so please leave early."),
  ("Anh/chị muốn mát-xa 60 hay 90 phút?", "Would you like a 60- or 90-minute massage?"),
  ("Lực như vậy được chưa ạ?", "Is the pressure OK?"),
  ("Hồ bơi mở cửa đến tám giờ tối.", "The pool is open until 8 p.m."),
  ("Đang giờ vàng, cốc-tai giảm nửa giá.", "It's happy hour, so cocktails are half price."),
  ("Anh/chị uống với đá không ạ?", "Would you like it with ice?"),
  ("Chúng tôi cần chốt số khách trước thứ Sáu.", "We need the final headcount by Friday."),
  ("Máy chiếu đã sẵn sàng trong phòng họp.", "The projector is ready in the meeting room."),
  ("Món của anh/chị sẽ lên phòng trong 30 phút.", "Your order will be up in 30 minutes."),
  ("Dùng xong anh/chị để khay ngoài cửa nhé.", "Please leave the tray outside the door when you finish."),
  ("Chào mừng anh/chị quay lại!", "Welcome back!"),
  ("Cảm ơn góp ý của anh/chị.", "Thank you for your feedback."),
  ("Vui lòng đi cầu thang bộ, không dùng thang máy.", "Please use the stairs, not the lift."),
 ],
 "reading": [
  {"t": "Concierge booking", "text": "CONCIERGE – BOOKING CONFIRMATION\nGuest: Ms. Laura Diaz, Room 604\nService: Vietnamese cooking class (2 people)\nDate: Thursday, 8:00 a.m. – 1:00 p.m.\nPick-up: hotel lobby, 7:45 a.m.\nPrice: 900,000 VND per person, charged to the room\nFree cancellation until Wednesday, 6 p.m.", "q": [
    {"q": "When should the guests be in the lobby?", "o": ["At 7:45 a.m.", "At 8:00 a.m.", "At 1:00 p.m."], "a": 0},
    {"q": "How will Ms. Diaz pay?", "o": ["In cash to the teacher", "It will be added to her room bill", "By card at the class"], "a": 1}]},
  {"t": "Pick-up message", "text": "Hi Ms. Park, this is Hoa Sen Hotel. Your driver, Mr. Tuấn, will meet you tomorrow in the arrivals hall after baggage claim. He will hold a sign with your name. Car: white seven-seater. If your flight is delayed, don't worry — we track all flight times. See you soon!", "q": [
    {"q": "Where will the driver meet Ms. Park?", "o": ["Outside the hotel", "In the arrivals hall", "At the check-in counter"], "a": 1},
    {"q": "What should Ms. Park do if her flight is late?", "o": ["Call the hotel to cancel", "Take a taxi", "Nothing — the hotel checks the flight"], "a": 2}]},
  {"t": "Spa price list", "text": "LOTUS SPA – PRICE LIST (VND)\nFoot massage, 45 min: 350,000\nVietnamese massage, 60 min: 550,000\nHot stone massage, 90 min: 850,000\n• Hotel guests: 15% off all treatments before 3 p.m.\n• Please book at least 2 hours in advance.\n• Pregnant guests: please tell our staff when booking.", "q": [
    {"q": "Which treatment is the longest?", "o": ["Foot massage", "Vietnamese massage", "Hot stone massage"], "a": 2},
    {"q": "How can hotel guests get 15% off?", "o": ["Book two treatments", "Have a treatment before 3 p.m.", "Book two hours in advance"], "a": 1}]},
  {"t": "Event order", "text": "EVENT ORDER #218\nClient: Green Valley Travel\nRoom: Lotus Ballroom, classroom layout\nDate: Tuesday, May 14, 8:30 a.m. – 5:00 p.m.\nGuests: 120 (final headcount due Friday, May 10)\nCoffee breaks: 10:15 a.m. and 3:00 p.m.\nLunch: buffet at 12:00, incl. 10 vegetarian meals\nAV: 1 projector, 2 wireless microphones", "q": [
    {"q": "When must the client confirm the number of guests?", "o": ["Friday, May 10", "Tuesday, May 14", "At 8:30 a.m. on the day"], "a": 0},
    {"q": "How many vegetarian meals are needed?", "o": ["Two", "Ten", "One hundred and twenty"], "a": 1}]},
  {"t": "Online review", "text": "★★★☆☆ Great location, slow room service\nThe room was clean and the staff were friendly. But our room service dinner took over an hour and arrived cold.\n\nReply from the hotel:\nDear guest, thank you for your feedback. We're very sorry about your dinner. We have spoken to our kitchen team, and we hope to welcome you back soon.", "q": [
    {"q": "What did the guest NOT like?", "o": ["The location", "The room service", "The staff"], "a": 1},
    {"q": "What did the hotel do?", "o": ["It talked to the kitchen team", "It gave a full refund", "It deleted the review"], "a": 0}]},
 ],
 "ai": [
  ("concierge", "Nhờ đặt dịch vụ", "You are a hotel guest at the concierge desk. Ask me to book a dinner table for tonight and two tickets for a local show. Ask about the dress code and the prices."),
  ("pickup", "Đón sân bay", "You are a guest calling the hotel from the airport. Your flight was delayed and you can't find the driver. Tell me where you are and ask what to do."),
  ("spa", "Đặt lịch spa", "You are a hotel guest who wants a massage today. Ask about the treatments, the prices, the free times and whether there is a discount for hotel guests."),
  ("roomservice", "Gọi đồ ăn lên phòng", "You are a guest ordering room service late at night. Ask what is available, how long it takes and whether there is a surcharge, then place your order."),
 ],
 "events": [
  ("conference", "Hội nghị công ty ở khách sạn", "You are an event organiser holding a one-day conference for 100 people at our hotel next week. Ask me about the room layout, the coffee breaks, the projector and lunch."),
  ("firedrill", "Diễn tập phòng cháy chữa cháy", "You are the hotel safety manager running a fire drill tomorrow. Ask me what I will say to guests, which exit I will use and where the assembly point is."),
  ("gala", "Tiệc tất niên (gala dinner)", "You are the manager of a foreign company booking a year-end gala dinner for 150 staff at our hotel. Ask about the banquet hall, the menu, the drinks and the stage."),
 ],
 "quips": [
  "Concierge magic: booked!",
  "Your driver is here!",
  "Relax… massage time!",
  "Happy hour, happy Mochi!",
  "Room service, knock knock!",
  "Welcome back, old friend!",
 ],
 "roles": {
  "reception": {
   "scenarios": [
    ("rc_upsell", "Mời nâng hạng phòng", "You are a guest checking in to a standard room. I will offer you an upgrade to a sea-view room. Ask about the price and the difference, then decide."),
    ("rc_repeat", "Đón khách quen", "You are a repeat guest on your fourth stay. Check in, mention what you liked last time and ask about the loyalty programme."),
   ],
   "dialogues": [
    ("Can I leave my passport with you? I don't trust the room safe.", [
      ("Of course. We can keep it in a safety deposit box at the front desk, and I'll give you a receipt.", True, "Đồng ý + nói rõ nơi cất + đưa biên nhận."),
      ("The safe is OK, you use it.", False, "Gạt đi lo lắng của khách, nghe như ra lệnh."),
      ("OK, I keep in drawer.", False, "Thiếu 'will' và tân ngữ — cất hộ chiếu trong ngăn kéo cũng không an toàn.")]),
    ("Someone knocked on my door and said he was from the hotel. I didn't call anyone.", [
      ("Thank you for telling me. Please don't open the door. I'll send security to your floor right now.", True, "Cảm ơn + dặn không mở cửa + cử an ninh lên ngay."),
      ("Maybe it's housekeeping, don't worry.", False, "Chủ quan — phải kiểm tra ngay vì an toàn của khách."),
      ("Who is he? I don't know.", False, "Không giúp khách, không có hành động gì.")]),
    ("I'd like to stay two more nights.", [
      ("Certainly. Let me check... Yes, your room is available. The rate is the same, 1.3 million dong per night.", True, "Kiểm tra + xác nhận + báo giá."),
      ("Yes, you can stay more.", False, "Hứa khi chưa kiểm tra phòng, không báo giá."),
      ("Two more night OK.", False, "Thiếu 's' số nhiều và động từ; chưa kiểm tra phòng.")]),
    ("Can you recommend a good place to watch the sunset?", [
      ("Yes, the rooftop bar on our tenth floor has a great view. Sunset is at about 5:45.", True, "Gợi ý cụ thể + giờ hoàng hôn."),
      ("Sunset is everywhere.", False, "Trả lời vô ích, không giúp được khách."),
      ("You go up, very nice.", False, "Mơ hồ — 'lên đâu?' — thiếu thông tin cụ thể.")]),
   ]},
  "fnb": {
   "scenarios": [
    ("fb_wine", "Tư vấn rượu vang", "You are a guest having dinner who knows little about wine. Ask me to suggest a wine for grilled fish and ask if you can order it by the glass."),
    ("fb_event", "Phục vụ tiệc cưới", "You are a guest at a wedding banquet in the hotel. Ask me for a vegetarian dish, more ice and where the toilets are."),
   ],
   "dialogues": [
    ("Could you recommend a wine for the grilled fish?", [
      ("I'd suggest a white wine. Our house white is light and goes well with fish.", True, "Gợi ý cụ thể + lý do ngắn gọn."),
      ("Red or white, same.", False, "Sai về chuyên môn và thiếu động từ."),
      ("All wine is good.", False, "Không giúp khách chọn.")]),
    ("This coffee is cold.", [
      ("I'm so sorry. I'll bring you a fresh, hot one right away.", True, "Xin lỗi + thay ly mới ngay."),
      ("You drink slow, so it cold.", False, "Đổ lỗi cho khách, thiếu động từ 'is'."),
      ("Sorry, coffee machine old.", False, "Đổ cho máy, thiếu 'the' và 'is', không thay ly mới.")]),
    ("Do you have a high chair for my son?", [
      ("Yes, we do. I'll bring one to your table now.", True, "Xác nhận + mang ra ngay."),
      ("Yes, have high chair.", False, "Thiếu chủ ngữ: 'Yes, we have one.'"),
      ("Your son can sit on your lap.", False, "Nhà hàng có ghế em bé thì phải mang ra, không bắt khách bế.")]),
    ("What time does the restaurant close?", [
      ("The kitchen closes at ten, and last orders are at half past nine.", True, "Giờ bếp đóng + giờ gọi món cuối."),
      ("Close late, no problem.", False, "Mơ hồ, thiếu chủ ngữ."),
      ("Restaurant close at 10.", False, "Thiếu 'The' và 's': 'The restaurant closes at 10.'")]),
   ]},
  "housekeeping": {
   "scenarios": [
    ("hk_found", "Báo khách đồ bỏ quên", "You are a guest who checked out this morning. I call you because housekeeping found your watch in the room. Ask how you can get it back before your flight."),
    ("hk_minibar", "Bổ sung minibar", "You are a guest in your room when I come to restock the minibar. Ask what is free, what the prices are and ask for more bottled water."),
   ],
   "dialogues": [
    ("Can you bring me a kettle? There isn't one in my room.", [
      ("I'm sorry about that. I'll bring one in five minutes, with some tea and coffee.", True, "Xin lỗi + thời gian + chu đáo thêm."),
      ("Kettle not have in this room.", False, "Dịch từng chữ: 'There's no kettle in this room' — và chưa đưa giải pháp."),
      ("You can drink cold water.", False, "Không đáp ứng yêu cầu hợp lý của khách.")]),
    ("I can smell smoke in the corridor.", [
      ("Thank you for telling me. I'll call security to check right now. If the fire alarm rings, please use the stairs.", True, "Cảm ơn + báo an ninh ngay + dặn an toàn."),
      ("Maybe someone smoking, not a problem.", False, "Chủ quan với mùi khói — phải báo kiểm tra ngay."),
      ("I don't smell anything.", False, "Phủ nhận thông tin khách báo.")]),
    ("The minibar is empty. There's no water.", [
      ("I'm sorry. I'll restock it now and bring you two extra bottles of water.", True, "Xin lỗi + bổ sung ngay + bù thêm."),
      ("Tomorrow morning we restock.", False, "Hẹn quá lâu, dịch từng chữ theo trật tự tiếng Việt."),
      ("Water in the minibar is not free.", False, "Lạc đề — khách đang báo thiếu nước.")]),
    ("I found a ring under the bed. It isn't mine.", [
      ("Thank you very much. I'll take it to lost and found and write down where it was found.", True, "Cảm ơn + nộp chỗ giữ đồ thất lạc + ghi lại."),
      ("OK, I keep it.", False, "Nghe như nhân viên giữ riêng — phải nộp chỗ giữ đồ thất lạc."),
      ("Throw it away.", False, "Sai quy trình — đồ thất lạc phải được lưu giữ.")]),
   ]},
  "guide": {
   "scenarios": [
    ("gd_lost", "Khách bị lạc đoàn", "You are a tourist who got separated from my tour group in a busy market. Call me, describe where you are and ask what to do."),
    ("gd_heat", "Khách mệt vì nắng nóng", "You are a tourist on a very hot day who feels dizzy and tired during a walking tour. Tell me how you feel and ask for help."),
   ],
   "dialogues": [
    ("I've lost the group! I'm near a big red gate.", [
      ("Please stay where you are. Don't worry, I'll come and find you in five minutes.", True, "Dặn đứng yên + trấn an + thời gian cụ thể."),
      ("You find the bus yourself.", False, "Bỏ mặc khách, nguy hiểm."),
      ("Why you not follow flag?", False, "Trách khách, sai ngữ pháp ('Why didn't you follow the flag?').")]),
    ("I feel dizzy. I think it's the heat.", [
      ("Please sit here in the shade and drink some water. I'll stay with you, and if you don't feel better, I'll call a doctor.", True, "Bóng mát + nước + ở cạnh khách + phương án gọi bác sĩ."),
      ("Just walk slowly, we're almost there.", False, "Bắt khách đi tiếp khi đang choáng — nguy hiểm."),
      ("Hot is normal in Vietnam.", False, "Coi nhẹ tình trạng của khách, thiếu chủ ngữ 'It'.")]),
    ("Is it safe to swim at this beach?", [
      ("Only in the area with the lifeguard. The waves are strong today, so please be careful.", True, "Chỉ khu có cứu hộ + cảnh báo sóng."),
      ("Yes, swim anywhere.", False, "Nguy hiểm, thiếu thông tin an toàn."),
      ("I think yes, maybe.", False, "Mơ hồ trong chuyện an toàn.")]),
    ("Can we visit the beach instead of the museum?", [
      ("Let me ask the group first. If everyone agrees, we can go to the beach after lunch.", True, "Hỏi ý cả đoàn + điều kiện + thời gian."),
      ("No, itinerary is itinerary.", False, "Cứng nhắc, thiếu mạo từ."),
      ("OK, I change now.", False, "Đổi ngay không hỏi cả đoàn, thiếu 'will'.")]),
   ]},
 },
}
