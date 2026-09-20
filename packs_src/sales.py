# -*- coding: utf-8 -*-
# Gói "sales" — Bán hàng · CSKH: nhân viên bán hàng tại cửa hàng, CSKH / call center / BPO, telesales, sale B2B.
# Người học làm việc với khách nói tiếng Anh ở Việt Nam. Tên sản phẩm / thương hiệu đều là tên tự đặt (Zenta, Lumo…).
# Chặng lõi lấy từ office: 3 (Email công việc), 11 (Phỏng vấn & phát triển sự nghiệp).
# Schema: xem packs_src/README.md. Build: python3 packs_src/build.py sales

PHASES = []

# ───────────────────────── 0. Chào khách & giới thiệu sản phẩm ─────────────────────────
PHASES.append({
 "title": "Chào khách & giới thiệu sản phẩm",
 "vocab": [
  ("customer", "/ˈkʌstəmə/", "n", "khách hàng", "Every <b>customer</b> gets a free gift today.", "Hôm nay mỗi khách hàng đều được tặng quà.", "顧客", "kokyaku"),
  ("product", "/ˈprɒdʌkt/", "n", "sản phẩm", "This <b>product</b> is made in Việt Nam.", "Sản phẩm này được sản xuất tại Việt Nam.", "製品", "seihin"),
  ("browse", "/braʊz/", "v", "xem lướt, ngắm hàng", "Feel free to <b>browse</b>. I'm here if you need me.", "Anh/chị cứ tự nhiên xem hàng, cần gì cứ gọi em."),
  ("collection", "/kəˈlekʃn/", "n", "bộ sưu tập, dòng hàng mới", "Our new summer <b>collection</b> has just arrived.", "Bộ sưu tập hè mới của bên em vừa về."),
  ("model", "/ˈmɒdl/", "n", "mẫu, đời (sản phẩm)", "This is the latest <b>model</b>.", "Đây là mẫu mới nhất ạ."),
  ("feature", "/ˈfiːtʃə/", "n", "tính năng, đặc điểm", "The best <b>feature</b> is the quiet motor.", "Tính năng hay nhất là động cơ chạy rất êm."),
  ("brochure", "/ˈbrəʊʃə/", "n", "tờ giới thiệu sản phẩm", "Here's a <b>brochure</b> with all our prices.", "Đây là tờ giới thiệu có đầy đủ bảng giá ạ.", "パンフレット", "panfuretto"),
  ("best-seller", "/ˌbestˈselə/", "n", "sản phẩm bán chạy nhất", "This rice cooker is our <b>best-seller</b>.", "Nồi cơm điện này là sản phẩm bán chạy nhất bên em."),
  ("demonstrate", "/ˈdemənstreɪt/", "v", "làm mẫu, trình diễn cách dùng", "Let me <b>demonstrate</b> how the vacuum cleaner works.", "Để em làm thử cho anh/chị xem máy hút bụi hoạt động thế nào."),
  ("in stock", "/ɪn ˈstɒk/", "phr", "còn hàng", "Size M is still <b>in stock</b>.", "Size M vẫn còn hàng ạ.", "在庫あり", "zaiko ari"),
 ],
 "phrases": [
  ("Good morning! Welcome to our store.", "Chào buổi sáng! Chào mừng anh/chị đến cửa hàng."),
  ("Are you looking for anything in particular?", "Anh/chị đang tìm món gì cụ thể không ạ?"),
  ("Feel free to look around.", "Anh/chị cứ tự nhiên xem hàng nhé."),
  ("Let me know if you need any help.", "Cần gì anh/chị cứ gọi em nhé."),
  ("This is our best-selling model this month.", "Đây là mẫu bán chạy nhất tháng này ạ."),
  ("It comes in three colours: black, white and blue.", "Sản phẩm có ba màu: đen, trắng và xanh dương."),
  ("Would you like me to show you how it works?", "Anh/chị có muốn em hướng dẫn cách dùng không ạ?"),
  ("The main feature is its long battery life.", "Điểm nổi bật nhất là pin dùng rất lâu."),
  ("We have it in stock in all sizes.", "Mẫu này còn hàng đủ các size ạ."),
  ("Here's a brochure with all the details.", "Đây là tờ giới thiệu có đầy đủ thông tin ạ."),
 ],
 "dialogues": [
  ("Hi, I'm just looking, thanks.", [
    ("No problem. Take your time, and let me know if you need anything.", True, "Tôn trọng khách + sẵn sàng giúp, không ép."),
    ("OK. But this one very good, you buy it.", False, "Thiếu 'is' và quá ép khách khi họ chỉ muốn xem."),
    ("You look what?", False, "Sai trật tự câu hỏi và cộc: 'What are you looking for?'"),
  ]),
  ("What's the difference between these two models?", [
    ("The S5 is lighter and has a bigger battery. The S3 is cheaper, but it's still very good.", True, "So sánh rõ từng mẫu, dùng so sánh hơn đúng."),
    ("The S5 more light and more big battery.", False, "Thiếu động từ 'is/has'; so sánh hơn phải là 'lighter', 'bigger'."),
    ("Both same same.", False, "'Same same' không chuyên nghiệp và không giúp khách chọn."),
  ]),
  ("Do you have this in blue?", [
    ("Yes, we do. Let me get one from the stockroom for you.", True, "Trả lời đủ 'Yes, we do' + hành động cụ thể."),
    ("Yes, have.", False, "Thiếu chủ ngữ: 'Yes, we do.' / 'Yes, we have it.'"),
    ("Blue is not beautiful, you take black.", False, "Chê lựa chọn của khách và áp đặt — thiếu lịch sự."),
  ]),
  ("Can you show me how this blender works?", [
    ("Of course. Just put the fruit in, close the lid and press this button.", True, "Đồng ý + hướng dẫn từng bước bằng câu ngắn, rõ."),
    ("Of course. You must read the brochure.", False, "Đẩy việc cho khách, không làm mẫu sản phẩm."),
    ("It working very easy.", False, "Sai ngữ pháp: 'It's very easy to use.'"),
  ]),
  ("Is this the newest model?", [
    ("Yes, it came out last month. It's also our best-seller right now.", True, "Xác nhận + thêm thông tin hấp dẫn."),
    ("Yes, it is come out last month.", False, "Sai thì: 'It came out last month' (không dùng 'is' với quá khứ)."),
    ("I think so, I don't know.", False, "Mâu thuẫn, thiếu hiểu biết sản phẩm — nên nói 'Let me check for you.'"),
  ]),
 ],
 "listen": [
  ("Welcome to our store, how can I help you", ["Welcome", "help"], "chào khách vào cửa hàng"),
  ("This model comes in three different colours", ["model", "colours"], "màu sắc sản phẩm"),
  ("The main feature is the long battery life", ["feature", "battery"], "tính năng chính"),
  ("We still have the large size in stock", ["large", "stock"], "còn hàng"),
  ("Good afternoon and welcome. This is our new collection for summer. Everything on this table is ten percent off.", ["collection", "summer", "table"], "giới thiệu hàng mới"),
  ("This air purifier is our best-seller. It's very quiet, so you can use it at night. Would you like to see a demo?", ["best-seller", "quiet", "demo"], "giới thiệu sản phẩm bán chạy"),
 ],
})

# ───────────────────────── 1. Tìm hiểu nhu cầu khách ─────────────────────────
PHASES.append({
 "title": "Tìm hiểu nhu cầu khách",
 "vocab": [
  ("need", "/niːd/", "n", "nhu cầu", "What are your main <b>needs</b> for a new laptop?", "Nhu cầu chính của anh/chị với chiếc laptop mới là gì ạ?", "ニーズ", "nīzu"),
  ("requirement", "/rɪˈkwaɪəmənt/", "n", "yêu cầu (bắt buộc)", "The client's main <b>requirement</b> is fast delivery.", "Yêu cầu chính của khách là giao hàng nhanh.", "要件", "yōken"),
  ("preference", "/ˈprefrəns/", "n", "sở thích, lựa chọn ưu tiên", "Do you have a colour <b>preference</b>?", "Anh/chị thích màu nào hơn không ạ?"),
  ("purpose", "/ˈpɜːpəs/", "n", "mục đích", "The <b>purpose</b> of this call is to understand your needs.", "Mục đích cuộc gọi này là để hiểu nhu cầu của anh/chị.", "目的", "mokuteki"),
  ("recommend", "/ˌrekəˈmend/", "v", "gợi ý, khuyên dùng", "I'd <b>recommend</b> the smaller size for your kitchen.", "Em gợi ý anh/chị chọn cỡ nhỏ hơn cho bếp nhà mình."),
  ("suitable", "/ˈsuːtəbl/", "adj", "phù hợp", "This model is <b>suitable</b> for a small office.", "Mẫu này phù hợp với văn phòng nhỏ."),
  ("price range", "/ˈpraɪs ˌreɪndʒ/", "n", "khoảng giá", "What's your <b>price range</b>?", "Anh/chị định mua trong khoảng giá bao nhiêu ạ?"),
  ("usage", "/ˈjuːsɪdʒ/", "n", "mức/cách sử dụng", "With your <b>usage</b>, the basic data plan is enough.", "Với mức sử dụng của anh/chị, gói data cơ bản là đủ."),
  ("open-ended question", "/ˌəʊpən ˈendɪd ˈkwestʃən/", "n", "câu hỏi mở", "Start with an <b>open-ended question</b> like 'What do you need it for?'", "Hãy bắt đầu bằng một câu hỏi mở như 'Anh/chị cần dùng vào việc gì?'"),
  ("narrow down", "/ˌnærəʊ ˈdaʊn/", "phr v", "thu hẹp (lựa chọn)", "Let's <b>narrow down</b> the options to two models.", "Mình thu hẹp lại còn hai mẫu nhé."),
 ],
 "phrases": [
  ("What will you mainly use it for?", "Anh/chị chủ yếu dùng nó vào việc gì ạ?"),
  ("Who is it for?", "Anh/chị mua cho ai dùng ạ?"),
  ("Do you have a price range in mind?", "Anh/chị đã tính trước khoảng giá chưa ạ?"),
  ("What's most important to you: price, size or quality?", "Với anh/chị điều gì quan trọng nhất: giá, kích thước hay chất lượng?"),
  ("How often will you use it?", "Anh/chị sẽ dùng nó thường xuyên không ạ?"),
  ("What are you using at the moment?", "Hiện tại anh/chị đang dùng loại nào ạ?"),
  ("So, if I understand correctly, you need something light for travel.", "Vậy nếu em hiểu đúng thì anh/chị cần một món nhẹ để mang đi xa."),
  ("Based on what you've told me, I'd recommend this one.", "Dựa trên những gì anh/chị chia sẻ, em gợi ý mẫu này."),
  ("Is there anything you didn't like about your old one?", "Có điểm nào anh/chị không thích ở cái cũ không ạ?"),
  ("When do you need it by?", "Anh/chị cần có hàng trước ngày nào ạ?"),
 ],
 "dialogues": [
  ("I need a new laptop, but I don't know much about them.", [
    ("No problem, I can help. What will you mainly use it for?", True, "Trấn an + hỏi câu hỏi mở về mục đích sử dụng."),
    ("You should buy the most expensive one.", False, "Chưa hỏi nhu cầu đã đẩy đồ đắt — khách dễ mất lòng tin."),
    ("You use for what?", False, "Sai trật tự câu hỏi: 'What will you use it for?'"),
  ]),
  ("It's a gift for my mother.", [
    ("That's lovely. Does she prefer something simple and easy to use?", True, "Phản hồi thân thiện + hỏi tiếp về sở thích người dùng."),
    ("Your mother how old?", False, "Thiếu động từ và hỏi tuổi đột ngột — nên hỏi 'Does she use a smartphone much?'"),
    ("OK. Gift is this.", False, "Dịch từng chữ, cộc lốc, không hỏi thêm nhu cầu."),
  ]),
  ("I don't want to spend more than ten million.", [
    ("Understood. We have some great options under ten million. Let me show you.", True, "Ghi nhận ngân sách + đưa lựa chọn phù hợp."),
    ("Ten million is too little. You add more money.", False, "Chê ngân sách của khách, nghe thiếu tôn trọng."),
    ("Understand. I am show you.", False, "Sai: 'Understood.' / 'Let me show you.'"),
  ]),
  ("I travel a lot for work.", [
    ("So you need something light with a long battery life, right?", True, "Tóm tắt lại nhu cầu để xác nhận — kỹ năng tư vấn tốt."),
    ("Travel is very fun!", False, "Chỉ nói chuyện phiếm, bỏ lỡ thông tin nhu cầu quan trọng."),
    ("So you need light, battery long.", False, "Thiếu mạo từ, trật tự kiểu tiếng Việt: 'something light with a long battery life'."),
  ]),
  ("Which one would you recommend?", [
    ("Based on your needs, I'd recommend the Lumo S3. It's light and within your price range.", True, "Gợi ý có lý do, gắn với nhu cầu khách."),
    ("I recommend you to buy S3.", False, "Sai cấu trúc: 'I'd recommend the S3' hoặc 'I'd recommend buying the S3.'"),
    ("All is good, you choose.", False, "Không tư vấn, đẩy quyết định lại cho khách."),
  ]),
 ],
 "listen": [
  ("What will you mainly use it for", ["mainly", "use"], "hỏi mục đích sử dụng"),
  ("Do you have a price range in mind", ["price", "range"], "hỏi khoảng giá"),
  ("She needs something light for travelling", ["light", "travelling"], "nhu cầu của khách"),
  ("I'd recommend the smaller one for your kitchen", ["recommend", "kitchen"], "gợi ý sản phẩm"),
  ("So, let me check I understand. You need a printer for a small office. You print about fifty pages a day.", ["printer", "office", "fifty"], "tóm tắt lại nhu cầu khách"),
  ("Our client wants fifty chairs for a new office. Delivery must be before the end of May. Their main requirement is quality.", ["chairs", "May", "quality"], "yêu cầu của khách doanh nghiệp"),
 ],
})

