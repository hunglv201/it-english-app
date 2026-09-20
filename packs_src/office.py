# -*- coding: utf-8 -*-
# Gói "office" — Công sở chung (gói MẶC ĐỊNH cho người không chọn ngành).
# Tiếng Anh văn phòng dùng được cho mọi người đi làm, sinh viên, người tìm việc — KHÔNG mang chất IT.
# Chặng 3 (Email), 10 (Nghỉ phép & hành chính), 11 (Phỏng vấn) được các gói ngành khác dùng lại qua "core"
# -> giữ trung lập, không gắn với ngành nào.
# Schema: xem packs_src/README.md. Build: python3 packs_src/build.py office

PHASES = []

# ───────────────────────── 0. Chào hỏi & làm quen ─────────────────────────
PHASES.append({
 "title": "Chào hỏi & làm quen",
 "vocab": [
  ("colleague", "/ˈkɒliːɡ/", "n", "đồng nghiệp", "This is my <b>colleague</b>, Minh.", "Đây là Minh, đồng nghiệp của mình.", "同僚", "dōryō"),
  ("introduce", "/ˌɪntrəˈdjuːs/", "v", "giới thiệu", "Let me <b>introduce</b> myself. I'm Lan.", "Cho mình tự giới thiệu. Mình là Lan.", "紹介する", "shōkai suru"),
  ("department", "/dɪˈpɑːtmənt/", "n", "phòng, ban", "I work in the sales <b>department</b>.", "Mình làm ở phòng kinh doanh.", "部署", "busho"),
  ("position", "/pəˈzɪʃn/", "n", "vị trí, chức vụ", "What's your <b>position</b> here?", "Bạn làm vị trí gì ở đây?", "ポジション", "pojishon"),
  ("manager", "/ˈmænɪdʒə/", "n", "quản lý, sếp", "My <b>manager</b> is Ms. Sarah Lee.", "Quản lý của mình là chị Sarah Lee.", "上司", "jōshi"),
  ("welcome", "/ˈwelkəm/", "excl/v", "chào mừng, đón tiếp", "<b>Welcome</b> to the team, Hoa!", "Chào mừng Hoa đến với nhóm!"),
  ("newcomer", "/ˈnjuːkʌmə/", "n", "người mới", "Ken is a <b>newcomer</b>, so please help him.", "Ken là người mới, mọi người giúp bạn ấy nhé.", "新人", "shinjin"),
  ("small talk", "/ˈsmɔːl tɔːk/", "n", "chuyện phiếm xã giao", "We made <b>small talk</b> about the weather.", "Tụi mình nói chuyện phiếm về thời tiết.", "雑談", "zatsudan"),
  ("business card", "/ˈbɪznəs kɑːd/", "n", "danh thiếp", "Here's my <b>business card</b>.", "Đây là danh thiếp của tôi.", "名刺", "meishi"),
  ("greet", "/ɡriːt/", "v", "chào hỏi", "She always <b>greets</b> everyone with a smile.", "Chị ấy luôn chào mọi người với nụ cười.", "挨拶する", "aisatsu suru"),
 ],
 "phrases": [
  ("Hi, I'm Lan. I'm new in the marketing team.", "Chào anh/chị, em là Lan, em mới vào nhóm marketing."),
  ("Nice to meet you. — Nice to meet you too.", "Rất vui được gặp bạn. — Mình cũng rất vui được gặp bạn."),
  ("What do you do here?", "Bạn làm công việc gì ở đây?"),
  ("I work in the accounting department.", "Mình làm ở phòng kế toán."),
  ("How long have you worked here?", "Bạn làm ở đây bao lâu rồi?"),
  ("Let me introduce you to Minh, our team leader.", "Để mình giới thiệu bạn với Minh, trưởng nhóm của tụi mình."),
  ("Welcome to the team!", "Chào mừng bạn đến với nhóm!"),
  ("How's it going? — Not bad, thanks. And you?", "Dạo này sao rồi? — Cũng ổn, cảm ơn. Còn bạn?"),
  ("Please call me Ken.", "Cứ gọi mình là Ken nhé."),
  ("Have a nice weekend! — You too!", "Cuối tuần vui vẻ nhé! — Bạn cũng vậy!"),
 ],
 "dialogues": [
  ("Hi, you must be the new person. I'm David.", [
    ("Yes, hi David. I'm Hoa. Nice to meet you.", True, "Xác nhận + nói tên + câu chào chuẩn."),
    ("Yes, I am new person. My name Hoa.", False, "Thiếu 'the' và 'is': 'I'm the new person. My name is Hoa.'"),
    ("Hello. Nice to meet you too.", False, "Chỉ nói 'too' khi người kia đã nói 'Nice to meet you' trước; lại chưa nói tên mình."),
  ]),
  ("What do you do here?", [
    ("I'm an accountant. I work in the finance department.", True, "Nêu công việc + phòng ban — gọn và rõ."),
    ("I do work accountant.", False, "Dịch từng chữ: nên nói 'I'm an accountant.'"),
    ("I'm fine, thank you.", False, "Nhầm với 'How are you?' — người ta hỏi bạn làm việc gì."),
  ]),
  ("How long have you been with the company?", [
    ("About two years. I joined in 2024.", True, "Nêu khoảng thời gian + năm vào công ty."),
    ("I work here since two years.", False, "Sai thì và giới từ: 'I've worked here for two years.'"),
    ("Two years ago.", False, "'ago' chỉ thời điểm trong quá khứ, không trả lời 'bao lâu'."),
  ]),
  ("How's it going?", [
    ("Pretty good, thanks. Busy week, though. How about you?", True, "Trả lời ngắn + hỏi lại — kiểu small talk tự nhiên."),
    ("It's going to the office.", False, "Hiểu theo nghĩa đen — đây chỉ là câu chào 'dạo này thế nào'."),
    ("I'm go well.", False, "Sai ngữ pháp: 'I'm doing well' hoặc 'Pretty good'."),
  ]),
  ("Welcome to the team! Let me know if you need anything.", [
    ("Thank you, that's very kind. I'll probably have lots of questions!", True, "Cảm ơn + đáp lại thân thiện."),
    ("Thank you for welcome me.", False, "Sau 'for' dùng V-ing: 'Thank you for welcoming me.'"),
    ("Yes, I need many things.", False, "Hiểu câu xã giao theo nghĩa đen, nghe kỳ và đòi hỏi."),
  ]),
 ],
 "listen": [
  ("Nice to meet you, I'm the new assistant", ["meet", "assistant"], "chào khi mới gặp"),
  ("I work in the sales department on the third floor", ["department", "third"], "phòng ban ở tầng mấy"),
  ("Let me introduce you to our team leader", ["introduce", "leader"], "giới thiệu trưởng nhóm"),
  ("How long have you worked here", ["long", "worked"], "hỏi thâm niên"),
  ("Good morning, everyone. This is Hoa, our new accountant. She joined us from a bank last month.", ["morning", "accountant", "bank"], "giới thiệu người mới đầu buổi họp"),
  ("Hi, I'm Ken from the Tokyo office. I'm here for two weeks. Please call me if you need anything.", ["Tokyo", "weeks", "call"], "đồng nghiệp văn phòng khác tự giới thiệu"),
 ],
})

# ───────────────────────── 1. Công việc hằng ngày & báo cáo ─────────────────────────
PHASES.append({
 "title": "Công việc hằng ngày & báo cáo",
 "vocab": [
  ("report", "/rɪˈpɔːt/", "n/v", "báo cáo", "I send a weekly <b>report</b> every Friday.", "Mình gửi báo cáo tuần vào mỗi thứ Sáu.", "報告", "hōkoku"),
  ("schedule", "/ˈʃedjuːl/", "n", "lịch, lịch trình", "My <b>schedule</b> is full today.", "Hôm nay lịch của mình kín rồi.", "予定", "yotei"),
  ("progress", "/ˈprəʊɡres/", "n", "tiến độ", "Here's my <b>progress</b> for this week.", "Đây là tiến độ công việc tuần này của mình.", "進捗", "shinchoku"),
  ("complete", "/kəmˈpliːt/", "v", "hoàn thành", "I <b>completed</b> the customer list yesterday.", "Hôm qua mình đã hoàn thành danh sách khách hàng.", "完了する", "kanryō suru"),
  ("task", "/tɑːsk/", "n", "nhiệm vụ, đầu việc", "I have three <b>tasks</b> to finish today.", "Hôm nay mình có ba việc phải làm xong."),
  ("routine", "/ruːˈtiːn/", "n", "việc thường nhật", "Checking emails is part of my morning <b>routine</b>.", "Kiểm tra email là việc quen thuộc mỗi sáng của mình."),
  ("to-do list", "/təˈduː lɪst/", "n", "danh sách việc cần làm", "Calling the bank is on my <b>to-do list</b>.", "Gọi ngân hàng nằm trong danh sách việc cần làm của mình."),
  ("in charge of", "/ɪn ˈtʃɑːdʒ əv/", "phr", "phụ trách", "Hoa is <b>in charge of</b> the new office.", "Hoa phụ trách văn phòng mới.", "担当", "tantō"),
  ("workload", "/ˈwɜːkləʊd/", "n", "khối lượng công việc", "My <b>workload</b> is heavy this week.", "Tuần này khối lượng việc của mình nhiều."),
  ("on track", "/ɒn ˈtræk/", "phr", "đúng tiến độ", "We're <b>on track</b> to finish by Friday.", "Tụi mình đang đúng tiến độ, kịp xong vào thứ Sáu."),
 ],
 "phrases": [
  ("Here's a quick update on my work.", "Đây là cập nhật nhanh về công việc của mình."),
  ("Yesterday I finished the monthly report.", "Hôm qua mình đã làm xong báo cáo tháng."),
  ("Today I'm going to call three customers.", "Hôm nay mình sẽ gọi cho ba khách hàng."),
  ("I'm still working on the price list.", "Mình vẫn đang làm bảng giá."),
  ("I'm about halfway done.", "Mình xong khoảng một nửa rồi."),
  ("We're on track to finish by Friday.", "Tụi mình đang đúng tiến độ, kịp xong vào thứ Sáu."),
  ("No issues from my side.", "Phía mình không có vấn đề gì."),
  ("I need some help with the budget numbers.", "Mình cần giúp một chút phần số liệu ngân sách."),
  ("My workload is a bit heavy this week.", "Tuần này khối lượng việc của mình hơi nhiều."),
  ("I'm in charge of the new customer list.", "Mình phụ trách danh sách khách hàng mới."),
 ],
 "dialogues": [
  ("Can you give me a quick update?", [
    ("Sure. I finished the sales report yesterday, and today I'm working on the slides.", True, "Việc đã xong (quá khứ) + việc hôm nay (tiếp diễn)."),
    ("Yesterday I finish report, today I do slides.", False, "Sai thì: 'I finished' cho hôm qua, 'I'm doing' cho hôm nay."),
    ("Everything is fine.", False, "Quá chung chung, sếp không biết bạn đã làm gì."),
  ]),
  ("How's the customer survey going?", [
    ("It's going well. I've collected 60 answers so far.", True, "Nhận định + con số cụ thể."),
    ("It going well.", False, "Thiếu 'is': 'It's going well.'"),
    ("The survey is going to customers.", False, "Hiểu sai câu hỏi — người ta hỏi tiến độ."),
  ]),
  ("Are we on track for Friday?", [
    ("Yes, we're on track. Only the last section is left.", True, "Trả lời có/không + phần còn lại."),
    ("Yes, we are on the track.", False, "Cụm cố định là 'on track', không có 'the'."),
    ("Friday OK maybe.", False, "Thiếu động từ, nghe không chắc chắn."),
  ]),
  ("Any issues?", [
    ("Just one. I'm waiting for the new prices from the sales team.", True, "Nêu vấn đề cụ thể + đang chờ ai."),
    ("Issue is have one.", False, "Dịch từng chữ 'vấn đề thì có một' — nên nói 'There's one issue.'"),
    ("No issue, but I cannot finish.", False, "Mâu thuẫn: không làm xong được chính là vấn đề cần báo."),
  ]),
  ("Who's in charge of the event budget?", [
    ("I am. Let me know if you have any questions about it.", True, "Nhận rõ mình phụ trách + mời hỏi."),
    ("Me charge.", False, "Thiếu động từ: 'I'm in charge of it.'"),
    ("The budget is 50 million.", False, "Trả lời sai câu hỏi — người ta hỏi ai phụ trách."),
  ]),
 ],
 "listen": [
  ("I finished the monthly report yesterday", ["finished", "monthly"], "việc đã xong"),
  ("Today I'm going to call three new customers", ["call", "customers"], "việc hôm nay"),
  ("My workload is quite heavy this week", ["workload", "heavy"], "khối lượng việc"),
  ("We are on track to finish by Friday", ["track", "Friday"], "tiến độ"),
  ("Yesterday I sent the invoices to our clients. Today I'm going to update the price list. No issues from my side.", ["invoices", "price", "issues"], "báo cáo nhanh buổi sáng"),
  ("I'm still working on the training plan. It's about seventy percent done. I need Hoa's help with the budget.", ["training", "seventy", "budget"], "báo tiến độ và nhờ giúp"),
 ],
})

