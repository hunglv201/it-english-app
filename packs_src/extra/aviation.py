# -*- coding: utf-8 -*-
# v4.1 — nội dung làm giàu cho gói aviation (nối vào cuối gói, xem build.py)
# Không nêu chính sách/phí/quy định thật của hãng nào — luôn nói chung ("let me check the fare rules").

PHASES = []

# ───────────────────────── 11. Mua vé, đổi vé & hoàn vé ─────────────────────────
PHASES.append({
 "title": "Mua vé, đổi vé & hoàn vé",
 "vocab": [
  ("fare", "/feə/", "n", "giá vé", "The <b>fare</b> for this flight is shown on the screen.", "Giá vé của chuyến bay này hiển thị trên màn hình.", "運賃", "unchin"),
  ("one-way", "/ˌwʌn ˈweɪ/", "adj", "một chiều", "Would you like a <b>one-way</b> or a return ticket?", "Anh/chị muốn vé một chiều hay vé khứ hồi ạ?", "片道", "katamichi"),
  ("itinerary", "/aɪˈtɪnərəri/", "n", "lịch trình bay (hành trình)", "I'll email you the new <b>itinerary</b>.", "Tôi sẽ gửi email lịch trình bay mới cho anh/chị.", "旅程表", "ryoteihyō"),
  ("ticket desk", "/ˈtɪkɪt desk/", "n", "quầy bán vé", "You can buy a ticket at the <b>ticket desk</b> on the first floor.", "Anh/chị có thể mua vé ở quầy bán vé tầng một."),
  ("change fee", "/ˈtʃeɪndʒ fiː/", "n", "phí đổi vé", "There is a <b>change fee</b> for this ticket.", "Vé này có tính phí đổi vé.", "変更手数料", "henkō tesūryō"),
  ("fare difference", "/ˈfeə ˌdɪfrəns/", "n", "tiền chênh lệch giá vé", "You also need to pay the <b>fare difference</b>.", "Anh/chị cũng cần trả tiền chênh lệch giá vé.", "差額", "sagaku"),
  ("refund", "/ˈriːfʌnd/", "n", "khoản tiền hoàn lại", "Your <b>refund</b> will take 7 to 14 working days.", "Tiền hoàn của anh/chị sẽ mất từ 7 đến 14 ngày làm việc.", "払い戻し", "haraimodoshi"),
  ("non-refundable", "/ˌnɒn rɪˈfʌndəbl/", "adj", "không được hoàn tiền", "I'm afraid this ticket is <b>non-refundable</b>.", "Tôi e là vé này không được hoàn tiền.", "払い戻し不可", "haraimodoshi fuka"),
  ("issue", "/ˈɪʃuː/", "v", "xuất (vé)", "I'll <b>issue</b> your new ticket now.", "Tôi sẽ xuất vé mới cho anh/chị ngay bây giờ.", "発券する", "hakken suru"),
  ("travel agent", "/ˈtrævl ˌeɪdʒənt/", "n", "đại lý vé, đại lý du lịch", "You booked through a <b>travel agent</b>, so please contact them for a refund.", "Anh/chị đặt vé qua đại lý nên vui lòng liên hệ đại lý để hoàn vé.", "旅行代理店", "ryokō dairiten"),
 ],
 "phrases": [
  ("Would you like a one-way or a return ticket?", "Anh/chị muốn vé một chiều hay vé khứ hồi ạ?"),
  ("Let me check the fare rules for your ticket.", "Để tôi kiểm tra điều kiện giá vé của anh/chị."),
  ("You can change the date, but there is a change fee.", "Anh/chị đổi được ngày bay, nhưng có tính phí đổi vé."),
  ("You also need to pay the fare difference.", "Anh/chị cũng cần trả tiền chênh lệch giá vé."),
  ("I'm afraid this ticket is non-refundable.", "Tôi e là vé này không được hoàn tiền."),
  ("You can still get the airport taxes back.", "Anh/chị vẫn được hoàn lại tiền thuế sân bay."),
  ("The refund will go back to the card you paid with.", "Tiền hoàn sẽ trả về thẻ anh/chị đã dùng để thanh toán."),
  ("Your new ticket has been issued. I'll email you the itinerary.", "Vé mới của anh/chị đã được xuất. Tôi sẽ gửi lịch trình bay qua email."),
  ("Since you booked through a travel agent, please contact them first.", "Vì anh/chị đặt qua đại lý, anh/chị vui lòng liên hệ đại lý trước."),
 ],
 "dialogues": [
  ("I'd like to change my flight to Friday.", [
    ("Let me check. There's a seat on Friday at 9:40. The change fee and the fare difference are shown on this screen.", True, "Kiểm tra + đưa chuyến cụ thể + chỉ rõ phí đổi và tiền chênh lệch."),
    ("Friday OK, pay more.", False, "Cộc lốc, thiếu chủ ngữ; nên nói rõ giờ bay và các khoản phí."),
    ("You must buy new ticket.", False, "Sai thông tin (vé đổi được) và thiếu mạo từ 'a new ticket'."),
  ]),
  ("Can I get my money back? I can't travel next week.", [
    ("Let me check your fare rules. I'm afraid this ticket is non-refundable, but you can still get the airport taxes back.", True, "Kiểm tra điều kiện vé + báo tin xấu lịch sự + nói phần vẫn được hoàn."),
    ("No money back, sorry.", False, "Trả lời cộc khi chưa kiểm tra, lại bỏ qua phần thuế vẫn được hoàn."),
    ("Yes, I give you money now.", False, "Thiếu 'will' và hứa hoàn tiền khi chưa xem điều kiện vé."),
  ]),
  ("How long does the refund take?", [
    ("It usually takes 7 to 14 working days. The money will go back to the card you paid with.", True, "Nói khoảng thời gian cụ thể + tiền về đâu."),
    ("Very fast, maybe tomorrow.", False, "Hứa bừa về thời gian — khách sẽ gọi lại phàn nàn."),
    ("Refund take long time.", False, "Thiếu 's' ('takes') và 'a'; không nói bao nhiêu ngày."),
  ]),
  ("I bought this ticket from a travel agent. Can you change it here?", [
    ("I'm sorry, we can't change it here because the agent issued it. Please contact your travel agent, and they can change it for you.", True, "Xin lỗi + lý do (đại lý xuất vé) + chỉ đúng nơi xử lý."),
    ("Travel agent not our business.", False, "Thiếu động từ 'is' và nghe như phủi trách nhiệm."),
    ("Yes, I change for you.", False, "Thiếu 'can/will' và tân ngữ 'it'; lại hứa khi chưa kiểm tra."),
  ]),
  ("Is it cheaper to buy a return ticket?", [
    ("Sometimes it is. Let me check both prices for you. A return ticket is 3.2 million dong, and two one-way tickets are 3.8 million.", True, "Không đoán — kiểm tra rồi so sánh bằng con số cụ thể."),
    ("Return is cheap more.", False, "Sai so sánh hơn: 'cheaper', không phải 'cheap more'."),
    ("I don't know, you check online.", False, "Đẩy việc cho khách; nhân viên quầy vé nên tự kiểm tra giá."),
  ]),
 ],
 "listen": [
  ("I'd like to change my flight to Friday", ["change", "Friday"], "đổi ngày bay"),
  ("There is a change fee for this ticket", ["fee", "ticket"], "phí đổi vé"),
  ("I'm afraid this ticket is non-refundable", ["afraid", "non-refundable"], "vé không hoàn tiền"),
  ("Your new ticket has been issued", ["new", "issued"], "xuất vé mới"),
  ("I can move you to the Friday flight at nine forty. You need to pay the fare difference and a change fee. I'll email you the new itinerary.", ["Friday", "difference", "itinerary"], "đổi chuyến sang thứ Sáu"),
  ("Your ticket is non-refundable, but you can get the airport taxes back. The money will go back to your card in about two weeks.", ["taxes", "card", "weeks"], "giải thích hoàn tiền"),
 ],
})

