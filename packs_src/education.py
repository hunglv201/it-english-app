# -*- coding: utf-8 -*-
# Gói "education" — Giáo dục · Đào tạo: giáo viên dạy song ngữ / trường quốc tế, trợ giảng, tư vấn tuyển sinh – du học,
# nhân viên giáo vụ & liên lạc phụ huynh. Người đối diện: học sinh, phụ huynh nước ngoài, giáo viên bản ngữ, đối tác trường quốc tế.
# Tên người / trường đều là tên tự đặt. Chặng lõi lấy từ office: 3 (Email công việc), 11 (Phỏng vấn & phát triển sự nghiệp).
# Schema: xem packs_src/README.md. Build: python3 packs_src/build.py education

PHASES = []

# ───────────────────────── 0. Lớp học & chỉ dẫn ─────────────────────────
PHASES.append({
 "title": "Lớp học & chỉ dẫn",
 "vocab": [
  ("instruction", "/ɪnˈstrʌkʃn/", "n", "lời hướng dẫn, chỉ dẫn", "Listen to the <b>instructions</b> first, then start.", "Nghe hướng dẫn trước rồi mới bắt đầu nhé."),
  ("worksheet", "/ˈwɜːkʃiːt/", "n", "phiếu bài tập", "Please finish the <b>worksheet</b> in ten minutes.", "Các em làm xong phiếu bài tập trong mười phút nhé."),
  ("handout", "/ˈhændaʊt/", "n", "tài liệu phát tay", "Take one <b>handout</b> and pass the rest back.", "Lấy một tờ tài liệu rồi chuyền phần còn lại ra sau."),
  ("whiteboard", "/ˈwaɪtbɔːd/", "n", "bảng trắng", "Copy the new words from the <b>whiteboard</b>.", "Chép các từ mới trên bảng vào vở."),
  ("pair work", "/ˈpeə ˌwɜːk/", "n", "hoạt động theo cặp", "This activity is <b>pair work</b>, so turn to your partner.", "Hoạt động này làm theo cặp, các em quay sang bạn bên cạnh nhé."),
  ("group work", "/ˈɡruːp ˌwɜːk/", "n", "hoạt động nhóm", "In <b>group work</b>, everyone has a job.", "Khi làm việc nhóm, ai cũng có một nhiệm vụ."),
  ("take turns", "/ˌteɪk ˈtɜːnz/", "phr v", "lần lượt, thay phiên nhau", "Please <b>take turns</b> to read the questions.", "Các em lần lượt đọc các câu hỏi nhé."),
  ("textbook", "/ˈtekstbʊk/", "n", "sách giáo khoa, sách học", "Open your <b>textbook</b> at page 24.", "Mở sách trang 24."),
  ("hand in", "/ˌhænd ˈɪn/", "phr v", "nộp (bài)", "Please <b>hand in</b> your homework on Friday.", "Các em nộp bài tập về nhà vào thứ Sáu nhé."),
  ("volunteer", "/ˌvɒlənˈtɪə/", "n/v", "người xung phong; xung phong", "Can I have a <b>volunteer</b> to read the first question?", "Có bạn nào xung phong đọc câu hỏi đầu tiên không?"),
 ],
 "phrases": [
  ("Open your books at page 24, please.", "Các em mở sách trang 24 nhé."),
  ("Work in pairs and ask your partner these questions.", "Làm theo cặp và hỏi bạn bên cạnh những câu này."),
  ("You have five minutes. Please start now.", "Các em có năm phút. Bắt đầu nhé."),
  ("Put your hand up if you know the answer.", "Ai biết đáp án thì giơ tay nhé."),
  ("Could you say that again, a bit louder?", "Em nói lại to hơn một chút được không?"),
  ("Let's check the answers together.", "Mình cùng chữa đáp án nhé."),
  ("Please pass the worksheets to the back.", "Các em chuyền phiếu bài tập ra phía sau nhé."),
  ("Eyes on me, please.", "Các em nhìn lên cô/thầy nhé."),
  ("Is everything clear? Any questions?", "Các em hiểu hết chưa? Có câu hỏi gì không?"),
  ("Please hand in your worksheet before you leave.", "Nộp phiếu bài tập trước khi ra về nhé."),
 ],
 "dialogues": [
  ("Teacher, what do we have to do?", [
    ("Read the text and answer the three questions. You can work with your partner.", True, "Chỉ dẫn rõ: làm gì + làm thế nào (theo cặp)."),
    ("You do the paper.", False, "Quá chung chung — học sinh không biết làm phần nào, làm ra sao."),
    ("Read and answer, I said already.", False, "Sai thì ('I've already said that') và nghe cáu kỉnh — nên nhắc lại kiên nhẫn."),
  ]),
  ("Can we work together on this?", [
    ("Yes, you can work in pairs, but each of you needs to write your own answers.", True, "Cho phép + quy định rõ ràng."),
    ("Yes, together, one person write.", False, "Sai chia động từ ('writes') và để một người làm hết."),
    ("No together.", False, "Cộc lốc, thiếu động từ — nên nói 'No, please work alone this time.'"),
  ]),
  ("I don't understand question three.", [
    ("OK, let me explain. You need to find a word that means 'happy' in paragraph two.", True, "Sẵn lòng + giải thích cụ thể."),
    ("It is easy, you think more.", False, "Gạt đi, sai cấu trúc ('Think about it a bit more')."),
    ("Question three is same question two.", False, "Thiếu 'the … as' và không giúp học sinh hiểu bài."),
  ]),
  ("How much time do we have?", [
    ("Five more minutes. I'll tell you when there's one minute left.", True, "Thời gian cụ thể + báo trước khi hết giờ."),
    ("Have five minutes.", False, "Thiếu chủ ngữ: 'You have five minutes.'"),
    ("Not much, hurry hurry.", False, "Lặp từ kiểu tiếng Việt ('nhanh nhanh') và không nói rõ thời gian."),
  ]),
  ("Should I hand out the worksheets now?", [
    ("Not yet. Let's give the instructions first, then hand them out.", True, "Trình tự chuẩn: hướng dẫn trước, phát phiếu sau để học sinh tập trung nghe."),
    ("Yes, give now, fast.", False, "Thiếu tân ngữ ('give them out now'); phát phiếu trước khi hướng dẫn làm học sinh mất tập trung."),
    ("Worksheets is on table.", False, "Sai chia động từ ('are'), thiếu mạo từ và không trả lời câu hỏi."),
  ]),
 ],
 "listen": [
  ("Open your books at page twenty-four", ["books", "page"], "mở sách"),
  ("Work in pairs and ask your partner", ["pairs", "partner"], "làm theo cặp"),
  ("Put your hand up if you know the answer", ["hand", "answer"], "giơ tay trả lời"),
  ("Please hand in your worksheet before you leave", ["worksheet", "leave"], "nộp bài"),
  ("Good morning, class. Today we are going to learn about animals. First, look at the pictures on the whiteboard.", ["animals", "pictures", "whiteboard"], "mở đầu tiết học"),
  ("You have ten minutes for this worksheet. Work alone first. Then check your answers with your partner.", ["ten", "alone", "check"], "chỉ dẫn làm phiếu bài tập"),
 ],
})

# ───────────────────────── 1. Quản lý lớp học & nề nếp ─────────────────────────
PHASES.append({
 "title": "Quản lý lớp học & nề nếp",
 "vocab": [
  ("behaviour", "/bɪˈheɪvjə/", "n", "hành vi, cách cư xử", "His <b>behaviour</b> is much better this week.", "Tuần này em ấy cư xử tốt hơn nhiều."),
  ("classroom rules", "/ˌklɑːsruːm ˈruːlz/", "n", "nội quy lớp học", "Let's read our <b>classroom rules</b> together.", "Cả lớp cùng đọc nội quy lớp nhé."),
  ("routine", "/ruːˈtiːn/", "n", "nề nếp, trình tự quen thuộc hằng ngày", "Our morning <b>routine</b> starts with ten minutes of reading.", "Nề nếp buổi sáng của lớp bắt đầu bằng mười phút đọc sách."),
  ("praise", "/preɪz/", "n/v", "lời khen; khen", "Specific <b>praise</b> works better than just 'good job'.", "Khen cụ thể hiệu quả hơn chỉ nói 'giỏi lắm'."),
  ("reward", "/rɪˈwɔːd/", "n/v", "phần thưởng; thưởng", "The class gets a <b>reward</b> when they collect ten stars.", "Cả lớp được thưởng khi gom đủ mười ngôi sao."),
  ("consequence", "/ˈkɒnsɪkwəns/", "n", "hệ quả (hình thức xử lý khi vi phạm)", "If you break the rule again, there will be a <b>consequence</b>.", "Nếu em vi phạm nội quy lần nữa thì sẽ bị xử lý."),
  ("seating plan", "/ˈsiːtɪŋ ˌplæn/", "n", "sơ đồ chỗ ngồi", "I'm changing the <b>seating plan</b> next week.", "Tuần sau tôi sẽ đổi sơ đồ chỗ ngồi."),
  ("disruptive", "/dɪsˈrʌptɪv/", "adj", "gây mất trật tự, làm gián đoạn", "His talking is <b>disruptive</b> to the other students.", "Việc em ấy nói chuyện làm ảnh hưởng các bạn khác."),
  ("calm down", "/ˌkɑːm ˈdaʊn/", "phr v", "bình tĩnh lại", "Let's take a deep breath and <b>calm down</b>.", "Mình hít thở sâu và bình tĩnh lại nhé."),
  ("on task", "/ˌɒn ˈtɑːsk/", "adj", "tập trung đúng việc được giao", "Most students stayed <b>on task</b> for the whole activity.", "Phần lớn học sinh tập trung làm bài suốt hoạt động."),
 ],
 "phrases": [
  ("Please sit down and get your books out.", "Các em ngồi xuống và lấy sách ra nhé."),
  ("I'm waiting for everyone to be quiet.", "Cô/thầy đang đợi cả lớp im lặng."),
  ("Thank you, Table 2, for being ready so quickly.", "Cảm ơn bàn 2 đã chuẩn bị nhanh như vậy."),
  ("Remember our rule: one person speaks at a time.", "Nhớ nội quy nhé: mỗi lần chỉ một người nói."),
  ("This is your first warning.", "Đây là lần nhắc nhở thứ nhất."),
  ("Can you tell me what you should be doing now?", "Em nói cô/thầy nghe bây giờ em nên làm gì?"),
  ("I'm going to move you to a different seat.", "Cô/thầy sẽ chuyển em sang chỗ khác."),
  ("Great teamwork! Your group gets a star.", "Làm việc nhóm tốt lắm! Nhóm em được một ngôi sao."),
  ("Let's talk after class.", "Mình nói chuyện sau giờ học nhé."),
  ("Phones go in your bag during lessons.", "Trong giờ học, điện thoại cất vào cặp."),
 ],
 "dialogues": [
  ("Two boys at the back keep talking. What should we do?", [
    ("I'll move closer and give them a quiet warning. If they continue, we'll change their seats.", True, "Xử lý nhẹ trước (đến gần + nhắc nhỏ), rồi mới áp dụng hệ quả."),
    ("Shout at them, they will stop.", False, "Quát học sinh không phải cách quản lý lớp hiệu quả, nhất là ở trường quốc tế."),
    ("Boys always talk, normal.", False, "Thiếu động từ ('It's normal') và bỏ mặc vấn đề."),
  ]),
  ("It wasn't me! Why do I have a warning?", [
    ("I saw you throw the paper. Let's talk about it calmly after class.", True, "Nêu hành vi cụ thể + bình tĩnh, nói riêng sau giờ."),
    ("Because I say so.", False, "Dùng quyền, không giải thích lý do."),
    ("You always make trouble.", False, "Gắn nhãn học sinh ('luôn luôn') thay vì nói về hành vi cụ thể."),
  ]),
  ("How do you get the class quiet so quickly?", [
    ("We have a routine. I raise my hand, and they raise theirs and stop talking.", True, "Chia sẻ nề nếp cụ thể, dễ áp dụng."),
    ("I am strict, they scared.", False, "Thiếu động từ ('they're scared') và quản lý lớp bằng nỗi sợ."),
    ("Quiet is easy, no need method.", False, "Sai cấu trúc ('you don't need a special method') và không chia sẻ được gì."),
  ]),
  ("How was Minh's behaviour this week?", [
    ("Much better. He stayed on task in most lessons, and he only needed one reminder on Tuesday.", True, "Nhận xét + dẫn chứng cụ thể."),
    ("Minh is bad boy but better.", False, "Gắn nhãn 'bad boy', thiếu mạo từ — hãy nói về hành vi, không phán xét con người."),
    ("Better, I think so, maybe.", False, "Mơ hồ, không có dẫn chứng."),
  ]),
  ("Should we give the whole class a reward today?", [
    ("Yes, they worked really well. Let's give them five extra minutes of game time.", True, "Đồng ý + lý do + phần thưởng cụ thể."),
    ("Yes, give candy all.", False, "Sai trật tự ('give everyone some candy') và không nói lý do thưởng."),
    ("Reward make them lazy.", False, "Sai chia động từ ('makes') và không trả lời theo tình huống."),
  ]),
 ],
 "listen": [
  ("Remember our rule: one person speaks at a time", ["rule", "person"], "nhắc nội quy"),
  ("This is your first warning", ["first", "warning"], "nhắc nhở"),
  ("Let's take a deep breath and calm down", ["breath", "calm"], "giúp học sinh bình tĩnh"),
  ("Thank you for being ready so quickly", ["ready", "quickly"], "khen chuẩn bị nhanh"),
  ("Everyone, eyes on me, please. You worked very well in your groups today. Each table gets two stars.", ["eyes", "groups", "stars"], "khen cả lớp"),
  ("Nam, you are talking again. This is your second warning. Please move to the seat near the window.", ["talking", "second", "window"], "nhắc nhở học sinh"),
 ],
})

