# -*- coding: utf-8 -*-
# Gói "hotel" — Khách sạn · Du lịch: lễ tân, nhà hàng – bar, buồng phòng, hướng dẫn viên
# phục vụ khách nước ngoài tại Việt Nam. Chặng lõi lấy từ office: 11 (Phỏng vấn), 10 (Nghỉ phép & hành chính).
# Schema: xem packs_src/README.md. Build: python3 packs_src/build.py hotel

PHASES = []

# ───────────────────────── 1. Lễ tân – nhận phòng ─────────────────────────
PHASES.append({
 "title": "Lễ tân – nhận phòng",
 "vocab": [
  ("reservation", "/ˌrezəˈveɪʃn/", "n", "sự đặt phòng trước", "Do you have a <b>reservation</b> with us?", "Anh/chị có đặt phòng trước với khách sạn không ạ?", "予約", "yoyaku"),
  ("check in", "/ˌtʃek ˈɪn/", "v", "nhận phòng, làm thủ tục vào", "You can <b>check in</b> from 2 p.m.", "Anh/chị có thể nhận phòng từ 2 giờ chiều.", "チェックイン", "chekkuin"),
  ("front desk", "/ˌfrʌnt ˈdesk/", "n", "quầy lễ tân", "Please leave your key at the <b>front desk</b>.", "Anh/chị vui lòng gửi chìa khoá ở quầy lễ tân.", "フロント", "furonto"),
  ("passport", "/ˈpɑːspɔːt/", "n", "hộ chiếu", "May I see your <b>passport</b>, please?", "Cho tôi xem hộ chiếu của anh/chị được không ạ?", "パスポート", "pasupōto"),
  ("key card", "/ˈkiː kɑːd/", "n", "thẻ phòng (thẻ từ)", "Here is your <b>key card</b>. You're in room 508.", "Đây là thẻ phòng của anh/chị. Anh/chị ở phòng 508.", "カードキー", "kādo kī"),
  ("deposit", "/dɪˈpɒzɪt/", "n", "tiền đặt cọc", "We need a <b>deposit</b> of two million dong.", "Khách sạn cần khoản đặt cọc hai triệu đồng.", "デポジット", "depojitto"),
  ("lobby", "/ˈlɒbi/", "n", "sảnh khách sạn", "Your driver is waiting in the <b>lobby</b>.", "Tài xế đang đợi anh/chị ở sảnh.", "ロビー", "robī"),
  ("luggage", "/ˈlʌɡɪdʒ/", "n", "hành lý", "The porter will take your <b>luggage</b> to your room.", "Nhân viên hành lý sẽ mang hành lý lên phòng cho anh/chị.", "荷物", "nimotsu"),
  ("upgrade", "/ˌʌpˈɡreɪd/", "v", "nâng hạng (phòng)", "We can <b>upgrade</b> you to a bigger room for free.", "Chúng tôi có thể nâng hạng miễn phí lên phòng rộng hơn cho anh/chị.", "アップグレード", "appugurēdo"),
  ("complimentary", "/ˌkɒmplɪˈmentri/", "adj", "miễn phí (khách sạn tặng)", "Wi-Fi and breakfast are <b>complimentary</b>.", "Wi-Fi và bữa sáng được miễn phí.", "無料", "muryō"),
 ],
 "phrases": [
  ("Good afternoon. Welcome to Hoa Sen Hotel.", "Chào buổi chiều. Chào mừng anh/chị đến khách sạn Hoa Sen."),
  ("Do you have a reservation?", "Anh/chị có đặt phòng trước không ạ?"),
  ("May I have your name, please?", "Cho tôi xin tên của anh/chị ạ."),
  ("Could I see your passport, please?", "Cho tôi xem hộ chiếu của anh/chị được không ạ?"),
  ("Could you fill in this form and sign here, please?", "Anh/chị điền phiếu này và ký vào đây giúp tôi nhé."),
  ("Your room is on the fifth floor. The lift is on your right.", "Phòng của anh/chị ở tầng năm. Thang máy ở bên phải ạ."),
  ("Breakfast is served from 6 to 10 on the second floor.", "Bữa sáng phục vụ từ 6 đến 10 giờ ở tầng hai."),
  ("The Wi-Fi password is on your key card holder.", "Mật khẩu Wi-Fi ghi trên bìa đựng thẻ phòng."),
  ("Would you like some help with your luggage?", "Anh/chị có cần giúp mang hành lý không ạ?"),
  ("Enjoy your stay!", "Chúc anh/chị có kỳ nghỉ vui vẻ!"),
 ],
 "dialogues": [
  ("Hi, I have a reservation under the name Smith.", [
    ("Welcome, Mr. Smith. Yes, a double room for three nights. May I see your passport, please?", True, "Chào + xác nhận đặt phòng + xin hộ chiếu lịch sự."),
    ("OK. Passport.", False, "Cộc lốc như ra lệnh; nên nói 'May I see your passport, please?'"),
    ("Yes, you have reservation Smith.", False, "Lặp lại từng chữ, thiếu 'a'; nên xác nhận loại phòng, số đêm rồi làm thủ tục."),
  ]),
  ("Is breakfast included?", [
    ("Yes, it is. Breakfast is from 6 to 10 in the restaurant on the ground floor.", True, "Trả lời có/không + giờ và địa điểm."),
    ("Yes, include.", False, "Thiếu chủ ngữ và dạng bị động: 'Yes, it's included.'"),
    ("Breakfast is very delicious.", False, "Không trả lời câu hỏi có bao gồm hay không."),
  ]),
  ("Can I check in now? It's only eleven.", [
    ("I'm sorry, your room isn't ready yet. Check-in is at two, but we can keep your luggage and call you when it's ready.", True, "Xin lỗi + giờ nhận phòng + đưa phương án giữ hành lý."),
    ("No. Two o'clock.", False, "Quá cộc; nên xin lỗi và đưa phương án cho khách."),
    ("Sorry, the room still not clean.", False, "Thiếu động từ 'is' và nghe không chuyên nghiệp: 'Your room isn't ready yet.'"),
  ]),
  ("Why do you need a deposit?", [
    ("It's for any extra charges, like the minibar. We'll return it when you check out.", True, "Giải thích lý do + khi nào hoàn lại."),
    ("Because is the rule.", False, "Thiếu chủ ngữ 'it' và không giải thích gì: 'It's hotel policy — it covers extra charges.'"),
    ("You pay deposit, after we give back.", False, "Dịch từng chữ, thiếu mạo từ và thì: 'We'll return it when you check out.'"),
  ]),
  ("What's the Wi-Fi password?", [
    ("It's 'hoasen2026'. It's also written on your key card holder.", True, "Nói mật khẩu + chỉ chỗ ghi sẵn."),
    ("Password on the paper, you read.", False, "Thiếu động từ 'is', nghe như ra lệnh cho khách."),
    ("The Wi-Fi is free.", False, "Không trả lời câu hỏi về mật khẩu."),
  ]),
 ],
 "listen": [
  ("Do you have a reservation with us", ["have", "reservation"], "hỏi đặt phòng"),
  ("Could I see your passport, please", ["see", "passport"], "xin hộ chiếu"),
  ("Your room is on the seventh floor", ["room", "seventh"], "phòng ở tầng mấy"),
  ("Breakfast is included in your room rate", ["Breakfast", "included"], "bữa sáng"),
  ("Welcome to Hoa Sen Hotel. Your room is on the fifth floor. Here is your key card, and the Wi-Fi password is on the holder.", ["fifth", "key", "password"], "giao phòng cho khách"),
  ("I'm sorry, your room isn't ready yet. Check-in time is two o'clock. We can keep your luggage at the front desk.", ["ready", "two", "luggage"], "khách đến sớm"),
 ],
})

# ───────────────────────── 2. Đặt phòng qua điện thoại & email ─────────────────────────
PHASES.append({
 "title": "Đặt phòng qua điện thoại & email",
 "vocab": [
  ("availability", "/əˌveɪləˈbɪləti/", "n", "tình trạng còn phòng trống", "Let me check our <b>availability</b> for those dates.", "Để tôi kiểm tra phòng trống cho những ngày đó.", "空室状況", "kūshitsu jōkyō"),
  ("twin room", "/ˌtwɪn ˈruːm/", "n", "phòng hai giường đơn", "A <b>twin room</b> has two single beds.", "Phòng twin có hai giường đơn.", "ツインルーム", "tsuin rūmu"),
  ("double room", "/ˌdʌbl ˈruːm/", "n", "phòng một giường đôi", "Would you like a <b>double room</b> or a twin room?", "Anh/chị muốn phòng giường đôi hay phòng hai giường đơn?", "ダブルルーム", "daburu rūmu"),
  ("room rate", "/ˈruːm reɪt/", "n", "giá phòng", "The <b>room rate</b> includes breakfast.", "Giá phòng đã bao gồm bữa sáng.", "客室料金", "kyakushitsu ryōkin"),
  ("per night", "/pə ˈnaɪt/", "phr", "mỗi đêm", "It's 1.2 million dong <b>per night</b>.", "Giá là 1,2 triệu đồng mỗi đêm.", "1泊あたり", "ippaku atari"),
  ("fully booked", "/ˌfʊli ˈbʊkt/", "adj", "kín phòng, hết phòng", "Sorry, we're <b>fully booked</b> on Saturday.", "Xin lỗi, thứ Bảy khách sạn đã kín phòng.", "満室", "manshitsu"),
  ("cancellation", "/ˌkænsəˈleɪʃn/", "n", "sự huỷ (đặt phòng)", "Free <b>cancellation</b> is possible up to 48 hours before arrival.", "Có thể huỷ miễn phí trước ngày đến 48 tiếng.", "キャンセル", "kyanseru"),
  ("non-refundable", "/ˌnɒn rɪˈfʌndəbl/", "adj", "không được hoàn tiền", "This special price is <b>non-refundable</b>.", "Giá ưu đãi này không được hoàn tiền.", "返金不可", "henkin fuka"),
  ("sea view", "/ˌsiː ˈvjuː/", "n", "hướng nhìn ra biển", "All our deluxe rooms have a <b>sea view</b>.", "Tất cả phòng deluxe đều có view biển.", "オーシャンビュー", "ōshan byū"),
  ("arrival", "/əˈraɪvl/", "n", "sự đến nơi", "What's your expected <b>arrival</b> time?", "Anh/chị dự kiến đến lúc mấy giờ?", "到着", "tōchaku"),
 ],
 "phrases": [
  ("Good morning, Hoa Sen Hotel. How may I help you?", "Khách sạn Hoa Sen xin nghe. Tôi có thể giúp gì cho anh/chị?"),
  ("Which dates would you like to book?", "Anh/chị muốn đặt phòng những ngày nào ạ?"),
  ("How many guests will there be?", "Sẽ có bao nhiêu khách ạ?"),
  ("Let me check our availability. One moment, please.", "Để tôi kiểm tra phòng trống. Anh/chị chờ một chút nhé."),
  ("We have a double room with a sea view for 1.5 million dong per night.", "Chúng tôi có phòng giường đôi view biển giá 1,5 triệu đồng mỗi đêm."),
  ("The rate includes breakfast and airport pick-up.", "Giá đã gồm bữa sáng và đón sân bay."),
  ("Could you spell your last name, please?", "Anh/chị đánh vần giúp tôi họ của mình được không?"),
  ("I'll send you a confirmation email in a few minutes.", "Vài phút nữa tôi sẽ gửi email xác nhận cho anh/chị."),
  ("You can cancel for free until 48 hours before arrival.", "Anh/chị có thể huỷ miễn phí đến trước ngày đến 48 tiếng."),
  ("Thank you for choosing Hoa Sen Hotel. We look forward to welcoming you.", "Cảm ơn anh/chị đã chọn khách sạn Hoa Sen. Chúng tôi rất mong được đón tiếp anh/chị."),
 ],
 "dialogues": [
  ("Hi, do you have a room for two people from the 12th to the 15th?", [
    ("Let me check... Yes, we have a double room for three nights. Would you like breakfast included?", True, "Kiểm tra + xác nhận số đêm + gợi ý thêm dịch vụ."),
    ("Yes, have.", False, "Thiếu chủ ngữ: 'Yes, we have a room available.'"),
    ("Room two people, 12 to 15, OK.", False, "Lặp lại từng chữ, thiếu động từ, chưa nói loại phòng."),
  ]),
  ("How much is it per night?", [
    ("It's 1.3 million dong per night, including breakfast and taxes.", True, "Giá + đơn vị + những gì đã bao gồm."),
    ("One million three.", False, "Thiếu chủ ngữ và đơn vị: 'It's 1.3 million dong per night.'"),
    ("It's not expensive.", False, "Không nói giá cụ thể."),
  ]),
  ("Can I cancel if my plans change?", [
    ("Yes, you can cancel for free up to two days before arrival.", True, "Trả lời rõ + điều kiện huỷ miễn phí."),
    ("Yes, can cancel free.", False, "Thiếu chủ ngữ và 'for': 'Yes, you can cancel for free.'"),
    ("Why you want cancel?", False, "Hỏi vặn khách và sai ngữ pháp ('Why do you want to cancel?') — không nên hỏi vậy."),
  ]),
  ("We'd like to stay this Saturday, but I can't book online.", [
    ("I'm sorry, we're fully booked on Saturday. We have rooms on Sunday, or I can recommend a hotel nearby.", True, "Xin lỗi + lý do + đưa phương án khác."),
    ("Saturday full room.", False, "Dịch từng chữ 'thứ Bảy đầy phòng' — nên nói 'We're fully booked on Saturday.'"),
    ("Sorry, no.", False, "Quá cộc, không đưa phương án khác."),
  ]),
  ("Could you send me the confirmation by email?", [
    ("Of course. Could I have your email address, please? I'll send it right away.", True, "Đồng ý + xin email + hẹn gửi ngay."),
    ("OK, I will sending.", False, "Sau 'will' dùng động từ nguyên mẫu: 'I'll send it.'"),
    ("You booked already, no need.", False, "Từ chối yêu cầu hợp lý, nghe thiếu chuyên nghiệp."),
  ]),
 ],
 "listen": [
  ("Let me check our availability for those dates", ["check", "availability"], "kiểm tra phòng trống"),
  ("We're fully booked this weekend", ["fully", "weekend"], "hết phòng"),
  ("The room rate includes breakfast", ["rate", "breakfast"], "giá phòng"),
  ("Could you spell your last name, please", ["spell", "last"], "xin đánh vần tên"),
  ("Thank you for calling Hoa Sen Hotel. We have a twin room for two nights. The price is one million dong per night.", ["twin", "two", "million"], "báo giá qua điện thoại"),
  ("Dear Ms. Brown, thank you for your booking. Your sea-view room is confirmed for June 3. Free cancellation is possible until June 1.", ["room", "confirmed", "cancellation"], "email xác nhận đặt phòng"),
 ],
})

