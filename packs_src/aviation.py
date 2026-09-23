# -*- coding: utf-8 -*-
# Gói "aviation" — Hàng không · Sân bay: quầy check-in, cửa ra máy bay, soi chiếu an ninh, tiếp viên,
# hỗ trợ đặc biệt, hành lý thất lạc. Hành khách đến từ nhiều nước. Chặng lõi lấy từ office: 10 (Nghỉ phép & hành chính),
# 11 (Phỏng vấn). Không nêu chính sách/phí/quy định thật của hãng nào — luôn nói chung ("according to our policy").
# Schema: xem packs_src/README.md. Build: python3 packs_src/build.py aviation

PHASES = []

# ───────────────────────── 1. Quầy check-in – làm thủ tục ─────────────────────────
PHASES.append({
 "title": "Quầy check-in – làm thủ tục",
 "vocab": [
  ("check-in counter", "/ˈtʃek ɪn ˌkaʊntə/", "n", "quầy làm thủ tục", "Please go to <b>check-in counter</b> 14.", "Anh/chị vui lòng đến quầy làm thủ tục số 14.", "チェックインカウンター", "chekkuin kauntā"),
  ("boarding pass", "/ˈbɔːdɪŋ pɑːs/", "n", "thẻ lên máy bay", "Here is your <b>boarding pass</b>. Your seat is 24A.", "Đây là thẻ lên máy bay của anh/chị. Ghế của anh/chị là 24A.", "搭乗券", "tōjōken"),
  ("booking reference", "/ˈbʊkɪŋ ˌrefrəns/", "n", "mã đặt chỗ", "Could you give me your <b>booking reference</b>, please?", "Anh/chị cho tôi xin mã đặt chỗ được không ạ?", "予約番号", "yoyaku bangō"),
  ("destination", "/ˌdestɪˈneɪʃn/", "n", "điểm đến", "What is your final <b>destination</b> today?", "Điểm đến cuối cùng của anh/chị hôm nay là đâu ạ?", "目的地", "mokutekichi"),
  ("visa", "/ˈviːzə/", "n", "thị thực, visa", "For this country, I need to see your <b>visa</b>.", "Với nước này, tôi cần xem thị thực của anh/chị.", "ビザ", "biza"),
  ("e-ticket", "/ˈiː tɪkɪt/", "n", "vé điện tử", "You don't need to print your <b>e-ticket</b>.", "Anh/chị không cần in vé điện tử.", "電子航空券", "denshi kōkūken"),
  ("self-service kiosk", "/ˌself ˈsɜːvɪs ˌkiːɒsk/", "n", "máy tự làm thủ tục", "You can print your boarding pass at the <b>self-service kiosk</b>.", "Anh/chị có thể in thẻ lên máy bay ở máy tự làm thủ tục.", "自動チェックイン機", "jidō chekkuin ki"),
  ("departure time", "/dɪˈpɑːtʃə taɪm/", "n", "giờ khởi hành", "The <b>departure time</b> is 10:50.", "Giờ khởi hành là 10 giờ 50.", "出発時刻", "shuppatsu jikoku"),
  ("return ticket", "/rɪˌtɜːn ˈtɪkɪt/", "n", "vé khứ hồi, vé chiều về", "Do you have a <b>return ticket</b>?", "Anh/chị có vé chiều về không ạ?", "往復航空券", "ōfuku kōkūken"),
  ("travel document", "/ˈtrævl ˌdɒkjumənt/", "n", "giấy tờ đi lại (hộ chiếu, thị thực…)", "Please keep your <b>travel documents</b> with you.", "Anh/chị vui lòng giữ giấy tờ đi lại bên mình."),
 ],
 "phrases": [
  ("Good morning. Where are you flying to today?", "Chào buổi sáng. Hôm nay anh/chị bay đi đâu ạ?"),
  ("May I see your passport and booking reference, please?", "Cho tôi xem hộ chiếu và mã đặt chỗ của anh/chị được không ạ?"),
  ("Are you checking in any bags today?", "Hôm nay anh/chị có ký gửi hành lý không ạ?"),
  ("Did you pack your bags yourself?", "Anh/chị có tự tay xếp hành lý không ạ?"),
  ("Here is your boarding pass. Your seat is 24A, by the window.", "Đây là thẻ lên máy bay. Ghế của anh/chị là 24A, cạnh cửa sổ."),
  ("Boarding starts at 9:15 at Gate 12.", "Bắt đầu lên máy bay lúc 9 giờ 15 ở cửa số 12."),
  ("Please be at the gate 30 minutes before departure.", "Anh/chị vui lòng có mặt ở cửa ra máy bay 30 phút trước giờ khởi hành."),
  ("For this destination, I need to see your visa, please.", "Với điểm đến này, tôi cần xem thị thực của anh/chị ạ."),
  ("Next time, you can also check in online or at the self-service kiosk.", "Lần sau anh/chị cũng có thể làm thủ tục trực tuyến hoặc ở máy tự làm thủ tục."),
  ("Have a nice flight!", "Chúc anh/chị có chuyến bay vui vẻ!"),
 ],
 "dialogues": [
  ("Hi, I'm flying to Tokyo. Here's my passport.", [
    ("Thank you, Ms. Tanaka. I can see your booking to Tokyo. Are you checking in any bags today?", True, "Cảm ơn + xác nhận đặt chỗ + hỏi hành lý ký gửi."),
    ("OK. Bag?", False, "Cộc lốc, chỉ một từ; nên hỏi đủ câu 'Are you checking in any bags?'"),
    ("You go Tokyo, yes?", False, "Thiếu động từ ('Are you going to…?') và hỏi lại điều khách vừa nói, không tiến hành thủ tục."),
  ]),
  ("What time does boarding start?", [
    ("Boarding starts at 10:20 at Gate 15. The gate closes at 10:40.", True, "Giờ lên máy bay + cửa số mấy + giờ đóng cửa."),
    ("Boarding 10:20.", False, "Thiếu động từ và thiếu số cửa: 'Boarding starts at 10:20 at Gate 15.'"),
    ("You look at the screen.", False, "Đẩy việc cho khách; khách hỏi thì nên trả lời giờ và cửa."),
  ]),
  ("I didn't print my ticket. Is that a problem?", [
    ("No problem at all. You have an e-ticket, so your passport is enough.", True, "Trấn an + giải thích ngắn vì sao không cần vé in."),
    ("No ticket, cannot fly.", False, "Sai và làm khách hoảng — vé điện tử chỉ cần hộ chiếu hoặc mã đặt chỗ."),
    ("Not problem.", False, "Sai cụm từ: 'No problem.' — và nên giải thích vì sao."),
  ]),
  ("Do I need a visa for this country?", [
    ("It depends on your nationality. Let me check the system... Yes, you need one. May I see your visa, please?", True, "Không đoán — kiểm tra hệ thống rồi mới trả lời và xin xem thị thực."),
    ("I think no need.", False, "Đoán mò chuyện giấy tờ — khách có thể bị từ chối nhập cảnh; phải kiểm tra."),
    ("Yes, need visa, you have?", False, "Thiếu chủ ngữ, câu hỏi cụt: 'You need a visa. Do you have it with you?'"),
  ]),
  ("The self-service kiosk isn't working. Can you help me?", [
    ("Of course. I can check you in here at the counter. May I see your passport, please?", True, "Nhận giúp ngay + xin giấy tờ để làm thủ tục."),
    ("Kiosk broken, you try again.", False, "Thiếu 'is', lại đẩy khách về máy đang hỏng."),
    ("Please wait, I busy.", False, "Thiếu 'am' ('I'm busy') và từ chối khách như vậy là thiếu chuyên nghiệp."),
  ]),
 ],
 "listen": [
  ("Where are you flying to today", ["flying", "today"], "hỏi điểm đến"),
  ("May I see your passport and booking reference", ["passport", "reference"], "xin giấy tờ"),
  ("Your seat is twenty-four A, by the window", ["seat", "window"], "báo số ghế"),
  ("Boarding starts at nine fifteen at Gate twelve", ["Boarding", "Gate"], "giờ và cửa lên máy bay"),
  ("Good morning. Here is your boarding pass. Boarding starts at ten twenty at Gate fifteen, and the gate closes at ten forty.", ["boarding", "fifteen", "closes"], "đưa thẻ lên máy bay"),
  ("Welcome to the check-in counter for the flight to Seoul. Please have your passport ready. You can also use the self-service kiosks on your left.", ["Seoul", "ready", "kiosks"], "hướng dẫn khách xếp hàng"),
 ],
})

# ───────────────────────── 2. Hành lý ký gửi & xách tay ─────────────────────────
PHASES.append({
 "title": "Hành lý ký gửi & xách tay",
 "vocab": [
  ("checked baggage", "/ˌtʃekt ˈbæɡɪdʒ/", "n", "hành lý ký gửi", "You have one piece of <b>checked baggage</b>.", "Anh/chị có một kiện hành lý ký gửi.", "受託手荷物", "jutaku tenimotsu"),
  ("carry-on", "/ˈkæri ɒn/", "n", "hành lý xách tay", "Your <b>carry-on</b> must fit under the seat or in the overhead bin.", "Hành lý xách tay phải để vừa dưới ghế hoặc trong hộc phía trên.", "機内持ち込み手荷物", "kinai mochikomi tenimotsu"),
  ("baggage allowance", "/ˈbæɡɪdʒ əˌlaʊəns/", "n", "hạn mức hành lý miễn cước", "Your <b>baggage allowance</b> is shown on your ticket.", "Hạn mức hành lý miễn cước của anh/chị ghi trên vé.", "無料手荷物許容量", "muryō tenimotsu kyoyōryō"),
  ("excess baggage", "/ˌekses ˈbæɡɪdʒ/", "n", "hành lý quá cước", "You need to pay for <b>excess baggage</b> at the ticket desk.", "Anh/chị cần trả phí hành lý quá cước ở quầy vé.", "超過手荷物", "chōka tenimotsu"),
  ("overweight", "/ˌəʊvəˈweɪt/", "adj", "quá cân", "I'm sorry, your bag is three kilos <b>overweight</b>.", "Xin lỗi, túi của anh/chị bị quá ba ký.", "重量超過", "jūryō chōka"),
  ("scale", "/skeɪl/", "n", "cái cân", "Could you put your bag on the <b>scale</b>, please?", "Anh/chị đặt túi lên cân giúp tôi nhé."),
  ("baggage tag", "/ˈbæɡɪdʒ tæɡ/", "n", "thẻ gắn hành lý", "I'll put a <b>baggage tag</b> on your suitcase.", "Tôi sẽ gắn thẻ hành lý lên vali của anh/chị.", "手荷物タグ", "tenimotsu tagu"),
  ("fragile", "/ˈfrædʒaɪl/", "adj", "dễ vỡ", "I'll put a <b>fragile</b> sticker on this box.", "Tôi sẽ dán nhãn 'dễ vỡ' lên thùng này.", "割れ物", "waremono"),
  ("power bank", "/ˈpaʊə bæŋk/", "n", "sạc dự phòng", "Is there a <b>power bank</b> in your suitcase?", "Trong vali của anh/chị có sạc dự phòng không ạ?", "モバイルバッテリー", "mobairu batterī"),
  ("oversized", "/ˌəʊvəˈsaɪzd/", "adj", "quá khổ", "Please take <b>oversized</b> items like bikes to counter 30.", "Đồ quá khổ như xe đạp, anh/chị vui lòng mang đến quầy 30."),
 ],
 "phrases": [
  ("Could you put your bag on the scale, please?", "Anh/chị đặt túi lên cân giúp tôi nhé."),
  ("Your bag is 26 kilos. Your allowance is 23 kilos.", "Túi của anh/chị nặng 26 ký. Hạn mức của anh/chị là 23 ký."),
  ("You can move some things to your carry-on, or pay for excess baggage.", "Anh/chị có thể chuyển bớt đồ sang hành lý xách tay, hoặc trả phí quá cước."),
  ("The fee is shown on this screen.", "Mức phí hiển thị trên màn hình này ạ."),
  ("Do you have any power banks or lithium batteries in this bag?", "Trong túi này anh/chị có sạc dự phòng hay pin lithium không ạ?"),
  ("According to our safety rules, power banks must stay in your carry-on.", "Theo quy định an toàn của chúng tôi, sạc dự phòng phải để trong hành lý xách tay."),
  ("Is there anything fragile inside?", "Bên trong có đồ dễ vỡ không ạ?"),
  ("Your bag is checked through to Paris.", "Hành lý của anh/chị được chuyển thẳng đến Paris."),
  ("Here is your baggage claim tag. Please keep it safe.", "Đây là cuống thẻ hành lý của anh/chị. Anh/chị giữ cẩn thận nhé."),
  ("Please take this bag to the oversized baggage counter.", "Anh/chị vui lòng mang túi này đến quầy hành lý quá khổ."),
 ],
 "dialogues": [
  ("Is my bag too heavy?", [
    ("It's 25 kilos, and your allowance is 23. You can take out two kilos, or pay the excess baggage fee.", True, "Nói số cân + hạn mức + đưa hai lựa chọn."),
    ("Yes, too heavy. Pay money.", False, "Cộc lốc, như ra lệnh; nên nói số ký và cho khách lựa chọn."),
    ("Your bag is heavy than the rule.", False, "Sai so sánh hơn: 'heavier than' — và nên nói rõ số ký."),
  ]),
  ("How much is the fee for the extra kilos?", [
    ("The fee is shown on this screen. You can pay at the ticket desk next to counter 20.", True, "Không tự đọc giá bừa — chỉ màn hình + chỗ thanh toán."),
    ("Very expensive, you should not pay.", False, "Không trả lời câu hỏi và khuyên khách một cách tiêu cực."),
    ("I don't know the price, maybe cheap.", False, "Đoán mò về tiền — nên chỉ màn hình hoặc hỏi quầy vé."),
  ]),
  ("Can I take this small bag on the plane?", [
    ("Yes, you can. One small bag is fine, as long as it fits in the overhead bin.", True, "Cho phép + điều kiện rõ ràng."),
    ("Yes, can bring.", False, "Thiếu chủ ngữ và tân ngữ: 'Yes, you can take it with you.'"),
    ("Small bag OK, big bag no OK.", False, "Nói kiểu từng chữ, không rõ nghĩa; nên giải thích điều kiện 'as long as it fits…'."),
  ]),
  ("There's a power bank in my suitcase. Is that OK?", [
    ("I'm afraid it can't go in checked baggage. Could you take it out and keep it in your carry-on, please?", True, "Nói lịch sự 'I'm afraid…' + hướng dẫn chuyển sang hành lý xách tay."),
    ("No, it will explode.", False, "Doạ khách, không hướng dẫn cần làm gì."),
    ("Power bank no put in the suitcase.", False, "Thiếu động từ, dịch từng chữ: 'You can't put a power bank in your suitcase.'"),
  ]),
  ("There's a glass vase in this box. Please be careful with it.", [
    ("Of course. I'll put a fragile sticker on it. The handling team will take extra care.", True, "Đồng ý + dán nhãn dễ vỡ + trấn an khách."),
    ("Glass is not our problem.", False, "Thiếu thiện chí, khách sẽ lo lắng hơn."),
    ("OK, I will careful.", False, "Thiếu 'be': 'I'll be careful.' — và nên dán nhãn 'fragile'."),
  ]),
 ],
 "listen": [
  ("Please put your bag on the scale", ["bag", "scale"], "đặt túi lên cân"),
  ("Your bag is three kilos overweight", ["three", "overweight"], "túi quá cân"),
  ("Do you have a power bank in this bag", ["power", "bag"], "hỏi sạc dự phòng"),
  ("Your suitcase is checked through to Paris", ["suitcase", "Paris"], "hành lý chuyển thẳng"),
  ("Your bag is twenty-six kilos, and your allowance is twenty-three. You can move some things to your carry-on. The fee for excess baggage is shown on the screen.", ["allowance", "carry-on", "fee"], "giải thích hành lý quá cân"),
  ("Is there anything fragile in this box? I'll put a sticker on it. Here is your claim tag. Please keep it safe.", ["fragile", "sticker", "claim"], "gửi thùng đồ dễ vỡ"),
 ],
})

