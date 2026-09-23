# -*- coding: utf-8 -*-
# v4.1 — nội dung làm giàu cho gói office (nối vào cuối gói, xem build.py)
# Lưu ý: các gói khác chỉ mượn office["phases"] (chặng 10, 11) làm "core"; phần EXTRA ở đây
# (phases2, rev, reading…) chỉ nối vào cuối gói office, không ảnh hưởng gói khác.

PHASES = []

# ───────────────────────── 12. Hội nhập & văn hoá công ty ─────────────────────────
PHASES.append({
 "title": "Hội nhập & văn hoá công ty",
 "vocab": [
  ("orientation", "/ˌɔːriənˈteɪʃn/", "n", "buổi định hướng cho nhân viên mới", "The <b>orientation</b> starts at 9 a.m. on Monday.", "Buổi định hướng bắt đầu lúc 9 giờ sáng thứ Hai.", "オリエンテーション", "orientēshon"),
  ("mentor", "/ˈmentɔː/", "n", "người kèm cặp, hướng dẫn", "Lan is your <b>mentor</b> for the first three months.", "Lan sẽ kèm bạn trong ba tháng đầu.", "メンター", "mentā"),
  ("probation", "/prəˈbeɪʃn/", "n", "thời gian thử việc", "My <b>probation</b> ends in two months.", "Hai tháng nữa mình hết thử việc.", "試用期間", "shiyō kikan"),
  ("dress code", "/ˈdres kəʊd/", "n", "quy định trang phục", "The <b>dress code</b> here is smart casual.", "Quy định trang phục ở đây là lịch sự nhưng thoải mái.", "服装規定", "fukusō kitei"),
  ("handbook", "/ˈhændbʊk/", "n", "sổ tay (nhân viên)", "You can find the rules in the employee <b>handbook</b>.", "Bạn có thể xem các quy định trong sổ tay nhân viên."),
  ("policy", "/ˈpɒləsi/", "n", "chính sách, quy định", "Our <b>policy</b> is to reply to customers within one day.", "Quy định của công ty là trả lời khách trong vòng một ngày."),
  ("culture", "/ˈkʌltʃə/", "n", "văn hoá (công ty)", "I really like the <b>culture</b> here. People help each other.", "Mình rất thích văn hoá ở đây. Mọi người hay giúp đỡ nhau.", "社風", "shafū"),
  ("access card", "/ˈækses kɑːd/", "n", "thẻ ra vào", "Don't forget your <b>access card</b>, or you can't open the door.", "Đừng quên thẻ ra vào, không là không mở được cửa đâu.", "入館証", "nyūkanshō"),
  ("facilities", "/fəˈsɪlətiz/", "n", "cơ sở vật chất, tiện ích", "Let me show you the <b>facilities</b>: the kitchen, the printer room and the gym.", "Để mình dẫn bạn đi xem các tiện ích: bếp, phòng máy in và phòng tập."),
  ("get used to", "/ɡet ˈjuːst tə/", "phr", "quen dần với", "I'm still <b>getting used to</b> the new system.", "Mình vẫn đang quen dần với hệ thống mới."),
 ],
 "phrases": [
  ("Where can I find the employee handbook?", "Mình tìm sổ tay nhân viên ở đâu nhỉ?"),
  ("Is there a dress code here?", "Ở đây có quy định về trang phục không?"),
  ("Who should I ask if I have questions?", "Nếu có thắc mắc thì mình nên hỏi ai?"),
  ("What time do people usually have lunch?", "Mọi người thường ăn trưa lúc mấy giờ?"),
  ("I'm still getting used to everything.", "Mình vẫn đang làm quen với mọi thứ."),
  ("My mentor showed me around the office.", "Người hướng dẫn đã dẫn mình đi một vòng văn phòng."),
  ("Do people here use first names?", "Ở đây mọi người gọi nhau bằng tên luôn à?"),
  ("Thanks for showing me the ropes.", "Cảm ơn bạn đã chỉ cho mình mọi thứ lúc mới vào."),
  ("My probation period is two months.", "Thời gian thử việc của mình là hai tháng."),
  ("Is it OK to leave at six, or do people usually stay late?", "Về lúc sáu giờ có sao không, hay mọi người hay ở lại muộn?"),
 ],
 "dialogues": [
  ("Welcome! How's your first week going?", [
    ("Really well, thanks. Everyone has been very helpful.", True, "Trả lời tích cực + ghi nhận mọi người, dùng hiện tại hoàn thành."),
    ("Very good, everyone help me.", False, "Sai chia động từ và thì: 'Everyone has been very helpful.'"),
    ("It's going to Friday.", False, "Hiểu 'going' theo nghĩa đen — người ta hỏi tuần đầu của bạn thế nào."),
  ]),
  ("Do you have any questions about the company policies?", [
    ("Yes, just one. How do I request a day off in the system?", True, "Có thắc mắc thì hỏi ngắn, cụ thể."),
    ("I no have question.", False, "Sai phủ định: 'I don't have any questions.'"),
    ("Policies is many.", False, "Sai hoà hợp ('are') và không trả lời — nếu không có câu hỏi thì nói 'Not right now, thanks.'"),
  ]),
  ("Sorry, you can't wear shorts in the office. It's in the dress code.", [
    ("Oh, sorry, I didn't know. I'll wear trousers from tomorrow.", True, "Xin lỗi + nói rõ sẽ sửa thế nào."),
    ("Sorry, I not know.", False, "Thiếu trợ động từ, sai thì: 'I didn't know.'"),
    ("But it's very hot today.", False, "Cãi lại quy định, nghe thiếu thiện chí."),
  ]),
  ("I'm Lan, your mentor. Let me know if you need anything.", [
    ("Thanks, Lan. Could we have a quick chat every Friday for the first month?", True, "Cảm ơn + đề xuất cụ thể cách làm việc với mentor."),
    ("Thank you, you teach me everything, OK?", False, "Nghe như ra lệnh và quá chung chung."),
    ("OK. I need.", False, "Cộc lốc, thiếu tân ngữ, không rõ cần gì."),
  ]),
  ("How do you like the company culture so far?", [
    ("I like it a lot. People are friendly, and managers listen to new ideas.", True, "Nêu ý kiến + lý do cụ thể."),
    ("I like very much the culture.", False, "Sai trật tự từ: 'I like the culture very much.'"),
    ("So far is OK.", False, "Thiếu chủ ngữ 'it': 'So far, it's OK.' — và hơi nhạt."),
  ]),
 ],
 "listen": [
  ("Your orientation starts at nine on Monday", ["orientation", "Monday"], "lịch buổi định hướng"),
  ("Please wear your access card at all times", ["wear", "card"], "quy định thẻ ra vào"),
  ("My mentor showed me around the office", ["mentor", "showed"], "người hướng dẫn"),
  ("I'm still getting used to the new system", ["getting", "system"], "làm quen với hệ thống"),
  ("Welcome to the company. Your probation period is two months. Please read the handbook before Friday.", ["probation", "handbook", "Friday"], "HR chào người mới"),
  ("Here is the kitchen, and the printer is next to the window. We usually have lunch at twelve. Feel free to join us.", ["kitchen", "printer", "lunch"], "dẫn người mới xem văn phòng"),
 ],
})

