# -*- coding: utf-8 -*-
# Gói "marketing" — Marketing · TMĐT: digital marketing & quảng cáo, content & mạng xã hội,
# vận hành gian hàng trên sàn thương mại điện tử, brand / account ở agency.
# Người học làm việc với sếp nước ngoài, agency, đối tác, KOL. Mọi tên thương hiệu / sàn / app đều tự đặt
# (Kivo, Bamboo Bites, Mira Home, Shopza, Loopa, Chirpy…).
# Chặng lõi lấy từ office: 3 (Email công việc), 11 (Phỏng vấn & phát triển sự nghiệp).
# Schema: xem packs_src/README.md. Build: python3 packs_src/build.py marketing

PHASES = []

# ───────────────────────── 0. Brief & mục tiêu chiến dịch ─────────────────────────
PHASES.append({
 "title": "Brief & mục tiêu chiến dịch",
 "vocab": [
  ("brief", "/briːf/", "n", "bản brief, bản mô tả yêu cầu chiến dịch", "Please read the <b>brief</b> before the kick-off meeting.", "Vui lòng đọc brief trước buổi họp khởi động."),
  ("campaign", "/kæmˈpeɪn/", "n", "chiến dịch", "The Tết <b>campaign</b> starts on January 5.", "Chiến dịch Tết bắt đầu từ ngày 5 tháng 1.", "キャンペーン", "kyanpēn"),
  ("objective", "/əbˈdʒektɪv/", "n", "mục tiêu (cụ thể, đo được)", "Our main <b>objective</b> is to get 2,000 new customers.", "Mục tiêu chính của mình là có thêm 2.000 khách hàng mới.", "目標", "mokuhyō"),
  ("target audience", "/ˌtɑːɡɪt ˈɔːdiəns/", "n", "tệp khách hàng mục tiêu", "Our <b>target audience</b> is office workers aged 25 to 35.", "Tệp khách hàng mục tiêu là dân văn phòng từ 25 đến 35 tuổi.", "ターゲット層", "tāgettosō"),
  ("key message", "/ˌkiː ˈmesɪdʒ/", "n", "thông điệp chính", "The <b>key message</b> is 'healthy snacks for busy people'.", "Thông điệp chính là 'đồ ăn vặt lành mạnh cho người bận rộn'."),
  ("deliverable", "/dɪˈlɪvərəbl/", "n", "hạng mục bàn giao, đầu việc cần nộp", "The <b>deliverables</b> are three videos and ten banners.", "Các hạng mục bàn giao gồm ba video và mười banner."),
  ("launch", "/lɔːntʃ/", "v/n", "ra mắt, tung ra (sản phẩm, chiến dịch)", "We will <b>launch</b> the new flavour in March.", "Tháng Ba mình sẽ ra mắt vị mới."),
  ("brand awareness", "/ˌbrænd əˈweənəs/", "n", "độ nhận diện thương hiệu", "This campaign is about <b>brand awareness</b>, not sales.", "Chiến dịch này để tăng độ nhận diện thương hiệu, không phải doanh số.", "認知度", "ninchido"),
  ("ad spend", "/ˈæd spend/", "n", "chi phí quảng cáo, tiền chạy ads", "Our <b>ad spend</b> this month is 80 million dong.", "Chi phí chạy quảng cáo tháng này là 80 triệu đồng.", "広告費", "kōkokuhi"),
  ("scope", "/skəʊp/", "n", "phạm vi công việc", "Video editing is not in the <b>scope</b> of this project.", "Dựng video không nằm trong phạm vi dự án này."),
 ],
 "phrases": [
  ("What's the main objective of this campaign?", "Mục tiêu chính của chiến dịch này là gì?"),
  ("Who exactly is our target audience?", "Chính xác thì tệp khách hàng mục tiêu của mình là ai?"),
  ("What's the total budget, including ad spend?", "Tổng ngân sách là bao nhiêu, tính cả tiền chạy quảng cáo?"),
  ("When do we plan to launch?", "Dự kiến khi nào mình ra mắt?"),
  ("Could you send us the full brief by Friday?", "Anh/chị gửi bên em bản brief đầy đủ trước thứ Sáu được không ạ?"),
  ("Let me go through the deliverables and the timeline.", "Để em điểm lại các hạng mục bàn giao và tiến độ."),
  ("Is this campaign about awareness or sales?", "Chiến dịch này để tăng nhận diện hay tăng doanh số?"),
  ("How will we measure success?", "Mình sẽ đo lường thành công bằng cách nào?"),
  ("Should the key message be the same on all channels?", "Thông điệp chính có cần giống nhau trên mọi kênh không?"),
  ("That's outside the scope, but we can quote it separately.", "Việc đó nằm ngoài phạm vi, nhưng bên em có thể báo giá riêng."),
 ],
 "dialogues": [
  ("Here's the brief for the Tết campaign. Any questions?", [
    ("Thanks. Just one: is the main objective sales or brand awareness?", True, "Cảm ơn + hỏi lại điểm quan trọng nhất của brief."),
    ("No question. I understand all.", False, "Cộc và thiếu 'any': 'I don't have any questions.' Nên hỏi lại ít nhất một điểm cho chắc."),
    ("What is objective of campaign?", False, "Thiếu mạo từ: 'What is the objective of the campaign?'"),
  ]),
  ("Who are we targeting with this product?", [
    ("Mainly young mothers aged 25 to 35 in big cities.", True, "Nêu tệp khách rõ: ai, bao nhiêu tuổi, ở đâu."),
    ("Target is mother young.", False, "Trật tự từ kiểu tiếng Việt: 'young mothers'; lại thiếu tuổi, khu vực."),
    ("Everybody can buy it.", False, "'Nhắm tất cả' là câu trả lời yếu — marketing cần tệp khách cụ thể."),
  ]),
  ("Can we launch the campaign next Monday?", [
    ("It's a bit tight. We need two more days for the videos. How about Wednesday?", True, "Nói rõ vướng mắc + lý do + đề xuất ngày khác."),
    ("Cannot. Too fast.", False, "Thiếu chủ ngữ, cộc lốc; nên nêu lý do và đưa phương án."),
    ("Yes, we can, but the videos is not ready.", False, "Mâu thuẫn và sai chia động từ: 'the videos aren't ready'."),
  ]),
  ("Can you also make a TV ad with the same budget?", [
    ("I'm afraid a TV ad is outside the scope. I can send you a separate quote.", True, "Từ chối mềm bằng 'outside the scope' + đề xuất báo giá riêng."),
    ("No, TV ad is not our job.", False, "Thiếu mạo từ 'a TV ad', từ chối thẳng thừng với khách."),
    ("OK, no problem, we do everything.", False, "Nhận bừa việc ngoài phạm vi, dễ vỡ ngân sách; lại thiếu 'will'."),
  ]),
  ("How will we measure success?", [
    ("We'll track reach, website visits and new customers every week.", True, "Nêu chỉ số cụ thể + tần suất theo dõi."),
    ("We will see it success or not.", False, "Sai từ loại: 'whether it's successful'; và không nêu chỉ số."),
    ("Success is when boss happy.", False, "Thiếu mạo từ, động từ ('the boss is happy') và không chuyên nghiệp."),
  ]),
 ],
 "listen": [
  ("Please read the brief before the meeting", ["brief", "meeting"], "chuẩn bị họp khởi động"),
  ("Our target audience is young office workers", ["target", "office"], "tệp khách hàng"),
  ("The main objective is brand awareness", ["objective", "awareness"], "mục tiêu chiến dịch"),
  ("We plan to launch the campaign in March", ["launch", "March"], "thời điểm ra mắt"),
  ("The client wants to launch a new green tea drink. The budget is 300 million dong for two months. The key message is fresh and healthy.", ["green", "budget", "healthy"], "tóm tắt brief"),
  ("Here are the deliverables. We need five short videos and twenty banners. Everything must be ready by the end of the month.", ["deliverables", "videos", "ready"], "hạng mục bàn giao"),
 ],
})

# ───────────────────────── 1. Chân dung khách hàng & nghiên cứu ─────────────────────────
PHASES.append({
 "title": "Chân dung khách hàng & nghiên cứu",
 "vocab": [
  ("persona", "/pəˈsəʊnə/", "n", "chân dung khách hàng (nhân vật đại diện)", "Our main <b>persona</b> is Linh, a 28-year-old accountant.", "Chân dung khách hàng chính là Linh, kế toán 28 tuổi.", "ペルソナ", "perusona"),
  ("survey", "/ˈsɜːveɪ/", "n", "khảo sát", "We sent an online <b>survey</b> to 500 customers.", "Bên mình đã gửi khảo sát online cho 500 khách hàng.", "アンケート", "ankēto"),
  ("insight", "/ˈɪnsaɪt/", "n", "insight, sự thấu hiểu khách hàng", "The key <b>insight</b> is that people shop late at night.", "Insight quan trọng là mọi người hay mua sắm lúc khuya."),
  ("competitor", "/kəmˈpetɪtə/", "n", "đối thủ cạnh tranh", "Our biggest <b>competitor</b> just cut its prices.", "Đối thủ lớn nhất của mình vừa giảm giá.", "競合", "kyōgō"),
  ("market research", "/ˌmɑːkɪt rɪˈsɜːtʃ/", "n", "nghiên cứu thị trường", "The <b>market research</b> shows strong demand in Đà Nẵng.", "Nghiên cứu thị trường cho thấy nhu cầu ở Đà Nẵng rất cao.", "市場調査", "shijō chōsa"),
  ("pain point", "/ˈpeɪn pɔɪnt/", "n", "nỗi đau, vấn đề khách đang gặp", "Slow delivery is a big <b>pain point</b> for our customers.", "Giao hàng chậm là một nỗi đau lớn của khách hàng."),
  ("segment", "/ˈseɡmənt/", "n", "phân khúc, nhóm khách hàng", "Students are our fastest-growing <b>segment</b>.", "Sinh viên là phân khúc tăng nhanh nhất của mình."),
  ("demographic", "/ˌdeməˈɡræfɪk/", "n/adj", "(thuộc) nhân khẩu học: tuổi, giới tính, thu nhập…", "Most buyers are in the 18–24 <b>demographic</b>.", "Phần lớn người mua thuộc nhóm tuổi 18–24."),
  ("focus group", "/ˈfəʊkəs ɡruːp/", "n", "nhóm thảo luận khách hàng (phỏng vấn nhóm)", "We ran a <b>focus group</b> with eight young mothers.", "Bên mình đã tổ chức một buổi thảo luận nhóm với tám bà mẹ trẻ."),
  ("trend", "/trend/", "n", "xu hướng", "Short videos are the biggest <b>trend</b> this year.", "Video ngắn là xu hướng lớn nhất năm nay.", "トレンド", "torendo"),
 ],
 "phrases": [
  ("Who is our typical customer?", "Khách hàng điển hình của mình là ai?"),
  ("What problem are we solving for them?", "Mình đang giải quyết vấn đề gì cho họ?"),
  ("According to the survey, 60% of users shop on their phones.", "Theo khảo sát, 60% người dùng mua sắm trên điện thoại."),
  ("The main insight is that they don't have time to cook.", "Insight chính là họ không có thời gian nấu ăn."),
  ("Let's look at what our competitors are doing.", "Mình cùng xem đối thủ đang làm gì nhé."),
  ("This segment is small, but it's growing fast.", "Phân khúc này nhỏ nhưng đang tăng nhanh."),
  ("Where do they usually spend time online?", "Họ thường dành thời gian ở đâu trên mạng?"),
  ("We need more data before we decide.", "Mình cần thêm dữ liệu trước khi quyết định."),
  ("I'll put the key findings on one slide.", "Em sẽ tóm các phát hiện chính vào một slide."),
 ],
 "dialogues": [
  ("Who is our main customer for this skincare line?", [
    ("Mostly women aged 22 to 30 who work in offices and care about natural ingredients.", True, "Mô tả chân dung đủ: giới tính, tuổi, công việc, mối quan tâm."),
    ("Woman, young, office.", False, "Chỉ liệt kê từ rời, không thành câu."),
    ("All woman like skincare.", False, "Thiếu 's' số nhiều ('All women') và quá chung chung, không có insight."),
  ]),
  ("What did the survey tell us?", [
    ("Most customers said the price was fine, but delivery was too slow.", True, "Tóm tắt kết quả rõ, lùi thì đúng khi thuật lại."),
    ("Customer say price OK but delivery slow.", False, "Thiếu 's'/lùi thì và mạo từ: 'Customers said the price was OK…'"),
    ("Survey is finish already.", False, "Sai cấu trúc ('The survey is finished') và không trả lời câu hỏi."),
  ]),
  ("What are our competitors doing on social media?", [
    ("They post short cooking videos every day, and their engagement is quite high.", True, "Mô tả cụ thể + nhận xét ngắn về hiệu quả."),
    ("They are doing very much posts.", False, "Sai cụm từ: 'They post a lot.' / 'They post very often.'"),
    ("I don't care competitors.", False, "Thiếu 'about' và sai thái độ — theo dõi đối thủ là việc của marketing."),
  ]),
  ("What's the biggest pain point for our users?", [
    ("They find it hard to choose the right size, so many of them return the product.", True, "Nêu vấn đề + hệ quả kinh doanh."),
    ("The biggest pain is in their back.", False, "Hiểu nhầm 'pain point' thành đau thật — đây là vấn đề khách gặp phải."),
    ("They difficult to choose size.", False, "Thiếu động từ: 'They find it difficult to choose…'"),
  ]),
  ("Should we target students too?", [
    ("Maybe later. The data shows they buy less often, so let's focus on young workers first.", True, "Đưa ý kiến dựa trên dữ liệu + đề xuất ưu tiên."),
    ("Yes, more people, more money.", False, "Lập luận cảm tính, không dựa trên dữ liệu hay tệp mục tiêu."),
    ("Student no money.", False, "Thiếu động từ, cộc và mang tính quy chụp: 'Students usually have a smaller budget.'"),
  ]),
 ],
 "listen": [
  ("We sent the survey to five hundred customers", ["survey", "hundred"], "khảo sát khách hàng"),
  ("The key insight is that people shop late at night", ["insight", "night"], "insight khách hàng"),
  ("Our biggest competitor cut its prices last week", ["competitor", "prices"], "động thái đối thủ"),
  ("Students are our fastest-growing segment", ["Students", "segment"], "phân khúc khách hàng"),
  ("Meet our persona, Linh. She's twenty-eight and works in an office. She buys most things on her phone.", ["persona", "office", "phone"], "giới thiệu chân dung khách hàng"),
  ("We ran two focus groups last week. Most people liked the new packaging. But they thought the price was too high.", ["focus", "packaging", "price"], "kết quả thảo luận nhóm"),
 ],
})