# ───────────────────────── 2. Họp & trao đổi ─────────────────────────
PHASES.append({
 "title": "Họp & trao đổi",
 "vocab": [
  ("meeting", "/ˈmiːtɪŋ/", "n", "cuộc họp", "The <b>meeting</b> starts at 9:30.", "Cuộc họp bắt đầu lúc 9 giờ 30.", "会議", "kaigi"),
  ("agenda", "/əˈdʒendə/", "n", "chương trình họp", "Let's look at today's <b>agenda</b>.", "Mình cùng xem chương trình họp hôm nay nhé.", "議題", "gidai"),
  ("minutes", "/ˈmɪnɪts/", "n", "biên bản họp", "Who's taking the <b>minutes</b> today?", "Hôm nay ai ghi biên bản?", "議事録", "gijiroku"),
  ("opinion", "/əˈpɪnjən/", "n", "ý kiến", "In my <b>opinion</b>, the price is too high.", "Theo ý kiến của mình, giá này cao quá.", "意見", "iken"),
  ("agree", "/əˈɡriː/", "v", "đồng ý", "I <b>agree</b> with Minh on this.", "Về việc này mình đồng ý với Minh."),
  ("suggest", "/səˈdʒest/", "v", "đề xuất, gợi ý", "I <b>suggest</b> we meet again on Monday.", "Mình đề xuất tụi mình họp lại vào thứ Hai.", "提案する", "teian suru"),
  ("action item", "/ˈækʃn ˌaɪtəm/", "n", "việc cần làm sau họp", "We have four <b>action items</b> from today's meeting.", "Buổi họp hôm nay có bốn việc cần làm tiếp."),
  ("point", "/pɔɪnt/", "n", "ý, luận điểm", "That's a good <b>point</b>, David.", "Ý đó hay đấy, David."),
  ("decision", "/dɪˈsɪʒn/", "n", "quyết định", "We need to make a <b>decision</b> today.", "Hôm nay tụi mình cần ra quyết định.", "決定", "kettei"),
  ("discuss", "/dɪˈskʌs/", "v", "thảo luận (không dùng 'about')", "Let's <b>discuss</b> the budget next.", "Tiếp theo mình thảo luận về ngân sách nhé."),
 ],
 "phrases": [
  ("Let's get started.", "Mình bắt đầu nhé."),
  ("The first item on the agenda is the budget.", "Mục đầu tiên trong chương trình họp là ngân sách."),
  ("What do you think, Minh?", "Minh thấy sao?"),
  ("I agree with you.", "Mình đồng ý với bạn."),
  ("I see your point, but I'm not sure it will work.", "Mình hiểu ý bạn, nhưng mình không chắc cách đó ổn."),
  ("Could I add something?", "Mình bổ sung một chút được không?"),
  ("Let's move on to the next point.", "Mình chuyển sang ý tiếp theo nhé."),
  ("So, to sum up, we'll start the campaign in May.", "Tóm lại, tụi mình sẽ bắt đầu chiến dịch vào tháng Năm."),
  ("Who's taking the minutes today?", "Hôm nay ai ghi biên bản?"),
  ("I'll send the action items after the meeting.", "Mình sẽ gửi các việc cần làm sau buổi họp."),
 ],
 "dialogues": [
  ("What do you think about the new schedule, Lan?", [
    ("I think it's a good idea, but Friday is a bit tight for me.", True, "Nêu ý kiến + điểm lo ngại, lịch sự."),
    ("I think is good.", False, "Thiếu chủ ngữ 'it': 'I think it's good.'"),
    ("I don't know, up to you.", False, "Né tránh — trong họp nên nêu ý kiến của mình."),
  ]),
  ("I think we should cancel the event.", [
    ("I see your point, but maybe we can make it smaller instead.", True, "Phản đối khéo: công nhận trước, đề xuất sau."),
    ("I am not agree.", False, "'agree' là động từ: 'I don't agree' hoặc 'I disagree'."),
    ("No, you are wrong.", False, "Quá thẳng, dễ gây mất lòng trong cuộc họp."),
  ]),
  ("Sorry, can I finish my point?", [
    ("Of course, sorry. Please go ahead.", True, "Xin lỗi + nhường lời, lịch sự."),
    ("Sorry, I interrupt you.", False, "Nên nói: 'Sorry for interrupting.'"),
    ("OK, but quick.", False, "Nghe thiếu tôn trọng người đang nói."),
  ]),
  ("Does anyone have any other questions?", [
    ("Just one. When do we need to send the final numbers?", True, "Có thắc mắc thì hỏi ngắn, cụ thể."),
    ("I have question one.", False, "Sai trật tự từ: 'I have one question.'"),
    ("No question.", False, "Cộc và thiếu 's': 'No questions from me, thanks.'"),
  ]),
  ("So, who will contact the hotel?", [
    ("I can do that. I'll call them this afternoon.", True, "Nhận việc + thời gian cụ thể."),
    ("I contact hotel.", False, "Thiếu 'will' và 'the': 'I'll contact the hotel.'"),
    ("The hotel is near the airport.", False, "Không trả lời câu hỏi 'ai sẽ làm'."),
  ]),
 ],
 "listen": [
  ("The first item on the agenda is the budget", ["agenda", "budget"], "mục đầu tiên của cuộc họp"),
  ("Could you take the minutes today", ["minutes", "today"], "phân công ghi biên bản"),
  ("I agree with Sarah about the new schedule", ["agree", "schedule"], "đồng ý với ai"),
  ("Let's move on to the next point", ["move", "point"], "chuyển ý"),
  ("Thanks for coming, everyone. We have three items today. First, let's look at last month's sales.", ["three", "items", "sales"], "mở đầu cuộc họp"),
  ("So, to sum up, we'll hold the party on May 20. Minh will book the restaurant. I'll send the minutes tonight.", ["party", "restaurant", "tonight"], "chốt cuộc họp"),
 ],
})

# ───────────────────────── 3. Email công việc (dùng chung cho mọi ngành) ─────────────────────────
PHASES.append({
 "title": "Email công việc",
 "vocab": [
  ("attach", "/əˈtætʃ/", "v", "đính kèm", "I've <b>attached</b> the contract.", "Tôi đã đính kèm hợp đồng.", "添付する", "tenpu suru"),
  ("subject line", "/ˈsʌbdʒɪkt laɪn/", "n", "tiêu đề email", "Write a clear <b>subject line</b>.", "Hãy viết tiêu đề email thật rõ ràng.", "件名", "kenmei"),
  ("reply", "/rɪˈplaɪ/", "v/n", "trả lời, phản hồi", "Sorry for the late <b>reply</b>.", "Xin lỗi vì trả lời muộn.", "返信", "henshin"),
  ("forward", "/ˈfɔːwəd/", "v", "chuyển tiếp", "Could you <b>forward</b> me that email?", "Bạn chuyển tiếp email đó cho mình được không?", "転送する", "tensō suru"),
  ("cc", "/ˌsiː ˈsiː/", "v", "gửi đồng thời (cc)", "Please <b>cc</b> my manager on the email.", "Vui lòng cc quản lý của tôi trong email."),
  ("regards", "/rɪˈɡɑːdz/", "n", "lời chào cuối thư", "Best <b>regards</b>, Tuấn", "Trân trọng, Tuấn"),
  ("inbox", "/ˈɪnbɒks/", "n", "hộp thư đến", "I have fifty emails in my <b>inbox</b>.", "Hộp thư đến của mình có năm mươi email."),
  ("follow up", "/ˌfɒləʊ ˈʌp/", "v", "nhắc lại, hỏi tiếp", "I'm writing to <b>follow up</b> on my last email.", "Tôi viết email này để nhắc lại email lần trước."),
  ("confirm", "/kənˈfɜːm/", "v", "xác nhận", "Could you <b>confirm</b> the date, please?", "Anh/chị xác nhận giúp tôi ngày được không?", "確認する", "kakunin suru"),
  ("draft", "/drɑːft/", "n", "bản nháp", "Here's a <b>draft</b> of the letter.", "Đây là bản nháp của lá thư.", "下書き", "shitagaki"),
 ],
 "phrases": [
  ("Dear Ms. Lee, / Hi Tom,", "Kính gửi chị Lee, / Chào Tom, (thân mật hơn)"),
  ("I hope you're well.", "Hy vọng anh/chị vẫn khỏe."),
  ("I'm writing to ask about the meeting on Monday.", "Tôi viết email này để hỏi về cuộc họp thứ Hai."),
  ("Please find the contract attached.", "Vui lòng xem hợp đồng đính kèm."),
  ("Could you please confirm by Thursday?", "Anh/chị vui lòng xác nhận trước thứ Năm được không?"),
  ("I'm just following up on my email from last week.", "Tôi xin nhắc lại email tuần trước."),
  ("Sorry for the late reply.", "Xin lỗi vì phản hồi muộn."),
  ("Please let me know if you have any questions.", "Nếu có câu hỏi gì, anh/chị cứ cho tôi biết nhé."),
  ("I look forward to hearing from you.", "Mong sớm nhận được phản hồi của anh/chị."),
  ("Best regards, Hoa", "Trân trọng, Hoa"),
 ],
 "dialogues": [
  ("Did you get my email about the contract?", [
    ("Yes, I did. I'll reply by the end of the day.", True, "Xác nhận + hẹn thời gian trả lời."),
    ("Yes, I get it yesterday.", False, "Sai thì: 'I got it yesterday.'"),
    ("What email?", False, "Cộc lốc; nên nói 'Sorry, I haven't seen it. Could you send it again?'"),
  ]),
  ("How should I start an email to a new client?", [
    ("Start with 'Dear Mr. Brown' and say why you're writing in the first line.", True, "Lời khuyên cụ thể, đúng chuẩn email trang trọng."),
    ("Start with 'Dear Brown Mr.'.", False, "Sai trật tự: danh xưng đứng trước họ — 'Dear Mr. Brown'."),
    ("Just write 'Hey bro'.", False, "Quá suồng sã với khách hàng mới."),
  ]),
  ("The file isn't attached to your email.", [
    ("Sorry about that! I'll send it again right now.", True, "Xin lỗi ngắn + gửi lại ngay."),
    ("Sorry, I forget attach.", False, "Sai: 'Sorry, I forgot to attach it.'"),
    ("I attached already, you check again.", False, "Sai ngữ pháp và đổ lỗi cho người nhận."),
  ]),
  ("Should I cc the manager on this email?", [
    ("Yes, please cc her. She needs to know about the change.", True, "Trả lời + lý do."),
    ("Yes, cc manager is must.", False, "Sai cấu trúc: 'You should cc the manager.'"),
    ("CC means carbon copy.", False, "Giải thích nghĩa, không trả lời câu hỏi."),
  ]),
  ("The client hasn't replied for a week.", [
    ("Let's send a short follow-up email and ask for a reply by Friday.", True, "Đề xuất hành động cụ thể + hạn trả lời."),
    ("We send email again?", False, "Thiếu trợ động từ: 'Should we send another email?'"),
    ("Client no reply, not our problem.", False, "Thiếu động từ và thái độ thiếu trách nhiệm."),
  ]),
 ],
 "listen": [
  ("Please find the contract attached to this email", ["contract", "attached"], "tệp đính kèm"),
  ("Could you confirm the date by Thursday", ["confirm", "Thursday"], "xin xác nhận"),
  ("Sorry for the late reply", ["late", "reply"], "xin lỗi trả lời muộn"),
  ("I'm writing to follow up on our meeting", ["writing", "follow"], "mục đích email"),
  ("Dear Mr. Brown, thank you for your email. I have attached the new price list. Please let me know if you have any questions.", ["attached", "price", "questions"], "email gửi bảng giá"),
  ("Hi team, the training has been moved to Wednesday afternoon. Please reply to this email to confirm. Thanks, Lan.", ["training", "Wednesday", "confirm"], "email báo đổi lịch"),
 ],
})

