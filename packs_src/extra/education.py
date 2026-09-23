# -*- coding: utf-8 -*-
# v4.1 — nội dung làm giàu cho gói education (nối vào cuối gói, xem build.py)
# 8 chặng mới: sự kiện trường · du học & học bổng · ngoại khoá & dã ngoại · học sinh có nhu cầu đặc biệt ·
# đào tạo doanh nghiệp · dự giờ & kiểm định · giáo vụ & học vụ · coi thi & kỳ thi.
# Tên người là tên tự đặt.

PHASES = []

# ───────────────────────── A. Sự kiện trường ─────────────────────────
PHASES.append({
 "title": "Sự kiện trường",
 "vocab": [
  ("open day", "/ˈəʊpən ˌdeɪ/", "n", "ngày hội mở cửa (ngày hội tuyển sinh)", "Our <b>open day</b> is on Saturday from 9 to 12.", "Ngày hội mở cửa của trường là thứ Bảy, từ 9 đến 12 giờ."),
  ("sports day", "/ˈspɔːts ˌdeɪ/", "n", "ngày hội thể thao", "Parents are welcome to watch <b>sports day</b>.", "Phụ huynh được mời đến xem ngày hội thể thao."),
  ("assembly", "/əˈsembli/", "n", "buổi chào cờ, sinh hoạt toàn trường", "We have a whole-school <b>assembly</b> every Monday morning.", "Sáng thứ Hai nào trường cũng có buổi sinh hoạt toàn trường."),
  ("performance", "/pəˈfɔːməns/", "n", "tiết mục biểu diễn, buổi biểu diễn", "Each class will do a short <b>performance</b>.", "Mỗi lớp sẽ có một tiết mục ngắn."),
  ("rehearsal", "/rɪˈhɜːsl/", "n", "buổi tập dượt, tổng duyệt", "The <b>rehearsal</b> is at 2 p.m. in the hall.", "Buổi tổng duyệt lúc 2 giờ chiều ở hội trường."),
  ("graduation", "/ˌɡrædʒuˈeɪʃn/", "n", "lễ tốt nghiệp, sự tốt nghiệp", "The Grade 12 <b>graduation</b> is in June.", "Lễ tốt nghiệp lớp 12 diễn ra vào tháng Sáu."),
  ("ceremony", "/ˈserəməni/", "n", "buổi lễ", "The <b>ceremony</b> starts at 8:30 sharp.", "Buổi lễ bắt đầu đúng 8 giờ 30."),
  ("certificate", "/səˈtɪfɪkət/", "n", "giấy chứng nhận, giấy khen", "Every student will receive a <b>certificate</b>.", "Học sinh nào cũng sẽ nhận giấy chứng nhận."),
  ("stage", "/steɪdʒ/", "n", "sân khấu", "Please don't stand in front of the <b>stage</b>.", "Vui lòng không đứng trước sân khấu."),
  ("invitation", "/ˌɪnvɪˈteɪʃn/", "n", "thư mời, lời mời", "The <b>invitation</b> has all the details about the event.", "Thư mời có đầy đủ thông tin về sự kiện."),
 ],
 "phrases": [
  ("Our open day is on Saturday from 9 to 12.", "Ngày hội mở cửa của trường là thứ Bảy, từ 9 đến 12 giờ."),
  ("Parents are welcome to watch the performance.", "Phụ huynh được mời đến xem buổi biểu diễn."),
  ("The rehearsal is at 2 p.m. in the hall.", "Buổi tổng duyệt lúc 2 giờ chiều ở hội trường."),
  ("Please bring your child to school by 7:30 on sports day.", "Hôm hội thao, phụ huynh cho cháu đến trường trước 7 giờ 30 nhé."),
  ("Each class will perform one song.", "Mỗi lớp sẽ biểu diễn một bài hát."),
  ("Could you help set up the chairs for the ceremony?", "Anh/chị giúp xếp ghế cho buổi lễ được không?"),
  ("Students will receive their certificates on stage.", "Học sinh sẽ lên sân khấu nhận giấy chứng nhận."),
  ("The invitation has all the details.", "Thư mời có đầy đủ thông tin."),
  ("Please stay in your seat when you take photos.", "Khi chụp ảnh, vui lòng ngồi tại chỗ."),
  ("Thank you all for making today so special.", "Cảm ơn mọi người đã làm cho hôm nay thật đặc biệt."),
 ],
 "dialogues": [
  ("What time does the Christmas performance start?", [
    ("It starts at 6 p.m. in the main hall. Please arrive by 5:45 to find a seat.", True, "Giờ + địa điểm + lời khuyên đến sớm."),
    ("Evening, around six maybe.", False, "Mơ hồ — sự kiện cần giờ chính xác."),
    ("Performance start six o'clock.", False, "Sai chia động từ ('starts at'), thiếu mạo từ và địa điểm."),
  ]),
  ("The students forgot their lines in the rehearsal.", [
    ("Let's practise the hard part twice more tomorrow and give them small cards with the key lines.", True, "Giải pháp cụ thể, khả thi."),
    ("They are children, forget is normal.", False, "Sai dạng từ ('forgetting is normal') và không có giải pháp."),
    ("Cancel the show.", False, "Phản ứng quá mức."),
  ]),
  ("Can I take photos during the graduation ceremony?", [
    ("Yes, but please stay in your seat. We'll also share professional photos after the event.", True, "Cho phép có điều kiện + thông tin thêm."),
    ("No photo, school rule.", False, "Cộc lốc, thiếu giải thích."),
    ("You can go on stage and take.", False, "Gây mất trật tự buổi lễ; thiếu tân ngữ ('take photos')."),
  ]),
  ("Is everything ready for the open day?", [
    ("Almost. The classrooms are ready, and the volunteers know their jobs. We're still waiting for the printed brochures.", True, "Tình trạng + việc còn lại."),
    ("Ready ready, no worry.", False, "Lặp từ kiểu tiếng Việt, sai cấu trúc ('don't worry'), không có thông tin."),
    ("I think everything OK maybe.", False, "Thiếu động từ ('everything is OK') và thiếu chắc chắn."),
  ]),
  ("It's raining. Is sports day cancelled?", [
    ("No, it's moved to the indoor gym. The schedule is the same.", True, "Trả lời + thay đổi + lịch giữ nguyên."),
    ("Rain, so no sports.", False, "Sai thông tin, cộc lốc."),
    ("I don't know, ask other teacher.", False, "Đùn đẩy, thiếu mạo từ ('another teacher')."),
  ]),
 ],
 "listen": [
  ("The rehearsal is at two in the hall", ["rehearsal", "hall"], "lịch tổng duyệt"),
  ("Our open day is on Saturday morning", ["open", "Saturday"], "ngày hội mở cửa"),
  ("Students will receive their certificates on stage", ["certificates", "stage"], "trao giấy chứng nhận"),
  ("Please arrive early to find a seat", ["arrive", "seat"], "nhắc đến sớm"),
  ("Good morning, everyone. Welcome to our school assembly. Today we will give certificates to the students of the month.", ["assembly", "certificates", "month"], "buổi sinh hoạt toàn trường"),
  ("Sports day is on Friday. Please wear your house colour and bring a water bottle. The events start at eight.", ["Friday", "colour", "eight"], "thông báo hội thao"),
 ],
})