# ───────────────────────── 2. Nội dung & mạng xã hội ─────────────────────────
PHASES.append({
 "title": "Nội dung & mạng xã hội",
 "vocab": [
  ("engagement", "/ɪnˈɡeɪdʒmənt/", "n", "tương tác (like, bình luận, chia sẻ)", "This video got great <b>engagement</b>: 3,000 comments.", "Video này tương tác rất tốt: 3.000 bình luận.", "エンゲージメント", "engējimento"),
  ("reach", "/riːtʃ/", "n/v", "lượt tiếp cận; tiếp cận", "The post had a <b>reach</b> of 50,000 people.", "Bài đăng tiếp cận được 50.000 người.", "リーチ", "rīchi"),
  ("caption", "/ˈkæpʃn/", "n", "chú thích, caption bài đăng", "Keep the <b>caption</b> short and add a question.", "Viết caption ngắn thôi và thêm một câu hỏi."),
  ("post", "/pəʊst/", "n/v", "bài đăng; đăng bài", "We <b>post</b> on our fan page twice a day.", "Bên mình đăng bài trên fanpage hai lần mỗi ngày.", "投稿", "tōkō"),
  ("hashtag", "/ˈhæʃtæɡ/", "n", "hashtag, thẻ #", "Use our campaign <b>hashtag</b> in every post.", "Dùng hashtag của chiến dịch trong mọi bài đăng.", "ハッシュタグ", "hasshutagu"),
  ("content calendar", "/ˈkɒntent ˌkælɪndə/", "n", "lịch nội dung", "The <b>content calendar</b> for March is ready.", "Lịch nội dung tháng Ba đã xong."),
  ("follower", "/ˈfɒləʊə/", "n", "người theo dõi", "Our Loopa channel reached 100,000 <b>followers</b>.", "Kênh Loopa của mình đã đạt 100.000 người theo dõi.", "フォロワー", "forowā"),
  ("share", "/ʃeə/", "v/n", "chia sẻ; lượt chia sẻ", "Ask people to <b>share</b> the video with a friend.", "Kêu gọi mọi người chia sẻ video cho một người bạn."),
  ("go viral", "/ɡəʊ ˈvaɪrəl/", "phr", "lan truyền mạnh, 'viral'", "Nobody expected the dance video to <b>go viral</b>.", "Không ai ngờ video nhảy lại viral như vậy."),
  ("livestream", "/ˈlaɪvstriːm/", "n/v", "phát trực tiếp, livestream", "We sell a lot during the Friday night <b>livestream</b>.", "Bên mình bán rất chạy trong buổi livestream tối thứ Sáu.", "ライブ配信", "raibu haishin"),
 ],
 "phrases": [
  ("Here's the content calendar for next month.", "Đây là lịch nội dung cho tháng sau."),
  ("Could you check the caption before I post it?", "Anh/chị xem giúp caption trước khi em đăng được không?"),
  ("This post got twice as much engagement as usual.", "Bài này có tương tác gấp đôi bình thường."),
  ("Our best time to post is 8 p.m.", "Khung giờ đăng tốt nhất của mình là 8 giờ tối."),
  ("Let's reply to every comment within an hour.", "Mình trả lời mọi bình luận trong vòng một tiếng nhé."),
  ("Short videos work better than photos for us.", "Với bên mình, video ngắn hiệu quả hơn ảnh."),
  ("We should add a clear call to action at the end.", "Mình nên thêm lời kêu gọi hành động rõ ràng ở cuối."),
  ("The livestream starts at 8 p.m. on Friday.", "Buổi livestream bắt đầu lúc 8 giờ tối thứ Sáu."),
  ("Can we reuse this video on other platforms?", "Mình dùng lại video này trên các nền tảng khác được không?"),
 ],
 "dialogues": [
  ("Can you write a caption for this photo?", [
    ("Sure. I'll keep it short and end with a question to get more comments.", True, "Nhận việc + nói rõ cách làm có mục đích."),
    ("Sure, I write now.", False, "Sai thì: 'I'll write it now.' (thiếu 'will' và tân ngữ 'it')."),
    ("Caption is not important.", False, "Phủ nhận yêu cầu, sai quan điểm nghề — caption ảnh hưởng tương tác."),
  ]),
  ("How did yesterday's video do?", [
    ("Really well. It reached 80,000 people and got 2,500 shares.", True, "Trả lời ngắn + số liệu cụ thể (reach, share)."),
    ("It very good, many people see.", False, "Thiếu động từ và dùng sai thì: 'It did very well. Many people saw it.'"),
    ("I don't check yet.", False, "Sai thì: 'I haven't checked yet.' — và nên kiểm tra số trước khi họp."),
  ]),
  ("Why is our engagement dropping?", [
    ("I think we post too many product photos. People respond better to real stories.", True, "Nêu giả thuyết + gợi ý hướng cải thiện."),
    ("Because the algorithm, I don't know.", False, "Thiếu 'of' ('Because of the algorithm') và đổ lỗi mơ hồ."),
    ("Engagement is drop because people lazy.", False, "Sai ngữ pháp ('is dropping', 'are lazy') và đổ lỗi cho khách."),
  ]),
  ("Someone left a rude comment on our post. What should we do?", [
    ("Let's reply politely and offer to help by private message. We shouldn't delete it.", True, "Xử lý chuyên nghiệp: trả lời lịch sự, chuyển sang tin nhắn riêng."),
    ("Delete and block him.", False, "Phản ứng cảm tính, dễ gây khủng hoảng truyền thông."),
    ("We reply him strong.", False, "Thiếu 'to' ('reply to him') và đôi co với khách là sai nguyên tắc."),
  ]),
  ("Can you host the livestream on Friday night?", [
    ("Yes, I can. Could you send me the product list and the vouchers by Thursday?", True, "Nhận lời + hỏi đúng thông tin cần chuẩn bị."),
    ("Yes, I can host. But I am shy with camera.", False, "Thiếu mạo từ ('the camera') và làm sếp mất tự tin vào mình."),
    ("Friday I busy.", False, "Thiếu 'am' và cộc lốc: 'Sorry, I'm busy on Friday. How about Saturday?'"),
  ]),
 ],
 "listen": [
  ("This post got great engagement yesterday", ["post", "engagement"], "kết quả bài đăng"),
  ("Please add our hashtag to every caption", ["hashtag", "caption"], "quy định bài đăng"),
  ("The livestream starts at eight on Friday", ["livestream", "Friday"], "lịch livestream"),
  ("Our channel now has fifty thousand followers", ["fifty", "followers"], "số người theo dõi"),
  ("The content calendar for April is ready. We have three videos and two posts every week. Please check the captions by Wednesday.", ["April", "videos", "Wednesday"], "lịch nội dung tháng"),
  ("The dance video went viral last night. It reached two million people. We got more followers in one day than in a whole month.", ["viral", "million", "month"], "video viral"),
 ],
})