# ───────────────────────── 3. Chỗ ngồi & yêu cầu dịch vụ ─────────────────────────
PHASES.append({
 "title": "Chỗ ngồi & yêu cầu dịch vụ",
 "vocab": [
  ("aisle seat", "/ˈaɪl siːt/", "n", "ghế cạnh lối đi", "Would you prefer a window seat or an <b>aisle seat</b>?", "Anh/chị muốn ghế cạnh cửa sổ hay ghế cạnh lối đi ạ?", "通路側の席", "tsūrogawa no seki"),
  ("window seat", "/ˈwɪndəʊ siːt/", "n", "ghế cạnh cửa sổ", "There's one <b>window seat</b> left in row 20.", "Hàng 20 còn một ghế cạnh cửa sổ.", "窓側の席", "madogawa no seki"),
  ("exit row", "/ˈeksɪt rəʊ/", "n", "hàng ghế cạnh cửa thoát hiểm", "Passengers in the <b>exit row</b> must be able to help in an emergency.", "Hành khách ngồi hàng cạnh cửa thoát hiểm phải có khả năng hỗ trợ khi khẩn cấp.", "非常口座席", "hijōguchi zaseki"),
  ("legroom", "/ˈleɡruːm/", "n", "chỗ để chân", "Seats in row 11 have more <b>legroom</b>.", "Ghế hàng 11 có nhiều chỗ để chân hơn."),
  ("business class", "/ˈbɪznəs klɑːs/", "n", "hạng thương gia", "The <b>business class</b> lounge is on the second floor.", "Phòng chờ hạng thương gia ở tầng hai.", "ビジネスクラス", "bijinesu kurasu"),
  ("economy class", "/ɪˈkɒnəmi klɑːs/", "n", "hạng phổ thông", "Your ticket is in <b>economy class</b>.", "Vé của anh/chị là hạng phổ thông.", "エコノミークラス", "ekonomī kurasu"),
  ("upgrade", "/ˌʌpˈɡreɪd/", "v", "nâng hạng (ghế)", "Would you like to <b>upgrade</b> to business class?", "Anh/chị có muốn nâng lên hạng thương gia không ạ?", "アップグレード", "appugurēdo"),
  ("special meal", "/ˌspeʃl ˈmiːl/", "n", "suất ăn đặc biệt (chay, không gluten…)", "Did you order a <b>special meal</b>?", "Anh/chị có đặt suất ăn đặc biệt không ạ?", "特別機内食", "tokubetsu kinaishoku"),
  ("overbooked", "/ˌəʊvəˈbʊkt/", "adj", "bán vượt số ghế", "The flight is <b>overbooked</b>, so we need two volunteers.", "Chuyến bay bị bán vượt số ghế nên chúng tôi cần hai khách tình nguyện đổi chuyến.", "オーバーブッキング", "ōbābukkingu"),
  ("bassinet", "/ˌbæsɪˈnet/", "n", "nôi em bé gắn vách", "We can give you a seat with a <b>bassinet</b> for your baby.", "Chúng tôi có thể xếp cho anh/chị ghế có nôi gắn vách cho em bé.", "バシネット", "bashinetto"),
 ],
 "phrases": [
  ("Would you like a window seat or an aisle seat?", "Anh/chị muốn ghế cửa sổ hay ghế lối đi ạ?"),
  ("I'm sorry, the flight is quite full. Let me see what I can do.", "Xin lỗi, chuyến bay khá kín chỗ. Để tôi xem có thể làm gì."),
  ("I can seat you together in row 32.", "Tôi có thể xếp anh chị ngồi cạnh nhau ở hàng 32."),
  ("This seat has extra legroom. There is an extra charge for it.", "Ghế này có thêm chỗ để chân. Ghế này có tính thêm phí ạ."),
  ("Are you willing and able to help in an emergency?", "Anh/chị có sẵn lòng và đủ khả năng hỗ trợ khi có tình huống khẩn cấp không?"),
  ("I can see your vegetarian meal is confirmed.", "Tôi thấy suất ăn chay của anh/chị đã được xác nhận."),
  ("I'm afraid special meals need to be ordered before the flight.", "Tôi e là suất ăn đặc biệt cần được đặt trước chuyến bay."),
  ("You can upgrade to business class for an extra charge. Would you like to know the price?", "Anh/chị có thể nâng lên hạng thương gia, có tính thêm phí. Anh/chị có muốn biết giá không ạ?"),
  ("The flight is overbooked. Would you be willing to take a later flight?", "Chuyến bay bị bán vượt ghế. Anh/chị có sẵn lòng đi chuyến muộn hơn không ạ?"),
  ("I've requested a bassinet seat for you.", "Tôi đã yêu cầu ghế có nôi em bé cho anh/chị."),
 ],
 "dialogues": [
  ("Can my wife and I sit together?", [
    ("Let me check. Yes, I have two seats together in row 28, a window and a middle seat. Is that OK?", True, "Kiểm tra + đưa ghế cụ thể + hỏi ý khách."),
    ("Together no have.", False, "Dịch từng chữ 'không có ghế cạnh nhau': 'I'm sorry, there are no seats together.'"),
    ("You can change seats on the plane.", False, "Đẩy việc cho khách và tiếp viên; nên kiểm tra sơ đồ ghế trước."),
  ]),
  ("Can I have a seat in the exit row?", [
    ("Yes, there's one in row 12. Are you willing and able to help the crew in an emergency?", True, "Có ghế + hỏi câu bắt buộc về khả năng hỗ trợ."),
    ("Yes, sit exit row, more space.", False, "Thiếu chủ ngữ và bỏ qua điều kiện an toàn của hàng thoát hiểm."),
    ("Exit row is for crew only.", False, "Thông tin sai — khách ngồi được nếu đủ điều kiện."),
  ]),
  ("I ordered a vegetarian meal. Can you check it?", [
    ("Of course. Yes, your vegetarian meal is confirmed for both flights.", True, "Kiểm tra + xác nhận rõ cho cả hai chặng."),
    ("Yes, you order vegetable.", False, "Sai thì ('ordered') và sai từ: suất chay là 'vegetarian meal'."),
    ("All meals are the same.", False, "Sai và không kiểm tra yêu cầu của khách."),
  ]),
  ("Is it possible to upgrade to business class?", [
    ("Yes, there are two seats left. There is an extra charge, and I can show you the price on the screen.", True, "Còn ghế + nói rõ có phí + chỉ giá trên màn hình."),
    ("Business class very expensive for you.", False, "Thiếu 'is', và đoán khả năng chi trả của khách là bất lịch sự."),
    ("Can, but pay more money.", False, "Thiếu chủ ngữ, nói kiểu từng chữ: 'Yes, but there is an extra charge.'"),
  ]),
  ("I'm travelling with my baby. Is there a better seat for us?", [
    ("Yes. I can give you a seat at the front with a bassinet. The crew will set it up after take-off.", True, "Đưa ghế có nôi + giải thích khi nào dùng."),
    ("Baby sit on your lap, OK.", False, "Thiếu động từ và không trả lời về ghế phù hợp hơn."),
    ("Sorry, full. No better seat.", False, "Trả lời cộc khi chưa kiểm tra; nên xem ghế có nôi hoặc ghế đầu khoang."),
  ]),
 ],
 "listen": [
  ("Would you like a window or an aisle seat", ["window", "aisle"], "chọn ghế"),
  ("I can seat you together in row thirty-two", ["together", "thirty-two"], "ngồi cạnh nhau"),
  ("Your vegetarian meal is confirmed", ["vegetarian", "confirmed"], "suất ăn chay"),
  ("This seat has extra legroom", ["seat", "legroom"], "ghế rộng chân"),
  ("This flight is overbooked today. We are looking for two passengers who can take a later flight. Please come to the counter if you are interested.", ["overbooked", "later", "counter"], "tìm khách tình nguyện"),
  ("You are in the exit row, seat twelve C. Are you willing to help in an emergency? Please read the safety card before take-off.", ["exit", "emergency", "card"], "khách ngồi hàng thoát hiểm"),
 ],
})