# ───────────────────────── 4. Chat & tin nhắn công việc ─────────────────────────
PHASES.append({
 "title": "Chat & tin nhắn công việc",
 "vocab": [
  ("message", "/ˈmesɪdʒ/", "n", "tin nhắn", "I sent you a <b>message</b> this morning.", "Sáng nay mình có nhắn tin cho bạn."),
  ("group chat", "/ˈɡruːp tʃæt/", "n", "nhóm chat", "I'll post it in the team <b>group chat</b>.", "Mình sẽ đăng lên nhóm chat của team."),
  ("tag", "/tæɡ/", "v", "gắn tên, tag (ai đó)", "Please <b>tag</b> me if you need anything.", "Cần gì cứ tag mình nhé."),
  ("quick question", "/ˌkwɪk ˈkwestʃən/", "n", "câu hỏi nhanh", "<b>Quick question</b>: where's the price list?", "Hỏi nhanh: bảng giá để ở đâu vậy?"),
  ("ASAP", "/ˌeɪ es eɪ ˈpiː/", "adv", "càng sớm càng tốt", "Please call the client back <b>ASAP</b>.", "Làm ơn gọi lại cho khách càng sớm càng tốt.", "至急", "shikyū"),
  ("heads-up", "/ˈhedz ʌp/", "n", "lời báo trước", "Thanks for the <b>heads-up</b>!", "Cảm ơn đã báo trước nhé!"),
  ("available", "/əˈveɪləbl/", "adj", "rảnh, có thể liên lạc", "Are you <b>available</b> for a call at two?", "Bạn rảnh gọi lúc hai giờ không?"),
  ("offline", "/ˌɒfˈlaɪn/", "adj", "không trực tuyến", "I'll be <b>offline</b> after 6 p.m.", "Sau 6 giờ tối mình sẽ không online."),
  ("thumbs-up", "/ˌθʌmz ˈʌp/", "n", "biểu tượng đồng ý (like)", "Just give it a <b>thumbs-up</b> if you agree.", "Nếu đồng ý thì thả like là được."),
  ("typo", "/ˈtaɪpəʊ/", "n", "lỗi đánh máy", "Sorry, <b>typo</b>! I meant Friday, not Monday.", "Xin lỗi, gõ nhầm! Ý mình là thứ Sáu, không phải thứ Hai."),
 ],
 "phrases": [
  ("Quick question: is the meeting still at 3?", "Hỏi nhanh: cuộc họp vẫn lúc 3 giờ hả?"),
  ("Just a heads-up: the client is coming at 10.", "Báo trước nhé: khách đến lúc 10 giờ."),
  ("Got it, thanks!", "Rõ rồi, cảm ơn nhé!"),
  ("On my way!", "Mình đang tới!"),
  ("Are you free for a quick call?", "Bạn rảnh gọi nhanh một chút không?"),
  ("Sorry, I missed your message.", "Xin lỗi, mình bỏ lỡ tin nhắn của bạn."),
  ("Let me check and get back to you.", "Để mình kiểm tra rồi báo lại bạn."),
  ("I'll be offline after 6 p.m.", "Sau 6 giờ tối mình sẽ không online."),
  ("Can you send me the link?", "Bạn gửi mình đường link được không?"),
  ("No rush.", "Không gấp đâu."),
 ],
 "dialogues": [
  ("Quick question: where's the sales file?", [
    ("It's in the team folder, under 'October'.", True, "Trả lời ngắn, chỉ đúng chỗ — hợp với chat."),
    ("Sales file is in there.", False, "Thiếu 'The', và 'in there' mơ hồ — người hỏi vẫn không biết ở đâu."),
    ("Why you ask?", False, "Thiếu trợ động từ và nghe khó chịu: 'Why do you ask?'"),
  ]),
  ("Can you join a quick call now?", [
    ("Sure, give me two minutes.", True, "Đồng ý + thời gian cụ thể."),
    ("I can joining.", False, "Sau 'can' dùng động từ nguyên mẫu: 'I can join.'"),
    ("Call what?", False, "Cộc lốc; nên hỏi 'Sure, what's it about?'"),
  ]),
  ("Please send the numbers ASAP.", [
    ("Will do. You'll have them in 30 minutes.", True, "Cam kết + thời gian cụ thể."),
    ("I sending now.", False, "Thiếu 'am': 'I'm sending them now.'"),
    ("OK ASAP.", False, "Chỉ lặp lại, không nói khi nào gửi."),
  ]),
  ("Sorry, I didn't see your message earlier.", [
    ("No worries! I still need the address when you have a minute.", True, "Thông cảm + nhắc lại việc còn cần."),
    ("Why you not see?", False, "Sai ngữ pháp và mang giọng trách móc."),
    ("It's OK, forget it.", False, "Bỏ qua luôn việc mình đang cần — việc bị bỏ dở."),
  ]),
  ("Just a heads-up: I'll be 15 minutes late.", [
    ("Thanks for letting me know. See you soon.", True, "Cảm ơn vì đã báo + thân thiện."),
    ("OK, I am waiting you.", False, "Thiếu 'for': 'I'll wait for you.'"),
    ("Why late?", False, "Cộc lốc, nghe như trách."),
  ]),
 ],
 "listen": [
  ("Quick question about the meeting room", ["question", "room"], "câu hỏi nhanh"),
  ("I'll be offline after six tonight", ["offline", "six"], "báo không online"),
  ("Can you send me the link to the file", ["link", "file"], "xin đường link"),
  ("Sorry, I missed your message this morning", ["missed", "message"], "xin lỗi vì bỏ lỡ tin"),
  ("Hi Minh, just a heads-up. The client is coming at ten, not eleven. Can you get the room ready?", ["heads-up", "ten", "ready"], "tin nhắn báo trước"),
  ("Thanks for the file! I checked it and it looks good. I'll send it to Sarah now.", ["checked", "good", "Sarah"], "trả lời tin nhắn"),
 ],
})

# ───────────────────────── 5. Điện thoại & gọi video ─────────────────────────
PHASES.append({
 "title": "Điện thoại & gọi video",
 "vocab": [
  ("call back", "/ˌkɔːl ˈbæk/", "v", "gọi lại", "I'll <b>call back</b> in ten minutes.", "Mình sẽ gọi lại sau mười phút.", "折り返し電話する", "orikaeshi denwa suru"),
  ("hold", "/həʊld/", "v", "giữ máy", "Could you <b>hold</b> for a moment, please?", "Anh/chị giữ máy một lát được không ạ?"),
  ("put through", "/ˌpʊt ˈθruː/", "v", "nối máy", "I'll <b>put</b> you <b>through</b> to Mr. Tanaka.", "Tôi sẽ nối máy cho anh gặp ông Tanaka."),
  ("extension", "/ɪkˈstenʃn/", "n", "số máy lẻ", "My <b>extension</b> is 204.", "Số máy lẻ của tôi là 204.", "内線", "naisen"),
  ("mute", "/mjuːt/", "n/v", "tắt tiếng, tắt mic", "Sorry, I was on <b>mute</b>.", "Xin lỗi, nãy mình tắt mic."),
  ("connection", "/kəˈnekʃn/", "n", "kết nối, đường truyền", "My <b>connection</b> is bad today.", "Hôm nay đường truyền của mình kém."),
  ("screen", "/skriːn/", "n", "màn hình", "Let me share my <b>screen</b>.", "Để mình chia sẻ màn hình."),
  ("break up", "/ˌbreɪk ˈʌp/", "v", "(tiếng) bị ngắt quãng", "Sorry, you're <b>breaking up</b>.", "Xin lỗi, tiếng bạn bị ngắt quãng."),
  ("voicemail", "/ˈvɔɪsmeɪl/", "n", "hộp thư thoại, tin nhắn thoại", "I left a <b>voicemail</b> for Mr. Brown.", "Tôi đã để lại tin nhắn thoại cho ông Brown.", "留守番電話", "rusuban denwa"),
  ("speak up", "/ˌspiːk ˈʌp/", "v", "nói to lên", "Could you <b>speak up</b> a little, please?", "Bạn nói to lên một chút được không?"),
 ],
 "phrases": [
  ("Hello, this is Lan from ABC Company.", "Alô, tôi là Lan từ công ty ABC."),
  ("May I speak to Mr. Tanaka, please?", "Cho tôi gặp ông Tanaka được không ạ?"),
  ("Could you hold for a moment, please?", "Anh/chị giữ máy một chút được không ạ?"),
  ("I'll put you through.", "Tôi sẽ nối máy cho anh/chị."),
  ("I'm afraid she's in a meeting. Can I take a message?", "Rất tiếc chị ấy đang họp. Tôi ghi lại lời nhắn nhé?"),
  ("Could you ask him to call me back?", "Nhờ anh nhắn anh ấy gọi lại cho tôi được không?"),
  ("Sorry, you're breaking up.", "Xin lỗi, tiếng của bạn bị ngắt quãng."),
  ("I think you're on mute.", "Hình như bạn đang tắt mic."),
  ("Can everyone see my screen?", "Mọi người thấy màn hình của mình không?"),
  ("Could you speak up a little?", "Bạn nói to hơn một chút được không?"),
 ],
 "dialogues": [
  ("Hello, may I speak to Ms. Hoa, please?", [
    ("Sure, may I ask who's calling?", True, "Lịch sự hỏi tên người gọi trước khi nối máy."),
    ("Yes, you can speak.", False, "Hiểu theo nghĩa đen — người gọi muốn gặp chị Hoa."),
    ("Who are you?", False, "Quá thẳng, thiếu lịch sự khi nghe điện thoại."),
  ]),
  ("I'm afraid he's not in today.", [
    ("I see. Could I leave a message for him?", True, "Chấp nhận + xin để lại lời nhắn."),
    ("Where he go?", False, "Sai ngữ pháp ('Where did he go?') và tò mò không cần thiết."),
    ("OK. Bye.", False, "Cúp máy ngay, bỏ lỡ việc cần nhắn."),
  ]),
  ("Can you hear me OK?", [
    ("Sorry, you're breaking up a little. Could you say that again?", True, "Báo rõ vấn đề + nhờ nói lại."),
    ("I no hear you good.", False, "Sai: 'I can't hear you very well.'"),
    ("Hello? Hello? Hello?", False, "Không nói rõ vấn đề là gì."),
  ]),
  ("You're on mute, Tuấn.", [
    ("Oh, sorry! Can you hear me now?", True, "Xin lỗi + kiểm tra lại."),
    ("I am not mute.", False, "Nghe như cãi lại; 'on mute' là tắt mic, còn 'mute' (tính từ) nghĩa là câm."),
    ("Sorry, I'm silent.", False, "Dịch từng chữ, không tự nhiên."),
  ]),
  ("Could you tell him I called?", [
    ("Of course. Could I have your name and number, please?", True, "Đồng ý + xin thông tin cần thiết."),
    ("OK, I tell.", False, "Thiếu 'will' và tân ngữ: 'I'll tell him.'"),
    ("He is busy always.", False, "Sai trật tự từ ('He's always busy') và không giúp gì."),
  ]),
 ],
 "listen": [
  ("Could you hold for a moment please", ["hold", "moment"], "xin giữ máy"),
  ("I'll put you through to the sales team", ["through", "sales"], "nối máy"),
  ("Sorry, you're breaking up a little", ["breaking"], "đường truyền kém"),
  ("Can everyone see my screen now", ["everyone", "screen"], "chia sẻ màn hình"),
  ("Good afternoon, this is Minh speaking. I'm afraid Ms. Lee is not in today. Can I take a message?", ["speaking", "today", "message"], "nghe máy thay đồng nghiệp"),
  ("Hi, this is David. I'm calling about the invoice. Could you call me back before five?", ["calling", "invoice", "five"], "tin nhắn thoại"),
 ],
})