# ───────────────────────── 3. Quảng cáo trả phí ─────────────────────────
PHASES.append({
 "title": "Quảng cáo trả phí",
 "vocab": [
  ("ad", "/æd/", "n", "quảng cáo (mẩu quảng cáo)", "The new <b>ad</b> goes live tomorrow morning.", "Mẫu quảng cáo mới sẽ chạy từ sáng mai.", "広告", "kōkoku"),
  ("impression", "/ɪmˈpreʃn/", "n", "lượt hiển thị", "The ad got 200,000 <b>impressions</b> but few clicks.", "Quảng cáo có 200.000 lượt hiển thị nhưng ít lượt nhấp.", "インプレッション", "inpuresshon"),
  ("CTR", "/ˌsiː tiː ˈɑː/", "n", "tỉ lệ nhấp (click-through rate) = số lượt nhấp ÷ số lượt hiển thị", "Our <b>CTR</b> went up from 1% to 2.5%.", "CTR của mình tăng từ 1% lên 2,5%.", "クリック率", "kurikkuritsu"),
  ("CPC", "/ˌsiː piː ˈsiː/", "n", "chi phí mỗi lượt nhấp (cost per click) = chi phí quảng cáo ÷ số lượt nhấp", "The <b>CPC</b> is about 3,000 dong on Chirpy.", "CPC trên Chirpy khoảng 3.000 đồng."),
  ("ROAS", "/ˈrəʊæs/", "n", "lợi tức trên chi phí quảng cáo (return on ad spend) = doanh thu từ quảng cáo ÷ chi phí quảng cáo", "A <b>ROAS</b> of 4 means 4 dong in revenue for every 1 dong we spend on ads.", "ROAS bằng 4 nghĩa là cứ chi 1 đồng quảng cáo thì thu về 4 đồng doanh thu (chưa phải lợi nhuận)."),
  ("A/B test", "/ˌeɪ ˈbiː test/", "n/v", "thử nghiệm A/B (so sánh hai phiên bản)", "Let's <b>A/B test</b> two different headlines.", "Mình chạy thử A/B hai tiêu đề khác nhau nhé.", "ABテスト", "ē-bī tesuto"),
  ("targeting", "/ˈtɑːɡɪtɪŋ/", "n", "nhắm mục tiêu (cài đặt đối tượng quảng cáo)", "The <b>targeting</b> is too broad, so the cost is high.", "Nhắm đối tượng quá rộng nên chi phí cao."),
  ("retargeting", "/ˌriːˈtɑːɡɪtɪŋ/", "n", "quảng cáo bám đuổi, tiếp thị lại", "Use <b>retargeting</b> for people who left items in their cart.", "Dùng quảng cáo bám đuổi cho người đã bỏ hàng trong giỏ.", "リターゲティング", "ritāgetingu"),
  ("landing page", "/ˈlændɪŋ peɪdʒ/", "n", "trang đích (trang khách vào sau khi nhấp)", "The <b>landing page</b> loads too slowly on mobile.", "Trang đích tải quá chậm trên điện thoại.", "ランディングページ", "randingu pēji"),
  ("creative", "/kriˈeɪtɪv/", "n", "mẫu thiết kế/nội dung quảng cáo (ảnh, video)", "This <b>creative</b> is getting tired. Let's make a new one.", "Mẫu quảng cáo này bị nhàm rồi, làm mẫu mới đi."),
 ],
 "phrases": [
  ("The ads will go live at 9 a.m. tomorrow.", "Quảng cáo sẽ chạy từ 9 giờ sáng mai."),
  ("Our CTR is below the industry average.", "CTR của mình thấp hơn mức trung bình của ngành."),
  ("The cost per click went up by 20% this week.", "Chi phí mỗi lượt nhấp tuần này tăng 20%."),
  ("Let's move more budget to the ads that are working.", "Mình chuyển thêm ngân sách sang các quảng cáo đang hiệu quả nhé."),
  ("I'd like to pause this ad. The ROAS is too low.", "Em muốn tạm dừng quảng cáo này. ROAS thấp quá."),
  ("We're A/B testing two versions of the video.", "Bên em đang thử A/B hai phiên bản video."),
  ("The targeting is too broad, so let's narrow it.", "Nhắm đối tượng rộng quá, mình thu hẹp lại nhé."),
  ("Version B has a higher click-through rate.", "Phiên bản B có tỉ lệ nhấp cao hơn."),
  ("We need a new creative every two weeks.", "Mình cần mẫu quảng cáo mới mỗi hai tuần."),
  ("Could you check why the ad was rejected?", "Anh/chị kiểm tra giúp vì sao quảng cáo bị từ chối được không?"),
 ],
 "dialogues": [
  ("How are the ads performing this week?", [
    ("Quite well. The ROAS is 3.8, and the CTR went up to 2%.", True, "Đánh giá chung + hai chỉ số chính có số cụ thể."),
    ("The ads is running.", False, "Sai chia động từ ('are') và không trả lời về hiệu quả."),
    ("Very good, very good.", False, "Cảm tính, không có số liệu — sếp sẽ hỏi lại ngay."),
  ]),
  ("Why is our cost per click so high?", [
    ("I think the targeting is too broad. I'll narrow it and test two new audiences.", True, "Nêu nguyên nhân + hành động cụ thể."),
    ("Because the platform is expensive, we cannot do anything.", False, "Đổ lỗi cho nền tảng, không đưa giải pháp."),
    ("Cost per click high because many people click.", False, "Sai logic (nhiều click không làm CPC tăng) và thiếu 'is'."),
  ]),
  ("Which version won the A/B test?", [
    ("Version B. Its CTR was 40% higher, so I'd suggest we use it for all ads.", True, "Trả lời thẳng + bằng chứng + đề xuất tiếp theo."),
    ("B win.", False, "Sai thì, cộc lốc: 'Version B won.'"),
    ("Both is OK, I think.", False, "Sai chia ('Both are') và không kết luận được — mất ý nghĩa thử A/B."),
  ]),
  ("The ad was rejected by the platform. What happened?", [
    ("The image had too much text. I'm fixing it now and will resubmit by noon.", True, "Nêu lý do + đang xử lý + mốc thời gian."),
    ("I don't know. The platform is stupid.", False, "Thiếu chuyên nghiệp, không tìm hiểu nguyên nhân."),
    ("It rejected because image.", False, "Sai bị động và thiếu 'of': 'It was rejected because of the image.'"),
  ]),
  ("Should we increase the ad spend for the weekend?", [
    ("Yes, but only on the two ads with the best ROAS. I'd add 20%.", True, "Đồng ý có điều kiện + mức cụ thể."),
    ("Yes, spend more, sell more.", False, "Đơn giản hoá quá — tăng tiền chưa chắc tăng đơn nếu ads kém."),
    ("We should increasing it.", False, "Sai: sau 'should' dùng động từ nguyên thể: 'We should increase it.'"),
  ]),
 ],
 "listen": [
  ("The new ads will go live tomorrow morning", ["ads", "tomorrow"], "lịch chạy quảng cáo"),
  ("Our click-through rate went up to two percent", ["click-through", "two"], "tỉ lệ nhấp"),
  ("Please pause the ads with a low ROAS", ["pause", "ROAS"], "tạm dừng quảng cáo"),
  ("The landing page is too slow on mobile", ["landing", "mobile"], "vấn đề trang đích"),
  ("We tested two videos last week. Version A was funny and version B was emotional. Version B had a much higher click-through rate.", ["tested", "emotional", "higher"], "kết quả thử A/B"),
  ("The cost per click is too high right now. I think our targeting is too broad. Let's focus on women aged twenty-five to thirty-five.", ["cost", "targeting", "women"], "tối ưu quảng cáo"),
 ],
})

# ───────────────────────── 4. Số liệu & báo cáo (KPI) ─────────────────────────
PHASES.append({
 "title": "Số liệu & báo cáo (KPI)",
 "vocab": [
  ("KPI", "/ˌkeɪ piː ˈaɪ/", "n", "chỉ số đánh giá hiệu quả (KPI)", "Our main <b>KPI</b> this quarter is new customers.", "KPI chính quý này là số khách hàng mới.", "KPI", "kē-pī-ai"),
  ("conversion rate", "/kənˈvɜːʃn reɪt/", "n", "tỉ lệ chuyển đổi = số đơn (hành động mục tiêu) ÷ số lượt truy cập", "The <b>conversion rate</b> on the website is 1.8%.", "Tỉ lệ chuyển đổi trên website là 1,8%.", "コンバージョン率", "konbājonritsu"),
  ("dashboard", "/ˈdæʃbɔːd/", "n", "bảng theo dõi số liệu (dashboard)", "You can see all the numbers on the <b>dashboard</b>.", "Anh/chị xem được toàn bộ số liệu trên dashboard."),
  ("metric", "/ˈmetrɪk/", "n", "chỉ số đo lường", "Likes are not the most important <b>metric</b>.", "Lượt thích không phải chỉ số quan trọng nhất."),
  ("benchmark", "/ˈbentʃmɑːk/", "n", "mức chuẩn để so sánh", "Our CTR is above the industry <b>benchmark</b>.", "CTR của mình cao hơn mức chuẩn của ngành."),
  ("revenue", "/ˈrevənjuː/", "n", "doanh thu", "Online <b>revenue</b> grew by 30% in May.", "Doanh thu online tháng Năm tăng 30%.", "売上", "uriage"),
  ("month-on-month", "/ˌmʌnθ ɒn ˈmʌnθ/", "adj/adv", "so với tháng trước", "Orders are up 12% <b>month-on-month</b>.", "Số đơn tăng 12% so với tháng trước.", "前月比", "zengetsuhi"),
  ("bounce rate", "/ˈbaʊns reɪt/", "n", "tỉ lệ thoát (vào trang rồi rời ngay)", "The <b>bounce rate</b> is 70%, so the page needs work.", "Tỉ lệ thoát là 70%, nên trang cần sửa lại.", "直帰率", "chokkiritsu"),
  ("outperform", "/ˌaʊtpəˈfɔːm/", "v", "hiệu quả hơn, vượt (đối thủ, kỳ vọng)", "Video ads <b>outperformed</b> image ads this month.", "Tháng này quảng cáo video hiệu quả hơn quảng cáo ảnh."),
  ("spike", "/spaɪk/", "n", "sự tăng vọt đột ngột", "There was a <b>spike</b> in traffic after the livestream.", "Lượng truy cập tăng vọt sau buổi livestream."),
 ],
 "phrases": [
  ("Let me walk you through the numbers.", "Để em trình bày qua các số liệu."),
  ("We reached 95% of our KPI this month.", "Tháng này mình đạt 95% KPI."),
  ("Revenue is up 15% month-on-month.", "Doanh thu tăng 15% so với tháng trước."),
  ("The conversion rate dropped slightly, from 2% to 1.7%.", "Tỉ lệ chuyển đổi giảm nhẹ, từ 2% xuống 1,7%."),
  ("As you can see on the dashboard, most orders come from mobile.", "Như anh/chị thấy trên dashboard, phần lớn đơn đến từ điện thoại."),
  ("There was a spike in traffic on Saturday.", "Lượng truy cập tăng vọt vào thứ Bảy."),
  ("We're still below the benchmark for email.", "Kênh email của mình vẫn dưới mức chuẩn."),
  ("The main reason is the new landing page.", "Lý do chính là trang đích mới."),
  ("I'll update the dashboard every Monday.", "Em sẽ cập nhật dashboard mỗi thứ Hai."),
  ("Which metric matters most to you?", "Với anh/chị, chỉ số nào quan trọng nhất?"),
 ],
 "dialogues": [
  ("Did we hit our KPI last month?", [
    ("Almost. We reached 92% of the target. We missed it mainly because the first week was slow.", True, "Trả lời trung thực + con số + lý do."),
    ("Yes, almost hit.", False, "Mâu thuẫn ('yes' mà 'almost') và thiếu số liệu."),
    ("We are hit 92%.", False, "Sai thì: 'We hit 92%.' / 'We reached 92%.'"),
  ]),
  ("Why did the conversion rate drop?", [
    ("The checkout page had an error for two days. It's fixed now, and the rate is recovering.", True, "Nguyên nhân + đã xử lý + tình hình hiện tại."),
    ("Because customer don't want buy.", False, "Thiếu 's', thiếu 'to' ('don't want to buy') và không phải phân tích thật."),
    ("It drop a little bit only.", False, "Sai thì ('It dropped') và né câu hỏi 'why'."),
  ]),
  ("What's our revenue compared to last month?", [
    ("It's up 18%, mostly from the flash sale on the 15th.", True, "So sánh bằng % + nguồn tăng trưởng chính."),
    ("More than last month very much.", False, "Trật tự từ kiểu tiếng Việt, không có con số."),
    ("Revenue is increase.", False, "Sai: 'Revenue increased.' / 'Revenue is up.'"),
  ]),
  ("Can you explain this spike on Saturday?", [
    ("Yes. A food blogger shared our video that morning, so traffic tripled.", True, "Giải thích nguyên nhân + mức độ tăng."),
    ("I also don't understand this spike.", False, "Không tìm hiểu trước khi họp; nên nói 'Let me check and get back to you.'"),
    ("Saturday many people online.", False, "Thiếu chủ ngữ giả 'there are' và giải thích quá chung."),
  ]),
  ("Is a 1.5% conversion rate good for us?", [
    ("It's close to the industry benchmark of 1.6%, so it's OK, but we can improve it.", True, "So với mức chuẩn + đánh giá cân bằng."),
    ("1.5% is too small, it's bad.", False, "Kết luận vội, không so sánh với benchmark."),
    ("It is good or not depend on you.", False, "Sai ngữ pháp ('depends') và né trách nhiệm phân tích."),
  ]),
 ],
 "listen": [
  ("Revenue is up fifteen percent month-on-month", ["Revenue", "month-on-month"], "doanh thu so với tháng trước"),
  ("Our conversion rate dropped to one point seven percent", ["conversion", "dropped"], "tỉ lệ chuyển đổi"),
  ("You can see all the numbers on the dashboard", ["numbers", "dashboard"], "xem số liệu"),
  ("The bounce rate on this page is too high", ["bounce", "high"], "tỉ lệ thoát"),
  ("This month we reached ninety-five percent of our KPI. Revenue grew by twelve percent. Most orders came from mobile.", ["KPI", "grew", "mobile"], "tóm tắt KPI tháng"),
  ("There was a big spike in traffic on Saturday. A famous blogger shared our video. Sales doubled that weekend.", ["spike", "blogger", "doubled"], "giải thích số liệu tăng vọt"),
 ],
})