# ───────────────────────── B. Du học & học bổng ─────────────────────────
PHASES.append({
 "title": "Du học & học bổng",
 "vocab": [
  ("study abroad", "/ˌstʌdi əˈbrɔːd/", "v", "đi du học", "She wants to <b>study abroad</b> after Grade 12.", "Em ấy muốn đi du học sau lớp 12."),
  ("scholarship", "/ˈskɒləʃɪp/", "n", "học bổng", "The <b>scholarship</b> covers half of the tuition.", "Học bổng chi trả một nửa học phí."),
  ("personal statement", "/ˌpɜːsənl ˈsteɪtmənt/", "n", "bài luận cá nhân (trong hồ sơ)", "Your <b>personal statement</b> should tell a real story.", "Bài luận cá nhân của em nên kể một câu chuyện thật."),
  ("transcript", "/ˈtrænskrɪpt/", "n", "bảng điểm, học bạ", "We need your <b>transcripts</b> for the last three years.", "Cần bảng điểm ba năm gần nhất của em."),
  ("recommendation letter", "/ˌrekəmenˈdeɪʃn ˌletə/", "n", "thư giới thiệu", "Your class teacher will write a <b>recommendation letter</b> for you.", "Giáo viên chủ nhiệm sẽ viết thư giới thiệu cho em."),
  ("student visa", "/ˈstjuːdnt ˌviːzə/", "n", "thị thực du học", "Apply for your <b>student visa</b> early — it can take weeks.", "Nộp hồ sơ thị thực du học sớm nhé — có thể mất vài tuần."),
  ("offer letter", "/ˈɒfə ˌletə/", "n", "thư mời nhập học", "You've received an <b>offer letter</b> — congratulations!", "Em đã nhận được thư mời nhập học — chúc mừng em!"),
  ("accommodation", "/əˌkɒməˈdeɪʃn/", "n", "chỗ ở", "First-year students usually live in university <b>accommodation</b>.", "Sinh viên năm nhất thường ở ký túc xá của trường."),
  ("foundation course", "/faʊnˈdeɪʃn ˌkɔːs/", "n", "khoá dự bị đại học", "He'll take a one-year <b>foundation course</b> first.", "Em ấy sẽ học một năm dự bị trước."),
  ("shortlist", "/ˈʃɔːtlɪst/", "v/n", "chọn ra danh sách rút gọn; danh sách rút gọn", "Let's <b>shortlist</b> five universities.", "Mình chọn ra năm trường đại học nhé."),
 ],
 "phrases": [
  ("Which country would you like to study in?", "Em muốn du học ở nước nào?"),
  ("What's your budget for tuition and living costs?", "Ngân sách cho học phí và sinh hoạt phí là bao nhiêu?"),
  ("Your personal statement should show who you are.", "Bài luận cá nhân nên cho thấy em là người như thế nào."),
  ("We need your transcripts for the last three years.", "Cần bảng điểm ba năm gần nhất của em."),
  ("Could you write a recommendation letter for me?", "Thầy/cô viết thư giới thiệu cho em được không ạ?"),
  ("The scholarship covers 50 percent of the tuition.", "Học bổng chi trả 50% học phí."),
  ("The application deadline is 15 January.", "Hạn nộp hồ sơ là ngày 15 tháng Một."),
  ("You've received an offer letter — congratulations!", "Em đã nhận được thư mời nhập học — chúc mừng em!"),
  ("Let's shortlist five universities.", "Mình chọn ra năm trường đại học nhé."),
  ("Please check the visa requirements on the official website.", "Em kiểm tra yêu cầu thị thực trên trang web chính thức nhé."),
 ],
 "dialogues": [
  ("Can you check my personal statement?", [
    ("Of course. Send it to me by Wednesday, and we'll go through it together on Friday.", True, "Đồng ý + hạn gửi + lịch xem cùng."),
    ("OK, I will check grammar only.", False, "Chỉ sửa ngữ pháp là chưa đủ — bài luận cần nội dung và câu chuyện cá nhân."),
    ("Personal statement not important.", False, "Sai — đây là phần quan trọng của hồ sơ; câu thiếu động từ."),
  ]),
  ("How much does it cost to study in Australia for a year?", [
    ("It depends on the city and the course. I'll send you a detailed estimate for three universities, with tuition and living costs.", True, "Không đưa con số bừa + cam kết gửi dự toán chi tiết."),
    ("Very expensive, maybe you can't.", False, "Thiếu tôn trọng, tự đoán khả năng tài chính của phụ huynh."),
    ("Same Vietnam price.", False, "Sai thông tin, thiếu cấu trúc câu."),
  ]),
  ("Do I have a chance of getting a scholarship?", [
    ("Your grades are strong, so you have a good chance. Let's also add your volunteer work and your science project.", True, "Đánh giá có căn cứ + cách tăng cơ hội."),
    ("Sure, you get 100 percent.", False, "Hứa chắc là thiếu trung thực."),
    ("Scholarship only for genius.", False, "Sai và làm học sinh nản; thiếu động từ."),
  ]),
  ("When will your students send their transcripts?", [
    ("We'll send them all by 30 November, translated into English and certified.", True, "Hạn + tình trạng hồ sơ."),
    ("Soon, students are busy.", False, "Mơ hồ, bào chữa."),
    ("Transcripts is in Vietnamese, OK?", False, "Sai chia động từ ('are') và hỏi ngược thay vì trả lời."),
  ]),
  ("I got two offer letters. Which one should I choose?", [
    ("Congratulations! Let's compare the course, the total cost and the scholarship, then talk with your parents.", True, "Chúc mừng + tiêu chí so sánh + cùng phụ huynh quyết định."),
    ("Choose the famous one.", False, "Tiêu chí hời hợt."),
    ("You choose, not my problem.", False, "Thiếu trách nhiệm tư vấn."),
  ]),
 ],
 "listen": [
  ("The application deadline is in January", ["application", "January"], "hạn nộp hồ sơ"),
  ("Could you write a recommendation letter for me", ["recommendation", "letter"], "xin thư giới thiệu"),
  ("The scholarship covers half of the tuition", ["scholarship", "half"], "mức học bổng"),
  ("Let's shortlist five universities", ["shortlist", "universities"], "chọn trường"),
  ("Congratulations on your offer letter. Now you need to accept the offer and pay the deposit. Then we will start your visa application.", ["offer", "deposit", "visa"], "sau khi nhận thư mời nhập học"),
  ("Your personal statement is too general. Tell a real story about your science project. Show why you love this subject.", ["general", "story", "subject"], "góp ý bài luận"),
 ],
})