# ───────────────────────── 2. Báo giá, ưu đãi & so sánh ─────────────────────────
PHASES.append({
 "title": "Báo giá, ưu đãi & so sánh",
 "vocab": [
  ("quotation", "/kwəʊˈteɪʃn/", "n", "bảng báo giá", "I'll email you a <b>quotation</b> today.", "Hôm nay em sẽ email báo giá cho anh/chị.", "見積もり", "mitsumori"),
  ("discount", "/ˈdɪskaʊnt/", "n", "khoản giảm giá", "We offer a 5% <b>discount</b> for orders over 100 units.", "Bên em giảm 5% cho đơn trên 100 cái.", "値引き", "nebiki"),
  ("special offer", "/ˌspeʃl ˈɒfə/", "n", "ưu đãi đặc biệt", "This <b>special offer</b> ends on Sunday.", "Ưu đãi đặc biệt này kết thúc vào Chủ nhật."),
  ("voucher", "/ˈvaʊtʃə/", "n", "phiếu mua hàng, voucher", "You can use this <b>voucher</b> next time.", "Lần sau anh/chị có thể dùng voucher này."),
  ("compare", "/kəmˈpeə/", "v", "so sánh", "Let me <b>compare</b> the two plans for you.", "Để em so sánh hai gói cho anh/chị.", "比較する", "hikaku suru"),
  ("value for money", "/ˌvæljuː fə ˈmʌni/", "phr", "đáng đồng tiền", "This model is great <b>value for money</b>.", "Mẫu này rất đáng đồng tiền."),
  ("warranty", "/ˈwɒrənti/", "n", "bảo hành", "It comes with a two-year <b>warranty</b>.", "Sản phẩm được bảo hành hai năm.", "保証", "hoshō"),
  ("bundle", "/ˈbʌndl/", "n", "combo, gói sản phẩm", "The phone and headphones <b>bundle</b> saves you 500,000 dong.", "Mua combo điện thoại và tai nghe tiết kiệm được 500.000 đồng."),
  ("valid", "/ˈvælɪd/", "adj", "còn hiệu lực", "This price is <b>valid</b> until the end of the month.", "Giá này có hiệu lực đến cuối tháng."),
  ("upgrade", "/ˌʌpˈɡreɪd/", "v/n", "nâng cấp", "For 300,000 dong more, you can <b>upgrade</b> to the larger size.", "Thêm 300.000 đồng là anh/chị nâng cấp lên cỡ lớn hơn."),
 ],
 "phrases": [
  ("The price is 4.5 million dong, including VAT.", "Giá là 4,5 triệu đồng, đã bao gồm VAT."),
  ("We have a special offer this week.", "Tuần này bên em có ưu đãi đặc biệt."),
  ("If you buy two, you get 10% off.", "Mua hai cái thì được giảm 10%."),
  ("This price is valid until Friday.", "Giá này có hiệu lực đến thứ Sáu."),
  ("Compared to the S3, the S5 has a better camera.", "So với S3, S5 có camera tốt hơn."),
  ("It's a little more expensive, but it lasts much longer.", "Nó đắt hơn một chút nhưng dùng bền hơn nhiều."),
  ("I'll send you a quotation by the end of today.", "Cuối ngày hôm nay em sẽ gửi báo giá cho anh/chị."),
  ("The warranty covers parts and repairs for two years.", "Bảo hành bao gồm linh kiện và sửa chữa trong hai năm."),
  ("Is there anything else you'd like me to include in the quote?", "Anh/chị có muốn em thêm gì vào báo giá không ạ?"),
  ("That's the best price I can offer.", "Đó là mức giá tốt nhất em có thể đưa ra ạ."),
 ],
 "dialogues": [
  ("How much is this one?", [
    ("It's 3.2 million dong. And this week it comes with a free case.", True, "Báo giá rõ + thêm ưu đãi để tăng giá trị."),
    ("It 3.2 million.", False, "Thiếu động từ: 'It's 3.2 million dong.'"),
    ("Very cheap, only 3.2 million!", False, "Tự khen 'rẻ' khi khách chưa hỏi — nên nói rõ giá và giá trị."),
  ]),
  ("Can you give me a discount?", [
    ("I can offer 5% off if you pay today. That's the best price I can do.", True, "Giảm có điều kiện + giữ mức giá hợp lý."),
    ("No discount. Price is price.", False, "Từ chối cộc lốc, dễ mất khách."),
    ("OK, I discount for you 20%.", False, "Dùng 'discount' như động từ sai cách và giảm quá tay: 'I can give you 5% off.'"),
  ]),
  ("Why is this one more expensive than the other?", [
    ("It has a stronger motor and a three-year warranty, so it lasts much longer.", True, "Giải thích giá bằng lợi ích cụ thể."),
    ("Because it is more expensive.", False, "Trả lời vòng vo, không nêu lý do."),
    ("Because quality more better.", False, "Sai so sánh kép 'more better' và thiếu động từ: 'Because the quality is better.'"),
  ]),
  ("Can you send me a quotation for 200 units?", [
    ("Of course. I'll email you the quotation by 5 p.m. today.", True, "Đồng ý + thời hạn cụ thể."),
    ("Of course. I send you tomorrow maybe.", False, "Thiếu 'will' và tân ngữ; 'maybe' làm khách mất tin tưởng."),
    ("200 is many, wait long time.", False, "Than phiền, sai ngữ pháp, không đáp ứng yêu cầu."),
  ]),
  ("Is the special offer still valid?", [
    ("Yes, it's valid until Sunday, so you're just in time.", True, "Xác nhận + thời hạn + tạo cảm giác may mắn cho khách."),
    ("Yes, it still valid.", False, "Thiếu 'is': 'Yes, it's still valid.'"),
    ("Offer finish Sunday.", False, "Thiếu mạo từ, sai động từ: 'The offer ends on Sunday.'"),
  ]),
 ],
 "listen": [
  ("The price is valid until the end of the month", ["valid", "month"], "thời hạn của giá"),
  ("We can offer a ten percent discount today", ["ten", "discount"], "mức giảm giá"),
  ("It comes with a two-year warranty", ["two-year", "warranty"], "bảo hành"),
  ("I'll send you the quotation this afternoon", ["quotation", "afternoon"], "hẹn gửi báo giá"),
  ("This week we have a special offer. If you buy the phone, you get the headphones for free. The offer ends on Sunday.", ["special", "headphones", "Sunday"], "giới thiệu ưu đãi"),
  ("Compared to the basic model, the Pro is faster and lighter. It's about two million more. But you can upgrade later if you prefer.", ["faster", "million", "upgrade"], "so sánh hai mẫu"),
 ],
})