# ───────────────────────── 2. Giáo án & chương trình ─────────────────────────
PHASES.append({
 "title": "Giáo án & chương trình",
 "vocab": [
  ("lesson plan", "/ˈlesn ˌplæn/", "n", "giáo án", "Please send me your <b>lesson plan</b> for Monday.", "Gửi tôi giáo án cho thứ Hai nhé."),
  ("curriculum", "/kəˈrɪkjələm/", "n", "chương trình học (khung chương trình)", "Our school follows a bilingual <b>curriculum</b>.", "Trường mình theo chương trình song ngữ."),
  ("learning objective", "/ˌlɜːnɪŋ əbˈdʒektɪv/", "n", "mục tiêu bài học", "Write the <b>learning objective</b> on the board at the start.", "Viết mục tiêu bài học lên bảng khi bắt đầu tiết."),
  ("scheme of work", "/ˌskiːm əv ˈwɜːk/", "n", "kế hoạch dạy học theo kỳ (phân phối chương trình)", "We're one week behind the <b>scheme of work</b>.", "Tụi mình đang chậm một tuần so với kế hoạch dạy học."),
  ("syllabus", "/ˈsɪləbəs/", "n", "đề cương môn học", "This topic isn't on the <b>syllabus</b> this year.", "Năm nay chủ đề này không có trong đề cương."),
  ("warm-up", "/ˈwɔːm ʌp/", "n", "hoạt động khởi động", "I'll start with a five-minute <b>warm-up</b> game.", "Tôi sẽ mở đầu bằng một trò chơi khởi động năm phút."),
  ("differentiation", "/ˌdɪfərenʃiˈeɪʃn/", "n", "dạy học phân hoá (theo trình độ)", "Good <b>differentiation</b> helps both strong and weak students.", "Phân hoá tốt giúp cả học sinh giỏi lẫn học sinh yếu."),
  ("resource", "/rɪˈzɔːs/", "n", "học liệu, tài nguyên dạy học", "Can we share <b>resources</b> for Unit 5?", "Mình chia sẻ học liệu cho Unit 5 được không?"),
  ("plenary", "/ˈpliːnəri/", "n", "phần tổng kết cuối tiết", "In the <b>plenary</b>, each group shares one idea.", "Ở phần tổng kết, mỗi nhóm chia sẻ một ý."),
  ("pace", "/peɪs/", "n", "tốc độ (dạy, học)", "The <b>pace</b> was a bit fast for Year 3.", "Tốc độ hơi nhanh so với lớp 3."),
 ],
 "phrases": [
  ("What's the learning objective for this lesson?", "Mục tiêu của tiết này là gì?"),
  ("I'll start with a short warm-up.", "Tôi sẽ mở đầu bằng một hoạt động khởi động ngắn."),
  ("This activity is too difficult for the lower group.", "Hoạt động này khó quá với nhóm yếu."),
  ("Let's prepare an easier version of the worksheet.", "Mình soạn một bản phiếu bài tập dễ hơn nhé."),
  ("We're one week behind the scheme of work.", "Tụi mình đang chậm một tuần so với kế hoạch dạy học."),
  ("Can we share resources for Unit 5?", "Mình chia sẻ học liệu cho Unit 5 được không?"),
  ("The pace was a bit fast for them.", "Tốc độ hơi nhanh với các em."),
  ("I'll finish with a quick plenary.", "Tôi sẽ kết thúc bằng phần tổng kết ngắn."),
  ("Does this topic follow the syllabus?", "Chủ đề này có đúng đề cương không?"),
  ("I'll upload the lesson plan to the shared folder.", "Tôi sẽ tải giáo án lên thư mục chung."),
 ],
 "dialogues": [
  ("What's your plan for tomorrow's lesson?", [
    ("We'll start with a vocabulary game, then read a short text, and finish with a speaking task.", True, "Nêu trình tự 3 phần rõ ràng."),
    ("Tomorrow I teach Unit 5.", False, "Sai thì ('I'll teach') và chỉ nói tên bài, chưa có kế hoạch."),
    ("Plan is in my head.", False, "Thiếu mạo từ và thiếu chuyên nghiệp — giáo án cần viết ra và chia sẻ."),
  ]),
  ("Some students finish early and get bored. Any ideas?", [
    ("Let's prepare an extension task for them, like writing two extra questions.", True, "Giải pháp phân hoá cụ thể cho học sinh làm nhanh."),
    ("They can sleep, no problem.", False, "Bỏ mặc học sinh — lãng phí thời gian học."),
    ("Give them more same exercises.", False, "Sai trật tự ('more of the same exercises') và chỉ thêm bài giống nhau, không nâng mức."),
  ]),
  ("Are we on track with the scheme of work?", [
    ("Not quite. We're about one week behind, so I'll combine Units 6 and 7.", True, "Tình trạng + mức chậm + cách bù."),
    ("Yes, sure, always on track.", False, "Trả lời chắc chắn mà không kiểm tra."),
    ("We are behind because many holiday.", False, "Sai ngữ pháp ('because of the holidays') và chưa có giải pháp."),
  ]),
  ("Can I see your lesson plan before the observation?", [
    ("Of course. I'll email it to you by Wednesday afternoon.", True, "Đồng ý + thời hạn cụ thể."),
    ("Why you want see?", False, "Sai cấu trúc câu hỏi ('Why do you want to see it?') và thiếu hợp tác."),
    ("OK, I send later.", False, "Thiếu 'will' và 'it'; 'later' quá mơ hồ."),
  ]),
  ("The reading text is too long for Year 3.", [
    ("You're right. Let's cut it to one paragraph and add some pictures.", True, "Đồng ý + điều chỉnh cụ thể."),
    ("They must try, it's good for them.", False, "Cứng nhắc, không điều chỉnh theo trình độ học sinh."),
    ("Text long, but OK.", False, "Thiếu động từ ('The text is long') và không xử lý."),
  ]),
 ],
 "listen": [
  ("The learning objective is on the board", ["learning", "board"], "mục tiêu bài học"),
  ("We will start with a short warm-up", ["short", "warm-up"], "khởi động"),
  ("This task is too difficult for the lower group", ["difficult", "lower"], "điều chỉnh độ khó"),
  ("Please upload your lesson plan by Friday", ["upload", "Friday"], "nộp giáo án"),
  ("We are one week behind the plan. Let's combine the last two units. I will update the scheme of work tonight.", ["behind", "combine", "update"], "bù chậm chương trình"),
  ("Today's plenary was great. The students explained the new words in their own way. Next time, let's give them more time.", ["plenary", "explained", "time"], "rút kinh nghiệm tiết dạy"),
 ],
})