# ───────────────────────── 12. Phòng chờ hạng thương gia ─────────────────────────
PHASES.append({
 "title": "Phòng chờ hạng thương gia",
 "vocab": [
  ("lounge", "/laʊndʒ/", "n", "phòng chờ (hạng thương gia)", "The <b>lounge</b> is open from 5 a.m. to midnight.", "Phòng chờ mở cửa từ 5 giờ sáng đến nửa đêm.", "ラウンジ", "raunji"),
  ("frequent flyer", "/ˌfriːkwənt ˈflaɪə/", "n", "khách bay thường xuyên (hội viên)", "As a gold <b>frequent flyer</b>, you can use the lounge.", "Là hội viên hạng vàng, anh/chị được dùng phòng chờ."),
  ("membership card", "/ˈmembəʃɪp kɑːd/", "n", "thẻ hội viên", "May I see your <b>membership card</b>, please?", "Cho tôi xem thẻ hội viên của anh/chị được không ạ?", "会員カード", "kaiin kādo"),
  ("access", "/ˈækses/", "n", "quyền ra vào, quyền sử dụng", "Your ticket includes lounge <b>access</b>.", "Vé của anh/chị bao gồm quyền vào phòng chờ."),
  ("eligible", "/ˈelɪdʒəbl/", "adj", "đủ điều kiện", "I'm sorry, this ticket isn't <b>eligible</b> for the lounge.", "Xin lỗi, vé này không đủ điều kiện vào phòng chờ."),
  ("guest", "/ɡest/", "n", "khách đi cùng", "Your card allows you to bring one <b>guest</b>.", "Thẻ của anh/chị được dẫn theo một khách đi cùng.", "同伴者", "dōhansha"),
  ("complimentary", "/ˌkɒmplɪˈmentri/", "adj", "miễn phí (tặng kèm)", "All drinks in the lounge are <b>complimentary</b>.", "Tất cả đồ uống trong phòng chờ đều miễn phí.", "無料", "muryō"),
  ("buffet", "/ˈbʊfeɪ/", "n", "quầy đồ ăn tự chọn", "The hot <b>buffet</b> is on your right.", "Quầy đồ ăn nóng tự chọn ở bên tay phải anh/chị.", "ビュッフェ", "byuffe"),
  ("shower room", "/ˈʃaʊə ruːm/", "n", "phòng tắm vòi sen", "The <b>shower room</b> will be ready in ten minutes.", "Mười phút nữa phòng tắm sẽ sẵn sàng.", "シャワールーム", "shawā rūmu"),
  ("quiet zone", "/ˈkwaɪət zəʊn/", "n", "khu yên tĩnh", "Please keep your voice down in the <b>quiet zone</b>.", "Anh/chị vui lòng nói nhỏ trong khu yên tĩnh."),
 ],
 "phrases": [
  ("Welcome to the lounge. May I see your boarding pass, please?", "Chào mừng anh/chị đến phòng chờ. Cho tôi xem thẻ lên máy bay được không ạ?"),
  ("Your ticket includes lounge access.", "Vé của anh/chị bao gồm quyền vào phòng chờ."),
  ("I'm sorry, this ticket isn't eligible for the lounge.", "Xin lỗi, vé này không đủ điều kiện vào phòng chờ."),
  ("Your card allows one guest.", "Thẻ của anh/chị được dẫn theo một khách."),
  ("The buffet and drinks are complimentary. Please help yourself.", "Đồ ăn tự chọn và đồ uống đều miễn phí. Anh/chị cứ tự nhiên ạ."),
  ("Would you like to book a shower room?", "Anh/chị có muốn đặt phòng tắm không ạ?"),
  ("The Wi-Fi password is on this card.", "Mật khẩu Wi-Fi ghi trên tấm thẻ này ạ."),
  ("We don't make boarding announcements in the lounge, so please check the screens.", "Phòng chờ không phát thông báo lên máy bay, anh/chị vui lòng theo dõi màn hình."),
  ("Your gate is a ten-minute walk, so please leave by 9:30.", "Cửa ra máy bay cách đây mười phút đi bộ, anh/chị vui lòng rời phòng chờ trước 9 giờ 30."),
  ("I'll let you know if there is any change to your flight.", "Nếu chuyến bay có thay đổi, tôi sẽ báo anh/chị."),
 ],
 "dialogues": [
  ("Hi, can I use the lounge? I'm flying business class.", [
    ("Welcome. May I see your boarding pass, please? ... Thank you, please come in. The buffet is on your right.", True, "Chào + kiểm tra thẻ lên máy bay + mời vào và chỉ chỗ."),
    ("Business, OK, go in.", False, "Cộc lốc và cho vào khi chưa kiểm tra thẻ lên máy bay."),
    ("You have card?", False, "Thiếu 'Do' và 'a'; khách hạng thương gia chỉ cần thẻ lên máy bay."),
  ]),
  ("Can my wife come in with me? She's flying economy.", [
    ("Let me check your membership. Yes, your card allows one guest, so she's welcome too.", True, "Kiểm tra quyền lợi hội viên trước khi trả lời + mời cả hai vào."),
    ("Economy no.", False, "Cộc, chưa kiểm tra quyền dẫn khách của thẻ hội viên."),
    ("Your wife must pay 100 dollars.", False, "Tự đặt giá bừa — phải kiểm tra chính sách và bảng phí."),
  ]),
  ("Will you tell me when my flight is boarding?", [
    ("We don't make boarding announcements here, but the screens show all the gate information. Your gate is ten minutes away, so please leave by 10:20.", True, "Giải thích đúng quy định + chỉ màn hình + nói giờ nên rời đi."),
    ("Yes, I call you.", False, "Thiếu 'will' và hứa điều phòng chờ không làm — khách có thể lỡ chuyến."),
    ("You look screen yourself.", False, "Cộc, thiếu 'at the'; nên giải thích và nhắc giờ rời phòng chờ."),
  ]),
  ("Is there somewhere I can take a shower?", [
    ("Yes, we have shower rooms. The next one will be free in about 15 minutes. May I have your name? I'll let you know when it's ready.", True, "Có dịch vụ + thời gian chờ + ghi tên để báo lại."),
    ("Shower full now.", False, "Thiếu động từ và không đưa phương án chờ."),
    ("Yes, you go shower.", False, "Thiếu 'can' và 'take a'; lại không chỉ chỗ hay thời gian."),
  ]),
  ("Sorry, is this food free, or do I have to pay?", [
    ("It's all complimentary. Please help yourself to the buffet and drinks.", True, "Trả lời rõ + mời khách tự nhiên."),
    ("Free, free, eat.", False, "Cụt lủn, lặp từ; nên nói 'It's complimentary. Please help yourself.'"),
    ("Food is not money.", False, "Dịch từng chữ 'không mất tiền', người bản xứ không hiểu."),
  ]),
 ],
 "listen": [
  ("Your ticket includes lounge access", ["includes", "access"], "quyền vào phòng chờ"),
  ("The buffet and drinks are complimentary", ["buffet", "complimentary"], "đồ ăn miễn phí"),
  ("Would you like to book a shower room", ["book", "shower"], "đặt phòng tắm"),
  ("Please keep your voice down in the quiet zone", ["voice", "quiet"], "khu yên tĩnh"),
  ("Welcome to the lounge. The buffet is on your right, and the shower rooms are at the back. We don't make boarding announcements, so please check the screens.", ["right", "shower", "screens"], "chào khách vào phòng chờ"),
  ("I'm sorry, your ticket isn't eligible for the lounge. You can buy a lounge pass at the front desk. Or you can wait at the food court near Gate ten.", ["eligible", "pass", "food"], "khách không đủ điều kiện"),
 ],
})