# ───────────────────────── 3. Trả phòng & thanh toán ─────────────────────────
PHASES.append({
 "title": "Trả phòng & thanh toán",
 "vocab": [
  ("check out", "/ˌtʃek ˈaʊt/", "v", "trả phòng", "Guests must <b>check out</b> by 12 noon.", "Khách cần trả phòng trước 12 giờ trưa.", "チェックアウト", "chekkuauto"),
  ("bill", "/bɪl/", "n", "hoá đơn (tổng tiền)", "Here is your <b>bill</b>. Please check it.", "Đây là hoá đơn của anh/chị. Anh/chị kiểm tra giúp nhé.", "請求書", "seikyūsho"),
  ("minibar", "/ˈmɪnibɑː/", "n", "tủ lạnh nhỏ trong phòng (minibar)", "Did you use anything from the <b>minibar</b>?", "Anh/chị có dùng gì trong minibar không ạ?", "ミニバー", "minibā"),
  ("receipt", "/rɪˈsiːt/", "n", "biên lai", "Would you like a <b>receipt</b>?", "Anh/chị có cần biên lai không ạ?", "領収書", "ryōshūsho"),
  ("credit card", "/ˈkredɪt kɑːd/", "n", "thẻ tín dụng", "Would you like to pay by <b>credit card</b> or in cash?", "Anh/chị muốn trả bằng thẻ tín dụng hay tiền mặt?", "クレジットカード", "kurejitto kādo"),
  ("cash", "/kæʃ/", "n", "tiền mặt", "You can pay in <b>cash</b>, in dong or US dollars.", "Anh/chị có thể trả tiền mặt bằng đồng hoặc đô la Mỹ.", "現金", "genkin"),
  ("exchange rate", "/ɪksˈtʃeɪndʒ reɪt/", "n", "tỷ giá", "Today's <b>exchange rate</b> is 26,300 dong to the dollar.", "Tỷ giá hôm nay là 26.300 đồng một đô.", "為替レート", "kawase rēto"),
  ("late check-out", "/ˌleɪt ˈtʃek aʊt/", "n", "trả phòng muộn", "A <b>late check-out</b> until 4 p.m. costs half the room rate.", "Trả phòng muộn đến 4 giờ chiều tính thêm nửa giá phòng.", "レイトチェックアウト", "reito chekkuauto"),
  ("service charge", "/ˈsɜːvɪs tʃɑːdʒ/", "n", "phí phục vụ", "The price includes a 5 percent <b>service charge</b>.", "Giá đã gồm 5% phí phục vụ.", "サービス料", "sābisu ryō"),
  ("airport transfer", "/ˈeəpɔːt ˌtrænsfɜː/", "n", "xe đưa đón sân bay", "Your <b>airport transfer</b> is at 3 p.m.", "Xe đưa anh/chị ra sân bay lúc 3 giờ chiều.", "空港送迎", "kūkō sōgei"),
 ],
 "phrases": [
  ("Are you checking out? May I have your key card, please?", "Anh/chị trả phòng ạ? Cho tôi xin lại thẻ phòng."),
  ("Did you take anything from the minibar last night?", "Tối qua anh/chị có dùng gì trong minibar không ạ?"),
  ("Here is your bill. The total is 4.2 million dong.", "Đây là hoá đơn. Tổng cộng 4,2 triệu đồng."),
  ("How would you like to pay?", "Anh/chị muốn thanh toán bằng cách nào ạ?"),
  ("Please enter your PIN.", "Anh/chị vui lòng nhập mã PIN."),
  ("Here is your receipt, and here is your deposit back.", "Đây là biên lai, và đây là tiền cọc hoàn lại anh/chị."),
  ("Would you like us to keep your luggage until your taxi comes?", "Anh/chị có muốn chúng tôi giữ hành lý đến khi taxi tới không?"),
  ("Your airport transfer will be here at 3 p.m.", "Xe đưa ra sân bay sẽ đến lúc 3 giờ chiều."),
  ("How was your stay with us?", "Kỳ nghỉ của anh/chị ở đây thế nào ạ?"),
  ("Thank you for staying with us. Have a safe trip!", "Cảm ơn anh/chị đã ở khách sạn chúng tôi. Chúc anh/chị thượng lộ bình an!"),
 ],
 "dialogues": [
  ("I'd like to check out, please. Room 312.", [
    ("Of course. Did you use anything from the minibar?", True, "Đồng ý + hỏi minibar trước khi in hoá đơn."),
    ("OK, give key.", False, "Thiếu chủ ngữ, nghe như ra lệnh: 'May I have your key card, please?'"),
    ("Why you check out so early?", False, "Tò mò chuyện riêng, lại sai ngữ pháp ('Why are you…')."),
  ]),
  ("What's this charge for 200,000 dong?", [
    ("That's for two drinks from the minibar. Would you like me to check it again?", True, "Giải thích khoản phí + đề nghị kiểm tra lại."),
    ("It is minibar you drink.", False, "Dịch từng chữ, sai trật tự: 'It's for the drinks from the minibar.'"),
    ("The computer says it, so you must pay.", False, "Đổ cho máy, không giải thích, thiếu thiện chí."),
  ]),
  ("Can I pay in US dollars?", [
    ("Yes, you can. Today's exchange rate is 26,300 dong to the dollar.", True, "Trả lời + nêu tỷ giá để khách biết."),
    ("Yes, you can pay dollar.", False, "Thiếu 'in' và 's': 'You can pay in US dollars.'"),
    ("Dollar no.", False, "Quá cộc, thiếu động từ; nếu không nhận đô thì xin lỗi và chỉ chỗ đổi tiền."),
  ]),
  ("My flight is at 6 p.m. Can I check out late?", [
    ("Let me check. We can offer a late check-out until 4 p.m. for 500,000 dong. Would that be OK?", True, "Kiểm tra + đưa lựa chọn cụ thể có giá."),
    ("Late check-out is have fee.", False, "Dịch từng chữ 'có phí' — nên nói 'There's a fee for late check-out.'"),
    ("No, check-out is 12. Rule is rule.", False, "Cứng nhắc; nên đưa phương án (giữ hành lý, trả phòng muộn có phí)."),
  ]),
  ("Could I get a receipt with my company name on it?", [
    ("Certainly. Could you write the company name and tax code here, please?", True, "Đồng ý + xin đúng thông tin cần in."),
    ("Yes, I make it.", False, "Sai động từ và thì: 'Sure, I'll print it for you.'"),
    ("Receipt is same as the bill.", False, "Không đáp ứng yêu cầu ghi tên công ty."),
  ]),
 ],
 "listen": [
  ("Would you like to pay by card or in cash", ["card", "cash"], "hỏi cách thanh toán"),
  ("Here is your bill for three nights", ["bill", "nights"], "đưa hoá đơn"),
  ("Did you use the minibar last night", ["minibar", "night"], "hỏi minibar"),
  ("Your taxi to the airport is waiting outside", ["taxi", "airport"], "báo xe đã đến"),
  ("Thank you for staying with us. The total is three million dong. Here is your receipt.", ["staying", "total", "receipt"], "tính tiền khi trả phòng"),
  ("Check-out time is twelve noon. If your flight is late, we can keep your luggage. The airport transfer leaves at three.", ["noon", "flight", "transfer"], "dặn giờ trả phòng"),
 ],
})