# ───────────────────────── 6. Nhờ giúp & hỏi lại cho rõ ─────────────────────────
PHASES.append({
 "title": "Nhờ giúp & hỏi lại cho rõ",
 "vocab": [
  ("favor", "/ˈfeɪvə/", "n", "việc nhờ, sự giúp đỡ", "Could you do me a <b>favor</b>?", "Bạn giúp mình một việc được không?"),
  ("give a hand", "/ɡɪv ə ˈhænd/", "phr", "giúp một tay", "Could you <b>give</b> me <b>a hand</b> with these boxes?", "Bạn giúp mình một tay với mấy cái thùng này được không?"),
  ("clarify", "/ˈklærəfaɪ/", "v", "làm rõ", "Could you <b>clarify</b> the deadline?", "Bạn nói rõ giúp mình hạn chót được không?"),
  ("repeat", "/rɪˈpiːt/", "v", "nhắc lại", "Could you <b>repeat</b> the last part?", "Bạn nhắc lại đoạn cuối được không?"),
  ("mean", "/miːn/", "v", "có ý là, nghĩa là", "What do you <b>mean</b> by 'soon'?", "'Sớm' ý bạn là khi nào?"),
  ("explain", "/ɪkˈspleɪn/", "v", "giải thích", "Can you <b>explain</b> the new process?", "Bạn giải thích quy trình mới được không?", "説明する", "setsumei suru"),
  ("example", "/ɪɡˈzɑːmpl/", "n", "ví dụ", "Could you give me an <b>example</b>?", "Bạn cho mình một ví dụ được không?"),
  ("misunderstand", "/ˌmɪsʌndəˈstænd/", "v", "hiểu nhầm", "Sorry, I <b>misunderstood</b> your email.", "Xin lỗi, mình hiểu nhầm email của bạn."),
  ("appreciate", "/əˈpriːʃieɪt/", "v", "cảm kích, trân trọng", "I really <b>appreciate</b> your help.", "Mình thật sự cảm kích sự giúp đỡ của bạn."),
  ("instruction", "/ɪnˈstrʌkʃn/", "n", "hướng dẫn, chỉ thị", "Please read the <b>instructions</b> first.", "Vui lòng đọc hướng dẫn trước.", "指示", "shiji"),
 ],
 "phrases": [
  ("Could you do me a favor?", "Bạn giúp mình một việc được không?"),
  ("Could you give me a hand with these boxes?", "Bạn giúp mình một tay với mấy cái thùng này được không?"),
  ("Sorry, could you say that again?", "Xin lỗi, bạn nói lại được không?"),
  ("What do you mean by 'soon'?", "'Sớm' là khoảng khi nào vậy?"),
  ("Just to clarify, do you need it today or tomorrow?", "Cho mình hỏi rõ: bạn cần hôm nay hay ngày mai?"),
  ("Could you give me an example?", "Bạn cho mình một ví dụ được không?"),
  ("Let me check I understand: you need three copies, right?", "Để mình kiểm tra lại: bạn cần ba bản, đúng không?"),
  ("Could you speak more slowly, please?", "Bạn nói chậm hơn một chút được không?"),
  ("Thanks, I really appreciate it.", "Cảm ơn, mình thật sự rất cảm kích."),
  ("Sorry, I misunderstood.", "Xin lỗi, mình hiểu nhầm."),
 ],
 "dialogues": [
  ("Can you get this done soon?", [
    ("Sure. Just to clarify, do you need it today or by Friday?", True, "Hỏi lại cho rõ 'soon' là khi nào."),
    ("How soon is soon you mean?", False, "Sai trật tự: 'What do you mean by soon?'"),
    ("Yes, soon.", False, "Không làm rõ — dễ hiểu lầm về thời hạn."),
  ]),
  ("The report needs to be more detailed.", [
    ("Could you give me an example of what's missing?", True, "Xin ví dụ cụ thể để sửa đúng ý."),
    ("OK, I will write more long.", False, "Sai so sánh: 'I'll make it longer' — mà dài hơn chưa chắc là chi tiết hơn."),
    ("It is detail already.", False, "Cãi lại và sai từ loại: 'It's already detailed.'"),
  ]),
  ("Could you give me a hand with this?", [
    ("Sure, what do you need?", True, "Sẵn sàng giúp + hỏi cần gì."),
    ("Give you my hand?", False, "Hiểu theo nghĩa đen — 'give me a hand' là giúp một tay."),
    ("I am busy, you do alone.", False, "Từ chối cộc lốc, sai ngữ pháp. Nếu bận: 'Sorry, I'm busy right now. Can I help after lunch?'"),
  ]),
  ("Sorry, did you say fifteen or fifty?", [
    ("Fifty. Five, zero.", True, "Nói lại rõ ràng, tách từng chữ số để tránh nhầm."),
    ("I say fifty.", False, "Sai thì: 'I said fifty.'"),
    ("Yes, fifteen or fifty.", False, "Không trả lời — người ta hỏi là số nào."),
  ]),
  ("Thanks for helping me with the slides.", [
    ("You're welcome. Happy to help anytime.", True, "Đáp lời cảm ơn tự nhiên."),
    ("Yes, you're welcome me.", False, "Chỉ nói 'You're welcome.' — không thêm 'me'."),
    ("Not at all, it's my duty.", False, "'It's my duty' nghe quá trang trọng, như dịch từng chữ 'trách nhiệm của em'."),
  ]),
 ],
 "listen": [
  ("Could you do me a favor this afternoon", ["favor", "afternoon"], "nhờ vả"),
  ("Sorry, could you say that again", ["say", "again"], "xin nhắc lại"),
  ("What do you mean by next week", ["mean", "week"], "hỏi rõ ý"),
  ("Could you give me a hand with these boxes", ["hand", "boxes"], "nhờ giúp một tay"),
  ("Just to clarify, you need twenty copies. Do you need them in color? And by what time?", ["clarify", "twenty", "color"], "hỏi lại yêu cầu in tài liệu"),
  ("Sorry, I misunderstood the instructions. I thought you wanted one file. I'll split it into three now.", ["misunderstood", "instructions", "three"], "nhận là đã hiểu nhầm"),
 ],
})

# ───────────────────────── 7. Kế hoạch, hạn chót & ưu tiên ─────────────────────────
PHASES.append({
 "title": "Kế hoạch, hạn chót & ưu tiên",
 "vocab": [
  ("deadline", "/ˈdedlaɪn/", "n", "hạn chót", "The <b>deadline</b> is next Wednesday.", "Hạn chót là thứ Tư tuần sau.", "締め切り", "shimekiri"),
  ("priority", "/praɪˈɒrəti/", "n", "việc ưu tiên, mức ưu tiên", "This report is our top <b>priority</b>.", "Báo cáo này là ưu tiên hàng đầu của tụi mình.", "優先事項", "yūsen jikō"),
  ("urgent", "/ˈɜːdʒənt/", "adj", "gấp, khẩn", "Is this <b>urgent</b>?", "Việc này có gấp không?"),
  ("postpone", "/pəˈspəʊn/", "v", "hoãn", "We have to <b>postpone</b> the meeting.", "Tụi mình phải hoãn cuộc họp.", "延期する", "enki suru"),
  ("extend", "/ɪkˈstend/", "v", "gia hạn, kéo dài", "Can we <b>extend</b> the deadline by two days?", "Mình gia hạn thêm hai ngày được không?"),
  ("timeline", "/ˈtaɪmlaɪn/", "n", "các mốc thời gian", "Here's the <b>timeline</b> for the project.", "Đây là các mốc thời gian của dự án."),
  ("estimate", "/ˈestɪmeɪt/", "v", "ước tính", "I <b>estimate</b> it'll take three days.", "Mình ước tính mất ba ngày."),
  ("milestone", "/ˈmaɪlstəʊn/", "n", "mốc quan trọng", "Our first <b>milestone</b> is the end of May.", "Mốc đầu tiên của tụi mình là cuối tháng Năm."),
  ("behind schedule", "/bɪˈhaɪnd ˈʃedjuːl/", "phr", "chậm tiến độ", "We're two days <b>behind schedule</b>.", "Tụi mình đang chậm tiến độ hai ngày."),
  ("realistic", "/ˌrɪəˈlɪstɪk/", "adj", "thực tế, khả thi", "Is Friday a <b>realistic</b> deadline?", "Hạn thứ Sáu có khả thi không?"),
 ],
 "phrases": [
  ("When is the deadline?", "Hạn chót là khi nào?"),
  ("This is our top priority this week.", "Đây là việc ưu tiên số một tuần này."),
  ("Can we push the deadline to Monday?", "Mình lùi hạn sang thứ Hai được không?"),
  ("I'm afraid we're a bit behind schedule.", "E là tụi mình hơi chậm tiến độ."),
  ("I can finish it by Thursday at the latest.", "Muộn nhất thứ Năm mình sẽ xong."),
  ("Is this urgent, or can it wait until tomorrow?", "Việc này gấp không, hay để mai được?"),
  ("Let's focus on the most important tasks first.", "Mình tập trung vào những việc quan trọng nhất trước nhé."),
  ("That deadline isn't realistic for me.", "Hạn đó không khả thi với mình."),
  ("I estimate it'll take about three days.", "Mình ước tính mất khoảng ba ngày."),
  ("The meeting has been postponed to next week.", "Cuộc họp đã được hoãn sang tuần sau."),
 ],
 "dialogues": [
  ("Can you finish the proposal by tomorrow?", [
    ("That's tight. I can send a first draft tomorrow and the final version on Friday.", True, "Không từ chối thẳng — đưa phương án khả thi."),
    ("Tomorrow I try finish.", False, "Sai: 'I'll try to finish it tomorrow' — và nghe không chắc chắn."),
    ("Cannot. Too much.", False, "Thiếu chủ ngữ, cộc lốc, không có phương án."),
  ]),
  ("Which task should I do first?", [
    ("Start with the client report. It's due today.", True, "Chỉ rõ việc ưu tiên + lý do."),
    ("All is important.", False, "Không giúp người hỏi chọn thứ tự; nên nói 'Everything is important, but…'."),
    ("You do what you like.", False, "Nghe thờ ơ, không định hướng."),
  ]),
  ("Is this urgent?", [
    ("Not really. It can wait until Monday.", True, "Trả lời mức độ gấp + mốc thời gian."),
    ("Urgent is not.", False, "Sai trật tự: 'It's not urgent.'"),
    ("Very urgent, maybe, I don't know.", False, "Mâu thuẫn, người nghe không biết phải làm gì."),
  ]),
  ("How long will the training plan take?", [
    ("I estimate about three days, including the review.", True, "Ước tính cụ thể + phạm vi công việc."),
    ("It take long time.", False, "Sai: 'It'll take a long time' — và thiếu con số."),
    ("Three days ago.", False, "'ago' nói về quá khứ, không phải thời lượng."),
  ]),
  ("We're behind schedule. What should we do?", [
    ("Let's move the less important tasks to next week and focus on the report.", True, "Đề xuất cụ thể: dời việc phụ + tập trung việc chính."),
    ("Schedule is behind us.", False, "Hiểu sai cụm 'behind schedule' (chậm tiến độ)."),
    ("We must work until midnight every day.", False, "Không thực tế, không phải giải pháp tốt."),
  ]),
 ],
 "listen": [
  ("The deadline for the proposal is next Monday", ["deadline", "Monday"], "hạn chót"),
  ("This is our top priority this week", ["top", "priority"], "việc ưu tiên"),
  ("I can finish it by Thursday at the latest", ["Thursday", "latest"], "muộn nhất khi nào"),
  ("The training has been postponed to next month", ["postponed", "month"], "hoãn lịch"),
  ("We're a little behind schedule. Can we move the deadline to Friday? I'll send the first part tomorrow.", ["behind", "Friday", "tomorrow"], "xin lùi hạn"),
  ("This is urgent. The client needs the prices today. Please do this before anything else.", ["urgent", "client", "before"], "giao việc gấp"),
 ],
})