# ───────────────────────── 4. Soi chiếu an ninh & xuất nhập cảnh ─────────────────────────
PHASES.append({
 "title": "Soi chiếu an ninh & xuất nhập cảnh",
 "vocab": [
  ("security check", "/sɪˈkjʊərəti tʃek/", "n", "khu kiểm tra an ninh", "The <b>security check</b> is busy this morning.", "Sáng nay khu kiểm tra an ninh rất đông.", "保安検査", "hoan kensa"),
  ("tray", "/treɪ/", "n", "khay (đựng đồ khi soi chiếu)", "Please put your phone and keys in the <b>tray</b>.", "Anh/chị vui lòng để điện thoại và chìa khoá vào khay.", "トレイ", "torei"),
  ("liquids", "/ˈlɪkwɪdz/", "n", "chất lỏng", "Do you have any <b>liquids</b> in your bag?", "Trong túi anh/chị có chất lỏng không ạ?", "液体物", "ekitaibutsu"),
  ("metal detector", "/ˈmetl dɪˌtektə/", "n", "cổng dò kim loại", "Please walk through the <b>metal detector</b>.", "Anh/chị vui lòng đi qua cổng dò kim loại.", "金属探知機", "kinzoku tanchiki"),
  ("body scanner", "/ˈbɒdi ˌskænə/", "n", "máy quét toàn thân", "Please stand in the <b>body scanner</b> and raise your arms.", "Anh/chị đứng vào máy quét toàn thân và giơ hai tay lên.", "ボディスキャナー", "bodi sukyanā"),
  ("pat-down", "/ˈpæt daʊn/", "n", "khám người bằng tay", "I need to do a quick <b>pat-down</b>. Is that OK?", "Tôi cần khám người nhanh bằng tay. Anh/chị đồng ý chứ ạ?"),
  ("prohibited items", "/prəˈhɪbɪtɪd ˌaɪtəmz/", "n", "đồ vật bị cấm mang theo", "The list of <b>prohibited items</b> is on the sign.", "Danh sách đồ vật bị cấm có trên biển thông báo.", "持ち込み禁止品", "mochikomi kinshihin"),
  ("sharp objects", "/ˌʃɑːp ˈɒbdʒɪkts/", "n", "vật sắc nhọn", "Knives and other <b>sharp objects</b> can't go in your carry-on.", "Dao và các vật sắc nhọn khác không được để trong hành lý xách tay."),
  ("laptop", "/ˈlæptɒp/", "n", "máy tính xách tay", "Please take your <b>laptop</b> out of the bag.", "Anh/chị vui lòng lấy máy tính xách tay ra khỏi túi.", "ノートパソコン", "nōto pasokon"),
  ("passport control", "/ˈpɑːspɔːt kənˌtrəʊl/", "n", "quầy kiểm soát hộ chiếu (xuất nhập cảnh)", "After security, go to <b>passport control</b>.", "Sau khu an ninh, anh/chị đi đến quầy kiểm soát hộ chiếu.", "出入国審査", "shutsunyūkoku shinsa"),
 ],
 "phrases": [
  ("Please put your bag and jacket in the tray.", "Anh/chị vui lòng để túi và áo khoác vào khay."),
  ("Please take out your laptop and any liquids.", "Anh/chị vui lòng lấy máy tính xách tay và chất lỏng ra ngoài."),
  ("Could you take off your belt and your watch, please?", "Anh/chị tháo thắt lưng và đồng hồ ra giúp tôi nhé."),
  ("Please empty your pockets.", "Anh/chị vui lòng lấy hết đồ trong túi quần áo ra."),
  ("Walk through, please. Raise your arms like this.", "Mời anh/chị đi qua. Giơ hai tay lên như thế này ạ."),
  ("I need to check your bag again. Is this your bag?", "Tôi cần kiểm tra lại túi của anh/chị. Đây có phải túi của anh/chị không?"),
  ("I'm sorry, you can't take this bottle through security.", "Xin lỗi, anh/chị không thể mang chai này qua khu an ninh."),
  ("You can drink it now, or put it in your checked bag.", "Anh/chị có thể uống ngay bây giờ, hoặc cho vào hành lý ký gửi."),
  ("Thank you for your patience. You can take your things now.", "Cảm ơn anh/chị đã kiên nhẫn. Anh/chị có thể lấy đồ rồi ạ."),
  ("Passport control is straight ahead, on your left.", "Quầy kiểm soát hộ chiếu ở phía trước, bên tay trái ạ."),
 ],
 "dialogues": [
  ("Do I need to take my shoes off?", [
    ("No, you don't need to. Please just put your jacket, belt and phone in the tray.", True, "Trả lời rõ + hướng dẫn cần bỏ gì vào khay."),
    ("No need shoes.", False, "Nói kiểu từng chữ; nên nói 'You don't need to take off your shoes.'"),
    ("Why you ask? Just go.", False, "Thiếu 'do' và rất thô; nên trả lời lịch sự."),
  ]),
  ("Why is my bag going through the scanner again?", [
    ("There's something we need to see more clearly. It will only take a minute. Is this your bag?", True, "Giải thích nhẹ nhàng + thời gian + xác nhận chủ túi."),
    ("Because your bag has problem.", False, "Thiếu mạo từ ('a problem') và làm khách lo lắng không cần thiết."),
    ("I don't know, it's the machine.", False, "Né tránh, không giải thích và thiếu chuyên nghiệp."),
  ]),
  ("This is just water. Can I take it with me?", [
    ("I'm sorry, this bottle is too big to take through security. You can drink it now or buy water after the check.", True, "Xin lỗi + lý do + hai lựa chọn."),
    ("No water. Throw it.", False, "Cộc lốc như ra lệnh; nên xin lỗi và đưa lựa chọn."),
    ("Water is danger.", False, "Sai từ loại ('dangerous') và giải thích sai lý do."),
  ]),
  ("I'd prefer not to go through the body scanner.", [
    ("That's fine. We can do a pat-down instead. A staff member of the same gender will do it.", True, "Tôn trọng lựa chọn + phương án thay thế + cùng giới."),
    ("You must go, no choice.", False, "Cứng nhắc; thường có phương án khám tay thay thế."),
    ("Scanner is safe, don't worry, go.", False, "Không tôn trọng yêu cầu của khách, thiếu mạo từ 'The'."),
  ]),
  ("The line is so long. My flight leaves in 40 minutes!", [
    ("Let me see your boarding pass... You're on the 10:30 flight. Please come with me to the priority lane.", True, "Kiểm tra giờ bay + hành động cụ thể giúp khách."),
    ("Everybody is in a hurry. Wait your turn.", False, "Lạnh lùng, bỏ qua khách sắp lỡ chuyến; nên xem giờ bay và giúp khách."),
    ("You should come early.", False, "Trách khách, không giúp gì."),
  ]),
 ],
 "listen": [
  ("Please put your laptop in a separate tray", ["laptop", "tray"], "để máy tính vào khay riêng"),
  ("Take off your belt and walk through", ["belt", "walk"], "qua cổng soi chiếu"),
  ("Is this black bag yours", ["black", "yours"], "xác nhận chủ túi"),
  ("Passport control is straight ahead", ["Passport", "straight"], "chỉ đường"),
  ("Please take out your laptop and any liquids. Put your jacket and belt in the tray. Then walk through the metal detector.", ["liquids", "jacket", "metal"], "hướng dẫn soi chiếu"),
  ("I'm sorry, this bottle is too big to take through security. You can drink it now or put it in the bin. Thank you for your patience.", ["bottle", "drink", "patience"], "khách mang chai nước"),
 ],
})

# ───────────────────────── 5. Cửa ra máy bay & lên máy bay ─────────────────────────
PHASES.append({
 "title": "Cửa ra máy bay & lên máy bay",
 "vocab": [
  ("gate", "/ɡeɪt/", "n", "cửa ra máy bay", "Your flight leaves from <b>Gate</b> 7.", "Chuyến bay của anh/chị khởi hành ở cửa số 7.", "搭乗口", "tōjōguchi"),
  ("board", "/bɔːd/", "v", "lên (máy bay)", "Passengers in rows 30 to 45 can <b>board</b> now.", "Hành khách hàng ghế 30 đến 45 có thể lên máy bay bây giờ.", "搭乗する", "tōjō suru"),
  ("final call", "/ˌfaɪnl ˈkɔːl/", "n", "lần gọi cuối", "This is the <b>final call</b> for flight 215 to Singapore.", "Đây là lần gọi cuối cho chuyến bay 215 đi Singapore.", "最終搭乗案内", "saishū tōjō annai"),
  ("priority boarding", "/praɪˈɒrəti ˌbɔːdɪŋ/", "n", "lên máy bay ưu tiên", "Families with small children can use <b>priority boarding</b>.", "Gia đình có con nhỏ được lên máy bay ưu tiên.", "優先搭乗", "yūsen tōjō"),
  ("jet bridge", "/ˈdʒet brɪdʒ/", "n", "ống lồng (cầu dẫn khách lên máy bay)", "Please walk down the <b>jet bridge</b> to the aircraft.", "Anh/chị đi theo ống lồng để lên máy bay.", "ボーディングブリッジ", "bōdingu burijji"),
  ("gate change", "/ˈɡeɪt tʃeɪndʒ/", "n", "việc đổi cửa ra máy bay", "There is a <b>gate change</b>. The flight now leaves from Gate 21.", "Có thay đổi cửa ra máy bay. Chuyến bay giờ khởi hành ở cửa 21.", "搭乗口変更", "tōjōguchi henkō"),
  ("standby", "/ˈstændbaɪ/", "n", "khách chờ ghế trống", "You are on the <b>standby</b> list for the next flight.", "Anh/chị đang trong danh sách chờ ghế trống của chuyến sau.", "キャンセル待ち", "kyanseru machi"),
  ("no-show", "/ˌnəʊ ˈʃəʊ/", "n", "khách vắng mặt (có vé/đã làm thủ tục nhưng không đến lên máy bay)", "We have one <b>no-show</b>, so we must offload his bag.", "Có một khách không có mặt nên chúng ta phải dỡ hành lý của anh ấy xuống.", "ノーショー", "nōshō"),
  ("offload", "/ˌɒfˈləʊd/", "v", "dỡ (hành lý/khách) khỏi chuyến bay", "The ramp team will <b>offload</b> his bag before departure.", "Đội sân đỗ sẽ dỡ túi của anh ấy xuống trước giờ khởi hành."),
  ("announcement", "/əˈnaʊnsmənt/", "n", "thông báo", "Please listen for the next <b>announcement</b>.", "Quý khách vui lòng chú ý nghe thông báo tiếp theo.", "アナウンス", "anaunsu"),
 ],
 "phrases": [
  ("Good afternoon, ladies and gentlemen. Flight 215 to Singapore is now boarding.", "Xin chào quý khách. Chuyến bay 215 đi Singapore hiện đang mời khách lên máy bay."),
  ("We now invite passengers with small children and those who need assistance to board.", "Chúng tôi xin mời hành khách có con nhỏ và hành khách cần hỗ trợ lên máy bay trước."),
  ("Please have your boarding pass and passport ready.", "Quý khách vui lòng chuẩn bị sẵn thẻ lên máy bay và hộ chiếu."),
  ("This is the final call for passenger David Lee.", "Đây là lần gọi cuối dành cho hành khách David Lee."),
  ("Please note there is a gate change. The flight will now leave from Gate 21.", "Xin lưu ý có thay đổi cửa ra máy bay. Chuyến bay sẽ khởi hành ở cửa 21."),
  ("I'm sorry, the gate is closed and we can't board you.", "Xin lỗi, cửa đã đóng và chúng tôi không thể cho anh/chị lên máy bay."),
  ("Your carry-on is too big for the cabin. We'll check it in here at the gate.", "Hành lý xách tay của anh/chị quá lớn cho khoang khách. Chúng tôi sẽ ký gửi ngay tại cửa ra máy bay."),
  ("All passengers are on board. The count is 186.", "Tất cả hành khách đã lên máy bay. Tổng số là 186."),
  ("One passenger is missing. Please don't close the door yet.", "Còn thiếu một hành khách. Đừng đóng cửa vội."),
  ("Ramp, we have one no-show. Please offload bag tag 4521.", "Sân đỗ ơi, có một khách không có mặt. Vui lòng dỡ túi có thẻ số 4521."),
 ],
 "dialogues": [
  ("Excuse me, is this the gate for the flight to Bangkok?", [
    ("Yes, it is. Boarding starts in about 15 minutes. Please have your passport ready.", True, "Xác nhận + giờ bắt đầu + nhắc chuẩn bị giấy tờ."),
    ("Yes, this is. Wait.", False, "Cộc lốc; nên nói bao lâu nữa bắt đầu lên máy bay."),
    ("Bangkok is here, correct.", False, "Dịch từng chữ, câu không tự nhiên: 'Yes, this is the gate for Bangkok.'"),
  ]),
  ("I just arrived. Can I still get on the plane?", [
    ("I'm very sorry, the gate closed five minutes ago and the door is closed. Let me take you to the customer service desk to find another flight.", True, "Xin lỗi + nói rõ lý do + hướng giải quyết tiếp."),
    ("Too late. Go home.", False, "Thô và không giúp khách; nên chỉ quầy để đổi chuyến."),
    ("You late, the plane go already.", False, "Thiếu 'are', sai thì ('has gone') và nghe như trách khách."),
  ]),
  ("Why can't I take my bag on board? It fit last time.", [
    ("I understand. Today the flight is full and the overhead bins are almost full. We'll check your bag in here, and you can collect it at your destination.", True, "Thông cảm + lý do cụ thể + giải pháp (ký gửi tại cửa, nhận ở điểm đến)."),
    ("Last time is last time.", False, "Nghe như cãi, không giải thích lý do."),
    ("Your bag big, no space.", False, "Thiếu động từ 'is'; cần lịch sự và nói phương án ký gửi."),
  ]),
  ("Gate, this is ramp. The hold door closes in five minutes. Are all passengers on board?", [
    ("Not yet. We're still missing one passenger. I'll give you an update in two minutes.", True, "Báo đúng tình trạng + hẹn cập nhật có thời gian."),
    ("Maybe yes, I think.", False, "Mơ hồ — với an toàn bay phải báo số chính xác."),
    ("Missing one people.", False, "Sai số ít/nhiều: 'one passenger' — và thiếu chủ ngữ 'We're…'."),
  ]),
  ("The screen says Gate 9, but my boarding pass says Gate 14. Which one is correct?", [
    ("Thanks for checking. There was a gate change, so please go to Gate 9. It's about five minutes' walk.", True, "Giải thích có đổi cửa + chỉ cửa đúng + thời gian đi."),
    ("Boarding pass is old.", False, "Thiếu mạo từ và không nói rõ khách cần đi đâu."),
    ("Both is OK.", False, "Sai hoàn toàn và sai ngữ pháp ('Both are'); khách có thể lỡ chuyến."),
  ]),
 ],
 "listen": [
  ("Flight two one five is now boarding", ["Flight", "boarding"], "mời khách lên máy bay"),
  ("Please have your boarding pass and passport ready", ["passport", "ready"], "chuẩn bị giấy tờ"),
  ("There is a gate change for this flight", ["gate", "change"], "đổi cửa"),
  ("One passenger is still missing", ["passenger", "missing"], "báo thiếu khách"),
  ("Ladies and gentlemen, this is the final call for flight two one five to Singapore. Please go to Gate seven immediately. The gate will close in five minutes.", ["final", "seven", "close"], "thông báo gọi lần cuối"),
  ("Good afternoon. Due to a gate change, flight six eight zero to Osaka will now leave from Gate twenty-one. We are sorry for any inconvenience.", ["change", "Osaka", "inconvenience"], "thông báo đổi cửa"),
 ],
})