# ───────────────────────── 4. Yêu cầu đặc biệt của khách ─────────────────────────
PHASES.append({
 "title": "Yêu cầu đặc biệt của khách",
 "vocab": [
  ("request", "/rɪˈkwest/", "n", "yêu cầu", "We received your <b>request</b> for a quiet room.", "Chúng tôi đã nhận yêu cầu phòng yên tĩnh của anh/chị.", "リクエスト", "rikuesuto"),
  ("arrange", "/əˈreɪndʒ/", "v", "sắp xếp, thu xếp", "I can <b>arrange</b> a taxi for you.", "Tôi có thể đặt taxi giúp anh/chị.", "手配する", "tehai suru"),
  ("extra bed", "/ˌekstrə ˈbed/", "n", "giường phụ", "An <b>extra bed</b> costs 400,000 dong per night.", "Giường phụ giá 400.000 đồng một đêm.", "エキストラベッド", "ekisutora beddo"),
  ("cot", "/kɒt/", "n", "nôi, cũi em bé", "We can put a baby <b>cot</b> in your room for free.", "Chúng tôi có thể đặt nôi em bé trong phòng miễn phí.", "ベビーベッド", "bebī beddo"),
  ("wake-up call", "/ˈweɪk ʌp kɔːl/", "n", "cuộc gọi báo thức", "Would you like a <b>wake-up call</b> tomorrow?", "Sáng mai anh/chị có cần gọi báo thức không ạ?", "モーニングコール", "mōningu kōru"),
  ("laundry service", "/ˈlɔːndri ˌsɜːvɪs/", "n", "dịch vụ giặt ủi", "Our <b>laundry service</b> takes 24 hours.", "Dịch vụ giặt ủi của khách sạn mất 24 tiếng.", "ランドリーサービス", "randorī sābisu"),
  ("early check-in", "/ˌɜːli ˈtʃek ɪn/", "n", "nhận phòng sớm", "<b>Early check-in</b> depends on availability.", "Nhận phòng sớm tuỳ vào tình trạng phòng trống.", "アーリーチェックイン", "ārī chekkuin"),
  ("connecting rooms", "/kəˌnektɪŋ ˈruːmz/", "n", "phòng thông nhau (có cửa nối)", "The family booked two <b>connecting rooms</b>.", "Gia đình ấy đặt hai phòng thông nhau.", "コネクティングルーム", "konekutingu rūmu"),
  ("anniversary", "/ˌænɪˈvɜːsəri/", "n", "ngày kỷ niệm", "It's their wedding <b>anniversary</b>, so let's put flowers in the room.", "Hôm nay là kỷ niệm ngày cưới của họ, mình đặt hoa trong phòng nhé.", "記念日", "kinenbi"),
  ("shuttle bus", "/ˈʃʌtl bʌs/", "n", "xe buýt đưa đón", "The free <b>shuttle bus</b> to the beach leaves every hour.", "Xe đưa đón miễn phí ra biển chạy mỗi giờ một chuyến.", "シャトルバス", "shatoru basu"),
 ],
 "phrases": [
  ("Is there anything else I can do for you?", "Tôi có thể giúp gì thêm cho anh/chị không ạ?"),
  ("Certainly. I'll arrange that for you.", "Vâng ạ. Tôi sẽ sắp xếp việc đó cho anh/chị."),
  ("What time would you like your wake-up call?", "Anh/chị muốn gọi báo thức lúc mấy giờ ạ?"),
  ("We can bring an extra bed to your room this afternoon.", "Chiều nay chúng tôi có thể mang giường phụ lên phòng anh/chị."),
  ("Please put your laundry in the bag and call housekeeping.", "Anh/chị cho đồ cần giặt vào túi rồi gọi bộ phận buồng phòng nhé."),
  ("I'll book a car to the airport for 5 a.m.", "Tôi sẽ đặt xe ra sân bay lúc 5 giờ sáng."),
  ("I'm afraid that's not possible, but I can offer you another option.", "Tôi e là việc đó không được, nhưng tôi có thể đưa anh/chị một lựa chọn khác."),
  ("Let me check with my manager and call you back in ten minutes.", "Để tôi hỏi quản lý rồi gọi lại cho anh/chị trong mười phút."),
  ("Happy anniversary! We've prepared a small cake for you.", "Chúc mừng kỷ niệm! Chúng tôi có chuẩn bị một chiếc bánh nhỏ tặng anh chị."),
 ],
 "dialogues": [
  ("Could I have a wake-up call at 5:30 tomorrow?", [
    ("Of course. A wake-up call at 5:30 tomorrow morning. Is there anything else?", True, "Nhắc lại giờ để xác nhận + hỏi thêm."),
    ("OK, I call you 5:30.", False, "Thiếu 'will' và 'at': 'I'll call you at 5:30.'"),
    ("You can use the alarm on your phone.", False, "Từ chối dịch vụ khách sạn vẫn làm — thiếu chuyên nghiệp."),
  ]),
  ("We're travelling with a baby. Do you have a cot?", [
    ("Yes, we do. I'll ask housekeeping to bring one to your room. It's free of charge.", True, "Xác nhận + hành động + báo miễn phí."),
    ("Yes, have cot for baby.", False, "Thiếu chủ ngữ: 'Yes, we have a cot.'"),
    ("Yes, I bring later.", False, "Thiếu 'will', 'later' mơ hồ — nên nói rõ: 'I'll bring it in 15 minutes.'"),
  ]),
  ("Can you book a table for us at a good seafood restaurant tonight?", [
    ("Certainly. How many people, and what time would you like?", True, "Nhận lời + hỏi đủ thông tin để đặt."),
    ("You can book on the app.", False, "Đẩy việc cho khách; lễ tân nên đặt giúp."),
    ("Yes, I booking for you.", False, "Sai thì: 'I'll book it for you.'"),
  ]),
  ("It's our 10th anniversary. Is there anything special you can do?", [
    ("Congratulations! We can decorate your room with flowers and send you a small cake. Would you like that?", True, "Chúc mừng + đề xuất cụ thể + hỏi ý khách."),
    ("Congratulation you.", False, "Luôn dùng số nhiều 'Congratulations!' và không thêm 'you'."),
    ("Sorry, we have no special.", False, "Thiếu danh từ và bỏ lỡ cơ hội làm khách vui — nên đề xuất gì đó."),
  ]),
  ("Could we get an early check-in? We arrive at 8 in the morning.", [
    ("I'll note your request. If the room isn't ready, you can leave your luggage with us and relax by the pool.", True, "Ghi nhận + không hứa chắc + đưa phương án."),
    ("8 o'clock is too early, cannot.", False, "Thiếu chủ ngữ và cộc — nên ghi nhận và đưa phương án."),
    ("Yes, 100 percent OK.", False, "Hứa chắc khi chưa kiểm tra phòng — dễ làm khách thất vọng."),
  ]),
 ],
 "listen": [
  ("I'll arrange a taxi for you at six", ["arrange", "taxi"], "đặt xe cho khách"),
  ("Your wake-up call is at five thirty", ["wake-up", "thirty"], "xác nhận giờ báo thức"),
  ("We can bring an extra bed this afternoon", ["extra", "afternoon"], "giường phụ"),
  ("The shuttle bus to the beach leaves every hour", ["shuttle", "beach"], "xe đưa đón"),
  ("Good evening, Mrs. Lee. We received your request for a baby cot. Housekeeping will bring it in ten minutes.", ["request", "cot", "ten"], "xác nhận yêu cầu"),
  ("It's the guests' wedding anniversary today. Please put flowers in room 402. The kitchen will send a cake at eight.", ["anniversary", "flowers", "cake"], "dặn đồng nghiệp chuẩn bị bất ngờ"),
 ],
})

# ───────────────────────── 5. Phàn nàn & xử lý sự cố ─────────────────────────
PHASES.append({
 "title": "Phàn nàn & xử lý sự cố",
 "vocab": [
  ("noisy", "/ˈnɔɪzi/", "adj", "ồn ào", "My room is too <b>noisy</b>. I can hear the music from the bar.", "Phòng tôi ồn quá. Tôi nghe thấy nhạc từ quầy bar."),
  ("air conditioner", "/ˈeə kənˌdɪʃənə/", "n", "máy lạnh, điều hoà", "The <b>air conditioner</b> in room 210 isn't working.", "Máy lạnh phòng 210 không chạy.", "エアコン", "eakon"),
  ("hot water", "/ˌhɒt ˈwɔːtə/", "n", "nước nóng", "There's no <b>hot water</b> in the shower.", "Vòi sen không có nước nóng.", "お湯", "oyu"),
  ("leak", "/liːk/", "n/v", "chỗ rò rỉ, bị dột", "There's a <b>leak</b> in the bathroom ceiling.", "Trần nhà tắm bị dột.", "水漏れ", "mizumore"),
  ("inconvenience", "/ˌɪnkənˈviːniəns/", "n", "sự bất tiện", "We're very sorry for the <b>inconvenience</b>.", "Chúng tôi rất xin lỗi vì sự bất tiện này.", "ご不便", "gofuben"),
  ("refund", "/ˈriːfʌnd/", "n", "khoản hoàn tiền", "We'll give you a <b>refund</b> for tonight.", "Chúng tôi sẽ hoàn tiền đêm nay cho anh/chị.", "返金", "henkin"),
  ("duty manager", "/ˈdjuːti ˌmænɪdʒə/", "n", "quản lý trực ca", "Let me call the <b>duty manager</b> for you.", "Để tôi gọi quản lý trực ca cho anh/chị."),
  ("look into", "/ˌlʊk ˈɪntuː/", "phr v", "xem xét, kiểm tra", "I'll <b>look into</b> it right away.", "Tôi sẽ kiểm tra việc này ngay."),
  ("disappointed", "/ˌdɪsəˈpɔɪntɪd/", "adj", "thất vọng", "I'm really <b>disappointed</b> with the room.", "Tôi thực sự thất vọng về căn phòng."),
  ("replace", "/rɪˈpleɪs/", "v", "thay, đổi cái mới", "We'll <b>replace</b> the towels right now.", "Chúng tôi sẽ thay khăn ngay bây giờ.", "交換する", "kōkan suru"),
 ],
 "phrases": [
  ("I'm very sorry to hear that.", "Tôi rất tiếc khi nghe điều đó."),
  ("I understand how you feel.", "Tôi hiểu cảm giác của anh/chị."),
  ("Thank you for telling us.", "Cảm ơn anh/chị đã báo cho chúng tôi."),
  ("I'll look into it right away.", "Tôi sẽ kiểm tra việc này ngay."),
  ("I'll send someone to your room in five minutes.", "Năm phút nữa tôi sẽ cho người lên phòng anh/chị."),
  ("Would you like to move to another room?", "Anh/chị có muốn đổi sang phòng khác không ạ?"),
  ("We're very sorry for the inconvenience.", "Chúng tôi rất xin lỗi vì sự bất tiện này."),
  ("As an apology, we'd like to offer you a free dinner tonight.", "Để xin lỗi, chúng tôi xin mời anh/chị bữa tối miễn phí tối nay."),
  ("Let me get the duty manager for you.", "Để tôi mời quản lý trực ca đến gặp anh/chị."),
  ("Is everything OK with your room now?", "Phòng của anh/chị giờ đã ổn chưa ạ?"),
 ],
 "dialogues": [
  ("The air conditioner in my room isn't working. It's so hot!", [
    ("I'm so sorry. I'll send a technician right now. Would you like a cold drink while you wait?", True, "Xin lỗi + hành động ngay + chăm sóc khách lúc chờ."),
    ("Maybe you use it wrong.", False, "Đổ lỗi cho khách — luôn xin lỗi và cử người kiểm tra trước."),
    ("Sorry, I will send people fix.", False, "Thiếu 'to' và dùng sai 'people': 'I'll send someone to fix it.'"),
  ]),
  ("My room is really noisy. I can't sleep.", [
    ("I'm very sorry. We have a quieter room on the eighth floor. Would you like to move?", True, "Xin lỗi + đưa giải pháp cụ thể."),
    ("It's normal, this is city center.", False, "Bác bỏ cảm nhận của khách, lại thiếu 'the'."),
    ("Sorry, sorry, sorry.", False, "Chỉ xin lỗi mà không có giải pháp."),
  ]),
  ("I've been waiting for my luggage for 40 minutes!", [
    ("I'm so sorry for the wait. Let me check with the porter and bring it up myself.", True, "Xin lỗi + tự xử lý ngay."),
    ("Please wait, it's coming.", False, "Khách đã chờ lâu — cần xin lỗi và hành động cụ thể."),
    ("Sorry for you wait long.", False, "Sai ngữ pháp: 'Sorry to keep you waiting.'"),
  ]),
  ("This is unacceptable. I want to speak to the manager.", [
    ("I understand. I'll call the duty manager now. Would you like to have a seat for a moment?", True, "Thừa nhận cảm xúc + đáp ứng yêu cầu + mời ngồi."),
    ("Manager is busy, you talk to me.", False, "Chặn khách, thiếu 'the' — khách sẽ càng bực."),
    ("Why you angry?", False, "Thiếu 'are', và câu hỏi này làm khách giận hơn."),
  ]),
  ("There's no hot water in the shower.", [
    ("I'm sorry about that. Our maintenance team will check it in ten minutes. I'll call you when it's working.", True, "Xin lỗi + thời gian cụ thể + hẹn báo lại."),
    ("Hot water no have.", False, "Dịch từng chữ 'nước nóng không có' — nên nói 'There's no hot water' và đưa giải pháp."),
    ("Wait 30 minutes, it will hot.", False, "Thiếu 'be': 'It'll be hot in 30 minutes' — lại chưa xin lỗi."),
  ]),
 ],
 "listen": [
  ("I'm very sorry for the inconvenience", ["sorry", "inconvenience"], "xin lỗi khách"),
  ("The air conditioner in my room is broken", ["conditioner", "broken"], "khách báo hỏng máy lạnh"),
  ("I'll send someone to your room right away", ["send", "right"], "cử người lên phòng"),
  ("Would you like to move to a quieter room", ["move", "quieter"], "đề nghị đổi phòng"),
  ("I'm really sorry about the noise last night. We've moved you to a room on the tenth floor. Breakfast today is on us.", ["noise", "tenth", "Breakfast"], "xin lỗi và bù đắp"),
  ("The guest in room 215 is very upset. There's a leak in the bathroom. Please call the duty manager now.", ["upset", "leak", "manager"], "báo sự cố cho đồng nghiệp"),
 ],
})

