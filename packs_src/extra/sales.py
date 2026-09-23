# -*- coding: utf-8 -*-
# v4.1 — nội dung làm giàu cho gói sales (nối vào cuối gói, xem build.py)
EXTRA = {
 "phases": [
  # ───────────── 1. Bán hàng B2B & gặp khách doanh nghiệp ─────────────
  {"title": "Bán hàng B2B & gặp khách doanh nghiệp",
   "vocab": [
    ("decision-maker", "/dɪˈsɪʒn ˌmeɪkə/", "n", "người ra quyết định", "Who is the final <b>decision-maker</b> for this purchase?", "Ai là người quyết định cuối cùng cho lần mua này ạ?", "決裁者", "kessaisha"),
    ("procurement", "/prəˈkjʊəmənt/", "n", "việc thu mua; phòng thu mua", "Please send the quotation to our <b>procurement</b> team.", "Anh/chị gửi báo giá cho phòng thu mua bên tôi nhé.", "調達", "chōtatsu"),
    ("supplier", "/səˈplaɪə/", "n", "nhà cung cấp", "We have been their main <b>supplier</b> for three years.", "Bên em là nhà cung cấp chính của họ ba năm nay.", "仕入先", "shiiresaki"),
    ("stakeholder", "/ˈsteɪkhəʊldə/", "n", "bên liên quan", "The IT manager is also a key <b>stakeholder</b> in this project.", "Trưởng phòng IT cũng là một bên liên quan quan trọng trong dự án này.", "関係者", "kankeisha"),
    ("business card", "/ˈbɪznəs ˌkɑːd/", "n", "danh thiếp", "Here's my <b>business card</b>. My mobile number is on the back.", "Đây là danh thiếp của em. Số di động ở mặt sau ạ.", "名刺", "meishi"),
    ("bulk order", "/ˌbʌlk ˈɔːdə/", "n", "đơn hàng số lượng lớn", "We give better prices for <b>bulk orders</b>.", "Bên em có giá tốt hơn cho đơn số lượng lớn."),
    ("headquarters", "/ˌhedˈkwɔːtəz/", "n", "trụ sở chính", "Their <b>headquarters</b> is in Singapore, but the factory is in Bình Dương.", "Trụ sở chính của họ ở Singapore, còn nhà máy ở Bình Dương.", "本社", "honsha"),
    ("partnership", "/ˈpɑːtnəʃɪp/", "n", "sự hợp tác, quan hệ đối tác", "We hope this is the start of a long <b>partnership</b>.", "Bên em mong đây là khởi đầu của một sự hợp tác lâu dài."),
    ("budget", "/ˈbʌdʒɪt/", "n", "ngân sách", "What's your <b>budget</b> for new equipment this year?", "Ngân sách mua thiết bị mới năm nay của bên anh/chị là bao nhiêu ạ?", "予算", "yosan"),
    ("account manager", "/əˈkaʊnt ˌmænɪdʒə/", "n", "nhân viên phụ trách khách hàng", "I'm your <b>account manager</b>, so please call me about any order.", "Em là người phụ trách khách hàng của anh/chị, có đơn nào cứ gọi em nhé."),
   ],
   "phrases": [
    ("Thank you for meeting with us today.", "Cảm ơn anh/chị đã dành thời gian gặp bên em hôm nay."),
    ("Let me briefly introduce our company.", "Cho phép em giới thiệu ngắn gọn về công ty bên em."),
    ("We supply office furniture to over 200 companies in Vietnam.", "Bên em cung cấp nội thất văn phòng cho hơn 200 công ty ở Việt Nam."),
    ("Could you tell me a little about your current supplier?", "Anh/chị có thể chia sẻ một chút về nhà cung cấp hiện tại không ạ?"),
    ("Who else will be involved in the decision?", "Còn ai khác tham gia vào quyết định này không ạ?"),
    ("What's your timeline for this project?", "Tiến độ dự kiến của dự án này thế nào ạ?"),
    ("Do you have a budget in mind?", "Bên anh/chị đã có ngân sách dự kiến chưa ạ?"),
    ("I'll send you a proposal by the end of the week.", "Cuối tuần này em sẽ gửi đề xuất cho anh/chị."),
    ("Would it be possible to visit your factory next month?", "Tháng sau bên em đến thăm nhà máy của anh/chị được không ạ?"),
    ("It was a pleasure meeting you.", "Rất vui được gặp anh/chị."),
   ],
   "dialogues": [
    ("Nice to meet you. So, tell me about your company.", [
      ("Nice to meet you too. We're an office furniture supplier, and we work with over 200 companies in Vietnam.", True, "Chào lại + giới thiệu ngắn gọn, có con số cụ thể."),
      ("Our company very big and very good.", False, "Thiếu động từ 'is' và chỉ khen chung chung, không có thông tin."),
      ("You can read on our website.", False, "Đẩy khách tự tìm hiểu — bỏ lỡ cơ hội giới thiệu trực tiếp."),
    ]),
    ("I'm not the one who makes the final decision.", [
      ("I understand. Who else should I talk to? Could we set up a meeting with them?", True, "Hỏi ra người quyết định + đề xuất bước tiếp theo."),
      ("So why you meet me?", False, "Sai ngữ pháp ('Why are you meeting me?') và nghe thô lỗ."),
      ("OK, no problem. Bye.", False, "Bỏ cuộc quá sớm — nên hỏi ai là người quyết định."),
    ]),
    ("We're happy with our current supplier.", [
      ("That's good to hear. May I ask what you like most about them? We might be able to offer something extra.", True, "Tôn trọng + hỏi để tìm điểm mình có thể khác biệt."),
      ("Your supplier is not good like us.", False, "Sai so sánh ('not as good as us') và chê đối thủ."),
      ("Why you happy?", False, "Thiếu động từ 'are' ('Why are you happy with them?') và nghe như tra hỏi."),
    ]),
    ("Can you handle a bulk order of 2,000 units?", [
      ("Yes, we can. For 2,000 units, we need about four weeks for production and delivery.", True, "Khẳng định + nêu thời gian cụ thể để khách lên kế hoạch."),
      ("Yes, no problem, tomorrow is OK.", False, "Hứa không thực tế — khách lớn sẽ mất tin khi trễ hẹn."),
      ("2,000 is very many.", False, "'very many' không tự nhiên (nói 'That's a lot') và không trả lời làm được hay không."),
    ]),
    ("Could you send us some information after the meeting?", [
      ("Of course. I'll email you our catalogue and a short proposal by Friday.", True, "Đồng ý + nói rõ gửi gì, trước khi nào."),
      ("OK, I send you.", False, "Thiếu 'will' và tân ngữ, không nói gửi gì, khi nào."),
      ("All information is in the brochure I gave.", False, "Từ chối gửi thêm — khách doanh nghiệp cần tài liệu để trình cấp trên."),
    ]),
   ],
   "listen": [
    ("Here's my business card with my mobile number", ["business", "mobile"], "đưa danh thiếp"),
    ("Who is the final decision-maker for this project", ["final", "decision-maker"], "hỏi người ra quyết định"),
    ("Our headquarters is in Hanoi, near the city centre", ["headquarters", "centre"], "trụ sở công ty"),
    ("What is your budget for new furniture this year", ["budget", "furniture"], "hỏi ngân sách"),
    ("Thank you for your time today. We supply chairs and desks to over two hundred offices. Could we visit your new building next week?", ["supply", "offices", "building"], "giới thiệu công ty với khách doanh nghiệp"),
    ("I'm the account manager for your company. If you have any questions about orders, please call me directly. I'll visit your office once a month.", ["account", "directly", "month"], "giới thiệu người phụ trách khách hàng"),
   ]},

  # ───────────── 2. Demo sản phẩm ─────────────
  {"title": "Demo sản phẩm",
   "vocab": [
    ("walk through", "/ˌwɔːk ˈθruː/", "phr v", "hướng dẫn lần lượt từng phần", "Let me <b>walk</b> you <b>through</b> the main screen.", "Để em hướng dẫn anh/chị lần lượt màn hình chính."),
    ("dashboard", "/ˈdæʃbɔːd/", "n", "màn hình tổng quan", "The <b>dashboard</b> shows today's sales at a glance.", "Màn hình tổng quan cho anh/chị xem nhanh doanh số hôm nay.", "ダッシュボード", "dasshubōdo"),
    ("customise", "/ˈkʌstəmaɪz/", "v", "tùy chỉnh", "You can <b>customise</b> the report for each branch.", "Anh/chị có thể tùy chỉnh báo cáo cho từng chi nhánh.", "カスタマイズする", "kasutamaizu suru"),
    ("user-friendly", "/ˌjuːzə ˈfrendli/", "adj", "dễ dùng", "The app is very <b>user-friendly</b>, so staff learn it in one day.", "Ứng dụng rất dễ dùng nên nhân viên học một ngày là quen."),
    ("integrate", "/ˈɪntɪɡreɪt/", "v", "tích hợp, kết nối (với hệ thống khác)", "It can <b>integrate</b> with your accounting software.", "Nó có thể kết nối với phần mềm kế toán của anh/chị."),
    ("compatible", "/kəmˈpætəbl/", "adj", "tương thích", "Is it <b>compatible</b> with our old printers?", "Nó có tương thích với máy in cũ bên tôi không?"),
    ("use case", "/ˈjuːs ˌkeɪs/", "n", "tình huống sử dụng thực tế", "Let's look at a real <b>use case</b> from a retail chain.", "Mình cùng xem một tình huống sử dụng thực tế của một chuỗi bán lẻ nhé."),
    ("pain point", "/ˈpeɪn ˌpɔɪnt/", "n", "vấn đề làm khách khổ sở nhất", "Their biggest <b>pain point</b> is slow stock checking.", "Vấn đề lớn nhất của họ là kiểm kho quá chậm."),
    ("highlight", "/ˈhaɪlaɪt/", "v", "nhấn mạnh, làm nổi bật", "I'd like to <b>highlight</b> three key features today.", "Hôm nay em muốn nhấn mạnh ba tính năng chính."),
    ("case study", "/ˈkeɪs ˌstʌdi/", "n", "câu chuyện khách hàng điển hình", "This <b>case study</b> shows how a hotel saved 20% on electricity.", "Câu chuyện khách hàng này cho thấy một khách sạn đã tiết kiệm 20% tiền điện thế nào."),
   ],
   "phrases": [
    ("Thanks for joining the demo today.", "Cảm ơn anh/chị đã tham gia buổi demo hôm nay."),
    ("Before we start, what would you like to see most?", "Trước khi bắt đầu, anh/chị muốn xem phần nào nhất ạ?"),
    ("Can everyone see my screen?", "Mọi người có thấy màn hình của em không ạ?"),
    ("Let me show you how it works with a real example.", "Để em cho anh/chị xem cách hoạt động qua một ví dụ thực tế."),
    ("This part solves the problem you mentioned earlier.", "Phần này giải quyết đúng vấn đề anh/chị nhắc lúc nãy."),
    ("Feel free to stop me if you have any questions.", "Có câu hỏi gì anh/chị cứ ngắt lời em nhé."),
    ("Would you like to try it yourself?", "Anh/chị có muốn tự thử không ạ?"),
    ("That's a great question. Let me show you.", "Câu hỏi rất hay ạ. Để em cho anh/chị xem."),
    ("I'm not sure about that, but I'll check with our technical team.", "Phần đó em chưa chắc, em sẽ hỏi lại đội kỹ thuật ạ."),
    ("So, to sum up, it saves your team about two hours a day.", "Tóm lại, nó giúp đội của anh/chị tiết kiệm khoảng hai giờ mỗi ngày."),
   ],
   "dialogues": [
    ("Can you show me how to create a report?", [
      ("Sure. Just click 'Reports', choose the dates and press 'Create'. It takes about ten seconds.", True, "Hướng dẫn từng bước ngắn gọn + thời gian cụ thể."),
      ("Very easy, you click and finish.", False, "Không hướng dẫn cụ thể; 'click and finish' là dịch từng chữ."),
      ("Report is in the user guide, page 20.", False, "Đang demo mà đẩy khách đi đọc tài liệu — hãy làm mẫu trực tiếp."),
    ]),
    ("Is it compatible with our current system?", [
      ("It works with most systems. Which software are you using now? I'll check for you.", True, "Trả lời trung thực + hỏi thêm để kiểm tra chính xác."),
      ("Yes, 100% compatible with everything.", False, "Hứa tuyệt đối khi chưa biết hệ thống của khách — dễ mất uy tín."),
      ("I think can, maybe.", False, "Thiếu chủ ngữ ('I think it can') và quá mơ hồ."),
    ]),
    ("Sorry, your screen is frozen.", [
      ("Sorry about that. Let me share my screen again. It'll just take a moment.", True, "Xin lỗi nhẹ nhàng + xử lý ngay, giữ bình tĩnh."),
      ("Your internet is slow.", False, "Đổ lỗi cho khách khi chưa kiểm tra."),
      ("Wait, wait, I am fix.", False, "Sai thì: 'I'm fixing it.' — lại nghe hoảng loạn."),
    ]),
    ("This looks nice, but will my staff find it difficult?", [
      ("Not at all. It's very user-friendly, and we offer free training for your team.", True, "Trấn an + nêu lợi ích cụ thể (đào tạo miễn phí)."),
      ("Your staff must learn.", False, "Nghe áp đặt, không giải quyết băn khoăn."),
      ("No difficult, very easy.", False, "Sai từ loại ('It isn't difficult') và không đưa bằng chứng."),
    ]),
    ("Can you customise it for our shops?", [
      ("Yes, we can. Could you tell me a bit more about how your shops work? Then I can show you the right settings.", True, "Đồng ý + hỏi thêm nhu cầu trước khi demo phần tùy chỉnh."),
      ("Yes, customise everything, no problem.", False, "Thiếu chủ ngữ và hứa quá mức."),
      ("Customise is more money.", False, "Sai từ loại ('Customisation costs extra') và nói chuyện tiền khi chưa hiểu nhu cầu."),
    ]),
   ],
   "listen": [
    ("Can everyone see my screen now", ["everyone", "screen"], "kiểm tra chia sẻ màn hình"),
    ("The dashboard shows all your sales in one place", ["dashboard", "place"], "giới thiệu màn hình tổng quan"),
    ("You can customise the report for each shop", ["customise", "shop"], "tùy chỉnh báo cáo"),
    ("Feel free to stop me if you have questions", ["stop", "questions"], "mời khách đặt câu hỏi"),
    ("Let me walk you through the main features. First, this is the dashboard. Here you can see today's orders and stock levels.", ["features", "orders", "stock"], "mở đầu buổi demo"),
    ("You mentioned that stock checking takes too long. With this app, your staff can scan each item with a phone. It saves about two hours a day.", ["mentioned", "scan", "hours"], "demo đúng vấn đề của khách"),
   ]},

  # ───────────── 3. Đàm phán hợp đồng & điều khoản ─────────────
  {"title": "Đàm phán hợp đồng & điều khoản",
   "vocab": [
    ("negotiate", "/nɪˈɡəʊʃieɪt/", "v", "đàm phán, thương lượng", "We need to <b>negotiate</b> the price before we sign.", "Mình cần thương lượng giá trước khi ký.", "交渉する", "kōshō suru"),
    ("payment terms", "/ˈpeɪmənt ˌtɜːmz/", "n", "điều khoản thanh toán", "Our standard <b>payment terms</b> are 30 days after delivery.", "Điều khoản thanh toán chuẩn của bên em là 30 ngày sau khi giao hàng.", "支払条件", "shiharai jōken"),
    ("clause", "/klɔːz/", "n", "điều khoản (trong hợp đồng)", "Please check the delivery <b>clause</b> on page four.", "Anh/chị xem giúp điều khoản giao hàng ở trang bốn nhé.", "条項", "jōkō"),
    ("draft", "/drɑːft/", "n", "bản nháp, bản dự thảo", "I'll send you the first <b>draft</b> of the contract today.", "Hôm nay em sẽ gửi anh/chị bản dự thảo đầu tiên của hợp đồng."),
    ("concession", "/kənˈseʃn/", "n", "sự nhượng bộ", "We can make a small <b>concession</b> on price if you order more.", "Bên em có thể nhượng bộ chút về giá nếu anh/chị đặt nhiều hơn."),
    ("counteroffer", "/ˈkaʊntərˌɒfə/", "n", "đề nghị ngược lại, trả giá lại", "The client made a <b>counteroffer</b> of 8% off.", "Khách đưa ra đề nghị ngược lại là giảm 8%."),
    ("volume discount", "/ˈvɒljuːm ˌdɪskaʊnt/", "n", "chiết khấu theo số lượng", "Orders over 1,000 units get a 7% <b>volume discount</b>.", "Đơn trên 1.000 cái được chiết khấu số lượng 7%."),
    ("lead time", "/ˈliːd ˌtaɪm/", "n", "thời gian từ lúc đặt đến lúc giao", "The <b>lead time</b> for custom orders is six weeks.", "Đơn đặt làm riêng cần sáu tuần từ lúc đặt đến lúc giao.", "リードタイム", "rīdotaimu"),
    ("penalty", "/ˈpenəlti/", "n", "tiền phạt (vi phạm hợp đồng)", "There's a <b>penalty</b> of 1% for each day of late delivery.", "Mỗi ngày giao trễ bị phạt 1%.", "違約金", "iyakukin"),
    ("win-win", "/ˌwɪn ˈwɪn/", "adj", "đôi bên cùng có lợi", "Let's find a <b>win-win</b> solution for both companies.", "Mình cùng tìm giải pháp đôi bên cùng có lợi cho hai công ty nhé."),
   ],
   "phrases": [
    ("I'm sure we can find a solution that works for both of us.", "Em tin mình sẽ tìm được giải pháp phù hợp cho cả hai bên."),
    ("If you order 1,000 units, we can offer 5% off.", "Nếu anh/chị đặt 1.000 cái, bên em có thể giảm 5%."),
    ("That's a bit lower than we expected.", "Mức đó thấp hơn bên em dự kiến một chút."),
    ("What if we offered free delivery instead?", "Nếu bên em miễn phí vận chuyển thay vào đó thì sao ạ?"),
    ("I need to check this with my manager first.", "Việc này em cần hỏi ý quản lý trước ạ."),
    ("Could we move the delivery date to the 20th?", "Mình dời ngày giao sang ngày 20 được không ạ?"),
    ("Our standard payment terms are 30 days.", "Điều khoản thanh toán chuẩn bên em là 30 ngày."),
    ("Let me summarise what we've agreed so far.", "Để em tóm tắt những gì mình đã thống nhất đến giờ."),
    ("I'll update the draft and send it to you tonight.", "Em sẽ sửa bản dự thảo và gửi anh/chị tối nay."),
    ("Please let me know if you'd like to change anything.", "Anh/chị muốn sửa gì thì báo em nhé."),
   ],
   "dialogues": [
    ("Your price is too high. Can you do 15% off?", [
      ("15% is difficult for us. But if you sign a one-year contract, we can offer 8%.", True, "Không từ chối thẳng + đưa đề nghị ngược lại có điều kiện."),
      ("OK, 15% no problem.", False, "Chấp nhận ngay khi chưa thương lượng — mất lợi nhuận, có thể vượt quyền."),
      ("Cannot. Price is fixed.", False, "Thiếu chủ ngữ, từ chối cứng nhắc làm đàm phán bế tắc."),
    ]),
    ("We'd like 60-day payment terms.", [
      ("I understand. Our standard is 30 days, but let me discuss 45 days with my finance team.", True, "Ghi nhận + nêu chuẩn + mở phương án trung gian, không hứa bừa."),
      ("60 days too long for us.", False, "Thiếu động từ 'is' và không đưa phương án khác."),
      ("Yes, 60 days, and 90 days also OK.", False, "Tự hứa vượt quyền khi chưa hỏi bộ phận tài chính."),
    ]),
    ("What happens if your delivery is late?", [
      ("There's a penalty clause in the contract: 1% for each day of delay, up to 10%.", True, "Trả lời thẳng bằng điều khoản cụ thể — tạo niềm tin."),
      ("Don't worry, we are never late.", False, "Hứa suông, né câu hỏi về điều khoản."),
      ("If late, we say sorry.", False, "Thiếu chủ ngữ ('If we're late…') và không chuyên nghiệp — khách cần điều khoản rõ."),
    ]),
    ("Can you give us free delivery as well?", [
      ("We can include free delivery if the order is over 500 million dong.", True, "Nhượng bộ có điều kiện — đúng kỹ thuật đàm phán."),
      ("Free delivery? You want everything free.", False, "Mỉa mai khách — làm hỏng không khí đàm phán."),
      ("Delivery free is not possible.", False, "Sai trật tự ('Free delivery isn't possible') và từ chối không lý do."),
    ]),
    ("I think we have a deal.", [
      ("Great! Let me summarise the main points, and I'll send you the updated contract tomorrow.", True, "Tóm tắt thỏa thuận + bước tiếp theo rõ ràng."),
      ("Yes! Finally we finish.", False, "Nghe như đàm phán là cực hình — thiếu chuyên nghiệp."),
      ("OK, you sign now, today.", False, "Ép ký ngay, bỏ bước xác nhận lại điều khoản."),
    ]),
   ],
   "listen": [
    ("Our standard payment terms are thirty days", ["payment", "thirty"], "điều khoản thanh toán"),
    ("The lead time for this order is six weeks", ["lead", "six"], "thời gian giao hàng"),
    ("I need to check this with my manager first", ["check", "manager"], "xin hỏi ý cấp trên"),
    ("Let's find a solution that works for both of us", ["solution", "both"], "tìm giải pháp chung"),
    ("We can't offer fifteen percent. But if you sign a two-year contract, we can give you eight percent off. We can also include free delivery.", ["fifteen", "two-year", "delivery"], "đưa đề nghị ngược lại"),
    ("Let me summarise what we agreed. The price is one hundred dollars per unit, and payment is within forty-five days. I'll send the updated draft tonight.", ["summarise", "forty-five", "draft"], "tóm tắt thỏa thuận"),
   ]},

  # ───────────── 4. Bán thêm & bán chéo ─────────────
  {"title": "Bán thêm & bán chéo",
   "vocab": [
    ("upsell", "/ˈʌpsel/", "v", "mời khách lên bản/gói cao hơn", "Only <b>upsell</b> the larger model if it fits the customer's needs.", "Chỉ mời khách lên mẫu lớn hơn khi nó hợp nhu cầu của họ.", "アップセル", "appuseru"),
    ("cross-sell", "/ˌkrɒs ˈsel/", "v", "bán chéo, gợi ý sản phẩm đi kèm", "We <b>cross-sell</b> printer paper with every printer.", "Bên em bán kèm giấy in với mỗi máy in.", "クロスセル", "kurosuseru"),
    ("accessory", "/əkˈsesəri/", "n", "phụ kiện", "Would you like a case or any other <b>accessories</b>?", "Anh/chị có muốn lấy thêm ốp lưng hay phụ kiện nào khác không ạ?"),
    ("add-on", "/ˈæd ɒn/", "n", "tiện ích/dịch vụ mua thêm", "Extra cloud storage is a popular <b>add-on</b>.", "Thêm dung lượng lưu trữ đám mây là tiện ích mua thêm được nhiều khách chọn."),
    ("premium", "/ˈpriːmiəm/", "adj", "cao cấp", "The <b>premium</b> plan includes 24/7 support.", "Gói cao cấp có hỗ trợ 24/7."),
    ("complement", "/ˈkɒmplɪment/", "v", "bổ sung, đi kèm rất hợp", "This bag <b>complements</b> the laptop perfectly.", "Chiếc túi này đi kèm với laptop rất hợp."),
    ("average order value", "/ˌævərɪdʒ ˈɔːdə ˌvæljuː/", "n", "giá trị đơn hàng trung bình", "Our <b>average order value</b> went up by 10% this month.", "Giá trị đơn hàng trung bình tháng này tăng 10%."),
    ("tier", "/tɪə/", "n", "hạng, cấp (gói dịch vụ)", "There are three <b>tiers</b>: Basic, Plus and Pro.", "Có ba hạng gói: Basic, Plus và Pro."),
    ("matching", "/ˈmætʃɪŋ/", "adj", "cùng bộ, đồng bộ", "We also have a <b>matching</b> chair for this desk.", "Bên em còn có ghế cùng bộ với chiếc bàn này."),
    ("consumables", "/kənˈsjuːməblz/", "n", "vật tư tiêu hao (mực, lõi lọc…)", "Remember to offer <b>consumables</b> like filters and ink.", "Nhớ mời khách mua thêm vật tư tiêu hao như lõi lọc và mực in.", "消耗品", "shōmōhin"),
   ],
   "phrases": [
    ("Would you like a case to go with your new phone?", "Anh/chị có muốn lấy thêm ốp lưng cho điện thoại mới không ạ?"),
    ("Many customers also buy a spare filter.", "Nhiều khách cũng mua thêm một lõi lọc dự phòng ạ."),
    ("For just 200,000 dong more, you get the bigger size.", "Chỉ thêm 200.000 đồng là anh/chị có cỡ lớn hơn."),
    ("The Plus plan is better if you have more than ten users.", "Nếu có hơn mười người dùng thì gói Plus sẽ phù hợp hơn."),
    ("This goes really well with what you've chosen.", "Món này rất hợp với món anh/chị đã chọn."),
    ("If you buy both, you save 15%.", "Mua cả hai thì anh/chị tiết kiệm được 15%."),
    ("Do you have enough ink at home?", "Ở nhà anh/chị còn đủ mực in không ạ?"),
    ("No pressure. I just wanted to let you know.", "Không sao đâu ạ, em chỉ muốn báo để anh/chị biết thôi."),
    ("Would you like me to add it to your order?", "Em thêm món này vào đơn cho anh/chị nhé?"),
   ],
   "dialogues": [
    ("I'll take this laptop.", [
      ("Great choice! Would you like a laptop bag as well? It's 20% off when you buy it with a laptop.", True, "Khen lựa chọn + gợi ý món đi kèm có lợi cho khách."),
      ("You must buy a bag also.", False, "Ép khách bằng 'must' — bán chéo phải là gợi ý."),
      ("Bag you want?", False, "Sai trật tự câu hỏi: 'Would you like a bag?'"),
    ]),
    ("Is the basic plan enough for my team?", [
      ("How many people are in your team? If it's more than ten, the Plus plan is better value.", True, "Hỏi nhu cầu trước rồi mới gợi ý nâng gói."),
      ("Basic is too basic, you buy Pro.", False, "Đẩy gói đắt khi chưa hỏi nhu cầu, câu lủng củng."),
      ("Yes, is enough.", False, "Thiếu chủ ngữ 'it' và trả lời khi chưa biết đội bao nhiêu người."),
    ]),
    ("No thanks, I don't need anything else.", [
      ("No problem at all. I'll get your order ready now.", True, "Tôn trọng lời từ chối, chuyển sang hoàn tất đơn."),
      ("Are you sure? It's very cheap.", False, "Nài ép sau khi khách đã từ chối — dễ gây khó chịu."),
      ("OK, but later you will need.", False, "Thiếu tân ngữ ('you'll need it') và nghe như dọa khách."),
    ]),
    ("What's the difference between Plus and Pro?", [
      ("Pro adds 24/7 support and more storage. It costs about 30% more per month.", True, "So sánh rõ lợi ích + chênh lệch giá."),
      ("Pro is more pro.", False, "Lặp từ, không giải thích gì."),
      ("Pro have more thing.", False, "Sai hòa hợp chủ–vị ('has'), thiếu 's' và quá chung chung."),
    ]),
    ("I bought a water filter here last year.", [
      ("Thanks for coming back! The filter should be changed every 12 months. Would you like a new one?", True, "Cảm ơn khách quay lại + gợi ý vật tư thay thế có lý do rõ."),
      ("So what you want today?", False, "Thiếu trợ động từ ('What would you like today?') và bỏ lỡ cơ hội gợi ý lõi lọc."),
      ("Last year is old, buy new machine.", False, "Ép mua máy mới không cần thiết, sai ngữ pháp."),
    ]),
   ],
   "listen": [
    ("Would you like a case for your new phone", ["case", "phone"], "gợi ý phụ kiện"),
    ("Many customers also buy a spare battery", ["spare", "battery"], "gợi ý mua thêm"),
    ("If you buy both, you save fifteen percent", ["both", "fifteen"], "ưu đãi mua kèm"),
    ("The premium plan comes with extra storage", ["premium", "storage"], "giới thiệu gói cao cấp"),
    ("That printer is a great choice. Do you need extra ink? If you buy two boxes today, you get the third one free.", ["printer", "ink", "free"], "bán kèm mực in"),
    ("For only three hundred thousand more, you can get the larger size. It holds twice as much water. Most families choose this one.", ["larger", "twice", "families"], "mời khách lên cỡ lớn hơn"),
   ]},

  # ───────────── 5. Hội chợ, triển lãm & networking ─────────────
  {"title": "Hội chợ, triển lãm & networking",
   "vocab": [
    ("trade show", "/ˈtreɪd ˌʃəʊ/", "n", "hội chợ thương mại, triển lãm", "Our company will join the <b>trade show</b> in Ho Chi Minh City next month.", "Tháng sau công ty mình sẽ tham gia triển lãm ở TP.HCM.", "展示会", "tenjikai"),
    ("booth", "/buːð/", "n", "gian hàng (ở hội chợ)", "Come and visit us at <b>booth</b> B12.", "Mời anh/chị ghé gian hàng B12 của bên em.", "ブース", "būsu"),
    ("exhibitor", "/ɪɡˈzɪbɪtə/", "n", "đơn vị tham gia trưng bày", "There are over 300 <b>exhibitors</b> this year.", "Năm nay có hơn 300 đơn vị tham gia trưng bày.", "出展者", "shuttensha"),
    ("networking", "/ˈnetwɜːkɪŋ/", "n", "giao lưu, mở rộng quan hệ", "The <b>networking</b> event starts at 6 p.m.", "Buổi giao lưu bắt đầu lúc 6 giờ tối."),
    ("giveaway", "/ˈɡɪvəweɪ/", "n", "quà tặng miễn phí", "We have free pens and bags as <b>giveaways</b>.", "Bên em có bút và túi làm quà tặng miễn phí."),
    ("sample", "/ˈsɑːmpl/", "n", "hàng mẫu", "Can I have a <b>sample</b> to show my boss?", "Cho tôi xin một mẫu để đưa sếp xem được không?", "サンプル", "sanpuru"),
    ("elevator pitch", "/ˈelɪveɪtə ˌpɪtʃ/", "n", "phần tự giới thiệu siêu ngắn (khoảng 30 giây)", "Practise your <b>elevator pitch</b> before the fair.", "Hãy luyện phần giới thiệu 30 giây trước hội chợ."),
    ("name badge", "/ˈneɪm ˌbædʒ/", "n", "thẻ tên", "May I scan the QR code on your <b>name badge</b>?", "Em quét mã QR trên thẻ tên của anh/chị được không ạ?"),
    ("catalogue", "/ˈkætəlɒɡ/", "n", "catalô, danh mục sản phẩm", "Here's our new <b>catalogue</b> with all our products.", "Đây là catalô mới có đủ sản phẩm của bên em.", "カタログ", "katarogu"),
    ("contact details", "/ˈkɒntækt ˌdiːteɪlz/", "n", "thông tin liên hệ", "Could I take your <b>contact details</b>?", "Cho em xin thông tin liên hệ của anh/chị nhé."),
   ],
   "phrases": [
    ("Hi there! Have you heard of our company before?", "Chào anh/chị! Anh/chị đã từng nghe về công ty bên em chưa ạ?"),
    ("What brings you to the show today?", "Hôm nay anh/chị đến triển lãm để tìm gì ạ?"),
    ("We make eco-friendly packaging for food companies.", "Bên em sản xuất bao bì thân thiện môi trường cho các công ty thực phẩm."),
    ("Would you like to try a sample?", "Anh/chị có muốn thử hàng mẫu không ạ?"),
    ("May I scan your badge?", "Em quét thẻ của anh/chị được không ạ?"),
    ("Here's my card. Let's keep in touch.", "Đây là danh thiếp của em. Mình giữ liên lạc nhé."),
    ("What line of business are you in?", "Anh/chị làm trong lĩnh vực gì ạ?"),
    ("I'll send you our price list after the show.", "Sau triển lãm em sẽ gửi anh/chị bảng giá."),
    ("It was great talking to you.", "Nói chuyện với anh/chị rất vui ạ."),
    ("Could we set up a call next week?", "Tuần sau mình hẹn một cuộc gọi được không ạ?"),
   ],
   "dialogues": [
    ("Hi, what does your company do?", [
      ("We make eco-friendly food boxes for restaurants and cafés. Are you in the food business?", True, "Giới thiệu một câu rõ ràng + hỏi lại để tìm hiểu khách."),
      ("Our company make many thing.", False, "Sai 'makes', thiếu 's' ('things') và quá mơ hồ."),
      ("Please take brochure and read.", False, "Thiếu mạo từ và đẩy khách đi — phí cơ hội nói chuyện trực tiếp."),
    ]),
    ("Can I take a sample?", [
      ("Of course. May I scan your badge first, so I can send you the price list later?", True, "Đồng ý + xin thông tin liên hệ một cách khéo léo."),
      ("Sample only for big customer.", False, "Thiếu động từ và mạo từ; từ chối khách tiềm năng."),
      ("Take, take.", False, "Cộc lốc và bỏ lỡ cơ hội xin thông tin liên hệ."),
    ]),
    ("I'm just walking around today.", [
      ("No problem. Here's a small gift from us. If anything catches your eye, I'm right here.", True, "Thân thiện, không ép, vẫn giữ kết nối."),
      ("Why you come if not buy?", False, "Sai ngữ pháp và bất lịch sự."),
      ("OK.", False, "Quá cụt, bỏ lỡ cơ hội tạo ấn tượng."),
    ]),
    ("Sorry, I have to go to another meeting.", [
      ("Of course. Here's my card. Could I email you next week to follow up?", True, "Tôn trọng thời gian + đưa danh thiếp + hẹn liên lạc tiếp."),
      ("Wait, five more minutes please.", False, "Giữ khách khi họ đã bận — gây khó chịu."),
      ("OK, you call me later.", False, "Đẩy việc liên lạc cho khách — người bán nên chủ động."),
    ]),
    ("Nice to meet you. I'm Kevin, from a hotel group in Da Nang.", [
      ("Nice to meet you, Kevin. I'm Hoa from Lumo Pack. How many hotels does your group have?", True, "Chào lại + tự giới thiệu + câu hỏi mở để tiếp chuyện."),
      ("Nice to meet you. I am Hoa. You buy our product?", False, "Mời mua ngay quá vội, lại sai cấu trúc câu hỏi."),
      ("Da Nang very beautiful!", False, "Thiếu 'is' và lạc khỏi mục đích networking."),
    ]),
   ],
   "listen": [
    ("Come and visit us at booth B12", ["visit", "booth"], "mời khách ghé gian hàng"),
    ("Would you like to try a free sample", ["try", "sample"], "mời thử hàng mẫu"),
    ("May I scan the QR code on your badge", ["scan", "badge"], "xin quét thẻ tên"),
    ("Here's my card, let's keep in touch", ["card", "touch"], "giữ liên lạc"),
    ("Hi, welcome to our booth! We make paper boxes for coffee shops. Would you like to see our new catalogue?", ["welcome", "paper", "catalogue"], "chào khách tại gian hàng"),
    ("It was great to meet you at the trade show yesterday. As promised, I've attached our price list. Could we have a short call next Tuesday?", ["trade", "attached", "Tuesday"], "email sau hội chợ"),
   ]},

  # ───────────── 6. Tìm khách mới & gọi lạnh ─────────────
  {"title": "Tìm khách mới & gọi lạnh",
   "vocab": [
    ("prospect", "/ˈprɒspekt/", "n", "khách hàng triển vọng", "I found twenty new <b>prospects</b> in a business directory.", "Em tìm được hai mươi khách triển vọng mới trong một danh bạ doanh nghiệp."),
    ("cold call", "/ˌkəʊld ˈkɔːl/", "n", "cuộc gọi cho khách chưa quen", "I make about 50 <b>cold calls</b> a day.", "Mỗi ngày em gọi khoảng 50 cuộc cho khách chưa quen."),
    ("gatekeeper", "/ˈɡeɪtkiːpə/", "n", "người 'giữ cửa' (lễ tân, thư ký)", "Be polite to the <b>gatekeeper</b>. She decides if you can speak to the boss.", "Hãy lịch sự với người giữ cửa. Chị ấy quyết định mình có được nói chuyện với sếp hay không."),
    ("script", "/skrɪpt/", "n", "kịch bản cuộc gọi", "Follow the <b>script</b>, but sound natural.", "Làm theo kịch bản nhưng nói cho tự nhiên."),
    ("voicemail", "/ˈvɔɪsmeɪl/", "n", "hộp thư thoại; lời nhắn thoại", "If nobody answers, leave a short <b>voicemail</b>.", "Nếu không ai nghe máy, hãy để lại lời nhắn thoại ngắn."),
    ("referral", "/rɪˈfɜːrəl/", "n", "sự giới thiệu (khách do người quen giới thiệu)", "This client came to us through a <b>referral</b>.", "Khách này đến với bên mình nhờ được giới thiệu.", "紹介", "shōkai"),
    ("outreach", "/ˈaʊtriːtʃ/", "n", "việc chủ động liên hệ khách", "Our email <b>outreach</b> to new hotels starts on Monday.", "Đợt chủ động gửi email cho các khách sạn mới bắt đầu từ thứ Hai."),
    ("qualify", "/ˈkwɒlɪfaɪ/", "v", "sàng lọc (xem khách có thật sự phù hợp không)", "We <b>qualify</b> each lead before we send a quotation.", "Bên em sàng lọc từng khách tiềm năng trước khi gửi báo giá."),
    ("opt out", "/ˌɒpt ˈaʊt/", "phr v", "từ chối nhận (cuộc gọi, email quảng cáo)", "Customers can <b>opt out</b> of our calls at any time.", "Khách có thể từ chối nhận cuộc gọi của bên em bất cứ lúc nào."),
    ("call back", "/ˌkɔːl ˈbæk/", "phr v", "gọi lại", "Could I <b>call</b> you <b>back</b> on Thursday morning?", "Sáng thứ Năm em gọi lại cho anh/chị được không ạ?"),
   ],
   "phrases": [
    ("Hi, is this Mr. Brown?", "Xin chào, có phải anh Brown không ạ?"),
    ("This is Nam from Zenta Office. Is now a good time?", "Em là Nam bên Zenta Office. Bây giờ anh/chị nói chuyện được không ạ?"),
    ("I'll be quick. It'll only take two minutes.", "Em xin nói nhanh, chỉ mất hai phút thôi ạ."),
    ("We help small offices cut their printing costs.", "Bên em giúp các văn phòng nhỏ giảm chi phí in ấn."),
    ("Could you put me through to the office manager, please?", "Chị nối máy giúp em tới quản lý văn phòng được không ạ?"),
    ("Who is the best person to talk to about this?", "Về việc này thì em nên trao đổi với ai là phù hợp nhất ạ?"),
    ("Mr. Tan from Sunrise Hotel suggested I call you.", "Anh Tân bên khách sạn Sunrise gợi ý em gọi cho anh/chị."),
    ("Would you be open to a short meeting next week?", "Tuần sau anh/chị có thể dành cho em một buổi gặp ngắn không ạ?"),
    ("I'll send you a short email with more information.", "Em sẽ gửi anh/chị một email ngắn kèm thêm thông tin."),
    ("Sorry to bother you. Have a good day.", "Xin lỗi đã làm phiền anh/chị. Chúc anh/chị một ngày tốt lành."),
   ],
   "dialogues": [
    ("Good morning, Sunrise Hotel. How can I help you?", [
      ("Good morning. This is Nam from Zenta Office. Could I speak to the person in charge of office supplies, please?", True, "Tự giới thiệu + hỏi đúng người phụ trách, lịch sự với lễ tân."),
      ("I want talk to your boss.", False, "Thiếu 'to' ('I'd like to talk to…') và nghe thiếu lịch sự."),
      ("Hello, I sell office supplies. You buy?", False, "Chào bán luôn với lễ tân — sai người, sai ngữ pháp."),
    ]),
    ("What is this about?", [
      ("We help hotels cut their printing costs by about 20%. I'd like to share a few ideas with your manager.", True, "Nêu lợi ích cụ thể trong một câu, lý do gọi rõ ràng."),
      ("It's about business.", False, "Quá mơ hồ — người giữ cửa sẽ không nối máy."),
      ("Is secret, only for manager.", False, "Thiếu chủ ngữ 'It' và nghe đáng ngờ."),
    ]),
    ("She's in a meeting right now.", [
      ("No problem. When would be a good time to call back?", True, "Chấp nhận + hỏi giờ gọi lại cụ thể."),
      ("I wait. How long meeting?", False, "Câu cụt, thiếu động từ ('How long will the meeting be?')."),
      ("OK, I call again and again.", False, "Nghe như dọa làm phiền; thiếu 'will'."),
    ]),
    ("Can you just send me an email?", [
      ("Of course. What's the best email address? I'll send a short summary today and call you on Friday to follow up.", True, "Đồng ý + xin email + hẹn gọi lại để giữ cơ hội."),
      ("Email is not good, better we talk.", False, "Cãi lại yêu cầu của khách; sai cấu trúc ('It's better if we talk')."),
      ("OK. Bye.", False, "Không xin địa chỉ email — mất luôn đầu mối."),
    ]),
    ("Please don't call this number again.", [
      ("I'm sorry to bother you. I'll remove your number from our list today.", True, "Xin lỗi + tôn trọng quyền từ chối của khách."),
      ("But our offer is very good!", False, "Vẫn nài khi khách đã yêu cầu ngừng gọi — không tôn trọng khách."),
      ("Why? I only call one time.", False, "Tranh cãi với khách; sai thì ('I've only called once')."),
    ]),
   ],
   "listen": [
    ("Is now a good time to talk", ["good", "talk"], "hỏi khách có tiện nói chuyện không"),
    ("Could you put me through to the manager, please", ["through", "manager"], "nhờ lễ tân nối máy"),
    ("I'll call you back on Thursday morning", ["back", "Thursday"], "hẹn gọi lại"),
    ("Your colleague Linda suggested that I call you", ["colleague", "suggested"], "gọi nhờ người giới thiệu"),
    ("Hi, this is Nam from Zenta Office. We help small companies save money on printing. Do you have two minutes?", ["Office", "save", "minutes"], "mở đầu cuộc gọi lạnh"),
    ("Hello, this is Mai from Lumo Tech. I'm calling about your new office in District 2. Please call me back on this number.", ["calling", "office", "back"], "để lại lời nhắn thoại"),
   ]},

  # ───────────── 7. CRM & theo dõi cơ hội bán hàng ─────────────
  {"title": "CRM & theo dõi cơ hội bán hàng",
   "vocab": [
    ("CRM", "/ˌsiː ɑːr ˈem/", "n", "hệ thống quản lý quan hệ khách hàng", "Please update the <b>CRM</b> after every call.", "Sau mỗi cuộc gọi nhớ cập nhật lên CRM nhé.", "顧客管理システム", "kokyaku kanri shisutemu"),
    ("opportunity", "/ˌɒpəˈtjuːnəti/", "n", "cơ hội bán hàng (thương vụ đang theo)", "I created a new <b>opportunity</b> for the hotel project.", "Em đã tạo một cơ hội bán hàng mới cho dự án khách sạn.", "商談", "shōdan"),
    ("deal stage", "/ˈdiːl ˌsteɪdʒ/", "n", "giai đoạn của thương vụ", "Change the <b>deal stage</b> to 'Negotiation' after the meeting.", "Sau buổi họp thì chuyển giai đoạn thương vụ sang 'Đàm phán'."),
    ("follow up", "/ˌfɒləʊ ˈʌp/", "phr v", "liên hệ lại, bám sát", "I'll <b>follow up</b> with the client on Monday.", "Thứ Hai em sẽ liên hệ lại với khách.", "フォローする", "forō suru"),
    ("reminder", "/rɪˈmaɪndə/", "n", "lời nhắc", "Set a <b>reminder</b> to call her next Tuesday.", "Đặt lời nhắc gọi chị ấy vào thứ Ba tuần sau.", "リマインダー", "rimaindā"),
    ("win rate", "/ˈwɪn ˌreɪt/", "n", "tỷ lệ thắng thương vụ", "Our <b>win rate</b> for B2B deals is about 30%.", "Tỷ lệ thắng thương vụ B2B của nhóm khoảng 30%."),
    ("sales cycle", "/ˈseɪlz ˌsaɪkl/", "n", "chu kỳ bán hàng", "The <b>sales cycle</b> for big companies is often three months.", "Chu kỳ bán hàng với công ty lớn thường kéo dài ba tháng."),
    ("stalled", "/stɔːld/", "adj", "bị đình trệ, không tiến triển", "The deal is <b>stalled</b> because the client's director is on leave.", "Thương vụ đang đứng yên vì giám đốc bên khách đang nghỉ phép."),
    ("duplicate", "/ˈdjuːplɪkət/", "n", "bản trùng lặp", "Please delete the <b>duplicate</b> of this contact.", "Vui lòng xóa bản trùng của liên hệ này."),
    ("assign", "/əˈsaɪn/", "v", "giao (việc, khách) cho ai", "My manager <b>assigned</b> five new leads to me.", "Quản lý giao cho em năm khách tiềm năng mới."),
   ],
   "phrases": [
    ("I've logged the call in the CRM.", "Em đã ghi cuộc gọi vào CRM rồi ạ."),
    ("The next step is to send a proposal on Friday.", "Bước tiếp theo là gửi đề xuất vào thứ Sáu."),
    ("This deal is at the negotiation stage.", "Thương vụ này đang ở giai đoạn đàm phán."),
    ("The expected close date is the end of June.", "Ngày dự kiến chốt là cuối tháng Sáu."),
    ("I haven't heard from them for two weeks.", "Hai tuần nay em chưa nhận được phản hồi của họ."),
    ("Can you assign this lead to me?", "Anh giao khách tiềm năng này cho em được không?"),
    ("Please keep your customer notes short and clear.", "Ghi chú về khách nên ngắn gọn, rõ ràng nhé."),
    ("I'll set a reminder to follow up next week.", "Em sẽ đặt lời nhắc để liên hệ lại tuần sau."),
    ("We lost this deal because of the price.", "Mình mất thương vụ này vì giá."),
    ("Let's go through the open deals one by one.", "Mình rà lần lượt từng thương vụ đang mở nhé."),
   ],
   "dialogues": [
    ("Did you update the CRM after the meeting?", [
      ("Yes, I did. I added the notes and moved the deal to the proposal stage.", True, "Trả lời đủ 'Yes, I did' + nói rõ đã cập nhật gì."),
      ("Yes, update already.", False, "Thiếu chủ ngữ, sai thì: 'Yes, I've updated it.'"),
      ("CRM is waste of time.", False, "Thiếu mạo từ 'a' và phàn nàn thay vì trả lời."),
    ]),
    ("What's the status of the Sunrise Hotel deal?", [
      ("It's at the negotiation stage. They want 5% off, and I'm meeting them on Thursday.", True, "Nêu giai đoạn + vướng mắc + bước tiếp theo."),
      ("It is going.", False, "Quá mơ hồ, không có giai đoạn hay bước tiếp theo."),
      ("Deal is good, they like us very much.", False, "Thiếu mạo từ; chỉ cảm tính, không có dữ liệu."),
    ]),
    ("This deal hasn't moved for a month. What's happening?", [
      ("Their director is on leave until next week. I've set a reminder to call him on Monday.", True, "Giải thích nguyên nhân + hành động cụ thể."),
      ("I don't know, they don't answer.", False, "Buông xuôi — cần có kế hoạch liên hệ lại."),
      ("Customer is slow, not me.", False, "Thiếu mạo từ, đổ lỗi cho khách."),
    ]),
    ("When do you expect to close it?", [
      ("I expect to close it by the end of June, if they approve the budget.", True, "Có mốc thời gian + điều kiện rõ ràng."),
      ("Maybe soon, maybe not.", False, "Không có dự báo — quản lý không lập kế hoạch được."),
      ("I close it June.", False, "Sai thì và thiếu giới từ: 'I expect to close it in June.'"),
    ]),
    ("I see two records for the same customer.", [
      ("Sorry, that's a duplicate. I'll merge them and keep the newer one.", True, "Nhận lỗi + cách xử lý cụ thể."),
      ("Two is better than one.", False, "Đùa không đúng lúc — dữ liệu trùng làm sai báo cáo."),
      ("Not me create it.", False, "Sai ngữ pháp ('I didn't create it') và né trách nhiệm."),
    ]),
   ],
   "listen": [
    ("Please update the CRM after every call", ["update", "call"], "cập nhật CRM"),
    ("This deal is at the negotiation stage", ["deal", "negotiation"], "giai đoạn thương vụ"),
    ("I'll set a reminder to follow up next week", ["reminder", "follow"], "đặt lời nhắc"),
    ("The expected close date is the end of June", ["expected", "June"], "ngày dự kiến chốt"),
    ("Let's review the pipeline. We have twelve open deals this month. Three of them have stalled, so let's talk about those first.", ["review", "twelve", "stalled"], "trưởng nhóm rà các thương vụ"),
    ("I called the client this morning. They liked the demo, but they need approval from their head office. I've logged the call and set a reminder for Friday.", ["demo", "approval", "logged"], "báo tiến độ một thương vụ"),
   ]},

  # ───────────── 8. Giữ chân khách & gia hạn hợp đồng ─────────────
  {"title": "Giữ chân khách & gia hạn hợp đồng",
   "vocab": [
    ("renewal", "/rɪˈnjuːəl/", "n", "sự gia hạn (hợp đồng, gói dịch vụ)", "Your contract is due for <b>renewal</b> next month.", "Hợp đồng của anh/chị đến hạn gia hạn vào tháng sau.", "契約更新", "keiyaku kōshin"),
    ("retention", "/rɪˈtenʃn/", "n", "việc giữ chân khách hàng", "Customer <b>retention</b> costs less than finding new customers.", "Giữ chân khách cũ tốn ít chi phí hơn tìm khách mới."),
    ("churn", "/tʃɜːn/", "n", "tỷ lệ khách rời bỏ", "Our <b>churn</b> went down to 3% this quarter.", "Tỷ lệ khách rời bỏ quý này giảm còn 3%."),
    ("expire", "/ɪkˈspaɪə/", "v", "hết hạn", "Your subscription will <b>expire</b> on 30 June.", "Gói đăng ký của anh/chị sẽ hết hạn vào ngày 30 tháng Sáu."),
    ("loyalty programme", "/ˈlɔɪəlti ˌprəʊɡræm/", "n", "chương trình khách hàng thân thiết", "Members of our <b>loyalty programme</b> get double points this week.", "Thành viên chương trình khách hàng thân thiết được nhân đôi điểm tuần này."),
    ("long-term", "/ˌlɒŋ ˈtɜːm/", "adj", "lâu dài, lâu năm", "We offer better prices to <b>long-term</b> customers.", "Bên em có giá tốt hơn cho khách hàng lâu năm."),
    ("survey", "/ˈsɜːveɪ/", "n", "phiếu khảo sát", "Could you fill in a short <b>survey</b> about our service?", "Anh/chị điền giúp em một phiếu khảo sát ngắn về dịch vụ nhé.", "アンケート", "ankēto"),
    ("feedback", "/ˈfiːdbæk/", "n", "ý kiến phản hồi, góp ý", "Thank you for your honest <b>feedback</b>.", "Cảm ơn anh/chị đã góp ý thẳng thắn.", "フィードバック", "fīdobakku"),
    ("cancel", "/ˈkænsl/", "v", "hủy (hợp đồng, dịch vụ)", "Why do you want to <b>cancel</b> your contract?", "Vì sao anh/chị muốn hủy hợp đồng ạ?", "解約する", "kaiyaku suru"),
    ("relationship", "/rɪˈleɪʃnʃɪp/", "n", "mối quan hệ", "We want to build a strong <b>relationship</b> with every client.", "Bên em muốn xây dựng mối quan hệ bền chặt với từng khách hàng."),
   ],
   "phrases": [
    ("I'm calling because your contract ends next month.", "Em gọi vì hợp đồng của anh/chị hết hạn vào tháng sau."),
    ("How has our service been for you this year?", "Năm nay dịch vụ bên em phục vụ anh/chị thế nào ạ?"),
    ("Is there anything we could do better?", "Có điều gì bên em có thể làm tốt hơn không ạ?"),
    ("As a long-term customer, you get a 10% loyalty discount.", "Là khách hàng lâu năm, anh/chị được giảm 10% tri ân."),
    ("If you renew for two years, the price stays the same.", "Nếu gia hạn hai năm, giá sẽ giữ nguyên."),
    ("I'm sorry to hear you're thinking of leaving.", "Em rất tiếc khi biết anh/chị đang tính ngừng sử dụng."),
    ("May I ask why you want to cancel?", "Em có thể hỏi vì sao anh/chị muốn hủy không ạ?"),
    ("Your points will expire at the end of the year.", "Điểm của anh/chị sẽ hết hạn vào cuối năm."),
    ("Thank you for being with us for three years.", "Cảm ơn anh/chị đã đồng hành cùng bên em ba năm qua."),
    ("I'll send you the renewal offer by email today.", "Hôm nay em sẽ gửi ưu đãi gia hạn qua email cho anh/chị."),
   ],
   "dialogues": [
    ("We're thinking of changing to another supplier.", [
      ("I'm sorry to hear that. May I ask what the main reason is? I'd like to see if we can fix it.", True, "Đồng cảm + hỏi nguyên nhân + mong muốn khắc phục."),
      ("Other supplier is worse, you will see.", False, "Thiếu mạo từ, chê đối thủ và nghe như dọa khách."),
      ("OK, it's your choice. Bye.", False, "Buông khách quá nhanh — mất cơ hội giữ chân."),
    ]),
    ("Your price went up again this year.", [
      ("I understand. Since you've been with us for three years, I can keep last year's price if you renew for two years.", True, "Đồng cảm + ưu đãi có điều kiện cho khách lâu năm."),
      ("Everything is more expensive now.", False, "Bào chữa chung chung, không đưa giải pháp."),
      ("Price up is not my decision.", False, "Dịch từng chữ ('The price increase…') và né trách nhiệm."),
    ]),
    ("I want to cancel my subscription.", [
      ("I'm sorry to hear that. Before I cancel it, may I ask what didn't work for you?", True, "Tôn trọng yêu cầu nhưng hỏi lý do để cải thiện, giữ chân khách."),
      ("You cannot cancel, contract says one year.", False, "Cộc, thiếu mạo từ ('the contract') — nên giải thích điều khoản nhẹ nhàng."),
      ("Why you cancel? Our service is good.", False, "Sai ngữ pháp ('Why do you want to cancel?') và cãi khách."),
    ]),
    ("Honestly, your support team was slow last month.", [
      ("Thank you for telling me, and I'm sorry about that. We've added two more staff, and I'll check your cases personally.", True, "Cảm ơn góp ý + xin lỗi + hành động cụ thể."),
      ("Last month everyone busy.", False, "Thiếu động từ 'was' và chỉ bào chữa."),
      ("No, our team is always fast.", False, "Phủ nhận góp ý của khách — khách càng muốn rời đi."),
    ]),
    ("OK, we'll renew for another year.", [
      ("Thank you so much! I'll send the renewal contract today, and we'll have a review meeting every quarter.", True, "Cảm ơn + bước tiếp theo + cam kết chăm sóc định kỳ."),
      ("Good, I knew you can't leave us.", False, "Nghe kiêu ngạo; sai thì ('I knew you wouldn't leave')."),
      ("OK thank you, bye bye.", False, "Quá sơ sài cho một lần gia hạn quan trọng."),
    ]),
   ],
   "listen": [
    ("Your contract will expire at the end of May", ["contract", "expire"], "báo hợp đồng sắp hết hạn"),
    ("Thank you for your honest feedback", ["honest", "feedback"], "cảm ơn góp ý"),
    ("Long-term customers get a ten percent discount", ["Long-term", "ten"], "ưu đãi khách lâu năm"),
    ("Could you fill in a short survey for us", ["fill", "survey"], "mời làm khảo sát"),
    ("Hi, this is Linh from Zenta. Your yearly contract ends next month. If you renew this week, you'll get two extra months for free.", ["yearly", "renew", "extra"], "gọi mời gia hạn"),
    ("Our churn was five percent last quarter. Most customers left because of slow support. This quarter, let's call every key customer once a month.", ["churn", "support", "key"], "họp về giữ chân khách"),
   ]},
 ],

 "rev": [
  ("Ai là người quyết định cuối cùng ạ?", "Who makes the final decision?"),
  ("Đây là danh thiếp của em.", "Here's my business card."),
  ("Mọi người có thấy màn hình của em không?", "Can everyone see my screen?"),
  ("Để em hướng dẫn anh/chị từng bước.", "Let me walk you through it step by step."),
  ("Em cần hỏi ý quản lý đã ạ.", "I need to check with my manager."),
  ("Điều khoản thanh toán chuẩn là 30 ngày.", "Our standard payment terms are 30 days."),
  ("Nếu đặt 1.000 cái, bên em giảm 5%.", "If you order 1,000 units, we can offer 5% off."),
  ("Anh/chị có muốn lấy thêm ốp lưng không ạ?", "Would you like a case as well?"),
  ("Mời anh/chị ghé gian hàng của bên em.", "Please come and visit our booth."),
  ("Cho em xin thông tin liên hệ nhé.", "Could I have your contact details?"),
  ("Bây giờ anh/chị nói chuyện được không ạ?", "Is now a good time to talk?"),
  ("Chị nối máy giúp em tới quản lý nhé.", "Could you put me through to the manager, please?"),
  ("Em đã cập nhật CRM rồi.", "I've updated the CRM."),
  ("Thương vụ này đang ở giai đoạn đàm phán.", "This deal is at the negotiation stage."),
  ("Hợp đồng của anh/chị hết hạn vào tháng sau.", "Your contract expires next month."),
  ("Cảm ơn anh/chị đã góp ý thẳng thắn.", "Thank you for your honest feedback."),
 ],

 "reading": [
  {"t": "Meeting request", "text": "Subject: Meeting request – office chairs\nDear Ms. Thu,\nThank you for your call last week. Our procurement team would like to meet you on Tuesday 14 May at 10 a.m. at our head office. Please bring samples of the two chair models and your price list for 300 units.\nBest regards,\nPeter Lim\nPurchasing Manager", "q": [
    {"q": "Where will the meeting take place?", "o": ["At the supplier's shop", "At the customer's head office", "Online"], "a": 1},
    {"q": "What should Ms. Thu bring?", "o": ["Samples and a price list", "A signed contract", "An invoice for 300 units"], "a": 0}]},
  {"t": "Contract terms", "text": "SUPPLY AGREEMENT – KEY TERMS (DRAFT 2)\n• Price: 1,150,000 VND per unit (6% volume discount included)\n• Payment: 30% deposit, balance within 45 days of delivery\n• Lead time: 5 weeks from deposit\n• Late delivery: penalty of 0.5% per day, max. 5%\n• Length: 12 months, renews automatically unless cancelled 30 days before the end", "q": [
    {"q": "When must the rest of the money be paid?", "o": ["Before delivery", "Within 45 days of delivery", "Within 5 weeks of signing"], "a": 1},
    {"q": "What happens if nobody cancels the contract?", "o": ["It ends after 12 months", "The price goes up 5%", "It renews automatically"], "a": 2}]},
  {"t": "Booth staff plan", "text": "HOME & LIVING FAIR – BOOTH C07 – STAFF PLAN\nSat 9:00–13:00: Hoa, Nam (product demos)\nSat 13:00–18:00: Linh, Tuấn (demos + badge scanning)\nSun 9:00–17:00: whole team\nRemember: scan every visitor's badge, give catalogues only to visitors who leave their contact details, and keep the samples on the back shelf.", "q": [
    {"q": "Who works on Saturday afternoon?", "o": ["Hoa and Nam", "Linh and Tuấn", "The whole team"], "a": 1},
    {"q": "Who can get a catalogue?", "o": ["Every visitor", "Only visitors who leave contact details", "Only other exhibitors"], "a": 1}]},
  {"t": "CRM record", "text": "Opportunity: Sunrise Hotel – 120 air purifiers\nStage: Negotiation\nValue: 480,000,000 VND\nExpected close date: 28 June\nLast activity (12 June): Demo at the hotel. The general manager liked it but wants free installation. Decision-maker: finance director (on leave until 20 June).\nNext step: send a revised quote on 21 June.", "q": [
    {"q": "Why is the deal waiting?", "o": ["The demo went badly", "The decision-maker is on leave", "The price list is not ready"], "a": 1},
    {"q": "What does the hotel want?", "o": ["Free installation", "A longer warranty", "More air purifiers"], "a": 0}]},
  {"t": "Renewal offer", "text": "Dear Mr. Harris,\nThank you for using Zenta Cloud POS for two years. Your plan expires on 31 August. Renew before 15 August and get:\n- the same price as last year\n- 2 free months on a 2-year plan\n- a free staff training session\nTo renew, simply reply to this email or call your account manager, Linh.", "q": [
    {"q": "What is the last day to get this renewal offer?", "o": ["31 August", "15 August", "In two years"], "a": 1},
    {"q": "What extra do you get with a 2-year plan?", "o": ["A lower price", "2 free months", "A new account manager"], "a": 1}]},
 ],

 "ai": [
  ("demo", "Demo sản phẩm cho khách", "You are the operations manager of a restaurant chain. I am giving you an online demo of our stock management app. Ask about ease of use, compatibility with your current software and staff training. Interrupt me once with a question."),
  ("negotiate", "Đàm phán điều khoản hợp đồng", "You are the purchasing manager of a foreign-owned company. We are negotiating a supply contract. Ask for 12% off and 60-day payment terms. Accept a fair compromise only if I ask for something in return."),
  ("upsell", "Bán thêm & bán chéo", "You are a customer buying a new printer in an electronics shop. I am the sales assistant. Say no to the first extra item I suggest, but agree to buy extra ink if I explain the benefit clearly."),
  ("gatekeeper", "Gọi lạnh qua lễ tân", "You are the receptionist at a hotel. I am cold calling to speak to the purchasing manager. Ask who I am and why I am calling. Put me through only if I am polite and clear; otherwise ask me to send an email."),
 ],

 "events": [
  ("qbr", "Họp đánh giá quý với khách lớn", "You are the operations director of a key business customer. We are having a quarterly business review. Ask about delivery performance, support problems last quarter and ideas to save costs next quarter."),
  ("kickoff", "Họp triển khai với khách mới", "You are the project manager of a new customer who has just signed a contract with us. We are at the kickoff meeting. Ask about the delivery schedule, who your main contact is and how staff training will work."),
  ("launch", "Ra mắt sản phẩm mới", "You are my store manager. We are launching a new product next week. Ask me to give a 30-second pitch, then ask how I will answer a customer who says it is too expensive."),
 ],

 "quips": [
  "Business card ready!",
  "Demo time — fingers crossed!",
  "Let's find a win-win!",
  "Would you like fries with that?",
  "CRM updated… probably!",
  "Gatekeeper passed!",
 ],

 "roles": {
  "retail": {
   "scenarios": [
    ("rt_upsell", "Gợi ý mua kèm", "You are a customer buying a new phone in a shop. I am the sales assistant. When I suggest a case or other accessories, ask why you need them, and buy one only if my reason makes sense."),
    ("rt_gift", "Chọn quà tặng", "You are a customer looking for a birthday gift for a colleague, under 500,000 dong. Ask me for ideas, ask about gift wrapping and whether your colleague can exchange it."),
   ],
   "dialogues": [
    ("Do I really need a screen protector?", [
      ("You don't have to, but it protects the screen from scratches. A new screen costs much more.", True, "Trung thực + nêu lợi ích và so sánh chi phí."),
      ("Yes, you must buy, everybody buys.", False, "Ép mua, thiếu tân ngữ ('buy one') và lấy 'ai cũng mua' làm lý do."),
      ("Not need, but it is nice.", False, "Sai ngữ pháp ('You don't need it') và không đưa lý do thuyết phục."),
    ]),
    ("Can you gift-wrap this for me?", [
      ("Of course, it's free. Would you like a card with it too?", True, "Đồng ý + báo miễn phí + gợi ý thêm nhẹ nhàng."),
      ("Yes, wrap is free.", False, "Dùng sai từ loại: 'Gift wrapping is free.'"),
      ("You can wrap at home.", False, "Thiếu tân ngữ ('wrap it') và từ chối dịch vụ khách cần."),
    ]),
    ("Where can I find the batteries?", [
      ("They're in aisle 3, next to the light bulbs. Let me show you.", True, "Chỉ vị trí rõ + chủ động dẫn khách."),
      ("Battery there.", False, "Thiếu động từ và 's': 'The batteries are over there.'"),
      ("I don't know, ask other staff.", False, "Đẩy khách cho người khác, không giúp."),
    ]),
    ("Can I get this cheaper if I buy three?", [
      ("Yes, if you buy three, you get 10% off the total.", True, "Xác nhận + mức giảm cụ thể."),
      ("Three is cheaper, yes.", False, "Câu lủng củng, không nói rõ giảm bao nhiêu."),
      ("You buy three I give discount.", False, "Thiếu 'If' và mạo từ: 'If you buy three, I can give you 10% off.'"),
    ]),
   ]},
  "cs": {
   "scenarios": [
    ("cs_cancel", "Khách muốn hủy dịch vụ", "You are a customer calling to cancel your home internet contract because a competitor is cheaper. I am the retention agent. Explain your reason, listen to my offer and decide at the end."),
    ("cs_survey", "Gọi khảo sát sau hỗ trợ", "You are a customer who called support yesterday about a billing problem. I am calling to ask a few survey questions. Give a score of 7 out of 10 and explain what could be better."),
   ],
   "dialogues": [
    ("I want to cancel my internet contract.", [
      ("I'm sorry to hear that. May I ask why? There might be a better plan for you.", True, "Đồng cảm + hỏi lý do + gợi mở phương án giữ khách."),
      ("Cancel is very difficult.", False, "Sai từ loại ('Cancelling is…') và làm khách thấy bị cản trở."),
      ("OK, cancelled. Bye.", False, "Hủy ngay mà không hỏi lý do — bỏ lỡ cơ hội giữ khách."),
    ]),
    ("Why are you calling me?", [
      ("I'm calling about your support call yesterday. Could you answer three quick questions about our service?", True, "Nói rõ lý do gọi + cho biết chỉ mất ít thời gian."),
      ("For survey.", False, "Câu cụt, thiếu chủ ngữ và động từ."),
      ("You must answer some questions.", False, "Ra lệnh — khách không có nghĩa vụ trả lời khảo sát."),
    ]),
    ("I'd give you seven out of ten.", [
      ("Thank you. What could we do to make it a ten next time?", True, "Cảm ơn + hỏi cách cải thiện cụ thể."),
      ("Only seven? Why so low?", False, "Chất vấn điểm của khách — khách sẽ ngại góp ý."),
      ("OK, seven. Next question.", False, "Bỏ qua cơ hội hỏi lý do để cải thiện."),
    ]),
    ("My points expired, and nobody told me!", [
      ("I'm sorry about that. Let me check your account. If we didn't send you a reminder, I'll ask my team to restore your points.", True, "Xin lỗi + kiểm tra + hướng xử lý đúng mức, không hứa bừa."),
      ("Points expire is normal.", False, "Sai cấu trúc ('It's normal for points to expire') và gạt đi bức xúc của khách."),
      ("You should read the rules.", False, "Đổ lỗi cho khách."),
    ]),
   ]},
  "telesales": {
   "scenarios": [
    ("ts_gatekeeper", "Qua cửa lễ tân", "You are the receptionist of a small trading company. I am a telesales agent asking for your director. Say he is busy, ask what it is about, and offer to take a message."),
    ("ts_referral", "Gọi khách được giới thiệu", "You are a restaurant owner. I am calling because your friend, another restaurant owner, gave me your number. Be curious, ask what your friend bought and ask for a price."),
   ],
   "dialogues": [
    ("He's busy. Can I take a message?", [
      ("Yes, please. Could you tell him Nam from Zenta called about cutting printing costs? My number is 0901 234 567.", True, "Để lại lời nhắn đủ tên, công ty, lý do và số điện thoại."),
      ("No, I call again.", False, "Thiếu 'will' và từ chối để lời nhắn — mất cơ hội."),
      ("Tell him call me.", False, "Thiếu 'to' ('Tell him to call me') và nghe như ra lệnh."),
    ]),
    ("Who gave you my number?", [
      ("Mr. Tan from Sunrise Café. He's been our customer for a year, and he thought you might be interested.", True, "Nêu rõ người giới thiệu + lý do liên hệ — minh bạch."),
      ("Your friend, I can't say name.", False, "Mập mờ khiến khách nghi ngờ; thiếu 'his'."),
      ("It's not important.", False, "Né câu hỏi — thiếu minh bạch."),
    ]),
    ("Sorry, I can't hear you very well.", [
      ("Sorry about that. Is this better? I'm calling from Zenta about your office printers.", True, "Xin lỗi + kiểm tra lại đường truyền + nhắc lại lý do gọi ngắn gọn."),
      ("I speak loud already!", False, "Cãi khách; sai trạng từ và thì ('I'm already speaking loudly')."),
      ("Your phone is bad.", False, "Đổ lỗi cho thiết bị của khách."),
    ]),
    ("Send me the price, and I'll think about it.", [
      ("Sure. I'll text you the price list now. Could I call you on Friday to hear what you think?", True, "Gửi ngay + hẹn thời gian liên hệ lại."),
      ("Price is on website, you check.", False, "Đẩy khách tự tìm, thiếu mạo từ."),
      ("Why think? Order now is cheaper.", False, "Gây áp lực; sai ngữ pháp ('Ordering now is cheaper')."),
    ]),
   ]},
  "b2b": {
   "scenarios": [
    ("bb_demo", "Demo phần mềm cho khách", "You are the IT manager of a logistics company. I am giving you an online demo of our warehouse software. Ask if it works with your current system and how long setup takes. Be a little sceptical."),
    ("bb_review", "Họp đánh giá với khách lớn", "You are a key account customer at a quarterly review meeting. Say you are happy with quality but unhappy with two late deliveries. Ask what next quarter will look like."),
   ],
   "dialogues": [
    ("How long does setup usually take?", [
      ("For a company your size, about two weeks. Our team will install it and train your staff.", True, "Thời gian cụ thể + nói rõ bên nào làm gì."),
      ("Very fast, one day maybe.", False, "Hứa mơ hồ, thiếu thực tế."),
      ("Setup is depend on you.", False, "Sai ngữ pháp ('It depends on…') và đẩy trách nhiệm cho khách."),
    ]),
    ("Can you share some results from other customers?", [
      ("Of course. I'll send you a case study from a logistics company that cut picking errors by 40%.", True, "Đồng ý + dẫn chứng cụ thể, cùng ngành với khách."),
      ("All customers are happy, trust me.", False, "Khẳng định suông, không có bằng chứng."),
      ("Other customer information is secret.", False, "Từ chối cứng; có thể chia sẻ câu chuyện khách hàng đã được phép công bố."),
    ]),
    ("We need approval from our head office in Japan.", [
      ("I understand. Would it help if I prepared a short summary in English for them?", True, "Thông cảm + chủ động giúp khách trình cấp trên."),
      ("How long Japan answer?", False, "Thiếu trợ động từ, câu cụt: 'How long will it take them to reply?'"),
      ("Japan is always slow.", False, "Nhận xét tiêu cực, vơ đũa cả nắm — thiếu tế nhị."),
    ]),
    ("We might need to reduce our order next quarter.", [
      ("Thanks for letting me know early. May I ask why? Maybe we can adjust the delivery schedule or the product mix.", True, "Cảm ơn + hỏi lý do + đề xuất linh hoạt."),
      ("If you reduce, price will go up.", False, "Dọa khách ngay; thiếu mạo từ ('the price')."),
      ("Why you reduce?", False, "Sai trật tự câu hỏi ('Why do you need to reduce it?') và cộc."),
    ]),
   ]},
 },
}