# ───────────────────────── 3. Xử lý từ chối & băn khoăn ─────────────────────────
PHASES.append({
 "title": "Xử lý từ chối & băn khoăn",
 "vocab": [
  ("objection", "/əbˈdʒekʃn/", "n", "lý do từ chối, ý phản đối (của khách)", "Price is the most common <b>objection</b> we hear.", "Giá là lý do từ chối phổ biến nhất bên mình hay gặp."),
  ("concern", "/kənˈsɜːn/", "n", "điều băn khoăn, lo lắng", "I understand your <b>concern</b> about the size.", "Em hiểu băn khoăn của anh/chị về kích thước."),
  ("hesitate", "/ˈhezɪteɪt/", "v", "do dự, ngần ngại", "Please don't <b>hesitate</b> to call me.", "Anh/chị đừng ngại gọi cho em nhé."),
  ("afford", "/əˈfɔːd/", "v", "đủ khả năng chi trả", "I'm not sure I can <b>afford</b> it right now.", "Tôi không chắc lúc này mình đủ tiền mua."),
  ("competitor", "/kəmˈpetɪtə/", "n", "đối thủ cạnh tranh", "Our <b>competitor</b> is cheaper, but their warranty is shorter.", "Đối thủ rẻ hơn nhưng thời gian bảo hành ngắn hơn.", "競合", "kyōgō"),
  ("benefit", "/ˈbenɪfɪt/", "n", "lợi ích", "The main <b>benefit</b> is that you save on electricity.", "Lợi ích chính là anh/chị tiết kiệm tiền điện.", "メリット", "meritto"),
  ("guarantee", "/ˌɡærənˈtiː/", "v/n", "cam kết, bảo đảm", "We <b>guarantee</b> free repairs for one year.", "Bên em cam kết sửa miễn phí trong một năm."),
  ("trial", "/ˈtraɪəl/", "n", "sự dùng thử", "You can start with a 14-day free <b>trial</b>.", "Anh/chị có thể bắt đầu với 14 ngày dùng thử miễn phí."),
  ("reassure", "/ˌriːəˈʃʊə/", "v", "trấn an, làm yên tâm", "She <b>reassured</b> the customer that installation was free.", "Cô ấy trấn an khách rằng lắp đặt là miễn phí."),
  ("think it over", "/ˌθɪŋk ɪt ˈəʊvə/", "phr v", "suy nghĩ thêm", "Take your time to <b>think it over</b>.", "Anh/chị cứ thong thả suy nghĩ thêm nhé."),
 ],
 "phrases": [
  ("I understand your concern.", "Em hiểu điều anh/chị băn khoăn."),
  ("That's a fair question.", "Anh/chị hỏi vậy là rất hợp lý ạ."),
  ("Can I ask what's stopping you from deciding today?", "Em có thể hỏi điều gì khiến anh/chị chưa quyết định hôm nay không ạ?"),
  ("Many customers felt the same at first.", "Nhiều khách lúc đầu cũng nghĩ vậy ạ."),
  ("Let me explain why it's worth the price.", "Để em giải thích vì sao sản phẩm đáng với giá tiền."),
  ("If price is the issue, we also have a basic version.", "Nếu vấn đề là giá, bên em cũng có bản cơ bản ạ."),
  ("You can try it free for 14 days.", "Anh/chị có thể dùng thử miễn phí 14 ngày."),
  ("No pressure. Take your time to think it over.", "Không vội đâu ạ. Anh/chị cứ thong thả suy nghĩ thêm."),
  ("Would it help if I sent you some customer reviews?", "Em gửi anh/chị vài đánh giá của khách hàng thì có giúp ích không ạ?"),
  ("When would be a good time for me to call you again?", "Khi nào em gọi lại thì tiện cho anh/chị ạ?"),
 ],
 "dialogues": [
  ("It's too expensive.", [
    ("I understand. It costs more at first, but it uses 30% less electricity, so you save money every month.", True, "Đồng cảm + chuyển sang lợi ích lâu dài."),
    ("It is not expensive. You are wrong.", False, "Cãi lại khách — mất thiện cảm ngay."),
    ("Expensive but good, you should buy.", False, "Thiếu chủ ngữ/động từ và ép mua, không giải thích giá trị."),
  ]),
  ("I need to think about it.", [
    ("Of course. Is there anything I can explain to help you decide?", True, "Tôn trọng + mở lời tìm hiểu băn khoăn thật."),
    ("Why you need think? It's a good price.", False, "Sai ngữ pháp ('Why do you need to…') và gây áp lực."),
    ("OK. Bye.", False, "Buông khách quá nhanh, không hỏi thêm hay hẹn liên hệ lại."),
  ]),
  ("Another shop sells it cheaper.", [
    ("That's possible. With us, you also get free installation and a two-year warranty.", True, "Không chê đối thủ, nêu giá trị cộng thêm của mình."),
    ("That shop sells fake products.", False, "Nói xấu đối thủ khi không có bằng chứng — thiếu chuyên nghiệp."),
    ("So you go to that shop.", False, "Như đuổi khách — mất đơn ngay."),
  ]),
  ("I'm not sure it will work for my business.", [
    ("That's a fair concern. Why don't you try it free for 14 days and see?", True, "Công nhận băn khoăn + đề xuất dùng thử để giảm rủi ro."),
    ("Sure it will work. Trust me.", False, "Hứa suông, không có bằng chứng hay giải pháp."),
    ("It is work for all business.", False, "Sai: 'It works for all kinds of businesses.'"),
  ]),
  ("I already use another brand.", [
    ("I see. May I ask what you like about it? Then I can show you what's different about ours.", True, "Hỏi để hiểu khách + so sánh có mục tiêu."),
    ("Other brand is not good as us.", False, "Thiếu mạo từ, sai so sánh ('not as good as ours') và chê đối thủ."),
    ("Why you don't change?", False, "Sai trật tự câu hỏi ('Why don't you…') và nghe ép buộc."),
  ]),
 ],
 "listen": [
  ("I understand your concern about the price", ["understand", "concern"], "đồng cảm với khách"),
  ("You can try it free for fourteen days", ["try", "fourteen"], "đề nghị dùng thử"),
  ("Please don't hesitate to call me", ["hesitate", "call"], "mời khách liên hệ"),
  ("Take your time to think it over", ["time", "think"], "để khách suy nghĩ"),
  ("I understand it's more expensive. But it uses less electricity, so you save money every month. Would you like to see the numbers?", ["expensive", "electricity", "numbers"], "xử lý lời chê đắt"),
  ("Many customers worried about the size at first. Now they love it because it's easy to store. We also have a thirty-day return policy.", ["size", "store", "thirty-day"], "trấn an khách"),
 ],
})

# ───────────────────────── 4. Chốt đơn & thanh toán ─────────────────────────
PHASES.append({
 "title": "Chốt đơn & thanh toán",
 "vocab": [
  ("order", "/ˈɔːdə/", "n/v", "đơn hàng; đặt hàng", "Shall I place the <b>order</b> for you now?", "Em đặt đơn cho anh/chị luôn nhé?", "注文", "chūmon"),
  ("checkout", "/ˈtʃekaʊt/", "n", "quầy thanh toán; bước thanh toán", "Please follow me to the <b>checkout</b>.", "Mời anh/chị theo em ra quầy thanh toán."),
  ("payment", "/ˈpeɪmənt/", "n", "sự thanh toán", "We accept <b>payment</b> by card, cash or QR code.", "Bên em nhận thanh toán bằng thẻ, tiền mặt hoặc mã QR.", "支払い", "shiharai"),
  ("instalment", "/ɪnˈstɔːlmənt/", "n", "khoản trả góp", "You can pay in six monthly <b>instalments</b> with 0% interest.", "Anh/chị có thể trả góp sáu tháng, lãi suất 0%.", "分割払い", "bunkatsu barai"),
  ("receipt", "/rɪˈsiːt/", "n", "hóa đơn bán lẻ, biên lai", "Here's your <b>receipt</b>. Please keep it for the warranty.", "Đây là hóa đơn của anh/chị, vui lòng giữ lại để bảo hành.", "領収書", "ryōshūsho"),
  ("invoice", "/ˈɪnvɔɪs/", "n", "hóa đơn đề nghị thanh toán, hóa đơn VAT", "We'll send the <b>invoice</b> with the goods.", "Bên em sẽ gửi hóa đơn kèm theo hàng.", "請求書", "seikyūsho"),
  ("deposit", "/dɪˈpɒzɪt/", "n", "tiền đặt cọc", "A 30% <b>deposit</b> is needed to start the order.", "Cần đặt cọc 30% để bắt đầu xử lý đơn."),
  ("bank transfer", "/ˈbæŋk ˌtrænsfɜː/", "n", "chuyển khoản ngân hàng", "You can pay by <b>bank transfer</b> within seven days.", "Anh/chị có thể chuyển khoản trong vòng bảy ngày.", "銀行振込", "ginkō furikomi"),
  ("close a deal", "/ˌkləʊz ə ˈdiːl/", "phr", "chốt đơn, chốt hợp đồng", "Hùng <b>closed a deal</b> with a hotel chain yesterday.", "Hôm qua Hùng đã chốt được hợp đồng với một chuỗi khách sạn."),
  ("contract", "/ˈkɒntrækt/", "n", "hợp đồng", "Please sign the <b>contract</b> on page three.", "Anh/chị vui lòng ký hợp đồng ở trang ba.", "契約", "keiyaku"),
 ],
 "phrases": [
  ("Great choice! Shall I get one ready for you?", "Anh/chị chọn chuẩn quá! Em chuẩn bị một cái cho anh/chị nhé?"),
  ("How would you like to pay?", "Anh/chị muốn thanh toán bằng hình thức nào ạ?"),
  ("We accept cash, card and bank transfer.", "Bên em nhận tiền mặt, thẻ và chuyển khoản."),
  ("Would you like to pay in instalments?", "Anh/chị có muốn trả góp không ạ?"),
  ("Please enter your PIN.", "Anh/chị vui lòng nhập mã PIN."),
  ("Do you need a VAT invoice?", "Anh/chị có cần xuất hóa đơn VAT không ạ?"),
  ("Here's your receipt and your change.", "Đây là hóa đơn và tiền thừa của anh/chị."),
  ("Could I have your company name and tax code for the invoice?", "Cho em xin tên công ty và mã số thuế để xuất hóa đơn ạ."),
  ("Once we receive the deposit, we'll start your order.", "Sau khi nhận tiền cọc, bên em sẽ bắt đầu xử lý đơn của anh/chị."),
  ("Thank you for your order!", "Cảm ơn anh/chị đã đặt hàng!"),
 ],
 "dialogues": [
  ("OK, I'll take it.", [
    ("Great choice! How would you like to pay: cash, card or QR code?", True, "Khen lựa chọn + hỏi ngay hình thức thanh toán."),
    ("OK. You pay how?", False, "Sai trật tự câu hỏi: 'How would you like to pay?'"),
    ("Really? You don't want the more expensive one?", False, "Khách đã chốt mà còn nghi ngờ lựa chọn — dễ làm khách đổi ý."),
  ]),
  ("Can I pay in instalments?", [
    ("Yes, you can pay over six or twelve months with 0% interest. You just need your ID card.", True, "Trả lời có + điều kiện cụ thể."),
    ("Yes, can. Six month.", False, "Thiếu chủ ngữ và 's': 'Yes, you can pay over six months.'"),
    ("Instalment is for people no money.", False, "Xúc phạm khách và sai ngữ pháp."),
  ]),
  ("Do I need to pay everything now?", [
    ("No, just a 30% deposit today. You can pay the rest when the goods arrive.", True, "Nói rõ tiền cọc và thời điểm trả phần còn lại."),
    ("No, you pay deposit only today, rest later.", False, "Thiếu mạo từ, lủng củng và không nói rõ tỷ lệ cọc."),
    ("Yes, you must pay all now.", False, "Sai chính sách (chỉ cần cọc) và nghe ép khách."),
  ]),
  ("I need a VAT invoice for my company.", [
    ("No problem. Could I have your company name, address and tax code, please?", True, "Đồng ý + xin đủ thông tin cần thiết, lịch sự."),
    ("Give me tax code.", False, "Mệnh lệnh cộc lốc, thiếu 'your' và 'please'."),
    ("Invoice is difficult, maybe next week.", False, "Khó khăn nội bộ không phải việc của khách — hãy hướng dẫn cách xuất hóa đơn."),
  ]),
  ("The card machine says 'declined'.", [
    ("I'm sorry about that. Would you like to try again, or pay by QR code instead?", True, "Xin lỗi tế nhị + đưa phương án khác, không làm khách ngại."),
    ("Your card no money.", False, "Thiếu động từ và làm khách xấu hổ."),
    ("Machine is broken, not my problem.", False, "Đổ lỗi, không giúp khách thanh toán."),
  ]),
 ],
 "listen": [
  ("How would you like to pay today", ["pay", "today"], "hỏi cách thanh toán"),
  ("We accept cash, card and bank transfer", ["cash", "transfer"], "các hình thức thanh toán"),
  ("Here's your receipt and your change", ["receipt", "change"], "đưa hóa đơn cho khách"),
  ("You can pay in six monthly instalments", ["six", "instalments"], "trả góp"),
  ("Thank you for your order. Please pay a thirty percent deposit by Friday. We'll send the invoice with the goods.", ["order", "deposit", "invoice"], "xác nhận đơn doanh nghiệp"),
  ("That's two million four hundred thousand dong. Would you like to pay by card? Please enter your PIN here.", ["million", "card", "PIN"], "thanh toán tại quầy"),
 ],
})