# ───────────────────────── 3. Đánh giá & chấm bài ─────────────────────────
PHASES.append({
 "title": "Đánh giá & chấm bài",
 "vocab": [
  ("assessment", "/əˈsesmənt/", "n", "sự đánh giá; bài đánh giá", "We have a reading <b>assessment</b> next week.", "Tuần sau có bài đánh giá kỹ năng đọc."),
  ("mark", "/mɑːk/", "v/n", "chấm (bài); điểm", "I'll <b>mark</b> the tests this weekend.", "Cuối tuần này tôi sẽ chấm bài kiểm tra."),
  ("grade", "/ɡreɪd/", "n/v", "điểm, xếp loại; chấm xếp loại", "She got a good <b>grade</b> for her project.", "Em ấy được điểm cao cho dự án."),
  ("rubric", "/ˈruːbrɪk/", "n", "thang tiêu chí chấm (rubric)", "Please read the <b>rubric</b> before you start writing.", "Đọc thang tiêu chí chấm trước khi bắt đầu viết nhé."),
  ("quiz", "/kwɪz/", "n", "bài kiểm tra nhanh", "We'll have a short vocabulary <b>quiz</b> on Monday.", "Thứ Hai lớp mình kiểm tra nhanh từ vựng."),
  ("assignment", "/əˈsaɪnmənt/", "n", "bài tập được giao (thường làm dài ngày)", "The history <b>assignment</b> is two pages long.", "Bài tập môn sử dài hai trang."),
  ("deadline", "/ˈdedlaɪn/", "n", "hạn nộp", "The <b>deadline</b> for this project is next Monday.", "Hạn nộp dự án này là thứ Hai tuần sau."),
  ("plagiarism", "/ˈpleɪdʒərɪzəm/", "n", "đạo văn, chép bài người khác", "Copying from the internet is <b>plagiarism</b>.", "Chép từ trên mạng là đạo văn."),
  ("retake", "/ˌriːˈteɪk/", "v", "làm lại, thi lại (bài kiểm tra)", "You can <b>retake</b> the quiz on Thursday.", "Em có thể làm lại bài kiểm tra vào thứ Năm."),
  ("criteria", "/kraɪˈtɪəriə/", "n", "các tiêu chí", "There are four <b>criteria</b>: ideas, organisation, vocabulary and grammar.", "Có bốn tiêu chí: ý tưởng, bố cục, từ vựng và ngữ pháp."),
 ],
 "phrases": [
  ("I'll mark your tests by Friday.", "Thầy/cô sẽ chấm xong bài của các em trước thứ Sáu."),
  ("The deadline for this assignment is next Monday.", "Hạn nộp bài tập này là thứ Hai tuần sau."),
  ("Please read the rubric before you start writing.", "Đọc thang tiêu chí chấm trước khi viết nhé."),
  ("You got 7 out of 10 for content.", "Phần nội dung em được 7/10."),
  ("You lost marks because you didn't answer question 4.", "Em bị trừ điểm vì không trả lời câu 4."),
  ("Your ideas are good, but check your spelling.", "Ý tưởng của em tốt, nhưng nhớ kiểm tra chính tả."),
  ("This part looks copied from the internet. We need to talk about it.", "Phần này có vẻ chép từ trên mạng. Mình cần nói chuyện về việc này."),
  ("You can retake the quiz on Thursday.", "Em có thể làm lại bài kiểm tra vào thứ Năm."),
  ("Could we check each other's marking?", "Mình kiểm tra chéo phần chấm bài của nhau được không?"),
  ("Please show your working.", "Các em nhớ ghi cả cách làm nhé."),
 ],
 "dialogues": [
  ("Why did I get a C on my essay?", [
    ("Your ideas are clear, but you didn't give examples. Look at the rubric — examples are 30 percent of the grade.", True, "Chỉ ra điểm tốt + lý do mất điểm + căn cứ theo rubric."),
    ("Because your essay is not good.", False, "Nhận xét chung chung, không giúp học sinh sửa."),
    ("C is OK, not bad what.", False, "Dịch kiểu chữ 'mà' tiếng Việt và không trả lời câu hỏi."),
  ]),
  ("Can my son hand in his project late? He was sick.", [
    ("Of course. Please send a note from the doctor, and he can hand it in next Wednesday.", True, "Thông cảm + điều kiện + hạn mới."),
    ("No, deadline is deadline.", False, "Cứng nhắc, bỏ qua lý do chính đáng."),
    ("He can send when he free.", False, "Thiếu động từ ('when he's free') và không có hạn cụ thể."),
  ]),
  ("Two essays are almost the same. What should we do?", [
    ("Let's check them carefully first, then talk to both students separately.", True, "Kiểm tra trước + nói riêng từng em — đúng cách xử lý nghi vấn chép bài."),
    ("Give zero both, done.", False, "Kết luận vội, sai ngữ pháp ('Give them both a zero')."),
    ("Maybe they are friends, it's normal.", False, "Bỏ qua dấu hiệu đạo văn."),
  ]),
  ("When will the test marks be ready?", [
    ("I've marked half of them. I'll enter all the marks into the system by Thursday.", True, "Tiến độ + hạn cụ thể."),
    ("Soon, I am marking.", False, "Mơ hồ, không có hạn."),
    ("Marks ready yesterday already.", False, "Thiếu động từ ('were ready') và mâu thuẫn với câu hỏi."),
  ]),
  ("Can I retake the quiz? I only got four out of ten.", [
    ("Yes. Review Unit 3 tonight, and you can retake it on Thursday at lunchtime.", True, "Đồng ý + cách ôn + thời gian cụ thể."),
    ("Four is low, you must study more hard.", False, "Sai so sánh hơn ('harder') và chỉ trách mà không trả lời."),
    ("Retake is not possible maybe.", False, "Mơ hồ ('maybe') — cần trả lời rõ có hay không."),
  ]),
 ],
 "listen": [
  ("The deadline for this assignment is Monday", ["deadline", "Monday"], "hạn nộp bài"),
  ("Please read the rubric before you start", ["rubric", "start"], "đọc tiêu chí chấm"),
  ("You can retake the quiz on Thursday", ["retake", "Thursday"], "làm lại bài kiểm tra"),
  ("I will mark your tests this weekend", ["mark", "weekend"], "lịch chấm bài"),
  ("Your essay has good ideas. However, you need more examples. Please check the rubric and try again.", ["ideas", "examples", "rubric"], "nhận xét bài luận"),
  ("The test is on Friday. It has three parts: reading, writing and listening. Please bring a pencil.", ["Friday", "listening", "pencil"], "thông báo bài kiểm tra"),
 ],
})

# ───────────────────────── 4. Họp phụ huynh ─────────────────────────
PHASES.append({
 "title": "Họp phụ huynh",
 "vocab": [
  ("parent-teacher meeting", "/ˌpeərənt ˈtiːtʃə ˌmiːtɪŋ/", "n", "buổi họp giữa phụ huynh và giáo viên", "The <b>parent-teacher meeting</b> is next Saturday morning.", "Buổi họp phụ huynh là sáng thứ Bảy tuần sau."),
  ("concern", "/kənˈsɜːn/", "n", "mối lo, điều băn khoăn", "Do you have any <b>concerns</b> about her progress?", "Anh/chị có băn khoăn gì về việc học của cháu không?"),
  ("strength", "/streŋθ/", "n", "điểm mạnh", "Speaking is his biggest <b>strength</b>.", "Nói là điểm mạnh nhất của cháu."),
  ("weakness", "/ˈwiːknəs/", "n", "điểm yếu", "Her main <b>weakness</b> is spelling.", "Điểm yếu chính của cháu là chính tả."),
  ("attitude", "/ˈætɪtjuːd/", "n", "thái độ", "He has a very positive <b>attitude</b> in class.", "Cháu có thái độ học rất tích cực."),
  ("confidence", "/ˈkɒnfɪdəns/", "n", "sự tự tin", "Her <b>confidence</b> has grown a lot this term.", "Học kỳ này cháu tự tin hơn nhiều."),
  ("homework", "/ˈhəʊmwɜːk/", "n", "bài tập về nhà", "The <b>homework</b> takes about 30 minutes a day.", "Bài tập về nhà mất khoảng 30 phút mỗi ngày."),
  ("appointment", "/əˈpɔɪntmənt/", "n", "cuộc hẹn", "Can I make an <b>appointment</b> with the class teacher?", "Tôi đặt lịch hẹn gặp giáo viên chủ nhiệm được không?"),
  ("interpreter", "/ɪnˈtɜːprɪtə/", "n", "phiên dịch viên (nói)", "We can arrange an <b>interpreter</b> for the meeting.", "Trường có thể bố trí phiên dịch cho buổi họp."),
  ("follow up", "/ˌfɒləʊ ˈʌp/", "phr v", "theo dõi, trao đổi tiếp", "I'll <b>follow up</b> with you in two weeks.", "Hai tuần nữa tôi sẽ trao đổi lại với anh/chị."),
 ],
 "phrases": [
  ("Thank you for coming today.", "Cảm ơn anh/chị hôm nay đã đến."),
  ("Anna is a very kind and helpful student.", "Anna là một học sinh rất tốt bụng và hay giúp đỡ bạn."),
  ("Her reading has improved a lot this term.", "Học kỳ này kỹ năng đọc của cháu tiến bộ nhiều."),
  ("One area to work on is her writing.", "Một phần cháu cần cố gắng thêm là kỹ năng viết."),
  ("Do you have any concerns?", "Anh/chị có băn khoăn gì không?"),
  ("At home, you can read with him for 15 minutes a day.", "Ở nhà, anh/chị có thể đọc sách cùng cháu 15 phút mỗi ngày."),
  ("I'll follow up with you in two weeks.", "Hai tuần nữa tôi sẽ trao đổi lại với anh/chị."),
  ("Would you like an interpreter for the meeting?", "Anh/chị có cần phiên dịch cho buổi họp không?"),
  ("Let's book another appointment for next month.", "Mình hẹn thêm một buổi vào tháng sau nhé."),
  ("Please contact me by email if you have any questions.", "Nếu có câu hỏi gì, anh/chị cứ email cho tôi nhé."),
 ],
 "dialogues": [
  ("How is my daughter doing in class?", [
    ("She's doing well. She's confident in speaking, and her reading has improved. Her next step is to write longer sentences.", True, "Điểm mạnh + tiến bộ + bước tiếp theo."),
    ("She is good girl, no problem.", False, "Thiếu mạo từ ('a good girl') và quá chung chung."),
    ("Your daughter so-so.", False, "Thiếu động từ và nghe thiếu tôn trọng — cần nói cụ thể, tích cực."),
  ]),
  ("My son says he's bored in class.", [
    ("Thank you for telling me. I'll give him more challenging tasks and check how he feels next week.", True, "Cảm ơn + hành động + theo dõi."),
    ("He is not bored, he is lazy.", False, "Phủ nhận cảm xúc của học sinh và gắn nhãn."),
    ("All students is bored sometimes.", False, "Sai chia động từ ('are') và gạt đi mối lo của phụ huynh."),
  ]),
  ("Why does he get so much homework?", [
    ("It's about 30 minutes a day. It helps him practise what we learn in class, but I can check if it's too much for him.", True, "Con số + mục đích + sẵn sàng điều chỉnh."),
    ("School rule, I can't do anything.", False, "Đẩy trách nhiệm, không giải thích mục đích."),
    ("Homework is not so much, other class more.", False, "So sánh vụng, thiếu động từ, không trả lời mối lo."),
  ]),
  ("Can we meet next week to talk more?", [
    ("Of course. Are you free on Tuesday at 4 p.m.? We can meet in Room 205.", True, "Đồng ý + đề xuất giờ và địa điểm cụ thể."),
    ("OK, when you want.", False, "Sai cấu trúc ('whenever you like') và không chốt lịch."),
    ("Next week I busy.", False, "Thiếu động từ ('I'm busy') và từ chối không đưa lựa chọn khác."),
  ]),
  ("I think the other kids are not kind to my son.", [
    ("I'm sorry to hear that. Can you tell me what he said? I'll watch closely and talk to the school counsellor.", True, "Đồng cảm + hỏi thông tin + hành động nghiêm túc."),
    ("Kids play like that, normal.", False, "Xem nhẹ — có thể là bắt nạt, phải tìm hiểu."),
    ("I never see this.", False, "Sai thì ('I've never seen that') và phủ nhận ngay."),
  ]),
 ],
 "listen": [
  ("Thank you for coming to the meeting today", ["coming", "meeting"], "mở đầu buổi họp"),
  ("Her reading has improved a lot this term", ["reading", "improved"], "báo tiến bộ"),
  ("Do you have any concerns about your son", ["concerns", "son"], "hỏi băn khoăn"),
  ("I will follow up with you in two weeks", ["follow", "weeks"], "hẹn trao đổi tiếp"),
  ("Leo is a kind and helpful student. His speaking is very good. One area to work on is his spelling.", ["kind", "speaking", "spelling"], "nhận xét với phụ huynh"),
  ("Please read with your child at home every day. Fifteen minutes is enough. You can ask simple questions about the story.", ["home", "Fifteen", "story"], "gợi ý phụ huynh hỗ trợ ở nhà"),
 ],
})