# ───────────────────────── 6. Chậm, huỷ chuyến & lỡ nối chuyến ─────────────────────────
PHASES.append({
 "title": "Chậm, huỷ chuyến & lỡ nối chuyến",
 "vocab": [
  ("delay", "/dɪˈleɪ/", "n/v", "sự chậm trễ; làm chậm", "We're sorry for the <b>delay</b>.", "Chúng tôi xin lỗi vì sự chậm trễ.", "遅延", "chien"),
  ("cancelled", "/ˈkænsld/", "adj", "bị huỷ (chuyến bay)", "I'm afraid your flight has been <b>cancelled</b>.", "Tôi e là chuyến bay của anh/chị đã bị huỷ.", "欠航", "kekkō"),
  ("connecting flight", "/kəˌnektɪŋ ˈflaɪt/", "n", "chuyến bay nối tiếp", "Your <b>connecting flight</b> to Paris leaves at 23:40.", "Chuyến bay nối tiếp đi Paris của anh/chị khởi hành lúc 23 giờ 40.", "乗り継ぎ便", "noritsugi bin"),
  ("missed connection", "/ˌmɪst kəˈnekʃn/", "n", "việc lỡ chuyến bay nối", "Passengers with a <b>missed connection</b>, please go to the transfer desk.", "Hành khách bị lỡ chuyến nối vui lòng đến quầy nối chuyến."),
  ("rebook", "/ˌriːˈbʊk/", "v", "đặt lại (sang chuyến khác)", "I can <b>rebook</b> you on the next flight.", "Tôi có thể đặt lại cho anh/chị sang chuyến kế tiếp."),
  ("meal voucher", "/ˈmiːl ˌvaʊtʃə/", "n", "phiếu ăn", "Here is a <b>meal voucher</b> for the restaurant upstairs.", "Đây là phiếu ăn dùng ở nhà hàng tầng trên.", "食事券", "shokujiken"),
  ("transit", "/ˈtrænzɪt/", "n", "quá cảnh", "Are you in <b>transit</b>, or is this your final destination?", "Anh/chị đang quá cảnh hay đây là điểm đến cuối cùng?", "トランジット", "toranjitto"),
  ("weather", "/ˈweðə/", "n", "thời tiết", "The flight is delayed because of bad <b>weather</b>.", "Chuyến bay bị chậm vì thời tiết xấu.", "天候", "tenkō"),
  ("compensation", "/ˌkɒmpenˈseɪʃn/", "n", "khoản bồi thường", "For questions about <b>compensation</b>, please fill in this form.", "Nếu có câu hỏi về bồi thường, anh/chị vui lòng điền vào mẫu này.", "補償", "hoshō"),
  ("accommodation", "/əˌkɒməˈdeɪʃn/", "n", "chỗ ở (khách sạn)", "We will arrange <b>accommodation</b> for you tonight.", "Chúng tôi sẽ sắp xếp chỗ ở cho anh/chị tối nay.", "宿泊", "shukuhaku"),
 ],
 "phrases": [
  ("I'm sorry, your flight is delayed by about two hours.", "Xin lỗi, chuyến bay của anh/chị bị chậm khoảng hai tiếng."),
  ("The delay is because of bad weather in Hong Kong.", "Chuyến bay bị chậm vì thời tiết xấu ở Hồng Kông."),
  ("The new departure time is 4:30 p.m.", "Giờ khởi hành mới là 4 giờ 30 chiều."),
  ("I'm afraid the flight has been cancelled.", "Tôi e là chuyến bay đã bị huỷ."),
  ("I can rebook you on the first flight tomorrow morning.", "Tôi có thể đặt lại cho anh/chị chuyến bay đầu tiên sáng mai."),
  ("Here is a meal voucher. You can use it at the restaurants after security.", "Đây là phiếu ăn. Anh/chị có thể dùng ở các nhà hàng sau khu an ninh."),
  ("We will arrange a hotel and transport for you tonight.", "Tối nay chúng tôi sẽ sắp xếp khách sạn và xe đưa đón cho anh/chị."),
  ("Don't worry. Your bag will be moved to your new flight.", "Anh/chị đừng lo. Hành lý sẽ được chuyển sang chuyến bay mới."),
  ("For compensation, please fill in this form. Our team will reply to you.", "Về việc bồi thường, anh/chị vui lòng điền mẫu này. Bộ phận của chúng tôi sẽ phản hồi anh/chị."),
  ("We'll give you an update as soon as we have more information.", "Chúng tôi sẽ cập nhật cho anh/chị ngay khi có thêm thông tin."),
 ],
 "dialogues": [
  ("Why is my flight delayed?", [
    ("I'm sorry for the delay. There's bad weather in Hong Kong, so the aircraft arrived late. The new departure time is 3:40.", True, "Xin lỗi + lý do + giờ khởi hành mới."),
    ("Delay because weather.", False, "Thiếu chủ ngữ và động từ; nên xin lỗi và báo giờ mới."),
    ("I don't know. Not my problem.", False, "Đẩy trách nhiệm — khách sẽ càng bực; hãy kiểm tra và giải thích."),
  ]),
  ("My flight was cancelled. What can I do now?", [
    ("I'm very sorry. I can rebook you on the first flight tomorrow at 8:10, and we'll arrange a hotel for tonight.", True, "Xin lỗi + chuyến mới cụ thể + lo chỗ ở."),
    ("You wait tomorrow.", False, "Thiếu 'until' và không nói chuyến nào, ở đâu tối nay."),
    ("Cancel is cancel, sorry.", False, "Cứng nhắc, sai từ loại ('cancelled'); cần đưa phương án cho khách."),
  ]),
  ("I'm going to miss my connection in Frankfurt!", [
    ("Let me check. If you miss it, we'll rebook you on the next flight, and your bag will go with you.", True, "Kiểm tra + trấn an bằng phương án cụ thể (chuyến sau + hành lý)."),
    ("Maybe you miss, maybe not.", False, "Mơ hồ, thiếu 'will'; khách cần biết phương án."),
    ("You should book a longer time.", False, "Trách khách, không giúp gì."),
  ]),
  ("Will I get compensation for this delay?", [
    ("It depends on the reason and the length of the delay. Please fill in this form, and our customer team will reply to you.", True, "Không hứa bừa — giải thích 'tuỳ trường hợp' + hướng dẫn quy trình."),
    ("Yes, you get money, 100 percent.", False, "Hứa chắc khi chưa biết — chỉ nên hướng dẫn quy trình, không tự quyết."),
    ("No, never compensation.", False, "Khẳng định bừa và sai ngữ pháp; nên hướng dẫn gửi yêu cầu."),
  ]),
  ("How long do we have to wait? Nobody tells us anything!", [
    ("I'm sorry, I understand it's frustrating. The engineers are checking the aircraft now. I'll give everyone an update in 30 minutes.", True, "Xin lỗi + thông cảm + tình hình + hẹn giờ cập nhật."),
    ("Calm down, sir.", False, "Bảo khách 'bình tĩnh' thường làm khách bực hơn; hãy xin lỗi và cho thông tin."),
    ("Soon, soon. Please sit.", False, "Mơ hồ, lặp từ kiểu 'sắp rồi sắp rồi'; khách cần mốc thời gian."),
  ]),
 ],
 "listen": [
  ("Your flight is delayed by two hours", ["delayed", "hours"], "báo chậm chuyến"),
  ("The new departure time is four thirty", ["new", "thirty"], "giờ khởi hành mới"),
  ("I can rebook you on the next flight", ["rebook", "next"], "đặt lại chuyến"),
  ("Here is a meal voucher for you", ["meal", "voucher"], "phiếu ăn"),
  ("Ladies and gentlemen, we are sorry to announce that flight three two zero to Hanoi is delayed because of bad weather. The new departure time is six fifteen. Meal vouchers are available at the gate.", ["delayed", "weather", "vouchers"], "thông báo chậm chuyến"),
  ("I'm very sorry, your flight has been cancelled. I have booked you on the first flight tomorrow morning. We will also arrange a hotel for tonight.", ["cancelled", "tomorrow", "hotel"], "báo huỷ chuyến"),
 ],
})