# ───────────────────────── 8. Sự cố, xin lỗi & giải quyết ─────────────────────────
PHASES.append({
 "title": "Sự cố, xin lỗi & giải quyết",
 "vocab": [
  ("apologize", "/əˈpɒlədʒaɪz/", "v", "xin lỗi (trang trọng)", "I <b>apologize</b> for the delay.", "Tôi xin lỗi vì sự chậm trễ."),
  ("mistake", "/mɪˈsteɪk/", "n", "lỗi, sai sót", "Sorry, that was my <b>mistake</b>.", "Xin lỗi, đó là lỗi của mình.", "ミス", "misu"),
  ("issue", "/ˈɪʃuː/", "n", "vấn đề", "We have an <b>issue</b> with the delivery.", "Chúng tôi đang gặp vấn đề với việc giao hàng."),
  ("solution", "/səˈluːʃn/", "n", "giải pháp", "Let's find a <b>solution</b> together.", "Mình cùng tìm giải pháp nhé.", "解決策", "kaiketsusaku"),
  ("fix", "/fɪks/", "v", "sửa, khắc phục", "I'll <b>fix</b> the numbers and send the file again.", "Mình sẽ sửa số liệu rồi gửi lại file."),
  ("delay", "/dɪˈleɪ/", "n/v", "sự chậm trễ; làm chậm", "There's a two-day <b>delay</b> in shipping.", "Việc vận chuyển bị trễ hai ngày.", "遅延", "chien"),
  ("complaint", "/kəmˈpleɪnt/", "n", "lời phàn nàn, khiếu nại", "We got a <b>complaint</b> from a customer.", "Chúng ta nhận một lời phàn nàn từ khách hàng.", "クレーム", "kurēmu"),
  ("cause", "/kɔːz/", "n", "nguyên nhân", "What was the <b>cause</b> of the problem?", "Nguyên nhân của vấn đề là gì?", "原因", "gen'in"),
  ("prevent", "/prɪˈvent/", "v", "ngăn ngừa", "How can we <b>prevent</b> this next time?", "Lần sau làm sao để ngăn chuyện này?", "防止する", "bōshi suru"),
  ("take responsibility", "/teɪk rɪˌspɒnsəˈbɪləti/", "phr", "nhận trách nhiệm", "I <b>take responsibility</b> for the error.", "Tôi nhận trách nhiệm về sai sót này."),
 ],
 "phrases": [
  ("I'm sorry, that was my mistake.", "Xin lỗi, đó là lỗi của mình."),
  ("I apologize for the delay.", "Tôi xin lỗi vì sự chậm trễ."),
  ("Let me look into it right away.", "Để mình kiểm tra ngay."),
  ("I'll fix it and send it again today.", "Mình sẽ sửa và gửi lại trong hôm nay."),
  ("What exactly happened?", "Chính xác là chuyện gì đã xảy ra?"),
  ("The cause was a wrong number in the order.", "Nguyên nhân là một con số sai trong đơn hàng."),
  ("It won't happen again.", "Chuyện này sẽ không lặp lại nữa."),
  ("Here's what we can do to solve it.", "Đây là cách tụi mình có thể giải quyết."),
  ("Thank you for your patience.", "Cảm ơn anh/chị đã kiên nhẫn."),
  ("I take full responsibility.", "Tôi xin nhận hoàn toàn trách nhiệm."),
 ],
 "dialogues": [
  ("The numbers in your report are wrong.", [
    ("I'm sorry about that. Which part is wrong? I'll fix it right away.", True, "Xin lỗi + hỏi cụ thể + hành động ngay."),
    ("Sorry, I am wrong number.", False, "Dịch từng chữ, sai nghĩa: 'Sorry, I used the wrong numbers.'"),
    ("It's not me, Minh gave me the numbers.", False, "Đổ lỗi cho người khác, không giải quyết vấn đề."),
  ]),
  ("Why was the delivery late?", [
    ("There was a problem with the supplier. We've found a new one, so it won't happen again.", True, "Nguyên nhân + giải pháp + cam kết."),
    ("The supplier make mistake, not us.", False, "Sai thì ('made a mistake') và chỉ lo đổ lỗi."),
    ("Because late.", False, "Không giải thích được gì."),
  ]),
  ("A customer is angry about the wrong bill.", [
    ("I'll call her now, apologize and send a correct bill today.", True, "Hành động nhanh: gọi, xin lỗi, sửa hóa đơn."),
    ("I will apologize her.", False, "Thiếu giới từ: 'apologize to her'."),
    ("Customer always angry.", False, "Thiếu động từ, thái độ thiếu chuyên nghiệp."),
  ]),
  ("Sorry, I forgot to send you the file.", [
    ("No problem. Could you send it by 3 p.m.?", True, "Thông cảm + nhắc thời hạn rõ ràng."),
    ("Again? You always forget.", False, "Trách móc, không giải quyết được việc."),
    ("No problem, never mind the file.", False, "Bỏ qua việc vẫn cần làm."),
  ]),
  ("How can we stop this from happening again?", [
    ("Let's use a checklist and have a second person check the numbers before we send them.", True, "Đưa biện pháp phòng ngừa cụ thể."),
    ("We will be careful more.", False, "Sai trật tự ('more careful') và quá chung chung."),
    ("Cannot stop. Mistakes are normal.", False, "Thiếu chủ ngữ, không có giải pháp."),
  ]),
 ],
 "listen": [
  ("I apologize for the delay in my reply", ["apologize", "delay"], "xin lỗi vì chậm trễ"),
  ("That was my mistake, and I'll fix it today", ["mistake", "fix"], "nhận lỗi"),
  ("The cause of the problem was a wrong address", ["cause", "address"], "nguyên nhân"),
  ("Thank you for your patience", ["patience"], "cảm ơn vì đã kiên nhẫn"),
  ("I'm sorry for the mistake in the invoice. We charged you twice by accident. We'll send you a refund this week.", ["invoice", "twice", "refund"], "xin lỗi khách vì hóa đơn sai"),
  ("The delivery was late because of the heavy rain. The boxes will arrive tomorrow morning. We're very sorry.", ["late", "rain", "tomorrow"], "báo giao hàng trễ"),
 ],
})

# ───────────────────────── 9. Thuyết trình & số liệu ─────────────────────────
PHASES.append({
 "title": "Thuyết trình & số liệu",
 "vocab": [
  ("presentation", "/ˌpreznˈteɪʃn/", "n", "bài thuyết trình", "My <b>presentation</b> is ten minutes long.", "Bài thuyết trình của mình dài mười phút.", "プレゼン", "purezen"),
  ("slide", "/slaɪd/", "n", "trang chiếu, slide", "Let's go to the next <b>slide</b>.", "Mình sang slide tiếp theo nhé."),
  ("chart", "/tʃɑːt/", "n", "biểu đồ", "This <b>chart</b> shows our monthly sales.", "Biểu đồ này thể hiện doanh số hàng tháng."),
  ("increase", "/ɪnˈkriːs/", "v", "tăng", "Sales <b>increased</b> by 20 percent.", "Doanh số tăng 20 phần trăm.", "増加する", "zōka suru"),
  ("decrease", "/dɪˈkriːs/", "v", "giảm", "Costs <b>decreased</b> in the second quarter.", "Chi phí giảm trong quý hai.", "減少する", "genshō suru"),
  ("percent", "/pəˈsent/", "n", "phần trăm", "About 30 <b>percent</b> of our customers are new.", "Khoảng 30 phần trăm khách hàng là khách mới."),
  ("figure", "/ˈfɪɡə/", "n", "con số, số liệu", "Here are the sales <b>figures</b> for May.", "Đây là số liệu doanh số tháng Năm."),
  ("result", "/rɪˈzʌlt/", "n", "kết quả", "The <b>results</b> were better than we expected.", "Kết quả tốt hơn tụi mình mong đợi.", "結果", "kekka"),
  ("summary", "/ˈsʌməri/", "n", "phần tóm tắt", "Here's a short <b>summary</b> of the report.", "Đây là phần tóm tắt ngắn của báo cáo.", "まとめ", "matome"),
  ("budget", "/ˈbʌdʒɪt/", "n", "ngân sách", "We're still under <b>budget</b>.", "Tụi mình vẫn chưa vượt ngân sách.", "予算", "yosan"),
 ],
 "phrases": [
  ("Today I'd like to talk about our sales results.", "Hôm nay tôi muốn nói về kết quả doanh số."),
  ("Let's look at this chart.", "Mời mọi người xem biểu đồ này."),
  ("Sales went up by 15 percent.", "Doanh số tăng 15 phần trăm."),
  ("Costs went down slightly in March.", "Chi phí giảm nhẹ trong tháng Ba."),
  ("As you can see, the number of customers doubled.", "Như mọi người thấy, số khách hàng đã tăng gấp đôi."),
  ("Compared to last year, we did much better.", "So với năm ngoái, tụi mình làm tốt hơn nhiều."),
  ("On the next slide, you'll see our plan.", "Ở slide tiếp theo là kế hoạch của tụi mình."),
  ("To sum up, we met our target.", "Tóm lại, chúng ta đã đạt chỉ tiêu."),
  ("Are there any questions?", "Mọi người có câu hỏi gì không?"),
  ("That's a good question. I'll send you the details after the meeting.", "Câu hỏi hay. Tôi sẽ gửi chi tiết cho anh/chị sau buổi họp."),
 ],
 "dialogues": [
  ("Can you explain this chart?", [
    ("Sure. It shows our monthly sales. As you can see, they went up in June.", True, "Nói biểu đồ thể hiện gì + điểm chính."),
    ("This chart is sales, going up.", False, "Thiếu động từ 'shows': 'This chart shows our sales.'"),
    ("The chart is blue and red.", False, "Tả màu sắc, không giải thích ý nghĩa."),
  ]),
  ("Why did sales drop in February?", [
    ("Mainly because of the Tết holiday. Many shops were closed for a week.", True, "Nêu lý do chính + chi tiết."),
    ("Sales drop because Tết.", False, "Sai thì và thiếu 'of': 'Sales dropped because of Tết.'"),
    ("I don't know, but it's OK.", False, "Không trả lời và tỏ ra thờ ơ."),
  ]),
  ("How much did costs go up?", [
    ("By about eight percent, mostly because of higher rent.", True, "Con số + nguyên nhân chính."),
    ("Eight percents.", False, "'percent' không thêm 's': 'eight percent'."),
    ("Costs up many.", False, "Thiếu động từ và con số cụ thể."),
  ]),
  ("Could you go back to the previous slide?", [
    ("Of course. Here it is. Is this the one?", True, "Làm theo + xác nhận đúng trang."),
    ("Previous is finish.", False, "Sai ngữ pháp, không làm theo yêu cầu."),
    ("Why? I explained already.", False, "Nghe khó chịu với người nghe."),
  ]),
  ("What's the main message of your presentation?", [
    ("In short, we met our target, and we expect to grow 10 percent next year.", True, "Tóm gọn thông điệp chính trong một câu."),
    ("Main message is many things.", False, "Mơ hồ và thiếu 'The'."),
    ("My presentation has 20 slides.", False, "Trả lời sai câu hỏi — người ta hỏi ý chính."),
  ]),
 ],
 "listen": [
  ("Sales went up by fifteen percent last quarter", ["fifteen", "quarter"], "doanh số tăng"),
  ("Let's look at the chart on this slide", ["chart", "slide"], "xem biểu đồ"),
  ("Our costs went down slightly in March", ["costs", "slightly"], "chi phí giảm"),
  ("The budget for next year is two billion dong", ["budget", "billion"], "ngân sách"),
  ("As you can see, the number of customers doubled this year. Most of them came from our website. Next, let's look at costs.", ["doubled", "website", "costs"], "trình bày số liệu"),
  ("To sum up, we met our sales target. Costs were a little higher than planned. Are there any questions?", ["target", "higher", "questions"], "kết thúc bài thuyết trình"),
 ],
})