# ───────────────────────── 5. Vận hành gian hàng TMĐT ─────────────────────────
PHASES.append({
 "title": "Vận hành gian hàng TMĐT",
 "vocab": [
  ("listing", "/ˈlɪstɪŋ/", "n", "trang sản phẩm đăng bán trên sàn", "Please add more photos to the <b>listing</b>.", "Thêm ảnh vào trang sản phẩm giúp em nhé."),
  ("SKU", "/ˌes keɪ ˈjuː/", "n", "mã hàng (mỗi biến thể màu/size một mã)", "This T-shirt has 12 <b>SKUs</b>: four colours and three sizes.", "Áo thun này có 12 mã hàng: bốn màu và ba size."),
  ("inventory", "/ˈɪnvəntri/", "n", "hàng tồn kho", "We check the <b>inventory</b> every morning before the sale.", "Sáng nào bên mình cũng kiểm tồn kho trước giờ sale.", "在庫", "zaiko"),
  ("storefront", "/ˈstɔːfrʌnt/", "n", "trang chủ gian hàng", "Let's update the <b>storefront</b> banner for Tết.", "Mình cập nhật banner trang chủ gian hàng cho Tết nhé."),
  ("product description", "/ˌprɒdʌkt dɪˈskrɪpʃn/", "n", "mô tả sản phẩm", "The <b>product description</b> doesn't mention the size.", "Mô tả sản phẩm không ghi kích thước.", "商品説明", "shōhin setsumei"),
  ("out of stock", "/ˌaʊt əv ˈstɒk/", "phr", "hết hàng", "The blue one is <b>out of stock</b> until Friday.", "Màu xanh hết hàng đến thứ Sáu.", "在庫切れ", "zaikogire"),
  ("fulfilment", "/fʊlˈfɪlmənt/", "n", "xử lý đơn (đóng gói, giao hàng)", "The platform handles <b>fulfilment</b> for our best-sellers.", "Sàn lo khâu đóng gói, giao hàng cho các mặt hàng bán chạy của mình."),
  ("shipping fee", "/ˈʃɪpɪŋ fiː/", "n", "phí vận chuyển", "The <b>shipping fee</b> to Hà Nội is 25,000 dong.", "Phí vận chuyển ra Hà Nội là 25.000 đồng.", "送料", "sōryō"),
  ("marketplace", "/ˈmɑːkɪtpleɪs/", "n", "sàn thương mại điện tử", "We sell on two <b>marketplaces</b> and our own website.", "Bên mình bán trên hai sàn và website riêng."),
  ("checkout", "/ˈtʃekaʊt/", "n", "bước thanh toán", "Many customers leave at <b>checkout</b> because of the shipping fee.", "Nhiều khách bỏ đi ở bước thanh toán vì phí vận chuyển."),
 ],
 "phrases": [
  ("I've updated the photos and the product description.", "Em đã cập nhật ảnh và mô tả sản phẩm."),
  ("This item is out of stock. We'll restock next week.", "Mặt hàng này đang hết. Tuần sau bên em nhập thêm."),
  ("Please double-check the SKU before you pack the order.", "Kiểm tra lại mã hàng trước khi đóng gói đơn nhé."),
  ("We have 20 pending orders to ship today.", "Hôm nay mình còn 20 đơn chờ gửi đi."),
  ("The listing was hidden because of a wrong category.", "Trang sản phẩm bị ẩn vì chọn sai danh mục."),
  ("Our store rating is 4.8 stars.", "Điểm đánh giá gian hàng của mình là 4,8 sao."),
  ("Orders placed before 3 p.m. ship the same day.", "Đơn đặt trước 3 giờ chiều được gửi đi ngay trong ngày."),
  ("The inventory on the website doesn't match the warehouse.", "Tồn kho trên website không khớp với kho thực tế."),
  ("Can we offer free shipping on orders over 300,000 dong?", "Mình miễn phí vận chuyển cho đơn trên 300.000 đồng được không?"),
 ],
 "dialogues": [
  ("Why was our listing hidden on Shopza?", [
    ("We used the wrong category. I've changed it, and it should be back within 24 hours.", True, "Nguyên nhân + đã sửa + thời gian dự kiến."),
    ("Shopza hide it, I don't know why.", False, "Sai thì ('hid') và chưa tìm hiểu nguyên nhân."),
    ("Because listing is wrong.", False, "Quá chung chung, thiếu mạo từ; phải nói sai ở đâu."),
  ]),
  ("A customer says the size chart is missing. Can you fix it?", [
    ("Sure. I'll add the size chart to the description and the photos this afternoon.", True, "Nhận việc + cách sửa + thời gian cụ thể."),
    ("Customer can ask in chat.", False, "Thiếu mạo từ ('The customer') và đẩy việc cho khách thay vì sửa trang sản phẩm."),
    ("OK, I fix it after.", False, "Thiếu 'will'; 'after' đứng cuối câu vừa sai vừa mơ hồ: 'I'll fix it this afternoon.'"),
  ]),
  ("How much stock do we have for the red bag?", [
    ("We have 45 left in the warehouse, enough for about three days.", True, "Con số tồn kho + ước lượng đủ bán bao lâu."),
    ("Red bag still have.", False, "Dịch từng chữ 'vẫn còn': 'We still have some red bags.' — và cần số lượng."),
    ("Many, many.", False, "Không có số liệu — vận hành cần con số chính xác."),
  ]),
  ("We sent the wrong colour to a customer. What happened?", [
    ("The two SKUs look very similar. I'm sorry. I'll send the right one today and label the shelves clearly.", True, "Nhận lỗi + khắc phục ngay + phòng ngừa lần sau."),
    ("The packer make mistake, not me.", False, "Sai chia ('made') và đổ lỗi cho người khác."),
    ("Customer can use it, same same.", False, "Coi nhẹ lỗi, không chuyên nghiệp."),
  ]),
  ("Can we ship this order today?", [
    ("Yes, if we pack it before 3 p.m. The courier comes at 4.", True, "Trả lời có điều kiện + mốc giờ rõ."),
    ("Maybe can, maybe cannot.", False, "Thiếu chủ ngữ và mơ hồ; nêu điều kiện cụ thể."),
    ("Yes, we can shipping today.", False, "Sau 'can' dùng nguyên thể: 'We can ship it today.'"),
  ]),
 ],
 "listen": [
  ("Please add more photos to the listing", ["photos", "listing"], "cập nhật trang sản phẩm"),
  ("The blue one is out of stock until Friday", ["stock", "Friday"], "hết hàng"),
  ("Check the SKU before you pack the order", ["SKU", "pack"], "đóng gói đơn hàng"),
  ("The shipping fee is twenty-five thousand dong", ["shipping", "twenty-five"], "phí vận chuyển"),
  ("We have thirty orders to ship today. The courier comes at four. Please pack everything before three thirty.", ["thirty", "courier", "pack"], "đóng gói đơn trong ngày"),
  ("Our listing was hidden this morning. We chose the wrong category. I've fixed it, and it should be back tonight.", ["hidden", "category", "tonight"], "sự cố trang sản phẩm"),
 ],
})