# ───────────────────────── 6. Nhà hàng – chào khách & gọi món ─────────────────────────
PHASES.append({
 "title": "Nhà hàng – chào khách & gọi món",
 "vocab": [
  ("menu", "/ˈmenjuː/", "n", "thực đơn", "Here's the <b>menu</b>. Today's specials are on the back.", "Đây là thực đơn. Món đặc biệt hôm nay ở mặt sau.", "メニュー", "menyū"),
  ("order", "/ˈɔːdə/", "v/n", "gọi món; món đã gọi", "Are you ready to <b>order</b>?", "Anh/chị gọi món được chưa ạ?", "注文", "chūmon"),
  ("recommend", "/ˌrekəˈmend/", "v", "gợi ý, giới thiệu (món)", "I <b>recommend</b> the grilled fish.", "Tôi gợi ý anh/chị thử món cá nướng.", "おすすめする", "osusume suru"),
  ("starter", "/ˈstɑːtə/", "n", "món khai vị", "Would you like a <b>starter</b>? The spring rolls are very popular.", "Anh/chị có dùng món khai vị không ạ? Món chả giò được khách rất thích.", "前菜", "zensai"),
  ("main course", "/ˌmeɪn ˈkɔːs/", "n", "món chính", "What would you like for your <b>main course</b>?", "Anh/chị muốn dùng món chính gì ạ?", "メインディッシュ", "mein disshu"),
  ("dessert", "/dɪˈzɜːt/", "n", "món tráng miệng", "Would you like to see the <b>dessert</b> menu?", "Anh/chị có muốn xem thực đơn tráng miệng không ạ?", "デザート", "dezāto"),
  ("specialty", "/ˈspeʃəlti/", "n", "đặc sản, món đặc trưng", "Cao lầu is a <b>specialty</b> of Hội An.", "Cao lầu là đặc sản của Hội An.", "名物", "meibutsu"),
  ("vegetarian", "/ˌvedʒəˈteəriən/", "adj/n", "chay; người ăn chay", "We have three <b>vegetarian</b> dishes on the menu.", "Thực đơn có ba món chay.", "ベジタリアン", "bejitarian"),
  ("spicy", "/ˈspaɪsi/", "adj", "cay", "Is this dish <b>spicy</b>?", "Món này có cay không?", "辛い", "karai"),
  ("breakfast buffet", "/ˈbrekfəst ˌbʊfeɪ/", "n", "tiệc buffet sáng", "The <b>breakfast buffet</b> is open from 6:30 to 10.", "Buffet sáng mở từ 6 giờ 30 đến 10 giờ.", "朝食ビュッフェ", "chōshoku byuffe"),
 ],
 "phrases": [
  ("Good evening. A table for two?", "Chào buổi tối. Bàn cho hai người ạ?"),
  ("Please follow me. Is this table OK?", "Mời anh/chị đi theo tôi. Bàn này được không ạ?"),
  ("Can I get you something to drink first?", "Anh/chị dùng gì để uống trước không ạ?"),
  ("Are you ready to order, or do you need a few more minutes?", "Anh/chị gọi món được chưa, hay cần thêm vài phút ạ?"),
  ("I recommend the grilled fish. It's our specialty.", "Tôi gợi ý món cá nướng. Đó là món đặc trưng của nhà hàng."),
  ("How spicy would you like it? Mild, medium or hot?", "Anh/chị muốn cay mức nào: ít, vừa hay nhiều?"),
  ("Would you like rice or noodles with that?", "Anh/chị muốn dùng kèm cơm hay mì ạ?"),
  ("So that's one beef pho and two spring rolls. Anything else?", "Vậy là một phở bò và hai chả giò. Anh/chị gọi thêm gì không ạ?"),
  ("Your food will be ready in about fifteen minutes.", "Món ăn sẽ có trong khoảng mười lăm phút."),
 ],
 "dialogues": [
  ("Hi, a table for two, please.", [
    ("Of course. Would you like to sit inside or outside on the terrace?", True, "Đáp nhanh + cho khách chọn chỗ."),
    ("Two people? Sit there.", False, "Cộc, như ra lệnh; nên nói 'This way, please.'"),
    ("Yes, table two.", False, "Dịch sai ý — 'table two' là bàn số hai, không phải bàn cho hai người."),
  ]),
  ("What do you recommend?", [
    ("Our specialty is cao lầu, a noodle dish from Hội An. The grilled fish is also very good.", True, "Gợi ý 1–2 món cụ thể + giải thích ngắn."),
    ("Everything is delicious.", False, "Không giúp khách chọn — nên gợi ý món cụ thể."),
    ("I recommend you eat pho is good.", False, "Sai cấu trúc: 'I recommend the pho. It's very good.'"),
  ]),
  ("Is the beef salad spicy?", [
    ("It's a little spicy, but we can make it mild for you.", True, "Nói rõ mức cay + đề nghị điều chỉnh."),
    ("No spicy.", False, "Thiếu động từ: 'It's not spicy.' — và nên nói rõ mức cay."),
    ("Vietnamese food is always spicy.", False, "Sai sự thật và không trả lời về món này."),
  ]),
  ("Do you have any vegetarian dishes?", [
    ("Yes, we do. The tofu in tomato sauce and the vegetable fried rice are both vegetarian.", True, "Xác nhận + giới thiệu món chay cụ thể."),
    ("Yes, have vegetable.", False, "Thiếu chủ ngữ và sai từ: món chay là 'vegetarian dishes', 'vegetable' là rau."),
    ("You can eat the rice.", False, "Nghe như từ chối — nên giới thiệu món chay cụ thể."),
  ]),
  ("Sorry, we need a few more minutes.", [
    ("No problem. Take your time. Just let me know when you're ready.", True, "Thoải mái, không giục khách."),
    ("OK. Fast, please.", False, "Giục khách, thiếu lịch sự."),
    ("OK, I come back after.", False, "Thiếu 'will', 'after' lơ lửng: 'I'll come back in a few minutes.'"),
  ]),
 ],
 "listen": [
  ("Are you ready to order", ["ready", "order"], "hỏi gọi món"),
  ("I recommend the grilled fish tonight", ["recommend", "fish"], "gợi ý món"),
  ("Would you like a starter before your main course", ["starter", "course"], "món khai vị"),
  ("The breakfast buffet is on the second floor", ["buffet", "second"], "buffet sáng ở đâu"),
  ("Good evening. Welcome to Lotus Restaurant. Here is the menu, and today's special is grilled prawns.", ["Welcome", "menu", "prawns"], "chào khách vào nhà hàng"),
  ("So that's two bowls of beef pho and one mango salad. Would you like anything to drink? The food will be ready in fifteen minutes.", ["bowls", "mango", "fifteen"], "nhắc lại món khách gọi"),
 ],
})

# ───────────────────────── 7. Nhà hàng – phục vụ, dị ứng & tính tiền ─────────────────────────
PHASES.append({
 "title": "Nhà hàng – phục vụ, dị ứng & tính tiền",
 "vocab": [
  ("allergy", "/ˈælədʒi/", "n", "dị ứng", "Do you have any food <b>allergies</b>?", "Anh/chị có dị ứng với món nào không?", "アレルギー", "arerugī"),
  ("allergic", "/əˈlɜːdʒɪk/", "adj", "bị dị ứng (với…)", "My son is <b>allergic</b> to eggs.", "Con trai tôi bị dị ứng trứng."),
  ("peanut", "/ˈpiːnʌt/", "n", "đậu phộng, lạc", "This sauce has <b>peanuts</b> in it.", "Nước sốt này có đậu phộng.", "ピーナッツ", "pīnattsu"),
  ("seafood", "/ˈsiːfuːd/", "n", "hải sản", "The soup is made with <b>seafood</b>.", "Món súp này nấu từ hải sản.", "魚介類", "gyokairui"),
  ("ingredient", "/ɪnˈɡriːdiənt/", "n", "nguyên liệu, thành phần", "Let me ask the chef about the <b>ingredients</b>.", "Để tôi hỏi đầu bếp về nguyên liệu.", "食材", "shokuzai"),
  ("gluten-free", "/ˌɡluːtn ˈfriː/", "adj", "không chứa gluten", "Our rice noodles are <b>gluten-free</b>, but let me check the sauce.", "Bánh phở làm từ gạo nên không có gluten, nhưng để tôi kiểm tra nước sốt.", "グルテンフリー", "guruten furī"),
  ("refill", "/ˈriːfɪl/", "n", "sự rót thêm, châm thêm", "Would you like a <b>refill</b> of your iced tea?", "Anh/chị có muốn châm thêm trà đá không ạ?", "おかわり", "okawari"),
  ("takeaway", "/ˈteɪkəweɪ/", "n", "đồ mang về", "Would you like a <b>takeaway</b> box for the rest?", "Anh/chị có cần hộp để gói phần còn lại mang về không ạ?", "持ち帰り", "mochikaeri"),
  ("split the bill", "/ˌsplɪt ðə ˈbɪl/", "phr", "chia hoá đơn", "Would you like to <b>split the bill</b>?", "Anh/chị có muốn chia hoá đơn không ạ?", "割り勘", "warikan"),
  ("tip", "/tɪp/", "n", "tiền boa", "A <b>tip</b> isn't required, but we really appreciate it.", "Tiền boa không bắt buộc, nhưng chúng tôi rất cảm kích.", "チップ", "chippu"),
 ],
 "phrases": [
  ("Do you have any allergies we should know about?", "Anh/chị có dị ứng gì mà chúng tôi cần biết không ạ?"),
  ("Let me check with the chef.", "Để tôi hỏi lại đầu bếp."),
  ("This dish has peanuts, but we can make it without them.", "Món này có đậu phộng, nhưng chúng tôi có thể làm không có đậu phộng."),
  ("Here's your grilled fish. Enjoy your meal!", "Món cá nướng của anh/chị đây. Chúc ngon miệng!"),
  ("Is everything OK with your meal?", "Món ăn có vừa ý anh/chị không ạ?"),
  ("May I take your plate?", "Tôi dọn đĩa được chưa ạ?"),
  ("Can I get you anything else? Some dessert or coffee?", "Anh/chị dùng thêm gì không ạ? Tráng miệng hay cà phê?"),
  ("Would you like to pay together or separately?", "Anh/chị muốn thanh toán chung hay riêng ạ?"),
  ("You can pay here or charge it to your room.", "Anh/chị có thể thanh toán ở đây hoặc tính vào tiền phòng."),
  ("Here's your change. Thank you, and have a nice evening.", "Tiền thừa của anh/chị đây. Cảm ơn và chúc buổi tối vui vẻ."),
 ],
 "dialogues": [
  ("I'm allergic to peanuts. Is the chicken salad OK?", [
    ("Thank you for telling me. The salad has peanuts, so let me check with the chef and find a safe dish for you.", True, "Cảm ơn + nói thật thành phần + hỏi bếp để chọn món an toàn (chỉ bỏ đậu phộng ra chưa chắc đủ an toàn)."),
    ("Just a little peanut, no problem.", False, "Rất nguy hiểm — đã dị ứng thì dù ít cũng không được."),
    ("I don't know. Maybe OK.", False, "Đoán mò chuyện dị ứng — phải hỏi đầu bếp cho chắc."),
  ]),
  ("Excuse me, this isn't what I ordered. I ordered the fish.", [
    ("I'm so sorry. I'll bring your fish right away.", True, "Xin lỗi + sửa ngay, không tranh cãi."),
    ("No, you ordered chicken.", False, "Cãi lại khách — nên xin lỗi và kiểm tra/đổi món."),
    ("Sorry, I bring wrong.", False, "Thiếu tân ngữ, sai thì: 'Sorry, I brought the wrong dish.'"),
  ]),
  ("Could we have the bill, please?", [
    ("Of course. Would you like to pay together or separately?", True, "Đồng ý + hỏi cách thanh toán."),
    ("OK, wait me.", False, "Sai: 'wait for me' — và nên nói 'One moment, please.'"),
    ("Bill is 850,000.", False, "Đọc số cộc lốc tại chỗ; nên mang hoá đơn ra bàn."),
  ]),
  ("Can we split the bill?", [
    ("Sure. Would you like to split it equally, or pay for what each person had?", True, "Đồng ý + hỏi cách chia."),
    ("Yes, can divide.", False, "Thiếu chủ ngữ, 'divide' không tự nhiên: 'Sure, we can split it.'"),
    ("Split is difficult, one person pay.", False, "Từ chối vì ngại việc, sai ngữ pháp ('pays')."),
  ]),
  ("Is service included?", [
    ("Yes, a 5 percent service charge is included. Tipping is up to you.", True, "Trả lời rõ + tip tuỳ khách."),
    ("Tip is must.", False, "Sai và ép khách — tiền boa ở Việt Nam là tuỳ ý."),
    ("Yes, include service.", False, "Thiếu chủ ngữ và dạng bị động: 'Yes, service is included.'"),
  ]),
 ],
 "listen": [
  ("Do you have any food allergies", ["food", "allergies"], "hỏi dị ứng"),
  ("This sauce is made with peanuts", ["sauce", "peanuts"], "thành phần nước sốt"),
  ("Would you like to pay together or separately", ["together", "separately"], "cách thanh toán"),
  ("Can I get you a refill", ["get", "refill"], "châm thêm đồ uống"),
  ("Excuse me, the guest at table six is allergic to seafood. Please don't use any seafood or fish sauce in her soup. Can you check with the chef?", ["six", "seafood", "chef"], "báo dị ứng với bếp"),
  ("Here is your bill. The total is 1.2 million dong, and the service charge is included. You can pay by card here.", ["total", "service", "card"], "tính tiền tại bàn"),
 ],
})