# ───────────────────────── C. Ngoại khoá & dã ngoại ─────────────────────────
PHASES.append({
 "title": "Ngoại khoá & dã ngoại",
 "vocab": [
  ("extracurricular", "/ˌekstrəkəˈrɪkjələ/", "adj", "ngoại khoá", "We offer over 20 <b>extracurricular</b> activities.", "Trường có hơn 20 hoạt động ngoại khoá."),
  ("club", "/klʌb/", "n", "câu lạc bộ", "The chess <b>club</b> meets on Wednesday afternoons.", "Câu lạc bộ cờ vua sinh hoạt chiều thứ Tư."),
  ("field trip", "/ˈfiːld ˌtrɪp/", "n", "chuyến dã ngoại, tham quan học tập", "Grade 4 is going on a <b>field trip</b> to the museum.", "Lớp 4 sẽ đi tham quan bảo tàng."),
  ("consent form", "/kənˈsent ˌfɔːm/", "n", "giấy đồng ý (của phụ huynh)", "Please sign the <b>consent form</b> and return it by Tuesday.", "Phụ huynh ký giấy đồng ý và gửi lại trước thứ Ba nhé."),
  ("headcount", "/ˈhedkaʊnt/", "n", "việc đếm sĩ số", "Let's do a <b>headcount</b> before we get on the bus.", "Mình đếm sĩ số trước khi lên xe nhé."),
  ("sign up", "/ˌsaɪn ˈʌp/", "phr v", "đăng ký (tham gia)", "You can <b>sign up</b> for two clubs this term.", "Học kỳ này em được đăng ký hai câu lạc bộ."),
  ("after-school", "/ˌɑːftə ˈskuːl/", "adj", "sau giờ học", "Our <b>after-school</b> clubs finish at 4:30.", "Các câu lạc bộ sau giờ học kết thúc lúc 4 giờ 30."),
  ("team spirit", "/ˌtiːm ˈspɪrɪt/", "n", "tinh thần đồng đội", "Great <b>team spirit</b> today, everyone!", "Hôm nay cả đội có tinh thần đồng đội tuyệt vời!"),
  ("packed lunch", "/ˌpækt ˈlʌntʃ/", "n", "cơm hộp mang theo", "Please bring a <b>packed lunch</b> and a water bottle.", "Nhớ mang theo cơm hộp và bình nước nhé."),
  ("meeting point", "/ˈmiːtɪŋ ˌpɔɪnt/", "n", "điểm tập trung", "If you get lost, go to the <b>meeting point</b>.", "Nếu bị lạc, em hãy đến điểm tập trung."),
 ],
 "phrases": [
  ("Our after-school clubs start next week.", "Các câu lạc bộ sau giờ học bắt đầu từ tuần sau."),
  ("You can sign up for two clubs this term.", "Học kỳ này em được đăng ký hai câu lạc bộ."),
  ("Please return the consent form by Tuesday.", "Phụ huynh gửi lại giấy đồng ý trước thứ Ba nhé."),
  ("The bus leaves at 8 a.m. sharp.", "Xe khởi hành đúng 8 giờ sáng."),
  ("Stay with your group at all times.", "Lúc nào cũng phải đi cùng nhóm."),
  ("Let's do a headcount before we get on the bus.", "Mình đếm sĩ số trước khi lên xe nhé."),
  ("Please bring a packed lunch and a water bottle.", "Nhớ mang theo cơm hộp và bình nước."),
  ("If you get lost, go to the meeting point.", "Nếu bị lạc, hãy đến điểm tập trung."),
  ("Each group has one teacher.", "Mỗi nhóm có một giáo viên phụ trách."),
  ("Great team spirit today!", "Hôm nay tinh thần đồng đội tuyệt lắm!"),
 ],
 "dialogues": [
  ("My son didn't return the consent form. Can he still go on the trip?", [
    ("I'm sorry, we need a signed form for every student. You can send me a photo of it before 5 p.m. today.", True, "Giữ nguyên tắc + đưa phương án gấp."),
    ("No problem, he can go.", False, "Đưa học sinh đi khi chưa có đồng ý của phụ huynh là sai quy trình."),
    ("No form, stay home.", False, "Cộc lốc, không đưa phương án."),
  ]),
  ("We have 24 students, but I only count 23.", [
    ("Let's stop here. I'll check the list and the toilets, and you keep the group together.", True, "Dừng lại + phân công đi tìm + giữ nhóm."),
    ("Maybe you count wrong, continue.", False, "Đi tiếp khi thiếu học sinh — rất nguy hiểm."),
    ("One student lost, not big problem.", False, "Thiếu động từ và mạo từ ('is lost', 'a big problem'), lại coi nhẹ sự việc."),
  ]),
  ("Can I join the robotics club and the football club?", [
    ("Yes, you can join two clubs. Please sign up on the school portal by Friday.", True, "Trả lời + cách đăng ký + hạn."),
    ("Robotics for smart students only.", False, "Phân biệt học sinh, thiếu động từ."),
    ("You choose one, two is too many for you.", False, "Áp đặt, không theo quy định."),
  ]),
  ("What should my daughter bring on the trip?", [
    ("A packed lunch, a water bottle, a hat and her school T-shirt, please.", True, "Liệt kê cụ thể."),
    ("Bring anything, it's fine.", False, "Không hướng dẫn gì."),
    ("She bring food.", False, "Sai chia động từ ('She should bring') và thiếu thông tin."),
  ]),
  ("How did your club go this term?", [
    ("Really well. Eighteen students joined, and they made a short film for the school assembly.", True, "Số liệu + sản phẩm cụ thể."),
    ("Very fun, everybody happy.", False, "Chung chung, thiếu động từ, không có kết quả."),
    ("Club is OK, not special.", False, "Thiếu thông tin, không có số liệu."),
  ]),
 ],
 "listen": [
  ("Please return the consent form by Tuesday", ["consent", "Tuesday"], "nhắc giấy đồng ý"),
  ("Stay with your group at all times", ["group", "times"], "nhắc đi theo nhóm"),
  ("If you get lost, go to the meeting point", ["lost", "meeting"], "điểm tập trung"),
  ("You can sign up for two clubs", ["sign", "clubs"], "đăng ký câu lạc bộ"),
  ("Good morning, everyone. The bus leaves at eight sharp. Please sit with your group and keep your seat belt on.", ["eight", "group", "belt"], "trước khi xe chạy"),
  ("We are at the museum now. Let's do a headcount. After lunch, we will meet at the main entrance.", ["museum", "headcount", "entrance"], "tại điểm tham quan"),
 ],
})

# ───────────────────────── D. Học sinh có nhu cầu đặc biệt ─────────────────────────
PHASES.append({
 "title": "Học sinh có nhu cầu đặc biệt",
 "vocab": [
  ("special needs", "/ˌspeʃl ˈniːdz/", "n", "nhu cầu giáo dục đặc biệt", "Our school supports students with <b>special needs</b>.", "Trường hỗ trợ học sinh có nhu cầu giáo dục đặc biệt."),
  ("learning support", "/ˈlɜːnɪŋ səˌpɔːt/", "n", "(bộ phận) hỗ trợ học tập", "I'll talk to the <b>learning support</b> team about him.", "Tôi sẽ trao đổi với bộ phận hỗ trợ học tập về cháu."),
  ("dyslexia", "/dɪsˈleksiə/", "n", "chứng khó đọc", "Students with <b>dyslexia</b> may need more time to read.", "Học sinh mắc chứng khó đọc có thể cần thêm thời gian để đọc."),
  ("autism", "/ˈɔːtɪzəm/", "n", "tự kỷ (rối loạn phổ tự kỷ)", "Every child with <b>autism</b> is different.", "Mỗi trẻ tự kỷ đều khác nhau."),
  ("individual education plan", "/ˌɪndɪˌvɪdʒuəl ˌedʒuˈkeɪʃn ˌplæn/", "n", "kế hoạch giáo dục cá nhân (IEP)", "Let's review his <b>individual education plan</b> next month.", "Tháng sau mình rà lại kế hoạch giáo dục cá nhân của cháu nhé."),
  ("extra time", "/ˌekstrə ˈtaɪm/", "n", "thời gian cộng thêm (khi làm bài)", "She gets <b>extra time</b> in tests.", "Khi kiểm tra, em ấy được cộng thêm thời gian."),
  ("one-to-one", "/ˌwʌn tə ˈwʌn/", "adj", "kèm riêng một thầy một trò", "He has a <b>one-to-one</b> reading session every Tuesday.", "Thứ Ba nào em ấy cũng có buổi kèm đọc riêng."),
  ("patience", "/ˈpeɪʃns/", "n", "sự kiên nhẫn", "Thank you for your <b>patience</b>.", "Cảm ơn anh/chị đã kiên nhẫn."),
  ("visual aid", "/ˌvɪʒuəl ˈeɪd/", "n", "đồ dùng trực quan (tranh, thẻ hình)", "<b>Visual aids</b> really help her understand.", "Đồ dùng trực quan giúp em ấy hiểu bài hơn hẳn."),
  ("overwhelmed", "/ˌəʊvəˈwelmd/", "adj", "quá tải, choáng ngợp", "He feels <b>overwhelmed</b> when the room is noisy.", "Em ấy thấy quá tải khi phòng học ồn ào."),
 ],
 "phrases": [
  ("Every child learns in a different way.", "Mỗi trẻ học theo một cách khác nhau."),
  ("He gets extra time in tests.", "Khi kiểm tra, em ấy được cộng thêm thời gian."),
  ("Let's break the task into small steps.", "Mình chia nhỏ nhiệm vụ thành từng bước nhé."),
  ("Visual aids really help her.", "Đồ dùng trực quan giúp em ấy rất nhiều."),
  ("She works better in a quiet corner.", "Em ấy làm bài tốt hơn ở góc yên tĩnh."),
  ("I'll talk to the learning support team.", "Tôi sẽ trao đổi với bộ phận hỗ trợ học tập."),
  ("Let's review his individual education plan next month.", "Tháng sau mình rà lại kế hoạch giáo dục cá nhân của cháu nhé."),
  ("Can we meet to talk about how to support him at home?", "Mình gặp nhau bàn cách hỗ trợ cháu ở nhà được không?"),
  ("He can take a short break when he feels overwhelmed.", "Khi thấy quá tải, cháu có thể nghỉ ngắn một chút."),
  ("Thank you for your patience.", "Cảm ơn anh/chị đã kiên nhẫn."),
 ],
 "dialogues": [
  ("I think my son might have dyslexia. What should I do?", [
    ("Thank you for telling me. I'll talk to our learning support team, and they can arrange an assessment with a specialist.", True, "Ghi nhận + chuyển đúng bộ phận; giáo viên không tự chẩn đoán."),
    ("Yes, he has dyslexia, I'm sure.", False, "Giáo viên không được tự chẩn đoán."),
    ("He is just lazy to read.", False, "Gắn nhãn và sai cấu trúc ('he just doesn't like reading')."),
  ]),
  ("Minh gets upset when the class is noisy.", [
    ("Let's give him a quiet corner and a card he can show when he needs a break.", True, "Điều chỉnh môi trường + công cụ hỗ trợ cụ thể."),
    ("He must learn to be normal.", False, "Thiếu tôn trọng — chữ 'normal' gây tổn thương."),
    ("Send him out of class.", False, "Loại trừ học sinh thay vì hỗ trợ."),
  ]),
  ("Will my daughter get extra time in the exam?", [
    ("Yes, it's in her learning plan. She'll get 25 percent extra time in a separate room.", True, "Xác nhận + chi tiết cụ thể."),
    ("Extra time is not fair for other.", False, "Sai — điều chỉnh hợp lý giúp em được công bằng; thiếu 's' ('others')."),
    ("Maybe, I will see.", False, "Mơ hồ, phụ huynh cần câu trả lời rõ."),
  ]),
  ("I can't do this. It's too hard!", [
    ("It's OK. Let's do the first step together, and then you try the next one.", True, "Trấn an + chia nhỏ nhiệm vụ."),
    ("Everyone can do it, why you can't?", False, "So sánh gây áp lực, sai cấu trúc câu hỏi ('why can't you?')."),
    ("Stop crying and do it.", False, "Ra lệnh, thiếu đồng cảm."),
  ]),
  ("How is the new plan working for Lan?", [
    ("It's going well. With picture cards, she answers more questions, and she only needed one break this week.", True, "Đánh giá có dẫn chứng."),
    ("I think fine.", False, "Thiếu chủ ngữ/động từ ('it's fine'), không có dẫn chứng."),
    ("The plan too much work for me.", False, "Thiếu động từ và than phiền thay vì báo cáo."),
  ]),
 ],
 "listen": [
  ("He gets extra time in every test", ["extra", "test"], "cộng thêm thời gian"),
  ("Let's break the task into small steps", ["break", "steps"], "chia nhỏ nhiệm vụ"),
  ("Visual aids really help her understand", ["Visual", "understand"], "đồ dùng trực quan"),
  ("She works better in a quiet corner", ["quiet", "corner"], "điều chỉnh chỗ ngồi"),
  ("Tom finds reading difficult. Please give him the text one day before the lesson. He can also listen to the audio.", ["reading", "day", "audio"], "hỗ trợ học sinh khó đọc"),
  ("When Mai feels overwhelmed, she shows a green card. Let her take a short break outside. She will come back in five minutes.", ["overwhelmed", "break", "five"], "thống nhất cách hỗ trợ"),
 ],
})