# ───────────────────────── 6. Khuyến mãi & flash sale ─────────────────────────
PHASES.append({
 "title": "Khuyến mãi & flash sale",
 "vocab": [
  ("voucher", "/ˈvaʊtʃə/", "n", "mã giảm giá, voucher", "New customers get a 50,000-dong <b>voucher</b>.", "Khách mới được tặng voucher 50.000 đồng.", "クーポン", "kūpon"),
  ("flash sale", "/ˈflæʃ seɪl/", "n", "giảm giá chớp nhoáng (khung giờ ngắn)", "The <b>flash sale</b> starts at midnight and lasts two hours.", "Flash sale bắt đầu lúc 0 giờ và kéo dài hai tiếng."),
  ("promo code", "/ˈprəʊməʊ kəʊd/", "n", "mã khuyến mãi", "Enter the <b>promo code</b> TET10 at checkout.", "Nhập mã khuyến mãi TET10 ở bước thanh toán."),
  ("free shipping", "/ˌfriː ˈʃɪpɪŋ/", "n", "miễn phí vận chuyển", "We offer <b>free shipping</b> on orders over 300,000 dong.", "Bên mình miễn phí vận chuyển cho đơn trên 300.000 đồng.", "送料無料", "sōryō muryō"),
  ("bundle deal", "/ˈbʌndl diːl/", "n", "ưu đãi mua combo", "The <b>bundle deal</b> is three bottles for the price of two.", "Ưu đãi combo là mua ba chai trả tiền hai chai."),
  ("minimum spend", "/ˌmɪnɪməm ˈspend/", "n", "giá trị đơn tối thiểu", "The voucher has a <b>minimum spend</b> of 200,000 dong.", "Voucher áp dụng cho đơn tối thiểu 200.000 đồng."),
  ("countdown", "/ˈkaʊntdaʊn/", "n", "đồng hồ đếm ngược", "Put a <b>countdown</b> timer on the banner.", "Gắn đồng hồ đếm ngược lên banner."),
  ("redeem", "/rɪˈdiːm/", "v", "dùng, đổi (voucher, điểm)", "Only 30% of customers <b>redeemed</b> their vouchers.", "Chỉ 30% khách đã dùng voucher của họ."),
  ("limited-time", "/ˌlɪmɪtɪd ˈtaɪm/", "adj", "có thời hạn, trong thời gian có hạn", "This is a <b>limited-time</b> offer for members.", "Đây là ưu đãi có thời hạn dành cho thành viên.", "期間限定", "kikan gentei"),
  ("add to cart", "/ˌæd tə ˈkɑːt/", "phr v", "thêm vào giỏ hàng", "Many shoppers <b>add to cart</b> but never check out.", "Nhiều khách thêm vào giỏ nhưng không thanh toán.", "カートに入れる", "kāto ni ireru"),
 ],
 "phrases": [
  ("The flash sale starts at midnight on the 11th.", "Flash sale bắt đầu lúc 0 giờ ngày 11."),
  ("Customers can use only one voucher per order.", "Mỗi đơn khách chỉ dùng được một voucher."),
  ("The promo code expires on Sunday.", "Mã khuyến mãi hết hạn vào Chủ nhật."),
  ("Do we have enough stock for the sale?", "Mình có đủ hàng cho đợt sale không?"),
  ("Let's set a minimum spend of 250,000 dong.", "Mình đặt giá trị đơn tối thiểu 250.000 đồng nhé."),
  ("We shouldn't lose money on this discount.", "Mình không được để lỗ vì mức giảm giá này."),
  ("We got 1,200 orders in the first hour.", "Giờ đầu tiên mình có 1.200 đơn."),
  ("Let's remind people with a countdown post.", "Mình nhắc khách bằng bài đăng đếm ngược nhé."),
  ("The bundle deal is our best-seller this week.", "Combo là mặt hàng bán chạy nhất tuần này."),
 ],
 "dialogues": [
  ("Are we ready for the 11.11 flash sale?", [
    ("Almost. The vouchers are set up. We're still waiting for 300 units from the warehouse.", True, "Tình trạng chung + việc đã xong + việc còn chờ."),
    ("Ready already, don't worry.", False, "Chủ quan, không nêu chi tiết để sếp kiểm tra."),
    ("We are prepare.", False, "Sai: 'We're preparing.' / 'We're ready.'"),
  ]),
  ("A customer says the promo code doesn't work.", [
    ("Let me check. The code needs a minimum spend of 200,000 dong. I'll explain that to her.", True, "Kiểm tra + tìm ra điều kiện + giải thích cho khách."),
    ("She typed wrong, sure.", False, "Đổ lỗi cho khách khi chưa kiểm tra."),
    ("Code is not work.", False, "Sai: 'The code doesn't work.' (không dùng 'is' + động từ nguyên thể)."),
  ]),
  ("How much discount should we give?", [
    ("I'd suggest 15%. Anything higher and we'll lose money on the small items.", True, "Đề xuất con số + lý do về lợi nhuận."),
    ("50% for everything, customers will love it.", False, "Không tính đến lợi nhuận — dễ bán lỗ."),
    ("Discount how much you want.", False, "Trật tự từ kiểu tiếng Việt và né trách nhiệm đề xuất."),
  ]),
  ("How did the flash sale go?", [
    ("Great. We got 2,000 orders in two hours, 30% more than last time.", True, "Kết quả + so sánh với lần trước."),
    ("It go very well.", False, "Sai thì: 'It went very well.'"),
    ("Many order, the team very tired.", False, "Thiếu 's', thiếu động từ và thiếu số liệu cụ thể."),
  ]),
  ("Can we add free shipping to this sale?", [
    ("Yes, but only for orders over 300,000 dong, or it will cost too much.", True, "Đồng ý có điều kiện + lý do chi phí."),
    ("Free shipping is free, why not?", False, "Hiểu sai: miễn phí cho khách nhưng shop vẫn phải trả phí."),
    ("Yes, we can add free ship.", False, "'Free ship' là cách nói kiểu Việt; tiếng Anh: 'free shipping'."),
  ]),
 ],
 "listen": [
  ("The flash sale starts at midnight", ["flash", "midnight"], "giờ mở flash sale"),
  ("Use the promo code at checkout", ["promo", "checkout"], "dùng mã khuyến mãi"),
  ("We offer free shipping on orders over three hundred thousand dong", ["free", "orders"], "điều kiện miễn phí vận chuyển"),
  ("Only one voucher can be used per order", ["voucher", "order"], "quy định voucher"),
  ("The sale starts at nine tonight. Every item is twenty percent off for two hours. Don't forget to use our voucher.", ["nine", "twenty", "voucher"], "thông báo khuyến mãi"),
  ("We got two thousand orders in the first hour. The bundle deal was the best-seller. We are almost out of stock.", ["thousand", "bundle", "stock"], "kết quả flash sale"),
 ],
})

# ───────────────────────── 7. Làm việc với agency & KOL ─────────────────────────
PHASES.append({
 "title": "Làm việc với agency & KOL",
 "vocab": [
  ("influencer", "/ˈɪnfluənsə/", "n", "người có ảnh hưởng (influencer)", "We're working with three beauty <b>influencers</b> this month.", "Tháng này bên mình hợp tác với ba influencer làm đẹp.", "インフルエンサー", "infuruensā"),
  ("agency", "/ˈeɪdʒənsi/", "n", "công ty dịch vụ (agency) quảng cáo, truyền thông", "Our <b>agency</b> will send three ideas next week.", "Tuần sau agency sẽ gửi ba ý tưởng.", "代理店", "dairiten"),
  ("KOL", "/ˌkeɪ əʊ ˈel/", "n", "người dẫn dắt dư luận (key opinion leader)", "The <b>KOL</b> has 2 million followers on Loopa.", "KOL này có 2 triệu người theo dõi trên Loopa."),
  ("proposal", "/prəˈpəʊzl/", "n", "bản đề xuất", "Please send the <b>proposal</b> with a cost breakdown.", "Vui lòng gửi bản đề xuất kèm bảng chi phí chi tiết.", "提案書", "teiansho"),
  ("rate card", "/ˈreɪt kɑːd/", "n", "bảng giá dịch vụ (booking KOL, quảng cáo)", "Could you send us her <b>rate card</b>?", "Anh/chị gửi bên em bảng giá booking của cô ấy được không?"),
  ("contract", "/ˈkɒntrækt/", "n", "hợp đồng", "The <b>contract</b> says two posts and one video.", "Hợp đồng ghi rõ hai bài đăng và một video.", "契約", "keiyaku"),
  ("sponsored post", "/ˌspɒnsəd ˈpəʊst/", "n", "bài đăng được tài trợ (có trả phí)", "Every <b>sponsored post</b> must say #ad.", "Bài đăng có tài trợ nào cũng phải ghi #ad."),
  ("collaboration", "/kəˌlæbəˈreɪʃn/", "n", "sự hợp tác", "We'd love to discuss a long-term <b>collaboration</b>.", "Bên em rất muốn bàn về hợp tác lâu dài."),
  ("revision", "/rɪˈvɪʒn/", "n", "lần chỉnh sửa", "The price includes two rounds of <b>revisions</b>.", "Giá đã bao gồm hai lần chỉnh sửa."),
  ("brand guidelines", "/ˌbrænd ˈɡaɪdlaɪnz/", "n", "bộ quy chuẩn thương hiệu (logo, màu, giọng văn)", "Please follow our <b>brand guidelines</b> for colours and fonts.", "Vui lòng làm theo bộ quy chuẩn thương hiệu về màu sắc và phông chữ."),
 ],
 "phrases": [
  ("Thanks for the proposal. We have a few comments.", "Cảm ơn bản đề xuất. Bên em có vài góp ý."),
  ("Could you send us her rate card and audience data?", "Anh/chị gửi bên em bảng giá và dữ liệu người theo dõi của cô ấy được không?"),
  ("The logo in this video is too small.", "Logo trong video này nhỏ quá."),
  ("Please follow our brand guidelines for the colours.", "Vui lòng làm theo bộ quy chuẩn thương hiệu về màu sắc."),
  ("We need the final version by Thursday noon.", "Bên em cần bản cuối chậm nhất trưa thứ Năm."),
  ("This is the last round of revisions.", "Đây là lần chỉnh sửa cuối cùng."),
  ("Can the influencer post it on Saturday evening instead?", "Influencer đổi sang đăng vào tối thứ Bảy được không?"),
  ("Please don't mention any competitors in the video.", "Vui lòng không nhắc đến đối thủ nào trong video."),
  ("Let's review the contract before we sign.", "Mình rà lại hợp đồng trước khi ký nhé."),
  ("We're really happy with the results. Thank you!", "Bên em rất hài lòng với kết quả. Cảm ơn anh/chị!"),
 ],
 "dialogues": [
  ("Here's the first draft of the video. What do you think?", [
    ("Thanks, it looks great. Just two changes: the logo is too small, and the music is too loud.", True, "Khen trước + góp ý cụ thể, có đánh số."),
    ("Not good. Do again.", False, "Cộc lốc, không nói sai ở đâu để agency sửa."),
    ("I think it's OK maybe, but I don't like.", False, "Mơ hồ và thiếu tân ngữ: 'I don't like it.' — phải nói rõ không thích điểm nào."),
  ]),
  ("The influencer wants 40 million dong for one video.", [
    ("That's above our budget. Could she do one video and two stories for 30 million?", True, "Nói rõ vượt ngân sách + đề xuất gói khác để thương lượng."),
    ("Too expensive! She is not worth.", False, "Thiếu 'it' ('not worth it') và thiếu tôn trọng đối tác."),
    ("OK, we pay.", False, "Đồng ý ngay không thương lượng, lại thiếu 'will'."),
  ]),
  ("Can we post the video one day late?", [
    ("I'm afraid not. It's linked to our flash sale. Could we keep the original date?", True, "Từ chối lịch sự + lý do + đề nghị giữ lịch."),
    ("No! The contract say Friday.", False, "Sai chia ('says') và giọng gay gắt với đối tác."),
    ("Late one day is not problem.", False, "Trật tự từ kiểu Việt và đồng ý bừa dù ảnh hưởng đợt sale."),
  ]),
  ("Do we need to say it's a sponsored post?", [
    ("Yes. Please add #ad in the caption. It's in the contract.", True, "Trả lời rõ + hướng dẫn cụ thể + căn cứ hợp đồng."),
    ("No need, customers don't know.", False, "Sai đạo đức nghề: bài có tài trợ phải công khai."),
    ("Yes, must say.", False, "Thiếu chủ ngữ: 'Yes, you must say it.' / 'Yes, please add #ad.'"),
  ]),
  ("When can you give us feedback on the proposal?", [
    ("By Wednesday. I need to check the numbers with my manager first.", True, "Hẹn thời điểm + lý do."),
    ("When I have time.", False, "Mơ hồ, làm đối tác không lên được kế hoạch."),
    ("I will feedback you Wednesday.", False, "'Feedback' không dùng như động từ: 'I'll give you feedback on Wednesday.'"),
  ]),
 ],
 "listen": [
  ("Please send the proposal by Friday", ["proposal", "Friday"], "hạn gửi đề xuất"),
  ("The logo in the video is too small", ["logo", "small"], "góp ý video"),
  ("Could you send us her rate card", ["send", "rate"], "hỏi bảng giá KOL"),
  ("Every sponsored post must include the hashtag ad", ["sponsored", "hashtag"], "quy định bài tài trợ"),
  ("Thanks for the first draft. The story is great. Could you make the logo bigger and change the music?", ["draft", "logo", "music"], "góp ý bản nháp"),
  ("We'd like to work with three influencers in May. Each one will post one video and two stories. Please send their rate cards.", ["three", "video", "rate"], "booking influencer"),
 ],
})