# ───────────────────────── 8. Buồng phòng & bảo trì ─────────────────────────
PHASES.append({
 "title": "Buồng phòng & bảo trì",
 "vocab": [
  ("housekeeping", "/ˈhaʊskiːpɪŋ/", "n", "bộ phận buồng phòng", "<b>Housekeeping</b>! May I come in?", "Buồng phòng đây ạ! Tôi vào được không?", "客室清掃", "kyakushitsu seisō"),
  ("turndown service", "/ˈtɜːndaʊn ˌsɜːvɪs/", "n", "dọn giường buổi tối (chuẩn bị đi ngủ)", "Would you like <b>turndown service</b> tonight?", "Tối nay anh/chị có muốn chúng tôi dọn giường chuẩn bị đi ngủ không ạ?", "ターンダウンサービス", "tāndaun sābisu"),
  ("bed sheet", "/ˈbed ʃiːt/", "n", "ga trải giường", "We change the <b>bed sheets</b> every two days.", "Chúng tôi thay ga giường hai ngày một lần.", "シーツ", "shītsu"),
  ("pillow", "/ˈpɪləʊ/", "n", "cái gối", "Could I have an extra <b>pillow</b>, please?", "Cho tôi thêm một cái gối được không?", "枕", "makura"),
  ("toiletries", "/ˈtɔɪlətriz/", "n", "đồ dùng vệ sinh cá nhân", "Shampoo, soap and other <b>toiletries</b> are in the bathroom.", "Dầu gội, xà phòng và đồ dùng vệ sinh cá nhân có trong phòng tắm.", "アメニティ", "amenitī"),
  ("hair dryer", "/ˈheə ˌdraɪə/", "n", "máy sấy tóc", "The <b>hair dryer</b> is in the drawer.", "Máy sấy tóc ở trong ngăn kéo.", "ドライヤー", "doraiyā"),
  ("safe", "/seɪf/", "n", "két sắt", "Please keep your passport in the <b>safe</b>.", "Anh/chị nên cất hộ chiếu trong két sắt.", "金庫", "kinko"),
  ("Do Not Disturb", "/ˌduː nɒt dɪˈstɜːb/", "phr", "Xin đừng làm phiền (biển treo cửa)", "The guest put the <b>Do Not Disturb</b> sign on the door.", "Khách đã treo biển 'Xin đừng làm phiền' trên cửa."),
  ("maintenance", "/ˈmeɪntənəns/", "n", "bộ phận bảo trì; việc bảo trì", "I'll ask <b>maintenance</b> to repair the light.", "Tôi sẽ nhờ bộ phận bảo trì sửa đèn.", "メンテナンス", "mentenansu"),
  ("lost and found", "/ˌlɒst ən ˈfaʊnd/", "n", "nơi giữ đồ thất lạc", "We keep items in <b>lost and found</b> for three months.", "Chúng tôi giữ đồ thất lạc trong ba tháng.", "忘れ物", "wasuremono"),
 ],
 "phrases": [
  ("Good morning. Housekeeping. May I clean your room now?", "Chào buổi sáng. Buồng phòng đây ạ. Tôi dọn phòng bây giờ được không?"),
  ("What time would be good for me to come back?", "Mấy giờ tôi quay lại thì tiện cho anh/chị ạ?"),
  ("I'll bring you some fresh towels right away.", "Tôi sẽ mang khăn sạch lên cho anh/chị ngay."),
  ("Would you like me to change the bed sheets today?", "Hôm nay anh/chị có muốn tôi thay ga giường không ạ?"),
  ("The safe is in the wardrobe. The instructions are on the door.", "Két sắt ở trong tủ quần áo. Hướng dẫn dán trên cửa tủ."),
  ("I'll ask the maintenance team to check the shower.", "Tôi sẽ nhờ đội bảo trì kiểm tra vòi sen."),
  ("The technician will come in about fifteen minutes.", "Thợ kỹ thuật sẽ đến trong khoảng mười lăm phút."),
  ("Sorry to disturb you. I'm here to repair the light.", "Xin lỗi đã làm phiền. Tôi đến sửa đèn ạ."),
  ("We found a phone in room 406. I'll take it to lost and found.", "Chúng tôi tìm thấy một chiếc điện thoại ở phòng 406. Tôi sẽ mang xuống chỗ giữ đồ thất lạc."),
 ],
 "dialogues": [
  ("Not now, please. Can you come back later?", [
    ("Of course. What time would be good for you?", True, "Đồng ý + hỏi giờ thuận tiện cho khách."),
    ("OK, but I must clean now.", False, "Mâu thuẫn và ép khách; nên hỏi giờ thuận tiện."),
    ("Later is what time?", False, "Dịch từng chữ 'lát nữa là mấy giờ' — nghe cộc; nên nói 'What time would be good for you?'"),
  ]),
  ("Could I have two more towels and an extra pillow?", [
    ("Certainly. I'll bring them in five minutes.", True, "Đồng ý + thời gian cụ thể."),
    ("Yes, I bring you two towel and pillow.", False, "Thiếu 'will' và số nhiều: 'I'll bring two towels and a pillow.'"),
    ("Towels are enough already.", False, "Từ chối yêu cầu nhỏ, thiếu thiện chí."),
  ]),
  ("The light in the bathroom doesn't work.", [
    ("Sorry about that. I'll call maintenance now. Someone will come in ten minutes.", True, "Xin lỗi + gọi bảo trì + thời gian."),
    ("Yes, light is broken since yesterday.", False, "Biết hỏng mà không sửa, lại sai thì ('has been broken') — khách sẽ bực."),
    ("You can use the light in the bedroom.", False, "Né vấn đề, không đưa giải pháp."),
  ]),
  ("I think I left my sunglasses in my room. I checked out this morning.", [
    ("Let me check with lost and found. Could you tell me your room number, please?", True, "Kiểm tra + xin thông tin cần thiết."),
    ("No, nobody found.", False, "Trả lời khi chưa kiểm tra, thiếu tân ngữ ('found them')."),
    ("Why you not check before leave?", False, "Trách khách + sai ngữ pháp."),
  ]),
  ("How do I use the safe?", [
    ("Close the door, enter a four-digit code and press the lock button. The instructions are also inside.", True, "Hướng dẫn từng bước rõ ràng."),
    ("Easy, you try.", False, "Cộc, không hướng dẫn."),
    ("You put code and lock.", False, "Thiếu mạo từ và chi tiết: 'Enter a four-digit code, then press Lock.'"),
  ]),
 ],
 "listen": [
  ("Housekeeping, may I come in", ["Housekeeping", "come"], "gõ cửa dọn phòng"),
  ("I'll bring you some fresh towels", ["bring", "towels"], "mang khăn"),
  ("Please keep your passport in the safe", ["passport", "safe"], "két sắt"),
  ("The maintenance team will check the shower", ["maintenance", "shower"], "báo bảo trì"),
  ("Room 305 has a Do Not Disturb sign. Please go back after two o'clock. The guest also asked for an extra pillow.", ["Disturb", "two", "pillow"], "dặn dò buồng phòng"),
  ("We found a black wallet in room 412. It's now in lost and found. Please call the guest before he leaves for the airport.", ["wallet", "lost", "airport"], "đồ khách bỏ quên"),
 ],
})