# ───────────────────────── 13. Đàm phán & thuyết phục ─────────────────────────
PHASES.append({
 "title": "Đàm phán & thuyết phục",
 "vocab": [
  ("negotiate", "/nɪˈɡəʊʃieɪt/", "v", "đàm phán, thương lượng", "We need to <b>negotiate</b> the price with the supplier.", "Tụi mình cần thương lượng giá với nhà cung cấp.", "交渉する", "kōshō suru"),
  ("proposal", "/prəˈpəʊzl/", "n", "bản đề xuất", "I'll send you our <b>proposal</b> by Friday.", "Tôi sẽ gửi bản đề xuất cho anh trước thứ Sáu."),
  ("compromise", "/ˈkɒmprəmaɪz/", "n/v", "sự thoả hiệp; nhượng bộ", "Let's find a <b>compromise</b> that works for both of us.", "Mình cùng tìm một phương án dung hoà cho cả hai bên nhé.", "妥協", "dakyō"),
  ("discount", "/ˈdɪskaʊnt/", "n", "chiết khấu, giảm giá", "Can you give us a ten percent <b>discount</b>?", "Bên anh giảm cho chúng tôi mười phần trăm được không?", "値引き", "nebiki"),
  ("terms", "/tɜːmz/", "n", "điều khoản, điều kiện", "We're happy with the payment <b>terms</b>.", "Chúng tôi đồng ý với điều khoản thanh toán.", "条件", "jōken"),
  ("persuade", "/pəˈsweɪd/", "v", "thuyết phục", "She <b>persuaded</b> the director to try the new plan.", "Chị ấy đã thuyết phục giám đốc thử kế hoạch mới."),
  ("benefit", "/ˈbenɪfɪt/", "n", "lợi ích", "The main <b>benefit</b> is a lower cost.", "Lợi ích chính là chi phí thấp hơn."),
  ("counteroffer", "/ˈkaʊntərˌɒfə/", "n", "đề nghị đáp lại, trả giá lại", "They didn't accept our price and made a <b>counteroffer</b>.", "Họ không chấp nhận giá của mình và đưa ra mức giá khác."),
  ("deal", "/diːl/", "n", "thoả thuận, giao dịch", "Great, it's a <b>deal</b>!", "Tuyệt, vậy mình chốt nhé!", "取引", "torihiki"),
  ("win-win", "/ˌwɪn ˈwɪn/", "adj", "đôi bên cùng có lợi", "This is a <b>win-win</b> solution for both teams.", "Đây là giải pháp đôi bên cùng có lợi cho cả hai nhóm."),
 ],
 "phrases": [
  ("What if we meet in the middle?", "Hay là mỗi bên nhường một chút?"),
  ("That's a bit higher than our budget.", "Mức đó hơi cao so với ngân sách của chúng tôi."),
  ("If you order 500 units, we can give you a discount.", "Nếu anh đặt 500 sản phẩm, chúng tôi có thể giảm giá."),
  ("Is that your best price?", "Đó là giá tốt nhất của bên anh chưa?"),
  ("I understand your concern, but let me explain.", "Tôi hiểu điều anh lo, nhưng để tôi giải thích."),
  ("The main benefit for you is faster delivery.", "Lợi ích chính cho bên anh là giao hàng nhanh hơn."),
  ("I need to check with my manager first.", "Tôi cần hỏi ý kiến quản lý trước đã."),
  ("Can we agree on the payment terms today?", "Hôm nay mình thống nhất điều khoản thanh toán được không?"),
  ("I think we have a deal.", "Tôi nghĩ vậy là mình chốt được rồi."),
  ("Let me put that in writing and send it to you.", "Để tôi ghi lại bằng văn bản rồi gửi anh."),
 ],
 "dialogues": [
  ("Our price is 200 dollars per unit.", [
    ("That's a bit high for us. Could you do 180 if we order 300 units?", True, "Chê khéo 'hơi cao' + đưa đề nghị có điều kiện."),
    ("Too expensive. Cheaper.", False, "Cộc lốc, không thành câu — nghe thiếu chuyên nghiệp."),
    ("Price is very high, can you discount me?", False, "Ở đây 'discount' nên dùng như danh từ: 'Could you give us a discount?'"),
  ]),
  ("Sorry, we can't give a bigger discount.", [
    ("I understand. What about free delivery instead?", True, "Chấp nhận rồi chuyển sang lợi ích khác — cách đàm phán khéo."),
    ("Why you can't?", False, "Sai trật tự câu hỏi: 'Why can't you?' — và nghe gắt."),
    ("OK, then we don't buy anything.", False, "Doạ dẫm quá sớm, dễ làm hỏng cuộc thương lượng."),
  ]),
  ("Can you deliver by the end of this month?", [
    ("Yes, we can, if you confirm the order by Friday.", True, "Đồng ý kèm điều kiện rõ ràng."),
    ("Yes, we can deliver end of month maybe.", False, "Thiếu 'by the', và 'maybe' làm mất uy tín."),
    ("We are delivery very fast.", False, "Nhầm danh từ với động từ: 'We deliver very fast.' — và chưa trả lời có kịp không."),
  ]),
  ("Why should we choose your plan and not the other one?", [
    ("Our plan costs 15 percent less, and we can start next week.", True, "Thuyết phục bằng lợi ích cụ thể, có số liệu."),
    ("Because our plan is more better.", False, "Sai so sánh: 'better', không dùng 'more better'."),
    ("Just trust me.", False, "Không đưa lý do — không thuyết phục được ai."),
  ]),
  ("OK, 180 per unit and free delivery. Do we have a deal?", [
    ("Yes, it's a deal. I'll send you the contract tomorrow.", True, "Chốt rõ ràng + bước tiếp theo."),
    ("Yes, deal is have.", False, "Dịch từng chữ: nên nói 'Yes, it's a deal.'"),
    ("Maybe, I think about it.", False, "Thiếu 'will' ('I'll think about it') và làm đối tác lưỡng lự."),
  ]),
 ],
 "listen": [
  ("Can you give us a small discount", ["give", "discount"], "xin giảm giá"),
  ("That is a bit higher than our budget", ["higher", "budget"], "chê giá khéo"),
  ("Let's find a compromise that works for both sides", ["compromise", "sides"], "tìm phương án dung hoà"),
  ("I need to check with my manager first", ["check", "first"], "xin thêm thời gian"),
  ("Thank you for the proposal. The price is fine, but the delivery time is too long. Can you do it in three weeks?", ["proposal", "delivery", "three"], "phản hồi bản đề xuất"),
  ("If you sign today, we can offer free training. That's a real benefit for your team.", ["sign", "training", "benefit"], "thuyết phục chốt hợp đồng"),
 ],
})