# ───────────────────────── 8. Đánh giá & phản hồi khách hàng ─────────────────────────
PHASES.append({
 "title": "Đánh giá & phản hồi khách hàng",
 "vocab": [
  ("review", "/rɪˈvjuː/", "n", "bài đánh giá (của khách)", "She left a long <b>review</b> with photos.", "Chị ấy để lại bài đánh giá dài kèm ảnh.", "レビュー", "rebyū"),
  ("rating", "/ˈreɪtɪŋ/", "n", "điểm đánh giá (số sao)", "Our store <b>rating</b> dropped to 4.6.", "Điểm đánh giá của gian hàng giảm xuống 4,6.", "評価", "hyōka"),
  ("feedback", "/ˈfiːdbæk/", "n", "phản hồi, góp ý", "Thank you for your <b>feedback</b>.", "Cảm ơn anh/chị đã góp ý."),
  ("negative", "/ˈneɡətɪv/", "adj", "tiêu cực, không tốt", "We got two <b>negative</b> reviews about the packaging.", "Mình bị hai đánh giá tiêu cực về bao bì."),
  ("respond", "/rɪˈspɒnd/", "v", "trả lời, phản hồi", "We <b>respond</b> to every review within 24 hours.", "Bên mình trả lời mọi đánh giá trong vòng 24 giờ."),
  ("five-star", "/ˌfaɪv ˈstɑː/", "adj", "năm sao", "Most of our reviews are <b>five-star</b>.", "Phần lớn đánh giá của mình là năm sao."),
  ("refund", "/ˈriːfʌnd/", "n", "khoản hoàn tiền", "The customer asked for a full <b>refund</b>.", "Khách yêu cầu hoàn tiền toàn bộ.", "返金", "henkin"),
  ("return", "/rɪˈtɜːn/", "n/v", "sự trả hàng; trả hàng", "<b>Returns</b> are free within seven days.", "Trả hàng miễn phí trong vòng bảy ngày.", "返品", "henpin"),
  ("customer satisfaction", "/ˌkʌstəmə ˌsætɪsˈfækʃn/", "n", "mức độ hài lòng của khách hàng", "<b>Customer satisfaction</b> went up after we changed couriers.", "Mức độ hài lòng của khách tăng sau khi đổi đơn vị vận chuyển.", "顧客満足度", "kokyaku manzokudo"),
  ("reputation", "/ˌrepjuˈteɪʃn/", "n", "uy tín, danh tiếng", "One bad reply can hurt our <b>reputation</b>.", "Một câu trả lời tệ có thể làm hỏng uy tín của mình."),
 ],
 "phrases": [
  ("Thank you for your review. We're glad you like it.", "Cảm ơn anh/chị đã đánh giá. Bên em rất vui vì anh/chị thích sản phẩm."),
  ("We're sorry the item arrived damaged.", "Bên em rất tiếc vì sản phẩm đến tay anh/chị bị hỏng."),
  ("Could you send us a photo of the product?", "Anh/chị gửi giúp bên em ảnh sản phẩm được không ạ?"),
  ("We'll send you a replacement today.", "Hôm nay bên em sẽ gửi sản phẩm thay thế."),
  ("You can return it for free within seven days.", "Anh/chị có thể trả hàng miễn phí trong vòng bảy ngày."),
  ("Your refund will arrive in three to five working days.", "Tiền hoàn sẽ về trong ba đến năm ngày làm việc."),
  ("Most negative reviews are about late delivery.", "Phần lớn đánh giá tiêu cực là về giao hàng trễ."),
  ("Let's reply to this review publicly and then message her.", "Mình trả lời đánh giá này công khai rồi nhắn riêng cho chị ấy nhé."),
  ("We've shared your feedback with our product team.", "Bên em đã chuyển góp ý của anh/chị cho đội sản phẩm."),
 ],
 "dialogues": [
  ("We got a one-star review about a broken bottle. How should we reply?", [
    ("Let's apologise, offer a replacement and ask her to message us with her order number.", True, "Đủ ba bước: xin lỗi, giải pháp, chuyển sang kênh riêng."),
    ("Tell her it's the courier's fault.", False, "Đổ lỗi công khai làm khách và người đọc mất thiện cảm."),
    ("We say sorry and don't care.", False, "Thiếu giải pháp; 'don't care' còn thể hiện thái độ tệ."),
  ]),
  ("A customer wants a refund. The product is fine but she doesn't like the colour.", [
    ("Our policy allows returns within seven days if the item is unused. Let's check the date and help her.", True, "Dựa vào chính sách + hành động cụ thể."),
    ("She don't like is her problem.", False, "Sai chia ('doesn't') và thái độ đẩy khách đi."),
    ("OK, refund all, no need to check.", False, "Hoàn tiền không kiểm tra điều kiện — dễ bị lợi dụng."),
  ]),
  ("Why did our rating drop this month?", [
    ("We had eight late deliveries during the sale. Most negative reviews mention delivery.", True, "Nguyên nhân kèm số liệu + bằng chứng từ review."),
    ("Because some customers is difficult.", False, "Sai chia ('are') và đổ lỗi cho khách."),
    ("Rating drop because review bad.", False, "Thiếu động từ/mạo từ và lặp lại câu hỏi, không phân tích."),
  ]),
  ("A customer left a five-star review. Should we reply?", [
    ("Yes. A short thank-you shows we care. I'll reply this afternoon.", True, "Đồng ý + lý do + thời gian."),
    ("No need, she already happy.", False, "Thiếu 'is' và bỏ lỡ cơ hội giữ chân khách."),
    ("Yes, we reply thanks you.", False, "Sai: 'We'll reply and thank her.' ('thanks you' là sai)."),
  ]),
  ("Can you summarise the customer feedback from last month?", [
    ("Sure. People love the taste, but many say the packaging is hard to open.", True, "Tóm tắt cân bằng: điểm khen + điểm chê chính."),
    ("Sure. Feedback is many, I send you all.", False, "Không tóm tắt; 'feedback' không đếm được, không dùng 'many'."),
    ("Customers is happy, no problem.", False, "Sai chia ('are') và tóm tắt thiếu trung thực."),
  ]),
 ],
 "listen": [
  ("Thank you for your review", ["Thank", "review"], "cảm ơn đánh giá"),
  ("Our store rating dropped to four point six", ["rating", "dropped"], "điểm đánh giá gian hàng"),
  ("You can return it within seven days", ["return", "seven"], "chính sách trả hàng"),
  ("Your refund will arrive in five working days", ["refund", "working"], "thời gian hoàn tiền"),
  ("We're sorry your order arrived late. We'll send you a voucher for your next order. Thank you for your patience.", ["sorry", "voucher", "patience"], "trả lời đánh giá tiêu cực"),
  ("Most customers love the new flavour. But many say the bottle is hard to open. We should share this with the product team.", ["flavour", "bottle", "product"], "tóm tắt phản hồi khách hàng"),
 ],
})

# ───────────────────────── 9. Thuyết trình ý tưởng (pitch) ─────────────────────────
PHASES.append({
 "title": "Thuyết trình ý tưởng (pitch)",
 "vocab": [
  ("pitch", "/pɪtʃ/", "n/v", "(buổi) thuyết trình chào ý tưởng", "We have a <b>pitch</b> with a new client on Monday.", "Thứ Hai bên mình có buổi pitch với một khách hàng mới.", "プレゼン", "purezen"),
  ("concept", "/ˈkɒnsept/", "n", "ý tưởng chủ đạo, concept", "The <b>concept</b> is 'small moments at home'.", "Concept là 'những khoảnh khắc nhỏ ở nhà'.", "コンセプト", "konseputo"),
  ("big idea", "/ˌbɪɡ aɪˈdɪə/", "n", "ý tưởng lớn (xuyên suốt chiến dịch)", "Our <b>big idea</b> is to let customers design the packaging.", "Ý tưởng lớn của bên em là để khách tự thiết kế bao bì."),
  ("mood board", "/ˈmuːd bɔːd/", "n", "bảng cảm hứng (ảnh, màu sắc định hướng)", "This <b>mood board</b> shows the colours and style.", "Bảng cảm hứng này thể hiện màu sắc và phong cách."),
  ("tagline", "/ˈtæɡlaɪn/", "n", "khẩu hiệu, câu slogan ngắn", "The <b>tagline</b> is 'Snack smart, live happy'.", "Khẩu hiệu là 'Ăn vặt thông minh, sống vui'.", "キャッチコピー", "kyatchi kopī"),
  ("storyboard", "/ˈstɔːribɔːd/", "n", "kịch bản phân cảnh", "Here's the <b>storyboard</b> for the 30-second video.", "Đây là kịch bản phân cảnh cho video 30 giây.", "絵コンテ", "ekonte"),
  ("rationale", "/ˌræʃəˈnɑːl/", "n", "lý do, cơ sở (của ý tưởng)", "The <b>rationale</b> comes from our survey results.", "Cơ sở của ý tưởng đến từ kết quả khảo sát."),
  ("stand out", "/ˌstænd ˈaʊt/", "phr v", "nổi bật", "Bright colours help us <b>stand out</b> on the shelf.", "Màu sắc tươi sáng giúp mình nổi bật trên kệ."),
  ("call to action", "/ˌkɔːl tə ˈækʃn/", "n", "lời kêu gọi hành động", "The <b>call to action</b> is 'Scan to get a free sample'.", "Lời kêu gọi hành động là 'Quét mã nhận mẫu thử miễn phí'."),
  ("unique selling point", "/juˌniːk ˈselɪŋ pɔɪnt/", "n", "điểm khác biệt độc nhất, lợi điểm bán hàng (USP)", "Our <b>unique selling point</b> is no added sugar.", "Điểm khác biệt độc nhất của mình là không thêm đường."),
 ],
 "phrases": [
  ("Thank you for having us today.", "Cảm ơn anh/chị đã dành thời gian cho bên em hôm nay."),
  ("Let me start with what we learned about your customers.", "Em xin bắt đầu với những gì bên em tìm hiểu được về khách hàng của anh/chị."),
  ("Our big idea is simple.", "Ý tưởng lớn của bên em rất đơn giản."),
  ("This is how the campaign will look on social media.", "Đây là hình dung chiến dịch trên mạng xã hội."),
  ("Why will this work? Because it solves a real pain point.", "Vì sao ý tưởng này hiệu quả? Vì nó giải quyết một nỗi đau thật của khách."),
  ("We expect to reach two million people in six weeks.", "Bên em kỳ vọng tiếp cận hai triệu người trong sáu tuần."),
  ("Here's a quick look at the budget.", "Đây là tóm tắt nhanh về ngân sách."),
  ("That's a great question. Let me explain.", "Câu hỏi rất hay. Để em giải thích."),
  ("We'd love to hear your thoughts.", "Bên em rất muốn nghe ý kiến của anh/chị."),
  ("To sum up, the idea is simple, affordable and easy to share.", "Tóm lại, ý tưởng đơn giản, vừa ngân sách và dễ lan truyền."),
 ],
 "dialogues": [
  ("So, what's your big idea?", [
    ("We want customers to share their own 'small moments' with our tea, using one hashtag.", True, "Nêu ý tưởng gọn trong một câu, có cách thực hiện."),
    ("Our idea is very creative and very new.", False, "Chỉ khen chung chung, không nói ý tưởng là gì."),
    ("Idea is customer share photo with tea.", False, "Thiếu mạo từ, số nhiều: 'The idea is that customers share photos…'"),
  ]),
  ("Why do you think this will work?", [
    ("Our survey shows young people love sharing daily moments, and it costs little to produce.", True, "Lập luận bằng dữ liệu + lợi ích chi phí."),
    ("Because we think so.", False, "Không có lý do — pitch cần cơ sở thuyết phục."),
    ("Because young people like, they share.", False, "Thiếu tân ngữ và liên từ: 'Young people like it, so they'll share it.'"),
  ]),
  ("The budget looks a bit high for us.", [
    ("I understand. We can start with the social media part only, which is about 60% of the cost.", True, "Ghi nhận + đưa phương án nhỏ hơn với con số."),
    ("No, it is not high, it is normal.", False, "Phủ nhận cảm nhận của khách, thiếu tinh thần hợp tác."),
    ("OK, we make it cheap.", False, "Hứa mơ hồ, thiếu 'will' và không nói bớt phần nào."),
  ]),
  ("How is this different from what our competitors are doing?", [
    ("They focus on price. We focus on emotion, so the brand will stand out.", True, "So sánh rõ ràng + lợi ích thương hiệu."),
    ("Competitors are boring, we are better.", False, "Chê đối thủ, không chỉ ra điểm khác biệt thật."),
    ("It's different very much.", False, "Trật tự sai và không nói khác ở đâu: 'It's very different because…'"),
  ]),
  ("Can you send us the deck after the meeting?", [
    ("Of course. I'll email it this afternoon with the timeline and costs.", True, "Đồng ý + thời gian + nội dung kèm theo."),
    ("Of course, I send it after.", False, "Thiếu 'will' và mốc thời gian: 'I'll send it this afternoon.'"),
    ("The deck is secret, sorry.", False, "Không hợp lý — gửi lại tài liệu sau pitch là chuyện bình thường."),
  ]),
 ],
 "listen": [
  ("Our big idea is very simple", ["big", "simple"], "mở đầu ý tưởng"),
  ("The tagline is short and easy to remember", ["tagline", "remember"], "giới thiệu khẩu hiệu"),
  ("Here's the storyboard for the main video", ["storyboard", "video"], "trình bày kịch bản phân cảnh"),
  ("Bright colours will help us stand out", ["colours", "stand"], "lý do chọn màu"),
  ("Thank you for having us today. First, we'll share what we learned about your customers. Then we'll show you our big idea.", ["today", "customers", "idea"], "mở đầu buổi pitch"),
  ("To sum up, the idea is simple and easy to share. We expect to reach two million people. We'd love to hear your thoughts.", ["simple", "million", "thoughts"], "kết thúc buổi pitch"),
 ],
})