# ───────────────────────── 9. Chỉ đường & giới thiệu địa điểm ─────────────────────────
PHASES.append({
 "title": "Chỉ đường & giới thiệu địa điểm",
 "vocab": [
  ("opposite", "/ˈɒpəzɪt/", "prep", "đối diện", "The pharmacy is <b>opposite</b> the hotel.", "Nhà thuốc ở đối diện khách sạn.", "向かい側", "mukaigawa"),
  ("intersection", "/ˌɪntəˈsekʃn/", "n", "ngã tư, giao lộ", "Turn left at the next <b>intersection</b>.", "Rẽ trái ở ngã tư tiếp theo.", "交差点", "kōsaten"),
  ("walking distance", "/ˈwɔːkɪŋ ˌdɪstəns/", "n", "khoảng cách đi bộ được", "The beach is within <b>walking distance</b>.", "Bãi biển gần, đi bộ tới được.", "徒歩圏内", "toho kennai"),
  ("landmark", "/ˈlændmɑːk/", "n", "địa danh, điểm mốc", "The Japanese Bridge is the most famous <b>landmark</b> in Hội An.", "Chùa Cầu là địa danh nổi tiếng nhất ở Hội An.", "名所", "meisho"),
  ("old town", "/ˌəʊld ˈtaʊn/", "n", "phố cổ", "The <b>old town</b> is beautiful at night with all the lanterns.", "Phố cổ về đêm rất đẹp với đèn lồng.", "旧市街", "kyūshigai"),
  ("night market", "/ˈnaɪt ˌmɑːkɪt/", "n", "chợ đêm", "The <b>night market</b> opens at 6 p.m.", "Chợ đêm mở cửa lúc 6 giờ tối."),
  ("pharmacy", "/ˈfɑːməsi/", "n", "nhà thuốc", "Is there a <b>pharmacy</b> near here?", "Gần đây có nhà thuốc không?", "薬局", "yakkyoku"),
  ("ride-hailing app", "/ˈraɪd heɪlɪŋ ˌæp/", "n", "ứng dụng gọi xe", "You can book a car with a <b>ride-hailing app</b>.", "Anh/chị có thể đặt xe bằng ứng dụng gọi xe.", "配車アプリ", "haisha apuri"),
  ("motorbike rental", "/ˈməʊtəbaɪk ˌrentl/", "n", "dịch vụ thuê xe máy", "<b>Motorbike rental</b> is 150,000 dong a day.", "Thuê xe máy giá 150.000 đồng một ngày.", "レンタルバイク", "rentaru baiku"),
  ("traffic lights", "/ˈtræfɪk laɪts/", "n", "đèn giao thông", "Go straight and turn right at the <b>traffic lights</b>.", "Đi thẳng rồi rẽ phải ở chỗ đèn giao thông.", "信号", "shingō"),
 ],
 "phrases": [
  ("Go straight for about 200 metres.", "Đi thẳng khoảng 200 mét."),
  ("Turn left at the traffic lights.", "Rẽ trái ở chỗ đèn giao thông."),
  ("It's on your right, next to the bank.", "Nó ở bên tay phải, cạnh ngân hàng."),
  ("It's about ten minutes on foot.", "Đi bộ khoảng mười phút."),
  ("It's a bit far to walk. I'd suggest taking a taxi.", "Đi bộ thì hơi xa. Anh/chị nên đi taxi."),
  ("Let me show you on the map.", "Để tôi chỉ trên bản đồ cho anh/chị."),
  ("I can call a taxi for you. It's about 100,000 dong.", "Tôi có thể gọi taxi cho anh/chị. Khoảng 100.000 đồng."),
  ("Please be careful when you cross the street.", "Anh/chị cẩn thận khi băng qua đường nhé."),
  ("If you rent a motorbike, you need a helmet and a driving licence.", "Nếu thuê xe máy, anh/chị cần mũ bảo hiểm và bằng lái."),
  ("The old town is best in the evening, when the lanterns are on.", "Phố cổ đẹp nhất vào buổi tối, khi đèn lồng được thắp lên."),
 ],
 "dialogues": [
  ("Excuse me, how do I get to the night market?", [
    ("Go out of the hotel, turn right and walk for about five minutes. It's on your left.", True, "Chỉ đường từng bước + thời gian + vị trí."),
    ("Night market very near.", False, "Thiếu động từ 'is' và không chỉ đường cụ thể."),
    ("You go, go, go, turn.", False, "Chỉ đường bằng cử chỉ, không rõ; nên dùng 'go straight / turn left'."),
  ]),
  ("Is the beach within walking distance?", [
    ("It's about 20 minutes on foot. A taxi takes five minutes and costs about 50,000 dong.", True, "Thời gian đi bộ + lựa chọn khác có giá."),
    ("Yes, walk is OK.", False, "Thiếu thông tin; nên nói mất bao lâu."),
    ("Beach is far, far.", False, "Lặp từ kiểu tiếng Việt 'xa xa', không có số liệu."),
  ]),
  ("Where can I buy some medicine for a headache?", [
    ("There's a pharmacy opposite the hotel. It's open until 10 p.m.", True, "Địa điểm cụ thể + giờ mở cửa."),
    ("You go hospital.", False, "Thiếu 'to the', lại quá mức — đau đầu chỉ cần nhà thuốc."),
    ("Medicine is at pharmacy.", False, "Thiếu mạo từ, không nói nhà thuốc ở đâu."),
  ]),
  ("Is it safe to rent a motorbike here?", [
    ("Yes, but the traffic is busy. Please wear a helmet and ride slowly. You also need a driving licence.", True, "Trả lời trung thực + lời khuyên an toàn + giấy tờ."),
    ("Very safe, no problem.", False, "Hứa hẹn quá mức — nên nhắc mũ bảo hiểm, bằng lái."),
    ("You can rent, but police catch you.", False, "Sai ngữ pháp và doạ khách; nên giải thích cần bằng lái."),
  ]),
  ("What's the best way to get to the airport?", [
    ("I'd recommend our airport transfer. It's 250,000 dong and takes about 30 minutes. Shall I book it for you?", True, "Gợi ý cụ thể + giá + thời gian + đề nghị đặt."),
    ("Many ways, up to you.", False, "Không đưa lời khuyên cụ thể, khách vẫn không biết đi thế nào."),
    ("The airport is have bus.", False, "Dịch từng chữ 'sân bay thì có xe buýt' — nên nói 'There's a bus to the airport.'"),
  ]),
 ],
 "listen": [
  ("Turn left at the traffic lights", ["left", "lights"], "rẽ ở đâu"),
  ("The pharmacy is opposite the hotel", ["pharmacy", "opposite"], "nhà thuốc"),
  ("It's about ten minutes on foot", ["ten", "foot"], "đi bộ bao lâu"),
  ("The night market opens at six", ["night", "six"], "giờ mở chợ đêm"),
  ("Go straight for two blocks and turn right at the intersection. The old town is on your left. You can't miss it.", ["straight", "right", "old"], "chỉ đường đến phố cổ"),
  ("The beach is a bit far to walk. I can call a taxi for you. It takes about fifteen minutes.", ["beach", "taxi", "fifteen"], "gợi ý đi taxi"),
 ],
})

# ───────────────────────── 10. Tour & hướng dẫn viên ─────────────────────────
PHASES.append({
 "title": "Tour & hướng dẫn viên",
 "vocab": [
  ("itinerary", "/aɪˈtɪnərəri/", "n", "lịch trình chuyến đi", "Here is the <b>itinerary</b> for tomorrow's tour.", "Đây là lịch trình tour ngày mai.", "行程表", "kōteihyō"),
  ("meeting point", "/ˈmiːtɪŋ pɔɪnt/", "n", "điểm tập trung", "Our <b>meeting point</b> is the hotel lobby at 7:30.", "Điểm tập trung là sảnh khách sạn lúc 7 giờ 30.", "集合場所", "shūgō basho"),
  ("sightseeing", "/ˈsaɪtsiːɪŋ/", "n", "việc tham quan, ngắm cảnh", "We'll spend the morning <b>sightseeing</b> in Huế.", "Buổi sáng chúng ta sẽ tham quan Huế.", "観光", "kankō"),
  ("entrance fee", "/ˈentrəns fiː/", "n", "phí vào cửa", "The <b>entrance fee</b> is included in the tour price.", "Vé vào cửa đã bao gồm trong giá tour.", "入場料", "nyūjōryō"),
  ("souvenir", "/ˌsuːvəˈnɪə/", "n", "quà lưu niệm", "You can buy <b>souvenirs</b> at the market.", "Quý khách có thể mua quà lưu niệm ở chợ.", "お土産", "omiyage"),
  ("tour guide", "/ˈtʊə ɡaɪd/", "n", "hướng dẫn viên du lịch", "I'm Nam, your <b>tour guide</b> for today.", "Tôi là Nam, hướng dẫn viên của quý khách hôm nay.", "ツアーガイド", "tsuā gaido"),
  ("departure", "/dɪˈpɑːtʃə/", "n", "sự khởi hành", "<b>Departure</b> is at 8 a.m. sharp.", "Xe khởi hành đúng 8 giờ sáng.", "出発", "shuppatsu"),
  ("boat trip", "/ˈbəʊt trɪp/", "n", "chuyến đi thuyền", "The <b>boat trip</b> around Hạ Long Bay takes four hours.", "Chuyến đi thuyền quanh vịnh Hạ Long mất bốn tiếng."),
  ("World Heritage Site", "/ˌwɜːld ˈherɪtɪdʒ saɪt/", "n", "Di sản Thế giới", "Hội An is a UNESCO <b>World Heritage Site</b>.", "Hội An là Di sản Thế giới được UNESCO công nhận.", "世界遺産", "sekai isan"),
  ("sunscreen", "/ˈsʌnskriːn/", "n", "kem chống nắng", "Don't forget your hat and <b>sunscreen</b>.", "Đừng quên mũ và kem chống nắng nhé.", "日焼け止め", "hiyakedome"),
 ],
 "phrases": [
  ("Good morning, everyone! My name is Nam, and I'm your guide today.", "Chào buổi sáng mọi người! Tôi tên là Nam, hướng dẫn viên của quý khách hôm nay."),
  ("Is everybody here? Let's get on the bus.", "Mọi người đủ chưa ạ? Chúng ta lên xe nhé."),
  ("First, we'll visit the Japanese Bridge. Then we'll have lunch.", "Đầu tiên, chúng ta sẽ tham quan Chùa Cầu. Sau đó sẽ ăn trưa."),
  ("You have 45 minutes of free time.", "Quý khách có 45 phút tự do."),
  ("Please be back at the bus by 11:30.", "Quý khách vui lòng quay lại xe trước 11 giờ 30."),
  ("Please stay together and follow the yellow flag.", "Mọi người đi cùng nhau và theo lá cờ vàng nhé."),
  ("This temple was built about 400 years ago.", "Ngôi chùa này được xây khoảng 400 năm trước."),
  ("Please cover your shoulders and knees inside the pagoda.", "Vào chùa quý khách vui lòng che vai và đầu gối."),
  ("Any questions before we start?", "Có ai muốn hỏi gì trước khi bắt đầu không ạ?"),
  ("Thank you for joining the tour today. I hope you enjoyed it!", "Cảm ơn quý khách đã tham gia tour hôm nay. Mong quý khách đã có một ngày vui!"),
 ],
 "dialogues": [
  ("What time do we leave tomorrow?", [
    ("Departure is at 7:30. Please meet in the hotel lobby at 7:15.", True, "Giờ khởi hành + điểm và giờ tập trung."),
    ("Tomorrow early morning.", False, "Mơ hồ, không có giờ cụ thể."),
    ("We leaving at 7:30.", False, "Thiếu 'are': 'We're leaving at 7:30.' — nên nói thêm điểm tập trung."),
  ]),
  ("Is the entrance fee included in the tour price?", [
    ("Yes, all entrance fees and lunch are included. Drinks are extra.", True, "Trả lời rõ cái gì gồm, cái gì không."),
    ("Yes, include all.", False, "Thiếu chủ ngữ và bị động: 'Yes, everything is included.'"),
    ("It's cheap, only 100,000.", False, "Không trả lời có bao gồm hay không."),
  ]),
  ("Can I take photos inside the temple?", [
    ("Yes, but please don't use the flash, and please be quiet. People are praying.", True, "Cho phép + nhắc quy tắc tôn trọng nơi thờ cúng."),
    ("Photo OK, no problem.", False, "Thiếu động từ, không nhắc tôn trọng nơi thờ cúng."),
    ("No can photo.", False, "Dịch từng chữ 'không được chụp': 'Sorry, photos aren't allowed here.'"),
  ]),
  ("I don't feel well. I think I'm seasick.", [
    ("I'm sorry to hear that. Please sit here in the fresh air. I'll get you some water and a seasickness tablet.", True, "Cảm thông + chăm sóc cụ thể."),
    ("Just a little, you are OK.", False, "Coi nhẹ tình trạng của khách."),
    ("Maybe you eat too much.", False, "Đổ lỗi cho khách, thiếu tế nhị."),
  ]),
  ("Where can I buy some good souvenirs?", [
    ("The night market has nice lanterns and silk scarves. You can bargain a little there.", True, "Gợi ý chỗ + món cụ thể + mẹo mặc cả."),
    ("Everywhere have souvenir.", False, "Dịch từng chữ 'chỗ nào cũng có' — nên nói 'There are souvenir shops everywhere' và gợi ý chỗ cụ thể."),
    ("Souvenir is expensive, don't buy.", False, "Khuyên tiêu cực, thiếu 's' số nhiều."),
  ]),
 ],
 "listen": [
  ("Our meeting point is the hotel lobby", ["meeting", "lobby"], "điểm tập trung"),
  ("Please be back at the bus by eleven thirty", ["back", "eleven"], "giờ quay lại xe"),
  ("The entrance fee is included in the price", ["entrance", "included"], "vé vào cửa"),
  ("Don't forget your hat and sunscreen", ["hat", "sunscreen"], "dặn chuẩn bị"),
  ("Good morning, everyone. My name is Nam, and I'm your guide today. First, we'll visit the old town, and then we'll take a boat trip.", ["guide", "visit", "boat"], "hướng dẫn viên mở đầu tour"),
  ("You have forty minutes of free time. Please stay together and follow my yellow flag. We'll meet here at eleven.", ["forty", "yellow", "eleven"], "dặn giờ tự do"),
 ],
})