# ───────────────────────── 5. Tư vấn tuyển sinh ─────────────────────────
PHASES.append({
 "title": "Tư vấn tuyển sinh",
 "vocab": [
  ("admissions", "/ədˈmɪʃnz/", "n", "(phòng) tuyển sinh", "Please call the <b>admissions</b> office to book a visit.", "Anh/chị gọi phòng tuyển sinh để đặt lịch tham quan nhé."),
  ("enrolment", "/ɪnˈrəʊlmənt/", "n", "việc nhập học, ghi danh", "<b>Enrolment</b> for next year starts in March.", "Việc ghi danh cho năm học sau bắt đầu từ tháng Ba."),
  ("entrance test", "/ˈentrəns ˌtest/", "n", "bài kiểm tra đầu vào", "The <b>entrance test</b> takes about one hour.", "Bài kiểm tra đầu vào mất khoảng một tiếng."),
  ("tuition fee", "/tjuˈɪʃn ˌfiː/", "n", "học phí", "The <b>tuition fee</b> can be paid by term or by year.", "Học phí có thể đóng theo kỳ hoặc theo năm."),
  ("application form", "/ˌæplɪˈkeɪʃn ˌfɔːm/", "n", "đơn đăng ký", "Please fill in the <b>application form</b> online.", "Anh/chị điền đơn đăng ký trực tuyến nhé."),
  ("campus tour", "/ˈkæmpəs ˌtʊə/", "n", "buổi tham quan trường", "Would you like a <b>campus tour</b> after the meeting?", "Sau buổi gặp anh/chị có muốn tham quan trường không?"),
  ("waiting list", "/ˈweɪtɪŋ ˌlɪst/", "n", "danh sách chờ", "Grade 3 is full, but we can put her on the <b>waiting list</b>.", "Lớp 3 đã đủ chỗ, nhưng trường có thể đưa cháu vào danh sách chờ."),
  ("deposit", "/dɪˈpɒzɪt/", "n", "tiền đặt cọc giữ chỗ", "Please pay the <b>deposit</b> to hold the place.", "Anh/chị đóng tiền cọc để giữ chỗ nhé."),
  ("sibling discount", "/ˈsɪblɪŋ ˌdɪskaʊnt/", "n", "ưu đãi học phí cho anh chị em ruột", "Your second child can get a <b>sibling discount</b>.", "Bé thứ hai nhà mình được hưởng ưu đãi anh chị em."),
  ("trial class", "/ˈtraɪəl ˌklɑːs/", "n", "buổi học thử", "Your son can join a free <b>trial class</b> on Friday.", "Thứ Sáu bé có thể học thử miễn phí một buổi."),
 ],
 "phrases": [
  ("Which grade is your child applying for?", "Bé nhà mình đăng ký vào lớp mấy ạ?"),
  ("Would you like a campus tour?", "Anh/chị có muốn tham quan trường không?"),
  ("The entrance test includes English and maths.", "Bài kiểm tra đầu vào gồm tiếng Anh và toán."),
  ("Class sizes are around 20 students.", "Mỗi lớp khoảng 20 học sinh."),
  ("Here is our fee schedule for this school year.", "Đây là biểu học phí năm học này."),
  ("Your child can join a free trial class.", "Bé có thể học thử một buổi miễn phí."),
  ("We have a 10 percent discount for siblings.", "Trường giảm 10% cho anh chị em ruột."),
  ("Grade 3 is full at the moment, but we have a waiting list.", "Lớp 3 hiện đã đủ chỗ, nhưng có danh sách chờ."),
  ("Please fill in the application form and bring a copy of the school report.", "Anh/chị điền đơn đăng ký và mang theo bản sao học bạ nhé."),
  ("I'll call you when the test results are ready.", "Khi có kết quả kiểm tra, tôi sẽ gọi cho anh/chị."),
 ],
 "dialogues": [
  ("What curriculum do you follow?", [
    ("We follow a bilingual curriculum: the Vietnamese programme in the morning, and English, maths and science in English in the afternoon.", True, "Trả lời rõ cấu trúc chương trình."),
    ("Our curriculum is very good, best in city.", False, "Quảng cáo chung chung, thiếu mạo từ ('the best in the city')."),
    ("Many subjects, many English.", False, "Sai danh từ không đếm được ('a lot of English') và không trả lời được câu hỏi."),
  ]),
  ("How much are the tuition fees?", [
    ("For Grade 3, it's about 250 million dong a year. Here's the full fee schedule, including the bus and lunch.", True, "Con số + tài liệu chi tiết + các khoản đi kèm."),
    ("Very cheap, don't worry.", False, "Né con số — phụ huynh cần thông tin rõ ràng."),
    ("Fee is depend on grade.", False, "Sai cấu trúc ('It depends on the grade') và chưa đưa con số."),
  ]),
  ("My son doesn't speak English yet. Can he still apply?", [
    ("Yes, he can. We have an English support programme for new students, and he'll do a short placement test first.", True, "Trấn an + giải pháp hỗ trợ + bước tiếp theo."),
    ("No English, no school.", False, "Cộc lốc, từ chối thô và có thể sai chính sách."),
    ("He can apply, but maybe he cannot follow.", False, "Gây lo lắng mà không nêu cách hỗ trợ."),
  ]),
  ("Is there a place in Grade 5 for next month?", [
    ("Grade 5 is full right now, but I can put your daughter on the waiting list and call you if a place opens.", True, "Thông tin thật + phương án + cam kết liên hệ."),
    ("Full, sorry, bye.", False, "Cộc lốc, bỏ lỡ cơ hội tuyển sinh."),
    ("Maybe have, maybe not.", False, "Thiếu chủ ngữ, mơ hồ."),
  ]),
  ("What happens after the entrance test?", [
    ("We'll send you the results within three working days. If your child passes, you pay a deposit to hold the place.", True, "Quy trình rõ từng bước + thời gian."),
    ("After test, you wait.", False, "Thiếu mạo từ ('After the test') và không nói rõ chờ bao lâu, làm gì."),
    ("Test result come fast.", False, "Sai chia động từ ('The results come') và không nói bước tiếp theo."),
  ]),
 ],
 "listen": [
  ("Which grade is your child applying for", ["grade", "applying"], "hỏi lớp đăng ký"),
  ("The entrance test includes English and maths", ["entrance", "maths"], "bài kiểm tra đầu vào"),
  ("Grade five is full, but we have a waiting list", ["full", "waiting"], "danh sách chờ"),
  ("Your child can join a free trial class", ["free", "trial"], "học thử"),
  ("Welcome to our school. Today we will visit the library, the science lab and the swimming pool. The tour takes about forty minutes.", ["library", "swimming", "forty"], "dẫn tham quan trường"),
  ("The test has two parts: English and maths. It takes one hour. We will call you with the results on Friday.", ["parts", "hour", "results"], "giải thích bài kiểm tra đầu vào"),
 ],
})

# ───────────────────────── 6. Làm việc với giáo viên nước ngoài ─────────────────────────
PHASES.append({
 "title": "Làm việc với giáo viên nước ngoài",
 "vocab": [
  ("co-teacher", "/ˌkəʊ ˈtiːtʃə/", "n", "giáo viên cùng dạy (đồng giảng)", "My <b>co-teacher</b> leads the speaking part.", "Giáo viên cùng dạy với tôi phụ trách phần nói."),
  ("native speaker", "/ˌneɪtɪv ˈspiːkə/", "n", "người bản ngữ", "Our school has six <b>native speakers</b> in the English department.", "Tổ tiếng Anh trường mình có sáu giáo viên bản ngữ."),
  ("planning meeting", "/ˈplænɪŋ ˌmiːtɪŋ/", "n", "buổi họp soạn bài chung", "Our <b>planning meeting</b> is every Tuesday at 3 p.m.", "Buổi họp soạn bài là 3 giờ chiều thứ Ba hằng tuần."),
  ("cover", "/ˈkʌvə/", "v/n", "dạy thay; tiết dạy thay", "Can you <b>cover</b> my class on Friday?", "Thứ Sáu anh dạy thay lớp tôi được không?"),
  ("department", "/dɪˈpɑːtmənt/", "n", "tổ bộ môn", "The science <b>department</b> meets on Wednesdays.", "Tổ khoa học họp vào thứ Tư."),
  ("head of department", "/ˌhed əv dɪˈpɑːtmənt/", "n", "tổ trưởng chuyên môn", "Please send the test to the <b>head of department</b> for checking.", "Gửi đề kiểm tra cho tổ trưởng chuyên môn duyệt nhé."),
  ("staff room", "/ˈstɑːf ˌruːm/", "n", "phòng giáo viên", "The <b>staff room</b> is on the second floor.", "Phòng giáo viên ở tầng hai."),
  ("work permit", "/ˈwɜːk ˌpɜːmɪt/", "n", "giấy phép lao động", "HR needs your documents for the <b>work permit</b>.", "Phòng nhân sự cần giấy tờ của anh để làm giấy phép lao động."),
  ("culture shock", "/ˈkʌltʃə ˌʃɒk/", "n", "sốc văn hoá", "Many new teachers feel some <b>culture shock</b> in the first month.", "Nhiều giáo viên mới bị sốc văn hoá một chút trong tháng đầu."),
  ("translate", "/trænsˈleɪt/", "v", "dịch", "I can <b>translate</b> the key words if the kids get lost.", "Nếu các em không theo kịp, tôi có thể dịch các từ khoá."),
 ],
 "phrases": [
  ("Shall we plan next week's lessons together on Monday?", "Thứ Hai mình cùng soạn bài cho tuần sau nhé?"),
  ("You lead the speaking part, and I'll support the weaker students.", "Anh phụ trách phần nói, còn tôi hỗ trợ các em yếu hơn."),
  ("Can you cover my Year 4 class on Friday?", "Thứ Sáu anh dạy thay lớp 4 của tôi được không?"),
  ("I can translate the instructions if the kids get lost.", "Nếu các em không hiểu, tôi có thể dịch phần hướng dẫn."),
  ("In Vietnam, parents often message the teacher directly.", "Ở Việt Nam, phụ huynh hay nhắn tin trực tiếp cho giáo viên."),
  ("Let me explain how things work here.", "Để tôi giải thích mọi việc ở đây vận hành thế nào."),
  ("The staff room is on the second floor.", "Phòng giáo viên ở tầng hai."),
  ("How are you settling in?", "Anh thấy đã quen dần với mọi thứ chưa?"),
  ("Let's agree on the rules before class starts.", "Mình thống nhất nội quy trước khi vào lớp nhé."),
  ("Could you speak a bit more slowly for the younger kids?", "Anh nói chậm hơn một chút cho các em nhỏ được không?"),
 ],
 "dialogues": [
  ("Should I explain everything in English, or will you translate?", [
    ("Let's keep it in English. I'll only translate key words if some students look lost.", True, "Thống nhất vai trò + ưu tiên tiếng Anh, chỉ dịch khi cần."),
    ("I translate all, faster.", False, "Thiếu 'will'; dịch hết khiến học sinh không được nghe tiếng Anh."),
    ("You speak, I am quiet.", False, "Giáo viên cùng dạy nên hỗ trợ tích cực, không đứng im."),
  ]),
  ("Why do parents keep messaging me at night?", [
    ("Here it's quite common for parents to message teachers directly. We can set clear contact hours and share them at the parent meeting.", True, "Giải thích văn hoá + đề xuất giải pháp."),
    ("Vietnamese parents like that, you must accept.", False, "Áp đặt, không giúp đồng nghiệp tìm cách xử lý."),
    ("Just block them.", False, "Cách xử lý thiếu chuyên nghiệp."),
  ]),
  ("Can you cover my class tomorrow? I have a doctor's appointment.", [
    ("Sure. Could you leave the lesson plan and the worksheets on your desk?", True, "Đồng ý + xin tài liệu để dạy thay."),
    ("OK, but I don't know what teach.", False, "Sai cấu trúc ('what to teach') và chưa hỏi tài liệu."),
    ("Tomorrow I am busy all, sorry.", False, "Sai trật tự ('busy all day') và không gợi ý người khác."),
  ]),
  ("I don't understand the school's reporting system.", [
    ("No problem. Let's sit together after school today, and I'll show you step by step.", True, "Sẵn lòng + thời gian cụ thể + cách hỗ trợ."),
    ("It's easy, you read the guide.", False, "Gạt đi — đồng nghiệp mới cần được hướng dẫn."),
    ("System very difficult, I also don't know.", False, "Thiếu động từ ('The system is…') và không giúp được."),
  ]),
  ("How do you think today's lesson went?", [
    ("The warm-up was great, but the group task was a bit long. Maybe next time we can give clearer roles.", True, "Nhận xét cân bằng + góp ý cụ thể, lịch sự."),
    ("Everything perfect.", False, "Thiếu động từ và không có góp ý thật."),
    ("Your lesson is too boring.", False, "Chê thẳng, thiếu tế nhị và không có đề xuất."),
  ]),
 ],
 "listen": [
  ("Can you cover my class on Friday", ["cover", "Friday"], "nhờ dạy thay"),
  ("Let's plan next week's lessons together", ["plan", "together"], "soạn bài chung"),
  ("The staff room is on the second floor", ["staff", "second"], "chỉ đường cho GV mới"),
  ("I will translate the key words", ["translate", "key"], "phân vai khi cùng dạy"),
  ("Welcome to the English department. Our planning meeting is every Tuesday at three. Please bring your ideas for the next unit.", ["department", "Tuesday", "ideas"], "chào đón giáo viên mới"),
  ("Tomorrow you will lead the speaking activity. I will help the weaker students. After class, let's talk about how it went.", ["lead", "weaker", "talk"], "phân công cùng dạy"),
 ],
})