# ───────────────────────── 5. Gọi điện chăm sóc khách hàng ─────────────────────────
PHASES.append({
 "title": "Gọi điện chăm sóc khách hàng",
 "vocab": [
  ("verify", "/ˈverɪfaɪ/", "v", "xác minh", "Before we continue, I need to <b>verify</b> your identity.", "Trước khi tiếp tục, em cần xác minh danh tính của anh/chị."),
  ("account", "/əˈkaʊnt/", "n", "tài khoản", "What's the phone number on your <b>account</b>?", "Số điện thoại đăng ký tài khoản của anh/chị là gì ạ?"),
  ("date of birth", "/ˌdeɪt əv ˈbɜːθ/", "n", "ngày sinh", "Can I have your full name and <b>date of birth</b>, please?", "Cho em xin họ tên đầy đủ và ngày sinh ạ.", "生年月日", "seinengappi"),
  ("transfer", "/trænsˈfɜː/", "v", "chuyển (cuộc gọi)", "I'll <b>transfer</b> you to our technical team.", "Em sẽ chuyển máy cho anh/chị sang bộ phận kỹ thuật."),
  ("escalate", "/ˈeskəleɪt/", "v", "chuyển lên cấp cao hơn xử lý", "If I can't solve it, I'll <b>escalate</b> it to my supervisor.", "Nếu em không xử lý được, em sẽ chuyển lên cấp trên."),
  ("hotline", "/ˈhɒtlaɪn/", "n", "đường dây nóng, tổng đài", "Our <b>hotline</b> is open 24/7.", "Tổng đài của bên em hoạt động 24/7."),
  ("inquiry", "/ɪnˈkwaɪəri/", "n", "yêu cầu hỏi thông tin, thắc mắc", "Thank you for your <b>inquiry</b> about our new plans.", "Cảm ơn anh/chị đã hỏi về các gói mới của bên em.", "問い合わせ", "toiawase"),
  ("patience", "/ˈpeɪʃns/", "n", "sự kiên nhẫn", "Thank you for your <b>patience</b>.", "Cảm ơn anh/chị đã kiên nhẫn chờ."),
  ("satisfaction", "/ˌsætɪsˈfækʃn/", "n", "sự hài lòng", "Customer <b>satisfaction</b> is our top priority.", "Sự hài lòng của khách hàng là ưu tiên hàng đầu của bên em.", "満足度", "manzokudo"),
  ("membership", "/ˈmembəʃɪp/", "n", "tư cách hội viên, thẻ thành viên", "Your <b>membership</b> gives you free delivery.", "Thẻ thành viên giúp anh/chị được giao hàng miễn phí.", "会員", "kaiin"),
 ],
 "phrases": [
  ("Thank you for calling Zenta customer service. This is Linh. How can I help you?", "Cảm ơn anh/chị đã gọi đến CSKH Zenta. Em là Linh. Em có thể giúp gì cho anh/chị ạ?"),
  ("For security, could you confirm your full name and date of birth?", "Để bảo mật, anh/chị vui lòng xác nhận họ tên đầy đủ và ngày sinh ạ."),
  ("Thank you. Your identity has been verified.", "Cảm ơn anh/chị. Danh tính đã được xác minh."),
  ("May I put you on hold for two minutes while I check?", "Em xin phép giữ máy hai phút để kiểm tra nhé ạ?"),
  ("Thank you for holding.", "Cảm ơn anh/chị đã chờ máy."),
  ("I'll transfer you to the billing team. Please stay on the line.", "Em sẽ chuyển máy sang bộ phận thanh toán. Anh/chị vui lòng giữ máy."),
  ("Sorry, the line isn't very clear. Could you say that again?", "Xin lỗi, đường truyền không rõ lắm. Anh/chị nói lại giúp em được không ạ?"),
  ("I'm calling to check that everything is working well.", "Em gọi để hỏi xem mọi thứ có hoạt động tốt không ạ."),
  ("Is there anything else I can help you with today?", "Anh/chị còn cần em hỗ trợ gì nữa không ạ?"),
  ("Thank you for calling. Have a nice day!", "Cảm ơn anh/chị đã gọi. Chúc anh/chị một ngày tốt lành!"),
 ],
 "dialogues": [
  ("Hi, I have a question about my bill.", [
    ("Of course. Before we start, could I have your full name and the phone number on the account?", True, "Nhận yêu cầu + xác minh danh tính trước — đúng quy trình."),
    ("OK. What is your bill?", False, "Hỏi mơ hồ và bỏ qua bước xác minh danh tính."),
    ("Tell me name, phone.", False, "Cộc lốc như ra lệnh; nên nói 'Could I have your name, please?'"),
  ]),
  ("Can you check why my internet is so slow?", [
    ("Sure. May I put you on hold for about two minutes while I check your line?", True, "Xin phép giữ máy + nói rõ thời gian và lý do."),
    ("Wait.", False, "Quá cộc; phải xin phép và nói khách chờ bao lâu."),
    ("You wait me two minute.", False, "Sai: 'Please hold for two minutes' (không nói 'wait me', thiếu 's')."),
  ]),
  ("I've been waiting on the line for twenty minutes!", [
    ("I'm really sorry for the long wait, and thank you for your patience. How can I help you today?", True, "Xin lỗi chân thành + cảm ơn sự kiên nhẫn + chuyển sang giúp."),
    ("Sorry, many customer call today.", False, "Thiếu 's' và động từ ('many customers are calling'), nghe như bào chữa."),
    ("It's not long. Other people wait more.", False, "Phủ nhận cảm xúc của khách — khách càng bực."),
  ]),
  ("I want to speak to a manager.", [
    ("I understand. Let me try to help first, and if I can't solve it, I'll escalate it to my supervisor right away.", True, "Tôn trọng yêu cầu + đề nghị hỗ trợ trước + cam kết chuyển cấp."),
    ("Manager is busy, no.", False, "Từ chối cộc lốc, khách sẽ càng khó chịu."),
    ("Why you want manager? I can do.", False, "Sai ngữ pháp và nghe như thách thức khách."),
  ]),
  ("Is there someone who can help with a technical problem?", [
    ("Yes, I'll transfer you to our technical team now. Please stay on the line.", True, "Nói rõ chuyển tới đâu + dặn khách giữ máy."),
    ("Yes, I transfer you.", False, "Thiếu 'will' và không dặn khách giữ máy: 'I'll transfer you now.'"),
    ("Technical is not my job.", False, "Đẩy trách nhiệm, không giúp khách tìm đúng bộ phận."),
  ]),
 ],
 "listen": [
  ("Thank you for calling, how can I help you", ["calling", "help"], "câu chào tổng đài"),
  ("Could you confirm your date of birth, please", ["confirm", "birth"], "xác minh danh tính"),
  ("I'll transfer you to the billing team", ["transfer", "billing"], "chuyển máy"),
  ("Thank you for your patience", ["patience"], "cảm ơn khách đã chờ"),
  ("Thank you for holding. I've checked your account. Your payment arrived yesterday, so your service is active again.", ["holding", "account", "active"], "quay lại sau khi giữ máy"),
  ("Hello, this is Minh from Zenta customer care. I'm calling to follow up on your repair. Is the washing machine working well now?", ["care", "repair", "washing"], "gọi chăm sóc sau sửa chữa"),
 ],
})

# ───────────────────────── 6. Khiếu nại, đổi trả & hoàn tiền ─────────────────────────
PHASES.append({
 "title": "Khiếu nại, đổi trả & hoàn tiền",
 "vocab": [
  ("refund", "/ˈriːfʌnd/", "n", "khoản hoàn tiền", "Your <b>refund</b> will arrive in five to seven working days.", "Tiền hoàn sẽ về trong năm đến bảy ngày làm việc.", "返金", "henkin"),
  ("return", "/rɪˈtɜːn/", "v/n", "trả lại (hàng); việc trả hàng", "You can <b>return</b> it within 30 days.", "Anh/chị có thể trả hàng trong vòng 30 ngày.", "返品", "henpin"),
  ("exchange", "/ɪksˈtʃeɪndʒ/", "v/n", "đổi (hàng)", "Would you like to <b>exchange</b> it for a bigger size?", "Anh/chị có muốn đổi sang cỡ lớn hơn không ạ?", "交換", "kōkan"),
  ("faulty", "/ˈfɔːlti/", "adj", "bị lỗi (do sản xuất)", "If the item is <b>faulty</b>, we'll replace it for free.", "Nếu sản phẩm bị lỗi, bên em sẽ đổi cái mới miễn phí."),
  ("damaged", "/ˈdæmɪdʒd/", "adj", "bị hư hỏng, móp méo", "The box was <b>damaged</b> during delivery.", "Hộp bị móp trong lúc giao hàng."),
  ("policy", "/ˈpɒləsi/", "n", "chính sách", "Our return <b>policy</b> is 30 days with the receipt.", "Chính sách đổi trả của bên em là 30 ngày, kèm hóa đơn."),
  ("compensation", "/ˌkɒmpenˈseɪʃn/", "n", "khoản bồi thường, bù đắp", "We'll give you a voucher as <b>compensation</b>.", "Bên em xin gửi anh/chị một voucher để bù đắp.", "補償", "hoshō"),
  ("inconvenience", "/ˌɪnkənˈviːniəns/", "n", "sự bất tiện, phiền toái", "We're sorry for the <b>inconvenience</b>.", "Bên em xin lỗi vì sự bất tiện này."),
  ("reference number", "/ˈrefrəns ˌnʌmbə/", "n", "mã số yêu cầu (tham chiếu)", "Your <b>reference number</b> is CS-4581.", "Mã số yêu cầu của anh/chị là CS-4581."),
  ("frustrated", "/frʌˈstreɪtɪd/", "adj", "bực bội, bức xúc", "I understand you're <b>frustrated</b>, and I'm here to help.", "Em hiểu anh/chị đang bức xúc, em sẽ hỗ trợ ngay ạ."),
 ],
 "phrases": [
  ("I'm very sorry to hear that.", "Em rất tiếc khi nghe điều đó."),
  ("I completely understand how you feel.", "Em hoàn toàn hiểu cảm giác của anh/chị."),
  ("Could you tell me exactly what happened?", "Anh/chị kể giúp em chính xác chuyện gì đã xảy ra được không ạ?"),
  ("Could you send me a photo of the damaged item?", "Anh/chị gửi giúp em ảnh sản phẩm bị hư được không ạ?"),
  ("You can return it within 30 days with the receipt.", "Anh/chị có thể trả hàng trong 30 ngày, kèm hóa đơn."),
  ("Would you prefer an exchange or a refund?", "Anh/chị muốn đổi hàng hay hoàn tiền ạ?"),
  ("Your refund will be processed within seven working days.", "Tiền hoàn sẽ được xử lý trong vòng bảy ngày làm việc."),
  ("We're sorry for the inconvenience.", "Bên em xin lỗi vì sự bất tiện."),
  ("Here's your reference number, in case you need to call again.", "Đây là mã yêu cầu của anh/chị, phòng khi cần gọi lại."),
  ("I'll personally make sure this is fixed.", "Em sẽ trực tiếp đảm bảo việc này được xử lý."),
 ],
 "dialogues": [
  ("The blender I bought yesterday doesn't work!", [
    ("I'm so sorry about that. Could you tell me what happens when you turn it on?", True, "Xin lỗi + hỏi chi tiết để xử lý."),
    ("Impossible. We test everything before selling.", False, "Phủ nhận lỗi, đổ ngược cho khách."),
    ("Maybe you use wrong.", False, "Sai ngữ pháp ('you used it wrongly') và đổ lỗi cho khách."),
  ]),
  ("I want my money back.", [
    ("I understand. Since the item is faulty, we can give you a full refund. It will take about five working days.", True, "Đồng ý theo chính sách + nói rõ thời gian hoàn tiền."),
    ("Money back is not possible, company rule.", False, "Từ chối cứng nhắc, không giải thích hay đưa phương án khác."),
    ("OK, I give back money tomorrow maybe.", False, "Sai trật tự ('give you your money back') và hứa không chắc chắn."),
  ]),
  ("Can I exchange this shirt? It's too small.", [
    ("Of course. Do you have the receipt? Then I can get you a bigger size.", True, "Đồng ý + hỏi hóa đơn + giải pháp cụ thể."),
    ("You buy wrong size, not our fault.", False, "Đổ lỗi, thiếu lịch sự dù khách đúng là chọn nhầm cỡ."),
    ("Can. Where is bill?", False, "Thiếu chủ ngữ, cộc lốc: 'Sure. Do you have the receipt?'"),
  ]),
  ("This is the third time I've called about this problem!", [
    ("I'm really sorry you've had to call again. I'll handle this myself and call you back before 5 p.m. today.", True, "Xin lỗi chân thành + nhận trách nhiệm + hẹn giờ cụ thể."),
    ("Sorry, other staff didn't write it down.", False, "Đổ lỗi cho đồng nghiệp — khách không quan tâm lỗi của ai."),
    ("Please calm down.", False, "Bảo khách 'bình tĩnh' thường làm khách bực hơn."),
  ]),
  ("My order arrived damaged. What are you going to do about it?", [
    ("I apologise for that. We'll send you a new one today, and you don't need to return the damaged one.", True, "Xin lỗi + giải pháp rõ ràng, nhanh gọn cho khách."),
    ("Damaged is shipping company fault.", False, "Đổ lỗi cho bên giao hàng; khách mua của mình nên mình phải chịu trách nhiệm."),
    ("I will check. Maybe next week.", False, "Mơ hồ, chậm, không cho khách giải pháp."),
  ]),
 ],
 "listen": [
  ("Would you prefer an exchange or a refund", ["exchange", "refund"], "hỏi khách muốn đổi hay hoàn tiền"),
  ("We're very sorry for the inconvenience", ["sorry", "inconvenience"], "xin lỗi khách"),
  ("You can return it within thirty days", ["return", "thirty"], "chính sách trả hàng"),
  ("Please keep your reference number for next time", ["reference", "next"], "mã yêu cầu"),
  ("I'm sorry the box arrived damaged. Could you send us a photo of it? We'll send a new one tomorrow.", ["damaged", "photo", "tomorrow"], "xử lý hàng bị hư"),
  ("Your refund has been approved. The money will be back in your account in five working days. We're sorry again for the trouble.", ["approved", "five", "trouble"], "báo đã duyệt hoàn tiền"),
 ],
})