# ───────────────────────── 7. Phục vụ trên máy bay ─────────────────────────
PHASES.append({
 "title": "Phục vụ trên máy bay",
 "vocab": [
  ("cabin crew", "/ˈkæbɪn kruː/", "n", "tổ tiếp viên", "Our <b>cabin crew</b> will serve dinner after take-off.", "Tổ tiếp viên sẽ phục vụ bữa tối sau khi cất cánh.", "客室乗務員", "kyakushitsu jōmuin"),
  ("galley", "/ˈɡæli/", "n", "khu bếp trên máy bay", "I'll get some hot water from the <b>galley</b>.", "Tôi sẽ lấy nước nóng ở khu bếp.", "ギャレー", "gyarē"),
  ("overhead bin", "/ˌəʊvəhed ˈbɪn/", "n", "hộc hành lý phía trên", "Let me put your bag in the <b>overhead bin</b>.", "Để tôi cất túi của anh/chị lên hộc hành lý phía trên.", "手荷物収納棚", "tenimotsu shūnōdana"),
  ("tray table", "/ˈtreɪ ˌteɪbl/", "n", "bàn ăn gập ở lưng ghế", "Could you open your <b>tray table</b>, please?", "Anh/chị mở bàn ăn giúp tôi nhé."),
  ("blanket", "/ˈblæŋkɪt/", "n", "chăn, mền", "Would you like a <b>blanket</b>? It's cold at night.", "Anh/chị có cần chăn không ạ? Ban đêm trời lạnh.", "毛布", "mōfu"),
  ("headphones", "/ˈhedfəʊnz/", "n", "tai nghe", "You can use these <b>headphones</b> for the movies.", "Anh/chị có thể dùng tai nghe này để xem phim.", "ヘッドホン", "heddohon"),
  ("duty-free", "/ˌdjuːti ˈfriː/", "adj", "miễn thuế", "We sell <b>duty-free</b> perfume and chocolate on board.", "Chúng tôi có bán nước hoa và sô-cô-la miễn thuế trên máy bay.", "免税", "menzei"),
  ("call button", "/ˈkɔːl ˌbʌtn/", "n", "nút gọi tiếp viên", "Please press the <b>call button</b> if you need anything.", "Anh/chị bấm nút gọi tiếp viên nếu cần gì nhé.", "呼び出しボタン", "yobidashi botan"),
  ("arrival card", "/əˈraɪvl kɑːd/", "n", "tờ khai nhập cảnh", "Please fill in this <b>arrival card</b> before landing.", "Anh/chị vui lòng điền tờ khai nhập cảnh này trước khi hạ cánh.", "入国カード", "nyūkoku kādo"),
  ("lavatory", "/ˈlævətri/", "n", "nhà vệ sinh (trên máy bay)", "The <b>lavatory</b> at the back is free now.", "Nhà vệ sinh phía sau đang trống.", "化粧室", "keshōshitsu"),
 ],
 "phrases": [
  ("Welcome on board. May I see your boarding pass?", "Chào mừng anh/chị lên máy bay. Cho tôi xem thẻ lên máy bay được không ạ?"),
  ("Your seat is on the left, about halfway down the aisle.", "Ghế của anh/chị ở bên trái, khoảng giữa lối đi."),
  ("Let me help you with your bag.", "Để tôi giúp anh/chị cất túi."),
  ("Would you like chicken with rice or beef with noodles?", "Anh/chị dùng gà với cơm hay bò với mì ạ?"),
  ("What would you like to drink? We have water, juice, tea and coffee.", "Anh/chị muốn uống gì ạ? Chúng tôi có nước, nước ép, trà và cà phê."),
  ("Could you open your tray table, please?", "Anh/chị mở bàn ăn giúp tôi nhé."),
  ("Are you finished? May I take your tray?", "Anh/chị dùng xong chưa ạ? Tôi dọn khay được không?"),
  ("Please press the call button if you need anything.", "Anh/chị cần gì thì bấm nút gọi tiếp viên nhé."),
  ("Here is your arrival card. Please fill it in before landing.", "Đây là tờ khai nhập cảnh. Anh/chị vui lòng điền trước khi hạ cánh."),
  ("The duty-free cart will come through the cabin shortly.", "Xe hàng miễn thuế sẽ đi qua khoang trong ít phút nữa."),
 ],
 "dialogues": [
  ("Excuse me, there's no space for my bag.", [
    ("Let me find some space for you. There's room in the bin across the aisle. I'll put it there.", True, "Chủ động tìm chỗ + tự cất giúp khách."),
    ("No space, your problem.", False, "Đẩy việc cho khách — tiếp viên nên giúp tìm chỗ."),
    ("You put under seat.", False, "Thiếu tân ngữ và mạo từ: 'You can put it under the seat in front of you.'"),
  ]),
  ("What are the meal choices?", [
    ("We have chicken with rice or fish with noodles. Which would you prefer?", True, "Nêu đủ lựa chọn + hỏi khách chọn món nào."),
    ("Chicken, fish, which?", False, "Cụt lủn, thiếu câu; nên nói đủ món kèm theo."),
    ("Food is free.", False, "Không trả lời câu hỏi về các món."),
  ]),
  ("Could I have another blanket? I'm a bit cold.", [
    ("Of course. I'll bring one right away. Would you like some hot tea too?", True, "Đồng ý + làm ngay + chăm sóc thêm."),
    ("Blanket finish already.", False, "Dịch từng chữ 'hết rồi': 'I'm sorry, we've run out of blankets.'"),
    ("You wear your jacket.", False, "Nghe như ra lệnh và không đáp ứng yêu cầu."),
  ]),
  ("Oh no, I'm so sorry. I spilled my coffee.", [
    ("Don't worry. Are you OK? I'll bring some napkins and another coffee.", True, "Trấn an + hỏi khách có sao không + xử lý ngay."),
    ("Oh no, you make it dirty.", False, "Trách khách, làm khách xấu hổ hơn."),
    ("Why you not careful?", False, "Sai ngữ pháp ('Why weren't you careful?') và rất thiếu lịch sự."),
  ]),
  ("Do I need to fill in this arrival card?", [
    ("Yes, you do. You'll give it to the officer at passport control. Do you need a pen?", True, "Trả lời + dùng để làm gì + đề nghị cho mượn bút."),
    ("Yes, you write.", False, "Cộc, thiếu tân ngữ; nên nói 'Yes, please fill it in.'"),
    ("Card is for immigration.", False, "Thiếu mạo từ và không trả lời rõ có cần điền hay không."),
  ]),
 ],
 "listen": [
  ("Would you like chicken or fish", ["chicken", "fish"], "chọn món"),
  ("Please put your bag in the overhead bin", ["overhead", "bin"], "cất hành lý"),
  ("Press the call button if you need anything", ["call", "anything"], "nút gọi tiếp viên"),
  ("Would you like a blanket or a pillow", ["blanket", "pillow"], "mời chăn gối"),
  ("Good evening and welcome on board. In a few minutes, we will serve dinner and drinks. Please open your tray table when the cart comes to your row.", ["welcome", "dinner", "tray"], "thông báo phục vụ bữa tối"),
  ("Ladies and gentlemen, our duty-free shop is now open. You can see all the items in the magazine in your seat pocket. We accept cards and some foreign currencies.", ["duty-free", "magazine", "cards"], "thông báo bán hàng miễn thuế"),
 ],
})

# ───────────────────────── 8. An toàn bay ─────────────────────────
PHASES.append({
 "title": "An toàn bay",
 "vocab": [
  ("seat belt", "/ˈsiːt belt/", "n", "dây an toàn", "Please keep your <b>seat belt</b> on while you are seated.", "Anh/chị vui lòng thắt dây an toàn khi ngồi tại ghế.", "シートベルト", "shītoberuto"),
  ("fasten", "/ˈfɑːsn/", "v", "thắt, cài (dây an toàn)", "Please <b>fasten</b> your seat belt.", "Anh/chị vui lòng thắt dây an toàn.", "締める", "shimeru"),
  ("turbulence", "/ˈtɜːbjələns/", "n", "nhiễu động không khí (máy bay rung lắc)", "We are expecting some <b>turbulence</b>.", "Chúng ta sắp gặp nhiễu động không khí.", "乱気流", "rankiryū"),
  ("life jacket", "/ˈlaɪf ˌdʒækɪt/", "n", "áo phao", "Your <b>life jacket</b> is under your seat.", "Áo phao ở dưới ghế của anh/chị.", "救命胴衣", "kyūmei dōi"),
  ("oxygen mask", "/ˈɒksɪdʒən mɑːsk/", "n", "mặt nạ dưỡng khí", "Put on your own <b>oxygen mask</b> before helping others.", "Hãy đeo mặt nạ dưỡng khí cho mình trước khi giúp người khác.", "酸素マスク", "sanso masuku"),
  ("emergency exit", "/ɪˌmɜːdʒənsi ˈeksɪt/", "n", "cửa thoát hiểm", "Please find your nearest <b>emergency exit</b>.", "Quý khách vui lòng xác định cửa thoát hiểm gần nhất.", "非常口", "hijōguchi"),
  ("upright", "/ˈʌpraɪt/", "adj", "thẳng đứng", "Please put your seat in the <b>upright</b> position.", "Quý khách vui lòng dựng thẳng lưng ghế."),
  ("airplane mode", "/ˈeəpleɪn məʊd/", "n", "chế độ máy bay (trên điện thoại)", "Please switch your phone to <b>airplane mode</b>.", "Anh/chị vui lòng chuyển điện thoại sang chế độ máy bay.", "機内モード", "kinai mōdo"),
  ("take-off", "/ˈteɪk ɒf/", "n", "sự cất cánh", "Please stay seated during <b>take-off</b>.", "Quý khách vui lòng ngồi yên tại chỗ khi cất cánh.", "離陸", "ririku"),
  ("landing", "/ˈlændɪŋ/", "n", "sự hạ cánh", "We will begin our <b>landing</b> in 20 minutes.", "Chúng ta sẽ bắt đầu hạ cánh sau 20 phút nữa.", "着陸", "chakuriku"),
 ],
 "phrases": [
  ("Please fasten your seat belt and put your bag under the seat.", "Anh/chị vui lòng thắt dây an toàn và để túi dưới ghế."),
  ("Please put your seat in the upright position for take-off.", "Anh/chị vui lòng dựng thẳng lưng ghế để cất cánh."),
  ("Please switch your phone to airplane mode.", "Anh/chị vui lòng chuyển điện thoại sang chế độ máy bay."),
  ("Please open the window shade for landing.", "Anh/chị vui lòng mở tấm che cửa sổ khi hạ cánh."),
  ("Your life jacket is under your seat. Please don't take it out.", "Áo phao ở dưới ghế. Anh/chị vui lòng không lấy ra."),
  ("If the cabin pressure drops, oxygen masks will fall from the panel above you.", "Nếu áp suất trong khoang giảm, mặt nạ dưỡng khí sẽ rơi xuống từ hộc phía trên."),
  ("Put on your own mask before helping others.", "Hãy đeo mặt nạ cho mình trước khi giúp người khác."),
  ("The captain has turned on the seat belt sign.", "Cơ trưởng đã bật đèn báo thắt dây an toàn."),
  ("Please return to your seat. We are expecting some turbulence.", "Anh/chị vui lòng về chỗ. Chúng ta sắp gặp nhiễu động."),
  ("Cabin crew, please prepare for landing.", "Tổ tiếp viên, chuẩn bị hạ cánh."),
 ],
 "dialogues": [
  ("Can I go to the toilet? The seat belt sign is on.", [
    ("I'm sorry, we're in some turbulence right now. Please stay seated, and I'll let you know when the sign goes off.", True, "Xin lỗi + lý do an toàn + hứa báo lại."),
    ("No toilet now!", False, "Quát, cộc lốc; nên giải thích lý do và hứa báo lại."),
    ("Yes, go fast before the captain sees.", False, "Vi phạm an toàn bay — tuyệt đối không khuyến khích khách đứng dậy khi đèn còn bật."),
  ]),
  ("Why do I have to open the window shade?", [
    ("It's for safety. During take-off and landing, we need to see outside clearly in case of an emergency.", True, "Giải thích ngắn, dễ hiểu lý do an toàn."),
    ("Captain say open.", False, "Sai ngữ pháp ('The captain says…') và không giải thích lý do."),
    ("Because is the rule.", False, "Thiếu 'it' ('Because it's the rule') và không giải thích gì."),
  ]),
  ("My seat belt doesn't fit. It's too short.", [
    ("No problem. I'll bring you a seat belt extension right away.", True, "Trấn an + giải pháp cụ thể (dây nối dài)."),
    ("You pull it strong.", False, "Sai từ loại ('harder') và không giải quyết vấn đề."),
    ("Seat belt is normal size.", False, "Làm khách ngại, không đưa giải pháp."),
  ]),
  ("I'm scared. Is this turbulence dangerous?", [
    ("I understand. Turbulence is normal, and the aircraft is built for it. Just keep your seat belt fastened. I'm right here if you need me.", True, "Thông cảm + trấn an + hướng dẫn + ở bên khách."),
    ("Don't scared.", False, "Sai ngữ pháp: 'Don't be scared.' — và chưa trấn an đủ."),
    ("I don't know. Ask the captain.", False, "Làm khách sợ hơn; tiếp viên cần trấn an khách."),
  ]),
  ("Can I send just one message? We're still on the ground.", [
    ("I'm sorry, the doors are closed now, so please switch your phone to airplane mode. Thank you for understanding.", True, "Xin lỗi + lý do (đã đóng cửa) + cảm ơn."),
    ("OK, a quick one.", False, "Nhân nhượng vi phạm quy định an toàn."),
    ("Phone must off, rule.", False, "Thiếu động từ 'be' ('must be off') và nghe như ra lệnh."),
  ]),
 ],
 "listen": [
  ("Please fasten your seat belt", ["fasten", "belt"], "thắt dây an toàn"),
  ("Switch your phone to airplane mode", ["phone", "airplane"], "chế độ máy bay"),
  ("Your life jacket is under your seat", ["life", "under"], "áo phao"),
  ("Put your seat in the upright position", ["seat", "upright"], "dựng thẳng ghế"),
  ("Ladies and gentlemen, the captain has turned on the seat belt sign. We are expecting some turbulence. Please return to your seats and fasten your seat belts.", ["captain", "turbulence", "return"], "thông báo nhiễu động"),
  ("Cabin crew, please prepare for landing. Ladies and gentlemen, please put your seat in the upright position and open the window shade. Make sure your tray table is closed.", ["landing", "window", "closed"], "chuẩn bị hạ cánh"),
 ],
})