# ───────────────────────── 7. An toàn & chăm sóc học sinh ─────────────────────────
PHASES.append({
 "title": "An toàn & chăm sóc học sinh",
 "vocab": [
  ("safeguarding", "/ˈseɪfɡɑːdɪŋ/", "n", "bảo vệ an toàn trẻ em, học sinh", "Every new teacher has <b>safeguarding</b> training in the first week.", "Giáo viên mới nào cũng được tập huấn bảo vệ học sinh trong tuần đầu."),
  ("pick-up", "/ˈpɪk ʌp/", "n", "việc đón (học sinh)", "<b>Pick-up</b> time is 4:30 at the main gate.", "Giờ đón học sinh là 4 giờ 30 ở cổng chính."),
  ("school nurse", "/ˌskuːl ˈnɜːs/", "n", "nhân viên y tế trường", "Let's take her to the <b>school nurse</b>.", "Mình đưa cháu xuống phòng y tế nhé."),
  ("allergy", "/ˈælədʒi/", "n", "dị ứng", "Does your child have any food <b>allergies</b>?", "Bé có bị dị ứng thực phẩm nào không?"),
  ("bullying", "/ˈbʊliɪŋ/", "n", "bắt nạt", "We take <b>bullying</b> very seriously.", "Trường rất nghiêm túc với chuyện bắt nạt."),
  ("supervise", "/ˈsuːpəvaɪz/", "v", "trông coi, giám sát", "Two teachers <b>supervise</b> the playground at break time.", "Giờ ra chơi có hai giáo viên trông sân."),
  ("duty", "/ˈdjuːti/", "n", "ca trực", "I'm on playground <b>duty</b> at lunchtime.", "Giờ trưa tôi trực sân chơi."),
  ("wellbeing", "/ˌwelˈbiːɪŋ/", "n", "sức khoẻ tinh thần và thể chất, sự khoẻ mạnh toàn diện", "Student <b>wellbeing</b> is as important as grades.", "Sức khoẻ tinh thần của học sinh quan trọng không kém điểm số."),
  ("injury", "/ˈɪndʒəri/", "n", "chấn thương", "Please report every <b>injury</b> to the office.", "Mọi chấn thương đều phải báo lên văn phòng."),
  ("emergency contact", "/ɪˌmɜːdʒənsi ˈkɒntækt/", "n", "người liên hệ khẩn cấp", "Please update your <b>emergency contact</b> details.", "Anh/chị vui lòng cập nhật thông tin người liên hệ khẩn cấp."),
 ],
 "phrases": [
  ("Only authorised adults can pick up the children.", "Chỉ người lớn đã đăng ký mới được đón các bé."),
  ("Please wait with me until your parents arrive.", "Em đợi cùng cô/thầy cho đến khi bố mẹ tới nhé."),
  ("Does he have any allergies?", "Cháu có bị dị ứng gì không?"),
  ("Let's take her to the school nurse.", "Mình đưa cháu xuống phòng y tế nhé."),
  ("I'm on playground duty today.", "Hôm nay tôi trực sân chơi."),
  ("If a child tells you something worrying, report it to the safeguarding lead.", "Nếu học sinh kể điều gì đáng lo, hãy báo cho người phụ trách bảo vệ học sinh."),
  ("Don't promise to keep it a secret.", "Đừng hứa giữ bí mật (khi học sinh kể chuyện đáng lo)."),
  ("Are you OK? Do you want to talk?", "Em có ổn không? Em có muốn nói chuyện không?"),
  ("Please update your emergency contact details.", "Anh/chị cập nhật thông tin liên hệ khẩn cấp giúp tôi nhé."),
  ("I'll write an incident report and call the parents.", "Tôi sẽ viết biên bản sự việc và gọi cho phụ huynh."),
 ],
 "dialogues": [
  ("Hi, I'm here to pick up Mai. I'm her uncle.", [
    ("Hello. I'm sorry, you're not on her pick-up list. Please wait here while I call her mother.", True, "Lịch sự nhưng đúng quy trình: không có trong danh sách đón thì gọi phụ huynh xác nhận."),
    ("OK, uncle is family, you can take her.", False, "Rất nguy hiểm — không giao học sinh cho người không có trong danh sách đón."),
    ("No list, no child, go away.", False, "Đúng nguyên tắc nhưng thô lỗ — cần lịch sự và giải thích."),
  ]),
  ("Teacher, I fell down and my knee hurts.", [
    ("Let me see. OK, let's go to the school nurse, and I'll tell your mum after school.", True, "Kiểm tra + đưa xuống y tế + báo phụ huynh."),
    ("It's small, you go play.", False, "Xem nhẹ chấn thương, sai cấu trúc ('go and play')."),
    ("Why you run so fast?", False, "Trách học sinh, sai cấu trúc câu hỏi ('Why were you running…?')."),
  ]),
  ("Can I tell you a secret? You can't tell anyone.", [
    ("You can talk to me. I can't promise to keep it a secret, but I'll only tell people who can help you.", True, "Đúng nguyên tắc bảo vệ học sinh: không hứa giữ bí mật, chỉ báo người có trách nhiệm."),
    ("Yes, I promise, I never tell anybody.", False, "Sai nguyên tắc — nếu em gặp nguy hiểm, giáo viên phải báo người phụ trách."),
    ("Secret later, now we study.", False, "Gạt đi — có thể bỏ lỡ dấu hiệu học sinh cần giúp."),
  ]),
  ("Does anyone in this class have food allergies?", [
    ("Yes, Bảo is allergic to peanuts. His medicine is in the nurse's office, and there's a note on the class list.", True, "Tên + dị ứng gì + thuốc để ở đâu."),
    ("I think no, maybe.", False, "Mơ hồ — thông tin dị ứng phải chắc chắn."),
    ("Allergy is not my job.", False, "Sai — mọi giáo viên phải biết học sinh nào bị dị ứng."),
  ]),
  ("I heard some older students took Nam's snack money.", [
    ("Thank you. I'll talk to Nam privately first, then report it to the safeguarding lead today.", True, "Nói riêng với học sinh + báo người phụ trách ngay trong ngày."),
    ("Boys play together, not bullying.", False, "Xem nhẹ dấu hiệu bắt nạt."),
    ("Nam should be strong.", False, "Đổ trách nhiệm cho học sinh bị bắt nạt."),
  ]),
 ],
 "listen": [
  ("Only authorised adults can pick up the children", ["authorised", "pick"], "quy định đón học sinh"),
  ("Does your son have any allergies", ["son", "allergies"], "hỏi về dị ứng"),
  ("I am on playground duty at lunchtime", ["playground", "lunchtime"], "ca trực"),
  ("Please take her to the school nurse", ["take", "nurse"], "đưa xuống y tế"),
  ("Tom fell in the playground this morning. The nurse cleaned his knee and put on a plaster. He is fine now.", ["playground", "knee", "fine"], "báo phụ huynh về chấn thương nhẹ"),
  ("If a student tells you something worrying, listen calmly. Do not promise to keep it secret. Report it to the safeguarding lead today.", ["calmly", "promise", "Report"], "nguyên tắc bảo vệ học sinh"),
 ],
})