# ───────────────────────── 10. Nghỉ phép & hành chính (dùng chung cho mọi ngành) ─────────────────────────
PHASES.append({
 "title": "Nghỉ phép & hành chính",
 "vocab": [
  ("annual leave", "/ˌænjuəl ˈliːv/", "n", "nghỉ phép năm", "I have eight days of <b>annual leave</b> left.", "Mình còn tám ngày phép năm.", "有給休暇", "yūkyū kyūka"),
  ("sick leave", "/ˈsɪk liːv/", "n", "nghỉ ốm", "Tuấn is on <b>sick leave</b> today.", "Hôm nay Tuấn nghỉ ốm.", "病気休暇", "byōki kyūka"),
  ("day off", "/ˌdeɪ ˈɒf/", "n", "ngày nghỉ", "Can I take a <b>day off</b> on Friday?", "Tôi xin nghỉ một ngày vào thứ Sáu được không?", "休み", "yasumi"),
  ("approve", "/əˈpruːv/", "v", "phê duyệt", "My manager <b>approved</b> my leave request.", "Quản lý đã duyệt đơn nghỉ phép của mình.", "承認する", "shōnin suru"),
  ("handover", "/ˈhændəʊvə/", "n", "sự bàn giao công việc", "I'll do the <b>handover</b> before my holiday.", "Mình sẽ bàn giao trước kỳ nghỉ.", "引き継ぎ", "hikitsugi"),
  ("overtime", "/ˈəʊvətaɪm/", "n", "làm thêm giờ", "I worked three hours of <b>overtime</b> yesterday.", "Hôm qua mình làm thêm ba tiếng.", "残業", "zangyō"),
  ("payslip", "/ˈpeɪslɪp/", "n", "phiếu lương", "You can check your <b>payslip</b> online.", "Bạn có thể xem phiếu lương trực tuyến.", "給与明細", "kyūyo meisai"),
  ("business trip", "/ˈbɪznəs trɪp/", "n", "chuyến công tác", "I'm on a <b>business trip</b> in Singapore.", "Mình đang đi công tác ở Singapore.", "出張", "shutchō"),
  ("public holiday", "/ˌpʌblɪk ˈhɒlədeɪ/", "n", "ngày lễ", "Monday is a <b>public holiday</b>.", "Thứ Hai là ngày lễ.", "祝日", "shukujitsu"),
  ("reimburse", "/ˌriːɪmˈbɜːs/", "v", "hoàn trả (chi phí)", "The company will <b>reimburse</b> your taxi fare.", "Công ty sẽ hoàn lại tiền taxi cho bạn.", "精算する", "seisan suru"),
 ],
 "phrases": [
  ("I'd like to take three days of annual leave next month.", "Tôi muốn nghỉ phép năm ba ngày vào tháng sau."),
  ("Could I take Friday off?", "Tôi xin nghỉ thứ Sáu được không?"),
  ("I'm not feeling well, so I need to take sick leave today.", "Hôm nay tôi không khỏe nên cần nghỉ ốm."),
  ("Who will cover my work while I'm away?", "Ai sẽ làm thay việc của tôi khi tôi vắng?"),
  ("I'll finish the handover before I leave.", "Tôi sẽ bàn giao xong trước khi nghỉ."),
  ("Has my leave request been approved?", "Đơn xin nghỉ của tôi đã được duyệt chưa?"),
  ("I worked two hours of overtime yesterday.", "Hôm qua tôi làm thêm hai tiếng."),
  ("How do I claim my travel expenses?", "Tôi làm thủ tục hoàn lại chi phí đi lại thế nào?"),
  ("I'll be on a business trip to Đà Nẵng next week.", "Tuần sau tôi đi công tác Đà Nẵng."),
  ("The office is closed on Monday for the public holiday.", "Văn phòng nghỉ thứ Hai vì ngày lễ."),
 ],
 "dialogues": [
  ("How many days do you want to take off?", [
    ("Three days, from May 12 to 14. Minh will cover my work.", True, "Số ngày + ngày cụ thể + người làm thay."),
    ("I want off three day.", False, "Sai: 'I'd like to take three days off.'"),
    ("Many days, I'm tired.", False, "Mơ hồ, không nêu ngày cụ thể."),
  ]),
  ("You look sick. Are you OK?", [
    ("Not really. I have a fever, so I think I should take sick leave this afternoon.", True, "Nói tình trạng + xin nghỉ rõ ràng."),
    ("I am sick since yesterday.", False, "Sai thì: 'I've been sick since yesterday.'"),
    ("I'm sick. I go home now.", False, "Nghe như tự quyết, thiếu xin phép: 'Is it OK if I go home early?'"),
  ]),
  ("Who will cover for you while you're away?", [
    ("Lan will. I'll do a full handover with her on Thursday.", True, "Nêu người thay + kế hoạch bàn giao."),
    ("Lan cover me.", False, "Thiếu 'will' và 'for': 'Lan will cover for me.'"),
    ("Nobody, my work can wait.", False, "Không có người thay, công việc bị bỏ trống."),
  ]),
  ("Did you send your receipts from the business trip?", [
    ("Not yet. I'll send them to accounting by Wednesday.", True, "Trả lời + hẹn ngày cụ thể."),
    ("I not yet send.", False, "Sai: 'I haven't sent them yet.'"),
    ("Receipts is in my bag.", False, "Sai hòa hợp ('are') và không trả lời câu hỏi."),
  ]),
  ("Your leave request is approved. Enjoy your holiday!", [
    ("Thank you! I'll set up an out-of-office reply before I go.", True, "Cảm ơn + chuẩn bị chu đáo trước khi nghỉ."),
    ("Thank you, I enjoy.", False, "Sai: 'Thanks, I will!'"),
    ("Approved? Great, so I can leave now.", False, "Quên bàn giao và báo trước — vẫn cần chuẩn bị trước khi nghỉ."),
  ]),
 ],
 "listen": [
  ("I'd like to take three days of annual leave", ["three", "annual"], "xin nghỉ phép"),
  ("Who will cover your work next week", ["cover", "week"], "người làm thay"),
  ("I worked two hours of overtime yesterday", ["two", "overtime"], "làm thêm giờ"),
  ("Please send your receipts to the accounting team", ["receipts", "accounting"], "nộp hóa đơn"),
  ("Hi Sarah, I'm not feeling well today. I'd like to take sick leave. Hoa will answer my emails.", ["well", "sick", "emails"], "tin nhắn xin nghỉ ốm"),
  ("Reminder: the office will be closed on Monday for the public holiday. Please send your overtime forms by Friday.", ["closed", "holiday", "Friday"], "thông báo hành chính"),
 ],
})