# ───────────────────────── 9. Hỗ trợ hành khách đặc biệt ─────────────────────────
PHASES.append({
 "title": "Hỗ trợ hành khách đặc biệt",
 "vocab": [
  ("wheelchair", "/ˈwiːltʃeə/", "n", "xe lăn", "A staff member will take you to the gate by <b>wheelchair</b>.", "Nhân viên sẽ đưa anh/chị ra cửa bằng xe lăn.", "車椅子", "kurumaisu"),
  ("special assistance", "/ˌspeʃl əˈsɪstəns/", "n", "dịch vụ hỗ trợ đặc biệt", "Did you request <b>special assistance</b> for this flight?", "Anh/chị có yêu cầu hỗ trợ đặc biệt cho chuyến bay này không?"),
  ("unaccompanied minor", "/ˌʌnəˌkʌmpənid ˈmaɪnə/", "n", "trẻ em đi máy bay một mình", "We have one <b>unaccompanied minor</b> on this flight.", "Chuyến bay này có một trẻ em đi một mình."),
  ("escort", "/ɪˈskɔːt/", "v", "đi kèm, dẫn (ai đó) đi", "A staff member will <b>escort</b> your daughter to the aircraft.", "Nhân viên sẽ đưa con gái anh/chị ra tận máy bay."),
  ("pregnant", "/ˈpreɡnənt/", "adj", "mang thai", "Since you are <b>pregnant</b>, let me check our policy for you.", "Vì chị đang mang thai, để tôi kiểm tra chính sách giúp chị.", "妊娠中", "ninshinchū"),
  ("infant", "/ˈɪnfənt/", "n", "em bé (còn bế trên tay)", "Are you travelling with an <b>infant</b>?", "Anh/chị có đi cùng em bé không ạ?", "幼児", "yōji"),
  ("medical certificate", "/ˈmedɪkl səˌtɪfɪkət/", "n", "giấy xác nhận của bác sĩ", "May I see your <b>medical certificate</b>, please?", "Cho tôi xem giấy xác nhận của bác sĩ được không ạ?", "診断書", "shindansho"),
  ("walking stick", "/ˈwɔːkɪŋ stɪk/", "n", "gậy chống", "You can keep your <b>walking stick</b> with you on board.", "Anh/chị có thể mang theo gậy chống lên máy bay.", "杖", "tsue"),
  ("stroller", "/ˈstrəʊlə/", "n", "xe đẩy em bé", "You can use your <b>stroller</b> up to the aircraft door.", "Anh/chị có thể dùng xe đẩy em bé đến tận cửa máy bay.", "ベビーカー", "bebīkā"),
  ("visually impaired", "/ˌvɪʒuəli ɪmˈpeəd/", "adj", "khiếm thị, nhìn kém", "The passenger in 5C is <b>visually impaired</b>.", "Hành khách ghế 5C bị khiếm thị."),
 ],
 "phrases": [
  ("Did you request wheelchair assistance?", "Anh/chị có yêu cầu hỗ trợ xe lăn không ạ?"),
  ("A staff member will take you to the gate by wheelchair.", "Nhân viên sẽ đưa anh/chị ra cửa bằng xe lăn."),
  ("Can you walk a few steps, or do you need help all the way to your seat?", "Anh/chị có đi được vài bước không, hay cần hỗ trợ đến tận ghế?"),
  ("You will board first, before the other passengers.", "Anh/chị sẽ lên máy bay trước các hành khách khác."),
  ("Please wait here. Someone will come to meet you in ten minutes.", "Anh/chị vui lòng đợi ở đây. Mười phút nữa sẽ có người đến đón."),
  ("Would you like me to guide you? You can hold my arm.", "Anh/chị có muốn tôi dẫn đường không? Anh/chị có thể khoác tay tôi."),
  ("Who will meet the child at the arrival airport?", "Ai sẽ đón cháu ở sân bay đến ạ?"),
  ("A staff member will stay with your son during the whole trip.", "Nhân viên sẽ ở cùng con trai anh/chị trong suốt chuyến đi."),
  ("May I see your medical certificate, please?", "Cho tôi xem giấy xác nhận của bác sĩ được không ạ?"),
  ("Please take your time. There's no hurry.", "Anh/chị cứ từ từ. Không cần vội đâu ạ."),
 ],
 "dialogues": [
  ("My mother can't walk very far. Can you help her?", [
    ("Of course. I'll arrange a wheelchair for her. A staff member will take her to the gate and help her board.", True, "Đồng ý + sắp xếp xe lăn + nói rõ ai giúp tới đâu."),
    ("She walk slowly, it's OK.", False, "Sai ngữ pháp ('walks') và không đáp ứng nhu cầu của khách."),
    ("Wheelchair must book before.", False, "Thiếu chủ ngữ, cứng nhắc; nên cố gắng sắp xếp ngay."),
  ]),
  ("I'm seven months pregnant. Is it OK for me to fly?", [
    ("Let me check our policy for you. We may need a medical certificate from your doctor. Do you have one with you?", True, "Không tự quyết — kiểm tra chính sách + hỏi giấy tờ cần thiết."),
    ("Yes, no problem, just fly.", False, "Hứa bừa khi chưa kiểm tra chính sách — có thể nguy hiểm cho khách."),
    ("Pregnant cannot fly.", False, "Thông tin sai, thiếu chủ ngữ và làm khách hoảng."),
  ]),
  ("This is my son. He's ten, and he's flying alone.", [
    ("Hello! We'll take good care of him. May I see the form, please? And who is meeting him at the arrival airport?", True, "Chào bé + trấn an + kiểm tra giấy tờ + hỏi người đón."),
    ("Child alone? Are you sure?", False, "Nghi ngờ phụ huynh, không làm thủ tục."),
    ("OK, he sit anywhere.", False, "Sai ngữ pháp ('he can sit') và bỏ qua quy trình với trẻ đi một mình."),
  ]),
  ("I can't see very well. Could someone help me to the gate?", [
    ("Of course. I'll take you there myself. You can hold my arm. There's an escalator in about ten metres.", True, "Tự dẫn đi + cách hỗ trợ + báo trước chướng ngại."),
    ("Gate is there. You go straight.", False, "Chỉ tay với người nhìn kém là vô ích; thiếu mạo từ 'The'."),
    ("Yes, I help you later.", False, "Thiếu 'will', 'later' mơ hồ; nên giúp ngay hoặc nói rõ thời gian."),
  ]),
  ("Can I take my baby's stroller to the gate?", [
    ("Yes, you can. I'll put a tag on it now, and you can leave it at the aircraft door.", True, "Cho phép + gắn thẻ + chỉ chỗ để xe."),
    ("Stroller go with baggage. Give me.", False, "Sai ngữ pháp và nghe như ra lệnh; nên giải thích lựa chọn."),
    ("No, you carry the baby.", False, "Từ chối cộc lốc, không đưa phương án."),
  ]),
 ],
 "listen": [
  ("A staff member will bring a wheelchair", ["staff", "wheelchair"], "xe lăn"),
  ("You will board before the other passengers", ["board", "before"], "lên máy bay trước"),
  ("Please wait here for the assistance team", ["wait", "assistance"], "chờ đội hỗ trợ"),
  ("Who will meet the child at arrival", ["meet", "child"], "trẻ đi một mình"),
  ("Good morning. I'm Hoa from the assistance team. I will take you to the gate by wheelchair, and you can board first.", ["assistance", "wheelchair", "first"], "đón khách xe lăn"),
  ("This is Minh at Gate eight. We have one unaccompanied minor on this flight. She is eleven years old, and her aunt will meet her in Sydney.", ["unaccompanied", "eleven", "aunt"], "bàn giao trẻ đi một mình"),
 ],
})

# ───────────────────────── 10. Hành lý thất lạc & hư hỏng ─────────────────────────
PHASES.append({
 "title": "Hành lý thất lạc & hư hỏng",
 "vocab": [
  ("baggage claim", "/ˈbæɡɪdʒ kleɪm/", "n", "khu nhận hành lý", "The <b>baggage claim</b> is downstairs, after passport control.", "Khu nhận hành lý ở tầng dưới, sau quầy kiểm soát hộ chiếu.", "手荷物受取所", "tenimotsu uketorijo"),
  ("carousel", "/ˌkærəˈsel/", "n", "băng chuyền hành lý", "Bags from the Seoul flight are on <b>carousel</b> 5.", "Hành lý chuyến từ Seoul ở băng chuyền số 5.", "ターンテーブル", "tāntēburu"),
  ("missing", "/ˈmɪsɪŋ/", "adj", "bị thiếu, không thấy đâu", "One of my bags is <b>missing</b>.", "Một túi của tôi không thấy đâu."),
  ("lost and found", "/ˌlɒst ən ˈfaʊnd/", "n", "bộ phận giữ đồ thất lạc", "Please ask at <b>lost and found</b> on the first floor.", "Anh/chị vui lòng hỏi ở bộ phận giữ đồ thất lạc tầng một.", "遺失物取扱所", "ishitsubutsu toriatsukaijo"),
  ("PIR", "/ˌpiː aɪ ˈɑː/", "n", "biên bản bất thường hành lý (Property Irregularity Report)", "Let's fill in a <b>PIR</b> for your missing bag.", "Mình cùng làm biên bản bất thường cho túi bị thiếu của anh/chị nhé."),
  ("claim tag", "/ˈkleɪm tæɡ/", "n", "cuống thẻ hành lý", "May I see your baggage <b>claim tag</b>?", "Cho tôi xem cuống thẻ hành lý của anh/chị được không?", "手荷物引換証", "tenimotsu hikikaeshō"),
  ("damaged", "/ˈdæmɪdʒd/", "adj", "bị hư hỏng", "My suitcase was <b>damaged</b> during the flight.", "Vali của tôi bị hỏng trong chuyến bay.", "破損した", "hason shita"),
  ("describe", "/dɪˈskraɪb/", "v", "mô tả", "Could you <b>describe</b> your bag, please?", "Anh/chị mô tả chiếc túi giúp tôi được không?"),
  ("deliver", "/dɪˈlɪvə/", "v", "giao (đến tận nơi)", "We'll <b>deliver</b> your bag to your hotel.", "Chúng tôi sẽ giao túi đến khách sạn của anh/chị.", "配送する", "haisō suru"),
  ("reference number", "/ˈrefrəns ˌnʌmbə/", "n", "mã số hồ sơ", "Please keep this <b>reference number</b> to track your bag.", "Anh/chị giữ mã số hồ sơ này để theo dõi hành lý."),
 ],
 "phrases": [
  ("I'm sorry your bag didn't arrive. Let's fill in a report together.", "Rất tiếc hành lý của anh/chị chưa đến. Mình cùng làm biên bản nhé."),
  ("May I see your boarding pass and your baggage claim tag?", "Cho tôi xem thẻ lên máy bay và cuống thẻ hành lý của anh/chị được không?"),
  ("Could you describe your bag? What colour and size is it?", "Anh/chị mô tả chiếc túi được không? Màu gì và cỡ nào ạ?"),
  ("Does it have a name tag or any stickers on it?", "Túi có thẻ tên hay nhãn dán gì không ạ?"),
  ("Your bag is still in Bangkok. It will arrive on tonight's flight.", "Túi của anh/chị vẫn ở Bangkok. Túi sẽ đến trên chuyến bay tối nay."),
  ("We'll deliver it to your hotel as soon as it arrives.", "Chúng tôi sẽ giao túi đến khách sạn ngay khi túi tới."),
  ("Here is your reference number. You can track your bag online.", "Đây là mã số hồ sơ. Anh/chị có thể theo dõi hành lý trực tuyến."),
  ("I'm sorry the handle is broken. Let me take some photos for the report.", "Rất tiếc tay cầm bị gãy. Để tôi chụp vài tấm ảnh cho biên bản."),
  ("Please keep your receipts. Our team will tell you what can be paid back.", "Anh/chị vui lòng giữ hoá đơn. Bộ phận chúng tôi sẽ báo khoản nào được hoàn lại."),
  ("Lost and found is on the first floor, next to the information desk.", "Bộ phận giữ đồ thất lạc ở tầng một, cạnh quầy thông tin."),
 ],
 "dialogues": [
  ("My suitcase didn't come out on the carousel.", [
    ("I'm very sorry. May I see your claim tag? I'll check where your bag is right now.", True, "Xin lỗi + xin cuống thẻ + kiểm tra ngay."),
    ("Suitcase lost, sorry.", False, "Kết luận 'mất' khi chưa kiểm tra, thiếu động từ — khách sẽ hoảng."),
    ("You check other carousel.", False, "Thiếu mạo từ và đẩy việc cho khách; nên tự kiểm tra hệ thống."),
  ]),
  ("Look! One wheel of my suitcase is broken.", [
    ("I'm sorry about that. Let me take a photo and fill in a damage report. Our team will contact you about a repair.", True, "Xin lỗi + ghi nhận bằng ảnh và biên bản + bước tiếp theo."),
    ("Wheels break easy, it's normal.", False, "Coi nhẹ vấn đề, sai từ loại ('easily')."),
    ("Not our fault. The bag is old.", False, "Đổ lỗi khi chưa kiểm tra — thiếu chuyên nghiệp."),
  ]),
  ("When will I get my bag back?", [
    ("It's on the next flight, which lands at 9 tonight. We'll deliver it to your hotel by tomorrow morning.", True, "Túi đang ở đâu + giờ đến + giao lúc nào."),
    ("Maybe tomorrow, maybe next week.", False, "Mơ hồ, khách không biết lên kế hoạch thế nào."),
    ("You come back airport tomorrow.", False, "Thiếu 'to the', nghe như ra lệnh; thường hãng giao tận nơi — nên nói rõ."),
  ]),
  ("I left my jacket on the plane.", [
    ("Let me call the cabin crew to check the aircraft. Which seat were you in?", True, "Hành động ngay + hỏi số ghế để tìm."),
    ("The plane is gone already.", False, "Kết luận vội khi chưa kiểm tra."),
    ("Why you forget?", False, "Trách khách và sai ngữ pháp ('Why did you forget it?')."),
  ]),
  ("Can I buy some clothes? I have a meeting tomorrow.", [
    ("I understand. Please keep your receipts and add them to your claim. Our team will tell you what can be paid back.", True, "Thông cảm + hướng dẫn giữ hoá đơn, không hứa chắc số tiền."),
    ("Yes, buy anything. We pay all.", False, "Hứa bừa thay công ty — có thể sai chính sách."),
    ("Clothes is your problem.", False, "Sai ngữ pháp ('are') và rất thiếu thiện chí."),
  ]),
 ],
 "listen": [
  ("Please show me your baggage claim tag", ["claim", "tag"], "xin cuống thẻ"),
  ("Could you describe your bag", ["describe", "bag"], "mô tả túi"),
  ("We will deliver it to your hotel", ["deliver", "hotel"], "giao hành lý"),
  ("Here is your reference number", ["reference", "number"], "mã số hồ sơ"),
  ("I'm sorry, your bag is still in Bangkok. It will arrive on tonight's flight. We will deliver it to your hotel tomorrow morning.", ["Bangkok", "tonight's", "deliver"], "báo hành lý đến chậm"),
  ("Hi, this is baggage services. We found your blue suitcase. It is at the lost and found office on the first floor, and it is open until ten tonight.", ["blue", "lost", "ten"], "gọi báo tìm thấy hành lý"),
 ],
})