# ───────────────────────── 13. Bán hàng miễn thuế trên máy bay ─────────────────────────
PHASES.append({
 "title": "Bán hàng miễn thuế trên máy bay",
 "vocab": [
  ("trolley", "/ˈtrɒli/", "n", "xe đẩy (phục vụ trên máy bay)", "The duty-free <b>trolley</b> is coming down the aisle.", "Xe đẩy hàng miễn thuế đang đi dọc lối đi.", "カート", "kāto"),
  ("catalogue", "/ˈkætəlɒɡ/", "n", "cuốn danh mục hàng", "All the items are in the <b>catalogue</b> in your seat pocket.", "Tất cả mặt hàng có trong cuốn danh mục ở túi lưng ghế.", "カタログ", "katarogu"),
  ("currency", "/ˈkʌrənsi/", "n", "loại tiền tệ", "We accept three <b>currencies</b>: dong, US dollars and euros.", "Chúng tôi nhận ba loại tiền: đồng, đô la Mỹ và euro.", "通貨", "tsūka"),
  ("exchange rate", "/ɪksˈtʃeɪndʒ reɪt/", "n", "tỉ giá", "The <b>exchange rate</b> is on the back of the catalogue.", "Tỉ giá in ở mặt sau cuốn danh mục.", "為替レート", "kawase rēto"),
  ("receipt", "/rɪˈsiːt/", "n", "hoá đơn, biên lai", "Here is your <b>receipt</b>. Thank you.", "Đây là hoá đơn của anh/chị. Cảm ơn anh/chị.", "領収書", "ryōshūsho"),
  ("pre-order", "/ˌpriː ˈɔːdə/", "v", "đặt hàng trước", "You can <b>pre-order</b> duty-free items online before your flight.", "Anh/chị có thể đặt trước hàng miễn thuế trên mạng trước chuyến bay."),
  ("out of stock", "/ˌaʊt əv ˈstɒk/", "adj", "hết hàng", "I'm sorry, this perfume is <b>out of stock</b>.", "Xin lỗi, loại nước hoa này hết hàng rồi ạ.", "在庫切れ", "zaiko gire"),
  ("perfume", "/ˈpɜːfjuːm/", "n", "nước hoa", "This <b>perfume</b> comes in 50 ml and 100 ml.", "Loại nước hoa này có chai 50 ml và 100 ml.", "香水", "kōsui"),
  ("card machine", "/ˈkɑːd məˌʃiːn/", "n", "máy quẹt thẻ", "The <b>card machine</b> works offline, so it may take a minute.", "Máy quẹt thẻ chạy ngoại tuyến nên có thể mất một phút."),
  ("sealed bag", "/ˌsiːld ˈbæɡ/", "n", "túi niêm phong", "Please keep the bottle in the <b>sealed bag</b> until your final destination.", "Anh/chị vui lòng giữ chai trong túi niêm phong đến điểm đến cuối cùng."),
 ],
 "phrases": [
  ("Our duty-free trolley is now coming through the cabin.", "Xe hàng miễn thuế đang đi qua khoang khách."),
  ("Would you like anything from duty-free today?", "Hôm nay anh/chị có muốn mua gì ở hàng miễn thuế không ạ?"),
  ("You can find all the items in the catalogue in your seat pocket.", "Anh/chị xem tất cả mặt hàng trong cuốn danh mục ở túi lưng ghế."),
  ("How would you like to pay, by card or in cash?", "Anh/chị muốn thanh toán bằng thẻ hay tiền mặt ạ?"),
  ("We accept US dollars, euros and Vietnamese dong.", "Chúng tôi nhận đô la Mỹ, euro và đồng Việt Nam."),
  ("I'm sorry, we only accept notes, not coins.", "Xin lỗi, chúng tôi chỉ nhận tiền giấy, không nhận tiền xu."),
  ("Your change will be in dong. Is that OK?", "Tiền thừa sẽ trả bằng tiền đồng. Như vậy được không ạ?"),
  ("I'm sorry, that one is out of stock. Would you like a different size?", "Xin lỗi, loại đó hết hàng rồi. Anh/chị có muốn lấy cỡ khác không ạ?"),
  ("If you have a connecting flight, please keep the bottle in the sealed bag.", "Nếu anh/chị có chuyến bay nối tiếp, vui lòng giữ chai trong túi niêm phong."),
  ("Here is your receipt. Thank you for shopping with us.", "Đây là hoá đơn của anh/chị. Cảm ơn anh/chị đã mua hàng."),
 ],
 "dialogues": [
  ("Do you have this perfume on the plane? It's on page 12.", [
    ("Let me check the trolley. Yes, we have it in 50 ml. It's 65 US dollars.", True, "Kiểm tra xe hàng + xác nhận có hàng + cỡ và giá."),
    ("Have, have.", False, "Dịch từng chữ 'có, có'; nên nói 'Yes, we have it.'"),
    ("Page 12 is perfume.", False, "Nhắc lại điều khách đã biết, không trả lời có hàng hay không."),
  ]),
  ("Can I pay in Japanese yen?", [
    ("I'm sorry, we only accept dong, US dollars and euros. You can also pay by card.", True, "Xin lỗi + nói các loại tiền nhận + phương án thẻ."),
    ("No yen.", False, "Cộc lốc, không đưa phương án thanh toán khác."),
    ("Yes, all money OK.", False, "Sai thông tin — chỉ nhận một số loại tiền nhất định."),
  ]),
  ("Why is the card machine taking so long?", [
    ("I'm sorry for the wait. The machine works offline in the air, so it's a little slower. It will be done in a moment.", True, "Xin lỗi + giải thích lý do + trấn an."),
    ("Machine old, sorry.", False, "Thiếu 'is' và đổ lỗi cho máy, không giải thích."),
    ("Maybe your card no money.", False, "Đoán bừa, rất bất lịch sự và thiếu động từ 'has'."),
  ]),
  ("I have a connecting flight to London. Can I take this whisky with me?", [
    ("Yes, but please keep it in the sealed bag with the receipt inside. Don't open the bag before your final destination.", True, "Cho phép + điều kiện túi niêm phong và hoá đơn khi nối chuyến."),
    ("No problem, open bag OK.", False, "Sai — mở túi niêm phong có thể bị giữ chai khi soi chiếu lúc nối chuyến."),
    ("You drink before transit.", False, "Lời khuyên vô lý và thiếu tân ngữ 'it'."),
  ]),
  ("Can I buy the chocolate on my flight back instead?", [
    ("Of course. You can also pre-order it online, and we'll bring it to your seat on the return flight.", True, "Đồng ý + gợi ý đặt trước để chắc có hàng."),
    ("Back flight maybe no chocolate.", False, "Dịch từng chữ, mơ hồ; nên gợi ý đặt trước."),
    ("You buy now better.", False, "Sai cấu trúc ('It's better to buy it now') và ép khách mua."),
  ]),
 ],
 "listen": [
  ("The duty-free trolley is coming through the cabin", ["trolley", "cabin"], "xe hàng miễn thuế"),
  ("All the items are in the catalogue", ["items", "catalogue"], "cuốn danh mục hàng"),
  ("We accept cards, US dollars and euros", ["cards", "euros"], "hình thức thanh toán"),
  ("I'm sorry, this size is out of stock", ["size", "stock"], "hết hàng"),
  ("Ladies and gentlemen, our duty-free trolley will come through the cabin in a few minutes. You can pay by card or in cash. We only accept notes, not coins.", ["trolley", "cash", "coins"], "thông báo bán hàng miễn thuế"),
  ("Here is your whisky and your receipt. The bottle is in a sealed bag. Please don't open it before your final destination.", ["receipt", "sealed", "open"], "giao hàng cho khách nối chuyến"),
 ],
})

# ───────────────────────── 14. Hành khách gây rối ─────────────────────────
PHASES.append({
 "title": "Hành khách gây rối",
 "vocab": [
  ("disruptive", "/dɪsˈrʌptɪv/", "adj", "gây rối, gây mất trật tự", "We have a <b>disruptive</b> passenger in row 22.", "Chúng ta có một hành khách gây rối ở hàng 22."),
  ("intoxicated", "/ɪnˈtɒksɪkeɪtɪd/", "adj", "say xỉn", "We can't board a passenger who is <b>intoxicated</b>.", "Chúng ta không thể cho hành khách đang say xỉn lên máy bay."),
  ("alcohol", "/ˈælkəhɒl/", "n", "đồ uống có cồn, rượu bia", "I'm sorry, I can't serve you any more <b>alcohol</b>.", "Xin lỗi, tôi không thể phục vụ thêm đồ uống có cồn cho anh.", "アルコール", "arukōru"),
  ("behaviour", "/bɪˈheɪvjə/", "n", "hành vi, cách cư xử", "Your <b>behaviour</b> is upsetting other passengers.", "Hành vi của anh đang làm phiền các hành khách khác."),
  ("warning", "/ˈwɔːnɪŋ/", "n", "lời cảnh cáo", "This is a formal <b>warning</b> from the captain.", "Đây là lời cảnh cáo chính thức từ cơ trưởng.", "警告", "keikoku"),
  ("instructions", "/ɪnˈstrʌkʃnz/", "n", "chỉ dẫn, hướng dẫn", "Please follow the crew's <b>instructions</b>.", "Anh vui lòng làm theo hướng dẫn của tổ bay.", "指示", "shiji"),
  ("purser", "/ˈpɜːsə/", "n", "tiếp viên trưởng", "I'll ask the <b>purser</b> to come and help.", "Tôi sẽ nhờ tiếp viên trưởng đến hỗ trợ.", "チーフパーサー", "chīfu pāsā"),
  ("captain", "/ˈkæptɪn/", "n", "cơ trưởng", "I have to inform the <b>captain</b> about this.", "Tôi phải báo việc này cho cơ trưởng.", "機長", "kichō"),
  ("incident report", "/ˈɪnsɪdənt rɪˌpɔːt/", "n", "biên bản sự việc", "I'll write an <b>incident report</b> after landing.", "Tôi sẽ viết biên bản sự việc sau khi hạ cánh."),
  ("vape", "/veɪp/", "v", "hút thuốc lá điện tử", "You can't <b>vape</b> on board, even in the lavatory.", "Anh/chị không được hút thuốc lá điện tử trên máy bay, kể cả trong nhà vệ sinh."),
 ],
 "phrases": [
  ("Sir, please lower your voice. Other passengers are trying to sleep.", "Thưa anh, anh vui lòng nói nhỏ lại. Các hành khách khác đang cố ngủ."),
  ("I understand you're upset. How can I help?", "Tôi hiểu anh đang bực. Tôi có thể giúp gì ạ?"),
  ("I'm sorry, I can't serve you any more alcohol. Would you like some water?", "Xin lỗi, tôi không thể phục vụ thêm rượu cho anh. Anh có muốn uống nước không ạ?"),
  ("Please return to your seat and fasten your seat belt.", "Anh vui lòng về chỗ và thắt dây an toàn."),
  ("Smoking and vaping are not allowed anywhere on board.", "Không được hút thuốc hay thuốc lá điện tử ở bất kỳ đâu trên máy bay."),
  ("Please follow the crew's instructions.", "Anh vui lòng làm theo hướng dẫn của tổ bay."),
  ("If this continues, I will have to inform the captain.", "Nếu việc này tiếp diễn, tôi buộc phải báo cơ trưởng."),
  ("This is a formal warning from the captain.", "Đây là lời cảnh cáo chính thức từ cơ trưởng."),
  ("Would you like to move to another seat?", "Anh/chị có muốn chuyển sang ghế khác không ạ?"),
  ("The police will meet the aircraft on arrival.", "Cảnh sát sẽ chờ ở máy bay khi hạ cánh."),
 ],
 "dialogues": [
  ("Another whisky! Now!", [
    ("I'm sorry, sir, I can't serve you any more alcohol. Can I get you some water or coffee instead?", True, "Từ chối lịch sự nhưng rõ ràng + đưa đồ uống thay thế."),
    ("OK, last one.", False, "Nhượng bộ khách đã say — trái quy trình và làm tình hình tệ hơn."),
    ("You drunk, stop drink!", False, "Thiếu 'are', sai dạng 'drinking' và xúc phạm khách, dễ gây căng thẳng."),
  ]),
  ("The passenger in 22C is still shouting. What happened?", [
    ("He's had a lot to drink, and he shouted at the woman next to him. I've stopped serving him alcohol and moved her to 30A.", True, "Báo đủ: chuyện gì xảy ra + đã làm gì — đúng kiểu báo cáo cho tiếp viên trưởng."),
    ("He crazy man.", False, "Thiếu 'is a', phán xét thay vì kể sự việc."),
    ("Nothing, I don't know.", False, "Không báo cáo — tiếp viên trưởng cần thông tin để xử lý."),
  ]),
  ("I can smell smoke from the lavatory!", [
    ("Thank you for telling me. I'll check it right away. Please stay in your seat.", True, "Cảm ơn + kiểm tra ngay — khói trên máy bay luôn phải xử lý khẩn."),
    ("Maybe perfume, don't worry.", False, "Coi nhẹ nguy cơ cháy — rất nguy hiểm."),
    ("Smoke? You go see.", False, "Đẩy việc cho khách, thiếu 'and'; tiếp viên phải tự kiểm tra."),
  ]),
  ("I'm not going to sit down. You can't tell me what to do!", [
    ("Sir, I understand you're upset, but the seat belt sign is on. Please follow the crew's instructions and return to your seat.", True, "Thể hiện thông cảm + lý do an toàn + yêu cầu rõ ràng, bình tĩnh."),
    ("Sit down or I call police!", False, "Đe doạ ngay từ đầu làm căng thêm; lại thiếu 'will' và 'the'."),
    ("OK, stand if you want.", False, "Bỏ qua an toàn khi đèn thắt dây an toàn đang bật."),
  ]),
  ("That man keeps kicking my seat. I can't take it any more.", [
    ("I'm very sorry. I'll speak to him now. If it continues, I can find you another seat.", True, "Xin lỗi + xử lý ngay + phương án dự phòng."),
    ("He don't mean it.", False, "Sai ngữ pháp ('doesn't') và bênh người kia, bỏ qua phàn nàn."),
    ("You kick back.", False, "Xúi khách đôi co — có thể gây xô xát trên máy bay."),
  ]),
 ],
 "listen": [
  ("Please lower your voice", ["lower", "voice"], "nhắc khách nói nhỏ"),
  ("I can't serve you any more alcohol", ["serve", "alcohol"], "ngừng phục vụ rượu"),
  ("Please follow the crew's instructions", ["follow", "instructions"], "làm theo hướng dẫn"),
  ("Vaping is not allowed on board", ["Vaping", "allowed"], "cấm thuốc lá điện tử"),
  ("Captain, this is the purser. We have a disruptive passenger in row twenty-two. He has had too much alcohol and is shouting at other passengers.", ["disruptive", "twenty-two", "shouting"], "báo cơ trưởng"),
  ("Sir, this is a formal warning from the captain. Please return to your seat and follow the crew's instructions. If you continue, the police will meet the aircraft.", ["warning", "seat", "police"], "cảnh cáo chính thức"),
 ],
})