# ───────────────────────── 7. Hỗ trợ qua chat & email ─────────────────────────
PHASES.append({
 "title": "Hỗ trợ qua chat & email",
 "vocab": [
  ("live chat", "/ˌlaɪv ˈtʃæt/", "n", "chat trực tuyến (với nhân viên)", "Our <b>live chat</b> is open from 8 a.m. to 10 p.m.", "Kênh chat trực tuyến hoạt động từ 8 giờ sáng đến 10 giờ tối."),
  ("response time", "/rɪˈspɒns ˌtaɪm/", "n", "thời gian phản hồi", "Our average <b>response time</b> is two minutes.", "Thời gian phản hồi trung bình của bên em là hai phút."),
  ("screenshot", "/ˈskriːnʃɒt/", "n", "ảnh chụp màn hình", "Could you send me a <b>screenshot</b> of the error?", "Anh/chị gửi giúp em ảnh chụp màn hình báo lỗi nhé."),
  ("template", "/ˈtempleɪt/", "n", "mẫu soạn sẵn", "Use this <b>template</b>, but add the customer's name.", "Dùng mẫu này nhưng nhớ thêm tên khách.", "テンプレート", "tenpurēto"),
  ("acknowledge", "/əkˈnɒlɪdʒ/", "v", "xác nhận đã nhận; ghi nhận", "We <b>acknowledge</b> every email within one hour.", "Bên em xác nhận đã nhận mọi email trong vòng một giờ."),
  ("step-by-step", "/ˌstep baɪ ˈstep/", "adj", "từng bước một", "Here's a <b>step-by-step</b> guide to reset your password.", "Đây là hướng dẫn từng bước để đặt lại mật khẩu."),
  ("resolve", "/rɪˈzɒlv/", "v", "giải quyết (dứt điểm)", "We aim to <b>resolve</b> every case within 48 hours.", "Bên em đặt mục tiêu giải quyết mọi trường hợp trong 48 giờ.", "解決する", "kaiketsu suru"),
  ("case", "/keɪs/", "n", "trường hợp, hồ sơ yêu cầu hỗ trợ", "I've opened a <b>case</b> for your problem.", "Em đã mở một hồ sơ hỗ trợ cho vấn đề của anh/chị."),
  ("FAQ", "/ˌef eɪ ˈkjuː/", "n", "mục câu hỏi thường gặp", "You can find the answer in our <b>FAQ</b> section.", "Anh/chị có thể tìm câu trả lời ở mục Câu hỏi thường gặp.", "よくある質問", "yoku aru shitsumon"),
  ("log in", "/ˌlɒɡ ˈɪn/", "phr v", "đăng nhập", "Please <b>log in</b> to your account and click 'My orders'.", "Anh/chị đăng nhập tài khoản rồi bấm 'My orders' nhé."),
 ],
 "phrases": [
  ("Hi Mai, thanks for reaching out. I'm happy to help.", "Chào chị Mai, cảm ơn chị đã liên hệ. Em rất sẵn lòng hỗ trợ."),
  ("Could you give me your order number, please?", "Chị cho em xin mã đơn hàng nhé."),
  ("Give me a moment while I check that for you.", "Chị đợi em một chút để em kiểm tra nhé."),
  ("Could you send a screenshot of the error message?", "Chị gửi giúp em ảnh chụp màn hình thông báo lỗi nhé."),
  ("Please follow these steps. First, log in to your account.", "Chị làm theo các bước sau nhé. Đầu tiên, đăng nhập tài khoản."),
  ("Does that answer your question?", "Như vậy đã giải đáp thắc mắc của chị chưa ạ?"),
  ("Thank you for your email. We have received your request.", "Cảm ơn anh/chị đã gửi email. Bên em đã nhận được yêu cầu."),
  ("We will get back to you within 24 hours.", "Bên em sẽ phản hồi trong vòng 24 giờ."),
  ("I've passed your case to our technical team.", "Em đã chuyển trường hợp của anh/chị sang đội kỹ thuật."),
  ("Is there anything else I can help with? Have a great day!", "Anh/chị còn cần hỗ trợ gì nữa không ạ? Chúc anh/chị một ngày tuyệt vời!"),
 ],
 "dialogues": [
  ("hi, I can't log in to my account", [
    ("Hi, sorry to hear that! Could you tell me what message you see when you try to log in?", True, "Chào + đồng cảm + hỏi thông tin cụ thể."),
    ("You forget password?", False, "Thiếu trợ động từ ('Did you forget your password?') và đoán vội."),
    ("Please read FAQ.", False, "Đẩy khách đi tự đọc, không hỗ trợ trực tiếp."),
  ]),
  ("Where is my order? I ordered it five days ago.", [
    ("Let me check for you. Could you give me your order number, please?", True, "Nhận việc + xin mã đơn lịch sự."),
    ("Order number?", False, "Quá cộc — qua chat càng dễ bị hiểu là khó chịu."),
    ("I don't know where. Ask shipping company.", False, "Đẩy khách sang bên khác, không kiểm tra giúp."),
  ]),
  ("Why hasn't anyone answered my email? I sent it on Monday!", [
    ("I'm sorry for the late reply. I've found your email, and I'll resolve it for you now.", True, "Xin lỗi phản hồi chậm + hành động ngay."),
    ("We very busy this week.", False, "Thiếu 'are' và chỉ bào chữa, không giải quyết."),
    ("Monday is holiday, so late.", False, "Dịch từng chữ, thiếu mạo từ và chỉ bào chữa."),
  ]),
  ("I tried everything but the app still crashes.", [
    ("Thanks for trying. Could you send me a screenshot and tell me your phone model? I'll pass it to our technical team.", True, "Cảm ơn + xin thông tin cần thiết + nói bước tiếp theo."),
    ("You try again.", False, "Mệnh lệnh cộc — khách đã thử rồi."),
    ("Your phone is too old maybe.", False, "Đoán mò và đổ lỗi cho thiết bị của khách."),
  ]),
  ("Thanks, it works now!", [
    ("Great, I'm glad it's working! Is there anything else I can help you with?", True, "Vui cùng khách + hỏi thêm trước khi kết thúc."),
    ("OK. Close chat.", False, "Cộc lốc, kết thúc đột ngột."),
    ("Of course it works, I told you.", False, "Nghe kiêu ngạo, làm khách khó chịu."),
  ]),
 ],
 "listen": [
  ("Could you send a screenshot of the error", ["screenshot", "error"], "xin ảnh chụp màn hình"),
  ("We will get back to you within twenty-four hours", ["back", "twenty-four"], "hẹn thời gian phản hồi"),
  ("Please log in and check your order history", ["log", "history"], "hướng dẫn kiểm tra đơn"),
  ("You can find the answer in our FAQ section", ["answer", "FAQ"], "chỉ khách mục FAQ"),
  ("Dear Ms. Hoa, thank you for your email. We have received your request about the missing item. We will reply within one working day.", ["email", "missing", "working"], "email xác nhận đã nhận yêu cầu"),
  ("Hi, thanks for waiting! I've checked your order. It left our warehouse this morning, so it should arrive tomorrow.", ["waiting", "warehouse", "tomorrow"], "trả lời khách qua chat"),
 ],
})