# ───────────────────────── 14. Làm việc với khách hàng & đối tác ─────────────────────────
PHASES.append({
 "title": "Làm việc với khách hàng & đối tác",
 "vocab": [
  ("client", "/ˈklaɪənt/", "n", "khách hàng (dịch vụ, lâu dài)", "We have a video call with the <b>client</b> at three.", "Tụi mình có cuộc gọi video với khách lúc ba giờ.", "顧客", "kokyaku"),
  ("partner", "/ˈpɑːtnə/", "n", "đối tác", "Our <b>partner</b> in Japan will visit next week.", "Đối tác bên Nhật sẽ sang thăm vào tuần sau.", "取引先", "torihikisaki"),
  ("contract", "/ˈkɒntrækt/", "n", "hợp đồng", "Please sign the <b>contract</b> and send it back.", "Vui lòng ký hợp đồng và gửi lại.", "契約", "keiyaku"),
  ("requirement", "/rɪˈkwaɪəmənt/", "n", "yêu cầu", "Let's go through the client's <b>requirements</b> again.", "Mình cùng xem lại các yêu cầu của khách nhé.", "要件", "yōken"),
  ("quotation", "/kwəʊˈteɪʃn/", "n", "bảng báo giá", "I'll send you a <b>quotation</b> this afternoon.", "Chiều nay tôi sẽ gửi anh bảng báo giá.", "見積書", "mitsumorisho"),
  ("deliver", "/dɪˈlɪvə/", "v", "giao (hàng, sản phẩm, kết quả)", "We will <b>deliver</b> the first part on May 10.", "Chúng tôi sẽ giao phần đầu tiên vào ngày 10 tháng Năm.", "納品する", "nōhin suru"),
  ("satisfied", "/ˈsætɪsfaɪd/", "adj", "hài lòng", "The client is very <b>satisfied</b> with our work.", "Khách rất hài lòng với công việc của mình."),
  ("relationship", "/rɪˈleɪʃnʃɪp/", "n", "mối quan hệ", "We have a good <b>relationship</b> with this partner.", "Tụi mình có quan hệ tốt với đối tác này."),
  ("on behalf of", "/ɒn bɪˈhɑːf əv/", "phr", "thay mặt cho", "I'm writing <b>on behalf of</b> my manager.", "Tôi viết thư này thay mặt quản lý của tôi."),
  ("expectation", "/ˌekspekˈteɪʃn/", "n", "kỳ vọng, mong đợi", "What are your <b>expectations</b> for this project?", "Anh chị kỳ vọng gì ở dự án này?"),
 ],
 "phrases": [
  ("Thank you for choosing us.", "Cảm ơn anh chị đã chọn chúng tôi."),
  ("Could you tell me more about your requirements?", "Anh chị cho tôi biết thêm về yêu cầu được không?"),
  ("I'll send you a quotation by tomorrow.", "Tôi sẽ gửi báo giá cho anh chị trước ngày mai."),
  ("Let me confirm the details with my team.", "Để tôi xác nhận lại chi tiết với nhóm."),
  ("We'll keep you updated every week.", "Hằng tuần chúng tôi sẽ cập nhật cho anh chị."),
  ("Is there anything else we can help with?", "Chúng tôi còn giúp được gì thêm không ạ?"),
  ("I'm calling on behalf of Ms. Hoa.", "Tôi gọi thay mặt chị Hoa."),
  ("We really value our relationship with you.", "Chúng tôi rất trân trọng mối quan hệ với bên anh chị."),
  ("Are you satisfied with the first part?", "Anh chị có hài lòng với phần đầu tiên không?"),
  ("I'm afraid that's not included in the contract.", "Tôi e là phần đó không nằm trong hợp đồng."),
 ],
 "dialogues": [
  ("Can you also design the invitation cards? At the same price?", [
    ("I'm afraid that's not in the contract, but I can send you a quotation for it today.", True, "Từ chối khéo + đưa phương án (báo giá phần thêm)."),
    ("No, not in contract.", False, "Cộc lốc, thiếu 'it's' và 'the'; nên nói mềm mỏng hơn."),
    ("Yes, no problem, free!", False, "Tự hứa làm miễn phí ngoài hợp đồng — dễ gây thiệt cho công ty."),
  ]),
  ("When will we get the first part?", [
    ("We'll deliver it on May 10, as planned.", True, "Có ngày cụ thể + 'as planned' giúp khách yên tâm."),
    ("We deliver soon soon.", False, "Mơ hồ, lặp từ kiểu tiếng Việt và thiếu 'will'."),
    ("I don't know, ask my boss.", False, "Đẩy trách nhiệm, thiếu chuyên nghiệp với khách."),
  ]),
  ("We're not happy with the colors in the design.", [
    ("I'm sorry to hear that. Could you tell me which parts you'd like to change?", True, "Thông cảm + hỏi cụ thể để sửa."),
    ("But the colors are beautiful.", False, "Cãi lại khách thay vì lắng nghe."),
    ("Sorry. What you want?", False, "Thiếu trợ động từ, nghe cộc: 'What would you like to change?'"),
  ]),
  ("Hello, I'm calling from Blue River Trading about our order.", [
    ("Hello, thanks for calling. Could I have your order number, please?", True, "Chào + hỏi thông tin cần thiết, lịch sự."),
    ("Yes, what order?", False, "Cộc, thiếu lời chào."),
    ("Hello, I am Lan speaking, I am not know about order.", False, "Sai: 'This is Lan speaking.' và 'I don't know about the order.'"),
  ]),
  ("Thanks for the meeting today. What are the next steps?", [
    ("I'll send you the meeting notes and a quotation by Thursday. Then we can sign the contract.", True, "Nêu rõ việc + hạn + bước sau."),
    ("Next step is I send.", False, "Thiếu tân ngữ, không rõ gửi gì, khi nào."),
    ("We will see.", False, "Mơ hồ, khách không biết chuyện gì sẽ diễn ra tiếp."),
  ]),
 ],
 "listen": [
  ("We'll send the quotation by tomorrow morning", ["quotation", "morning"], "hẹn gửi báo giá"),
  ("The client wants to change the delivery date", ["client", "date"], "khách muốn đổi lịch"),
  ("I'm calling on behalf of our sales manager", ["behalf", "sales"], "gọi thay mặt"),
  ("Please sign both copies of the contract", ["sign", "contract"], "ký hợp đồng"),
  ("Thanks for your email. We're happy with the first part. Could you send the rest by the end of June?", ["happy", "rest", "June"], "khách phản hồi"),
  ("Our partner from Osaka arrives on Tuesday. Please book a meeting room. I'd like everyone to join the lunch after that.", ["partner", "Tuesday", "lunch"], "chuẩn bị đón đối tác"),
 ],
})

# ───────────────────────── 15. Đào tạo & chia sẻ kiến thức ─────────────────────────
PHASES.append({
 "title": "Đào tạo & chia sẻ kiến thức",
 "vocab": [
  ("training", "/ˈtreɪnɪŋ/", "n", "đào tạo, khoá đào tạo", "All new staff join a two-day <b>training</b>.", "Mọi nhân viên mới đều tham gia khoá đào tạo hai ngày.", "研修", "kenshū"),
  ("workshop", "/ˈwɜːkʃɒp/", "n", "buổi hội thảo thực hành", "I'm running a <b>workshop</b> on spreadsheet tips next Friday.", "Thứ Sáu tới mình sẽ dẫn một buổi workshop về mẹo dùng bảng tính.", "ワークショップ", "wākushoppu"),
  ("trainee", "/ˌtreɪˈniː/", "n", "học viên, người được đào tạo", "We have five <b>trainees</b> this month.", "Tháng này tụi mình có năm học viên.", "研修生", "kenshūsei"),
  ("hands-on", "/ˌhændz ˈɒn/", "adj", "thực hành trực tiếp", "The course is very <b>hands-on</b>, so bring your laptop.", "Khoá học thực hành nhiều nên nhớ mang laptop nhé."),
  ("guideline", "/ˈɡaɪdlaɪn/", "n", "hướng dẫn, nguyên tắc", "Please follow the <b>guidelines</b> for writing reports.", "Vui lòng làm theo hướng dẫn viết báo cáo.", "ガイドライン", "gaidorain"),
  ("step by step", "/ˌstep baɪ ˈstep/", "phr", "từng bước một", "I'll show you <b>step by step</b>.", "Mình sẽ chỉ bạn từng bước một."),
  ("knowledge", "/ˈnɒlɪdʒ/", "n", "kiến thức", "Thanks for sharing your <b>knowledge</b> with the team.", "Cảm ơn bạn đã chia sẻ kiến thức với cả nhóm."),
  ("tip", "/tɪp/", "n", "mẹo", "Here's a useful <b>tip</b> for saving time.", "Đây là một mẹo hay để tiết kiệm thời gian."),
  ("manual", "/ˈmænjuəl/", "n", "sách hướng dẫn", "The <b>manual</b> is in the shared folder.", "Sách hướng dẫn nằm trong thư mục chung.", "マニュアル", "manyuaru"),
  ("session", "/ˈseʃn/", "n", "buổi (học, làm việc)", "The next <b>session</b> is on Thursday afternoon.", "Buổi tiếp theo vào chiều thứ Năm."),
 ],
 "phrases": [
  ("Today I'll show you how to use the new booking system.", "Hôm nay mình sẽ chỉ các bạn cách dùng hệ thống đặt lịch mới."),
  ("Please stop me if you have any questions.", "Có câu hỏi thì cứ ngắt lời mình nhé."),
  ("Let me show you step by step.", "Để mình chỉ từng bước một."),
  ("Now it's your turn. Try it yourself.", "Giờ đến lượt bạn. Bạn tự làm thử nhé."),
  ("Does that make sense?", "Như vậy bạn hiểu chưa?"),
  ("Here's a quick tip.", "Đây là một mẹo nhỏ."),
  ("You can find all the slides in the shared folder.", "Toàn bộ slide có trong thư mục chung."),
  ("Could you show me that part again?", "Bạn chỉ lại phần đó cho mình được không?"),
  ("I learned a lot from this session.", "Mình học được nhiều điều từ buổi này."),
  ("Let's take a ten-minute break.", "Mình nghỉ giải lao mười phút nhé."),
 ],
 "dialogues": [
  ("Does that make sense so far?", [
    ("Mostly, yes. But could you show me the last step again?", True, "Nói rõ phần đã hiểu và phần cần xem lại."),
    ("Yes make sense.", False, "Thiếu chủ ngữ: 'Yes, it makes sense.'"),
    ("Sense is OK.", False, "Dịch từng chữ, người nghe không hiểu bạn muốn nói gì."),
  ]),
  ("Can you run a short training for the new staff?", [
    ("Sure. I can do a one-hour session next Tuesday morning.", True, "Đồng ý + đề xuất thời lượng và thời gian."),
    ("Sure, I will training them.", False, "'training' là danh từ; nói 'I'll train them.'"),
    ("I'm not a teacher.", False, "Từ chối không lý do, thiếu tinh thần hỗ trợ."),
  ]),
  ("I tried it, but the form won't save.", [
    ("No worries. Let's look at it together. Can you share your screen?", True, "Trấn an + cùng xem vấn đề."),
    ("You do wrong.", False, "Sai thì, thiếu tân ngữ ('You did it wrong') — và nghe như trách móc."),
    ("Try again, try again.", False, "Không hướng dẫn gì cụ thể."),
  ]),
  ("How was the workshop yesterday?", [
    ("It was really useful. I learned some good tips for writing reports.", True, "Thì quá khứ + điều cụ thể học được."),
    ("It is very useful.", False, "Sai thì: chuyện hôm qua → 'It was very useful.'"),
    ("I learned many knowledges.", False, "'knowledge' không đếm được: 'I learned a lot.'"),
  ]),
  ("Could you share your notes from the training?", [
    ("Of course. I'll upload them to the shared folder this afternoon.", True, "Đồng ý + nói rõ để ở đâu, khi nào."),
    ("OK, I share you.", False, "Thiếu tân ngữ và 'with': 'I'll share them with you.'"),
    ("My notes are not beautiful.", False, "Né tránh, không trả lời yêu cầu."),
  ]),
 ],
 "listen": [
  ("The training starts at nine in Room A", ["training", "nine"], "lịch đào tạo"),
  ("Please bring your laptop to the workshop", ["laptop", "workshop"], "chuẩn bị cho buổi workshop"),
  ("Let me show you how it works step by step", ["show", "works"], "hướng dẫn từng bước"),
  ("You can find the manual in the shared folder", ["manual", "folder"], "tìm tài liệu"),
  ("Good morning, everyone. Today we'll learn how to use the new expense form. Please stop me if you have questions.", ["morning", "expense", "questions"], "mở đầu buổi đào tạo"),
  ("That's all for today. The slides are in the shared folder. Next week we'll do some hands-on practice.", ["slides", "shared", "practice"], "kết thúc buổi đào tạo"),
 ],
})