# ───────────────────────── 15. Sân đỗ & điều phối chuyến bay (ramp) ─────────────────────────
PHASES.append({
 "title": "Sân đỗ & điều phối chuyến bay",
 "vocab": [
  ("apron", "/ˈeɪprən/", "n", "sân đỗ tàu bay", "Everyone on the <b>apron</b> must wear a safety vest.", "Mọi người trên sân đỗ phải mặc áo phản quang.", "エプロン", "epuron"),
  ("stand", "/stænd/", "n", "vị trí đỗ tàu bay", "The aircraft will park at <b>stand</b> 14.", "Tàu bay sẽ đỗ ở vị trí số 14.", "スポット", "supotto"),
  ("turnaround", "/ˈtɜːnəraʊnd/", "n", "thời gian phục vụ tàu bay giữa hai chuyến (quay đầu)", "We have a 45-minute <b>turnaround</b> for this flight.", "Chuyến này chúng ta có 45 phút quay đầu."),
  ("refuelling", "/ˌriːˈfjuːəlɪŋ/", "n", "việc tra nạp nhiên liệu", "<b>Refuelling</b> will start in five minutes.", "Năm phút nữa sẽ bắt đầu tra nạp nhiên liệu.", "給油", "kyūyu"),
  ("pushback", "/ˈpʊʃbæk/", "n", "việc đẩy lùi tàu bay", "We are ready for <b>pushback</b>.", "Chúng ta đã sẵn sàng đẩy lùi tàu bay.", "プッシュバック", "pusshubakku"),
  ("load sheet", "/ˈləʊd ʃiːt/", "n", "bảng cân bằng trọng tải", "The captain needs to sign the <b>load sheet</b>.", "Cơ trưởng cần ký bảng cân bằng trọng tải.", "ロードシート", "rōdo shīto"),
  ("hold", "/həʊld/", "n", "khoang hàng (dưới thân máy bay)", "All the bags are in the <b>hold</b> now.", "Tất cả hành lý đã ở trong khoang hàng.", "貨物室", "kamotsushitsu"),
  ("chocks", "/tʃɒks/", "n", "chèn bánh (tàu bay)", "Place the <b>chocks</b> as soon as the engines are off.", "Đặt chèn bánh ngay khi động cơ đã tắt."),
  ("marshaller", "/ˈmɑːʃələ/", "n", "nhân viên dẫn đỗ tàu bay", "The <b>marshaller</b> guides the aircraft onto the stand.", "Nhân viên dẫn đỗ hướng dẫn tàu bay vào vị trí đỗ."),
  ("dispatcher", "/dɪˈspætʃə/", "n", "nhân viên điều phối chuyến bay", "Call the <b>dispatcher</b> if the fuel truck is late.", "Gọi nhân viên điều phối nếu xe nhiên liệu đến trễ."),
 ],
 "phrases": [
  ("The aircraft is on stand 14. Engines are off and chocks are on.", "Tàu bay đã vào vị trí 14. Động cơ đã tắt và đã chèn bánh."),
  ("Don't go near the aircraft until the engines are off.", "Đừng lại gần tàu bay cho đến khi động cơ tắt hẳn."),
  ("We have a 45-minute turnaround today.", "Hôm nay chúng ta có 45 phút quay đầu."),
  ("Offloading is finished. We're starting to load the bags now.", "Đã dỡ hàng xong. Chúng tôi bắt đầu chất hành lý."),
  ("Refuelling is complete.", "Đã tra nạp nhiên liệu xong."),
  ("Catering is late. Can you call them, please?", "Suất ăn đến trễ. Anh/chị gọi họ giúp được không?"),
  ("Please send me the final load sheet.", "Vui lòng gửi tôi bảng cân bằng trọng tải chốt."),
  ("The hold door is closed.", "Cửa khoang hàng đã đóng."),
  ("We're ready for pushback.", "Chúng tôi đã sẵn sàng đẩy lùi tàu bay."),
  ("Estimated departure is 10:25, five minutes late.", "Giờ khởi hành dự kiến là 10 giờ 25, trễ năm phút."),
 ],
 "dialogues": [
  ("Ramp, this is dispatch. What's the status on the bags?", [
    ("All bags are loaded except two transfer bags. They'll arrive in three minutes.", True, "Báo đúng tình trạng + số lượng còn thiếu + thời gian."),
    ("Bags OK, maybe.", False, "Mơ hồ — điều phối cần số liệu chính xác."),
    ("Loading, loading.", False, "Thiếu chủ ngữ, động từ và không có con số cụ thể."),
  ]),
  ("The fuel truck isn't here yet, and the flight leaves in 30 minutes.", [
    ("I'll call the fuel company now and ask for their arrival time. I'll update you in five minutes.", True, "Hành động ngay + hẹn cập nhật có mốc thời gian."),
    ("Fuel late, not my job.", False, "Thiếu 'is' và phủi trách nhiệm trong lúc chuyến bay đang gấp."),
    ("Don't worry, the tank is probably full.", False, "Đoán mò về nhiên liệu — cực kỳ nguy hiểm, phải có số liệu thật."),
  ]),
  ("Is the load sheet ready?", [
    ("Yes, captain. Here is the final load sheet. We have 172 passengers and 3,200 kilos in the hold.", True, "Xác nhận + đưa bảng + nêu số liệu chính."),
    ("Ready soon, captain, wait.", False, "Mơ hồ, cụt; nên nói bao giờ xong."),
    ("Load sheet is finish.", False, "Sai dạng từ: 'is finished' / 'is ready'; và nên nêu số liệu."),
  ]),
  ("There's a small dent near the hold door.", [
    ("Don't touch it. I'll report it to the engineer and the captain right away. The aircraft can't leave until it's checked.", True, "Báo ngay cho kỹ thuật và cơ trưởng — hư hỏng thân máy bay luôn phải kiểm tra."),
    ("Small, no problem.", False, "Bỏ qua hư hỏng — rất nguy hiểm cho an toàn bay."),
    ("Who did it? Not me.", False, "Đổ lỗi thay vì báo cáo ngay."),
  ]),
  ("Can you give me the doors-closed time?", [
    ("The doors closed at 10:18, and we're ready for pushback.", True, "Giờ chính xác + tình trạng tiếp theo."),
    ("Door close ten eighteen.", False, "Sai thì: 'The doors closed at 10:18.'"),
    ("Maybe around ten.", False, "Mơ hồ — giờ đóng cửa phải ghi chính xác vào báo cáo chuyến bay."),
  ]),
 ],
 "listen": [
  ("The aircraft is parked at stand fourteen", ["parked", "fourteen"], "vị trí đỗ"),
  ("Refuelling is complete", ["Refuelling", "complete"], "tra nạp xong"),
  ("Please send me the final load sheet", ["final", "load"], "bảng cân bằng trọng tải"),
  ("We are ready for pushback", ["ready", "pushback"], "sẵn sàng đẩy lùi"),
  ("Ramp, this is dispatch. The aircraft lands at nine forty on stand fourteen. We have a forty-five minute turnaround, so please have the belt loader ready.", ["fourteen", "turnaround", "belt"], "điều phối báo tàu đến"),
  ("All bags are loaded, and the hold door is closed. Refuelling is complete. We are ready for pushback.", ["loaded", "hold", "pushback"], "báo sẵn sàng khởi hành"),
 ],
})