# ───────────────────────── E. Đào tạo doanh nghiệp ─────────────────────────
PHASES.append({
 "title": "Đào tạo doanh nghiệp",
 "vocab": [
  ("trainer", "/ˈtreɪnə/", "n", "giảng viên đào tạo, người đào tạo", "Our <b>trainer</b> has ten years of experience.", "Giảng viên đào tạo của chúng tôi có mười năm kinh nghiệm."),
  ("trainee", "/ˌtreɪˈniː/", "n", "học viên (khoá đào tạo)", "There are 16 <b>trainees</b> in this group.", "Nhóm này có 16 học viên."),
  ("workshop", "/ˈwɜːkʃɒp/", "n", "buổi hội thảo thực hành, lớp tập huấn", "Welcome to today's <b>workshop</b>.", "Chào mừng mọi người đến với buổi tập huấn hôm nay."),
  ("training needs", "/ˈtreɪnɪŋ ˌniːdz/", "n", "nhu cầu đào tạo", "First, let's find out your team's <b>training needs</b>.", "Trước tiên, mình tìm hiểu nhu cầu đào tạo của đội anh chị."),
  ("icebreaker", "/ˈaɪsbreɪkə/", "n", "hoạt động làm quen, phá băng", "Let's start with a quick <b>icebreaker</b>.", "Mình bắt đầu bằng một hoạt động phá băng ngắn nhé."),
  ("role-play", "/ˈrəʊl pleɪ/", "n/v", "đóng vai; luyện tập đóng vai", "Now, let's do a <b>role-play</b> in pairs.", "Giờ mình luyện đóng vai theo cặp nhé."),
  ("session", "/ˈseʃn/", "n", "buổi (học, đào tạo)", "The course has four <b>sessions</b>, two hours each.", "Khoá học có bốn buổi, mỗi buổi hai tiếng."),
  ("evaluation form", "/ɪˌvæljuˈeɪʃn ˌfɔːm/", "n", "phiếu đánh giá (khoá học)", "Please fill in the <b>evaluation form</b> before you leave.", "Mọi người điền phiếu đánh giá trước khi về nhé."),
  ("hands-on", "/ˌhændz ˈɒn/", "adj", "thực hành trực tiếp", "The course is very <b>hands-on</b>, with lots of practice.", "Khoá học thiên về thực hành, luyện tập rất nhiều."),
  ("takeaway", "/ˈteɪkəweɪ/", "n", "điều rút ra, bài học mang về", "What's your biggest <b>takeaway</b> from today?", "Điều lớn nhất anh chị rút ra hôm nay là gì?"),
 ],
 "phrases": [
  ("Welcome to today's workshop.", "Chào mừng mọi người đến với buổi tập huấn hôm nay."),
  ("Let's start with a quick icebreaker.", "Mình bắt đầu bằng một hoạt động phá băng ngắn nhé."),
  ("By the end of this session, you will be able to handle customer calls in English.", "Cuối buổi này, anh chị sẽ xử lý được cuộc gọi khách hàng bằng tiếng Anh."),
  ("Please put your phones on silent.", "Mọi người để điện thoại chế độ im lặng nhé."),
  ("Let's take a ten-minute break.", "Mình nghỉ giải lao mười phút nhé."),
  ("Now, let's do a role-play in pairs.", "Giờ mình luyện đóng vai theo cặp nhé."),
  ("What's your biggest takeaway from today?", "Điều lớn nhất anh chị rút ra hôm nay là gì?"),
  ("Please fill in the evaluation form before you leave.", "Mọi người điền phiếu đánh giá trước khi về nhé."),
  ("What are your team's training needs?", "Nhu cầu đào tạo của đội anh chị là gì?"),
  ("The course has four sessions, two hours each.", "Khoá học có bốn buổi, mỗi buổi hai tiếng."),
 ],
 "dialogues": [
  ("What will our staff learn in this course?", [
    ("They'll practise emails, meetings and phone calls in English, with role-plays based on their real work.", True, "Nội dung cụ thể + gắn với công việc thật."),
    ("Many things, very useful.", False, "Chung chung, không thuyết phục khách hàng."),
    ("They learn English, of course.", False, "Hiển nhiên, không có thông tin."),
  ]),
  ("Can I leave early today? I have a meeting.", [
    ("Sure. The slides will be in the group chat, so please do the practice task before the next session.", True, "Linh hoạt + đảm bảo học viên không mất bài."),
    ("No, company pays, you must stay.", False, "Cứng nhắc, thiếu mạo từ ('the company pays')."),
    ("OK, but you miss everything.", False, "Nghe như trách móc, sai thì ('you'll miss'), không hỗ trợ."),
  ]),
  ("How will you measure the results?", [
    ("We'll do a short test at the start and at the end, and managers will give feedback after one month.", True, "Cách đo cụ thể + thời điểm."),
    ("Staff will feel better, you will see.", False, "Mơ hồ, không đo được."),
    ("Result is depend on staff.", False, "Sai cấu trúc ('It depends on the staff') và đẩy trách nhiệm."),
  ]),
  ("This role-play is embarrassing. Can I just watch?", [
    ("I understand. You can watch the first one, then try a short part with me.", True, "Tôn trọng cảm xúc + khuyến khích từng bước."),
    ("No, everyone must do, no exception.", False, "Ép buộc gây căng thẳng; thiếu tân ngữ ('do it')."),
    ("Why you shy? Just speak.", False, "Sai cấu trúc ('Why are you shy?') và làm học viên ngại thêm."),
  ]),
  ("The group is tired after lunch. What should we do?", [
    ("Let's start with a quick standing activity, then move to the role-play.", True, "Giải pháp cụ thể để lấy lại năng lượng."),
    ("Continue slides, they will wake up.", False, "Chiếu slide liên tục càng làm người học buồn ngủ."),
    ("Tired is their problem.", False, "Thiếu trách nhiệm với lớp học, sai cấu trúc."),
  ]),
 ],
 "listen": [
  ("Let's start with a quick icebreaker", ["quick", "icebreaker"], "mở đầu buổi đào tạo"),
  ("Please fill in the evaluation form", ["fill", "evaluation"], "phiếu đánh giá"),
  ("The course has four sessions", ["four", "sessions"], "cấu trúc khoá học"),
  ("Now let's do a role-play in pairs", ["role-play", "pairs"], "luyện đóng vai"),
  ("Welcome back from lunch. In this session, we will practise phone calls. First, watch me and my partner, then try it in pairs.", ["lunch", "phone", "pairs"], "buổi chiều của khoá đào tạo"),
  ("Thank you for coming today. Please write your biggest takeaway on a sticky note. Then put it on the wall before you leave.", ["takeaway", "note", "wall"], "kết thúc buổi đào tạo"),
 ],
})