# ───────────────────────── 16. Làm việc từ xa & công cụ online ─────────────────────────
PHASES.append({
 "title": "Làm việc từ xa & công cụ online",
 "vocab": [
  ("remote", "/rɪˈməʊt/", "adj", "từ xa", "Most of our team is <b>remote</b>.", "Phần lớn thành viên nhóm mình làm việc từ xa.", "リモート", "rimōto"),
  ("work from home", "/ˌwɜːk frəm ˈhəʊm/", "phr", "làm việc tại nhà", "Can I <b>work from home</b> tomorrow?", "Mai em làm việc ở nhà được không ạ?", "在宅勤務", "zaitaku kinmu"),
  ("time zone", "/ˈtaɪm zəʊn/", "n", "múi giờ", "We're in different <b>time zones</b>, so let's meet at 4 p.m. my time.", "Mình khác múi giờ nên họp lúc 4 giờ chiều theo giờ bên mình nhé."),
  ("shared folder", "/ˌʃeəd ˈfəʊldə/", "n", "thư mục dùng chung", "I've put the file in the <b>shared folder</b>.", "Mình đã để file trong thư mục chung.", "共有フォルダ", "kyōyū foruda"),
  ("upload", "/ˌʌpˈləʊd/", "v", "tải lên", "Please <b>upload</b> your photo before Monday.", "Vui lòng tải ảnh của bạn lên trước thứ Hai."),
  ("log in", "/ˌlɒɡ ˈɪn/", "phr v", "đăng nhập", "I can't <b>log in</b> to my email.", "Mình không đăng nhập vào email được."),
  ("password", "/ˈpɑːswɜːd/", "n", "mật khẩu", "Never share your <b>password</b> with anyone.", "Đừng bao giờ đưa mật khẩu cho ai.", "パスワード", "pasuwādo"),
  ("calendar invite", "/ˈkælɪndər ˌɪnvaɪt/", "n", "lời mời họp gửi qua lịch", "I'll send you a <b>calendar invite</b> for Monday.", "Mình sẽ gửi bạn lời mời họp trên lịch cho thứ Hai."),
  ("status", "/ˈsteɪtəs/", "n", "trạng thái (trên ứng dụng chat)", "My <b>status</b> says 'Away' when I'm at lunch.", "Khi mình đi ăn trưa, trạng thái sẽ hiện 'Vắng mặt'."),
  ("touch base", "/ˌtʌtʃ ˈbeɪs/", "phr", "trao đổi nhanh, cập nhật cho nhau", "Let's <b>touch base</b> on Monday morning.", "Sáng thứ Hai mình trao đổi nhanh nhé."),
 ],
 "phrases": [
  ("I'm working from home today.", "Hôm nay mình làm việc ở nhà."),
  ("Can you see my screen?", "Bạn có thấy màn hình của mình không?"),
  ("I'll send a calendar invite for 3 p.m.", "Mình sẽ gửi lời mời họp lúc 3 giờ chiều."),
  ("What time is it there?", "Bên đó bây giờ là mấy giờ?"),
  ("The file is in the shared folder.", "File nằm trong thư mục chung."),
  ("I can't log in. Could you reset my password?", "Mình không đăng nhập được. Bạn đặt lại mật khẩu giúp mình được không?"),
  ("Sorry, my internet is slow today.", "Xin lỗi, hôm nay mạng nhà mình chậm."),
  ("Let's touch base tomorrow morning.", "Sáng mai mình trao đổi nhanh nhé."),
  ("I'll be away from 12 to 1.", "Từ 12 đến 1 giờ mình không có mặt."),
  ("Could everyone turn on their cameras, please?", "Mọi người bật camera lên giúp mình nhé."),
 ],
 "dialogues": [
  ("Are you coming to the office tomorrow?", [
    ("No, I'm working from home tomorrow, but I'll join the 10 a.m. meeting online.", True, "Kế hoạch đã định dùng hiện tại tiếp diễn + hứa vẫn họp online."),
    ("No, tomorrow I at home.", False, "Thiếu động từ: 'I'm working from home tomorrow.'"),
    ("No, I work in home.", False, "Sai giới từ: 'work from home' hoặc 'work at home'."),
  ]),
  ("What time works for you? I'm in London.", [
    ("How about 4 p.m. my time? That's 10 a.m. for you.", True, "Đề xuất giờ + quy đổi múi giờ giúp người kia."),
    ("Any time OK, you choose.", False, "Thiếu động từ 'is' và không tính đến chênh lệch múi giờ."),
    ("My time is 4 p.m. now.", False, "Không trả lời câu hỏi — người ta hỏi giờ nào tiện để họp."),
  ]),
  ("I can't find the file you mentioned.", [
    ("Sorry, I'll send you the link now. It's in the shared folder, under 'June'.", True, "Xin lỗi + gửi link + chỉ rõ vị trí."),
    ("You find in folder.", False, "Thiếu 'it' và 'the', nghe như ra lệnh."),
    ("I sent already.", False, "Thiếu tân ngữ: 'I've already sent it.' — và không giúp người kia tìm."),
  ]),
  ("Sorry, you're on mute.", [
    ("Oh, sorry! Can you hear me now?", True, "Xin lỗi + kiểm tra lại — phản xạ chuẩn khi họp online."),
    ("Yes, I am mute.", False, "Chỉ xác nhận mà không bật mic; lại nói sai: 'Sorry, I was on mute.'"),
    ("What? What? What?", False, "Lúng túng, không xử lý — chỉ cần bật mic và xin lỗi."),
  ]),
  ("Your status said 'Away' all morning. Is everything OK?", [
    ("Yes, sorry. I was at the bank. I should have updated my status.", True, "Giải thích ngắn + nhận phần lỗi của mình."),
    ("I not away, I am working.", False, "Thiếu động từ, sai thì: 'I wasn't away. I was working.' — và giọng chối bay."),
    ("Status is wrong.", False, "Đổ lỗi cho ứng dụng, không giải thích."),
  ]),
 ],
 "listen": [
  ("I'm working from home today", ["working", "home"], "báo làm ở nhà"),
  ("Please upload the file to the shared folder", ["upload", "folder"], "tải file lên"),
  ("I'll send you a calendar invite for Monday", ["calendar", "Monday"], "hẹn lịch họp online"),
  ("Sorry, I can't log in to the system", ["log", "system"], "không đăng nhập được"),
  ("Hi everyone. Sorry, my internet is slow today. I'll turn off my camera so you can hear me better.", ["internet", "camera", "hear"], "mạng chậm khi họp online"),
  ("Our partners are in Berlin, so we're in different time zones. Let's meet at four in the afternoon. I'll send the invite tonight.", ["Berlin", "zones", "invite"], "hẹn họp khác múi giờ"),
 ],
})