# ───────────────────────── Vai trong ngành ─────────────────────────
ROLES = {
 "reception": {"label": "Lễ tân", "emoji": "🛎️",
  "scenarios": [
   ("rc_walkin", "Khách vãng lai hỏi phòng", "You are a foreign traveller walking into the hotel without a booking at 10 p.m. Ask if there is a room tonight, the price and whether breakfast is included."),
   ("rc_late", "Khách nhận phòng lúc nửa đêm", "You are a tired guest arriving at midnight after a delayed flight. Check in quickly and ask about room service and the Wi-Fi."),
   ("rc_bill", "Thắc mắc hoá đơn", "You are a guest checking out who thinks the bill is too high. Ask about the minibar charge and the service charge, and stay polite but firm."),
   ("rc_taxi", "Đặt xe & tour", "You are a guest who needs a taxi to the airport tomorrow at 5 a.m. and a day tour to Hội An the day after. Ask me to arrange both and ask the prices."),
  ],
  "dialogues": [
   ("Hello, do you have any rooms for tonight? I don't have a booking.", [
     ("Let me check for you. Yes, we have a double room for 1.4 million dong, including breakfast.", True, "Kiểm tra + loại phòng, giá, quyền lợi."),
     ("Have. One million four.", False, "Thiếu chủ ngữ và đơn vị: 'Yes, we have a room. It's 1.4 million dong.'"),
     ("No booking, cannot.", False, "Sai — khách vãng lai vẫn thuê được nếu còn phòng; lại cộc lốc.")]),
   ("My key card doesn't work.", [
     ("I'm sorry about that. Let me make you a new one. May I see your ID, please?", True, "Xin lỗi + làm lại thẻ + kiểm tra danh tính."),
     ("You put it wrong.", False, "Đổ lỗi cho khách; luôn xin lỗi và làm lại thẻ."),
     ("Card is broken, I make new.", False, "Thiếu mạo từ và 'will': 'I'll make a new one for you.'")]),
   ("Could you keep my bags after I check out? My flight is at night.", [
     ("Of course. We'll keep them in the luggage room. Here's your luggage tag.", True, "Đồng ý + giữ ở đâu + đưa phiếu gửi đồ."),
     ("Yes, you leave here.", False, "Nghe như ra lệnh: 'Sure, you can leave them with us.'"),
     ("Bags keep until what time?", False, "Dịch từng chữ, sai trật tự: 'What time will you pick them up?'")]),
   ("Where can I change money?", [
     ("We can change US dollars here at the front desk, or there's a bank two minutes away.", True, "Đưa hai lựa chọn cụ thể."),
     ("Change money at bank.", False, "Thiếu chủ ngữ và mạo từ; chưa nói ngân hàng ở đâu."),
     ("Money in Vietnam is dong.", False, "Không trả lời câu hỏi đổi tiền ở đâu.")]),
   ("Is there a gym in the hotel?", [
     ("Yes, it's on the third floor, next to the pool. It's open from 6 a.m. to 10 p.m.", True, "Vị trí + giờ mở cửa."),
     ("Yes, have gym floor three.", False, "Thiếu chủ ngữ, sai cấu trúc: 'Yes, there's a gym on the third floor.'"),
     ("Gym is free.", False, "Không nói có hay không, ở đâu.")]),
   ("Can you call a taxi for me? I'm going to the airport.", [
     ("Sure. It'll be here in about ten minutes. The fare is around 200,000 dong.", True, "Đồng ý + thời gian chờ + giá tham khảo."),
     ("OK, you wait.", False, "Cộc lốc; nên nói bao lâu xe đến."),
     ("Taxi is coming ten minutes.", False, "Thiếu 'in': 'The taxi will be here in ten minutes.'")]),
  ]},
 "fnb": {"label": "Nhà hàng · Bar", "emoji": "🍽️",
  "scenarios": [
   ("fb_seat", "Đón khách & xếp bàn", "You are a foreign couple arriving at the hotel restaurant without a booking on a busy night. Ask for a table by the window and ask how long you need to wait."),
   ("fb_order", "Gọi món", "You are a hungry tourist who doesn't know Vietnamese food. Ask me to explain two dishes and recommend something not too spicy."),
   ("fb_wrong", "Mang nhầm món", "You are a guest who got the wrong dish after waiting 30 minutes. Complain politely and ask what I can do."),
   ("fb_bar", "Quầy bar", "You are a hotel guest at the bar in the evening. Ask about local beer, cocktails and happy hour, then ask to charge the drinks to your room."),
  ],
  "dialogues": [
   ("Can we sit outside?", [
     ("Of course. This way, please. Would you like a table near the garden?", True, "Đồng ý + dẫn khách + gợi ý chỗ."),
     ("Outside is hot, inside better.", False, "Áp ý mình lên khách, thiếu động từ 'is'."),
     ("Yes, you sit anywhere.", False, "Không dẫn khách, nghe thiếu chuyên nghiệp.")]),
   ("What's in the spring rolls?", [
     ("They have pork, shrimp, vegetables and glass noodles. They come with a fish sauce dip.", True, "Liệt kê thành phần rõ ràng — quan trọng với khách dị ứng."),
     ("Many things inside.", False, "Mơ hồ, khách không biết có gì (nguy hiểm nếu dị ứng)."),
     ("Spring roll is Vietnamese food.", False, "Không trả lời câu hỏi về thành phần.")]),
   ("Could I have a glass of water, please?", [
     ("Certainly. Still or sparkling?", True, "Đồng ý + hỏi loại nước — chuẩn nhà hàng."),
     ("One water. OK.", False, "Cộc; nên nói 'Certainly' và hỏi loại nước."),
     ("Water is not free.", False, "Nói thẳng quá; nếu tính phí thì báo giá lịch sự.")]),
   ("Excuse me, we've been waiting for our food for 30 minutes.", [
     ("I'm very sorry. Let me check with the kitchen right now. It'll be out in a few minutes.", True, "Xin lỗi + kiểm tra + báo thời gian."),
     ("Kitchen is busy today.", False, "Chỉ giải thích, không xin lỗi, không có giải pháp."),
     ("Sorry, food coming soon.", False, "Thiếu 'the' và 'is'; 'soon' mơ hồ — nên nói bao nhiêu phút.")]),
   ("Can I charge this to my room?", [
     ("Of course. May I have your room number, and could you sign here, please?", True, "Đồng ý + xin số phòng và chữ ký."),
     ("Yes. What your room?", False, "Thiếu 'is' và 'number', nghe cộc: 'May I have your room number, please?'"),
     ("You must pay cash here.", False, "Cứng nhắc và sai quy trình — khách lưu trú thường được ghi vào tiền phòng.")]),
   ("That was delicious, thank you!", [
     ("I'm so glad you enjoyed it! I'll tell the chef.", True, "Vui vẻ đáp lời khen + chuyển lời cho bếp."),
     ("Yes, I know.", False, "Nghe kiêu, không cảm ơn."),
     ("Thank you, you are welcome.", False, "Lẫn lộn: 'You're welcome' dùng để đáp lời cảm ơn, không đáp lời khen.")]),
  ]},
 "housekeeping": {"label": "Buồng phòng", "emoji": "🧹",
  "scenarios": [
   ("hk_clean", "Dọn phòng khi khách có mặt", "You are a guest working in your room when I knock to clean it. Ask me to come back later and ask for fresh towels and bottled water."),
   ("hk_broken", "Báo đồ hỏng", "You are a guest whose TV and hair dryer are not working. Tell me about the problems and ask when someone will repair them."),
   ("hk_lost", "Đồ thất lạc", "You are a guest who left a phone charger in the room after checking out. Call housekeeping, describe it and ask how to get it back."),
   ("hk_amenity", "Xin thêm đồ dùng", "You are a guest with a small child. Ask me for an extra blanket, more pillows, children's slippers and a kettle."),
  ],
  "dialogues": [
   ("Can you clean my room now? I'm going out.", [
     ("Of course. I'll clean it now, and it'll be ready in about thirty minutes.", True, "Đồng ý + thời gian hoàn thành."),
     ("OK, I clean.", False, "Thiếu 'will' và tân ngữ: 'I'll clean it now.'"),
     ("Now is not my time. Afternoon.", False, "Từ chối khách và dịch từng chữ.")]),
   ("Could I get some more coffee and tea bags?", [
     ("Certainly. I'll bring some right away.", True, "Đồng ý + làm ngay."),
     ("One day only two.", False, "Nêu quy định cộc lốc; nếu có giới hạn thì giải thích lịch sự."),
     ("Yes, I bringing.", False, "Sai thì: 'I'll bring them.'")]),
   ("The TV isn't working.", [
     ("I'm sorry. Let me try the remote first. If it still doesn't work, I'll call maintenance.", True, "Xin lỗi + thử trước + phương án tiếp theo."),
     ("TV is old, sorry.", False, "Thừa nhận lỗi nhưng không xử lý."),
     ("Not my job.", False, "Đẩy trách nhiệm, rất thiếu chuyên nghiệp.")]),
   ("Please don't change the towels every day. I want to save water.", [
     ("Thank you, that's very kind. Just hang them up and we'll leave them.", True, "Cảm ơn + hướng dẫn treo khăn."),
     ("OK, no change.", False, "Cộc, thiếu lời cảm ơn."),
     ("But hotel rule is change.", False, "Cứng nhắc; khách sạn thường khuyến khích tiết kiệm nước.")]),
   ("I found a stain on the bed sheet.", [
     ("I'm so sorry. I'll change the sheets for you right now.", True, "Xin lỗi + thay ngay."),
     ("It's not a stain, it's old.", False, "Cãi khách, không giải quyết."),
     ("Sorry, I change tomorrow.", False, "Thiếu 'will' và hẹn quá lâu — nên thay ngay.")]),
   ("Excuse me, what time do you usually clean the rooms?", [
     ("Usually between 9 a.m. and 3 p.m. Would you like a special time?", True, "Khung giờ + hỏi yêu cầu riêng."),
     ("Morning, afternoon.", False, "Mơ hồ, không thành câu."),
     ("We clean when you not here.", False, "Thiếu 'are': 'when you're not here' — lại không nói giờ.")]),
  ]},
 "guide": {"label": "Hướng dẫn viên · Tour", "emoji": "🗺️",
  "scenarios": [
   ("gd_start", "Mở đầu tour", "You are a tourist on my day tour. At the start, ask me about the plan for the day, lunch and when we will come back to the hotel."),
   ("gd_history", "Hỏi về lịch sử", "You are a curious tourist in the old town of Hội An. Ask me about the history of the Japanese Bridge and why the town has so many lanterns."),
   ("gd_late", "Khách về trễ điểm hẹn", "You are a tourist who came back to the bus 20 minutes late. Apologise and explain that you got lost at the market."),
   ("gd_price", "Mặc cả & mua sắm", "You are a tourist at a market with me as your guide. Ask me how to bargain, what a fair price is and what souvenirs to buy."),
  ],
  "dialogues": [
   ("How long does the boat trip take?", [
     ("About three hours. We'll stop at a cave and a floating village.", True, "Thời gian + các điểm dừng."),
     ("Three hour.", False, "Thiếu 's': 'three hours' — và nên nói thêm lịch trình."),
     ("Not long, don't worry.", False, "Mơ hồ, khách cần con số cụ thể.")]),
   ("Can I go to the toilet before we leave?", [
     ("Of course. The toilets are next to the ticket office. We leave in ten minutes.", True, "Chỉ chỗ + nhắc giờ đi."),
     ("Toilet there, quick.", False, "Cộc, giục khách."),
     ("You can go toilet.", False, "Thiếu 'to the': 'You can go to the toilet.'")]),
   ("What does this sign say?", [
     ("It says, 'Please take off your shoes before entering the temple.'", True, "Dịch rõ nội dung biển."),
     ("It say no shoes.", False, "Thiếu 's' ở 'says' và quá cụt."),
     ("Vietnamese words, very difficult.", False, "Không giúp khách hiểu biển.")]),
   ("It's raining. Will the tour still go ahead?", [
     ("Yes, it will. We'll visit the indoor places first, and I have raincoats for everyone.", True, "Trả lời + điều chỉnh lịch trình + chuẩn bị áo mưa."),
     ("Rain is no problem.", False, "Chủ quan, không nói phương án."),
     ("Maybe yes, maybe no.", False, "Mơ hồ, khách không biết chuẩn bị gì.")]),
   ("Is the tap water safe to drink?", [
     ("I'm afraid not. Please drink bottled water. I have some for everyone on the bus.", True, "Cảnh báo + có sẵn giải pháp."),
     ("Yes, drink OK.", False, "Sai thông tin, nguy hiểm cho khách."),
     ("Water is not clean, you buy.", False, "Thiếu mạo từ, nghe cộc; nên nói có nước đóng chai.")]),
   ("Thank you so much for today. You were a great guide!", [
     ("Thank you! It was a pleasure. I hope you enjoy the rest of your trip.", True, "Cảm ơn + chúc tiếp chuyến đi."),
     ("Yes, I am a great guide.", False, "Nhận lời khen thiếu khiêm tốn, nghe kỳ."),
     ("You're welcome. Tip, please.", False, "Đòi tiền boa, rất thiếu chuyên nghiệp.")]),
  ]},
}