# ───────────────────────── F. Dự giờ & kiểm định ─────────────────────────
PHASES.append({
 "title": "Dự giờ & kiểm định",
 "vocab": [
  ("observation", "/ˌɒbzəˈveɪʃn/", "n", "buổi dự giờ, sự quan sát", "My lesson <b>observation</b> is on Thursday, period 3.", "Tiết 3 thứ Năm tôi bị dự giờ."),
  ("observer", "/əbˈzɜːvə/", "n", "người dự giờ", "The <b>observer</b> will sit at the back and take notes.", "Người dự giờ sẽ ngồi cuối lớp và ghi chép."),
  ("accreditation", "/əˌkredɪˈteɪʃn/", "n", "kiểm định (công nhận chất lượng)", "The <b>accreditation</b> team will visit in March.", "Đoàn kiểm định sẽ đến vào tháng Ba."),
  ("evidence", "/ˈevɪdəns/", "n", "minh chứng, bằng chứng", "We need <b>evidence</b> for each standard.", "Mình cần minh chứng cho từng tiêu chuẩn."),
  ("policy", "/ˈpɒləsi/", "n", "chính sách, quy định", "What's the school's <b>policy</b> on phones?", "Quy định của trường về điện thoại là gì?"),
  ("standard", "/ˈstændəd/", "n", "tiêu chuẩn", "Our teaching must meet every <b>standard</b> in the framework.", "Việc giảng dạy phải đạt mọi tiêu chuẩn trong bộ khung."),
  ("action plan", "/ˈækʃn ˌplæn/", "n", "kế hoạch hành động (khắc phục, cải tiến)", "Let's make an <b>action plan</b> for next term.", "Mình lập kế hoạch hành động cho học kỳ sau nhé."),
  ("best practice", "/ˌbest ˈpræktɪs/", "n", "cách làm tốt, thực hành tốt nhất", "Can you share some <b>best practice</b> from your class?", "Chị chia sẻ vài cách làm hay ở lớp chị được không?"),
  ("self-assessment", "/ˌself əˈsesmənt/", "n", "tự đánh giá", "Please send your <b>self-assessment</b> form by Friday.", "Gửi phiếu tự đánh giá trước thứ Sáu nhé."),
  ("professional development", "/prəˌfeʃənl dɪˈveləpmənt/", "n", "bồi dưỡng, phát triển chuyên môn", "The school pays for <b>professional development</b> courses.", "Trường chi trả cho các khoá bồi dưỡng chuyên môn."),
 ],
 "phrases": [
  ("My lesson observation is on Thursday, period 3.", "Tiết 3 thứ Năm tôi bị dự giờ."),
  ("The observer will sit at the back and take notes.", "Người dự giờ sẽ ngồi cuối lớp và ghi chép."),
  ("What went well in my lesson?", "Tiết dạy của tôi có điểm gì tốt?"),
  ("What's one thing I can improve?", "Tôi có thể cải thiện điều gì?"),
  ("We need evidence for each standard.", "Mình cần minh chứng cho từng tiêu chuẩn."),
  ("Please upload your documents to the shared folder by Friday.", "Tải tài liệu lên thư mục chung trước thứ Sáu nhé."),
  ("The accreditation team will visit in March.", "Đoàn kiểm định sẽ đến vào tháng Ba."),
  ("Let's make an action plan for next term.", "Mình lập kế hoạch hành động cho học kỳ sau nhé."),
  ("I'd like to share some best practice from my class.", "Tôi muốn chia sẻ vài cách làm hay ở lớp mình."),
  ("I'm going to a professional development workshop next week.", "Tuần sau tôi đi dự một buổi bồi dưỡng chuyên môn."),
 ],
 "dialogues": [
  ("How do you think your lesson went?", [
    ("I think the group work went well, but I spoke too much at the start. Next time, I'll give shorter instructions.", True, "Tự đánh giá cân bằng + kế hoạch cải thiện."),
    ("Perfect, no problem.", False, "Không tự đánh giá thật."),
    ("Students were bad today, not normal.", False, "Đổ lỗi cho học sinh."),
  ]),
  ("How did you check that the students understood?", [
    ("I asked three quick questions, and they showed their answers on mini whiteboards.", True, "Nêu kỹ thuật kiểm tra mức hiểu cụ thể."),
    ("I ask, 'Do you understand?', and they say yes.", False, "Sai thì ('I asked'); hỏi 'hiểu không?' không phải cách kiểm tra hiệu quả."),
    ("They understand, I know.", False, "Khẳng định mà không có bằng chứng."),
  ]),
  ("Can you show me evidence of how you support new students?", [
    ("Yes. Here is our welcome plan, the buddy list and feedback from last term's new families.", True, "Đưa minh chứng cụ thể."),
    ("We support very well, trust me.", False, "Chỉ khẳng định, không có minh chứng."),
    ("Evidence is in office somewhere.", False, "Thiếu mạo từ ('in the office') và thiếu chuẩn bị."),
  ]),
  ("Your self-assessment form is due tomorrow.", [
    ("Thanks for the reminder. I've done most of it, and I'll send it by 10 a.m. tomorrow.", True, "Cảm ơn + tiến độ + hạn cụ thể."),
    ("I forget, sorry.", False, "Sai thì ('I forgot') và không có kế hoạch."),
    ("Form too long, not useful.", False, "Than phiền, thiếu động từ."),
  ]),
  ("What's the school's policy on phones in class?", [
    ("Students keep their phones in their bags, and they can only use them when the teacher says so.", True, "Nêu quy định rõ ràng."),
    ("Policy? I don't know, do what you like.", False, "Không nắm quy định, khuyên sai."),
    ("Phones is not allowed never.", False, "Sai chia động từ ('are') và phủ định kép."),
  ]),
 ],
 "listen": [
  ("The observer will sit at the back", ["observer", "back"], "chuẩn bị dự giờ"),
  ("We need evidence for each standard", ["evidence", "standard"], "minh chứng kiểm định"),
  ("Let's make an action plan for next term", ["action", "term"], "kế hoạch hành động"),
  ("The accreditation team will visit in March", ["accreditation", "March"], "lịch kiểm định"),
  ("Thank you for your lesson today. The students were very active in the group work. Next time, try to give shorter instructions.", ["active", "group", "shorter"], "góp ý sau dự giờ"),
  ("The visitors will arrive on Monday. They will observe some lessons and talk to students. Please keep your classroom tidy.", ["Monday", "observe", "tidy"], "thông báo đoàn kiểm định"),
 ],
})