# ───────────────────────── 17. Phản hồi & đánh giá hiệu suất ─────────────────────────
PHASES.append({
 "title": "Phản hồi & đánh giá hiệu suất",
 "vocab": [
  ("feedback", "/ˈfiːdbæk/", "n", "phản hồi, góp ý", "Thanks for the <b>feedback</b>. It's really helpful.", "Cảm ơn góp ý của anh. Nó thật sự hữu ích.", "フィードバック", "fīdobakku"),
  ("performance", "/pəˈfɔːməns/", "n", "hiệu suất, kết quả làm việc", "My <b>performance</b> review is next week.", "Tuần sau là buổi đánh giá hiệu suất của mình."),
  ("achievement", "/əˈtʃiːvmənt/", "n", "thành tích", "Your biggest <b>achievement</b> this year was the new client.", "Thành tích lớn nhất năm nay của bạn là có thêm khách hàng mới."),
  ("improve", "/ɪmˈpruːv/", "v", "cải thiện", "I want to <b>improve</b> my presentation skills.", "Mình muốn cải thiện kỹ năng thuyết trình."),
  ("target", "/ˈtɑːɡɪt/", "n", "chỉ tiêu", "We reached our sales <b>target</b> in March.", "Tụi mình đạt chỉ tiêu doanh số trong tháng Ba."),
  ("constructive", "/kənˈstrʌktɪv/", "adj", "mang tính xây dựng", "Thanks for the <b>constructive</b> comments.", "Cảm ơn những góp ý mang tính xây dựng."),
  ("praise", "/preɪz/", "v/n", "khen ngợi; lời khen", "The director <b>praised</b> our team at the meeting.", "Giám đốc đã khen nhóm mình trong buổi họp."),
  ("evaluate", "/ɪˈvæljueɪt/", "v", "đánh giá", "Managers <b>evaluate</b> staff twice a year.", "Quản lý đánh giá nhân viên hai lần một năm.", "評価する", "hyōka suru"),
  ("self-assessment", "/ˌself əˈsesmənt/", "n", "bản tự đánh giá", "Please fill in your <b>self-assessment</b> before the review.", "Vui lòng điền bản tự đánh giá trước buổi đánh giá.", "自己評価", "jiko hyōka"),
  ("KPI", "/ˌkeɪ piː ˈaɪ/", "n", "chỉ số đánh giá hiệu quả công việc", "One of my <b>KPIs</b> is customer satisfaction.", "Một trong các KPI của mình là mức độ hài lòng của khách hàng."),
 ],
 "phrases": [
  ("Could I get some feedback on my report?", "Anh góp ý giúp em bản báo cáo được không ạ?"),
  ("You did a great job on the event.", "Bạn làm sự kiện rất tốt."),
  ("One thing you could improve is time management.", "Một điểm bạn có thể cải thiện là quản lý thời gian."),
  ("Thanks, that's really helpful.", "Cảm ơn, góp ý đó thật sự hữu ích."),
  ("What should I focus on next quarter?", "Quý tới em nên tập trung vào việc gì ạ?"),
  ("I reached 110 percent of my target.", "Em đạt 110 phần trăm chỉ tiêu."),
  ("I'd like to work on my public speaking.", "Em muốn rèn thêm kỹ năng nói trước đám đông."),
  ("Can you give me an example?", "Anh cho em một ví dụ được không?"),
  ("Next time, try to send it one day earlier.", "Lần sau cố gửi sớm hơn một ngày nhé."),
  ("I'll keep that in mind.", "Em sẽ ghi nhớ điều đó."),
 ],
 "dialogues": [
  ("Your report was good, but it was a bit long.", [
    ("Thanks for the feedback. I'll keep the next one to two pages.", True, "Cảm ơn + nói rõ lần sau sẽ sửa thế nào."),
    ("But my report need long.", False, "Sai chia động từ ('needs to be long') và phản bác ngay thay vì lắng nghe."),
    ("Sorry, sorry, I am bad.", False, "Tự hạ thấp quá mức, không có hướng cải thiện."),
  ]),
  ("What was your biggest achievement this year?", [
    ("I brought in three new clients, and I reached 110 percent of my target.", True, "Thành tích cụ thể + số liệu."),
    ("I am achieve many things.", False, "Sai: 'I achieved a lot this year.'"),
    ("I work hard every day.", False, "Chung chung, không nêu thành tích cụ thể."),
  ]),
  ("What do you think you could improve?", [
    ("I think I could plan my time better. I sometimes finish tasks at the last minute.", True, "Thẳng thắn + ví dụ thật."),
    ("I think nothing.", False, "Dịch từng chữ và nghe thiếu cầu tiến; nếu chưa chắc: 'I'm not sure. What do you think?'"),
    ("Improve is difficult for me.", False, "Dùng động từ làm chủ ngữ và không trả lời câu hỏi."),
  ]),
  ("Can I give you some feedback on your presentation?", [
    ("Of course, please do. I want to get better at it.", True, "Sẵn lòng nghe góp ý + thái độ cầu tiến."),
    ("Why? It was bad?", False, "Câu hỏi phải đảo: 'Was it bad?' — và nghe phòng thủ."),
    ("No need, thanks.", False, "Từ chối góp ý — mất cơ hội tiến bộ."),
  ]),
  ("Have you finished your self-assessment?", [
    ("Not yet. I'll send it to you by Wednesday.", True, "Trả lời thật + hẹn ngày."),
    ("I finish yesterday already.", False, "Sai thì: 'I finished it yesterday.' hoặc 'I've already finished it.'"),
    ("Self-assessment is not important.", False, "Xem nhẹ quy trình, gây ấn tượng xấu với sếp."),
  ]),
 ],
 "listen": [
  ("Thanks for the feedback on my report", ["feedback", "report"], "cảm ơn góp ý"),
  ("You reached your sales target this month", ["reached", "target"], "đạt chỉ tiêu"),
  ("Please send your self-assessment by Friday", ["self-assessment", "Friday"], "hạn nộp bản tự đánh giá"),
  ("I'd like to improve my presentation skills", ["improve", "presentation"], "mục tiêu cải thiện"),
  ("You did a great job with the new clients this year. One thing to work on is your reports. Try to make them shorter.", ["clients", "reports", "shorter"], "sếp nhận xét cuối năm"),
  ("Your performance review is on Monday at two. Please bring your self-assessment and your goals for next year.", ["review", "Monday", "goals"], "hẹn buổi đánh giá"),
 ],
})