# ───────────────────────── 16. Hàng hoá hàng không (cargo) ─────────────────────────
PHASES.append({
 "title": "Hàng hoá hàng không (cargo)",
 "vocab": [
  ("air waybill", "/ˌeə ˈweɪbɪl/", "n", "vận đơn hàng không (AWB)", "Please write the <b>air waybill</b> number on every box.", "Vui lòng ghi số vận đơn hàng không lên từng thùng.", "航空運送状", "kōkū unsōjō"),
  ("consignment", "/kənˈsaɪnmənt/", "n", "lô hàng", "This <b>consignment</b> has 12 boxes of fresh fruit.", "Lô hàng này có 12 thùng trái cây tươi."),
  ("shipper", "/ˈʃɪpə/", "n", "người gửi hàng", "The <b>shipper</b> must sign this declaration.", "Người gửi hàng phải ký tờ khai này.", "荷送人", "niokurinin"),
  ("consignee", "/ˌkɒnsaɪˈniː/", "n", "người nhận hàng", "The <b>consignee</b> will collect the goods in Osaka.", "Người nhận hàng sẽ nhận hàng ở Osaka.", "荷受人", "niukenin"),
  ("dangerous goods", "/ˌdeɪndʒərəs ˈɡʊdz/", "n", "hàng nguy hiểm", "Lithium batteries are <b>dangerous goods</b>.", "Pin lithium là hàng nguy hiểm.", "危険物", "kikenbutsu"),
  ("perishable", "/ˈperɪʃəbl/", "adj", "dễ hư hỏng (hàng tươi sống)", "<b>Perishable</b> goods go to the cold room first.", "Hàng dễ hư hỏng được đưa vào kho lạnh trước."),
  ("pallet", "/ˈpælət/", "n", "pa-lét, mâm hàng", "We can put these boxes on one <b>pallet</b>.", "Chúng ta có thể xếp các thùng này lên một pa-lét.", "パレット", "paretto"),
  ("chargeable weight", "/ˌtʃɑːdʒəbl ˈweɪt/", "n", "trọng lượng tính cước", "The <b>chargeable weight</b> is 250 kilos.", "Trọng lượng tính cước là 250 ký."),
  ("customs clearance", "/ˈkʌstəmz ˌklɪərəns/", "n", "thủ tục thông quan", "<b>Customs clearance</b> usually takes one day.", "Thủ tục thông quan thường mất một ngày.", "通関", "tsūkan"),
  ("cut-off time", "/ˈkʌt ɒf taɪm/", "n", "giờ chót nhận hàng", "The <b>cut-off time</b> for tonight's flight is 6 p.m.", "Giờ chót nhận hàng cho chuyến tối nay là 6 giờ chiều."),
 ],
 "phrases": [
  ("What is the air waybill number, please?", "Cho tôi xin số vận đơn hàng không ạ?"),
  ("The cut-off time for tonight's flight is 6 p.m.", "Giờ chót nhận hàng cho chuyến tối nay là 6 giờ chiều."),
  ("Is there anything dangerous in this consignment, like batteries or perfume?", "Trong lô hàng này có gì nguy hiểm không, như pin hay nước hoa?"),
  ("Please fill in the shipper's declaration for dangerous goods.", "Vui lòng điền tờ khai hàng nguy hiểm của người gửi."),
  ("The chargeable weight is higher because the boxes are large but light.", "Trọng lượng tính cước cao hơn vì thùng to nhưng nhẹ."),
  ("Perishable goods will go straight to the cold room.", "Hàng dễ hư hỏng sẽ được đưa thẳng vào kho lạnh."),
  ("Your consignment is booked on flight 842 tomorrow.", "Lô hàng của anh/chị đã được đặt chỗ trên chuyến 842 ngày mai."),
  ("The consignee needs to arrange customs clearance.", "Người nhận hàng cần lo thủ tục thông quan."),
  ("You can track your shipment online with the air waybill number.", "Anh/chị có thể theo dõi lô hàng trên mạng bằng số vận đơn."),
  ("I'm sorry, the flight is full. Your cargo will go on the next flight.", "Xin lỗi, chuyến bay đã kín tải. Hàng của anh/chị sẽ đi chuyến kế tiếp."),
 ],
 "dialogues": [
  ("I want to send 200 kilos of dragon fruit to Seoul tomorrow.", [
    ("Sure. Fresh fruit is perishable, so it needs cold storage. The cut-off time for tomorrow's flight is 4 p.m.", True, "Nhận yêu cầu + lưu ý hàng dễ hỏng + giờ chót nhận hàng."),
    ("OK, bring fruit anytime.", False, "Bỏ qua giờ chót — hàng đến muộn sẽ không kịp chuyến."),
    ("Fruit to Seoul, can.", False, "Dịch từng chữ, thiếu chủ ngữ: 'Yes, we can send it to Seoul.'"),
  ]),
  ("Why am I paying for 250 kilos? My boxes only weigh 180.", [
    ("Your boxes are large but light, so we also measure the volume. The chargeable weight is the higher of the two.", True, "Giải thích đúng cách tính trọng lượng tính cước (thực tế và thể tích)."),
    ("Our scale is correct. You pay.", False, "Cộc lốc, không giải thích cách tính cước."),
    ("Because price up.", False, "Thiếu chủ ngữ và động từ ('the price went up'), lại giải thích sai."),
  ]),
  ("There are some phone batteries in this box. Is that OK?", [
    ("Thank you for telling me. Batteries are dangerous goods, so we need to check them, and you must fill in a declaration.", True, "Cảm ơn khách khai báo + nêu đúng quy trình hàng nguy hiểm."),
    ("Small batteries, no one knows.", False, "Khuyến khích giấu hàng nguy hiểm — vi phạm nghiêm trọng an toàn bay."),
    ("Battery is no problem.", False, "Sai thông tin và thiếu số nhiều ('Batteries are…')."),
  ]),
  ("Has my cargo left Hanoi yet?", [
    ("Let me check with the air waybill number... Yes, it left on flight 842 at 1:10 this morning. It should arrive in Tokyo at 8:30.", True, "Tra bằng số vận đơn + chuyến + giờ đi và giờ đến dự kiến."),
    ("I think yes.", False, "Đoán mò; nên tra hệ thống bằng số vận đơn."),
    ("Cargo go already.", False, "Sai thì: 'It has already left.'"),
  ]),
  ("The consignee says two boxes are missing.", [
    ("I'm sorry. Let me check the records at both stations. I'll send you an update within two hours.", True, "Xin lỗi + kiểm tra ở cả hai đầu + hẹn thời gian phản hồi."),
    ("Maybe consignee count wrong.", False, "Đổ lỗi cho người nhận khi chưa kiểm tra; thiếu 'the' và 'counted'."),
    ("Two box lost, sorry.", False, "Kết luận vội và thiếu số nhiều 'boxes'."),
  ]),
 ],
 "listen": [
  ("What is the air waybill number", ["air", "waybill"], "hỏi số vận đơn"),
  ("The cut-off time is six o'clock tonight", ["cut-off", "tonight"], "giờ chót nhận hàng"),
  ("Lithium batteries are dangerous goods", ["Lithium", "dangerous"], "hàng nguy hiểm"),
  ("Fresh fruit goes to the cold room", ["fruit", "cold"], "hàng dễ hỏng"),
  ("Your consignment is booked on flight eight four two tomorrow morning. The chargeable weight is two hundred and fifty kilos. Please bring the boxes before four o'clock today.", ["booked", "chargeable", "boxes"], "xác nhận đặt chỗ hàng hoá"),
  ("This box has lithium batteries inside. They are dangerous goods, so the shipper must fill in a declaration.", ["lithium", "shipper", "declaration"], "khai báo hàng nguy hiểm"),
 ],
})