# ───────────────────────── G. Giáo vụ & học vụ ─────────────────────────
PHASES.append({
 "title": "Giáo vụ & học vụ",
 "vocab": [
  ("timetable", "/ˈtaɪmteɪbl/", "n", "thời khoá biểu", "There's a change to your <b>timetable</b> this week.", "Tuần này thời khoá biểu của anh có thay đổi."),
  ("attendance", "/əˈtendəns/", "n", "sự chuyên cần, việc có mặt", "His <b>attendance</b> this term is 98 percent.", "Học kỳ này em ấy đi học đủ 98%."),
  ("absence", "/ˈæbsəns/", "n", "sự vắng mặt", "Please call the office to report an <b>absence</b>.", "Vui lòng gọi văn phòng để báo học sinh vắng mặt."),
  ("register", "/ˈredʒɪstə/", "n", "sổ điểm danh", "Please take the <b>register</b> at 8 a.m.", "Điểm danh lúc 8 giờ sáng nhé."),
  ("school calendar", "/ˌskuːl ˈkælɪndə/", "n", "lịch năm học", "All holidays are on the <b>school calendar</b>.", "Mọi ngày nghỉ đều có trên lịch năm học."),
  ("uniform", "/ˈjuːnɪfɔːm/", "n", "đồng phục", "Students must wear their <b>uniform</b> every day.", "Học sinh phải mặc đồng phục hằng ngày."),
  ("student record", "/ˌstjuːdnt ˈrekɔːd/", "n", "hồ sơ học sinh", "I'll update your address in the <b>student record</b>.", "Tôi sẽ cập nhật địa chỉ mới vào hồ sơ học sinh."),
  ("invoice", "/ˈɪnvɔɪs/", "n", "hoá đơn, giấy báo thu", "The <b>invoice</b> for Term 2 has been sent by email.", "Giấy báo thu học kỳ 2 đã được gửi qua email."),
  ("school bus", "/ˌskuːl ˈbʌs/", "n", "xe buýt đưa đón của trường", "The <b>school bus</b> will be ten minutes late today.", "Hôm nay xe buýt trường sẽ đến trễ mười phút."),
  ("sick note", "/ˈsɪk ˌnəʊt/", "n", "giấy xin phép nghỉ ốm", "Please send a <b>sick note</b> when she comes back.", "Khi cháu đi học lại, anh/chị gửi giấy xin nghỉ ốm nhé."),
 ],
 "phrases": [
  ("Please take the register at 8 a.m.", "Điểm danh lúc 8 giờ sáng nhé."),
  ("Is there a change to my timetable this week?", "Tuần này thời khoá biểu của tôi có thay đổi gì không?"),
  ("Your son was absent on Monday and Tuesday.", "Cháu nhà mình vắng mặt thứ Hai và thứ Ba."),
  ("Please send a sick note when she's back.", "Khi cháu đi học lại, anh/chị gửi giấy xin nghỉ ốm nhé."),
  ("The school calendar is on the website.", "Lịch năm học có trên trang web của trường."),
  ("Students wear their PE uniform on Fridays.", "Thứ Sáu học sinh mặc đồng phục thể dục."),
  ("I'll update your address in the student record.", "Tôi sẽ cập nhật địa chỉ mới vào hồ sơ học sinh."),
  ("The invoice for Term 2 has been sent by email.", "Giấy báo thu học kỳ 2 đã được gửi qua email."),
  ("The school bus will be ten minutes late today.", "Hôm nay xe buýt trường sẽ đến trễ mười phút."),
  ("Could you fill in this form, please?", "Anh/chị điền giúp tôi mẫu đơn này nhé."),
 ],
 "dialogues": [
  ("Where can I find this week's timetable?", [
    ("It's on the staff portal, and there's a printed copy on the staff room notice board.", True, "Chỉ rõ hai nơi tìm được."),
    ("Timetable change every week, I don't know.", False, "Sai chia động từ ('changes') và không giúp được."),
    ("Ask principal.", False, "Thiếu mạo từ ('the principal') và đùn đẩy lên hiệu trưởng."),
  ]),
  ("Why does the report say my son was absent on Monday?", [
    ("Let me check the register. He was marked absent in period 1 — maybe he arrived late. I'll check with his teacher today.", True, "Kiểm tra dữ liệu + giả thuyết + xác minh."),
    ("The system is correct, he was absent.", False, "Khẳng định khi chưa kiểm tra."),
    ("Maybe he skip class.", False, "Sai thì ('skipped') và nghi ngờ học sinh khi chưa rõ."),
  ]),
  ("Can my daughter wear her own shoes? Her school shoes are broken.", [
    ("Yes, for this week. Please write a short note in her diary so the teachers know.", True, "Linh hoạt + cách báo cho giáo viên."),
    ("No, uniform is rule.", False, "Cứng nhắc, thiếu mạo từ ('the rule')."),
    ("Buy new shoes today.", False, "Ra lệnh, không thông cảm."),
  ]),
  ("I'm sick today. What should I do?", [
    ("I'm sorry to hear that. Please send your lesson plans to the office, and I'll arrange cover for your classes.", True, "Hỏi thăm + việc cần làm + sắp xếp dạy thay."),
    ("You come, today is busy.", False, "Ép giáo viên ốm đi làm, sai ngữ pháp."),
    ("Tell students yourself.", False, "Không phải cách xử lý của giáo vụ."),
  ]),
  ("When is the last day of school before Tết?", [
    ("It's on the 5th of February, and school starts again on the 15th. It's all on the school calendar.", True, "Ngày cụ thể + nơi tra cứu."),
    ("Tết holiday long, maybe two weeks.", False, "Thiếu động từ, mơ hồ, không có ngày cụ thể."),
    ("You check website.", False, "Cộc lốc, thiếu mạo từ, không hỗ trợ."),
  ]),
 ],
 "listen": [
  ("Please take the register at eight", ["register", "eight"], "nhắc điểm danh"),
  ("Your son was absent on Monday", ["absent", "Monday"], "báo vắng mặt"),
  ("The school calendar is on the website", ["calendar", "website"], "lịch năm học"),
  ("Please send a sick note tomorrow", ["sick", "tomorrow"], "giấy xin nghỉ ốm"),
  ("Dear parents, the school bus will be late today. There is heavy traffic on the main road. The bus will arrive at seven forty.", ["late", "traffic", "forty"], "báo xe buýt trễ"),
  ("Next week there are some room changes. Grade six will use Room 302. Please check your new timetable on the portal.", ["room", "Grade", "timetable"], "báo đổi phòng học"),
 ],
})

# ───────────────────────── H. Coi thi & kỳ thi ─────────────────────────
PHASES.append({
 "title": "Coi thi & kỳ thi",
 "vocab": [
  ("exam hall", "/ɪɡˈzæm ˌhɔːl/", "n", "phòng thi (lớn), hội trường thi", "Please line up outside the <b>exam hall</b>.", "Các em xếp hàng bên ngoài phòng thi nhé."),
  ("invigilator", "/ɪnˈvɪdʒɪleɪtə/", "n", "giám thị coi thi", "Put your hand up and the <b>invigilator</b> will come to you.", "Giơ tay lên, giám thị sẽ đến chỗ em."),
  ("candidate", "/ˈkændɪdət/", "n", "thí sinh", "Each <b>candidate</b> has a number on the desk.", "Mỗi thí sinh có một số báo danh trên bàn."),
  ("answer sheet", "/ˈɑːnsə ˌʃiːt/", "n", "phiếu trả lời, giấy làm bài", "Write your name on the <b>answer sheet</b> now.", "Bây giờ các em ghi tên vào phiếu trả lời."),
  ("seat number", "/ˈsiːt ˌnʌmbə/", "n", "số ghế, vị trí ngồi", "Find your <b>seat number</b> and sit down.", "Tìm đúng số ghế của mình rồi ngồi xuống."),
  ("cheating", "/ˈtʃiːtɪŋ/", "n", "gian lận (quay cóp)", "<b>Cheating</b> in an exam is taken very seriously.", "Gian lận trong thi cử bị xử lý rất nghiêm."),
  ("mock exam", "/ˌmɒk ɪɡˈzæm/", "n", "kỳ thi thử", "The <b>mock exams</b> start next Monday.", "Thi thử bắt đầu từ thứ Hai tuần sau."),
  ("results day", "/rɪˈzʌlts ˌdeɪ/", "n", "ngày công bố kết quả", "Teachers will be at school on <b>results day</b> to help students.", "Ngày có kết quả, giáo viên sẽ có mặt ở trường để hỗ trợ học sinh."),
  ("question paper", "/ˈkwestʃən ˌpeɪpə/", "n", "đề thi (tờ đề)", "Don't open the <b>question paper</b> until I tell you.", "Chưa mở đề cho đến khi có hiệu lệnh."),
  ("silence", "/ˈsaɪləns/", "n", "sự im lặng", "Please work in <b>silence</b> until the end of the exam.", "Các em làm bài trong im lặng cho đến hết giờ thi nhé."),
 ],
 "phrases": [
  ("Please leave your phones and bags at the front.", "Để điện thoại và cặp ở đầu phòng nhé."),
  ("Find your seat number and sit down.", "Tìm đúng số ghế rồi ngồi xuống."),
  ("Write your name and candidate number on the answer sheet.", "Ghi tên và số báo danh lên phiếu trả lời."),
  ("Do not open the question paper until I tell you.", "Chưa mở đề cho đến khi có hiệu lệnh."),
  ("You have one hour and thirty minutes.", "Các em có một tiếng rưỡi."),
  ("There are ten minutes left.", "Còn mười phút nữa."),
  ("If you need help, put your hand up.", "Cần hỗ trợ thì giơ tay."),
  ("Stop writing and put your pens down.", "Dừng bút, đặt bút xuống."),
  ("Talking during the exam is not allowed.", "Không được nói chuyện trong giờ thi."),
  ("Results will be available online next Friday.", "Thứ Sáu tuần sau sẽ có kết quả trực tuyến."),
 ],
 "dialogues": [
  ("Can I go to the toilet?", [
    ("Yes, but a staff member will go with you. Please leave your paper face down.", True, "Cho phép theo đúng quy trình coi thi."),
    ("No, wait until the end.", False, "Cứng nhắc, không theo quy trình thông thường."),
    ("Go quick, come back fast.", False, "Để thí sinh ra ngoài không giám sát; sai dạng từ ('quickly')."),
  ]),
  ("I think the student in seat 14 is looking at his phone.", [
    ("Let's check quietly. I'll go to him, and you watch the rest of the room.", True, "Xử lý kín đáo + phân công."),
    ("Shout his name to stop him.", False, "Làm ồn phòng thi, ảnh hưởng thí sinh khác."),
    ("Maybe he check time, no problem.", False, "Sai chia động từ ('he's checking') và bỏ qua dấu hiệu gian lận."),
  ]),
  ("I forgot my calculator!", [
    ("Stay calm. We have spare calculators — I'll bring you one now.", True, "Trấn an + giải pháp."),
    ("Your problem, not mine.", False, "Thiếu hỗ trợ."),
    ("Why you always forget?", False, "Sai cấu trúc câu hỏi ('Why do you always forget?') và trách móc."),
  ]),
  ("When will the mock exam results come out?", [
    ("Teachers are marking now. The results will be on the parent portal next Friday.", True, "Tiến độ + ngày + nơi xem."),
    ("Mock exam not important, don't worry.", False, "Xem nhẹ thi thử — kết quả giúp học sinh chuẩn bị."),
    ("Result come maybe soon.", False, "Sai chia động từ, mơ hồ."),
  ]),
  ("There's a page missing in my question paper.", [
    ("Thank you for telling me. I'll give you a new paper now and note the time in the exam report.", True, "Xử lý ngay + ghi biên bản."),
    ("Just do the other pages.", False, "Bất công cho thí sinh."),
    ("Impossible, paper is checked.", False, "Phủ nhận khi chưa kiểm tra; sai ngữ pháp ('the papers were checked')."),
  ]),
 ],
 "listen": [
  ("Find your seat number and sit down", ["seat", "sit"], "vào phòng thi"),
  ("Do not open the question paper yet", ["open", "paper"], "chưa mở đề"),
  ("There are ten minutes left", ["ten", "left"], "báo giờ"),
  ("Stop writing and put your pens down", ["writing", "pens"], "hết giờ"),
  ("Good morning, candidates. Please leave your phones at the front. Write your name on the answer sheet now.", ["candidates", "phones", "name"], "hướng dẫn đầu giờ thi"),
  ("The exam starts now. You have one hour. If you need help, put your hand up quietly.", ["starts", "hour", "quietly"], "bắt đầu giờ thi"),
 ],
})