# ───────────────────────── 18. Công tác nước ngoài & đi lại ─────────────────────────
PHASES.append({
 "title": "Công tác nước ngoài & đi lại",
 "vocab": [
  ("itinerary", "/aɪˈtɪnərəri/", "n", "lịch trình chuyến đi", "I'll email you the <b>itinerary</b> for the trip.", "Mình sẽ gửi lịch trình chuyến đi qua email."),
  ("flight", "/flaɪt/", "n", "chuyến bay", "My <b>flight</b> leaves at 7 a.m.", "Chuyến bay của mình cất cánh lúc 7 giờ sáng."),
  ("boarding pass", "/ˈbɔːdɪŋ pɑːs/", "n", "thẻ lên máy bay", "Please show your <b>boarding pass</b> at the gate.", "Vui lòng xuất trình thẻ lên máy bay ở cửa ra máy bay."),
  ("visa", "/ˈviːzə/", "n", "thị thực, visa", "Do I need a <b>visa</b> for a three-day trip?", "Đi ba ngày thì mình có cần visa không?", "ビザ", "biza"),
  ("accommodation", "/əˌkɒməˈdeɪʃn/", "n", "chỗ ở", "The company will pay for your <b>accommodation</b>.", "Công ty sẽ trả tiền chỗ ở cho bạn."),
  ("allowance", "/əˈlaʊəns/", "n", "phụ cấp", "The daily travel <b>allowance</b> is 50 dollars.", "Phụ cấp công tác mỗi ngày là 50 đô.", "出張手当", "shutchō teate"),
  ("jet lag", "/ˈdʒet læɡ/", "n", "mệt do lệch múi giờ", "I still have <b>jet lag</b>, so I'm a bit slow today.", "Mình vẫn còn mệt vì lệch múi giờ nên hôm nay hơi chậm.", "時差ボケ", "jisa boke"),
  ("receipt", "/rɪˈsiːt/", "n", "hoá đơn, biên lai", "Keep all your taxi <b>receipts</b>.", "Nhớ giữ lại toàn bộ hoá đơn taxi nhé.", "領収書", "ryōshūsho"),
  ("pick up", "/ˌpɪk ˈʌp/", "phr v", "đón (ai đó)", "Our driver will <b>pick up</b> the team at the airport.", "Tài xế bên mình sẽ đón cả nhóm ở sân bay."),
  ("expense", "/ɪkˈspens/", "n", "chi phí, khoản chi", "Please send your travel <b>expenses</b> within a week.", "Vui lòng gửi các khoản chi đi lại trong vòng một tuần.", "経費", "keihi"),
 ],
 "phrases": [
  ("I'll be in Singapore from Monday to Thursday.", "Mình sẽ ở Singapore từ thứ Hai đến thứ Năm."),
  ("Could you send me the itinerary?", "Bạn gửi mình lịch trình được không?"),
  ("Is someone picking us up at the airport?", "Có ai đón tụi mình ở sân bay không?"),
  ("My flight was delayed by two hours.", "Chuyến bay của mình bị trễ hai tiếng."),
  ("Hi, I'd like to check in. I have a reservation.", "Chào anh, tôi muốn nhận phòng. Tôi đã đặt trước."),
  ("Does the room include breakfast?", "Phòng có kèm bữa sáng không?"),
  ("Could I have a receipt, please?", "Cho tôi xin hoá đơn được không?"),
  ("Sorry, I'm still a bit jet-lagged.", "Xin lỗi, mình vẫn còn hơi mệt vì lệch múi giờ."),
  ("I'll send my expense report when I'm back.", "Về rồi mình sẽ gửi báo cáo chi phí."),
  ("What's the local time now?", "Bây giờ giờ địa phương là mấy giờ?"),
 ],
 "dialogues": [
  ("How was your flight?", [
    ("A bit long, but fine, thanks. I slept most of the way.", True, "Trả lời ngắn + chi tiết, dùng thì quá khứ đúng."),
    ("It is long and I am tired.", False, "Sai thì: chuyến bay đã qua → 'It was long.'"),
    ("Flight 305.", False, "Hiểu sai câu hỏi — người ta hỏi chuyến bay có ổn không."),
  ]),
  ("Do you have your receipts from the trip?", [
    ("Yes, I have all of them. I'll attach them to my expense form.", True, "Xác nhận + nói bước tiếp theo."),
    ("Yes, I have receipt all.", False, "Sai trật tự từ: 'I have all the receipts.'"),
    ("I lost some, but no problem.", False, "Coi nhẹ — mất hoá đơn thường không được hoàn tiền, cần báo kế toán ngay."),
  ]),
  ("Hello, welcome to Tokyo! Is this your first visit?", [
    ("Yes, it is. Thank you for picking me up.", True, "Trả lời + cảm ơn người ra đón."),
    ("Yes, first time I come.", False, "Dịch từng chữ: 'Yes, it's my first time here.'"),
    ("Yes. Where is hotel?", False, "Hỏi dồn, thiếu 'the' và quên cảm ơn người đón."),
  ]),
  ("Your flight is at 6 a.m. Can you get to the airport on time?", [
    ("Yes, I'll book a taxi for 4 a.m. to be safe.", True, "Có kế hoạch cụ thể + dư thời gian."),
    ("Yes, I will go early early.", False, "Lặp từ kiểu tiếng Việt, không có giờ cụ thể."),
    ("Can we change to afternoon?", False, "Né câu hỏi và thiếu 'the': 'Can I change to an afternoon flight?'"),
  ]),
  ("You look tired. Jet lag?", [
    ("Yes, a little. It's 3 a.m. in Vietnam right now!", True, "Trả lời vui vẻ, tự nhiên."),
    ("Yes, I am jet lag.", False, "'jet lag' là danh từ: 'I have jet lag.' hoặc 'I'm jet-lagged.'"),
    ("Yes, because the time is different very much.", False, "Dịch từng chữ: 'Yes, because of the time difference.'"),
  ]),
 ],
 "listen": [
  ("My flight leaves at seven tomorrow morning", ["flight", "seven"], "giờ bay"),
  ("Please keep all your taxi receipts", ["taxi", "receipts"], "giữ hoá đơn"),
  ("A driver will pick you up at the airport", ["driver", "airport"], "được đón ở sân bay"),
  ("Do I need a visa for this trip", ["visa", "trip"], "hỏi về thị thực"),
  ("Here is your itinerary. You fly to Bangkok on Monday. The meeting with our partner is on Tuesday morning.", ["itinerary", "Bangkok", "partner"], "lịch trình công tác"),
  ("Welcome back! Please send your expense form and receipts to accounting by Friday. The daily allowance is paid next month.", ["expense", "Friday", "allowance"], "sau chuyến công tác"),
 ],
})

# ───────────────────────── 19. Tiệc công ty & xã giao ─────────────────────────
PHASES.append({
 "title": "Tiệc công ty & xã giao",
 "vocab": [
  ("year-end party", "/ˌjɪər end ˈpɑːti/", "n", "tiệc tất niên", "The <b>year-end party</b> is on December 20.", "Tiệc tất niên vào ngày 20 tháng Mười Hai.", "忘年会", "bōnenkai"),
  ("toast", "/təʊst/", "n", "lời nâng ly chúc mừng", "Our director will make a <b>toast</b> at the start.", "Giám đốc sẽ nâng ly chúc mừng lúc mở đầu.", "乾杯", "kanpai"),
  ("cheers", "/tʃɪəz/", "excl", "zô, cạn ly (khi nâng ly)", "<b>Cheers</b>, everyone! Happy New Year!", "Zô nào mọi người! Chúc mừng năm mới!"),
  ("invitation", "/ˌɪnvɪˈteɪʃn/", "n", "lời mời, thiệp mời", "Thanks for the <b>invitation</b>. I'd love to come.", "Cảm ơn lời mời. Mình rất muốn đến.", "招待", "shōtai"),
  ("RSVP", "/ˌɑːr es viː ˈpiː/", "v/n", "báo lại có tham dự hay không", "Please <b>RSVP</b> by Friday.", "Vui lòng báo lại việc tham dự trước thứ Sáu."),
  ("get-together", "/ˈɡet təˌɡeðə/", "n", "buổi gặp mặt thân mật", "We're having a small <b>get-together</b> after work.", "Tan làm tụi mình có buổi gặp mặt nhỏ."),
  ("catch up", "/ˌkætʃ ˈʌp/", "phr v", "hàn huyên, hỏi thăm tình hình", "Let's grab a coffee and <b>catch up</b>.", "Mình đi cà phê hàn huyên chút nhé."),
  ("hobby", "/ˈhɒbi/", "n", "sở thích", "Do you have any <b>hobbies</b>?", "Bạn có sở thích gì không?", "趣味", "shumi"),
  ("compliment", "/ˈkɒmplɪmənt/", "n", "lời khen", "Thanks for the <b>compliment</b>!", "Cảm ơn lời khen nhé!"),
  ("team building", "/ˌtiːm ˈbɪldɪŋ/", "n", "hoạt động gắn kết đội nhóm", "The <b>team building</b> trip is in Phan Thiết this year.", "Chuyến team building năm nay đi Phan Thiết.", "チームビルディング", "chīmu birudingu"),
 ],
 "phrases": [
  ("Thanks for inviting me.", "Cảm ơn bạn đã mời mình."),
  ("I'd love to come, but I have other plans that night.", "Mình rất muốn đi, nhưng tối đó mình có hẹn khác rồi."),
  ("Can I get you a drink?", "Mình lấy đồ uống cho bạn nhé?"),
  ("I don't drink alcohol. Juice is fine, thanks.", "Mình không uống rượu bia. Nước ép là được rồi, cảm ơn."),
  ("I'd like to make a toast to our team.", "Tôi xin nâng ly chúc mừng cả nhóm."),
  ("So, what do you do for fun?", "Vậy lúc rảnh bạn hay làm gì cho vui?"),
  ("It was great to catch up with you.", "Rất vui được hàn huyên với bạn."),
  ("I love your dress. — Thanks, that's kind of you!", "Váy bạn đẹp quá. — Cảm ơn, bạn dễ thương quá!"),
  ("I should get going. See you on Monday!", "Mình phải về đây. Hẹn gặp thứ Hai nhé!"),
  ("Have you tried the spring rolls? They're really good.", "Bạn ăn thử chả giò chưa? Ngon lắm đó."),
 ],
 "dialogues": [
  ("Are you coming to the year-end party on Friday?", [
    ("Yes, I wouldn't miss it! Are you going too?", True, "Nhận lời vui vẻ + hỏi lại."),
    ("Yes, I will coming.", False, "Sau 'will' dùng nguyên mẫu: 'I'll come.' hoặc 'I'm coming.'"),
    ("Maybe. Depends.", False, "Cộc lốc, không rõ ràng — nên nói rõ có đi hay không, vì sao."),
  ]),
  ("Can I get you a beer?", [
    ("Thanks, but I don't drink. I'll have some juice.", True, "Từ chối lịch sự + nói mình muốn uống gì."),
    ("No. I no drink.", False, "Sai phủ định: 'I don't drink.' — và nghe cộc."),
    ("Beer is not good for health.", False, "Nghe như giảng giải, làm người mời khó xử."),
  ]),
  ("So, what do you do in your free time?", [
    ("I play badminton on weekends, and I'm learning to cook. How about you?", True, "Sở thích cụ thể + hỏi lại để câu chuyện tiếp tục."),
    ("I have free time on Sunday.", False, "Trả lời lạc ý — người ta hỏi bạn làm gì lúc rảnh."),
    ("My hobby is play badminton.", False, "Sau 'is' dùng V-ing: 'My hobby is playing badminton.'"),
  ]),
  ("Your speech tonight was great!", [
    ("Oh, thank you! I was really nervous.", True, "Nhận lời khen tự nhiên, không chối."),
    ("No, no, my speech is very bad.", False, "Chối lời khen kiểu khiêm tốn quá mức làm người khen khó xử; lại sai thì ('was')."),
    ("I know.", False, "Nghe kiêu ngạo, thiếu lời cảm ơn."),
  ]),
  ("It's getting late. Are you heading home?", [
    ("Yes, I should get going. Thanks for a great evening!", True, "Chào ra về lịch sự + cảm ơn."),
    ("Yes, I go home now, bye.", False, "Sai thì ('I'm going home now') và quên cảm ơn."),
    ("Heading? My head is OK.", False, "Hiểu nhầm 'heading home' (đang về nhà) theo nghĩa đen."),
  ]),
 ],
 "listen": [
  ("The year-end party starts at seven on Friday", ["party", "Friday"], "giờ tiệc tất niên"),
  ("Please RSVP by the end of this week", ["RSVP", "week"], "báo tham dự"),
  ("Let's grab a coffee and catch up soon", ["coffee", "catch"], "hẹn hàn huyên"),
  ("I'd like to make a toast to our amazing team", ["toast", "amazing"], "nâng ly"),
  ("Thank you all for a great year. Please raise your glasses. Cheers to next year!", ["great", "glasses", "Cheers"], "phát biểu nâng ly"),
  ("This year's team building trip is in Đà Lạt. We'll leave on Saturday morning. Please tell Hoa if you can't join.", ["building", "Saturday", "join"], "thông báo team building"),
 ],
})