# ───────────────────────── Vai trò (roles) ─────────────────────────
ROLES = {
 "digital": {"label": "Digital marketing · Ads", "emoji": "📱",
  "scenarios": [
   ("dg_perf", "Sếp hỏi hiệu quả ads", "You are my foreign marketing manager. Ask me how our paid ads performed last week. Ask about ROAS, CTR and cost per click, and ask what I will change."),
   ("dg_budget", "Xin thêm ngân sách", "You are the head of marketing. I want more ad budget for the year-end sale. Ask me why, how much, and what results I expect. Agree only if I give clear numbers."),
   ("dg_reject", "Quảng cáo bị từ chối", "You are my manager. Our main ad was rejected by the ad platform the day before a big sale. Ask what happened and what the backup plan is."),
   ("dg_abtest", "Kết quả A/B test", "You are a foreign product owner. Ask me to explain the results of our A/B test on two landing pages, and ask which one we should keep."),
  ],
  "dialogues": [
   ("What was our ROAS last week?", [
     ("It was 4.2, a little higher than the week before.", True, "Con số + so sánh ngắn gọn."),
     ("ROAS is 4.2 last week.", False, "Sai thì: nói về tuần trước dùng 'was'."),
     ("It's good, don't worry.", False, "Né con số — sếp hỏi số thì phải đưa số.")]),
   ("Why did the cost per click go up?", [
     ("Competition is higher before the holiday, and our creative is getting old. I'll launch two new ones tomorrow.", True, "Hai nguyên nhân + hành động cụ thể."),
     ("Cost go up because is holiday.", False, "Thiếu 's'/'went' và thiếu chủ ngữ 'it'."),
     ("I cannot control it.", False, "Buông xuôi, không đề xuất cách tối ưu.")]),
   ("Can we cut the ad spend by 20%?", [
     ("Yes, if we pause the three ads with the lowest ROAS. Sales should drop only a little.", True, "Đồng ý có điều kiện + dự báo ảnh hưởng."),
     ("Cut is not good.", False, "Cộc lốc, không phân tích."),
     ("Yes, we can cutting.", False, "Sau 'can' dùng nguyên thể: 'we can cut it'.")]),
   ("Which audience is working best?", [
     ("Women aged 25 to 34 in Hồ Chí Minh City. Their conversion rate is almost double.", True, "Nêu tệp cụ thể + bằng chứng số liệu."),
     ("Woman is best.", False, "Thiếu số nhiều và quá chung chung."),
     ("All audience is similar.", False, "Sai số nhiều ('All audiences are') và không đúng thực tế nếu chưa phân tích.")]),
   ("The landing page is slow. Who can fix it?", [
     ("I'll ask the web team today and send them the speed report.", True, "Nhận chuyển việc + tài liệu kèm theo + thời gian."),
     ("Not my job.", False, "Đẩy việc, thiếu tinh thần phối hợp."),
     ("I will tell web team fix.", False, "Thiếu mạo từ và 'to': 'I'll ask the web team to fix it.'")]),
   ("What will you test next week?", [
     ("I'll test two headlines: one about price and one about quality.", True, "Kế hoạch thử nghiệm rõ ràng."),
     ("I test many things.", False, "Sai thì và mơ hồ: 'I'll test…' + nêu cụ thể."),
     ("Maybe headline, maybe picture, I don't know.", False, "Thiếu kế hoạch, thiếu mạo từ.")]),
  ]},
 "content": {"label": "Content · Social", "emoji": "✍️",
  "scenarios": [
   ("ct_calendar", "Duyệt lịch nội dung", "You are my foreign content lead. Review my content calendar for next month. Ask about the topics, the posting times and why I chose them."),
   ("ct_crisis", "Bình luận tiêu cực lan rộng", "You are my manager. A negative comment about our product is getting many likes. Ask me how I will reply and how fast."),
   ("ct_live", "Chuẩn bị livestream", "You are the brand manager. I will host tonight's livestream sale. Ask about the products, the vouchers and how I will keep viewers watching."),
   ("ct_idea", "Đề xuất trend mới", "You are my creative director. I want to join a new short-video trend. Ask if it fits our brand and what the risks are."),
  ],
  "dialogues": [
   ("Can you write three captions for the new product?", [
     ("Sure. I'll send them by 3 p.m. Do you want a fun or a serious tone?", True, "Nhận việc + hạn + hỏi rõ giọng văn."),
     ("Sure, how many word?", False, "Thiếu 's' ('words') và nên hỏi về giọng văn, mục đích."),
     ("Captions is easy, no problem.", False, "Sai chia ('are') và coi nhẹ việc.")]),
   ("This post has almost no engagement. Why?", [
     ("It went out at 2 p.m., which is a quiet time for us. Let's repost it at 8 p.m.", True, "Phân tích giờ đăng + đề xuất cụ thể."),
     ("Because people don't like it maybe.", False, "Đoán mơ hồ, không có dữ liệu."),
     ("It no engagement because bad luck.", False, "Thiếu động từ và lý do không chuyên nghiệp.")]),
   ("A customer says our video is misleading.", [
     ("Let's reply politely, explain the facts, and edit the video if we made a mistake.", True, "Lắng nghe + làm rõ + sẵn sàng sửa sai."),
     ("He is wrong, ignore him.", False, "Phớt lờ phản hồi dễ khiến vấn đề lan rộng."),
     ("We delete comment, finish.", False, "Thiếu mạo từ; xoá bình luận thường làm khủng hoảng tệ hơn.")]),
   ("How long should our videos be?", [
     ("Under 30 seconds. Our data shows most people stop watching after that.", True, "Đề xuất rõ + dựa trên dữ liệu."),
     ("Long is better, more information.", False, "Trái với dữ liệu xem video ngắn phổ biến."),
     ("Should be short short.", False, "Lặp từ kiểu tiếng Việt, thiếu chủ ngữ: 'They should be short.'")]),
   ("Can we use this song in our video?", [
     ("Only if we have the licence. I'll check with the platform's music library first.", True, "Chú ý bản quyền + hành động kiểm tra."),
     ("Yes, everybody uses it.", False, "Người khác dùng không có nghĩa là mình được dùng — rủi ro bản quyền."),
     ("I think no problem.", False, "Thiếu cấu trúc: 'I don't think it's a problem.' — và chưa kiểm tra bản quyền.")]),
   ("Are you ready for tonight's livestream?", [
     ("Yes. The products, the vouchers and the script are ready. We start at 8.", True, "Liệt kê những gì đã sẵn sàng + giờ bắt đầu."),
     ("Ready 100%!", False, "Thiếu chủ ngữ, động từ và không có chi tiết để kiểm tra."),
     ("I'm still prepare.", False, "Sai: 'I'm still preparing.'")]),
  ]},
 "ecom": {"label": "Vận hành sàn TMĐT", "emoji": "🛒",
  "scenarios": [
   ("ec_sale", "Chuẩn bị ngày sale lớn", "You are my foreign e-commerce manager. The 12.12 sale is in three days. Ask about stock, vouchers, listings and how many orders we can ship per day."),
   ("ec_wrong", "Giao nhầm hàng hàng loạt", "You are my manager. Twenty customers received the wrong size yesterday. Ask what happened, how we will fix it and how to stop it happening again."),
   ("ec_platform", "Làm việc với quản lý sàn", "You are an account manager from the Shopza marketplace. Tell me our shop's late-delivery rate is too high and ask for an improvement plan."),
   ("ec_new", "Đưa sản phẩm mới lên sàn", "You are the brand owner. Ask me what I need from you to list a new product: photos, descriptions, prices and stock."),
  ],
  "dialogues": [
   ("How many orders did we get yesterday?", [
     ("We got 640 orders. About 90% have already shipped.", True, "Con số + tình trạng xử lý đơn."),
     ("Yesterday have 640 orders.", False, "Dịch từng chữ 'hôm qua có': 'We got 640 orders yesterday.'"),
     ("A lot, I'm very busy.", False, "Không có số liệu, chỉ than bận.")]),
   ("The listing photos look old. Can you update them?", [
     ("Yes. I'll book a photo shoot this week and update all the listings by Monday.", True, "Kế hoạch cụ thể + hạn hoàn thành."),
     ("Photos is still OK.", False, "Sai chia ('are') và bác bỏ yêu cầu không có lý do."),
     ("OK, update after.", False, "Thiếu chủ ngữ và thời gian cụ thể.")]),
   ("We're almost out of stock on the best-seller.", [
     ("I'll ask the warehouse for 500 more units and set a purchase limit of two per customer.", True, "Xử lý hai hướng: bổ sung hàng + giới hạn mua."),
     ("Good, it means we sell well.", False, "Bỏ qua rủi ro hết hàng giữa đợt sale."),
     ("Stock is finish.", False, "Sai: 'We're out of stock.' / 'The stock has run out.'")]),
   ("Why is our late-delivery rate so high?", [
     ("One courier had problems last week. We've moved most orders to another courier.", True, "Nguyên nhân + đã hành động."),
     ("Courier is slow, not our fault.", False, "Thiếu mạo từ và đổ lỗi — sàn vẫn tính điểm cho shop."),
     ("Because many order.", False, "Thiếu 's' và quá chung chung.")]),
   ("Can we change the price during the sale?", [
     ("No, the platform locks prices during the campaign. We need to set them before Friday.", True, "Nêu quy định + hạn cần làm."),
     ("Yes, change anytime.", False, "Sai thông tin và thiếu chủ ngữ."),
     ("Price change is can.", False, "Trật tự từ sai: 'We can change the price.'")]),
   ("A customer says the parcel was empty.", [
     ("I'm sorry to hear that. I'll check the packing video and reply to her within two hours.", True, "Đồng cảm + kiểm tra bằng chứng + thời hạn trả lời."),
     ("Impossible, we always pack.", False, "Phủ nhận ngay khi chưa kiểm tra."),
     ("She lie maybe.", False, "Sai chia ('is lying') và nghi ngờ khách thiếu căn cứ.")]),
  ]},
 "brand": {"label": "Brand · Account agency", "emoji": "🎯",
  "scenarios": [
   ("br_brief", "Nhận brief từ khách", "You are a foreign client giving me a brief for a new coffee brand launch. Answer my questions about the target audience, budget and timeline, but only if I ask."),
   ("br_feedback", "Khách chê bản thiết kế", "You are a client who doesn't like our first key visual. Say the colours are too dark and the logo is too small. Expect me to stay positive and agree on next steps."),
   ("br_pitch", "Pitch ý tưởng", "You are the marketing director of a snack brand. I am pitching a campaign idea to you. Ask why it will work, how much it costs and how we will measure results."),
   ("br_late", "Báo trễ tiến độ", "You are an important client. I must tell you that the video will be two days late. Be disappointed at first, then accept if I give a clear new date and a reason."),
  ],
  "dialogues": [
   ("I don't like the colours in this design.", [
     ("Thanks for the feedback. Which colours would you like to see more of?", True, "Ghi nhận + hỏi rõ để sửa đúng ý."),
     ("But the colours is our brand guidelines.", False, "Sai chia ('are') và cãi khách ngay lập tức."),
     ("OK, we change all.", False, "Thiếu 'will' và sửa hết khi chưa hiểu rõ vấn đề.")]),
   ("When will the first draft be ready?", [
     ("By next Tuesday. I'll send you a preview on Friday so you can give early feedback.", True, "Hạn cụ thể + cơ hội góp ý sớm."),
     ("Soon, very soon.", False, "Mơ hồ, khách không lên kế hoạch được."),
     ("Next Tuesday is ready.", False, "Thiếu chủ ngữ: 'It will be ready next Tuesday.'")]),
   ("Can you add two more videos at no extra cost?", [
     ("I'd love to help. The price covers three videos, but I can offer the extra two at a 20% discount.", True, "Giữ phạm vi + đưa ưu đãi hợp lý."),
     ("No, no free.", False, "Cộc lốc, thiếu lịch sự với khách."),
     ("Yes, free for you.", False, "Nhận thêm việc miễn phí, ảnh hưởng lợi nhuận agency.")]),
   ("The video will be late? This is a big problem for us.", [
     ("I'm really sorry. The shoot was delayed by rain. The final video will be ready on Thursday.", True, "Xin lỗi + lý do + ngày mới cụ thể."),
     ("Sorry, but rain is not our fault.", False, "Xin lỗi nửa vời, đổ lỗi thời tiết."),
     ("Sorry, it late two days.", False, "Thiếu động từ: 'It will be two days late.'")]),
   ("What's the rationale behind this idea?", [
     ("Our research shows that your customers buy snacks as small rewards after work.", True, "Lý do dựa trên nghiên cứu khách hàng."),
     ("Because it's creative.", False, "Không đưa ra cơ sở thuyết phục."),
     ("Rationale is our team like it.", False, "Thiếu mạo từ/'s' và lý do chủ quan.")]),
   ("Can we have a call tomorrow to discuss the plan?", [
     ("Sure. Does 10 a.m. work for you? I'll send an invite.", True, "Đồng ý + đề xuất giờ + gửi lời mời."),
     ("Tomorrow OK.", False, "Thiếu chủ ngữ/động từ và không chốt giờ."),
     ("Yes, what time you free?", False, "Sai cấu trúc câu hỏi: 'What time are you free?'")]),
  ]},
}