# ───────────────────────── 8. Dạy online ─────────────────────────
PHASES.append({
 "title": "Dạy online",
 "vocab": [
  ("breakout room", "/ˈbreɪkaʊt ˌruːm/", "n", "phòng nhóm nhỏ (khi học online)", "I'll put you into <b>breakout rooms</b> for ten minutes.", "Thầy/cô sẽ chia các em vào phòng nhóm nhỏ trong mười phút."),
  ("mute", "/mjuːt/", "v/adj", "tắt tiếng; đang tắt tiếng", "Please <b>mute</b> your microphone when you're not speaking.", "Khi không nói thì các em tắt mic nhé."),
  ("webcam", "/ˈwebkæm/", "n", "camera máy tính (webcam)", "My <b>webcam</b> isn't working today.", "Hôm nay camera máy tính của tôi bị hỏng."),
  ("connection", "/kəˈnekʃn/", "n", "kết nối (mạng)", "Your <b>connection</b> is weak, so your video keeps stopping.", "Mạng của em yếu nên hình cứ bị đứng."),
  ("chat box", "/ˈtʃæt ˌbɒks/", "n", "khung chat", "Type your answer in the <b>chat box</b>.", "Các em gõ đáp án vào khung chat nhé."),
  ("recording", "/rɪˈkɔːdɪŋ/", "n", "bản ghi hình", "The <b>recording</b> will be on the platform after class.", "Sau giờ học, bản ghi hình sẽ có trên nền tảng."),
  ("link", "/lɪŋk/", "n", "đường dẫn (link)", "I'll send the <b>link</b> again in the chat.", "Tôi sẽ gửi lại đường link trong khung chat."),
  ("lag", "/læɡ/", "v/n", "giật, trễ (hình, tiếng); độ trễ", "The video <b>lags</b> when too many cameras are on.", "Khi bật quá nhiều camera thì video bị giật."),
  ("platform", "/ˈplætfɔːm/", "n", "nền tảng (học trực tuyến)", "All homework is on the learning <b>platform</b>.", "Mọi bài tập về nhà đều có trên nền tảng học tập."),
  ("log in", "/ˌlɒɡ ˈɪn/", "phr v", "đăng nhập", "Please <b>log in</b> five minutes before class starts.", "Các em đăng nhập trước giờ học năm phút nhé."),
 ],
 "phrases": [
  ("Can everyone hear me?", "Mọi người có nghe thấy tôi không?"),
  ("Please turn on your camera.", "Các em bật camera lên nhé."),
  ("You're on mute. Please unmute yourself.", "Em đang tắt mic. Em bật mic lên nhé."),
  ("Type your answer in the chat box.", "Gõ đáp án vào khung chat nhé."),
  ("I'm going to share my screen now.", "Bây giờ thầy/cô chia sẻ màn hình nhé."),
  ("I'll put you into breakout rooms for ten minutes.", "Thầy/cô sẽ chia các em vào phòng nhóm nhỏ trong mười phút."),
  ("Your voice is breaking up. Can you say that again?", "Tiếng của em bị rè, đứt quãng. Em nói lại được không?"),
  ("The recording will be on the platform after class.", "Bản ghi hình sẽ có trên nền tảng sau giờ học."),
  ("I'll send the link again in the chat.", "Tôi sẽ gửi lại link trong khung chat."),
  ("Please log in five minutes before class starts.", "Các em đăng nhập trước giờ học năm phút nhé."),
 ],
 "dialogues": [
  ("Teacher, I can't hear you.", [
    ("Sorry, let me check my microphone. Can you hear me now?", True, "Xin lỗi + kiểm tra + xác nhận lại."),
    ("You check your computer.", False, "Đổ cho học sinh khi chưa kiểm tra phía mình."),
    ("I speak loud already.", False, "Sai thì và trạng từ ('I'm already speaking loudly') và không giải quyết lỗi kỹ thuật."),
  ]),
  ("My daughter missed the online class because of the internet.", [
    ("No problem. The recording is on the platform, and I've sent her the homework by email.", True, "Trấn an + đưa bản ghi + gửi bài tập."),
    ("Internet is her problem.", False, "Thiếu mạo từ và đẩy trách nhiệm."),
    ("She must come next time.", False, "Không giúp em bù phần đã lỡ."),
  ]),
  ("The students are very quiet online. How can we get them to talk?", [
    ("Let's use breakout rooms with three students each and give each group one clear question.", True, "Giải pháp cụ thể: nhóm nhỏ + câu hỏi rõ."),
    ("Online is always quiet, nothing to do.", False, "Buông xuôi, không có giải pháp."),
    ("Tell them talk more.", False, "Sai cấu trúc ('Tell them to talk more') và không hiệu quả."),
  ]),
  ("Where is the link for tomorrow's class?", [
    ("It's on the class platform, under 'Timetable'. I'll also post it in the chat tonight.", True, "Chỉ đúng chỗ + gửi thêm lần nữa."),
    ("I sent already, you find.", False, "Sai thì ('I've already sent it') và thiếu hỗ trợ."),
    ("Link same same yesterday.", False, "Lặp 'same same', thiếu 'as' — cần nói rõ link ở đâu."),
  ]),
  ("Your screen froze for five minutes during class.", [
    ("Yes, my connection dropped. I switched to my phone's hotspot, and next time I'll test it before class.", True, "Xác nhận + xử lý tức thời + phòng ngừa."),
    ("Internet in Vietnam is slow, not my fault.", False, "Đổ lỗi chung chung, không có kế hoạch phòng ngừa."),
    ("Screen freeze, I don't know why.", False, "Sai thì ('froze') và không có giải pháp."),
  ]),
 ],
 "listen": [
  ("Please turn on your camera", ["turn", "camera"], "bật camera"),
  ("You are on mute right now", ["mute", "now"], "nhắc tắt mic"),
  ("Type your answer in the chat box", ["answer", "chat"], "trả lời qua khung chat"),
  ("I will share my screen now", ["share", "screen"], "chia sẻ màn hình"),
  ("Now I will put you into breakout rooms. You have ten minutes. When you come back, one person will share your answers.", ["breakout", "ten", "share"], "chia nhóm online"),
  ("Your voice is breaking up. Please check your connection. You can also type your question in the chat.", ["voice", "connection", "type"], "xử lý tiếng rè"),
 ],
})

# ───────────────────────── 9. Phản hồi & báo cáo học tập ─────────────────────────
PHASES.append({
 "title": "Phản hồi & báo cáo học tập",
 "vocab": [
  ("feedback", "/ˈfiːdbæk/", "n", "nhận xét, góp ý (phản hồi)", "Here is some <b>feedback</b> on your writing.", "Đây là vài góp ý cho bài viết của em."),
  ("report card", "/rɪˈpɔːt ˌkɑːd/", "n", "phiếu báo kết quả học tập", "<b>Report cards</b> will be sent home on Friday.", "Thứ Sáu trường sẽ gửi phiếu báo kết quả về nhà."),
  ("comment", "/ˈkɒment/", "n", "lời nhận xét", "Please write two <b>comments</b> for each student.", "Mỗi học sinh viết hai lời nhận xét nhé."),
  ("progress", "/ˈprəʊɡres/", "n", "sự tiến bộ", "You've made great <b>progress</b> this term.", "Học kỳ này em tiến bộ rất nhiều."),
  ("target", "/ˈtɑːɡɪt/", "n", "mục tiêu (học tập)", "Your <b>target</b> for next term is to use more linking words.", "Mục tiêu học kỳ sau của em là dùng thêm từ nối."),
  ("achievement", "/əˈtʃiːvmənt/", "n", "thành tích, kết quả đạt được", "Winning the science fair is a big <b>achievement</b>.", "Thắng hội thi khoa học là một thành tích lớn."),
  ("effort", "/ˈefət/", "n", "sự nỗ lực", "She always puts a lot of <b>effort</b> into her work.", "Em ấy luôn rất nỗ lực trong học tập."),
  ("term", "/tɜːm/", "n", "học kỳ", "The first <b>term</b> ends in December.", "Học kỳ một kết thúc vào tháng Mười hai."),
  ("predicted grade", "/prɪˌdɪktɪd ˈɡreɪd/", "n", "điểm dự đoán (giáo viên dự báo)", "His <b>predicted grade</b> for maths is a B.", "Điểm dự đoán môn toán của em là B."),
  ("portfolio", "/pɔːtˈfəʊliəʊ/", "n", "hồ sơ bài làm (portfolio)", "Let's add this project to your <b>portfolio</b>.", "Mình đưa dự án này vào hồ sơ bài làm của em nhé."),
 ],
 "phrases": [
  ("Here is some feedback on your writing.", "Đây là vài góp ý cho bài viết của em."),
  ("You've made great progress this term.", "Học kỳ này em tiến bộ rất nhiều."),
  ("Your target for next term is to use more linking words.", "Mục tiêu học kỳ sau của em là dùng thêm từ nối."),
  ("Keep up the good work!", "Cứ tiếp tục phát huy nhé!"),
  ("Report cards will be sent home on Friday.", "Thứ Sáu trường sẽ gửi phiếu báo kết quả về nhà."),
  ("Please write two comments for each student.", "Mỗi học sinh viết hai lời nhận xét nhé."),
  ("She always puts a lot of effort into her work.", "Em ấy luôn rất nỗ lực trong học tập."),
  ("His predicted grade is a B.", "Điểm dự đoán của em ấy là B."),
  ("Let's add this project to your portfolio.", "Mình đưa dự án này vào hồ sơ bài làm của em nhé."),
  ("What went well, and what can you do better?", "Em làm tốt phần nào, và phần nào có thể làm tốt hơn?"),
 ],
 "dialogues": [
  ("What can I do to improve my writing?", [
    ("Plan before you write, and use linking words like 'because' and 'however'. Let's make that your target.", True, "Góp ý cụ thể + đặt mục tiêu."),
    ("Write more, better.", False, "Mơ hồ, sai cấu trúc ('The more you write, the better')."),
    ("Your writing is bad now.", False, "Chê mà không hướng dẫn cách cải thiện."),
  ]),
  ("The report comments are due on Friday. Are yours ready?", [
    ("Almost. I've finished 20 out of 25. I'll finish the rest tomorrow and ask you to check them.", True, "Con số + hạn + mời kiểm tra."),
    ("Yes ready, maybe Friday.", False, "Mâu thuẫn: nói 'ready' nhưng lại 'maybe Friday'."),
    ("Too many students, cannot finish.", False, "Thiếu chủ ngữ, than phiền, không có kế hoạch."),
  ]),
  ("Why is his predicted grade only a C?", [
    ("His class work is good, but he missed two assignments. If he hands them in, it can go up to a B.", True, "Lý do + cách cải thiện rõ ràng."),
    ("Because he is not smart.", False, "Phán xét năng lực học sinh — không chấp nhận được."),
    ("C is the system give.", False, "Sai ngữ pháp ('The system gave him a C') và đổ cho hệ thống."),
  ]),
  ("How should I write a comment for a weak student?", [
    ("Start with one strength, then give one clear target and one way parents can help.", True, "Cấu trúc nhận xét tích cực, có mục tiêu."),
    ("Write true: he is weak.", False, "Nhận xét tiêu cực, không giúp học sinh tiến bộ."),
    ("Copy the same comment all students.", False, "Thiếu giới từ ('for all students') và nhận xét rập khuôn."),
  ]),
  ("Did I do well on my project?", [
    ("Yes! Your research was excellent. Next time, try to speak more slowly in your presentation.", True, "Khen cụ thể + một góp ý nhẹ."),
    ("Yes good, good.", False, "Lặp từ, không có thông tin cụ thể."),
    ("Not bad, not good.", False, "Mơ hồ, học sinh không biết cần cải thiện gì."),
  ]),
 ],
 "listen": [
  ("You have made great progress this term", ["progress", "term"], "khen tiến bộ"),
  ("Report cards will be sent home on Friday", ["cards", "Friday"], "thông báo phiếu báo kết quả"),
  ("Your target is to use more linking words", ["target", "linking"], "đặt mục tiêu"),
  ("She always puts a lot of effort into her work", ["effort", "work"], "nhận xét sự nỗ lực"),
  ("Minh has worked very hard this term. His reading is much better. His target for next term is to write longer answers.", ["hard", "reading", "longer"], "nhận xét cuối kỳ"),
  ("Please finish your report comments by Friday. Write one strength and one target for each student. I will check them on Monday.", ["comments", "strength", "Monday"], "nhắc viết nhận xét"),
 ],
})