PACK = {
 "id": "hotel",
 "label": "Khách sạn · Du lịch",
 "short": "Khách sạn",
 "emoji": "🏨",
 "desc": "Lễ tân · nhà hàng · buồng phòng · tour",
 "persona": "a Vietnamese hotel and tourism worker",
 "counterpart": "a foreign guest",
 "context": "hotel and tourism",
 "core": [10, 11],
 "report": {
  "title": "Giao ca 60 giây", "short": "Giao ca 60s", "sub": "Nói như lúc giao ca 🎙️",
  "steps": [["In my shift", "Twelve guests checked in …"], ["Pending", "Room 305 is waiting for …"], ["Notes", "Please call … / No issues."]],
  "kind": "shift handover report",
  "structure": "what happened in my shift / what is pending / notes for the next shift",
  "sample": "In my shift, twelve guests checked in and five checked out. Room 305 is still waiting for an extra bed, and the guest in room 210 asked for a late check-out. Please call room 210 at 8 a.m. to confirm. The airport transfer for room 412 is at 5:30.",
 },
 "podcast": "Podcast khách sạn",
 "game_tag": "Game anime: đánh quái, hạ boss khách khó tính",
 "reverse_tag": "kiểu khách sạn",
 "jd_placeholder": "VD: Lễ tân khách sạn 4 sao ở Đà Nẵng, khách Hàn/Úc, check-in, đặt tour, xử lý phàn nàn…",
 "rw_placeholder": "VD: phòng 305 chưa dọn xong, khách chờ 30 phút",
 "quips": [
  "Checking in a guest…",
  "Your key card, madam!",
  "Fresh towels on the way!",
  "Pho for table six!",
  "Wake-up call: rise and shine!",
  "Room 305 is ready!",
  "Follow my yellow flag!",
  "Spicy? Just a little!",
  "No vacancy for bad reviews!",
  "Enjoy your stay!",
 ],
 "ai": [
  ("checkin", "Nhận phòng", "You are a foreign guest checking in at the hotel front desk. I am the receptionist. Give your name, then ask about breakfast, the Wi-Fi and the deposit."),
  ("booking", "Đặt phòng qua điện thoại", "You are a foreign tourist calling the hotel to book a room for two people for three nights next month. Ask about the price, breakfast and the cancellation policy."),
  ("checkout", "Trả phòng & thanh toán", "You are a guest checking out. You don't understand one charge on your bill and you want to pay in US dollars. Ask me about both."),
  ("complaint", "Khách phàn nàn", "You are an unhappy hotel guest. Your air conditioner is broken and the room is noisy. Complain politely but firmly and ask what I will do about it."),
  ("restaurant", "Gọi món nhà hàng", "You are a foreign guest in the hotel restaurant. Ask me for a recommendation, ask if a dish is spicy and tell me you are allergic to peanuts."),
  ("directions", "Hỏi đường", "You are a tourist asking me, the receptionist, how to get to the old town and the night market, and whether it is safe to rent a motorbike."),
  ("tour", "Hỏi về tour", "You are a guest interested in a day tour to Hạ Long Bay. Ask about the itinerary, the departure time, the price and what is included."),
  ("request", "Yêu cầu đặc biệt", "You are a guest celebrating your wedding anniversary at the hotel. Ask what the hotel can do to make it special, and ask for a late check-out."),
 ],
 "rev": [
  ("Phòng của anh ở tầng năm.", "Your room is on the fifth floor."),
  ("Cho tôi xem hộ chiếu của anh/chị được không?", "May I see your passport, please?"),
  ("Bữa sáng phục vụ từ 6 đến 10 giờ.", "Breakfast is served from 6 to 10."),
  ("Xin lỗi, tối nay khách sạn đã kín phòng.", "Sorry, we're fully booked tonight."),
  ("Anh/chị muốn trả bằng thẻ hay tiền mặt?", "Would you like to pay by card or in cash?"),
  ("Tôi sẽ cho người lên phòng ngay.", "I'll send someone to your room right away."),
  ("Chúng tôi rất xin lỗi vì sự bất tiện này.", "We're very sorry for the inconvenience."),
  ("Anh/chị gọi món được chưa ạ?", "Are you ready to order?"),
  ("Món này hơi cay.", "This dish is a little spicy."),
  ("Anh/chị có dị ứng món gì không?", "Do you have any food allergies?"),
  ("Rẽ trái ở chỗ đèn giao thông.", "Turn left at the traffic lights."),
  ("Đi bộ khoảng mười phút.", "It's about ten minutes on foot."),
  ("Xe khởi hành lúc bảy giờ rưỡi.", "The bus leaves at seven thirty."),
  ("Tôi mang thêm khăn lên cho anh/chị nhé.", "I'll bring you some more towels."),
 ],
 "reading": [
  {"t": "Booking email", "text": "Dear Hoa Sen Hotel,\nI'd like to book a double room for two adults from Friday, March 14 to Monday, March 17. We arrive by train at about 9 p.m. Could you also arrange a car to the airport on Monday morning?\nBest regards,\nAnna Weber", "q": [
    {"q": "How many nights will the guests stay?", "o": ["Two", "Three", "Four"], "a": 1},
    {"q": "What does Anna ask the hotel to arrange?", "o": ["A train ticket", "A late check-in", "A car to the airport"], "a": 2}]},
  {"t": "Pool notice", "text": "SWIMMING POOL\nThe pool is open from 6 a.m. to 8 p.m. every day. On Wednesday, June 5, it will be closed from 1 to 4 p.m. for cleaning. Towels are available at the pool bar. Children under 12 must be with an adult.", "q": [
    {"q": "When is the pool closed on June 5?", "o": ["All day", "From 1 to 4 p.m.", "After 8 p.m."], "a": 1},
    {"q": "Where can guests get towels?", "o": ["At the pool bar", "At reception", "Only in their room"], "a": 0}]},
  {"t": "Lunch menu", "text": "LOTUS RESTAURANT – SET LUNCH 250,000 VND\nStarter: spring rolls (contain peanuts) or green papaya salad (no peanuts)\nMain: grilled chicken with rice or tofu curry (V)\nDessert: fresh fruit\n(V) = vegetarian. Prices include service charge.", "q": [
    {"q": "Which main dish is vegetarian?", "o": ["Grilled chicken", "Spring rolls", "Tofu curry"], "a": 2},
    {"q": "Which starter is NOT OK for someone allergic to peanuts?", "o": ["Spring rolls", "Green papaya salad", "Neither of them"], "a": 0}]},
  {"t": "Staff chat", "text": "Linh (Housekeeping): Hi front desk, room 507 still has a Do Not Disturb sign and it's already 3 p.m. The guest checks out tomorrow. Could you call the room and ask if they want cleaning today? Thanks!", "q": [
    {"q": "What is the situation in room 507?", "o": ["The room is very dirty", "There is a Do Not Disturb sign", "The guest lost the key"], "a": 1},
    {"q": "What does Linh ask the front desk to do?", "o": ["Call the guest", "Clean the room", "Check the guest out"], "a": 0}]},
  {"t": "Tour voucher", "text": "HỘI AN DAY TOUR – VOUCHER\nGuest: Mr. Tom Hill (2 adults)\nPick-up: hotel lobby, 7:45 a.m.\nIncluded: guide, entrance tickets, lunch, boat ride\nNot included: drinks, tips\nPlease bring a hat and sunscreen.", "q": [
    {"q": "Where will the guests be picked up?", "o": ["In the old town", "In the hotel lobby", "At the boat station"], "a": 1},
    {"q": "What must the guests pay for themselves?", "o": ["Lunch", "Entrance tickets", "Drinks"], "a": 2}]},
 ],
 "events": [
  ("vip", "Đón đoàn khách VIP", "You are the tour leader of a VIP group of 20 guests arriving tomorrow. Ask me about the rooms, the schedule and special requests."),
  ("wedding", "Tiệc cưới ở khách sạn", "You are a foreign couple planning a small wedding party at our hotel next month. Ask about the party room, the menu and the prices."),
  ("inspection", "Đoàn kiểm tra chất lượng", "You are a hotel quality inspector visiting tomorrow. Ask me how we check rooms, handle guest complaints and train new staff."),
  ("interview", "Phỏng vấn làm khách sạn", "You are the HR manager of a 5-star resort interviewing me for a front desk job. Ask about my experience, my English and how I would handle an angry guest."),
  ("group", "Đoàn tour ăn tối", "You are a tour leader bringing a group of 30 tourists for dinner tonight. Ask about the set menu, vegetarian options and how to pay the bill."),
  ("peak", "Mùa cao điểm Tết", "You are a guest who wants to book during the Tết holiday when the hotel is almost full. Ask about availability, higher prices and what is open during Tết."),
  ("other", "Khác", ""),
 ],
 "roles": ROLES,
 "phases": PHASES,
}