# ───────────────────────── Vai trong ngành ─────────────────────────
ROLES = {
 "checkin": {"label": "Check-in · Quầy vé", "emoji": "🎫",
  "scenarios": [
   ("ci_heavy", "Hành lý quá cân", "You are a passenger at the check-in counter. Your suitcase is five kilos over your allowance. Ask what you can do, complain a little about the fee, then decide."),
   ("ci_visa", "Thiếu giấy tờ", "You are a passenger flying abroad, but you can't find your visa on your phone. Ask me what you can do and whether you can still check in."),
   ("ci_family", "Gia đình muốn ngồi cạnh nhau", "You are a parent travelling with two young children, and your seats are not together. Ask me to seat your family together and ask about priority boarding."),
   ("ci_late", "Đến quầy muộn", "You are a passenger who arrives at the check-in counter 40 minutes before departure, and the counter is closing. Ask me to help you get on the flight."),
  ],
  "dialogues": [
   ("Hi, I'd like to check in for the flight to Seoul.", [
     ("Of course. May I see your passport, please? Are you checking in any bags today?", True, "Nhận khách + xin hộ chiếu + hỏi hành lý."),
     ("Passport.", False, "Một từ, như ra lệnh; nên nói 'May I see your passport, please?'"),
     ("Yes, Seoul. You have ticket?", False, "Thiếu 'Do' và 'a'; lại không cần vé in — hộ chiếu là đủ.")]),
   ("How many carry-on bags can I take?", [
     ("Let me check your ticket. You can take one carry-on bag and one small personal item, like a handbag.", True, "Kiểm tra theo vé của khách + ví dụ cụ thể."),
     ("Two bag no.", False, "Nói kiểu từng chữ, thiếu 's'; khách không hiểu được bao nhiêu."),
     ("Take as many as you like.", False, "Sai — hạn mức tuỳ vé; khách có thể bị chặn ở cửa.")]),
   ("My name is spelled wrong on the ticket.", [
     ("Let me check. It's only one letter, so I'll ask my supervisor if we can correct it here.", True, "Kiểm tra + hỏi cấp trên, không tự quyết."),
     ("Name wrong, cannot fly.", False, "Kết luận vội, thiếu động từ, làm khách hoảng."),
     ("No problem, nobody checks.", False, "Sai và thiếu trách nhiệm — tên phải khớp giấy tờ.")]),
   ("Can I pay the excess baggage fee by card?", [
     ("Yes, you can pay by card or in cash at the ticket desk. It's just next to counter 20.", True, "Trả lời + nơi thanh toán cụ thể."),
     ("Yes, card can.", False, "Sai trật tự từ: 'Yes, you can pay by card.'"),
     ("Only cash. Go to the ATM.", False, "Khẳng định khi chưa chắc và nghe cộc.")]),
   ("I'm a frequent flyer member. Can I use the lounge?", [
     ("Let me check your membership level... Yes, you can. The lounge is on the third floor, after passport control.", True, "Kiểm tra hạng thẻ + vị trí phòng chờ."),
     ("Lounge is for business class only.", False, "Trả lời khi chưa kiểm tra quyền lợi của khách."),
     ("Yes, you go lounge.", False, "Thiếu 'can' và 'to the': 'Yes, you can go to the lounge.'")]),
   ("Is the flight on time?", [
     ("Yes, it's on time at the moment. Boarding starts at 2:15 at Gate 11.", True, "Trạng thái + giờ lên máy bay + cửa."),
     ("On time, I think.", False, "Không chắc chắn; nên kiểm tra và báo thông tin cụ thể."),
     ("Yes, time is OK.", False, "Dịch từng chữ 'giờ ổn'; nên nói 'It's on time.'")]),
  ]},
 "gate": {"label": "Cửa ra máy bay", "emoji": "🛫",
  "scenarios": [
   ("gt_late", "Khách đến khi cửa đã đóng", "You are a passenger who arrives at the gate two minutes after it closed. You are upset because you have an important meeting. Ask me to let you board."),
   ("gt_bag", "Hành lý xách tay quá lớn", "You are a passenger at the gate with a big carry-on bag. I tell you it must go in the hold. Ask why, and ask about the laptop inside."),
   ("gt_delay", "Hỏi thông tin chậm chuyến", "You are a passenger waiting at the gate. The flight is delayed and there is no information. Ask me why, how long, and whether you will miss your connection."),
   ("gt_volunteer", "Khách tình nguyện đổi chuyến", "The flight is overbooked and you are thinking about taking a later flight. Ask me when the next flight is and what the airline will offer you."),
  ],
  "dialogues": [
   ("Can I board now? I'm in row 35.", [
     ("Yes, rows 30 to 45 are boarding now. May I see your boarding pass and passport, please?", True, "Xác nhận nhóm đang lên + xin giấy tờ."),
     ("Row 35 go.", False, "Thiếu động từ đúng: 'Row 35 can board now.'"),
     ("Wait, wait.", False, "Cộc, không giải thích — mà hàng 35 đang được mời lên.")]),
   ("I'm on standby. Is there a seat for me?", [
     ("Let me check. Yes, we have one seat left. Here is your new boarding pass, seat 41B.", True, "Kiểm tra + báo kết quả + đưa thẻ lên máy bay mới."),
     ("Maybe. You wait and see.", False, "Mơ hồ; nên kiểm tra và báo khi nào có kết quả."),
     ("Standby no seat.", False, "Thiếu động từ; dù hết ghế cũng cần xin lỗi và nói phương án.")]),
   ("Where can I charge my phone?", [
     ("There are charging points under the seats by the window, next to Gate 8.", True, "Chỉ chỗ cụ thể."),
     ("Charge at home.", False, "Vô lý và thiếu lịch sự."),
     ("I don't know. You find it.", False, "Đẩy việc cho khách.")]),
   ("Do I have time to buy a coffee?", [
     ("Yes, boarding starts in 25 minutes. There's a café just behind you, but please be back by 3:10.", True, "Thời gian còn lại + chỗ mua + giờ phải quay lại."),
     ("Coffee is on the plane.", False, "Không trả lời khách có kịp hay không."),
     ("No time, never.", False, "Sai và cộc; còn 25 phút là đủ.")]),
   ("Which boarding group am I in?", [
     ("You're in group 3. We'll call your group in about ten minutes.", True, "Nói nhóm + khi nào được gọi."),
     ("Group three, you see.", False, "Cụt lủn, 'you see' không tự nhiên ở đây."),
     ("You are in group, wait.", False, "Thiếu số nhóm và mạo từ — khách vẫn không biết.")]),
   ("The flight is delayed. Will I miss my connection in Tokyo?", [
     ("Let me check your booking. You'll still have 50 minutes in Tokyo. I'll inform the transfer team, and if you miss it, we'll rebook you.", True, "Kiểm tra + thời gian nối còn lại + phương án dự phòng."),
     ("Maybe miss, sorry.", False, "Thiếu chủ ngữ và 'will', không có phương án."),
     ("Tokyo is not my problem.", False, "Đẩy trách nhiệm, rất thiếu chuyên nghiệp.")]),
  ]},
 "cabin": {"label": "Tiếp viên", "emoji": "💺",
  "scenarios": [
   ("cb_seat", "Khách ngồi nhầm ghế", "You are a passenger sitting in the wrong seat on the plane. You don't want to move because you like the window. Talk to me, the flight attendant."),
   ("cb_meal", "Phục vụ suất ăn", "You are a passenger during meal service. The meal you want is finished, and you have a food allergy. Ask me about other choices."),
   ("cb_sick", "Khách không khoẻ", "You are a passenger who feels sick and dizzy during the flight. Tell me how you feel and ask for help."),
   ("cb_noise", "Khách phàn nàn người bên cạnh", "You are a passenger who can't sleep because the passenger next to you is very loud. Ask me to help you or to change your seat."),
  ],
  "dialogues": [
   ("Excuse me, I think someone is in my seat.", [
     ("Let me check your boarding pass. Yes, 18C is your seat. I'll speak to the passenger for you.", True, "Kiểm tra + xác nhận + tiếp viên tự nói chuyện với khách kia."),
     ("You sit other seat, same same.", False, "Thiếu 'in another', 'same same' là kiểu nói bồi; nên giúp khách về đúng ghế."),
     ("Your problem, you tell him.", False, "Đẩy việc cho khách, dễ gây cãi nhau.")]),
   ("Can I have some water, please?", [
     ("Of course. Would you like it with ice or without?", True, "Đồng ý + hỏi thêm lựa chọn."),
     ("Water later.", False, "Cụt, không nói khi nào."),
     ("Yes, water is free.", False, "Không cần nói miễn phí; nên đáp 'Of course' và mang nước.")]),
   ("I don't feel well. I think I'm going to be sick.", [
     ("I'm sorry to hear that. Here's a sickness bag. Would you like some water? I'll check on you in a few minutes.", True, "Cảm thông + giúp ngay + hẹn quay lại kiểm tra."),
     ("Close your eyes and sleep.", False, "Coi nhẹ tình trạng của khách."),
     ("You eat too much?", False, "Thiếu 'Did', câu hỏi thiếu tế nhị.")]),
   ("Can I move to the empty row at the back?", [
     ("Please stay in your seat for take-off. After the seat belt sign goes off, I'll check and let you know.", True, "Giữ an toàn khi cất cánh + hứa kiểm tra sau."),
     ("OK, go now.", False, "Cho đổi chỗ trước khi cất cánh — ảnh hưởng an toàn và cân bằng tải."),
     ("No change, never.", False, "Cứng nhắc, không giải thích.")]),
   ("Is there any vegetarian food left?", [
     ("I'm sorry, the vegetarian meals are finished. I can bring you bread, salad and some fruit. Would that be OK?", True, "Xin lỗi + phương án thay thế + hỏi ý khách."),
     ("No vegetarian. You eat chicken.", False, "Ép khách ăn món không phù hợp — rất thiếu tôn trọng."),
     ("Vegetable finish.", False, "Dịch từng chữ 'hết rau'; 'vegetable' là rau, món chay là 'vegetarian meal'.")]),
   ("The man next to me is drunk and very loud.", [
     ("Thank you for telling me. I'll speak to him now. If you like, I can also find you another seat.", True, "Cảm ơn + xử lý + đưa thêm lựa chọn."),
     ("He is happy, it's OK.", False, "Bỏ qua phàn nàn của khách."),
     ("You tell him quiet.", False, "Đẩy việc cho khách và sai ngữ pháp ('to be quiet').")]),
  ]},
 "baggage": {"label": "Hành lý · Thất lạc", "emoji": "🧳",
  "scenarios": [
   ("bg_lost", "Hành lý không đến", "You are a passenger at the baggage services desk. Your suitcase did not arrive. Describe it and ask when and how you will get it back."),
   ("bg_damage", "Vali bị hỏng", "You are a passenger whose suitcase arrived with a broken handle and a crack. Complain politely and ask what the airline will do."),
   ("bg_item", "Quên đồ trên máy bay", "You are a passenger who left a tablet in the seat pocket on the plane. Ask me how to get it back before you leave the airport."),
   ("bg_call", "Gọi hỏi tình trạng hành lý", "You are a passenger calling baggage services on the second day because your bag has still not arrived. Ask for an update, and be a little frustrated."),
  ],
  "dialogues": [
   ("Where is the baggage claim for the flight from Seoul?", [
     ("It's carousel 5. Go down the stairs, and it's on your right.", True, "Số băng chuyền + chỉ đường."),
     ("Carousel, you look screen.", False, "Cụt, thiếu 'at the'; nên nói số băng chuyền luôn."),
     ("Baggage come later.", False, "Sai ngữ pháp ('comes') và không trả lời câu hỏi.")]),
   ("My bag is the last one missing. Everyone else has theirs.", [
     ("I'm sorry. Let me check the system with your tag number. If it's not here, I'll help you fill in a report.", True, "Xin lỗi + kiểm tra + bước tiếp theo."),
     ("Maybe somebody take it.", False, "Đoán mò làm khách lo; sai thì ('took')."),
     ("Wait one more hour.", False, "Băng chuyền đã hết hành lý — bắt khách chờ vô ích.")]),
   ("How will you find my bag?", [
     ("We'll send your bag details to all the airports on your route. The system will look for your tag number.", True, "Giải thích quy trình tìm kiếm rõ ràng."),
     ("We try, but maybe no.", False, "Thiếu 'will', nghe bi quan, khách mất niềm tin."),
     ("You call every airport.", False, "Đẩy việc cho khách — đây là việc của hãng.")]),
   ("Do I have to come back to the airport to pick it up?", [
     ("No, you don't. We'll deliver it to your hotel or home. Could you write the address here, please?", True, "Trả lời rõ + xin địa chỉ giao."),
     ("Yes, come airport again.", False, "Thiếu 'to the', cộc; nên kiểm tra và đề nghị giao tận nơi."),
     ("Up to you.", False, "Không trả lời, khách không biết làm gì.")]),
   ("My bag was damaged. Who will pay for it?", [
     ("I'm sorry. Let me write a damage report. Our claims team will contact you about a repair or other options.", True, "Xin lỗi + lập biên bản + ai sẽ liên hệ, không hứa bừa."),
     ("Airline pay all, no problem.", False, "Hứa bừa thay công ty và sai ngữ pháp ('The airline will pay')."),
     ("Bags break every day. Normal.", False, "Coi nhẹ thiệt hại của khách.")]),
   ("This suitcase looks like mine, but it's not! Someone took my bag by mistake.", [
     ("Thank you for telling us. Let me check the name tag on this bag. We'll contact the other passenger and get your bag back.", True, "Cảm ơn + kiểm tra + liên hệ khách cầm nhầm."),
     ("Take this one. Same colour.", False, "Rất sai — không được đưa hành lý của người khác."),
     ("Not our problem. Call the police.", False, "Đẩy trách nhiệm; hãng có thể liên hệ khách cầm nhầm.")]),
  ]},
}