# ───────────────────────── 17. Thông báo trên loa (PA) ─────────────────────────
PHASES.append({
 "title": "Thông báo trên loa (PA)",
 "vocab": [
  ("PA", "/ˌpiː ˈeɪ/", "n", "thông báo qua loa (public address)", "I'll make a <b>PA</b> about the delay.", "Tôi sẽ phát thông báo qua loa về việc chậm chuyến."),
  ("flight deck", "/ˈflaɪt dek/", "n", "buồng lái", "This is your captain speaking from the <b>flight deck</b>.", "Cơ trưởng xin thông báo từ buồng lái.", "操縦室", "sōjūshitsu"),
  ("flight time", "/ˈflaɪt taɪm/", "n", "thời gian bay", "Our <b>flight time</b> today is two hours and ten minutes.", "Thời gian bay hôm nay là hai tiếng mười phút.", "飛行時間", "hikō jikan"),
  ("cruising altitude", "/ˌkruːzɪŋ ˈæltɪtjuːd/", "n", "độ cao bay bằng", "We have reached our <b>cruising altitude</b> of 11,000 metres.", "Chúng ta đã đạt độ cao bay bằng 11.000 mét.", "巡航高度", "junkō kōdo"),
  ("local time", "/ˌləʊkl ˈtaɪm/", "n", "giờ địa phương", "The <b>local time</b> in Tokyo is 7:15 in the morning.", "Giờ địa phương ở Tokyo là 7 giờ 15 sáng.", "現地時間", "genchi jikan"),
  ("descent", "/dɪˈsent/", "n", "việc giảm độ cao (chuẩn bị hạ cánh)", "We will start our <b>descent</b> in 15 minutes.", "Chúng ta sẽ bắt đầu giảm độ cao sau 15 phút nữa.", "降下", "kōka"),
  ("taxi", "/ˈtæksi/", "v", "lăn (tàu bay chạy trên đường lăn)", "We will <b>taxi</b> to the gate in about five minutes.", "Tàu bay sẽ lăn vào cửa trong khoảng năm phút."),
  ("complete stop", "/kəmˌpliːt ˈstɒp/", "n", "sự dừng hẳn", "Please stay seated until the aircraft comes to a <b>complete stop</b>.", "Quý khách vui lòng ngồi tại chỗ cho đến khi tàu bay dừng hẳn."),
  ("disembark", "/ˌdɪsɪmˈbɑːk/", "v", "rời máy bay", "Business class passengers will <b>disembark</b> first.", "Hành khách hạng thương gia sẽ rời máy bay trước.", "降機する", "kōki suru"),
  ("belongings", "/bɪˈlɒŋɪŋz/", "n", "đồ đạc, tư trang", "Please take all your <b>belongings</b> with you.", "Quý khách vui lòng mang theo toàn bộ tư trang.", "お手回り品", "otemawarihin"),
 ],
 "phrases": [
  ("Good morning, ladies and gentlemen. Welcome on board flight 312 to Tokyo.", "Xin chào quý khách. Chào mừng quý khách lên chuyến bay 312 đi Tokyo."),
  ("On behalf of the captain and the crew, we wish you a pleasant flight.", "Thay mặt cơ trưởng và tổ bay, chúc quý khách một chuyến bay dễ chịu."),
  ("Our flight time today is five hours and twenty minutes.", "Thời gian bay hôm nay là năm tiếng hai mươi phút."),
  ("We have now reached our cruising altitude.", "Chúng ta đã đạt độ cao bay bằng."),
  ("The seat belt sign is now off, but please keep your belt fastened while seated.", "Đèn báo thắt dây an toàn đã tắt, nhưng quý khách vui lòng thắt dây khi ngồi tại ghế."),
  ("We will start our descent into Tokyo in about 20 minutes.", "Khoảng 20 phút nữa chúng ta sẽ bắt đầu giảm độ cao xuống Tokyo."),
  ("The local time in Tokyo is 3:40 p.m., and the temperature is 18 degrees.", "Giờ địa phương ở Tokyo là 3 giờ 40 chiều, nhiệt độ 18 độ C."),
  ("Please stay seated until the aircraft comes to a complete stop.", "Quý khách vui lòng ngồi tại chỗ cho đến khi tàu bay dừng hẳn."),
  ("Please check the seat pocket and take all your belongings with you.", "Quý khách vui lòng kiểm tra túi lưng ghế và mang theo toàn bộ tư trang."),
  ("Thank you for flying with us. We hope to see you again soon.", "Cảm ơn quý khách đã bay cùng chúng tôi. Hẹn sớm gặp lại quý khách."),
 ],
 "dialogues": [
  ("Can you make the welcome PA in English today?", [
    ("Sure. I'll do it after the doors close. Should I include the flight time?", True, "Nhận việc + nói khi nào làm + hỏi lại nội dung cho chắc."),
    ("Yes, I will speaking now.", False, "Sai ngữ pháp ('I'll do it now') và chưa hỏi rõ lúc nào, nói gì."),
    ("My English not good, you do.", False, "Thiếu 'is' và từ chối việc được giao."),
  ]),
  ("Sorry, I didn't hear the announcement. What did the captain say?", [
    ("He said we'll start our descent in 20 minutes, and we'll land in Tokyo at about 3:40 local time.", True, "Tóm lại đúng nội dung thông báo, có giờ cụ thể."),
    ("Captain say landing soon.", False, "Sai thì ('said') và thiếu thông tin giờ hạ cánh."),
    ("Nothing important.", False, "Coi thường câu hỏi của khách."),
  ]),
  ("What's the local time in Tokyo?", [
    ("It's 3:10 in the afternoon. Tokyo is two hours ahead of Hanoi.", True, "Nói giờ + chênh lệch múi giờ giúp khách chỉnh đồng hồ."),
    ("Same Vietnam.", False, "Sai thông tin (Tokyo nhanh hơn 2 giờ) và thiếu 'as'."),
    ("Look your phone.", False, "Thiếu 'at' và đẩy việc cho khách."),
  ]),
  ("Can I get my bag now? We've landed.", [
    ("Please stay seated until the aircraft comes to a complete stop and the seat belt sign is off.", True, "Nhắc lịch sự + điều kiện rõ ràng để được đứng dậy."),
    ("OK, quick.", False, "Cho khách đứng khi tàu bay còn đang lăn — nguy hiểm."),
    ("No stand! Sit!", False, "Quát cộc lốc; nên nói lịch sự và giải thích."),
  ]),
  ("We'll be 20 minutes late because of air traffic. Please tell the passengers.", [
    ("Understood, captain. I'll make a PA now and give them the new arrival time.", True, "Xác nhận + làm ngay + nói rõ sẽ thông báo gì."),
    ("OK, maybe later.", False, "Trì hoãn thông báo — khách nối chuyến cần biết sớm."),
    ("Passengers angry, you tell.", False, "Thiếu 'will be', đẩy việc lại cho cơ trưởng."),
  ]),
 ],
 "listen": [
  ("Welcome on board flight three one two to Tokyo", ["Welcome", "Tokyo"], "chào khách lên máy bay"),
  ("We have reached our cruising altitude", ["reached", "cruising"], "đạt độ cao bay bằng"),
  ("The local time in Tokyo is three forty", ["local", "forty"], "giờ địa phương"),
  ("Please take all your belongings with you", ["take", "belongings"], "nhắc mang tư trang"),
  ("Good afternoon, this is your captain speaking from the flight deck. Our flight time today is five hours and twenty minutes. The weather in Tokyo is sunny.", ["captain", "twenty", "sunny"], "cơ trưởng chào khách"),
  ("Ladies and gentlemen, welcome to Tokyo. Please stay seated until the aircraft comes to a complete stop. Check the seat pocket and take all your belongings with you.", ["stop", "pocket", "belongings"], "thông báo sau hạ cánh"),
 ],
})

# ───────────────────────── 18. Sơ cứu & y tế trên máy bay ─────────────────────────
PHASES.append({
 "title": "Sơ cứu & y tế trên máy bay",
 "vocab": [
  ("first aid kit", "/ˌfɜːst ˈeɪd kɪt/", "n", "bộ dụng cụ sơ cứu", "Please bring the <b>first aid kit</b> to row 15.", "Vui lòng mang bộ sơ cứu đến hàng 15.", "救急箱", "kyūkyūbako"),
  ("dizzy", "/ˈdɪzi/", "adj", "chóng mặt", "I feel <b>dizzy</b> when I stand up.", "Tôi thấy chóng mặt khi đứng dậy."),
  ("faint", "/feɪnt/", "v", "ngất, xỉu", "The passenger in 15C <b>fainted</b> near the lavatory.", "Hành khách ghế 15C bị ngất gần nhà vệ sinh."),
  ("allergy", "/ˈælədʒi/", "n", "dị ứng", "Do you have a food <b>allergy</b>?", "Anh/chị có bị dị ứng thực phẩm không ạ?", "アレルギー", "arerugī"),
  ("chest pain", "/ˈtʃest peɪn/", "n", "đau ngực", "He has <b>chest pain</b>, and his left arm hurts.", "Ông ấy bị đau ngực và tay trái cũng đau.", "胸痛", "kyōtsū"),
  ("conscious", "/ˈkɒnʃəs/", "adj", "tỉnh, còn ý thức", "Is the passenger <b>conscious</b>?", "Hành khách còn tỉnh không?"),
  ("breathing", "/ˈbriːðɪŋ/", "n", "hơi thở, việc thở", "Her <b>breathing</b> is normal now.", "Bây giờ bà ấy thở bình thường rồi.", "呼吸", "kokyū"),
  ("defibrillator", "/diːˈfɪbrɪleɪtə/", "n", "máy khử rung tim (AED)", "The <b>defibrillator</b> is in the front galley.", "Máy khử rung tim để ở khu bếp phía trước."),
  ("medication", "/ˌmedɪˈkeɪʃn/", "n", "thuốc (đang dùng)", "Do you take any <b>medication</b>?", "Anh/chị có đang dùng thuốc gì không ạ?"),
  ("diversion", "/daɪˈvɜːʃn/", "n", "việc chuyển hướng hạ cánh xuống sân bay khác", "The captain may decide on a <b>diversion</b> to Bangkok.", "Cơ trưởng có thể quyết định chuyển hướng hạ cánh xuống Bangkok.", "ダイバート", "daibāto"),
 ],
 "phrases": [
  ("If there is a doctor or a nurse on board, please press your call button.", "Nếu trên máy bay có bác sĩ hoặc y tá, xin vui lòng bấm nút gọi tiếp viên."),
  ("Can you hear me? How are you feeling?", "Anh/chị có nghe tôi nói không? Anh/chị thấy trong người thế nào?"),
  ("Please lie down here. I'll raise your legs a little.", "Anh/chị nằm xuống đây nhé. Tôi sẽ kê chân anh/chị cao lên một chút."),
  ("Do you have any allergies, or do you take any medication?", "Anh/chị có bị dị ứng gì không, có đang dùng thuốc gì không?"),
  ("Do you have your own medicine with you?", "Anh/chị có mang theo thuốc của mình không?"),
  ("I'm giving you some oxygen. Breathe slowly.", "Tôi cho anh/chị thở oxy. Anh/chị thở chậm thôi."),
  ("For a nosebleed, lean forward and pinch the soft part of your nose.", "Khi chảy máu cam, hãy cúi người về trước và bóp phần mềm của mũi."),
  ("I'm getting the defibrillator. Please give us some space.", "Tôi đi lấy máy khử rung tim. Mọi người vui lòng tránh ra một chút."),
  ("I'll inform the captain, and a medical team will meet us on arrival.", "Tôi sẽ báo cơ trưởng, và đội y tế sẽ đón chúng ta khi hạ cánh."),
  ("A doctor is with him now. Please stay in your seats.", "Bác sĩ đang ở cạnh ông ấy. Quý khách vui lòng ngồi tại chỗ."),
 ],
 "dialogues": [
  ("My husband feels dizzy, and his face is very pale.", [
    ("Let's help him lie down across these seats. I'll bring some oxygen. Does he have any medical problems?", True, "Cho khách nằm + hỗ trợ oxy + hỏi tiền sử bệnh."),
    ("Dizzy, drink water, OK.", False, "Cụt lủn, thiếu câu và chưa đánh giá tình trạng khách."),
    ("Maybe he is tired. Just sleep.", False, "Coi nhẹ triệu chứng — có thể là dấu hiệu nguy hiểm."),
  ]),
  ("I have a nut allergy. Are there any nuts in this meal?", [
    ("I'm not sure, so please don't eat it yet. Let me check the meal information for you.", True, "Không đoán — dặn khách chưa ăn + kiểm tra thông tin suất ăn."),
    ("No nuts, I think. Eat.", False, "Đoán mò — rất nguy hiểm với người bị dị ứng."),
    ("Nut is small, no problem.", False, "Coi nhẹ dị ứng và sai số nhiều ('Nuts are…')."),
  ]),
  ("The passenger in 15C fainted! What should I do?", [
    ("Check if he's conscious and breathing. I'll bring the first aid kit and tell the purser.", True, "Kiểm tra ý thức và hơi thở + mang bộ sơ cứu + báo tiếp viên trưởng."),
    ("Wait, maybe he wake up.", False, "Chờ đợi là nguy hiểm; lại sai ngữ pháp ('he'll wake up')."),
    ("Don't touch, not our job.", False, "Bỏ mặc khách — tổ bay phải sơ cứu ban đầu."),
  ]),
  ("Can you give me something for my headache?", [
    ("Let me check what we have in the first aid kit. Do you have any allergies, or do you take any medication?", True, "Hỏi dị ứng và thuốc đang dùng trước khi đưa thuốc."),
    ("Take this. It's my own medicine.", False, "Không được đưa thuốc cá nhân cho khách — có thể gây phản ứng."),
    ("Headache normal on plane.", False, "Thiếu 'is' và coi nhẹ khó chịu của khách."),
  ]),
  ("How is the passenger with chest pain?", [
    ("He's conscious and breathing, and a doctor on board is with him. He's on oxygen now. The doctor wants a medical team on arrival.", True, "Báo đủ tình trạng + ai đang giúp + đề nghị — để cơ trưởng quyết định."),
    ("He OK, maybe.", False, "Thiếu 'is', mơ hồ — cơ trưởng cần thông tin rõ để quyết định chuyển hướng."),
    ("Very bad! Land now!", False, "Hoảng loạn và ra lệnh cho cơ trưởng, không báo tình trạng cụ thể."),
  ]),
 ],
 "listen": [
  ("Is there a doctor on board", ["doctor", "board"], "tìm bác sĩ"),
  ("Do you have any allergies", ["allergies"], "hỏi dị ứng"),
  ("Please bring the first aid kit to row fifteen", ["aid", "fifteen"], "mang bộ sơ cứu"),
  ("He is conscious and breathing normally", ["conscious", "breathing"], "báo tình trạng khách"),
  ("Ladies and gentlemen, if there is a doctor or a nurse on board, please press your call button. Thank you.", ["doctor", "nurse", "call"], "thông báo tìm nhân viên y tế"),
  ("Captain, the passenger in fifteen C is conscious now. A doctor is with him, and he is on oxygen. We need a medical team on arrival.", ["conscious", "oxygen", "medical"], "báo cơ trưởng"),
 ],
})