PACK = {
 "id": "marketing",
 "label": "Marketing · TMĐT",
 "short": "Marketing",
 "emoji": "📣",
 "desc": "Marketing · quảng cáo · vận hành shop online",
 "persona": "a Vietnamese marketing and e-commerce worker",
 "counterpart": "a foreign manager, agency or partner",
 "context": "marketing and e-commerce",
 "core": [3, 11],
 "report": {
  "title": "Báo cáo chiến dịch 60 giây", "short": "Báo cáo chiến dịch", "sub": "Nói như họp marketing 🎙️",
  "steps": [["Results", "Last week the campaign reached …"], ["Insights", "We found that … works better than …"], ["Next", "Next week we will …"]],
  "kind": "campaign performance update",
  "structure": "results and key metrics / insights / next actions",
  "sample": "Last week the Tết campaign reached 1.2 million people, and revenue from ads was 350 million dong with a ROAS of 4.1. We found that short videos had twice the click-through rate of photo ads. Next week we will move 20% of the budget to video and test two new landing pages.",
 },
 "podcast": "Podcast marketing",
 "game_tag": "Game anime: đánh quái số liệu, hạ boss khách khó chiều",
 "reverse_tag": "kiểu marketing",
 "jd_placeholder": "VD: Digital marketing cho thương hiệu mỹ phẩm, chạy ads, báo cáo ROAS cho sếp nước ngoài, làm việc với KOL…",
 "rw_placeholder": "VD: quảng cáo bị từ chối ngay trước flash sale, sếp hỏi phương án",
 "quips": [
  "Campaign is live!",
  "ROAS looking good!",
  "One more A/B test!",
  "Flash sale starts in 3, 2, 1…",
  "Going viral!",
  "Don't forget the hashtag!",
  "Checking the dashboard…",
  "Add to cart!",
  "The client loved the pitch!",
  "Five stars, please!",
 ],
 "ai": [
  ("brief", "Nhận brief chiến dịch", "You are a foreign client giving me a brief for a product launch. Answer my questions about objectives, target audience, budget and timeline. Give details only when I ask clear questions."),
  ("ads", "Báo cáo hiệu quả quảng cáo", "You are my foreign marketing manager. Ask me how our paid ads performed this week: ROAS, CTR, cost per click. Ask one follow-up question about what I will change."),
  ("agency", "Góp ý cho agency", "You are an account manager from our creative agency. You just sent us the first draft of a video. Ask for my feedback and push back politely on one of my comments."),
  ("kol", "Deal giá với KOL", "You are the manager of a popular influencer. Offer one sponsored video for 40 million dong. Negotiate with me, and accept a lower price only if I offer more posts or a longer contract."),
  ("review", "Xử lý đánh giá 1 sao", "You are an unhappy online customer who left a one-star review because your order arrived damaged. Chat with me. Calm down if I apologise and offer a clear solution."),
  ("sale", "Chuẩn bị flash sale", "You are my e-commerce manager. The big flash sale is in two days. Ask me about stock, vouchers, listings and the shipping plan."),
  ("pitch", "Pitch ý tưởng cho khách", "You are the marketing director of a snack brand. I am pitching a campaign idea. Ask about the big idea, why it will work, the cost and how we will measure results."),
  ("report", "Báo cáo nhanh với sếp", "You are my marketing manager. Ask me for a quick campaign update: results, insights and next steps. Ask one follow-up question about my numbers."),
 ],
 "rev": [
  ("Mục tiêu chính của chiến dịch là gì?", "What's the main objective of the campaign?"),
  ("Tệp khách hàng mục tiêu là dân văn phòng trẻ.", "Our target audience is young office workers."),
  ("Quảng cáo sẽ chạy từ sáng mai.", "The ads will go live tomorrow morning."),
  ("Tỉ lệ nhấp tăng lên hai phần trăm.", "The click-through rate went up to two percent."),
  ("Doanh thu tăng 15% so với tháng trước.", "Revenue is up 15% month-on-month."),
  ("Màu xanh đang hết hàng.", "The blue one is out of stock."),
  ("Flash sale bắt đầu lúc nửa đêm.", "The flash sale starts at midnight."),
  ("Mỗi đơn chỉ dùng được một voucher.", "You can use only one voucher per order."),
  ("Logo trong video nhỏ quá.", "The logo in the video is too small."),
  ("Bên em sẽ gửi bản cuối trước thứ Năm.", "We'll send the final version before Thursday."),
  ("Cảm ơn anh/chị đã góp ý.", "Thank you for your feedback."),
  ("Việc đó nằm ngoài phạm vi dự án.", "That's outside the scope of the project."),
  ("Mình tạm dừng quảng cáo này nhé.", "Let's pause this ad."),
  ("Phiên bản B hiệu quả hơn.", "Version B performed better."),
 ],
 "reading": [
  {"t": "Campaign brief", "text": "CAMPAIGN BRIEF – Bamboo Bites Summer Launch\nProduct: new mango rice crackers\nObjective: 5,000 online orders in 6 weeks\nTarget audience: office workers aged 22–35 in Hà Nội and HCMC\nKey message: 'A light snack for busy afternoons'\nBudget: 400 million dong (70% paid ads, 30% influencers)\nLaunch date: June 3", "q": [
    {"q": "What is the objective of the campaign?", "o": ["5,000 new followers", "5,000 online orders", "400 million dong in revenue"], "a": 1},
    {"q": "How much of the budget goes to influencers?", "o": ["30%", "70%", "All of it"], "a": 0}]},
  {"t": "Weekly ads report", "text": "Week 23 – Paid ads summary\nAd spend: 52 million dong (+10% vs last week)\nRevenue from ads: 208 million dong\nROAS: 4.0 (target: 3.5)\nCTR: 1.9% (last week: 1.4%)\nNote: Video ads outperformed photo ads. Photo ads will be paused on Monday.", "q": [
    {"q": "Did the ads meet the ROAS target?", "o": ["Yes, it was higher", "No, it was lower", "It was exactly the same"], "a": 0},
    {"q": "What will happen on Monday?", "o": ["The budget will go up", "Photo ads will stop", "A new video will launch"], "a": 1}]},
  {"t": "Marketplace notice", "text": "Shopza Seller Centre\nDear seller, 3 of your listings have been hidden because the product category is incorrect. Please edit the listings within 48 hours. Listings that are not fixed will be removed. Your shop's late-delivery rate this month is 4.2% (limit: 5%).", "q": [
    {"q": "Why were the listings hidden?", "o": ["The prices were too low", "The category was wrong", "The photos were missing"], "a": 1},
    {"q": "What is true about the late-delivery rate?", "o": ["It is below the limit", "It is above the limit", "It is not measured"], "a": 0}]},
  {"t": "Email from an agency", "text": "Hi Mai,\nThanks for your comments on the video. We've made the logo bigger and changed the music. The price includes one more round of revisions. Could you send your final feedback by Wednesday noon? Then we can deliver the final file on Friday.\nBest,\nTom – Brightwave Agency", "q": [
    {"q": "What did the agency change?", "o": ["The logo and the music", "The script and the actors", "The price and the date"], "a": 0},
    {"q": "When does Tom need Mai's final feedback?", "o": ["Friday", "Wednesday noon", "Monday morning"], "a": 1}]},
  {"t": "Customer review", "text": "★★☆☆☆ 'I love the taste of these crackers, but the bag was open when it arrived. Delivery also took five days. I hope the shop can fix this.' – Reply from Bamboo Bites: 'We're so sorry! We've sent you a new bag and a 30,000-dong voucher for your next order.'", "q": [
    {"q": "What did the customer like?", "o": ["The delivery speed", "The packaging", "The taste"], "a": 2},
    {"q": "What did the shop give the customer?", "o": ["A full refund", "A new bag and a voucher", "Free shipping for a year"], "a": 1}]},
 ],
 "events": [
  ("pitch", "Pitch ý tưởng với khách", "You are the marketing director of a foreign brand. I am pitching a campaign to win your business. Ask about the idea, the budget, the timeline and why my agency is the right choice."),
  ("review", "Họp tổng kết chiến dịch", "You are my regional marketing manager at a campaign review. Ask about results against KPIs, what worked, what didn't and what I learned."),
  ("megasale", "Ngày sale lớn trên sàn", "You are my e-commerce director one day before a big marketplace sale. Ask about stock, vouchers, ads, livestreams and the plan if the website gets too busy."),
  ("kol", "Gặp đối tác KOL", "You are a foreign influencer meeting our brand for a possible collaboration. Ask about the product, what content we want, the fee and the timeline."),
  ("launch", "Ra mắt sản phẩm mới", "You are the product manager of a new skincare line. Ask me how marketing will support the launch: channels, key message, budget and first-month targets."),
  ("interview", "Phỏng vấn vị trí marketing", "You are the hiring manager for a digital marketing role at an international company. Ask about my experience with ads, a campaign I'm proud of and the numbers behind it."),
  ("other", "Khác", ""),
 ],
 "roles": ROLES,
 "phases": PHASES,
}