PACK = {
 "id": "aviation",
 "label": "Hàng không · Sân bay",
 "short": "Hàng không",
 "emoji": "✈️",
 "desc": "Check-in · cửa ra máy bay · tiếp viên · hành lý",
 "persona": "a Vietnamese airline and airport staff member",
 "counterpart": "an international passenger",
 "context": "airline and airport operations",
 "core": [10, 11],
 "report": {
  "title": "Bàn giao ca 60 giây", "short": "Bàn giao ca", "sub": "Nói như lúc bàn giao ca ✈️",
  "steps": [["Flights", "In my shift, we handled … flights …"], ["Issues", "Flight … was delayed because … / No issues."], ["Notes", "Please call … / Nothing pending."]],
  "kind": "shift handover report",
  "structure": "flights handled / issues / notes for the next shift",
  "sample": "In my shift, we handled eight flights and checked in about 1,200 passengers. Flight 320 to Hanoi was delayed two hours because of bad weather, and we gave meal vouchers to all passengers. One bag from the Seoul flight is still missing. Please call the passenger at 9 a.m. with an update.",
 },
 "podcast": "Podcast sân bay",
 "game_tag": "Game anime: đánh quái vali quá cân, hạ boss khách lỡ chuyến",
 "reverse_tag": "kiểu hàng không",
 "jd_placeholder": "VD: Nhân viên check-in ở sân bay quốc tế TP.HCM, khách Hàn/Nhật/Úc, hành lý quá cân, chậm chuyến, hỗ trợ xe lăn…",
 "rw_placeholder": "VD: chuyến bay chậm 3 tiếng, khách nối chuyến đi Tokyo sợ lỡ chuyến",
 "quips": [
  "Boarding pass, please!",
  "Window or aisle?",
  "Bag on the scale, please!",
  "Fasten your seat belt!",
  "Final call for Mochi!",
  "Gate change: Gate 7!",
  "Chicken or fish?",
  "Please stay seated!",
  "Ready for take-off!",
  "Have a nice flight!",
 ],
 "ai": [
  ("checkin", "Làm thủ tục check-in", "You are an international passenger at the check-in counter. I am the check-in agent. Give me your passport, ask for a window seat and ask what time boarding starts."),
  ("baggage", "Hành lý quá cân", "You are a passenger whose checked bag is four kilos overweight. Ask me why, what your options are and how much you have to pay. Be a little unhappy."),
  ("delay", "Chuyến bay bị chậm", "You are a passenger at the gate. Your flight is delayed by three hours. Ask me why, when the new departure time is and whether you can get something to eat."),
  ("cancel", "Huỷ chuyến & đặt lại", "You are a passenger whose flight was cancelled because of a storm. Ask me about the next flight, a hotel for tonight and compensation."),
  ("connection", "Lỡ chuyến nối", "You are a transit passenger who missed your connecting flight because the first flight was late. Ask me to rebook you and ask about your checked bag."),
  ("lost", "Thất lạc hành lý", "You are a passenger at baggage services. Your suitcase did not arrive. Describe your bag and ask when it will be delivered to your hotel."),
  ("cabin", "Phục vụ trên máy bay", "You are a passenger on a long flight. I am the flight attendant. Ask for a drink and a blanket, ask about the meal choices and ask how to fill in the arrival card."),
  ("assist", "Hỗ trợ hành khách đặc biệt", "You are travelling with your elderly father, who can't walk far. Ask me for a wheelchair, priority boarding and help at the arrival airport."),
 ],
 "rev": [
  ("Hôm nay anh/chị bay đi đâu ạ?", "Where are you flying to today?"),
  ("Cho tôi xem hộ chiếu của anh/chị được không?", "May I see your passport, please?"),
  ("Túi của anh/chị bị quá ba ký.", "Your bag is three kilos overweight."),
  ("Anh/chị muốn ghế cửa sổ hay ghế lối đi?", "Would you like a window or an aisle seat?"),
  ("Giờ lên máy bay là 9 giờ 15 ở cửa số 12.", "Boarding is at 9:15 at Gate 12."),
  ("Vui lòng lấy máy tính xách tay ra khỏi túi.", "Please take your laptop out of your bag."),
  ("Chuyến bay bị chậm khoảng hai tiếng.", "The flight is delayed by about two hours."),
  ("Tôi e là chuyến bay đã bị huỷ.", "I'm afraid the flight has been cancelled."),
  ("Tôi sẽ đặt chỗ cho anh/chị trên chuyến bay kế tiếp.", "I'll book you on the next flight."),
  ("Vui lòng thắt dây an toàn.", "Please fasten your seat belt."),
  ("Anh/chị muốn uống gì ạ?", "What would you like to drink?"),
  ("Nhân viên sẽ đưa anh/chị ra cửa bằng xe lăn.", "A staff member will take you to the gate by wheelchair."),
  ("Anh/chị mô tả chiếc túi giúp tôi được không?", "Could you describe your bag, please?"),
  ("Chúng tôi sẽ giao hành lý đến khách sạn của anh/chị.", "We'll deliver your bag to your hotel."),
 ],
 "reading": [
  {"t": "Departures screen", "text": "DEPARTURES\n10:15  Singapore  Gate 7   Boarding\n10:40  Tokyo      Gate 12  Delayed – new time 12:20\n11:05  Seoul      Gate 21  Gate change (was Gate 9)\n11:30  Bangkok    –        Cancelled – please go to the customer service desk", "q": [
    {"q": "What is the new departure time for Tokyo?", "o": ["10:40", "12:20", "11:05"], "a": 1},
    {"q": "What should passengers to Bangkok do?", "o": ["Go to Gate 21", "Wait at Gate 7", "Go to the customer service desk"], "a": 2}]},
  {"t": "Check-in notice", "text": "CHECKED BAGGAGE – PLEASE READ\n• Your baggage allowance is printed on your ticket.\n• Power banks and spare batteries must stay in your carry-on.\n• Please tell our staff if your bag has fragile items inside.\n• Excess baggage fees are shown at the ticket desk.", "q": [
    {"q": "Where must power banks go?", "o": ["In checked baggage", "In your carry-on", "At the ticket desk"], "a": 1},
    {"q": "Where can passengers see excess baggage fees?", "o": ["On the ticket", "At the ticket desk", "On the plane"], "a": 1}]},
  {"t": "Gate chat", "text": "Tuấn (Gate 7): Flight 215 – 184 of 186 passengers are on board. Two are still at security. I've called their names twice. Ramp, please don't close the hold yet. I'll confirm in 5 minutes.", "q": [
    {"q": "How many passengers are not on board yet?", "o": ["Two", "Four", "186"], "a": 0},
    {"q": "What does Tuấn ask the ramp team to do?", "o": ["Close the hold now", "Wait before closing the hold", "Call the passengers"], "a": 1}]},
  {"t": "Delay message", "text": "Dear passenger,\nWe're sorry. Flight 680 to Osaka on 12 May is delayed because of a technical issue. The new departure time is 18:30. Please show this message at the gate to get a meal voucher. Check-in closes at 17:30.", "q": [
    {"q": "Why is the flight delayed?", "o": ["Bad weather", "A technical issue", "A gate change"], "a": 1},
    {"q": "What can passengers get at the gate?", "o": ["A hotel room", "A new ticket", "A meal voucher"], "a": 2}]},
  {"t": "Baggage report (PIR)", "text": "PROPERTY IRREGULARITY REPORT\nReference number: 48213\nPassenger: Ms. Laura Bianchi\nFlight: from Paris via Bangkok\nBag: large grey suitcase, hard shell, green ribbon on the handle\nDelivery address: Lotus Hotel, room 305\nStatus: bag found in Bangkok, arriving tonight", "q": [
    {"q": "Where is the bag now?", "o": ["In Paris", "In Bangkok", "At the hotel"], "a": 1},
    {"q": "How can staff recognise the bag?", "o": ["It is small and black", "It has a green ribbon", "It has a red name tag"], "a": 1}]},
 ],
 "events": [
  ("peak", "Mùa cao điểm Tết", "You are a passenger flying home for Tết. The airport is very crowded and your flight is full. Ask me about check-in times, baggage and what to do if the flight is delayed."),
  ("storm", "Bão – huỷ nhiều chuyến", "You are an upset passenger. A storm has cancelled many flights today, including yours. Ask me about the next flight, a hotel for tonight and your connecting flight."),
  ("group", "Đoàn khách làm thủ tục", "You are the leader of a tour group of 25 passengers checking in together. Ask me about group check-in, seats together and special meals."),
  ("audit", "Đoàn kiểm tra an toàn", "You are a safety auditor visiting our ground team tomorrow. Ask me how we check baggage, count passengers before departure and report problems."),
  ("interview", "Phỏng vấn tiếp viên / nhân viên mặt đất", "You are the HR manager of an airline interviewing me for a cabin crew or ground staff job. Ask about my experience, my English and how I would handle an angry passenger."),
  ("training", "Huấn luyện tình huống khẩn cấp", "You are a trainer running an emergency training session. Ask me to explain the safety demo, the emergency exits and what I would say to calm passengers."),
  ("other", "Khác", ""),
 ],
 "roles": ROLES,
 "phases": PHASES,
}