EXTRA = {
 "phases": PHASES,
 "rev": [
  ("Vé này không được hoàn tiền.", "This ticket is non-refundable."),
  ("Anh/chị cần trả thêm tiền chênh lệch giá vé.", "You need to pay the fare difference."),
  ("Tiền sẽ được hoàn về thẻ của anh/chị.", "The money will go back to your card."),
  ("Vé của anh/chị bao gồm quyền vào phòng chờ.", "Your ticket includes lounge access."),
  ("Đồ ăn và đồ uống ở đây đều miễn phí.", "The food and drinks here are complimentary."),
  ("Anh/chị muốn trả bằng thẻ hay tiền mặt?", "Would you like to pay by card or in cash?"),
  ("Xin lỗi, chúng tôi không nhận tiền xu.", "I'm sorry, we don't accept coins."),
  ("Xin lỗi, tôi không thể phục vụ thêm rượu cho anh.", "I'm sorry, I can't serve you any more alcohol."),
  ("Anh vui lòng làm theo hướng dẫn của tổ bay.", "Please follow the crew's instructions."),
  ("Chúng ta đã sẵn sàng đẩy lùi tàu bay.", "We are ready for pushback."),
  ("Hành lý đã chất xong hết.", "All the bags are loaded."),
  ("Giờ chót nhận hàng là sáu giờ tối.", "The cut-off time is 6 p.m."),
  ("Trong lô hàng này có pin không ạ?", "Are there any batteries in this consignment?"),
  ("Giờ địa phương ở Tokyo là ba giờ chiều.", "The local time in Tokyo is 3 p.m."),
  ("Quý khách vui lòng mang theo toàn bộ tư trang.", "Please take all your belongings with you."),
  ("Trên máy bay có bác sĩ không ạ?", "Is there a doctor on board?"),
 ],
 "reading": [
  {"t": "Refund email", "text": "Subject: Your refund request R-2291\nDear Mr. Kim,\nWe have received your refund request for flight 512, Hanoi–Busan, on 3 June. Your ticket is non-refundable, but we will refund the airport taxes of 1,150,000 VND. The money will go back to your card in 7–14 working days.\nCustomer Service Team", "q": [
    {"q": "What will Mr. Kim get back?", "o": ["The full ticket price", "The airport taxes", "A travel voucher"], "a": 1},
    {"q": "How will he receive the money?", "o": ["In cash at the airport", "To his card", "From his travel agent"], "a": 1}]},
  {"t": "Lounge notice", "text": "WELCOME TO THE LOUNGE\nOpen 04:30–00:30\n• Business class passengers and gold members: free entry\n• Gold members may bring one guest\n• Shower rooms: please book at the front desk\n• This is a quiet lounge. There are no boarding announcements. Please check the screens.", "q": [
    {"q": "Who can bring a guest?", "o": ["All passengers", "Gold members", "Economy passengers"], "a": 1},
    {"q": "How do passengers know when to go to the gate?", "o": ["They hear an announcement", "They check the screens", "Staff call their phones"], "a": 1}]},
  {"t": "Duty-free price list", "text": "ON-BOARD DUTY-FREE – PRICE LIST\nPerfume 50 ml ........ USD 65\nChocolate gift box ... USD 18\nWhisky 1 litre ....... USD 42 (in a sealed bag)\nWe accept cards, USD, EUR and VND (notes only).\nPre-order online up to 24 hours before your flight.", "q": [
    {"q": "How much is the whisky?", "o": ["USD 18", "USD 42", "USD 65"], "a": 1},
    {"q": "Which of these can passengers NOT pay with?", "o": ["Cards", "Euros", "Coins"], "a": 2}]},
  {"t": "Turnaround chat", "text": "Lan (Dispatch): Flight 215, stand 14, ETD 10:25.\n• Refuelling done at 09:58.\n• Bags: 142 loaded, 2 transfer bags coming from Gate 3.\n• Catering is late – ETA 10:05.\n• Final load sheet after catering.\nRamp, please confirm hold door closed by 10:15.", "q": [
    {"q": "What is late?", "o": ["Refuelling", "Catering", "The transfer bags from Gate 14"], "a": 1},
    {"q": "When must the hold door be closed?", "o": ["By 10:05", "By 10:15", "By 10:25"], "a": 1}]},
  {"t": "Cargo booking", "text": "CARGO BOOKING CONFIRMATION\nAWB: 738-4512 6630\nShipper: Green Farm Co., Bắc Giang\nConsignee: Fresh Market Ltd., Osaka\nGoods: fresh lychees, 40 boxes (perishable)\nActual weight: 620 kg · Chargeable weight: 700 kg\nFlight: 842, 18 June, departs 01:10\nCut-off: 17 June, 18:00, Cargo Terminal 2", "q": [
    {"q": "Who will receive the goods?", "o": ["Green Farm Co.", "Fresh Market Ltd.", "Cargo Terminal 2"], "a": 1},
    {"q": "When must the goods arrive at the terminal?", "o": ["18 June, 01:10", "17 June, 18:00", "18 June, 18:00"], "a": 1}]},
 ],
 "ai": [
  ("change", "Đổi vé & hoàn vé", "You are a passenger at the airline ticket desk. You want to move your flight to another day, or get a refund if the change is too expensive. Ask about the change fee, the fare difference and how long a refund takes."),
  ("lounge", "Phòng chờ thương gia", "You are a frequent flyer at the lounge entrance. You want to bring your friend, who has an economy ticket. Ask about the guest rules, the shower rooms and when you should leave for the gate."),
  ("dutyfree", "Bán hàng miễn thuế", "You are a passenger on the plane. I am the flight attendant with the duty-free trolley. Ask about a perfume and a bottle of whisky, ask which currencies we accept, and ask what to do because you have a connecting flight."),
  ("medical", "Khách bị ốm trên máy bay", "You are a passenger whose travel partner suddenly feels dizzy and has chest pain during the flight. I am the flight attendant. Tell me what is happening and answer my questions about allergies and medication."),
 ],
 "events": [
  ("newroute", "Khai trương đường bay mới", "You are the station manager at a new destination. Our airline starts a new route there next week. Ask me about the first flight, the check-in plan, the turnaround and the welcome event for passengers."),
  ("fruitseason", "Mùa xuất khẩu trái cây bằng máy bay", "You are a fruit exporter who wants to send many tonnes of fresh lychees by air next month. Ask me about bookings, cut-off times, cold storage and the documents you need."),
  ("vipflight", "Chuyến bay có đoàn khách VIP", "You are the protocol officer for a government delegation flying with us next week. Ask me about the lounge, priority boarding, seating and security arrangements."),
 ],
 "quips": [
  "Duty-free, anyone?",
  "Chocks on, engines off!",
  "Pushback in three, two, one!",
  "Mochi signed the load sheet!",
  "Lounge snacks are complimentary!",
  "Local time: snack o'clock!",
 ],
 "roles": {
  "checkin": {
   "scenarios": [
    ("ci_refund", "Hoàn vé vì ốm", "You are a passenger at the ticket desk. You are ill and can't travel next week. Ask if you can get a refund or change the date, and ask how long a refund takes."),
    ("ci_agent", "Vé mua qua đại lý", "You bought your ticket through a travel agent, and now you want to change the return date at the airport counter. Ask me what you can do, and be a little impatient."),
   ],
   "dialogues": [
    ("Can I change my return date here at the airport?", [
      ("Yes, you can. Let me check the fare rules. There's a change fee, and you may need to pay the fare difference.", True, "Trả lời + kiểm tra điều kiện vé + báo trước các khoản phí."),
      ("Change here no, online.", False, "Thiếu chủ ngữ và động từ; lại sai — đổi được tại quầy."),
      ("Sure, free of charge.", False, "Hứa miễn phí khi chưa kiểm tra điều kiện vé.")]),
    ("Why is the fare so different from yesterday?", [
      ("Fares change with demand, and the cheaper seats have sold out. Let me show you the cheapest option now.", True, "Giải thích ngắn vì sao giá đổi + đưa lựa chọn rẻ nhất."),
      ("Price go up, sorry.", False, "Sai thì ('The price went up') và không giúp khách."),
      ("Yesterday is yesterday.", False, "Nghe như cãi, không giải thích gì.")]),
    ("Can I add my baby to my booking now?", [
      ("Of course. May I see the baby's passport, please? I'll add the infant to your booking. The infant fare is shown on this screen.", True, "Xin giấy tờ của bé + thêm vào đặt chỗ + chỉ giá vé em bé."),
      ("Baby free, no need.", False, "Sai — em bé vẫn phải có tên trong đặt chỗ và có vé em bé."),
      ("You add online yourself.", False, "Đẩy việc cho khách khi khách đang đứng ở quầy.")]),
    ("I've paid for my new ticket. When will I get it?", [
      ("It's issued now. I've sent the e-ticket to your email, and here is a printed copy of your itinerary.", True, "Xác nhận đã xuất vé + gửi email + đưa bản in."),
      ("Ticket later, wait.", False, "Cụt lủn, không nói bao giờ."),
      ("You get ticket tomorrow maybe.", False, "Mơ hồ, thiếu 'will' và 'the'; vé điện tử xuất ngay được.")]),
   ]},
  "gate": {
   "scenarios": [
    ("gt_missing", "Gọi khách chưa ra cửa", "You are a passenger who is shopping far from the gate. I call your phone because the gate is closing soon. Ask how much time you have and how to get to the gate quickly."),
    ("gt_upgrade", "Nâng hạng tại cửa", "You are a passenger at the gate who wants to upgrade to business class for this flight. Ask about the price, the seat and the meal."),
   ],
   "dialogues": [
    ("Hello? Why is the airline calling me?", [
      ("Hello, this is the gate for flight 215 to Singapore. The gate closes in ten minutes. Where are you now?", True, "Giới thiệu mình là ai + lý do gọi + hỏi vị trí khách."),
      ("You late! Come now!", False, "Quát khách, thiếu 'are'; nên giới thiệu và nói rõ thời gian."),
      ("Is it you, passenger?", False, "Câu kỳ quặc; nên hỏi 'Is this Mr. Lee?' và giới thiệu mình.")]),
    ("I'm at the duty-free shop. Can you wait for me?", [
      ("Please come straight to Gate 7 now. It's about five minutes' walk, and we close the gate at 10:40.", True, "Yêu cầu rõ + thời gian đi bộ + giờ đóng cửa."),
      ("Yes, we wait, no problem.", False, "Hứa giữ chuyến bay — không thể, và thiếu 'will'."),
      ("Shop more later.", False, "Vô nghĩa, không nói khách phải làm gì.")]),
    ("Two passengers are still missing. What's the plan?", [
      ("I'll make a final call now. If they aren't here by 10:40, we'll close the gate and ask the ramp to offload their bags.", True, "Gọi lần cuối + mốc giờ + dỡ hành lý khách vắng mặt đúng quy trình."),
      ("We wait until they come.", False, "Sai quy trình, làm chậm cả chuyến bay."),
      ("Close the door. Bags stay.", False, "Nguy hiểm — hành lý của khách không lên máy bay phải được dỡ xuống.")]),
    ("Can I upgrade here at the gate?", [
      ("Let me check. Yes, there's one business class seat left. The price is shown here, and you can pay by card.", True, "Kiểm tra + còn ghế + giá + cách thanh toán."),
      ("Upgrade? Too late.", False, "Trả lời khi chưa kiểm tra còn ghế hay không."),
      ("Can, give me money.", False, "Thiếu chủ ngữ và thô: 'Yes, you can. There's an extra charge.'")]),
   ]},
  "cabin": {
   "scenarios": [
    ("cb_vape", "Khách hút thuốc điện tử", "You are a passenger who was vaping in the lavatory, and I found you. Say you didn't know it was a problem, and ask what will happen now."),
    ("cb_dutyfree", "Mua hàng miễn thuế", "You are a passenger who wants to buy two perfumes from the duty-free trolley. The card machine is slow, and you want to pay partly in cash. Ask me questions."),
   ],
   "dialogues": [
    ("Is it OK to use my e-cigarette in the toilet?", [
      ("I'm sorry, smoking and vaping aren't allowed anywhere on board, including the lavatory. It's a safety rule.", True, "Từ chối rõ + phạm vi (cả nhà vệ sinh) + lý do an toàn."),
      ("OK, quick. Don't tell anyone.", False, "Vi phạm an toàn bay nghiêm trọng."),
      ("No smoke! Crazy!", False, "Thô, xúc phạm khách; nên giải thích lịch sự.")]),
    ("Can I pay half in cash and half by card?", [
      ("Yes, you can. Let's do the cash first, and then I'll put the rest on your card.", True, "Đồng ý + nói rõ thứ tự thanh toán."),
      ("Half half, no.", False, "Cụt lủn, lại từ chối khi thực tế làm được."),
      ("Only one way pay.", False, "Dịch từng chữ, sai trật tự từ và sai thông tin.")]),
    ("I think I dropped my ring somewhere near my seat.", [
      ("I'm sorry to hear that. Let me bring a torch and help you look around your seat.", True, "Cảm thông + hành động cụ thể giúp tìm."),
      ("Ring small, can't find.", False, "Bi quan, thiếu chủ ngữ và động từ."),
      ("You look yourself.", False, "Đẩy việc cho khách; thiếu 'for it'.")]),
    ("The woman behind me feels sick. I think she needs help.", [
      ("Thank you for telling me. I'll go to her right away.", True, "Cảm ơn + đến ngay."),
      ("She sick, wait a minute.", False, "Thiếu 'is' và chậm trễ khi khách cần giúp."),
      ("Not your business, sir.", False, "Thô và bỏ qua thông tin quan trọng.")]),
   ]},
  "baggage": {
   "scenarios": [
    ("bg_sports", "Dụng cụ thể thao bị hỏng", "You are a passenger whose golf bag arrived with a broken club. You are upset because you have a competition tomorrow. Ask what the airline will do."),
    ("bg_delivery", "Hẹn lại giờ giao hành lý", "Your delayed bag will be delivered to your hotel today, but you will be out all afternoon. Call me to change the delivery time and address."),
   ],
   "dialogues": [
    ("My bag is being delivered today, but I won't be at the hotel.", [
      ("No problem. We can leave it at the hotel reception, or deliver it this evening. Which would you prefer?", True, "Trấn an + hai lựa chọn + hỏi ý khách."),
      ("Driver come, you must wait.", False, "Sai ngữ pháp ('The driver will come') và ép khách."),
      ("Then no delivery.", False, "Cứng nhắc, không đưa phương án.")]),
    ("Can I give you a different address for the delivery?", [
      ("Of course. Could you spell the new address for me, please? I'll update your file now.", True, "Đồng ý + xin đánh vần địa chỉ + cập nhật hồ sơ."),
      ("Address change not possible.", False, "Cứng nhắc khi chưa kiểm tra, thiếu động từ 'is'."),
      ("Yes, you tell driver.", False, "Thiếu 'the' và đẩy việc cho khách.")]),
    ("One of my golf clubs is broken, and I have a competition tomorrow!", [
      ("I'm very sorry. Let me take photos and write a damage report now. If you need to rent clubs, please keep the receipt.", True, "Xin lỗi + lập biên bản có ảnh + hướng dẫn giữ hoá đơn, không hứa bừa."),
      ("Golf bag is your risk.", False, "Lạnh lùng, không lập biên bản cho khách."),
      ("We buy you new clubs today.", False, "Hứa bừa thay công ty, thiếu 'will'.")]),
    ("It's the third day, and my bag still isn't here. Is it lost?", [
      ("I understand how frustrating this is. We haven't found it yet, but we're still searching every airport on your route. I'll call you with an update by 5 p.m.", True, "Thông cảm + tình hình thật + hẹn giờ cập nhật."),
      ("Yes, lost forever.", False, "Kết luận vội, làm khách hoảng."),
      ("Maybe it come tomorrow.", False, "Sai ngữ pháp ('it will come') và mơ hồ.")]),
   ]},
 },
}