# ───────────────────────── Vai: tình huống + hội thoại mới ─────────────────────────
ROLES_X = {
 "teacher": {
  "scenarios": [
   ("te_newstudent", "Đón học sinh mới chưa nói được tiếng Anh", "You are a Korean mother bringing your 8-year-old son to his first day. He speaks little English. Ask how the teacher will help him, who his buddy is and how you will get updates."),
   ("te_observe", "Nhận góp ý sau dự giờ", "You are the foreign academic director. You observed my Grade 6 lesson. Give me one strength and one area to improve, and ask what I will change."),
  ],
  "dialogues": [
   ("My son can't make friends in the new class.", [
     ("Thank you for telling me. I'll give him a buddy and put him in a group with some kind students.", True, "Ghi nhận + hỗ trợ hoà nhập cụ thể."),
     ("He is shy, he will be OK later.", False, "Chờ đợi thụ động, không hỗ trợ."),
     ("Making friends is not school job.", False, "Sai — hỗ trợ hoà nhập là việc của trường; thiếu mạo từ ('the school's job').")]),
   ("Can you use less Vietnamese in the science lesson?", [
     ("Sure. I'll use more pictures and gestures, and only use Vietnamese for new key words.", True, "Đồng ý + cách làm cụ thể."),
     ("If no Vietnamese, students don't understand.", False, "Bào chữa, sai cấu trúc câu điều kiện ('If I don't use Vietnamese, …')."),
     ("Vietnamese is faster, I prefer.", False, "Đặt sở thích cá nhân lên trên mục tiêu song ngữ.")]),
   ("I got a lower mark than my friend, but our answers are the same.", [
     ("Let's look at both papers together. If I made a mistake, I'll change your mark.", True, "Cầu thị + kiểm tra lại."),
     ("My marking is always right.", False, "Bảo thủ."),
     ("You copy your friend?", False, "Buộc tội vô căn cứ; sai cấu trúc câu hỏi ('Did you copy…?').")]),
   ("Why didn't you tell me earlier that my daughter was struggling?", [
     ("You're right, I should have told you sooner. Let's meet this week and make a plan together.", True, "Nhận trách nhiệm + hành động."),
     ("I was busy, many students.", False, "Bào chữa, câu thiếu cấu trúc."),
     ("She didn't tell you?", False, "Né tránh bằng câu hỏi ngược.")]),
  ]},
 "assistant": {
  "scenarios": [
   ("as_trip", "Hỗ trợ chuyến dã ngoại", "You are the foreign class teacher leading a field trip. I am the teaching assistant. Give me my group of students, ask me to do a headcount and tell me what to do if a child feels sick."),
   ("as_exam", "Coi thi cùng giáo viên", "You are a foreign teacher. We invigilate an exam together. Explain the rules, ask me to hand out the papers and tell me what to do if a student cheats."),
  ],
  "dialogues": [
   ("How many students are in your group?", [
     ("Eight. I've just counted them, and everyone is here.", True, "Con số + vừa kiểm tra."),
     ("Many, I think eight or nine.", False, "Không chắc số học sinh — nguy hiểm khi ra ngoài trường."),
     ("All here, don't worry.", False, "Thiếu động từ ('Everyone's here') và không nêu con số.")]),
   ("Could you sit with Bảo during the test? He needs extra support.", [
     ("Of course. I'll read the questions to him, but I won't give him the answers.", True, "Hỗ trợ đúng mức, giữ công bằng."),
     ("OK, I help him answer.", False, "Làm hộ học sinh là sai; thiếu 'will'."),
     ("He can do alone, no need.", False, "Bỏ qua nhu cầu hỗ trợ của em; thiếu tân ngữ ('do it alone').")]),
   ("Can you make the classroom display for the open day?", [
     ("Sure. I'll use the students' best posters and finish it by Thursday afternoon.", True, "Đồng ý + cách làm + hạn."),
     ("I not good at art.", False, "Thiếu động từ ('I'm not good at…') và từ chối ngay."),
     ("Display for what?", False, "Hỏi cộc lốc, thiếu lịch sự.")]),
   ("A student is crying in the corridor.", [
     ("I'll stay with her and ask what's wrong. If it's serious, I'll tell you and the counsellor.", True, "Ở bên học sinh + tìm hiểu + báo người phụ trách."),
     ("Children cry, it's nothing.", False, "Xem nhẹ cảm xúc học sinh."),
     ("Tell her go back to class.", False, "Sai cấu trúc ('Tell her to go') và bỏ mặc học sinh.")]),
  ]},
 "admissions": {
  "scenarios": [
   ("ad_openday", "Tư vấn ở ngày hội mở cửa", "You are a foreign parent at our school's open day. Ask me quick questions about the curriculum, school hours, lunch and how to apply."),
   ("ad_scholar", "Tư vấn hồ sơ học bổng", "You are a Grade 12 student applying for a scholarship abroad. Ask me what documents you need, how to write the personal statement and when the deadline is."),
  ],
  "dialogues": [
   ("What are the school hours?", [
     ("Classes are from 7:45 to 3:30, and after-school clubs finish at 4:30.", True, "Giờ học + giờ câu lạc bộ."),
     ("Morning to afternoon.", False, "Mơ hồ, không có giờ cụ thể."),
     ("School open early, close late.", False, "Sai chia động từ ('opens', 'closes') và không có giờ.")]),
   ("Is lunch included in the fee?", [
     ("No, lunch is a separate fee. I'll show you this month's menu and the price.", True, "Trả lời rõ + thông tin kèm theo."),
     ("Lunch? I think yes, maybe.", False, "Đoán mò về chi phí."),
     ("Lunch very delicious.", False, "Thiếu động từ và không trả lời câu hỏi.")]),
   ("What documents do I need for the scholarship?", [
     ("Your transcripts, two recommendation letters, a personal statement and an English test score.", True, "Liệt kê đủ giấy tờ."),
     ("Many papers, I send you later.", False, "Mơ hồ, thiếu 'will'."),
     ("Only money is enough.", False, "Sai hoàn toàn về hồ sơ học bổng.")]),
   ("Can your students arrive one day early?", [
     ("Let me check with the parents and the flight options, and I'll confirm by Friday.", True, "Kiểm tra trước + hẹn ngày xác nhận."),
     ("Yes, sure, no problem.", False, "Hứa khi chưa kiểm tra."),
     ("Early is difficult, cannot.", False, "Thiếu chủ ngữ, từ chối không lý do.")]),
  ]},
 "admin": {
  "scenarios": [
   ("ga_record", "Cập nhật hồ sơ học sinh", "You are a foreign parent who just moved house and changed your phone number. Call the school office to update your child's record and ask if you need to fill in a form."),
   ("ga_event", "Nhắc lịch sự kiện", "You are a busy foreign parent. The school office calls you about next week's sports day. Ask about the time, what your child should wear and whether parents can watch."),
  ],
  "dialogues": [
   ("I've changed my phone number.", [
     ("Thanks for letting us know. Could you tell me the new number? I'll update the student record now.", True, "Cảm ơn + hỏi thông tin + cập nhật ngay."),
     ("OK, you write in paper.", False, "Sai giới từ ('on paper') và không tự xử lý."),
     ("Phone change, why?", False, "Hỏi thừa, thiếu lịch sự.")]),
   ("Can parents watch sports day?", [
     ("Yes, parents are welcome. The events start at 8 a.m., and there's parking behind the gym.", True, "Trả lời + giờ + thông tin gửi xe."),
     ("Can, but no parking.", False, "Thiếu chủ ngữ, thông tin cụt."),
     ("Sports day is for students only maybe.", False, "Mơ hồ, sai thông tin.")]),
   ("The register system isn't working.", [
     ("Please take attendance on paper for now, and I'll ask IT support to fix it.", True, "Phương án tạm + xử lý gốc."),
     ("No register today, OK.", False, "Không điểm danh là sai — phải có phương án tạm."),
     ("System always broken.", False, "Than phiền, thiếu động từ.")]),
   ("I paid the fee, but I got a reminder.", [
     ("I'm sorry about that. Could you send me the transfer receipt? I'll check with the accounts team today.", True, "Xin lỗi + xin chứng từ + kiểm tra."),
     ("System say you not pay.", False, "Sai chia động từ ('says you haven't paid') và đổ cho hệ thống."),
     ("Maybe you pay wrong account.", False, "Đổ lỗi khi chưa kiểm tra, sai thì.")]),
  ]},
}