# ───────────────────────── Vai trong ngành ─────────────────────────
ROLES = {
 "teacher": {"label": "Giáo viên song ngữ", "emoji": "👩‍🏫",
  "scenarios": [
   ("te_parent", "Phụ huynh lo điểm thấp", "You are a foreign parent. Your child got a low mark in a science test and you are worried. I am the bilingual teacher. Ask why, what the school will do and how you can help at home."),
   ("te_hod", "Báo cáo với tổ trưởng", "You are my foreign head of department. Ask about my class's progress with the scheme of work, one student who needs support and my plan for the next test."),
   ("te_coteach", "Soạn bài với giáo viên bản ngữ", "You are a native English teacher who co-teaches my Grade 4 class. Plan next week's lesson with me. Suggest one activity, ask what I think and agree on who does what."),
   ("te_student", "Nói chuyện với học sinh không làm bài", "You are a 12-year-old student who didn't do your homework for the third time. I am your teacher. Give excuses at first, then tell me the real problem."),
  ],
  "dialogues": [
   ("Can you tell me more about my son's maths?", [
     ("Sure. He's good at calculations, but word problems are still hard for him. We practise them every Thursday.", True, "Điểm mạnh + khó khăn + cách hỗ trợ ở lớp."),
     ("Maths he is OK.", False, "Sai trật tự ('He's OK at maths') và quá chung chung."),
     ("He needs more tutor outside.", False, "Thiếu mạo từ ('a tutor') và đẩy sang học thêm thay vì nói về việc học ở lớp.")]),
   ("Your class is two weeks behind the other Grade 5 classes.", [
     ("I know. We spent extra time on fractions. I'll combine two units and catch up by the end of the month.", True, "Nhận thông tin + lý do + kế hoạch bù."),
     ("Other classes teach too fast.", False, "Đổ cho lớp khác, không có kế hoạch."),
     ("My class is weak, so slow.", False, "Thiếu động từ và đổ cho học sinh.")]),
   ("Why do we need to learn science in English?", [
     ("Because many books and websites about science are in English, and it will help you if you study abroad later.", True, "Giải thích lý do thiết thực, dễ hiểu."),
     ("Because school say.", False, "Sai chia động từ ('the school says so') và không thuyết phục."),
     ("Don't ask, just learn.", False, "Gạt câu hỏi, dập tắt sự tò mò của học sinh.")]),
   ("Can you explain this to the class in Vietnamese?", [
     ("Sure. I'll explain it quickly in Vietnamese, then ask them to say it again in English.", True, "Hỗ trợ bằng tiếng mẹ đẻ nhưng quay lại tiếng Anh ngay."),
     ("Yes, I explain all lesson in Vietnamese.", False, "Sai ngữ pháp ('the whole lesson') và lạm dụng tiếng Việt."),
     ("They understand already, no need.", False, "Khẳng định khi chưa kiểm tra học sinh hiểu chưa.")]),
   ("Can you give my daughter extra lessons after school?", [
     ("Thank you for asking, but I'm not able to tutor students from my own class. I can give her some extra practice to do at home.", True, "Từ chối lịch sự, giữ nguyên tắc nghề nghiệp + đưa cách hỗ trợ khác."),
     ("OK, 500 thousand one hour.", False, "Nhận dạy thêm học sinh lớp mình dễ gây xung đột lợi ích; báo giá cộc lốc."),
     ("No, I am very busy all the time.", False, "Từ chối mà không đưa cách hỗ trợ khác.")]),
   ("How did the new reading activity go?", [
     ("It went well. Most students finished on time, but the lower group needed more pictures. I'll add them next time.", True, "Đánh giá + điểm cần sửa + kế hoạch."),
     ("Good, very good, all happy.", False, "Chung chung, thiếu thông tin."),
     ("The activity is go well.", False, "Sai ngữ pháp ('It went well').")]),
  ]},
 "assistant": {"label": "Trợ giảng", "emoji": "📝",
  "scenarios": [
   ("as_support", "Hỗ trợ nhóm học sinh yếu", "You are a native English teacher. During the lesson, you ask me, the teaching assistant, to help a group of weaker students. Tell me what they should do, and later ask me how they did."),
   ("as_translate", "Dịch giữa giáo viên và phụ huynh", "You are a foreign teacher meeting a Vietnamese parent. I am the teaching assistant and I help with Vietnamese. Speak in short sentences, and ask me to check what the parent means."),
   ("as_behaviour", "Báo lại sự việc trong lớp", "You are the foreign class teacher. After class, ask me what happened with two students who were fighting during group work, and what I did."),
   ("as_prepare", "Chuẩn bị đồ dùng dạy học", "You are a foreign teacher. Tomorrow you need materials for a science lesson. Ask me to print, cut and prepare things, and check what time I will finish."),
  ],
  "dialogues": [
   ("Could you print 25 copies of this worksheet before class?", [
     ("Sure. I'll print them now and put them on your desk by 8:15.", True, "Đồng ý + thời gian cụ thể."),
     ("OK, I print.", False, "Thiếu 'will' và tân ngữ: 'I'll print them.'"),
     ("Printer maybe broken.", False, "Thiếu động từ và đoán mò, chưa kiểm tra.")]),
   ("How did your group do today?", [
     ("They did well. Three of them finished the task, but Linh still needs help with the past tense.", True, "Kết quả + học sinh cụ thể + điểm cần hỗ trợ."),
     ("They is good.", False, "Sai chia động từ ('They did well')."),
     ("I don't know, I just sit.", False, "Trợ giảng phải quan sát và báo lại được.")]),
   ("What did the parent say?", [
     ("She said her son has been sick this week, so he couldn't do his homework. She'll send a note tomorrow.", True, "Truyền đạt đủ ý + hệ quả + việc tiếp theo."),
     ("She say the boy sick.", False, "Sai thì và thiếu động từ ('She said her son was sick')."),
     ("Not important, she just talk.", False, "Tự lọc thông tin — phải dịch đủ ý cho giáo viên.")]),
   ("Why were those two boys fighting?", [
     ("They both wanted the same marker. I separated them, and they apologised to each other.", True, "Nguyên nhân + đã xử lý thế nào."),
     ("Boys fight, normal.", False, "Thiếu động từ và xem nhẹ sự việc."),
     ("I don't see, I was busy.", False, "Sai thì ('I didn't see it') — trợ giảng cần theo dõi lớp.")]),
   ("Can you take the class to the library at ten?", [
     ("Yes. I'll take them at ten and bring them back by 10:40.", True, "Xác nhận + giờ đi và giờ về."),
     ("Library far, maybe late.", False, "Thiếu động từ, lo trước mà không xác nhận."),
     ("Yes, I bring them go.", False, "Sai cấu trúc ('I'll take them there').")]),
   ("A student says she feels sick.", [
     ("I'll take her to the school nurse now and let you know what the nurse says.", True, "Hành động ngay + báo lại."),
     ("She wants to go home, I think lie.", False, "Nghi học sinh nói dối, sai ngữ pháp ('I think she's lying')."),
     ("Tell her sit down and wait.", False, "Sai cấu trúc ('Tell her to sit down') và bỏ qua sức khoẻ học sinh.")]),
  ]},
 "admissions": {"label": "Tư vấn tuyển sinh · Du học", "emoji": "🎓",
  "scenarios": [
   ("ad_tour", "Dẫn phụ huynh tham quan trường", "You are a Korean parent living in Hanoi. Your 7-year-old daughter may join our school. I am the admissions officer showing you around. Ask about class size, English support, lunch and the school bus."),
   ("ad_fee", "Hỏi học phí & ưu đãi", "You are a foreign parent with two children. Ask me about tuition fees, the sibling discount, the deposit and what happens if you leave in the middle of the year."),
   ("ad_abroad", "Tư vấn du học", "You are a Grade 11 student who wants to study business abroad. I am the study abroad counsellor. Ask about countries, costs, English test scores and scholarships."),
   ("ad_partner", "Gọi đối tác trường nước ngoài", "You are the international officer at a partner university abroad. I call to ask about a summer programme for our students. Ask how many students, which dates and what support they need."),
  ],
  "dialogues": [
   ("How many students are in each class?", [
     ("Around 20, with one teacher and one teaching assistant in every class.", True, "Con số + thông tin phụ huynh quan tâm."),
     ("Not many, don't worry.", False, "Né con số cụ thể."),
     ("Class have 20.", False, "Sai chia động từ và thiếu danh từ ('Each class has 20 students').")]),
   ("What if we move to another country in the middle of the year?", [
     ("You need to tell us one term before you leave. I'll email you our refund policy today.", True, "Nêu điều kiện + gửi chính sách bằng văn bản."),
     ("Money no return.", False, "Cộc lốc, sai ngữ pháp và có thể sai chính sách — cần đưa văn bản."),
     ("Don't think about that now.", False, "Né câu hỏi quan trọng của phụ huynh.")]),
   ("Which country is best for studying business?", [
     ("It depends on your budget and goals. Let's compare three options and look at the costs and scholarships.", True, "Không áp đặt + đưa cách so sánh cụ thể."),
     ("America best, everybody go.", False, "Áp đặt, thiếu động từ, sai chia động từ."),
     ("All country same.", False, "Sai số nhiều ('All countries are the same') và không có giá trị tư vấn.")]),
   ("Does my child need to take an entrance test?", [
     ("Yes, for Grade 2 and above. It's a short test in English and maths, and it takes about one hour.", True, "Đối tượng + nội dung + thời gian."),
     ("Test is easy, no need study.", False, "Không trả lời đúng câu hỏi, sai ngữ pháp."),
     ("Yes must.", False, "Cộc lốc, thiếu thông tin.")]),
   ("How many students will join the summer programme?", [
     ("About 15 students from Grades 10 and 11, with two teachers from our school.", True, "Số lượng + đối tượng + người đi kèm."),
     ("Many students want, maybe 15, maybe 30.", False, "Mơ hồ — đối tác cần con số để chuẩn bị."),
     ("I will tell you, I don't know.", False, "Lộn xộn, không hẹn thời gian báo lại.")]),
   ("Can you guarantee my son will get a scholarship?", [
     ("I can't guarantee that, but his grades are strong. We'll choose schools where he has a good chance.", True, "Trung thực (không hứa chắc) + phương án thực tế."),
     ("Yes, 100 percent sure.", False, "Hứa chắc là thiếu trung thực và rủi ro."),
     ("Scholarship is luck.", False, "Phủ nhận vai trò chuẩn bị hồ sơ, không giúp phụ huynh.")]),
  ]},
 "admin": {"label": "Giáo vụ · Liên lạc phụ huynh", "emoji": "🗂️",
  "scenarios": [
   ("ga_absent", "Phụ huynh báo con nghỉ ốm", "You are a foreign parent calling the school office. Your son is sick and will miss school for two days. Ask about homework, what document you need and the school bus."),
   ("ga_fee", "Nhắc đóng học phí", "You are a foreign parent. The school office calls you because the second-term fee is overdue. Be a bit embarrassed, ask for the bank details again and ask for one more week."),
   ("ga_timetable", "Giáo viên mới hỏi lịch dạy", "You are a new native English teacher. Ask me, the school office staff, about your timetable, the room changes this week, where to get the register and who to contact if you are sick."),
   ("ga_complaint", "Phụ huynh phàn nàn xe buýt", "You are an angry foreign parent. The school bus was 30 minutes late this morning and nobody told you. Complain, then ask what the school will do."),
  ],
  "dialogues": [
   ("My daughter is sick today. What should I do?", [
     ("I'm sorry to hear that. I'll mark her absent, and please send a doctor's note when she's back.", True, "Hỏi thăm + ghi nhận + giấy tờ cần có."),
     ("OK, sick no problem.", False, "Cộc lốc, không hướng dẫn giấy tờ."),
     ("She must come, today has test.", False, "Ép học sinh ốm đi học, sai ngữ pháp ('there's a test today').")]),
   ("I haven't received the invoice for this term.", [
     ("I'm sorry. Let me check your email address in our system, and I'll resend it within an hour.", True, "Xin lỗi + kiểm tra + hạn gửi lại."),
     ("We sent already, check spam.", False, "Đẩy trách nhiệm, sai thì ('We've already sent it')."),
     ("Invoice is not my job.", False, "Đùn đẩy — nhận việc hoặc chuyển đúng người.")]),
   ("Which room am I teaching in this afternoon?", [
     ("Room 305. Room 204 is closed today because the air-con is being fixed.", True, "Trả lời + lý do đổi phòng."),
     ("Same room, I think.", False, "Đoán mò — phải kiểm tra thời khoá biểu."),
     ("Room change, you not see email?", False, "Trách ngược, sai ngữ pháp ('Didn't you see the email?').")]),
   ("The bus was 30 minutes late, and nobody told me!", [
     ("I'm really sorry. There was an accident on the road. From now on, we'll message parents if the bus is more than ten minutes late.", True, "Xin lỗi + nguyên nhân + cam kết cải thiện."),
     ("Traffic in Hanoi always bad.", False, "Thiếu động từ ('is always bad') và bào chữa chung chung."),
     ("Not school fault, driver fault.", False, "Đổ lỗi, sai ngữ pháp ('It's not the school's fault').")]),
   ("Can you send me a letter to confirm my son studies here?", [
     ("Of course. I'll prepare the letter today, and you can collect it at the office tomorrow after 2 p.m.", True, "Đồng ý + thời gian + nơi nhận."),
     ("Letter take one week, maybe.", False, "Sai chia động từ ('takes') và mơ hồ."),
     ("Why you need letter?", False, "Sai cấu trúc câu hỏi ('Why do you need it?') và thiếu hỗ trợ.")]),
   ("The second-term fee is due tomorrow, right?", [
     ("That's right. You can pay by bank transfer, and please write your child's name and class in the message.", True, "Xác nhận + cách thanh toán + lưu ý khi chuyển khoản."),
     ("Yes, tomorrow, pay fast.", False, "Cộc lốc, nghe như ra lệnh."),
     ("Fee due is yesterday.", False, "Sai ngữ pháp và thông tin mâu thuẫn.")]),
  ]},
}