# ───────────────────────── 8. Giao hàng & theo dõi đơn ─────────────────────────
PHASES.append({
 "title": "Giao hàng & theo dõi đơn",
 "vocab": [
  ("delivery", "/dɪˈlɪvəri/", "n", "việc giao hàng", "<b>Delivery</b> takes two to three days in Hà Nội.", "Giao hàng trong Hà Nội mất hai đến ba ngày.", "配送", "haisō"),
  ("shipping fee", "/ˈʃɪpɪŋ ˌfiː/", "n", "phí vận chuyển", "There's no <b>shipping fee</b> for orders over 500,000 dong.", "Đơn trên 500.000 đồng được miễn phí vận chuyển.", "送料", "sōryō"),
  ("tracking number", "/ˈtrækɪŋ ˌnʌmbə/", "n", "mã vận đơn", "Here's your <b>tracking number</b>: VN2048.", "Đây là mã vận đơn của anh/chị: VN2048.", "追跡番号", "tsuiseki bangō"),
  ("courier", "/ˈkʊriə/", "n", "nhân viên / đơn vị giao hàng", "The <b>courier</b> will call you before he arrives.", "Anh giao hàng sẽ gọi cho anh/chị trước khi tới."),
  ("dispatch", "/dɪˈspætʃ/", "v", "gửi hàng đi, xuất kho", "Your order was <b>dispatched</b> this morning.", "Đơn của anh/chị đã được xuất kho sáng nay.", "出荷", "shukka"),
  ("out of stock", "/ˌaʊt əv ˈstɒk/", "phr", "hết hàng", "Sorry, the red one is <b>out of stock</b> until next week.", "Xin lỗi, màu đỏ đang hết hàng đến tuần sau.", "在庫切れ", "zaikogire"),
  ("cash on delivery", "/ˌkæʃ ɒn dɪˈlɪvəri/", "n", "thanh toán khi nhận hàng (COD)", "Most customers choose <b>cash on delivery</b>.", "Phần lớn khách chọn thanh toán khi nhận hàng.", "代金引換", "daikin hikikae"),
  ("address", "/əˈdres/", "n", "địa chỉ", "Could you confirm your delivery <b>address</b>?", "Anh/chị xác nhận giúp em địa chỉ giao hàng nhé.", "住所", "jūsho"),
  ("package", "/ˈpækɪdʒ/", "n", "kiện hàng, gói hàng", "Your <b>package</b> is on its way.", "Kiện hàng của anh/chị đang trên đường giao.", "荷物", "nimotsu"),
  ("recipient", "/rɪˈsɪpiənt/", "n", "người nhận", "Please write the <b>recipient</b>'s name and phone number.", "Vui lòng ghi tên và số điện thoại người nhận.", "受取人", "uketorinin"),
 ],
 "phrases": [
  ("Your order has been dispatched.", "Đơn hàng của anh/chị đã được gửi đi."),
  ("It should arrive in two to three working days.", "Hàng sẽ đến trong khoảng hai đến ba ngày làm việc."),
  ("You can track your order with this number.", "Anh/chị có thể theo dõi đơn bằng mã này."),
  ("Could you confirm your delivery address, please?", "Anh/chị xác nhận giúp em địa chỉ giao hàng nhé."),
  ("The courier will call you 30 minutes before delivery.", "Nhân viên giao hàng sẽ gọi anh/chị 30 phút trước khi giao."),
  ("Delivery is free for orders over 500,000 dong.", "Miễn phí giao hàng cho đơn trên 500.000 đồng."),
  ("I'm sorry, your order is delayed because of the heavy rain.", "Em xin lỗi, đơn hàng bị chậm do mưa lớn."),
  ("Would you like to change the delivery time?", "Anh/chị có muốn đổi giờ giao không ạ?"),
  ("That item is out of stock, but it'll be back next Monday.", "Món đó đang hết hàng, thứ Hai tuần sau sẽ có lại ạ."),
  ("Please check the package before you sign.", "Anh/chị vui lòng kiểm tra hàng trước khi ký nhận."),
 ],
 "dialogues": [
  ("When will my order arrive?", [
    ("It was dispatched this morning, so it should arrive on Thursday.", True, "Nêu trạng thái đơn + ngày dự kiến."),
    ("It arrive Thursday.", False, "Thiếu 'will'/'should' và 'on': 'It will arrive on Thursday.'"),
    ("Soon, soon.", False, "Mơ hồ, khách không biết khi nào nhận hàng."),
  ]),
  ("Can I change my delivery address?", [
    ("Yes, you can, as long as the order hasn't been dispatched. What's the new address?", True, "Đồng ý có điều kiện + hỏi thông tin mới."),
    ("Yes, change OK. Address new?", False, "Thiếu động từ, trật tự kiểu tiếng Việt: 'What's the new address?'"),
    ("No, cannot change.", False, "Thiếu chủ ngữ và từ chối khi chưa kiểm tra."),
  ]),
  ("The tracking page hasn't updated for three days.", [
    ("I'm sorry about that. Let me contact the courier and get back to you within an hour.", True, "Xin lỗi + hành động cụ thể + thời gian phản hồi."),
    ("It is normal, don't worry.", False, "Gạt đi lo lắng của khách, không kiểm tra gì."),
    ("Tracking page not our system.", False, "Thiếu động từ 'is' và đẩy trách nhiệm."),
  ]),
  ("Do you offer cash on delivery?", [
    ("Yes, we do. You can pay the courier in cash when you receive the package.", True, "Trả lời đầy đủ + giải thích cách làm."),
    ("Yes, have cash on delivery.", False, "Thiếu chủ ngữ: 'Yes, we offer cash on delivery.'"),
    ("Yes, but you must pay first.", False, "Mâu thuẫn — COD là trả tiền khi nhận hàng."),
  ]),
  ("I wasn't home when the courier came.", [
    ("No problem. The courier will try again tomorrow. What time is best for you?", True, "Trấn an + phương án giao lại + hỏi giờ tiện cho khách."),
    ("Why you not at home?", False, "Sai ngữ pháp ('Why weren't you…') và trách khách."),
    ("So your package go back to warehouse.", False, "Sai động từ ('will go back to the warehouse') và không đưa giải pháp."),
  ]),
 ],
 "listen": [
  ("Your order was dispatched this morning", ["dispatched", "morning"], "trạng thái đơn"),
  ("The courier will call you before delivery", ["courier", "delivery"], "nhân viên giao hàng gọi trước"),
  ("Delivery is free for orders over five hundred thousand dong", ["free", "hundred"], "phí giao hàng"),
  ("Please check the package before you sign", ["package", "sign"], "kiểm tra hàng khi nhận"),
  ("Your package left our warehouse today. Here's your tracking number. It should arrive on Friday afternoon.", ["warehouse", "tracking", "Friday"], "tin nhắn báo gửi hàng"),
  ("I'm sorry, your delivery is delayed because of the storm. The courier will bring it tomorrow morning. You don't need to do anything.", ["delayed", "storm", "tomorrow"], "báo giao hàng trễ"),
 ],
})

# ───────────────────────── 9. Chỉ tiêu, báo cáo & họp sale ─────────────────────────
PHASES.append({
 "title": "Chỉ tiêu, báo cáo & họp sale",
 "vocab": [
  ("target", "/ˈtɑːɡɪt/", "n", "chỉ tiêu, mục tiêu doanh số", "Our monthly <b>target</b> is 500 million dong.", "Chỉ tiêu tháng của nhóm là 500 triệu đồng.", "ノルマ", "noruma"),
  ("revenue", "/ˈrevənjuː/", "n", "doanh thu", "<b>Revenue</b> went up 12% this month.", "Doanh thu tháng này tăng 12%.", "売上", "uriage"),
  ("commission", "/kəˈmɪʃn/", "n", "tiền hoa hồng", "Sales staff get a 3% <b>commission</b> on every order.", "Nhân viên sale được hoa hồng 3% trên mỗi đơn."),
  ("lead", "/liːd/", "n", "khách hàng tiềm năng", "I got ten new <b>leads</b> from the trade fair.", "Em có thêm mười khách tiềm năng từ hội chợ.", "見込み客", "mikomikyaku"),
  ("conversion rate", "/kənˈvɜːʃn ˌreɪt/", "n", "tỷ lệ chốt đơn (chuyển đổi)", "Our <b>conversion rate</b> on calls is about 15%.", "Tỷ lệ chốt đơn qua điện thoại của nhóm khoảng 15%."),
  ("pipeline", "/ˈpaɪplaɪn/", "n", "danh sách cơ hội bán hàng đang theo", "I have five big deals in my <b>pipeline</b>.", "Em đang theo năm cơ hội bán hàng lớn."),
  ("forecast", "/ˈfɔːkɑːst/", "n/v", "dự báo", "Our sales <b>forecast</b> for next month looks good.", "Dự báo doanh số tháng tới khá khả quan.", "予測", "yosoku"),
  ("quarter", "/ˈkwɔːtə/", "n", "quý", "We hit our target in the first <b>quarter</b>.", "Nhóm đã đạt chỉ tiêu trong quý một.", "四半期", "shihanki"),
  ("exceed", "/ɪkˈsiːd/", "v", "vượt (mức)", "Lan <b>exceeded</b> her target by 20%.", "Lan vượt chỉ tiêu 20%."),
  ("KPI", "/ˌkeɪ piː ˈaɪ/", "n", "chỉ số đánh giá hiệu quả (KPI)", "One of our <b>KPIs</b> is the number of calls per day.", "Một trong các KPI của nhóm là số cuộc gọi mỗi ngày."),
 ],
 "phrases": [
  ("Yesterday I closed three deals worth 80 million dong.", "Hôm qua em chốt được ba đơn trị giá 80 triệu đồng."),
  ("I've reached 70% of my monthly target.", "Em đã đạt 70% chỉ tiêu tháng."),
  ("Today I'm going to call 40 leads.", "Hôm nay em sẽ gọi 40 khách tiềm năng."),
  ("We're behind target this month because of the holiday.", "Tháng này nhóm đang chậm chỉ tiêu vì kỳ nghỉ lễ."),
  ("My conversion rate went up from 10 to 14 percent.", "Tỷ lệ chốt đơn của em tăng từ 10 lên 14 phần trăm."),
  ("The main challenge is that customers compare prices online.", "Khó khăn chính là khách hay so giá trên mạng."),
  ("I need more leads from the marketing team.", "Em cần bộ phận marketing hỗ trợ thêm khách tiềm năng."),
  ("Revenue this quarter is 15% higher than last year.", "Doanh thu quý này cao hơn cùng kỳ năm ngoái 15%."),
  ("Congratulations on exceeding your target!", "Chúc mừng bạn đã vượt chỉ tiêu!"),
  ("Let's review the pipeline for next week.", "Mình cùng rà lại các cơ hội bán hàng cho tuần tới nhé."),
 ],
 "dialogues": [
  ("How are your numbers this month?", [
    ("I've reached 80% of my target, and I have two big deals to close next week.", True, "Con số cụ thể + kế hoạch cho phần còn lại."),
    ("My numbers is good.", False, "Sai hòa hợp chủ–vị ('are') và không có số liệu."),
    ("I reach eighty percent already.", False, "Sai thì: 'I've reached 80% already.'"),
  ]),
  ("Why are sales down this week?", [
    ("Mainly because of the holiday. Many customers delayed buying, so I've planned follow-up calls for Monday.", True, "Nêu nguyên nhân + hành động khắc phục."),
    ("Because customers no buy.", False, "Thiếu trợ động từ ('customers didn't buy') và chưa giải thích lý do."),
    ("It's not my fault.", False, "Phòng thủ, không phân tích hay đề xuất giải pháp."),
  ]),
  ("What do you need to hit your target?", [
    ("More good leads. Could marketing send us the contact list from the trade fair?", True, "Nêu nhu cầu rõ + đề xuất cụ thể."),
    ("I need more lead.", False, "Thiếu 's' ('more leads') và quá chung chung."),
    ("Lower target, please.", False, "Chỉ xin giảm chỉ tiêu, không đề xuất giải pháp."),
  ]),
  ("Great job! You exceeded your target by 20%.", [
    ("Thank you! The new bundle offer really helped, and the team supported me a lot.", True, "Cảm ơn + lý do thành công + ghi nhận đồng đội."),
    ("Thank you, I am very excellent.", False, "Tự khen 'excellent' nghe khoe khoang và không tự nhiên."),
    ("Yes. When I get commission?", False, "Sai ngữ pháp ('When will I get…') và chỉ nghĩ tới tiền, không đúng lúc."),
  ]),
  ("Can you share your forecast for next month?", [
    ("Sure. I expect about 400 million, based on the five deals in my pipeline.", True, "Con số dự báo + căn cứ rõ ràng."),
    ("Next month I think many.", False, "Thiếu động từ, không có con số."),
    ("I can't know the future.", False, "Né câu hỏi — dự báo doanh số là việc của sale."),
  ]),
 ],
 "listen": [
  ("I've reached seventy percent of my target", ["reached", "target"], "tiến độ chỉ tiêu"),
  ("Our revenue went up this quarter", ["revenue", "quarter"], "doanh thu quý"),
  ("Today I'm going to call forty new leads", ["forty", "leads"], "kế hoạch gọi khách"),
  ("Congratulations on exceeding your target", ["Congratulations", "exceeding"], "chúc mừng vượt chỉ tiêu"),
  ("Yesterday I closed two deals worth sixty million dong. Today I'm going to visit a new client in District 7. My only challenge is slow delivery from the warehouse.", ["deals", "client", "delivery"], "báo cáo sale đầu ngày"),
  ("Good morning, team. We're at ninety percent of our monthly target. We need two more big orders by Friday.", ["ninety", "monthly", "orders"], "trưởng nhóm mở đầu họp sale"),
 ],
})