EXTRA = {
 "phases": PHASES,
 "rev": [
  ("Tuần đầu của bạn thế nào?", "How was your first week?"),
  ("Ở đây có quy định trang phục không?", "Is there a dress code here?"),
  ("Đó là giá tốt nhất của bên anh chưa?", "Is that your best price?"),
  ("Nếu đặt nhiều hơn, bên anh có giảm giá không?", "If we order more, can you give us a discount?"),
  ("Tôi sẽ gửi báo giá trước ngày mai.", "I'll send the quotation by tomorrow."),
  ("Phần này không có trong hợp đồng.", "This part isn't in the contract."),
  ("Để mình chỉ bạn từng bước.", "Let me show you step by step."),
  ("File nằm trong thư mục chung.", "The file is in the shared folder."),
  ("Hôm nay mình làm việc ở nhà.", "I'm working from home today."),
  ("Bên đó bây giờ là mấy giờ?", "What time is it there now?"),
  ("Cảm ơn góp ý của anh.", "Thanks for your feedback."),
  ("Tháng này em đạt chỉ tiêu.", "I reached my target this month."),
  ("Chuyến bay của tôi bị trễ hai tiếng.", "My flight was delayed by two hours."),
  ("Cho tôi xin hoá đơn.", "Could I have a receipt, please?"),
  ("Mình không uống rượu bia, cảm ơn.", "I don't drink alcohol, thanks."),
  ("Cảm ơn bạn đã mời mình.", "Thanks for inviting me."),
 ],
 "reading": [
  {"t": "Welcome email", "text": "Hi Nam,\nWelcome to the team! Your first day is Monday, June 3. Please come to the reception on the 5th floor at 8:30 a.m. Bring your ID card and your bank details for the salary form. Lan will be your mentor and will show you around.\nBest,\nHoa (HR)", "q": [
    {"q": "What time should Nam arrive?", "o": ["9:00 a.m.", "8:30 a.m.", "5:30 p.m."], "a": 1},
    {"q": "What should Nam bring?", "o": ["His laptop", "A photo", "His ID card and bank details"], "a": 2}]},
  {"t": "Quotation", "text": "QUOTATION No. Q-0412\nTo: Green Leaf Co.\nItem: Office chairs (model C2) × 40\nUnit price: 1,200,000 VND\nDiscount: 5% for orders over 30 units\nDelivery: within 10 working days\nValid until: July 15", "q": [
    {"q": "How many chairs are in the quotation?", "o": ["30", "40", "15"], "a": 1},
    {"q": "Why is there a discount?", "o": ["The order is over 30 units", "The customer pays early", "It is a holiday sale"], "a": 0}]},
  {"t": "Remote work notice", "text": "REMOTE WORK POLICY (update)\nFrom October, staff can work from home up to two days a week. Please tell your manager by Friday of the week before. On remote days, keep your chat status updated and join all meetings with your camera on.", "q": [
    {"q": "How many days a week can staff work from home?", "o": ["One", "Three", "Up to two"], "a": 2},
    {"q": "What must staff do on remote days?", "o": ["Keep their chat status updated", "Come to the office in the morning", "Call their manager every hour"], "a": 0}]},
  {"t": "Training invite", "text": "Calendar invite: New expense system – training\nWhen: Thursday, 2:00–3:30 p.m.\nWhere: Room C (or join online)\nWho: all team leaders\nPlease bring your laptop. The session is hands-on. The slides will be shared after the training.", "q": [
    {"q": "Who should join the training?", "o": ["All new staff", "All team leaders", "Only the accounting team"], "a": 1},
    {"q": "What will happen after the training?", "o": ["There will be a test", "A party will start", "The slides will be shared"], "a": 2}]},
  {"t": "Party invitation", "text": "YEAR-END PARTY\nFriday, December 20, 6:30 p.m.\nRiverside Restaurant, 2nd floor\nDinner, games and a lucky draw. Vegetarian food available.\nPlease RSVP to Minh by December 13. Family members are welcome.", "q": [
    {"q": "What should you do by December 13?", "o": ["Buy a ticket", "Tell Minh if you are coming", "Send a gift"], "a": 1},
    {"q": "Who else can come to the party?", "o": ["Family members", "Clients", "Only managers"], "a": 0}]},
 ],
 "ai": [
  ("negotiate", "Đàm phán giá", "You are a supplier selling printing services to my company. Your price is 20 percent above my budget. Negotiate with me, ask about the order size and payment terms, and agree to a small discount only if I give a good reason."),
  ("client", "Làm việc với khách hàng", "You are a client who hired my company to organize a staff event. You want to add extra activities that are not in the contract. Ask me politely and see how I handle it."),
  ("feedback", "Nhận góp ý từ sếp", "You are my manager giving me feedback on a report I wrote. Say two good things and one thing to improve. Then ask me what I will change next time."),
  ("remote", "Họp online khác múi giờ", "You are a colleague in another country on a video call with me. The connection is not great and we are in different time zones. Plan a follow-up meeting time with me and ask where to find the shared files."),
 ],
 "events": [
  ("workshop", "Dẫn buổi đào tạo nội bộ", "You are a new colleague attending a short training session that I am running. Ask me two or three questions about the steps, and ask me to repeat one part more slowly."),
  ("trip", "Đi công tác nước ngoài", "You are a foreign partner meeting me at the airport on my first business trip to your country. Welcome me, make small talk about my flight and explain the plan for the next two days."),
  ("party", "Tiệc tất niên công ty", "You are a foreign colleague at our company year-end party. Make small talk about the year, the food and holiday plans. At some point, ask me to say a few words for a toast."),
 ],
 "quips": [
  "Welcome aboard, rookie!",
  "Let's meet in the middle!",
  "Can you hear me now?",
  "Jet lag? Coffee fixes it!",
  "Cheers to Friday!",
  "Feedback is a gift… I think!",
 ],
 "roles": {
  "staff": {
   "scenarios": [
    ("st_remote", "Họp online từ nhà", "You are my team leader. I am working from home today and my internet is slow during our video call. Ask me for a quick update and agree on how we will stay in touch for the rest of the day."),
    ("st_party", "Rủ đồng nghiệp đi tiệc", "You are a foreign colleague who is new and a bit shy. I invite you to the team's Friday get-together. Ask about the place, the time and what people usually do there."),
   ],
   "dialogues": [
    ("Could you show me how to use the new expense form?", [
      ("Sure. Let me show you step by step. First, open the form in the shared folder.", True, "Đồng ý + bắt đầu hướng dẫn rõ ràng."),
      ("Easy, you do yourself.", False, "Cộc lốc, thiếu tân ngữ 'it' — nên giúp hoặc hẹn lúc khác."),
      ("OK, I show you tomorrow maybe.", False, "Thiếu 'will', và 'maybe' làm người nhờ không yên tâm.")]),
    ("Are you joining the team dinner tonight?", [
      ("I'd love to, but I have to pick up my son. Maybe next time!", True, "Từ chối khéo + lý do + hẹn lần sau."),
      ("No, I busy.", False, "Thiếu 'am' và quá cộc."),
      ("Dinner is what time?", False, "Sai trật tự câu hỏi: 'What time is dinner?' — và chưa trả lời có đi không.")]),
    ("Can you touch base with the client this afternoon?", [
      ("Sure, I'll call them at three and let you know how it goes.", True, "Nhận việc + giờ cụ thể + hứa báo lại."),
      ("Touch what?", False, "Chưa hiểu thành ngữ thì hỏi lịch sự: 'Sorry, do you mean call the client?'"),
      ("I call client, OK.", False, "Thiếu 'will' và 'the': 'I'll call the client.'")]),
    ("You did a great job on the report.", [
      ("Thank you! I'm glad it was useful.", True, "Nhận lời khen tự nhiên."),
      ("No, it is not good.", False, "Chối lời khen kiểu khiêm tốn quá mức, người khen khó xử."),
      ("Thanks. So can I get a raise?", False, "Chuyển chủ đề đột ngột, không phù hợp lúc này.")]),
   ]},
  "admin": {
   "scenarios": [
    ("ad_trip", "Đặt lịch công tác cho sếp", "You are a manager going on a three-day business trip to Singapore. I am the admin assistant. Tell me your dates, ask me to book the flight and hotel, and ask about the travel allowance."),
    ("ad_orient", "Dẫn buổi định hướng", "You are a new employee at your orientation. I am from HR. Ask me about the probation period, the dress code and the company's leave policy."),
   ],
   "dialogues": [
    ("Do I need to keep my taxi receipts from the trip?", [
      ("Yes, please. We need all the receipts to reimburse you.", True, "Trả lời rõ + nêu lý do."),
      ("Yes, keep all.", False, "Thiếu tân ngữ, cộc: 'Yes, please keep all of them.'"),
      ("Not need, we trust you.", False, "Sai ngữ pháp và sai quy trình — kế toán cần hoá đơn để hoàn tiền.")]),
    ("How long is the probation period?", [
      ("It's two months. Your manager will do a short review at the end.", True, "Có con số + nói điều xảy ra sau đó."),
      ("Two month.", False, "Thiếu 's': 'Two months.' — và nên nói câu đầy đủ."),
      ("Probation is not long, don't worry.", False, "Không trả lời bằng con số cụ thể.")]),
    ("Can you book my flight to Hà Nội for Monday morning?", [
      ("Sure. There's a 7 a.m. flight and a 9 a.m. flight. Which one do you prefer?", True, "Đưa lựa chọn + hỏi ý."),
      ("OK, I book flight.", False, "Thiếu 'will' và 'the': 'I'll book the flight.'"),
      ("Morning flight is expensive.", False, "Chỉ nhận xét mà không giải quyết yêu cầu.")]),
    ("What's the dress code for the year-end party?", [
      ("It's smart casual. You don't need a suit.", True, "Trả lời thẳng + nói rõ thêm."),
      ("Dress code is dress.", False, "Dịch vụng, không có nghĩa."),
      ("You wear what you like, I don't care.", False, "'I don't care' nghe thô lỗ.")]),
   ]},
  "lead": {
   "scenarios": [
    ("ld_review", "Buổi đánh giá hiệu suất", "You are a team member at your mid-year performance review. I am your manager. Talk about your achievements, react calmly to one piece of constructive feedback and ask what you should focus on next."),
    ("ld_budget", "Thuyết phục sếp duyệt ngân sách", "You are my director. I want a bigger budget for team training next year. Ask me about the benefits, the cost and why now. Agree only if I give clear reasons."),
   ],
   "dialogues": [
    ("Can you give me some feedback on my work?", [
      ("Sure. Your reports are clear. One thing to improve is replying to clients faster.", True, "Khen cụ thể trước, góp ý cụ thể sau."),
      ("Your work is so-so.", False, "Mơ hồ và dễ làm nhân viên nản."),
      ("Everything is bad, you must change.", False, "Tiêu cực, không có ví dụ, không mang tính xây dựng.")]),
    ("Why should we spend money on this training?", [
      ("It'll save the team about five hours a week, so it will pay for itself in two months.", True, "Thuyết phục bằng lợi ích + con số."),
      ("Because training is good.", False, "Lý do chung chung, không thuyết phục."),
      ("Everybody want it.", False, "Sai chia động từ ('wants') và không nêu lợi ích.")]),
    ("I'm new. How does the team usually work?", [
      ("We meet every Monday, and we use the group chat for quick questions. Lan will be your mentor.", True, "Giải thích nếp làm việc + giao người hỗ trợ."),
      ("You will know later.", False, "Bỏ mặc người mới."),
      ("Team work hard, very hard.", False, "Thiếu 'The', sai chia động từ ('works') và không có thông tin.")]),
    ("The client wants a 15 percent discount.", [
      ("Let's offer five percent and free delivery, and see how they respond.", True, "Đưa phương án thoả hiệp cụ thể."),
      ("OK, give them.", False, "Nhượng bộ ngay, thiếu tân ngữ, không hề đàm phán."),
      ("No way. Tell them go away.", False, "Thiếu 'to' và làm hỏng quan hệ với khách.")]),
   ]},
  "candidate": {
   "scenarios": [
    ("cd_probation", "Hết thử việc – gặp sếp", "You are my manager at the end of my two-month probation. Tell me I passed, give me one piece of feedback and ask about my goals for the next six months."),
    ("cd_policy", "Hỏi về chính sách công ty", "You are an HR manager at the end of my job interview. I ask about training for new staff, the remote work policy and the probation period. Answer clearly and briefly."),
   ],
   "dialogues": [
    ("How was your first month here?", [
      ("It went well. I've learned a lot, especially from my mentor.", True, "Thì quá khứ + ghi nhận người hướng dẫn."),
      ("It is go well.", False, "Sai: 'It went well.'"),
      ("Very tired, a lot of work.", False, "Than vãn, không thành câu hoàn chỉnh.")]),
    ("Congratulations, you've passed your probation!", [
      ("Thank you so much! I'm really happy to stay with the team.", True, "Cảm ơn + bày tỏ niềm vui."),
      ("Really? I think I fail.", False, "Sai thì ('I thought I'd failed') và thiếu tự tin."),
      ("OK. So my salary goes up now?", False, "Hỏi lương ngay lập tức, nghe thực dụng.")]),
    ("Do you have any questions about our training program?", [
      ("Yes. How long is the training, and is it online or in the office?", True, "Câu hỏi cụ thể, cho thấy bạn quan tâm."),
      ("Training is free?", False, "Nên hỏi đúng dạng câu hỏi: 'Is the training free?'"),
      ("No, I know everything.", False, "Nghe kiêu, không cầu tiến.")]),
    ("We offer hybrid work: three days in the office and two days at home.", [
      ("That sounds great. Are the office days fixed?", True, "Phản hồi tích cực + hỏi thêm chi tiết."),
      ("I want five days at home.", False, "Đòi hỏi thẳng, nghe thiếu linh hoạt."),
      ("Hybrid is what?", False, "Sai trật tự câu hỏi: 'What does hybrid mean?'")]),
   ]},
 },
}