PACK = {
 "id": "education",
 "label": "Giáo dục · Đào tạo",
 "short": "Giáo dục",
 "emoji": "🎓",
 "desc": "Giáo viên song ngữ · trợ giảng · tuyển sinh · giáo vụ",
 "persona": "a Vietnamese teacher or education worker at a bilingual or international school",
 "counterpart": "a foreign parent, student or native English teacher",
 "context": "education and school",
 "core": [3, 11],
 "report": {
  "title": "Báo cáo buổi học 60 giây", "short": "Báo cáo lớp", "sub": "Nói như lúc báo lại với giáo viên chủ nhiệm 🎙️",
  "steps": [["Today's lesson", "Today Class 4A learned …"], ["Students", "Most students … / Minh needs help with …"], ["Next lesson", "Next time we will … / Please remind …"]],
  "kind": "end-of-lesson class report",
  "structure": "what the class did today / how the students did / plan and notes for the next lesson",
  "sample": "Today Class 4A learned the past simple and did a speaking game in pairs. Most students used the new verbs well, but Minh and Lan still mixed up 'go' and 'went'. Next lesson we will review irregular verbs, and please remind the class to bring their workbooks.",
 },
 "podcast": "Podcast lớp học",
 "game_tag": "Game anime: đánh quái lớp học, hạ boss phụ huynh khó tính",
 "reverse_tag": "kiểu lớp học",
 "jd_placeholder": "VD: Giáo viên tiếng Anh trường song ngữ ở TP.HCM, dạy cùng giáo viên bản ngữ, họp phụ huynh Hàn/Nhật, tư vấn tuyển sinh…",
 "rw_placeholder": "VD: phụ huynh lớp 4A lo con bị điểm thấp môn khoa học",
 "quips": [
  "Eyes on me, please!",
  "Hands up, don't shout out!",
  "Pair work time!",
  "Homework handed in!",
  "Great progress this term!",
  "Red pen ready!",
  "You're on mute!",
  "Warm-up first!",
  "Phones in your bag!",
  "A star for Table 2!",
 ],
 "ai": [
  ("parent_meet", "Họp phụ huynh", "You are a foreign parent at a parent-teacher meeting. I am your child's teacher. Ask how your child is doing, raise one concern about homework and ask how you can help at home. Speak simple English."),
  ("admission", "Tư vấn tuyển sinh", "You are a foreign parent who just moved to Vietnam. You visit the school admissions office. Ask about the curriculum, class size, tuition fees and the entrance test."),
  ("coteach", "Soạn bài với GV bản ngữ", "You are a native English teacher. We plan next week's lesson together. Suggest ideas, ask my opinion and agree on who teaches which part."),
  ("behaviour", "Nói chuyện với học sinh", "You are a 13-year-old student who often talks in class. I am your teacher and want to talk to you after class. Be a bit defensive at first, then agree on a plan."),
  ("feedback", "Góp ý bài làm", "You are a student who got a low mark on an essay. Ask me why, what you did well and what you should do next time."),
  ("online", "Lớp online trục trặc", "You are a student in an online class. Your audio is not working well and you missed the instructions. Tell me the problem and ask me to explain the task again."),
  ("observation", "Góp ý sau dự giờ", "You are a foreign academic director who observed my lesson. Give me one strength and one thing to improve, and ask what I will change next time."),
  ("sick_child", "Báo học sinh bị ốm", "You are a foreign parent. I am the teacher and I call you because your son has a fever at school. Ask how he is, what the school nurse did and when you should pick him up."),
 ],
 "rev": [
  ("Các em mở sách trang 20 nhé.", "Open your books at page 20, please."),
  ("Các em làm theo cặp nhé.", "Please work in pairs."),
  ("Ai biết đáp án thì giơ tay.", "Put your hand up if you know the answer."),
  ("Nộp bài trước thứ Sáu nhé.", "Please hand it in by Friday."),
  ("Học kỳ này cháu tiến bộ nhiều.", "Your child has made great progress this term."),
  ("Em cần luyện thêm kỹ năng viết.", "You need more writing practice."),
  ("Lớp 3 hiện đã hết chỗ.", "Grade 3 is full at the moment."),
  ("Chị có muốn tham quan trường không?", "Would you like a tour of the school?"),
  ("Mai tôi dạy thay lớp anh được.", "I can cover your class tomorrow."),
  ("Cháu bị dị ứng đậu phộng.", "She's allergic to peanuts."),
  ("Em đang tắt mic.", "You're on mute."),
  ("Mình cùng chữa đáp án nhé.", "Let's check the answers together."),
  ("Mục tiêu học kỳ sau là viết câu dài hơn.", "Next term's target is to write longer sentences."),
  ("Đây là lần nhắc nhở thứ nhất.", "This is your first warning."),
 ],
 "reading": [
  {"t": "Email from a parent", "text": "Dear Ms. Lan,\nMy son Ken says the maths homework is too difficult. He spends more than an hour on it every night and gets upset. Could we meet next week to talk about it? I'm free on Tuesday or Thursday after 4 p.m.\nBest regards,\nYuki Mori", "q": [
    {"q": "What is the parent worried about?", "o": ["The homework is too hard", "The class is too big", "The school bus is late"], "a": 0},
    {"q": "When is the parent free?", "o": ["Monday morning", "Tuesday or Thursday after 4 p.m.", "Every day at lunchtime"], "a": 1}]},
  {"t": "Lesson plan", "text": "LESSON PLAN – Grade 5 Science\nTopic: The water cycle\nObjective: Students can explain the four stages of the water cycle.\nWarm-up (5 min): picture quiz\nMain activity (25 min): group poster\nPlenary (10 min): each group presents one stage\nHomework: worksheet, page 12", "q": [
    {"q": "How long is the main activity?", "o": ["5 minutes", "10 minutes", "25 minutes"], "a": 2},
    {"q": "What do the students do at the end?", "o": ["Take a test", "Present one stage", "Watch a video"], "a": 1}]},
  {"t": "Admissions notice", "text": "ADMISSIONS 2027–2028\nApplications for Grades 1–9 are now open.\nEntrance test: every Saturday in March, 8:30–10:00.\nPlease bring: the application form, a copy of the birth certificate and the last school report.\nSibling discount: 10% for the second child.\nCampus tours: weekdays at 9:00 – please book by phone.", "q": [
    {"q": "When is the entrance test?", "o": ["Every Saturday in March", "Every weekday at 9:00", "Only on 1 March"], "a": 0},
    {"q": "Who gets a 10% discount?", "o": ["All new students", "The second child in a family", "Students who pass the test"], "a": 1}]},
  {"t": "Online class message", "text": "Class 7B chat – 18:40\nMr. Phong: Tomorrow's lesson is online because of the storm. Please log in at 7:55 using the same link. Keep your camera on and your microphone on mute. We will use breakout rooms for group work. The recording will be on the platform by 17:00.", "q": [
    {"q": "Why is the lesson online?", "o": ["The teacher is sick", "There is a storm", "It is a holiday"], "a": 1},
    {"q": "When will the recording be ready?", "o": ["Next week", "By 7:55", "By 17:00"], "a": 2}]},
  {"t": "Report card comment", "text": "TERM 1 REPORT – English\nStudent: An Nguyen, Grade 6\nEffort: Excellent   Achievement: Good\nComment: An is a hard-working student who always takes part in class. Her speaking has improved a lot. Her target for Term 2 is to check her spelling and use more linking words in her writing.", "q": [
    {"q": "What has improved a lot?", "o": ["Her speaking", "Her spelling", "Her maths"], "a": 0},
    {"q": "What is one target for Term 2?", "o": ["Speak more in class", "Read more books", "Check her spelling"], "a": 2}]},
 ],
 "events": [
  ("parent_meeting", "Buổi họp phụ huynh", "You are a foreign parent coming to the parent-teacher meeting next week. Ask about your child's progress, behaviour, homework and how to help at home."),
  ("observation", "Buổi dự giờ", "You are the academic director who will observe my lesson tomorrow. Ask about my learning objective, activities, how I support different levels and how I check learning."),
  ("admission_tour", "Đón phụ huynh tham quan trường", "You are a foreign parent visiting our school next week before you choose a school for your child. Ask about the curriculum, teachers, class size, fees and the entrance test."),
  ("new_teacher", "Đón giáo viên nước ngoài mới", "You are a new native English teacher starting at our school next week. Ask me about the timetable, the classes, the school rules and life in Vietnam."),
  ("demo_lesson", "Dạy thử khi xin việc", "You are the head of English at an international school. I will teach a demo lesson and have an interview tomorrow. Ask about my teaching style, classroom management and how I use English in class."),
  ("report_day", "Trả phiếu kết quả cuối kỳ", "You are a parent receiving your child's end-of-term report next week. Ask about the grades, the teacher's comments and the targets for next term."),
  ("other", "Khác", ""),
 ],
 "roles": ROLES,
 "phases": PHASES,
}