# ───────────────────────── Vai trò (roles) ─────────────────────────
ROLES = {
 "retail": {"label": "Bán hàng tại cửa hàng", "emoji": "🛍️",
  "scenarios": [
   ("rt_browse", "Khách vào xem hàng", "You are a foreign customer walking into a home appliance store. At first say you are just looking, then ask about an air purifier for a small bedroom."),
   ("rt_size", "Hỏi size & màu", "You are a customer in a clothing shop. Ask if a jacket comes in another colour and a bigger size, then ask to try it on."),
   ("rt_pay", "Thanh toán tại quầy", "You are a customer at the checkout. Ask if you can pay by foreign card, ask about a membership discount and ask for a VAT invoice."),
   ("rt_return", "Đổi hàng tại cửa hàng", "You are a customer who wants to exchange shoes you bought three days ago because they are too small. You have the receipt."),
  ],
  "dialogues": [
   ("Excuse me, do you have these shoes in size 42?", [
     ("Let me check for you. Please have a seat, I'll be right back.", True, "Nhận kiểm tra + mời khách ngồi chờ — lịch sự."),
     ("Size 42 no have.", False, "Dịch từng chữ 'không có': 'Sorry, we don't have size 42.' — lại chưa kiểm tra kho."),
     ("Your foot too big.", False, "Thiếu động từ và bình luận cơ thể khách — rất bất lịch sự.")]),
   ("Can I try this on?", [
     ("Of course. The fitting room is just over there, on the left.", True, "Đồng ý + chỉ đường rõ ràng."),
     ("Yes, you can try on there.", False, "Thiếu tân ngữ: 'try it on'."),
     ("Try is free.", False, "Dịch từng chữ, nghe kỳ và không chỉ phòng thử.")]),
   ("Is this on sale?", [
     ("Yes, it's 30% off this week, so it's 700,000 dong now.", True, "Xác nhận + mức giảm + giá sau giảm."),
     ("Yes, sale 30.", False, "Thiếu động từ và đơn vị: 'Yes, it's 30% off.'"),
     ("No sale, but it's good.", False, "Trả lời cụt, không đưa thông tin giá hay lợi ích.")]),
   ("Can I get a discount with my membership card?", [
     ("Yes, members get 5% off. Could I scan your card, please?", True, "Xác nhận quyền lợi + xin thẻ lịch sự."),
     ("Yes, give me card.", False, "Mệnh lệnh cộc, thiếu 'your' và 'please'."),
     ("Membership only for VIP.", False, "Thiếu động từ, thông tin mơ hồ, dễ làm khách phật ý.")]),
   ("It's a bit too expensive for me.", [
     ("I understand. This one is similar but 20% cheaper. Would you like to see it?", True, "Đồng cảm + gợi ý lựa chọn vừa túi tiền."),
     ("Cheap one is not good quality.", False, "Thiếu mạo từ và ép khách mua đồ đắt."),
     ("So you don't buy?", False, "Dùng câu khẳng định làm câu hỏi, nghe như trách khách.")]),
   ("Can I pay with a foreign credit card?", [
     ("Yes, we accept all major international cards. Please tap it here.", True, "Trả lời rõ + hướng dẫn thao tác."),
     ("Yes, can pay.", False, "Thiếu chủ ngữ: 'Yes, you can.'"),
     ("Foreign card is problem, pay cash better.", False, "Thiếu mạo từ/động từ và gây bất tiện cho khách không cần thiết.")]),
  ]},
 "cs": {"label": "CSKH · Call center", "emoji": "🎧",
  "scenarios": [
   ("cs_bill", "Thắc mắc hóa đơn", "You are a customer calling because this month's phone bill is 200,000 dong higher than usual. I am the call center agent. Answer my identity questions, then explain the problem."),
   ("cs_angry", "Khách giận dữ", "You are an angry customer. Your internet has been down for two days and you have called twice before. Calm down only if I apologise and give a clear plan."),
   ("cs_transfer", "Chuyển máy & giữ máy", "You are a customer with a technical problem the agent cannot fix. Accept being put on hold, then ask who you will be transferred to and how long it will take."),
   ("cs_followup", "Gọi lại chăm sóc", "You are a customer who had a washing machine repaired last week. I am calling to follow up. Say it works, but mention a small noise and ask what to do."),
  ],
  "dialogues": [
   ("Hello? I'm calling about my account.", [
     ("Thank you for calling. My name is Linh. For security, could I have your full name and date of birth, please?", True, "Chào + giới thiệu + xác minh danh tính lịch sự."),
     ("OK, what is your account?", False, "Chưa chào, chưa xác minh, hỏi mơ hồ."),
     ("Give me your ID number.", False, "Mệnh lệnh cộc lốc, thiếu 'please'.")]),
   ("Why is my bill so high this month?", [
     ("Let me check that for you. May I put you on hold for about one minute?", True, "Nhận kiểm tra + xin phép giữ máy + thời gian."),
     ("Because you use too much.", False, "Kết luận khi chưa kiểm tra, nghe như trách khách."),
     ("I don't know why high.", False, "Sai cấu trúc ('why it's so high') và không có hướng xử lý.")]),
   ("I've called three times and nobody fixed it!", [
     ("I'm very sorry. I'll take care of this personally and call you back by 3 p.m. today.", True, "Xin lỗi + nhận trách nhiệm + hẹn giờ cụ thể."),
     ("Calm down, please.", False, "Bảo khách bình tĩnh khiến họ bực hơn."),
     ("Before is other agent, not me.", False, "Thiếu động từ, đổ lỗi cho đồng nghiệp.")]),
   ("Can I speak to your supervisor?", [
     ("Of course. I'll transfer you now. It may take about two minutes, so please stay on the line.", True, "Đồng ý + báo thời gian + dặn giữ máy."),
     ("Supervisor no time.", False, "Thiếu động từ và từ chối cộc."),
     ("Why? I am not good?", False, "Sai cấu trúc câu hỏi ('Am I not…?') và nghe tự ái.")]),
   ("Sorry, can you speak more slowly?", [
     ("Of course. I said your new plan starts on the first of next month.", True, "Nói chậm lại + nhắc lại ý chính."),
     ("I speak slowly already.", False, "Cãi khách; đúng ra phải nói chậm lại."),
     ("You don't understand English?", False, "Nghe xúc phạm khách — hãy nói chậm và nhắc lại.")]),
   ("No, that's all. Thank you.", [
     ("You're welcome. Thank you for calling, and have a nice day!", True, "Kết thúc cuộc gọi chuẩn, thân thiện."),
     ("OK bye.", False, "Quá cộc cho lời kết cuộc gọi CSKH."),
     ("Please give me five stars.", False, "Xin đánh giá thẳng thừng, thiếu chuyên nghiệp.")]),
  ]},
 "telesales": {"label": "Telesales", "emoji": "📞",
  "scenarios": [
   ("ts_cold", "Gọi khách lần đầu", "You are a busy person receiving my first call about a home internet plan. Ask who I am and how I got your number. Give me thirty seconds to explain."),
   ("ts_busy", "Khách bận, hẹn gọi lại", "You are a customer who is driving when I call. Ask me to call back later and agree on a time."),
   ("ts_objection", "Khách từ chối", "You are a customer I am calling about a health insurance plan. Say it's too expensive and you already have one. Stay polite but hard to convince."),
   ("ts_close", "Chốt đơn qua điện thoại", "You are interested in the product I'm selling by phone. Ask about the price, delivery and how to pay, then agree to order if my answers are clear."),
  ],
  "dialogues": [
   ("Who is this?", [
     ("Hi, this is Nam from Zenta Home. I'm calling about our new air purifier offer. Do you have two minutes?", True, "Giới thiệu tên + công ty + lý do + xin phép thời gian."),
     ("I am Nam. I sell air purifier.", False, "Thiếu 's' và vào thẳng bán hàng, không hỏi khách có rảnh không."),
     ("You don't know me, but listen.", False, "Nghe áp đặt — khách sẽ cúp máy.")]),
   ("I'm not interested.", [
     ("I understand. Can I just ask: do you already use an air purifier at home?", True, "Tôn trọng + một câu hỏi ngắn để giữ cuộc trò chuyện."),
     ("Why you not interested?", False, "Thiếu trợ động từ ('Why aren't you…') và nghe như tra hỏi."),
     ("But it is very cheap, you must buy!", False, "Ép buộc — khách càng từ chối.")]),
   ("I'm driving right now.", [
     ("Sorry to bother you. When would be a good time to call you back?", True, "Xin lỗi + hỏi giờ gọi lại — tôn trọng an toàn của khách."),
     ("It's OK, only one minute.", False, "Không tôn trọng việc khách đang lái xe."),
     ("I call again later.", False, "Thiếu 'will' và không hẹn giờ cụ thể: 'I'll call you back at 5.'")]),
   ("How did you get my number?", [
     ("You signed up on our website last month. If you prefer, I can remove your number from our list.", True, "Giải thích nguồn số + tôn trọng quyền từ chối của khách."),
     ("I have many numbers.", False, "Né câu hỏi, làm khách nghi ngờ."),
     ("Secret.", False, "Cộc và thiếu minh bạch.")]),
   ("How much is it?", [
     ("It's 2.9 million dong, and this month you also get free delivery and installation.", True, "Báo giá + ưu đãi kèm theo."),
     ("It 2.9 million.", False, "Thiếu động từ 'is'."),
     ("Very cheap, you will love it.", False, "Né giá cụ thể — khách sẽ mất tin tưởng.")]),
   ("OK, I'll order one.", [
     ("Great! Let me confirm your name and delivery address, and I'll text you an order confirmation.", True, "Vui mừng + xác nhận thông tin + bước tiếp theo."),
     ("OK. You give address.", False, "Mệnh lệnh cộc; nên nói 'Could I have your address, please?'"),
     ("Why only one? Buy two is cheaper.", False, "Khách vừa đồng ý đã ép thêm — dễ đổi ý; sai ngữ pháp ('Buying two is cheaper').")]),
  ]},
 "b2b": {"label": "Sale B2B · Account", "emoji": "🤝",
  "scenarios": [
   ("bb_meet", "Gặp khách doanh nghiệp", "You are the purchasing manager of a foreign-owned factory. I am an account manager visiting you. Ask about our products, minimum order and delivery times."),
   ("bb_quote", "Thương lượng báo giá", "You received my quotation for 500 office chairs. Say the price is 10% higher than another supplier and ask for better payment terms."),
   ("bb_issue", "Xử lý sự cố với khách lớn", "You are a key customer. Our last delivery was one week late and your work was delayed. Ask what happened and what we will do to prevent it."),
   ("bb_renew", "Gia hạn hợp đồng năm", "You are a long-term customer. Your yearly contract ends next month. Ask about new prices and what extra service we can offer."),
  ],
  "dialogues": [
   ("What's your minimum order?", [
     ("Our minimum order is 100 units, but for a first trial order we can accept 50.", True, "Thông tin rõ + linh hoạt để mở cơ hội hợp tác."),
     ("Minimum is many.", False, "Mơ hồ, không có con số."),
     ("You must order 100, no less.", False, "Cứng nhắc, dễ mất khách mới.")]),
   ("Your price is higher than your competitor's.", [
     ("I understand. Our price includes a two-year warranty and on-site support, which saves you money in the long run.", True, "Công nhận + chứng minh giá trị tổng thể."),
     ("Their quality is bad.", False, "Chê đối thủ thiếu căn cứ — không chuyên nghiệp."),
     ("OK, I reduce 20%.", False, "Thiếu 'will' và giảm giá ngay, quá nhiều, không thương lượng.")]),
   ("Can we pay 60 days after delivery?", [
     ("Our standard terms are 30 days, but let me check with my manager and get back to you tomorrow.", True, "Nêu điều khoản chuẩn + không hứa bừa + hẹn thời gian."),
     ("Yes, no problem, 90 days also OK.", False, "Hứa vượt quyền hạn khi chưa hỏi cấp trên."),
     ("60 days is too long, cannot.", False, "Thiếu chủ ngữ và từ chối cứng nhắc.")]),
   ("The last delivery was a week late.", [
     ("I'm very sorry. There was a problem with our supplier. We've changed our process, and I'll update you on every order from now on.", True, "Xin lỗi + nguyên nhân + biện pháp phòng ngừa."),
     ("Delivery late is normal in rainy season.", False, "Coi chậm trễ là bình thường — khách lớn sẽ không chấp nhận."),
     ("Sorry, is not my department.", False, "Thiếu chủ ngữ 'it' và né trách nhiệm của người quản lý khách hàng.")]),
   ("Could you send me a formal quotation?", [
     ("Certainly. I'll email it to you by Wednesday, with prices, delivery times and payment terms.", True, "Đồng ý + thời hạn + nội dung báo giá rõ ràng."),
     ("OK, I send later.", False, "Thiếu 'will', thiếu tân ngữ và không có thời hạn."),
     ("Price same as I said, no need.", False, "Bỏ qua yêu cầu chính thức của khách doanh nghiệp.")]),
   ("We're happy to sign the contract.", [
     ("That's great news! I'll send the contract today, and I'll be your main contact for every order.", True, "Vui mừng + bước tiếp theo + cam kết chăm sóc lâu dài."),
     ("Finally! Sign quickly please.", False, "Nghe sốt ruột, thiếu chuyên nghiệp."),
     ("OK thank.", False, "Cộc, thiếu 's', không nói bước tiếp theo.")]),
  ]},
}