EXTRA = {
 "phases": PHASES,
 "rev": [
  ("Thứ Bảy này trường có ngày hội mở cửa.", "Our open day is this Saturday."),
  ("Buổi tổng duyệt lúc 2 giờ ở hội trường.", "The rehearsal is at 2 p.m. in the hall."),
  ("Cần bảng điểm ba năm gần nhất của em.", "We need your transcripts for the last three years."),
  ("Học bổng chi trả một nửa học phí.", "The scholarship covers half of the tuition."),
  ("Nhớ gửi lại giấy đồng ý trước thứ Ba.", "Please return the consent form by Tuesday."),
  ("Đếm sĩ số trước khi lên xe nhé.", "Let's do a headcount before we get on the bus."),
  ("Khi kiểm tra, em được cộng thêm thời gian.", "You get extra time in tests."),
  ("Mình chia nhỏ bài này ra nhé.", "Let's break this task into small steps."),
  ("Mọi người điền phiếu đánh giá nhé.", "Please fill in the evaluation form."),
  ("Điều anh chị rút ra hôm nay là gì?", "What's your biggest takeaway from today?"),
  ("Thứ Năm tôi bị dự giờ.", "My lesson is being observed on Thursday."),
  ("Mình cần minh chứng cho từng tiêu chuẩn.", "We need evidence for each standard."),
  ("Hôm qua cháu nghỉ học vì ốm.", "He was absent yesterday because he was sick."),
  ("Xe buýt trường sẽ đến trễ mười phút.", "The school bus will be ten minutes late."),
  ("Chưa được mở đề cho đến khi có hiệu lệnh.", "Don't open the question paper until I tell you."),
  ("Còn mười phút nữa.", "There are ten minutes left."),
 ],
 "reading": [
  {"t": "Field trip letter", "text": "Dear Parents,\nGrade 4 will visit the science museum on Friday, 16 October. The bus leaves school at 8:00 and returns at 14:30. Please sign the consent form and return it by Tuesday. Students should bring a packed lunch and a water bottle, and wear their PE uniform.\nGrade 4 Team", "q": [
    {"q": "When must parents return the form?", "o": ["Friday", "Tuesday", "Monday"], "a": 1},
    {"q": "What should students bring?", "o": ["A packed lunch and water", "Money for lunch", "Their textbooks"], "a": 0}]},
  {"t": "Scholarship notice", "text": "MERIT SCHOLARSHIP 2027\nOpen to: Grade 12 students with an average score of 8.5 or above\nAward: 50% of first-year tuition\nDocuments: transcripts (Grades 10–12), one recommendation letter, personal statement (max. 650 words)\nDeadline: 15 January, 17:00\nShortlisted students will have an online interview in February.", "q": [
    {"q": "How much does the scholarship cover?", "o": ["All tuition for four years", "Half of first-year tuition", "Only accommodation"], "a": 1},
    {"q": "What happens in February?", "o": ["Shortlisted students have an interview", "Students get their visas", "Applications open"], "a": 0}]},
  {"t": "Learning support profile", "text": "LEARNING SUPPORT – Student profile\nStudent: Khang, Grade 3\nNeeds: finds reading and spelling difficult (dyslexia)\nWhat helps: large font, coloured paper, audio versions of texts, extra time (25%)\nPlease avoid: asking him to read aloud without warning.\nContact: Ms. Thảo, Learning Support", "q": [
    {"q": "What should teachers avoid?", "o": ["Giving extra time", "Asking him to read aloud without warning", "Using coloured paper"], "a": 1},
    {"q": "How much extra time does he get?", "o": ["25%", "10%", "50%"], "a": 0}]},
  {"t": "Observation feedback", "text": "LESSON OBSERVATION – Grade 7 English\nStrengths: clear learning objective; good pair work; students used English most of the time.\nArea to improve: instructions were long, and some students started late.\nAction: give instructions in 3 short steps and check with one question.\nFollow-up visit: 12 November", "q": [
    {"q": "What was the problem?", "o": ["The pair work was weak", "Students spoke Vietnamese", "The instructions were too long"], "a": 2},
    {"q": "What should the teacher do next time?", "o": ["Give instructions in 3 short steps", "Stop pair work", "Teach in Vietnamese"], "a": 0}]},
  {"t": "Exam rules", "text": "EXAM RULES\n1. Arrive 15 minutes before the start.\n2. Leave phones and smartwatches at the front.\n3. Write your name and candidate number on every answer sheet.\n4. You may not leave in the first 30 minutes or the last 10 minutes.\n5. Put your hand up if you need help.", "q": [
    {"q": "When should candidates arrive?", "o": ["At the start time", "15 minutes before the start", "30 minutes before the start"], "a": 1},
    {"q": "When can't candidates leave?", "o": ["In the first 30 minutes", "After one hour", "In the middle of the exam"], "a": 0}]},
 ],
 "ai": [
  ("open_day", "Ngày hội mở cửa", "You are a foreign parent at our school's open day. Ask me about the school, the teachers, after-school clubs and how to apply. Speak simple English."),
  ("study_abroad", "Tư vấn du học", "You are a Grade 11 student who wants to study abroad. Ask me which country to choose, what documents you need and how to get a scholarship."),
  ("field_trip", "Thiếu học sinh khi dã ngoại", "You are a foreign teacher leading a school field trip with me. One student is missing at the museum. Ask me what I know and agree on what to do now."),
  ("training", "Chào khoá đào tạo doanh nghiệp", "You are an HR manager at a company where I will teach an English course for staff. Ask about the goals of the course, the activities and how we will measure results."),
 ],
 "events": [
  ("sports_day", "Ngày hội thể thao", "You are a foreign parent. Sports day is next week. Ask me about the time, the events, what your child should wear and whether parents can join."),
  ("accreditation", "Đoàn kiểm định trường", "You are a member of an international accreditation team visiting our school next month. Ask about our teaching standards, evidence, student support and action plans."),
  ("graduation", "Lễ tốt nghiệp", "You are a foreign parent. Your child's graduation ceremony is next week. Ask me about the time, the dress code, seats for family and photos."),
 ],
 "quips": [
  "Consent form signed!",
  "Headcount: all here!",
  "Pens down, please!",
  "Scholarship unlocked!",
  "Rehearsal time!",
  "Every child learns differently!",
 ],
 "roles": ROLES_X,
}