# ───────────────────────── 11. Phỏng vấn & phát triển sự nghiệp (dùng chung cho mọi ngành) ─────────────────────────
PHASES.append({
 "title": "Phỏng vấn & phát triển sự nghiệp",
 "vocab": [
  ("interview", "/ˈɪntəvjuː/", "n/v", "buổi phỏng vấn; phỏng vấn", "My <b>interview</b> is on Tuesday at 10.", "Buổi phỏng vấn của mình vào 10 giờ thứ Ba.", "面接", "mensetsu"),
  ("CV", "/ˌsiː ˈviː/", "n", "sơ yếu lý lịch, CV", "Please send your <b>CV</b> by email.", "Vui lòng gửi CV qua email.", "履歴書", "rirekisho"),
  ("experience", "/ɪkˈspɪəriəns/", "n", "kinh nghiệm", "I have two years of <b>experience</b> in sales.", "Tôi có hai năm kinh nghiệm bán hàng.", "経験", "keiken"),
  ("strength", "/streŋθ/", "n", "điểm mạnh", "My biggest <b>strength</b> is teamwork.", "Điểm mạnh lớn nhất của tôi là làm việc nhóm.", "長所", "chōsho"),
  ("weakness", "/ˈwiːknəs/", "n", "điểm yếu", "One <b>weakness</b> of mine is public speaking.", "Một điểm yếu của tôi là nói trước đám đông.", "短所", "tansho"),
  ("internship", "/ˈɪntɜːnʃɪp/", "n", "kỳ thực tập", "I did a three-month <b>internship</b> at a bank.", "Tôi đã thực tập ba tháng ở một ngân hàng.", "インターンシップ", "intānshippu"),
  ("salary", "/ˈsæləri/", "n", "lương", "What's the starting <b>salary</b>?", "Lương khởi điểm là bao nhiêu?", "給料", "kyūryō"),
  ("promotion", "/prəˈməʊʃn/", "n", "sự thăng chức", "She got a <b>promotion</b> last year.", "Năm ngoái chị ấy được thăng chức.", "昇進", "shōshin"),
  ("skill", "/skɪl/", "n", "kỹ năng", "Communication is an important <b>skill</b>.", "Giao tiếp là một kỹ năng quan trọng.", "スキル", "sukiru"),
  ("goal", "/ɡəʊl/", "n", "mục tiêu", "What are your <b>goals</b> for next year?", "Mục tiêu năm tới của bạn là gì?", "目標", "mokuhyō"),
 ],
 "phrases": [
  ("Thank you for inviting me to this interview.", "Cảm ơn anh/chị đã mời tôi đến phỏng vấn."),
  ("I graduated in economics last year.", "Tôi tốt nghiệp ngành kinh tế năm ngoái."),
  ("I have two years of experience in customer service.", "Tôi có hai năm kinh nghiệm chăm sóc khách hàng."),
  ("My main strength is that I learn quickly.", "Điểm mạnh chính của tôi là học nhanh."),
  ("One of my weaknesses is public speaking, but I'm working on it.", "Một điểm yếu của tôi là nói trước đám đông, nhưng tôi đang cải thiện."),
  ("I'm looking for a job where I can grow.", "Tôi đang tìm một công việc giúp tôi phát triển."),
  ("In five years, I'd like to lead a small team.", "Trong năm năm tới, tôi muốn dẫn dắt một nhóm nhỏ."),
  ("What are the next steps in the hiring process?", "Các bước tiếp theo trong quy trình tuyển dụng là gì?"),
  ("I'd like to talk about my career goals.", "Tôi muốn trao đổi về mục tiêu nghề nghiệp của mình."),
  ("I'm interested in a promotion to team leader.", "Tôi mong muốn được thăng chức lên trưởng nhóm."),
 ],
 "dialogues": [
  ("Can you tell me about your experience?", [
    ("I've worked as a sales assistant for two years, mostly with foreign customers.", True, "Thì hiện tại hoàn thành + thời gian + điểm nổi bật."),
    ("I have experience two years sale.", False, "Sai trật tự: 'I have two years of experience in sales.'"),
    ("My experience is very good.", False, "Chung chung, không có thông tin cụ thể."),
  ]),
  ("What are your strengths?", [
    ("I'm organized and I work well under pressure. For example, I planned our company trip for 80 people.", True, "Điểm mạnh + ví dụ chứng minh."),
    ("I am strong.", False, "Hiểu sai — 'strong' là khỏe về thể chất; nên nói 'My strength is…'."),
    ("I good at everything.", False, "Thiếu 'am' và nghe khoe khoang, thiếu thuyết phục."),
  ]),
  ("Where do you see yourself in five years?", [
    ("I'd like to become a team leader and help train new staff.", True, "Mục tiêu rõ ràng, gắn với công việc."),
    ("I see myself in the mirror.", False, "Hiểu theo nghĩa đen — câu hỏi về mục tiêu nghề nghiệp."),
    ("Maybe I work other company.", False, "Sai ngữ pháp và gây ấn tượng xấu với nhà tuyển dụng."),
  ]),
  ("What salary are you expecting?", [
    ("Based on my experience, I'm expecting around 15 million dong a month.", True, "Có căn cứ + con số cụ thể."),
    ("I want salary high, very high.", False, "Sai trật tự từ và không có con số."),
    ("Any salary is OK.", False, "Thiếu tự tin, dễ bị trả thấp."),
  ]),
  ("Why are you leaving your current job?", [
    ("I'm looking for new challenges and a chance to use my English more.", True, "Lý do tích cực, hướng về tương lai."),
    ("Because I am boring there.", False, "Nhầm tính từ: 'I'm bored' (mình thấy chán); 'I'm boring' là mình nhàm chán."),
    ("My boss is terrible.", False, "Nói xấu sếp cũ — điều nên tránh khi phỏng vấn."),
  ]),
 ],
 "listen": [
  ("I have two years of experience in customer service", ["experience", "customer"], "kinh nghiệm"),
  ("My main strength is that I learn quickly", ["strength", "quickly"], "điểm mạnh"),
  ("Please send your CV before the end of June", ["CV", "June"], "nộp hồ sơ"),
  ("She got a promotion to team leader last month", ["promotion", "leader"], "thăng chức"),
  ("Thank you for coming in today. First, please tell us about yourself. Then we'll talk about the internship.", ["coming", "yourself", "internship"], "mở đầu buổi phỏng vấn"),
  ("We'd like to offer you the position. The salary is twelve million a month. Can you start on Monday?", ["offer", "salary", "Monday"], "báo trúng tuyển"),
 ],
})

# ───────────────────────── Vai trò (roles) ─────────────────────────
ROLES = {
 "staff": {"label": "Nhân viên văn phòng", "emoji": "🧑‍💼",
  "scenarios": [
   ("st_task", "Nhận việc từ sếp", "You are my manager giving me a new task: a one-page summary of customer feedback from last month. Explain it briefly, then check that I understand the deadline and the format."),
   ("st_help", "Nhờ đồng nghiệp giúp", "You are a busy but friendly colleague. I need your help with a spreadsheet formula. Agree to help, but ask me to wait ten minutes first."),
   ("st_mistake", "Nhận lỗi với sếp", "You are my manager. I sent an email to a client with the wrong price. Ask what happened, what I will do to fix it and how I will avoid it next time."),
   ("st_lunch", "Trò chuyện giờ nghỉ", "You are a friendly foreign colleague having lunch with me. Make small talk about the weekend, food and hobbies. Keep your sentences short."),
  ],
  "dialogues": [
   ("Can you send me the file by lunchtime?", [
     ("Sure, I'll send it before twelve.", True, "Đồng ý + mốc thời gian cụ thể."),
     ("Yes, I send you lunch.", False, "Sai nghĩa và thiếu 'will': 'I'll send it by lunchtime.'"),
     ("Maybe. I'm busy.", False, "Cộc lốc, không cho biết khi nào gửi được.")]),
   ("Did you finish the customer list?", [
     ("Almost. I've done about 80 percent, and I'll finish it this afternoon.", True, "Nêu tiến độ bằng con số + khi nào xong."),
     ("Yes finish.", False, "Thiếu chủ ngữ, sai thì: 'Yes, I've finished it.'"),
     ("I am finishing it yesterday.", False, "Sai thì: không dùng 'am finishing' với 'yesterday'.")]),
   ("Do you have a minute?", [
     ("Sure, what's up?", True, "Tự nhiên, sẵn sàng lắng nghe."),
     ("Yes, I have one minute only.", False, "Hiểu theo nghĩa đen — câu này chỉ là 'bạn rảnh chút không?'."),
     ("What you want?", False, "Thiếu trợ động từ và nghe thô: 'What can I do for you?'")]),
   ("Could you print twenty copies for the meeting?", [
     ("No problem. I'll put them on the meeting table.", True, "Đồng ý + nói rõ sẽ làm gì."),
     ("OK, I will printing.", False, "Sau 'will' dùng động từ nguyên mẫu: 'I'll print them.'"),
     ("Twenty is many.", False, "Than phiền, không trả lời yêu cầu.")]),
   ("How was your weekend?", [
     ("It was great, thanks. I went to Vũng Tàu with my family. How about you?", True, "Trả lời + hỏi lại — small talk tự nhiên."),
     ("It is good.", False, "Sai thì: cuối tuần đã qua → 'It was good.'"),
     ("Normal.", False, "Quá cộc, cuộc nói chuyện dừng lại.")]),
   ("The client says the price in your email is wrong.", [
     ("I'm sorry. Let me check it now and send the correct price within an hour.", True, "Xin lỗi + hành động + thời gian."),
     ("Not my fault, the system wrong.", False, "Đổ lỗi và thiếu động từ 'is'."),
     ("Oh. OK.", False, "Không nhận trách nhiệm, không có hướng xử lý.")]),
  ]},
 "admin": {"label": "Hành chính – Nhân sự", "emoji": "🗂️",
  "scenarios": [
   ("ad_new", "Đón nhân viên mới", "You are a new foreign employee on your first day. I work in HR and admin. Ask me about your desk, ID card, lunch and working hours."),
   ("ad_room", "Đặt phòng họp", "You are a manager who needs a meeting room for eight people next Tuesday afternoon, with a projector. Ask me to book it and confirm the details."),
   ("ad_leave", "Giải đáp nghỉ phép", "You are an employee asking me, the HR officer, how many days of annual leave you have left and how to apply for sick leave."),
   ("ad_visitor", "Tiếp khách đến công ty", "You are a visitor arriving at reception for a 10 a.m. meeting with Ms. Hoa. Give your name and company, and ask where to wait."),
  ],
  "dialogues": [
   ("Hi, it's my first day. Where should I go?", [
     ("Welcome! I'm Hoa from HR. Let me show you to your desk.", True, "Chào đón + giới thiệu + hướng dẫn."),
     ("You go floor three.", False, "Thiếu 'to the': 'Please go to the third floor.'"),
     ("Wait.", False, "Cộc lốc, thiếu lịch sự với người mới.")]),
   ("How many days of annual leave do I have left?", [
     ("You have five days left this year.", True, "Trả lời thẳng, có con số."),
     ("You have leave five day.", False, "Sai trật tự và thiếu 's': 'You have five days of leave.'"),
     ("Many days.", False, "Mơ hồ, không có số cụ thể.")]),
   ("Can you book a meeting room for Tuesday afternoon?", [
     ("Sure. Room B is free from two to four. Shall I book it?", True, "Đưa lựa chọn cụ thể + hỏi xác nhận."),
     ("OK, I booking.", False, "Sai: 'I'll book it' hoặc 'I'm booking it now.'"),
     ("Tuesday afternoon full.", False, "Thiếu động từ 'is' và không đưa phương án khác.")]),
   ("I'm here to see Ms. Hoa. I have a ten o'clock meeting.", [
     ("Good morning. May I have your name, please? I'll let her know you're here.", True, "Hỏi tên lịch sự + báo sẽ gọi người."),
     ("What your name?", False, "Thiếu 'is' và hơi cộc: 'May I have your name, please?'"),
     ("She busy. You sit.", False, "Thiếu động từ, nghe như ra lệnh.")]),
   ("When will I get my ID card?", [
     ("It'll be ready on Wednesday. I'll bring it to your desk.", True, "Có ngày cụ thể + hành động."),
     ("Your card is ready Wednesday maybe.", False, "Mơ hồ, thiếu 'will be' và 'on'."),
     ("I don't know, ask other people.", False, "Đẩy trách nhiệm, không lịch sự.")]),
   ("I feel sick. What do I need to do for sick leave?", [
     ("I'm sorry to hear that. Just fill in this form and send us a doctor's note later.", True, "Thông cảm + hướng dẫn rõ ràng."),
     ("You must come office to sign.", False, "Thiếu 'to the' và không thông cảm với người ốm."),
     ("Sick leave is difficult.", False, "Không hướng dẫn gì, gây lo lắng.")]),
  ]},
 "lead": {"label": "Trưởng nhóm / Quản lý", "emoji": "📋",
  "scenarios": [
   ("ld_assign", "Giao việc cho nhân viên", "You are a team member. I am your team leader giving you a new task. Ask questions about the deadline, the priority and who can help you."),
   ("ld_feedback", "Góp ý nhân viên", "You are a team member who has missed two deadlines this month. I am your manager giving feedback. Explain your reasons and agree on a plan with me."),
   ("ld_boss", "Báo cáo lên cấp trên", "You are my director. Ask me about my team's results this quarter, the main problem and what support I need."),
   ("ld_conflict", "Giải quyết bất đồng", "You are one of two team members who disagree about how to split the work on a project. Explain your side calmly and listen to my suggestion."),
  ],
  "dialogues": [
   ("How is your team doing this month?", [
     ("We're on track. We've finished three of our four projects, and the last one will be done next week.", True, "Kết luận trước + số liệu + mốc thời gian."),
     ("Team is OK, everybody working.", False, "Thiếu mạo từ và 'is', không có kết quả cụ thể."),
     ("Very busy, very tired.", False, "Than vãn, không báo cáo kết quả.")]),
   ("Can my team get one more person?", [
     ("Let me check the budget first. I'll give you an answer by Friday.", True, "Không hứa ngay, hẹn ngày trả lời."),
     ("OK OK, I give you.", False, "Hứa bừa và sai ngữ pháp: 'I'll'."),
     ("Impossible.", False, "Từ chối cộc, không giải thích.")]),
   ("I'm sorry, I missed the deadline again.", [
     ("Thanks for telling me. Let's talk about what's slowing you down and make a plan.", True, "Ghi nhận + hướng tới giải pháp."),
     ("Why you always late?", False, "Sai ngữ pháp ('Why are you…') và mang tính chỉ trích."),
     ("Don't do again.", False, "Thiếu tân ngữ 'it', nghe như ra lệnh.")]),
   ("Who should do the customer survey?", [
     ("Lan has done it before, so I'd like her to lead it this time.", True, "Chọn người + lý do rõ ràng."),
     ("I think Lan, because she do before.", False, "Sai: 'because she's done it before'."),
     ("Somebody do it.", False, "Không giao cho ai cụ thể.")]),
   ("Minh and Tuấn don't agree on the plan.", [
     ("Let's get them together and hear both sides before we decide.", True, "Trung lập, nghe cả hai phía."),
     ("Minh is right, Tuấn is wrong.", False, "Kết luận vội khi chưa nghe cả hai."),
     ("Not my problem.", False, "Né tránh trách nhiệm của trưởng nhóm.")]),
   ("Great job on the event last week!", [
     ("Thank you! The whole team worked really hard on it.", True, "Cảm ơn + ghi nhận công của cả nhóm."),
     ("Thank. It is nothing.", False, "Nói 'Thanks'; 'It is nothing' là dịch từng chữ 'có gì đâu'."),
     ("Yes, I know.", False, "Nghe kiêu ngạo, thiếu lời cảm ơn.")]),
  ]},
 "candidate": {"label": "Sinh viên · Ứng viên", "emoji": "🎓",
  "scenarios": [
   ("cd_interview", "Phỏng vấn thực tập", "You are an HR manager interviewing me for an internship. Ask me to introduce myself, my major, my skills and why I want to join your company."),
   ("cd_first", "Ngày đầu đi thực tập", "You are my mentor on my first day as an intern. Explain my tasks for the first week and ask if I have any questions."),
   ("cd_call", "Gọi điện hỏi kết quả", "You are an HR assistant. I am calling to ask about the result of my interview last week. Answer politely and tell me when they will decide."),
   ("cd_salary", "Thoả thuận lương", "You are a hiring manager offering me a job. Tell me the salary and ask if I accept. Negotiate a little if I ask for more."),
  ],
  "dialogues": [
   ("Tell me a little about yourself.", [
     ("I'm Hoa. I've just graduated in business, and I did a six-month internship in marketing.", True, "Ngắn gọn: tên + học vấn + kinh nghiệm."),
     ("My name Hoa, I am student finish.", False, "Thiếu 'is' và dịch từng chữ: 'I've just graduated.'"),
     ("What do you want to know?", False, "Né câu hỏi, gây ấn tượng kém.")]),
   ("What's your biggest weakness?", [
     ("I sometimes spend too long on details, so now I set a time limit for each task.", True, "Nêu điểm yếu thật + cách khắc phục."),
     ("My weak is English.", False, "'weak' là tính từ → 'My weakness is my English.'"),
     ("I have no weakness.", False, "Nghe thiếu thành thật.")]),
   ("Why do you want to work here?", [
     ("I like your focus on training young staff, and I want to grow in this field.", True, "Lý do gắn với công ty + mục tiêu bản thân."),
     ("Because salary high.", False, "Thiếu động từ và chỉ nói về tiền."),
     ("Because my house is near.", False, "Lý do không thuyết phục nhà tuyển dụng.")]),
   ("Do you have any questions for us?", [
     ("Yes. What would a typical day in this role look like?", True, "Luôn hỏi lại — cho thấy bạn quan tâm."),
     ("How many holiday I have?", False, "Sai ngữ pháp ('How many days off…?') và hỏi quyền lợi quá sớm."),
     ("No.", False, "Bỏ lỡ cơ hội thể hiện sự quan tâm.")]),
   ("When can you start?", [
     ("I can start on the first of next month.", True, "Có ngày cụ thể."),
     ("Anytime you want I come.", False, "Sai trật tự từ: 'I can start anytime.'"),
     ("I start already.", False, "Sai nghĩa và sai thì.")]),
   ("We'd like to offer you the position.", [
     ("Thank you so much! I'm happy to accept. Could you send me the offer by email?", True, "Cảm ơn + nhận lời + xin văn bản."),
     ("Really? I am very surprise.", False, "Sai: 'I'm very surprised.'"),
     ("OK good.", False, "Quá cộc cho một tin vui quan trọng.")]),
  ]},
}