# ───────────────────────── Gói ─────────────────────────
PACK = {
 "id": "sales",
 "label": "Bán hàng · CSKH",
 "short": "Bán hàng",
 "emoji": "🎧",
 "desc": "Sale · chăm sóc khách hàng · call center",
 "persona": "a Vietnamese sales and customer service worker",
 "counterpart": "a customer",
 "context": "sales and customer service",
 "core": [3, 11],
 "report": {
  "title": "Báo cáo sale 60 giây", "short": "Báo cáo 60s", "sub": "Nói như họp sale đầu ngày 🎙️",
  "steps": [["Results", "Yesterday I closed …"], ["Today", "Today I'm going to call …"], ["Challenges", "No big challenges. / I need help with …"]],
  "kind": "daily sales update",
  "structure": "yesterday's results / today's plan / challenges",
  "sample": "Yesterday I closed three orders worth 45 million dong, so I'm at 70% of my monthly target. Today I'm going to call 30 leads from the trade fair and send two quotations. My main challenge is that one big customer wants a bigger discount.",
 },
 "podcast": "Podcast bán hàng",
 "game_tag": "Game anime: đánh quái lời từ chối, hạ boss khách khó tính",
 "reverse_tag": "kiểu bán hàng",
 "jd_placeholder": "VD: CSKH call center cho khách Mỹ/Úc, xác minh tài khoản, xử lý khiếu nại, đổi trả, hoàn tiền…",
 "rw_placeholder": "VD: khách gọi lần thứ ba vì đơn giao trễ, đòi hoàn tiền",
 "quips": [
  "How can I help you today?",
  "Thank you for holding!",
  "Deal closed!",
  "Target smashed!",
  "Let me check that for you…",
  "Your call is important to us!",
  "Refund processed!",
  "One more call before lunch!",
  "Objection handled!",
  "The customer is always… interesting!",
 ],
 "ai": [
  ("walkin", "Tư vấn khách tại cửa hàng", "You are a foreign customer in an electronics shop looking for a new laptop. I am the sales assistant. Answer my questions about your needs and price range, and ask about the warranty."),
  ("needs", "Tìm hiểu nhu cầu", "You are a small business owner who needs new office chairs. I am a sales representative. Give details about your needs only when I ask good questions."),
  ("price", "Mặc cả & xin giảm giá", "You are a customer who likes the product but thinks the price is too high. Ask me for a discount twice and mention a cheaper competitor."),
  ("objection", "Xử lý từ chối", "You are a busy customer receiving my telesales call about an internet plan. Say you are not interested, then say you need to think about it. Agree to hear more only if I handle your objections politely."),
  ("verify", "Gọi tổng đài CSKH", "You are a customer calling the call center because your bill is higher than usual. I am the agent. Wait for me to verify your identity, then explain the problem. Accept being put on hold once."),
  ("angry", "Khách khiếu nại gay gắt", "You are an angry customer. Your washing machine was delivered damaged and this is your second call. Be upset at first, and calm down if I apologise sincerely and offer a clear solution."),
  ("chat", "Hỗ trợ qua chat", "You are a customer using the live chat of an online shop. Your order is five days late. Write short, informal messages and ask for a tracking update and a discount."),
  ("report", "Báo cáo với trưởng nhóm sale", "You are my sales manager. Ask me for a quick update: my results yesterday, my plan for today and any challenges. Ask one follow-up question about my numbers."),
 ],
 "rev": [
  ("Anh/chị cần em giúp gì ạ?", "How can I help you?"),
  ("Mẫu này đang bán chạy nhất.", "This model is our best-seller."),
  ("Anh/chị muốn thanh toán bằng thẻ hay tiền mặt?", "Would you like to pay by card or cash?"),
  ("Em xin phép giữ máy một chút nhé.", "May I put you on hold for a moment?"),
  ("Giá này có hiệu lực đến thứ Sáu.", "This price is valid until Friday."),
  ("Em sẽ chuyển máy sang bộ phận kỹ thuật.", "I'll transfer you to the technical team."),
  ("Em xin lỗi vì sự bất tiện này.", "I'm sorry for the inconvenience."),
  ("Anh/chị có mang theo hóa đơn không ạ?", "Do you have the receipt with you?"),
  ("Đơn hàng sẽ đến vào thứ Năm.", "Your order will arrive on Thursday."),
  ("Em đã đạt tám mươi phần trăm chỉ tiêu.", "I've reached 80% of my target."),
  ("Em sẽ gửi báo giá trước 5 giờ chiều.", "I'll send the quotation before 5 p.m."),
  ("Anh/chị muốn đổi hàng hay hoàn tiền?", "Would you prefer an exchange or a refund?"),
  ("Màu này đang hết hàng.", "This colour is out of stock."),
  ("Anh/chị cứ thong thả suy nghĩ thêm.", "Take your time to think it over."),
 ],
 "reading": [
  {"t": "Sale flyer", "text": "MID-YEAR SALE at Zenta Home\n- 20% off all air purifiers\n- Buy any blender, get a free juice cup\n- 0% instalments for 6 months on orders over 5 million dong\nOffer valid from June 15 to June 30. Cannot be used with other vouchers.", "q": [
    {"q": "How long can you pay in 0% instalments?", "o": ["3 months", "6 months", "12 months"], "a": 1},
    {"q": "Can you use this offer with another voucher?", "o": ["Yes, always", "Only online", "No"], "a": 2}]},
  {"t": "Customer email", "text": "Subject: Wrong item delivered (Order #58213)\nHello,\nI ordered a black office chair on May 3, but I received a grey one today. I need the black one for a new employee who starts on Monday. Please tell me how to exchange it.\nThanks,\nDaniel Moore", "q": [
    {"q": "What is the problem?", "o": ["The chair is broken", "He received the wrong colour", "The delivery was late"], "a": 1},
    {"q": "Why is Daniel in a hurry?", "o": ["A new employee starts on Monday", "He is moving office", "The price will go up"], "a": 0}]},
  {"t": "Call script", "text": "CALL SCRIPT – BILLING QUESTIONS\n1. Greet the customer and give your name.\n2. Verify identity: full name + date of birth + last 4 digits of the phone number.\n3. Listen, then repeat the problem back to the customer.\n4. Always ask before putting the customer on hold (max. 2 minutes).\n5. Refunds over 1 million dong: escalate to a supervisor.", "q": [
    {"q": "What must the agent do before putting a customer on hold?", "o": ["Ask the customer first", "Transfer the call", "Give a refund"], "a": 0},
    {"q": "Who handles refunds over 1 million dong?", "o": ["The agent", "The billing team", "A supervisor"], "a": 2}]},
  {"t": "Delivery text message", "text": "Zenta Shop: Your order #77410 has been dispatched. Tracking number: VN2048315. Delivery: Thu 12 Sep, 9 a.m.–12 p.m. Payment: cash on delivery, 1,250,000 VND. Reply 1 to change the delivery time.", "q": [
    {"q": "How will the customer pay?", "o": ["By card online", "In cash to the courier", "By bank transfer"], "a": 1},
    {"q": "What should the customer do to change the time?", "o": ["Call the shop", "Reply 1", "Visit the warehouse"], "a": 1}]},
  {"t": "Sales team chat", "text": "Tuấn (Team Lead): Great week, team! We're at 92% of the monthly target with one week to go. Lan exceeded her personal target by 15% — well done! Reminder: send me your forecast for next week by Friday 4 p.m. The sales meeting moves to Monday at 9 a.m.", "q": [
    {"q": "How much of the monthly target has the team reached?", "o": ["85%", "92%", "115%"], "a": 1},
    {"q": "When is the sales meeting now?", "o": ["Friday at 4 p.m.", "Monday at 9 a.m.", "Monday at 4 p.m."], "a": 1}]},
 ],
 "events": [
  ("fair", "Hội chợ triển lãm", "You are a foreign business visitor at our booth at a trade fair. Ask what our company sells, the prices for large orders and delivery times."),
  ("pitch", "Gặp khách B2B lần đầu", "You are the purchasing manager of a foreign company meeting me for the first time. Ask about our products, prices, payment terms and why you should choose us."),
  ("renewal", "Gia hạn hợp đồng", "You are an existing business customer whose contract ends next month. You are thinking of moving to a cheaper competitor. Ask me for a better deal."),
  ("qa", "Chấm điểm cuộc gọi (QA)", "You are a quality supervisor at a call center. Role-play a customer call with me, then give me short feedback on my greeting, identity check and closing."),
  ("review", "Họp đánh giá doanh số", "You are my sales director at the monthly review. Ask about my results against target, my best deal and my plan for next month."),
  ("sale", "Đợt khuyến mãi lớn", "You are a customer shopping during a big holiday sale. Ask about discounts, vouchers, instalments and the return policy."),
  ("other", "Khác", ""),
 ],
 "roles": ROLES,
 "phases": PHASES,
}