# ───────────────────────── Gói ─────────────────────────
PACK = {
 "id": "office",
 "label": "Công sở chung",
 "short": "Công sở",
 "emoji": "🏢",
 "desc": "Văn phòng · họp · email · phỏng vấn",
 "persona": "a Vietnamese office worker",
 "counterpart": "a colleague or manager",
 "context": "office",
 "core": [],
 "report": {
  "title": "Báo cáo nhanh 60 giây", "short": "Báo cáo 60s", "sub": "Nói như họp giao ban 🎙️",
  "steps": [["Done", "I finished …"], ["Next", "Today I'm going to …"], ["Issues", "No issues. / I need help with …"]],
  "kind": "quick daily work update",
  "structure": "done / next / issues",
  "sample": "Yesterday I finished the monthly sales report and sent it to Sarah. Today I'm going to prepare the slides for Friday's meeting. No big issues, but I need the new price list from the sales team.",
 },
 "podcast": "Podcast công sở",
 "game_tag": "Game anime: đánh quái deadline, hạ boss sếp khó tính",
 "reverse_tag": "kiểu công sở",
 "jd_placeholder": "VD: Nhân viên hành chính công ty Nhật ở TP.HCM, viết email, họp với sếp nước ngoài, báo cáo tuần…",
 "rw_placeholder": "VD: gửi báo cáo tháng trễ một ngày, sếp hỏi lý do",
 "quips": [
  "Coffee first, then emails!",
  "Checking my inbox…",
  "This meeting could be an email!",
  "Deadline defeated!",
  "Reply all? Think twice!",
  "Paper jam? I've got this.",
  "One more slide, boss!",
  "Let's circle back after lunch.",
  "Friday report: done!",
  "Out of office… just kidding!",
 ],
 "ai": [
  ("intro", "Làm quen đồng nghiệp", "You are a new colleague from another department. We meet in the office kitchen during my first week. Introduce yourself, then ask about my role and my team."),
  ("update", "Báo cáo với sếp", "You are my manager. Ask me for a quick update on my work this week: what I finished, what is next and whether I need any help."),
  ("meeting", "Họp nhóm", "You are leading a short team meeting to plan a company year-end party. Ask for my opinion, disagree politely once and give me one action item."),
  ("phone", "Gọi điện cho đối tác", "You are a receptionist at a partner company. I am calling to speak with Mr. Brown, who is out of the office. Offer to take a message and ask for my name and number."),
  ("deadline", "Xin lùi hạn", "You are my manager. I need two more days for a report. Ask me why, what the risk is and what I can deliver on time."),
  ("leave", "Xin nghỉ phép", "You are my manager. I want to take three days of annual leave next month. Ask about the dates, who will cover my work and my handover plan."),
  ("interview", "Phỏng vấn xin việc", "You are an HR interviewer for an office job. Ask me to introduce myself, talk about my strengths and weaknesses, and explain why I want this job."),
  ("problem", "Xử lý sự cố", "You are a colleague from another team. The report I sent you had wrong numbers. Tell me politely and ask how we can fix it quickly."),
 ],
 "rev": [
  ("Mình sẽ gửi báo cáo trước 5 giờ chiều.", "I'll send the report before 5 p.m."),
  ("Bạn nói lại được không?", "Could you say that again, please?"),
  ("Xin lỗi, mình đến muộn.", "Sorry I'm late."),
  ("Cuộc họp dời sang thứ Năm.", "The meeting has been moved to Thursday."),
  ("Mình làm xong slide rồi.", "I've finished the slides."),
  ("Chiều nay bạn rảnh không?", "Are you free this afternoon?"),
  ("Để mình kiểm tra rồi báo lại bạn.", "Let me check and get back to you."),
  ("Tôi xin nghỉ thứ Sáu tuần sau.", "I'd like to take next Friday off."),
  ("Tôi đã đính kèm hợp đồng trong email này.", "I've attached the contract to this email."),
  ("Hạn chót là cuối tháng này.", "The deadline is the end of this month."),
  ("Mình cần thêm một ngày để làm xong.", "I need one more day to finish it."),
  ("Cảm ơn bạn đã giúp mình.", "Thanks for your help."),
  ("Anh ấy đang họp, tôi ghi lại lời nhắn nhé?", "He's in a meeting. Can I take a message?"),
  ("Doanh số tăng mười phần trăm so với tháng trước.", "Sales went up ten percent from last month."),
 ],
 "reading": [
  {"t": "Meeting email", "text": "Hi team,\nOur monthly meeting has been moved to Thursday at 10 a.m. in Room B. Please bring your sales numbers for October. The meeting will take about one hour.\nThanks,\nSarah", "q": [
    {"q": "When is the meeting now?", "o": ["Thursday at 10 a.m.", "Tuesday at 10 a.m.", "Thursday at 2 p.m."], "a": 0},
    {"q": "What should people bring?", "o": ["Their laptops", "October sales numbers", "A new plan"], "a": 1}]},
  {"t": "HR notice", "text": "NOTICE\nThe office will be closed on Monday, September 2, for National Day. Please send your timesheets to HR by Friday, August 30. If you have any questions, contact Hoa in HR at extension 204.", "q": [
    {"q": "Why is the office closed on Monday?", "o": ["A company trip", "Repairs", "A public holiday"], "a": 2},
    {"q": "When must timesheets be sent?", "o": ["By Monday, September 2", "By Friday, August 30", "By Thursday, August 29"], "a": 1}]},
  {"t": "Chat message", "text": "Minh: Hi Lan, are you joining the 3 p.m. call with the client? I can't make it, I'm stuck at the bank. Could you take notes and send them to me later? Thanks a lot!", "q": [
    {"q": "Why can't Minh join the call?", "o": ["He is sick", "He is at the bank", "He is in another meeting"], "a": 1},
    {"q": "What does Minh ask Lan to do?", "o": ["Take notes", "Call the bank", "Cancel the call"], "a": 0}]},
  {"t": "Out-of-office reply", "text": "Thank you for your email. I am out of the office from May 6 to May 10 with limited access to email. For urgent matters, please contact David Tran on extension 115. I will reply when I return on May 13.", "q": [
    {"q": "When will the writer be back?", "o": ["May 10", "May 6", "May 13"], "a": 2},
    {"q": "Who should you contact for something urgent?", "o": ["David Tran", "The HR team", "Nobody"], "a": 0}]},
  {"t": "Job advertisement", "text": "WE ARE HIRING: Office Assistant (full-time)\n- Answer phone calls and emails\n- Prepare documents and book meeting rooms\n- Good English and basic spreadsheet skills\nSend your CV by email before June 30. Only shortlisted candidates will be contacted.", "q": [
    {"q": "What is one task in this job?", "o": ["Driving the company car", "Teaching English", "Answering phone calls"], "a": 2},
    {"q": "How do you apply?", "o": ["Call the office", "Send your CV by email", "Visit the office"], "a": 1}]},
 ],
 "events": [
  ("interview", "Phỏng vấn xin việc", "You are the hiring manager interviewing me for an office position tomorrow. Ask me about my experience, my strengths and why I want this job."),
  ("review", "Đánh giá cuối năm", "You are my manager doing my annual performance review. Ask what I achieved this year, what was difficult and what my goals are for next year."),
  ("present", "Thuyết trình trước sếp", "You are a senior manager listening to my short presentation of this month's results. Ask me two questions about the numbers and the next steps."),
  ("partner", "Tiếp đối tác nước ngoài", "You are a foreign partner visiting our office for the first time. Make small talk first, then ask about our company and the plan for today."),
  ("onboard", "Ngày đầu đi làm", "You are my new team leader on my first day at work. Welcome me, explain what the team does and ask me a few questions about myself."),
  ("raise", "Đề xuất tăng lương", "You are my manager. I want to talk about a salary raise. Ask me what I have achieved and why I think I deserve it."),
  ("other", "Khác", ""),
 ],
 "roles": ROLES,
 "phases": PHASES,
}
