# -*- coding: utf-8 -*-
# Gói "health" — Y tế · Điều dưỡng: điều dưỡng, lễ tân phòng khám, nhà thuốc · dược, chăm sóc · hộ lý
# phục vụ bệnh nhân / bác sĩ nói tiếng Anh ở Việt Nam (phòng khám quốc tế, bệnh viện có khoa quốc tế).
# ĐÂY LÀ TIẾNG ANH GIAO TIẾP CHO NHÂN VIÊN, KHÔNG PHẢI TƯ VẤN Y KHOA: không đưa liều lượng hay chẩn đoán;
# câu đúng luôn mô phỏng thực hành an toàn (xác nhận danh tính, hỏi dị ứng, báo bác sĩ khi cần).
# Tên phòng khám / bệnh viện đều tự đặt (Sen Xanh Clinic, An Tâm Hospital…).
# Chặng lõi lấy từ office: 10 (Nghỉ phép & hành chính), 11 (Phỏng vấn & phát triển sự nghiệp).
# Schema: xem packs_src/README.md. Build: python3 packs_src/build.py health

PHASES = []

# ───────────────────────── 0. Tiếp đón & đăng ký khám ─────────────────────────
PHASES.append({
 "title": "Tiếp đón & đăng ký khám",
 "vocab": [
  ("appointment", "/əˈpɔɪntmənt/", "n", "lịch hẹn khám", "Do you have an <b>appointment</b> today?", "Hôm nay anh/chị có lịch hẹn khám không ạ?", "予約", "yoyaku"),
  ("reception", "/rɪˈsepʃn/", "n", "quầy lễ tân, quầy tiếp đón", "Please go to <b>reception</b> first.", "Anh/chị vui lòng đến quầy tiếp đón trước ạ.", "受付", "uketsuke"),
  ("registration form", "/ˌredʒɪˈstreɪʃn fɔːm/", "n", "phiếu đăng ký khám", "Please fill in this <b>registration form</b>.", "Anh/chị vui lòng điền phiếu đăng ký khám này ạ."),
  ("waiting room", "/ˈweɪtɪŋ ruːm/", "n", "phòng chờ", "Please have a seat in the <b>waiting room</b>.", "Mời anh/chị ngồi chờ ở phòng chờ ạ.", "待合室", "machiaishitsu"),
  ("walk-in", "/ˈwɔːk ɪn/", "n/adj", "khách/bệnh nhân đến không hẹn trước", "We accept <b>walk-in</b> patients until 4 p.m.", "Phòng khám nhận bệnh nhân không hẹn trước đến 4 giờ chiều."),
  ("queue number", "/ˈkjuː ˌnʌmbə/", "n", "số thứ tự", "Your <b>queue number</b> is 25.", "Số thứ tự của anh/chị là 25."),
  ("ID card", "/ˌaɪ ˈdiː kɑːd/", "n", "giấy tờ tùy thân (CCCD, hộ chiếu…)", "May I see your passport or <b>ID card</b>, please?", "Cho em xem hộ chiếu hoặc giấy tờ tùy thân được không ạ?", "身分証", "mibunshō"),
  ("date of birth", "/ˌdeɪt əv ˈbɜːθ/", "n", "ngày sinh", "Could you tell me your full name and <b>date of birth</b>?", "Anh/chị cho em biết họ tên đầy đủ và ngày sinh ạ.", "生年月日", "seinengappi"),
  ("specialist", "/ˈspeʃəlɪst/", "n", "bác sĩ chuyên khoa", "Would you like to see a skin <b>specialist</b>?", "Anh/chị có muốn khám bác sĩ chuyên khoa da liễu không ạ?", "専門医", "senmon'i"),
  ("first visit", "/ˌfɜːst ˈvɪzɪt/", "n", "lần khám đầu tiên", "Is this your <b>first visit</b> to our clinic?", "Đây có phải lần đầu anh/chị khám ở phòng khám mình không ạ?", "初診", "shoshin"),
 ],
 "phrases": [
  ("Good morning. How can I help you?", "Chào buổi sáng. Em có thể giúp gì cho anh/chị ạ?"),
  ("Do you have an appointment?", "Anh/chị có lịch hẹn trước không ạ?"),
  ("Is this your first visit here?", "Đây là lần đầu anh/chị khám ở đây phải không ạ?"),
  ("Could you fill in this form, please?", "Anh/chị điền giúp em phiếu này nhé."),
  ("May I see your passport, please?", "Cho em xem hộ chiếu của anh/chị được không ạ?"),
  ("Could you spell your last name for me?", "Anh/chị đánh vần giúp em họ của mình được không ạ?"),
  ("Which doctor would you like to see?", "Anh/chị muốn khám với bác sĩ nào ạ?"),
  ("The waiting time is about twenty minutes.", "Thời gian chờ khoảng hai mươi phút ạ."),
  ("Please take a seat. We'll call your number.", "Mời anh/chị ngồi. Bên em sẽ gọi số của anh/chị."),
  ("Would you like an interpreter?", "Anh/chị có cần người phiên dịch không ạ?"),
 ],
 "dialogues": [
  ("Hi, I'd like to see a doctor. I don't have an appointment.", [
    ("No problem. We accept walk-in patients. Could you fill in this registration form first?", True, "Trấn an + hướng dẫn bước tiếp theo rõ ràng."),
    ("No appointment, cannot.", False, "Cộc lốc và sai thông tin — nhiều phòng khám vẫn nhận khách không hẹn."),
    ("You wait there.", False, "Mệnh lệnh cộc, thiếu 'please' và chưa đăng ký cho khách."),
  ]),
  ("Is this where I register?", [
    ("Yes, it is. May I have your full name and date of birth, please?", True, "Xác nhận + hỏi thông tin nhận dạng lịch sự."),
    ("Yes. Name?", False, "Hỏi cụt một chữ nghe thiếu lịch sự."),
    ("Yes, you register here, what your name?", False, "Thiếu động từ trong câu hỏi: 'What's your name?'"),
  ]),
  ("How long do I have to wait?", [
    ("About twenty minutes. There are three patients before you.", True, "Thời gian ước tính + lý do cụ thể."),
    ("I don't know, maybe long.", False, "Mơ hồ, làm bệnh nhân lo lắng hơn."),
    ("You must wait until doctor call.", False, "Thiếu mạo từ, chia sai ('the doctor calls') và nghe khó chịu."),
  ]),
  ("I'd like to see a doctor about my skin.", [
    ("Of course. Our skin specialist is available at 2 p.m. Would that be OK?", True, "Gợi ý đúng chuyên khoa + giờ cụ thể + hỏi ý bệnh nhân."),
    ("Skin doctor is busy, come tomorrow.", False, "Thiếu mạo từ, từ chối ngay mà không đưa lựa chọn."),
    ("What wrong with your skin?", False, "Thiếu 'is' và lễ tân không nên hỏi sâu triệu chứng ở quầy đông người."),
  ]),
  ("Sorry, can you say my name again? That's not right.", [
    ("I'm sorry. Could you spell it for me, please? I'll correct it now.", True, "Xin lỗi + nhờ đánh vần để ghi đúng — tránh nhầm hồ sơ."),
    ("It's OK, the name is not important.", False, "Sai nghiêm trọng: tên sai dễ dẫn đến nhầm bệnh nhân."),
    ("Your name very difficult.", False, "Thiếu 'is' và thiếu lịch sự với bệnh nhân."),
  ]),
 ],
 "listen": [
  ("Do you have an appointment today", ["appointment", "today"], "hỏi lịch hẹn"),
  ("Please fill in this registration form", ["fill", "registration"], "điền phiếu đăng ký"),
  ("Your queue number is twenty-five", ["queue", "twenty-five"], "số thứ tự"),
  ("Could you tell me your date of birth", ["tell", "birth"], "hỏi ngày sinh"),
  ("Good morning and welcome to Sen Xanh Clinic. Is this your first visit? May I see your passport, please?", ["welcome", "first", "passport"], "đón bệnh nhân mới"),
  ("The doctor is running a little late today. The waiting time is about thirty minutes. Please take a seat in the waiting room.", ["late", "thirty", "seat"], "báo thời gian chờ"),
 ],
})

# ───────────────────────── 1. Hỏi triệu chứng & bệnh sử ─────────────────────────
PHASES.append({
 "title": "Hỏi triệu chứng & bệnh sử",
 "vocab": [
  ("symptom", "/ˈsɪmptəm/", "n", "triệu chứng", "What <b>symptoms</b> do you have?", "Anh/chị có những triệu chứng gì ạ?", "症状", "shōjō"),
  ("allergy", "/ˈælədʒi/", "n", "dị ứng", "Do you have any <b>allergies</b> to medicine?", "Anh/chị có dị ứng với thuốc nào không ạ?", "アレルギー", "arerugī"),
  ("medical history", "/ˌmedɪkl ˈhɪstri/", "n", "tiền sử bệnh", "The doctor will ask about your <b>medical history</b>.", "Bác sĩ sẽ hỏi về tiền sử bệnh của anh/chị.", "既往歴", "kiōreki"),
  ("pain", "/peɪn/", "n", "cơn đau, sự đau", "On a scale of 0 to 10, how bad is the <b>pain</b>?", "Trên thang từ 0 đến 10, anh/chị đau mức nào ạ?", "痛み", "itami"),
  ("fever", "/ˈfiːvə/", "n", "sốt", "When did the <b>fever</b> start?", "Anh/chị bắt đầu sốt từ khi nào ạ?", "熱", "netsu"),
  ("dizzy", "/ˈdɪzi/", "adj", "chóng mặt", "Do you feel <b>dizzy</b> when you stand up?", "Anh/chị có thấy chóng mặt khi đứng dậy không ạ?"),
  ("cough", "/kɒf/", "n/v", "ho; cơn ho", "How long have you had this <b>cough</b>?", "Anh/chị bị ho bao lâu rồi ạ?", "咳", "seki"),
  ("nausea", "/ˈnɔːziə/", "n", "buồn nôn", "Do you have any <b>nausea</b> or vomiting?", "Anh/chị có buồn nôn hay nôn không ạ?", "吐き気", "hakike"),
  ("sore throat", "/ˌsɔː ˈθrəʊt/", "n", "đau họng", "I've had a <b>sore throat</b> since Monday.", "Tôi bị đau họng từ thứ Hai."),
  ("chronic", "/ˈkrɒnɪk/", "adj", "mạn tính, kéo dài", "Do you have any <b>chronic</b> illnesses, like diabetes?", "Anh/chị có bệnh mạn tính nào không, ví dụ tiểu đường?", "慢性の", "mansei no"),
 ],
 "phrases": [
  ("What brings you in today?", "Hôm nay anh/chị đến khám vì vấn đề gì ạ?"),
  ("When did it start?", "Triệu chứng bắt đầu từ khi nào ạ?"),
  ("Can you show me where it hurts?", "Anh/chị chỉ giúp em chỗ nào đau ạ?"),
  ("On a scale of 0 to 10, how bad is the pain?", "Trên thang từ 0 đến 10, anh/chị đau mức nào ạ?"),
  ("Is the pain getting better or worse?", "Cơn đau đang đỡ hơn hay nặng hơn ạ?"),
  ("Are you allergic to any medicine or food?", "Anh/chị có dị ứng thuốc hay thức ăn nào không ạ?"),
  ("Are you taking any medicine at the moment?", "Hiện tại anh/chị có đang dùng thuốc gì không ạ?"),
  ("Have you had this problem before?", "Trước đây anh/chị đã bị như vậy chưa ạ?"),
  ("Is there any chance you could be pregnant?", "Chị có khả năng đang mang thai không ạ?"),
  ("I'll let the doctor know. She'll ask you more questions.", "Em sẽ báo bác sĩ. Bác sĩ sẽ hỏi thêm anh/chị ạ."),
 ],
 "dialogues": [
  ("I've had a headache for three days.", [
    ("I'm sorry to hear that. Is it getting worse, and do you have any other symptoms?", True, "Đồng cảm + hỏi diễn tiến và triệu chứng kèm theo."),
    ("Three days is not long, don't worry.", False, "Đánh giá thay bác sĩ, coi nhẹ triệu chứng của bệnh nhân."),
    ("Why you have headache?", False, "Sai cấu trúc câu hỏi và hỏi nguyên nhân là việc của bác sĩ."),
  ]),
  ("Do I need to tell you about my allergies?", [
    ("Yes, please. It's very important. What are you allergic to?", True, "Khẳng định tầm quan trọng + hỏi cụ thể."),
    ("No need, the doctor knows.", False, "Sai nguyên tắc an toàn — luôn phải hỏi và ghi lại dị ứng."),
    ("Yes, you allergy what?", False, "Sai từ loại và trật tự: 'What are you allergic to?'"),
  ]),
  ("It hurts here, on the right side.", [
    ("Thank you. When did the pain start, and how bad is it from 0 to 10?", True, "Ghi nhận + hỏi thời điểm và mức độ đau."),
    ("Right side is appendix, I think.", False, "Tự chẩn đoán — không phải vai trò của điều dưỡng/lễ tân."),
    ("It hurt how much?", False, "Trật tự từ kiểu tiếng Việt: 'How much does it hurt?'"),
  ]),
  ("I take medicine for high blood pressure.", [
    ("Thank you. Do you know the name of the medicine? I'll add it to your notes for the doctor.", True, "Hỏi tên thuốc + ghi hồ sơ cho bác sĩ."),
    ("OK, stop it today.", False, "Rất nguy hiểm — chỉ bác sĩ mới quyết định ngừng thuốc."),
    ("What medicine you take?", False, "Thiếu trợ động từ: 'What medicine do you take?'"),
  ]),
  ("I feel dizzy when I stand up.", [
    ("Please sit down and don't stand up on your own. I'll call the doctor and stay with you.", True, "Ưu tiên an toàn (tránh ngã) + gọi bác sĩ + ở cạnh bệnh nhân."),
    ("Maybe you are hungry. Eat something.", False, "Đoán nguyên nhân và khuyên thay bác sĩ."),
    ("You is dizzy since when?", False, "Sai chia ('are') và trật tự câu: 'How long have you felt dizzy?'"),
  ]),
 ],
 "listen": [
  ("What brings you in today", ["brings", "today"], "câu mở đầu hỏi bệnh"),
  ("Are you allergic to any medicine", ["allergic", "medicine"], "hỏi dị ứng"),
  ("When did the fever start", ["fever", "start"], "hỏi thời điểm sốt"),
  ("I've had a sore throat since Monday", ["sore", "Monday"], "bệnh nhân kể triệu chứng"),
  ("I've had a cough for about a week. It's worse at night. I don't have a fever.", ["cough", "night", "fever"], "bệnh nhân kể bệnh"),
  ("Before you see the doctor, I have a few questions. Are you taking any medicine now? And do you have any allergies?", ["questions", "medicine", "allergies"], "hỏi bệnh trước khi vào khám"),
 ],
})

# ───────────────────────── 2. Đo sinh hiệu & chuẩn bị khám ─────────────────────────
PHASES.append({
 "title": "Đo sinh hiệu & chuẩn bị khám",
 "vocab": [
  ("vital signs", "/ˌvaɪtl ˈsaɪnz/", "n", "dấu hiệu sinh tồn, sinh hiệu", "I need to check your <b>vital signs</b> first.", "Em cần đo sinh hiệu cho anh/chị trước ạ.", "バイタルサイン", "baitaru sain"),
  ("blood pressure", "/ˈblʌd ˌpreʃə/", "n", "huyết áp", "Let me take your <b>blood pressure</b>.", "Để em đo huyết áp cho anh/chị.", "血圧", "ketsuatsu"),
  ("temperature", "/ˈtemprətʃə/", "n", "nhiệt độ cơ thể", "Your <b>temperature</b> is normal.", "Nhiệt độ của anh/chị bình thường.", "体温", "taion"),
  ("pulse", "/pʌls/", "n", "mạch", "I'm going to check your <b>pulse</b>.", "Em sẽ bắt mạch cho anh/chị.", "脈拍", "myakuhaku"),
  ("weight", "/weɪt/", "n", "cân nặng", "Could you step on the scale? I need your <b>weight</b>.", "Anh/chị bước lên cân giúp em. Em cần cân nặng của anh/chị.", "体重", "taijū"),
  ("height", "/haɪt/", "n", "chiều cao", "Please stand straight so I can measure your <b>height</b>.", "Anh/chị đứng thẳng để em đo chiều cao ạ.", "身長", "shinchō"),
  ("oxygen level", "/ˈɒksɪdʒən ˌlevl/", "n", "nồng độ oxy (SpO2)", "This clip on your finger checks your <b>oxygen level</b>.", "Cái kẹp ở ngón tay này để đo nồng độ oxy của anh/chị."),
  ("sleeve", "/sliːv/", "n", "tay áo", "Could you roll up your <b>sleeve</b>, please?", "Anh/chị xắn tay áo lên giúp em nhé."),
  ("gown", "/ɡaʊn/", "n", "áo choàng khám bệnh", "Please change into this <b>gown</b>. You can keep your trousers on.", "Anh/chị thay áo choàng này nhé. Anh/chị có thể giữ nguyên quần."),
  ("thermometer", "/θəˈmɒmɪtə/", "n", "nhiệt kế", "I'll put the <b>thermometer</b> under your arm.", "Em sẽ kẹp nhiệt kế vào nách anh/chị.", "体温計", "taionkei"),
 ],
 "phrases": [
  ("Before you see the doctor, I'll check your vital signs.", "Trước khi gặp bác sĩ, em sẽ đo sinh hiệu cho anh/chị."),
  ("Please sit down and relax your arm.", "Anh/chị ngồi xuống và thả lỏng tay ạ."),
  ("You'll feel a little squeeze on your arm.", "Anh/chị sẽ thấy tay hơi bị bóp chặt một chút."),
  ("Please don't talk for a moment.", "Anh/chị vui lòng không nói chuyện trong giây lát."),
  ("Could you step on the scale, please?", "Anh/chị bước lên cân giúp em nhé."),
  ("Please take off your shoes.", "Anh/chị vui lòng cởi giày ạ."),
  ("Your blood pressure is a little high. I'll let the doctor know.", "Huyết áp của anh/chị hơi cao. Em sẽ báo bác sĩ."),
  ("Please change into this gown. It opens at the back.", "Anh/chị thay áo choàng này nhé. Áo mở phía sau."),
  ("I'll close the curtain for your privacy.", "Em sẽ kéo rèm để giữ riêng tư cho anh/chị."),
  ("The doctor will be with you in a few minutes.", "Vài phút nữa bác sĩ sẽ vào khám ạ."),
 ],
 "dialogues": [
  ("What are you going to do?", [
    ("I'm going to check your blood pressure. You'll feel a little squeeze on your arm.", True, "Giải thích trước khi làm + nói cảm giác sẽ có."),
    ("Don't worry, just sit.", False, "Không giải thích thủ thuật — bệnh nhân có quyền được biết."),
    ("I check blood pressure you.", False, "Sai trật tự và thiếu 'will/going to': 'I'm going to check your blood pressure.'"),
  ]),
  ("Is my blood pressure OK?", [
    ("It's a little high today. I'll tell the doctor, and she'll talk to you about it.", True, "Thông tin trung thực + để bác sĩ tư vấn."),
    ("It's high. You have heart disease.", False, "Tự kết luận bệnh — chỉ bác sĩ mới chẩn đoán."),
    ("It high a little bit.", False, "Thiếu 'is' và trật tự: 'It's a little high.'"),
  ]),
  ("Do I have to take off my shirt?", [
    ("Yes, please. You can change into this gown. I'll close the curtain for you.", True, "Hướng dẫn rõ + tôn trọng riêng tư."),
    ("Yes, take off now.", False, "Mệnh lệnh cộc, thiếu tân ngữ 'it' và không quan tâm riêng tư."),
    ("Yes, you must open shirt.", False, "Dịch từng chữ 'mở áo': 'take off your shirt'."),
  ]),
  ("I'm sorry, my hands are shaking. I'm nervous.", [
    ("That's completely OK. Take your time. Let's wait a minute and then try again.", True, "Trấn an + cho bệnh nhân thời gian, đo lại sau."),
    ("Please stop shaking.", False, "Yêu cầu vô lý, làm bệnh nhân căng thẳng hơn."),
    ("Why you nervous?", False, "Thiếu 'are' và nghe như trách bệnh nhân."),
  ]),
  ("How much do I weigh?", [
    ("You're 62 kilos. I'll write it in your notes.", True, "Trả lời số liệu + ghi hồ sơ."),
    ("You are 62 kilos, a bit fat.", False, "Nhận xét ngoại hình — thiếu tôn trọng."),
    ("Weight you is 62.", False, "Sai sở hữu cách: 'Your weight is 62 kilos.'"),
  ]),
 ],
 "listen": [
  ("I need to check your vital signs", ["check", "vital"], "chuẩn bị đo sinh hiệu"),
  ("Please roll up your sleeve", ["roll", "sleeve"], "đo huyết áp"),
  ("Your temperature is normal", ["temperature", "normal"], "báo nhiệt độ"),
  ("Could you step on the scale, please", ["step", "scale"], "đo cân nặng"),
  ("I'm going to check your blood pressure now. You'll feel a little squeeze. Please try not to talk.", ["blood", "squeeze", "talk"], "hướng dẫn đo huyết áp"),
  ("Please change into this gown. It opens at the back. I'll close the curtain for your privacy.", ["gown", "back", "curtain"], "chuẩn bị trước khi khám"),
 ],
})

# ───────────────────────── 3. Giải thích thủ tục & xét nghiệm ─────────────────────────
PHASES.append({
 "title": "Giải thích thủ tục & xét nghiệm",
 "vocab": [
  ("blood test", "/ˈblʌd test/", "n", "xét nghiệm máu", "The doctor has ordered a <b>blood test</b>.", "Bác sĩ đã chỉ định xét nghiệm máu.", "血液検査", "ketsueki kensa"),
  ("X-ray", "/ˈeks reɪ/", "n", "chụp X-quang", "The <b>X-ray</b> room is on the second floor.", "Phòng chụp X-quang ở tầng hai.", "レントゲン", "rentogen"),
  ("ultrasound", "/ˈʌltrəsaʊnd/", "n", "siêu âm", "The <b>ultrasound</b> takes about fifteen minutes.", "Siêu âm mất khoảng mười lăm phút.", "超音波検査", "chōonpa kensa"),
  ("fasting", "/ˈfɑːstɪŋ/", "n/adj", "nhịn ăn (trước xét nghiệm)", "This is a <b>fasting</b> blood test. Please don't eat after 10 p.m.", "Đây là xét nghiệm máu cần nhịn ăn. Anh/chị vui lòng không ăn sau 10 giờ tối."),
  ("sample", "/ˈsɑːmpl/", "n", "mẫu (máu, nước tiểu…)", "Please bring the urine <b>sample</b> to the lab.", "Anh/chị mang mẫu nước tiểu đến phòng xét nghiệm ạ.", "検体", "kentai"),
  ("procedure", "/prəˈsiːdʒə/", "n", "thủ thuật, quy trình", "The doctor will explain the <b>procedure</b> to you.", "Bác sĩ sẽ giải thích thủ thuật cho anh/chị."),
  ("consent form", "/kənˈsent fɔːm/", "n", "giấy cam đoan đồng ý thực hiện thủ thuật", "Please read and sign the <b>consent form</b>.", "Anh/chị vui lòng đọc và ký giấy cam kết đồng ý.", "同意書", "dōisho"),
  ("lab", "/læb/", "n", "phòng xét nghiệm", "The <b>lab</b> is open from 7 a.m.", "Phòng xét nghiệm mở cửa từ 7 giờ sáng.", "検査室", "kensashitsu"),
  ("scan", "/skæn/", "n/v", "chụp chiếu (CT, MRI); chụp", "You'll have a <b>scan</b> of your knee this afternoon.", "Chiều nay anh/chị sẽ được chụp đầu gối."),
  ("referral", "/rɪˈfɜːrəl/", "n", "giấy chuyển khám / chuyển tuyến", "You need a <b>referral</b> to see the heart specialist.", "Anh/chị cần giấy chuyển để khám bác sĩ tim mạch.", "紹介状", "shōkaijō"),
 ],
 "phrases": [
  ("The doctor would like you to have a blood test.", "Bác sĩ muốn anh/chị làm xét nghiệm máu."),
  ("Please don't eat or drink anything except water after 10 p.m.", "Sau 10 giờ tối anh/chị vui lòng không ăn uống gì ngoài nước lọc."),
  ("It will only take a few minutes.", "Chỉ mất vài phút thôi ạ."),
  ("You'll feel a small sharp scratch.", "Anh/chị sẽ thấy nhói nhẹ một chút."),
  ("The results will be ready in about two hours.", "Khoảng hai tiếng nữa sẽ có kết quả ạ."),
  ("The doctor will go through the results with you.", "Bác sĩ sẽ giải thích kết quả cho anh/chị."),
  ("Please follow the blue line to the X-ray room.", "Anh/chị đi theo vạch xanh đến phòng chụp X-quang ạ."),
  ("Before we start, please read and sign this consent form.", "Trước khi bắt đầu, anh/chị vui lòng đọc và ký giấy cam kết này."),
  ("Do you have any questions before we begin?", "Anh/chị có câu hỏi gì trước khi bắt đầu không ạ?"),
 ],
 "dialogues": [
  ("Will the blood test hurt?", [
    ("You'll feel a small scratch, but it's very quick. Tell me if you feel unwell.", True, "Nói thật nhẹ nhàng + mời bệnh nhân báo khi khó chịu."),
    ("No, not hurt at all.", False, "Hứa không đau là không trung thực; lại thiếu động từ."),
    ("Everybody afraid needle, don't worry.", False, "Thiếu 'is'/'of' và câu trấn an vụng về."),
  ]),
  ("Can I have breakfast before the test?", [
    ("I'm afraid not. This test needs fasting. You can drink water, and eat right after the test.", True, "Từ chối rõ + lý do + điều được phép làm."),
    ("Yes, eat a little is OK.", False, "Sai hướng dẫn — có thể làm sai kết quả xét nghiệm."),
    ("No eat, no drink, nothing.", False, "Cộc lốc và sai: thường vẫn được uống nước lọc — nên nói rõ."),
  ]),
  ("When will I get my results?", [
    ("In about two hours. The doctor will go through them with you.", True, "Thời gian cụ thể + ai sẽ giải thích kết quả."),
    ("Tomorrow maybe, I'm not sure.", False, "Mơ hồ — nên kiểm tra rồi trả lời."),
    ("Your results is bad, I think.", False, "Sai chia ('are') và tuyệt đối không tự nhận định kết quả."),
  ]),
  ("Do I have to sign this?", [
    ("Yes, it's a consent form. It says you agree to the procedure. Please ask me if anything isn't clear.", True, "Nói rõ ý nghĩa giấy tờ + mời hỏi lại."),
    ("Just sign, it's normal paper.", False, "Không giải thích giấy cam kết là sai quy trình và thiếu tôn trọng."),
    ("Yes, sign here quick.", False, "Hối thúc, thiếu 'please'."),
  ]),
  ("Where do I go for the X-ray?", [
    ("It's on the second floor. Take the lift and turn left. I'll walk with you if you like.", True, "Chỉ đường rõ + đề nghị đưa đi."),
    ("Second floor, go.", False, "Cộc lốc, thiếu chỉ dẫn."),
    ("You go up floor two.", False, "Sai cách nói tầng: 'It's on the second floor.'"),
  ]),
 ],
 "listen": [
  ("The doctor has ordered a blood test", ["ordered", "blood"], "chỉ định xét nghiệm"),
  ("Please don't eat after ten o'clock", ["eat", "ten"], "hướng dẫn nhịn ăn"),
  ("The results will be ready in two hours", ["results", "hours"], "thời gian có kết quả"),
  ("Please sign the consent form here", ["sign", "consent"], "ký giấy cam kết"),
  ("Tomorrow you'll have an ultrasound at eight. Please don't eat after midnight. You can drink a little water.", ["ultrasound", "midnight", "water"], "dặn trước siêu âm"),
  ("The X-ray room is on the second floor. Take the lift and turn left. Please show this paper at the desk.", ["second", "lift", "paper"], "chỉ đường đi chụp X-quang"),
 ],
})

# ───────────────────────── 4. Thuốc & hướng dẫn dùng thuốc ─────────────────────────
PHASES.append({
 "title": "Thuốc & hướng dẫn dùng thuốc",
 "vocab": [
  ("prescription", "/prɪˈskrɪpʃn/", "n", "đơn thuốc", "Please take this <b>prescription</b> to the pharmacy.", "Anh/chị mang đơn thuốc này đến nhà thuốc ạ.", "処方箋", "shohōsen"),
  ("dosage", "/ˈdəʊsɪdʒ/", "n", "liều dùng", "The doctor will decide the <b>dosage</b>.", "Bác sĩ sẽ quyết định liều dùng.", "用量", "yōryō"),
  ("side effect", "/ˈsaɪd ɪˌfekt/", "n", "tác dụng phụ", "Tell us if you notice any <b>side effects</b>.", "Anh/chị báo bên em nếu thấy tác dụng phụ nào nhé.", "副作用", "fukusayō"),
  ("tablet", "/ˈtæblət/", "n", "viên thuốc (viên nén)", "Take the <b>tablets</b> as written on the label.", "Uống thuốc theo đúng hướng dẫn trên nhãn.", "錠剤", "jōzai"),
  ("pharmacist", "/ˈfɑːməsɪst/", "n", "dược sĩ", "The <b>pharmacist</b> will explain how to take it.", "Dược sĩ sẽ hướng dẫn cách dùng.", "薬剤師", "yakuzaishi"),
  ("empty stomach", "/ˌempti ˈstʌmək/", "n", "bụng đói", "Take this one on an <b>empty stomach</b>, as the label says.", "Thuốc này uống lúc bụng đói, theo hướng dẫn trên nhãn.", "空腹時", "kūfukuji"),
  ("ointment", "/ˈɔɪntmənt/", "n", "thuốc mỡ, thuốc bôi", "Put a thin layer of <b>ointment</b> on the area.", "Bôi một lớp thuốc mỏng lên vùng da đó."),
  ("over-the-counter", "/ˌəʊvə ðə ˈkaʊntə/", "adj", "(thuốc) không kê đơn", "This is an <b>over-the-counter</b> medicine, but please ask the pharmacist before you take it.", "Đây là thuốc không kê đơn, nhưng anh/chị nên hỏi dược sĩ trước khi dùng."),
  ("antibiotic", "/ˌæntibaɪˈɒtɪk/", "n", "thuốc kháng sinh", "We can't sell <b>antibiotics</b> without a prescription.", "Bên em không bán kháng sinh khi không có đơn.", "抗生物質", "kōsei busshitsu"),
  ("label", "/ˈleɪbl/", "n", "nhãn thuốc", "Please read the <b>label</b> before you take it.", "Anh/chị vui lòng đọc nhãn trước khi dùng."),
 ],
 "phrases": [
  ("Do you have a prescription from your doctor?", "Anh/chị có đơn thuốc của bác sĩ không ạ?"),
  ("Are you allergic to any medicine?", "Anh/chị có dị ứng với thuốc nào không ạ?"),
  ("Please take it exactly as the doctor prescribed.", "Anh/chị dùng đúng theo đơn bác sĩ kê nhé."),
  ("The instructions are on the label.", "Hướng dẫn có ghi trên nhãn ạ."),
  ("The label says to take this one after meals.", "Trên nhãn ghi thuốc này uống sau bữa ăn."),
  ("Please finish the whole course unless the doctor tells you to stop.", "Anh/chị dùng hết đợt thuốc, trừ khi bác sĩ bảo ngừng."),
  ("If you notice any side effects, please call us.", "Nếu thấy tác dụng phụ, anh/chị gọi cho bên em nhé."),
  ("I'm not able to change the dose. Please ask your doctor.", "Em không thể thay đổi liều. Anh/chị vui lòng hỏi bác sĩ."),
  ("Are you taking any other medicine at the moment?", "Hiện anh/chị có đang dùng thuốc nào khác không ạ?"),
  ("Keep it in a cool, dry place.", "Bảo quản ở nơi khô ráo, thoáng mát."),
 ],
 "dialogues": [
  ("Can I have some antibiotics for my cold?", [
    ("I'm sorry, we can't sell antibiotics without a prescription. I'd suggest you see a doctor.", True, "Tuân thủ quy định + hướng bệnh nhân đi khám."),
    ("Sure, antibiotics is good for cold.", False, "Sai quy định bán thuốc và sai chia ('are')."),
    ("No prescription, no medicine, bye.", False, "Cộc lốc, không hướng dẫn thêm."),
  ]),
  ("How many should I take?", [
    ("Please take them exactly as it says on the label. The doctor decided the dose for you.", True, "Chỉ vào đơn/nhãn, không tự đưa liều."),
    ("Take many is better, you get well fast.", False, "Nguy hiểm — không bao giờ khuyên dùng quá liều."),
    ("You take how many you want.", False, "Sai trật tự và hướng dẫn sai nguyên tắc an toàn."),
  ]),
  ("I feel better. Can I stop taking the medicine?", [
    ("Please check with your doctor first. Some medicines need to be finished even if you feel better.", True, "Không tự quyết + chuyển bác sĩ + giải thích ngắn."),
    ("Yes, if you feel better, stop.", False, "Khuyên ngừng thuốc khi chưa hỏi bác sĩ là không an toàn."),
    ("You must to finish all.", False, "Sai: 'must' không đi với 'to'; nên hướng bệnh nhân hỏi bác sĩ."),
  ]),
  ("This medicine makes me feel sick.", [
    ("Thank you for telling me. I'll let the doctor know right away and ask her about your next dose.", True, "Ghi nhận + báo bác sĩ ngay + để bác sĩ quyết định liều tiếp theo."),
    ("It's normal, just continue.", False, "Tự đánh giá tác dụng phụ thay bác sĩ."),
    ("Medicine make everybody sick.", False, "Sai chia ('makes') và không xử lý phản hồi của bệnh nhân."),
  ]),
  ("Can I take this with my other medicine?", [
    ("Let me check with the pharmacist. What other medicine are you taking?", True, "Hỏi tên thuốc đang dùng + kiểm tra với dược sĩ."),
    ("No problem, all medicine is safe.", False, "Khẳng định sai — tương tác thuốc cần được kiểm tra."),
    ("I think can.", False, "Thiếu chủ ngữ và đoán mò: 'Let me check for you.'"),
  ]),
 ],
 "listen": [
  ("Please take this prescription to the pharmacy", ["prescription", "pharmacy"], "hướng dẫn lấy thuốc"),
  ("The doctor will decide the dosage", ["doctor", "dosage"], "ai quyết định liều"),
  ("Tell us if you notice any side effects", ["notice", "side"], "báo tác dụng phụ"),
  ("Please read the label before you take it", ["read", "label"], "đọc nhãn thuốc"),
  ("Here is your medicine. Please take it exactly as it says on the label. If you have any side effects, call the clinic.", ["medicine", "label", "clinic"], "phát thuốc tại quầy"),
  ("I'm sorry, we can't sell this without a prescription. There's a clinic next door. The doctor can see you today.", ["sell", "prescription", "next"], "từ chối bán thuốc kê đơn"),
 ],
})

# ───────────────────────── 5. Chăm sóc người bệnh nội trú ─────────────────────────
PHASES.append({
 "title": "Chăm sóc người bệnh nội trú",
 "vocab": [
  ("ward", "/wɔːd/", "n", "khoa, buồng bệnh", "Your room is in the surgical <b>ward</b> on the fourth floor.", "Phòng của anh/chị ở khoa ngoại, tầng bốn.", "病棟", "byōtō"),
  ("admission", "/ədˈmɪʃn/", "n", "sự nhập viện", "Your <b>admission</b> papers are ready.", "Giấy tờ nhập viện của anh/chị đã xong.", "入院", "nyūin"),
  ("discharge", "/dɪsˈtʃɑːdʒ/", "n/v", "sự xuất viện; cho xuất viện", "The doctor may <b>discharge</b> you tomorrow.", "Ngày mai bác sĩ có thể cho anh/chị xuất viện.", "退院", "taiin"),
  ("IV drip", "/ˌaɪ ˈviː drɪp/", "n", "dịch truyền, truyền dịch", "Please tell me if the <b>IV drip</b> stops.", "Anh/chị báo em nếu dịch truyền ngừng chảy nhé.", "点滴", "tenteki"),
  ("call button", "/ˈkɔːl ˌbʌtn/", "n", "nút gọi điều dưỡng", "Press the <b>call button</b> if you need help.", "Anh/chị bấm nút gọi nếu cần giúp đỡ.", "ナースコール", "nāsu kōru"),
  ("fall risk", "/ˈfɔːl rɪsk/", "n", "nguy cơ té ngã", "Mr Brown is a <b>fall risk</b>, so keep the bed rails up.", "Ông Brown có nguy cơ té ngã, nên luôn kéo thanh chắn giường lên."),
  ("visiting hours", "/ˈvɪzɪtɪŋ ˌaʊəz/", "n", "giờ thăm bệnh", "<b>Visiting hours</b> are from 3 to 8 p.m.", "Giờ thăm bệnh từ 3 đến 8 giờ tối.", "面会時間", "menkai jikan"),
  ("wound", "/wuːnd/", "n", "vết thương", "I'm going to check your <b>wound</b> now.", "Bây giờ em sẽ kiểm tra vết thương cho anh/chị."),
  ("dressing", "/ˈdresɪŋ/", "n", "băng gạc (che vết thương)", "We'll change the <b>dressing</b> every morning.", "Mỗi sáng bên em sẽ thay băng."),
  ("bed rest", "/ˌbed ˈrest/", "n", "nằm nghỉ tại giường", "The doctor wants you on <b>bed rest</b> today.", "Hôm nay bác sĩ muốn anh/chị nằm nghỉ tại giường.", "ベッド上安静", "beddojō ansei"),
 ],
 "phrases": [
  ("Good morning. I'm Hoa, your nurse today.", "Chào buổi sáng. Em là Hoa, điều dưỡng phụ trách anh/chị hôm nay."),
  ("Can you tell me your name and date of birth?", "Anh/chị cho em biết họ tên và ngày sinh ạ."),
  ("I'm just going to check your name band.", "Em kiểm tra vòng tay tên của anh/chị một chút nhé."),
  ("How are you feeling this morning?", "Sáng nay anh/chị thấy trong người thế nào ạ?"),
  ("Did you sleep well last night?", "Tối qua anh/chị ngủ có ngon không ạ?"),
  ("Please press the call button if you need to get up.", "Nếu cần đứng dậy, anh/chị bấm nút gọi nhé."),
  ("I'm going to change your dressing now. Is that OK?", "Bây giờ em sẽ thay băng cho anh/chị. Được không ạ?"),
  ("Let me help you sit up.", "Để em đỡ anh/chị ngồi dậy."),
  ("Your family can visit from 3 to 8 p.m.", "Người nhà có thể vào thăm từ 3 đến 8 giờ tối."),
  ("I'll be back in an hour to check on you.", "Một tiếng nữa em sẽ quay lại xem anh/chị thế nào."),
 ],
 "dialogues": [
  ("Nurse, I need to go to the toilet.", [
    ("Of course. Please wait a moment. I'll help you so you don't fall.", True, "Đáp ứng + đi cùng để phòng té ngã."),
    ("Go by yourself, it's near.", False, "Bỏ qua nguy cơ té ngã của người bệnh nội trú."),
    ("Wait, I busy.", False, "Thiếu 'am' và thiếu quan tâm; nếu bận, nói khi nào sẽ quay lại."),
  ]),
  ("Can my family stay tonight?", [
    ("One family member can stay overnight. Visiting hours for others are from 3 to 8 p.m.", True, "Trả lời theo quy định, rõ ràng."),
    ("No, family is not allow.", False, "Sai bị động ('allowed') và từ chối mà không nêu quy định."),
    ("Family stay OK, many people OK.", False, "Sai thông tin và không đúng quy định bệnh viện."),
  ]),
  ("My drip isn't working. Nothing is coming out.", [
    ("Thank you for telling me. Let me check it now. Please keep your arm still.", True, "Cảm ơn + kiểm tra ngay + hướng dẫn bệnh nhân."),
    ("It's OK, it will work again.", False, "Không kiểm tra — có thể bỏ sót vấn đề."),
    ("Don't touch, you make broken.", False, "Đổ lỗi cho bệnh nhân và sai ngữ pháp."),
  ]),
  ("When can I go home?", [
    ("The doctor will decide on the ward round tomorrow morning. I'll let you know as soon as I hear.", True, "Không tự hứa + nói khi nào bác sĩ quyết định."),
    ("Tomorrow, sure.", False, "Hứa thay bác sĩ khi chưa có quyết định."),
    ("I don't know, ask doctor.", False, "Cộc lốc, thiếu mạo từ 'the doctor'."),
  ]),
  ("I'm in a lot of pain.", [
    ("I'm sorry. On a scale of 0 to 10, how bad is it? I'll tell the doctor straight away.", True, "Đồng cảm + đánh giá mức đau + báo bác sĩ ngay."),
    ("I'll give you more painkillers now.", False, "Tự ý tăng thuốc giảm đau khi chưa có y lệnh."),
    ("Everybody pain after surgery.", False, "Thiếu động từ ('has pain') và coi nhẹ cơn đau."),
  ]),
 ],
 "listen": [
  ("Press the call button if you need help", ["call", "help"], "hướng dẫn nút gọi"),
  ("Visiting hours are from three to eight", ["Visiting", "eight"], "giờ thăm bệnh"),
  ("I'm going to change your dressing now", ["change", "dressing"], "thay băng"),
  ("The doctor may discharge you tomorrow", ["discharge", "tomorrow"], "dự kiến xuất viện"),
  ("Good morning. I'm your nurse today. Can you tell me your full name and date of birth?", ["nurse", "name", "birth"], "chào bệnh nhân đầu ca"),
  ("Mr Brown is a fall risk. Please keep the bed rails up. Help him when he goes to the toilet.", ["fall", "rails", "toilet"], "dặn dò phòng té ngã"),
 ],
})

# ───────────────────────── 6. Trấn an & giao tiếp đồng cảm ─────────────────────────
PHASES.append({
 "title": "Trấn an & giao tiếp đồng cảm",
 "vocab": [
  ("reassure", "/ˌriːəˈʃʊə/", "v", "trấn an, làm yên lòng", "The nurse <b>reassured</b> her before the scan.", "Điều dưỡng trấn an chị ấy trước khi chụp."),
  ("anxious", "/ˈæŋkʃəs/", "adj", "lo lắng, bồn chồn", "It's normal to feel <b>anxious</b> before surgery.", "Cảm thấy lo lắng trước phẫu thuật là bình thường.", "不安な", "fuan na"),
  ("comfortable", "/ˈkʌmftəbl/", "adj", "thoải mái, dễ chịu", "Are you <b>comfortable</b>? Would you like another pillow?", "Anh/chị nằm có thoải mái không? Có cần thêm gối không ạ?"),
  ("privacy", "/ˈprɪvəsi/", "n", "sự riêng tư", "We respect your <b>privacy</b>.", "Bên em tôn trọng sự riêng tư của anh/chị.", "プライバシー", "puraibashī"),
  ("empathy", "/ˈempəθi/", "n", "sự đồng cảm", "Good nurses show <b>empathy</b> in every conversation.", "Điều dưỡng giỏi luôn thể hiện sự đồng cảm khi nói chuyện."),
  ("calm", "/kɑːm/", "adj/v", "bình tĩnh; làm dịu", "Try to stay <b>calm</b>. We're here with you.", "Anh/chị cố gắng bình tĩnh. Có bên em ở đây rồi."),
  ("interpreter", "/ɪnˈtɜːprɪtə/", "n", "người phiên dịch", "Would you like an <b>interpreter</b> for the consultation?", "Anh/chị có muốn có phiên dịch khi khám không ạ?", "通訳", "tsūyaku"),
  ("relative", "/ˈrelətɪv/", "n", "người thân, người nhà", "Only two <b>relatives</b> can visit at a time.", "Mỗi lần chỉ hai người thân được vào thăm."),
  ("deep breath", "/ˌdiːp ˈbreθ/", "n", "hít thở sâu", "Take a <b>deep breath</b> and relax your shoulders.", "Anh/chị hít thở sâu và thả lỏng vai nhé.", "深呼吸", "shinkokyū"),
  ("concern", "/kənˈsɜːn/", "n", "điều lo lắng, băn khoăn", "Do you have any <b>concerns</b> about tomorrow?", "Anh/chị có lo lắng gì về ngày mai không ạ?"),
 ],
 "phrases": [
  ("I understand this is difficult for you.", "Em hiểu đây là chuyện khó khăn với anh/chị."),
  ("It's completely normal to feel this way.", "Cảm thấy như vậy là hoàn toàn bình thường ạ."),
  ("Take your time. There's no rush.", "Anh/chị cứ từ từ. Không vội đâu ạ."),
  ("Is there anything that worries you?", "Có điều gì làm anh/chị lo lắng không ạ?"),
  ("Let's take a deep breath together.", "Mình cùng hít thở sâu nhé."),
  ("You're doing really well.", "Anh/chị đang làm rất tốt ạ."),
  ("I'll stay with you until the doctor comes.", "Em sẽ ở bên anh/chị cho đến khi bác sĩ tới."),
  ("I don't know the answer, but I'll find out for you.", "Em chưa biết câu trả lời, nhưng em sẽ hỏi lại cho anh/chị."),
  ("Would you like me to call a relative for you?", "Anh/chị có muốn em gọi người nhà giúp không ạ?"),
 ],
 "dialogues": [
  ("I'm really scared about the surgery tomorrow.", [
    ("That's completely understandable. What worries you most? I can ask the doctor to talk to you again.", True, "Công nhận cảm xúc + hỏi mối lo cụ thể + đề nghị hỗ trợ."),
    ("Don't be scared, it's easy.", False, "Gạt bỏ cảm xúc bệnh nhân và hứa hẹn không chắc chắn."),
    ("Why you scared? Doctor very good.", False, "Thiếu 'are', 'is'; không lắng nghe nỗi lo của bệnh nhân."),
  ]),
  ("I don't understand what the doctor said.", [
    ("I'm sorry about that. Would you like an interpreter, or shall I ask the doctor to explain again more slowly?", True, "Xin lỗi + hai phương án giúp bệnh nhân hiểu."),
    ("It's not important, just follow.", False, "Coi nhẹ quyền được hiểu thông tin của bệnh nhân."),
    ("Doctor speak English very good.", False, "Sai chia ('speaks'), sai từ loại ('well') và không giúp gì."),
  ]),
  ("Is my father going to be OK?", [
    ("I know this is hard. The doctor is with him now, and she'll talk to you as soon as she can.", True, "Đồng cảm, trung thực, không hứa trước kết quả."),
    ("Yes, 100% OK.", False, "Hứa chắc chắn khi chưa biết — không trung thực."),
    ("I cannot say, it's secret.", False, "Lạnh lùng; nên hướng người nhà đến bác sĩ."),
  ]),
  ("I've been waiting for two hours! Nobody tells me anything!", [
    ("I'm really sorry for the long wait. Let me check where you are in the queue and come back in five minutes.", True, "Xin lỗi + hành động cụ thể + hẹn thời gian quay lại."),
    ("Everybody is waiting, not only you.", False, "Phản bác, làm bệnh nhân bực hơn."),
    ("Calm down! Calm down!", False, "Ra lệnh 'bình tĩnh' thường khiến người đang bực càng bực."),
  ]),
  ("Can you close the curtain, please?", [
    ("Of course. Tell me if you need anything else.", True, "Đáp ứng ngay + sẵn sàng hỗ trợ."),
    ("Why? Nobody look.", False, "Thiếu 's' ('looks') và không tôn trọng riêng tư."),
    ("OK, I close for you.", False, "Thiếu 'will' và tân ngữ: 'I'll close it for you.'"),
  ]),
 ],
 "listen": [
  ("It's completely normal to feel anxious", ["normal", "anxious"], "trấn an bệnh nhân"),
  ("Take a deep breath and relax", ["deep", "relax"], "hướng dẫn thở"),
  ("Would you like an interpreter", ["like", "interpreter"], "đề nghị phiên dịch"),
  ("I'll stay with you until the doctor comes", ["stay", "doctor"], "ở cạnh bệnh nhân"),
  ("I understand you're worried. That's completely normal. Is there anything you'd like to ask the doctor?", ["worried", "normal", "ask"], "lắng nghe mối lo"),
  ("I'm sorry you've waited so long. Let me check with the doctor. I'll come back in five minutes.", ["waited", "check", "five"], "xin lỗi vì chờ lâu"),
 ],
})

# ───────────────────────── 7. Cấp cứu & tình huống khẩn ─────────────────────────
PHASES.append({
 "title": "Cấp cứu & tình huống khẩn",
 "vocab": [
  ("emergency", "/ɪˈmɜːdʒənsi/", "n", "tình huống khẩn cấp, cấp cứu", "In an <b>emergency</b>, call 115.", "Khi khẩn cấp, hãy gọi 115.", "救急", "kyūkyū"),
  ("ambulance", "/ˈæmbjələns/", "n", "xe cứu thương", "The <b>ambulance</b> is on its way.", "Xe cứu thương đang tới.", "救急車", "kyūkyūsha"),
  ("conscious", "/ˈkɒnʃəs/", "adj", "tỉnh táo, còn ý thức", "Is he <b>conscious</b>? Can he answer you?", "Anh ấy còn tỉnh không? Có trả lời được không?"),
  ("breathing", "/ˈbriːðɪŋ/", "n", "hơi thở, sự hô hấp", "Check her <b>breathing</b> and call the doctor.", "Kiểm tra hơi thở của chị ấy và gọi bác sĩ.", "呼吸", "kokyū"),
  ("chest pain", "/ˌtʃest ˈpeɪn/", "n", "đau ngực", "A patient with <b>chest pain</b> must be seen first.", "Bệnh nhân đau ngực phải được khám trước.", "胸痛", "kyōtsū"),
  ("triage", "/ˈtriːɑːʒ/", "n", "phân loại cấp cứu (ưu tiên theo mức độ nặng)", "The <b>triage</b> nurse decides who is seen first.", "Điều dưỡng phân loại sẽ quyết định ai được khám trước.", "トリアージ", "toriāji"),
  ("first aid", "/ˌfɜːst ˈeɪd/", "n", "sơ cứu", "All staff must know basic <b>first aid</b>.", "Mọi nhân viên đều phải biết sơ cứu cơ bản.", "応急処置", "ōkyū shochi"),
  ("bleeding", "/ˈbliːdɪŋ/", "n", "sự chảy máu", "Press here to stop the <b>bleeding</b>.", "Ấn vào đây để cầm máu.", "出血", "shukketsu"),
  ("faint", "/feɪnt/", "v", "ngất, xỉu", "A visitor <b>fainted</b> in the waiting room.", "Một người đến thăm bị ngất ở phòng chờ."),
  ("stretcher", "/ˈstretʃə/", "n", "cáng", "Bring a <b>stretcher</b> to the entrance, please.", "Mang cáng ra cửa chính giúp em.", "担架", "tanka"),
 ],
 "phrases": [
  ("I need help here, please!", "Ở đây cần giúp đỡ!"),
  ("Please call the doctor now.", "Gọi bác sĩ ngay giúp em."),
  ("Can you hear me? What's your name?", "Anh/chị có nghe em nói không? Anh/chị tên gì ạ?"),
  ("Stay with me. Help is coming.", "Anh/chị cố lên. Người hỗ trợ đang tới rồi."),
  ("Don't move. Stay where you are.", "Đừng cử động. Anh/chị cứ ở nguyên chỗ đó."),
  ("Please step back and give us some space.", "Mọi người lùi lại, cho bên em chút không gian nhé."),
  ("The ambulance will be here in ten minutes.", "Mười phút nữa xe cứu thương sẽ đến."),
  ("Does he have any allergies or medical conditions?", "Anh ấy có dị ứng hay bệnh lý gì không ạ?"),
  ("Please wait here. The doctor will come out to talk to you.", "Anh/chị vui lòng chờ ở đây. Bác sĩ sẽ ra nói chuyện với anh/chị."),
 ],
 "dialogues": [
  ("Help! My husband has chest pain!", [
    ("I'm calling the doctor now. Please help him sit down and stay with him.", True, "Hành động ngay + hướng dẫn người nhà việc đơn giản, an toàn."),
    ("Please take a number and wait.", False, "Sai nguy hiểm — đau ngực phải được ưu tiên ngay."),
    ("Maybe he is tired only.", False, "Tự đánh giá thấp triệu chứng khẩn cấp."),
  ]),
  ("A man just fainted in the waiting room!", [
    ("Call for help and bring a stretcher. I'll check if he's breathing.", True, "Phân việc rõ ràng + kiểm tra hô hấp."),
    ("Give him some water, he will OK.", False, "Không cho người bất tỉnh uống gì; lại thiếu 'be'."),
    ("Who fainted? Why he fainted?", False, "Hỏi lan man thay vì hành động; sai cấu trúc câu hỏi."),
  ]),
  ("Why is that patient going in first? I came earlier!", [
    ("I understand. We see the most serious cases first. I'm sorry for the wait, and I'll update you soon.", True, "Giải thích nguyên tắc phân loại + xin lỗi + hứa cập nhật."),
    ("He is more sick than you.", False, "Tiết lộ thông tin bệnh nhân khác, lại sai so sánh ('sicker')."),
    ("Rule is rule.", False, "Cộc lốc, không giải thích."),
  ]),
  ("Is he going to be OK?", [
    ("The team is doing everything they can. The doctor will talk to you as soon as possible.", True, "Trung thực, không hứa trước, chỉ đúng người sẽ thông báo."),
    ("Yes, don't worry, he is OK.", False, "Hứa khi chưa biết — sai nguyên tắc."),
    ("I don't know, not my patient.", False, "Lạnh lùng, đẩy trách nhiệm."),
  ]),
  ("Should I drive my mother to the hospital?", [
    ("No, please don't move her. I'm calling an ambulance now.", True, "Hướng dẫn an toàn + hành động ngay."),
    ("Yes, drive fast.", False, "Có thể nguy hiểm cho người bệnh và người lái xe."),
    ("You can bring her by motorbike.", False, "Rất không an toàn cho người bệnh nặng."),
  ]),
 ],
 "listen": [
  ("Please call the doctor now", ["call", "doctor"], "gọi bác sĩ"),
  ("The ambulance is on its way", ["ambulance", "way"], "báo xe cứu thương"),
  ("Can you hear me, sir", ["hear", "sir"], "kiểm tra tỉnh táo"),
  ("Please step back and give us some space", ["step", "space"], "giải tán đám đông"),
  ("A patient has chest pain in room five. Please call the doctor now. I'll bring the emergency trolley.", ["chest", "doctor", "trolley"], "báo động khẩn trong khoa"),
  ("A woman fainted in the waiting room. She's conscious now and she's breathing normally. We need a stretcher, please.", ["fainted", "conscious", "stretcher"], "báo tình huống ngất"),
 ],
})

# ───────────────────────── 8. Bảo hiểm, viện phí & giấy tờ ─────────────────────────
PHASES.append({
 "title": "Bảo hiểm, viện phí & giấy tờ",
 "vocab": [
  ("health insurance", "/ˈhelθ ɪnˌʃʊərəns/", "n", "bảo hiểm y tế / bảo hiểm sức khỏe", "Do you have <b>health insurance</b>?", "Anh/chị có bảo hiểm sức khỏe không ạ?", "健康保険", "kenkō hoken"),
  ("insurance card", "/ɪnˈʃʊərəns kɑːd/", "n", "thẻ bảo hiểm", "May I see your <b>insurance card</b>, please?", "Cho em xem thẻ bảo hiểm của anh/chị được không ạ?", "保険証", "hokenshō"),
  ("medical fees", "/ˌmedɪkl ˈfiːz/", "n", "chi phí khám chữa bệnh, viện phí", "The <b>medical fees</b> are listed on this sheet.", "Chi phí khám chữa bệnh được liệt kê ở tờ này.", "医療費", "iryōhi"),
  ("receipt", "/rɪˈsiːt/", "n", "biên lai, hóa đơn thanh toán", "Here's your <b>receipt</b> for the insurance claim.", "Đây là biên lai để anh/chị làm hồ sơ bảo hiểm.", "領収書", "ryōshūsho"),
  ("claim", "/kleɪm/", "n/v", "hồ sơ yêu cầu bồi thường; yêu cầu bồi thường", "You can <b>claim</b> the cost from your insurance company.", "Anh/chị có thể yêu cầu công ty bảo hiểm chi trả khoản này."),
  ("medical certificate", "/ˌmedɪkl səˈtɪfɪkət/", "n", "giấy xác nhận của bác sĩ (giấy nghỉ ốm, chứng nhận tình trạng bệnh)", "Your employer needs a <b>medical certificate</b>.", "Công ty của anh/chị cần giấy xác nhận của bác sĩ.", "診断書", "shindansho"),
  ("deposit", "/dɪˈpɒzɪt/", "n", "tiền tạm ứng, đặt cọc", "We need a <b>deposit</b> of five million dong for admission.", "Nhập viện cần tạm ứng năm triệu đồng."),
  ("co-payment", "/ˌkəʊˈpeɪmənt/", "n", "phần đồng chi trả (người bệnh tự trả)", "Your insurance covers 80%, and the <b>co-payment</b> is 20%.", "Bảo hiểm chi trả 80%, anh/chị đồng chi trả 20%.", "自己負担", "jiko futan"),
  ("itemised bill", "/ˌaɪtəmaɪzd ˈbɪl/", "n", "hóa đơn chi tiết từng khoản", "Could I have an <b>itemised bill</b>, please?", "Cho tôi xin hóa đơn chi tiết được không?", "明細書", "meisaisho"),
  ("cashier", "/kæˈʃɪə/", "n", "quầy thu ngân, thu ngân", "Please pay at the <b>cashier</b> on the ground floor.", "Anh/chị vui lòng thanh toán ở quầy thu ngân tầng trệt.", "会計", "kaikei"),
 ],
 "phrases": [
  ("Will you use your insurance, or pay yourself?", "Anh/chị thanh toán qua bảo hiểm hay tự chi trả ạ?"),
  ("May I make a copy of your insurance card?", "Em photo thẻ bảo hiểm của anh/chị được không ạ?"),
  ("Your insurance covers most of the cost.", "Bảo hiểm của anh/chị chi trả phần lớn chi phí."),
  ("We need to check with your insurance company first.", "Bên em cần xác nhận với công ty bảo hiểm trước."),
  ("Here is your itemised bill.", "Đây là hóa đơn chi tiết của anh/chị."),
  ("You can pay by card, cash or bank transfer.", "Anh/chị có thể thanh toán bằng thẻ, tiền mặt hoặc chuyển khoản."),
  ("Please keep your receipts for the claim.", "Anh/chị giữ lại biên lai để làm hồ sơ bồi thường nhé."),
  ("The medical certificate will be ready tomorrow.", "Ngày mai sẽ có giấy xác nhận của bác sĩ ạ."),
  ("Please sign here to confirm your details.", "Anh/chị ký vào đây để xác nhận thông tin ạ."),
 ],
 "dialogues": [
  ("Does my insurance cover this?", [
    ("Let me check with your insurance company. It usually takes about 20 minutes.", True, "Không đoán + kiểm tra + thời gian dự kiến."),
    ("Yes, insurance cover all.", False, "Hứa khi chưa kiểm tra; lại thiếu 's' ('covers')."),
    ("I don't know, it's your insurance.", False, "Đẩy trách nhiệm, thiếu hỗ trợ."),
  ]),
  ("Why is the bill so high?", [
    ("I understand. Here's the itemised bill. Let me go through each item with you.", True, "Đồng cảm + minh bạch từng khoản."),
    ("Because hospital is expensive.", False, "Thiếu mạo từ và không giải thích chi tiết."),
    ("You used many things.", False, "Nghe như trách bệnh nhân, không cụ thể."),
  ]),
  ("I need a medical certificate for my company.", [
    ("Of course. The doctor needs to sign it. It'll be ready tomorrow morning.", True, "Nói rõ quy trình (bác sĩ ký) + thời gian."),
    ("OK, I write it for you now.", False, "Lễ tân không được tự viết giấy thay bác sĩ; lại thiếu 'will'."),
    ("Certificate is not free.", False, "Chưa trả lời yêu cầu mà nói chuyện phí trước, nghe cộc."),
  ]),
  ("Can I pay by card?", [
    ("Yes, of course. We accept all major cards. Please insert it here.", True, "Trả lời rõ + hướng dẫn thao tác."),
    ("Yes, can.", False, "Thiếu chủ ngữ: 'Yes, you can.'"),
    ("Card is problem, cash better.", False, "Thiếu mạo từ/động từ và gây bất tiện không cần thiết."),
  ]),
  ("Do I have to pay a deposit?", [
    ("Yes, for admission we need a deposit of five million dong. It will be taken off your final bill.", True, "Xác nhận + số tiền + giải thích cách trừ vào hóa đơn."),
    ("Yes, pay first, then we treat.", False, "Nghe lạnh lùng; nên giải thích tiền tạm ứng."),
    ("Deposit is five millions.", False, "Sai: 'five million' (không thêm 's' sau số)."),
  ]),
 ],
 "listen": [
  ("May I see your insurance card, please", ["insurance", "card"], "hỏi thẻ bảo hiểm"),
  ("Please pay at the cashier on the ground floor", ["cashier", "ground"], "chỉ quầy thu ngân"),
  ("Here is your receipt for the insurance claim", ["receipt", "claim"], "đưa biên lai"),
  ("Your insurance covers eighty percent of the cost", ["covers", "eighty"], "mức bảo hiểm chi trả"),
  ("Your total today is one point two million dong. Your insurance covers most of it. You only need to pay two hundred thousand.", ["total", "insurance", "hundred"], "báo chi phí"),
  ("For admission, we need a deposit of five million dong. It will be taken off your final bill. Please keep the receipt.", ["admission", "deposit", "receipt"], "tạm ứng nhập viện"),
 ],
})

# ───────────────────────── 9. Giao ban & phối hợp với bác sĩ ─────────────────────────
PHASES.append({
 "title": "Giao ban & phối hợp với bác sĩ",
 "vocab": [
  ("shift", "/ʃɪft/", "n", "ca trực, ca làm", "I'm on the night <b>shift</b> this week.", "Tuần này em trực ca đêm.", "勤務", "kinmu"),
  ("medical record", "/ˌmedɪkl ˈrekɔːd/", "n", "hồ sơ bệnh án", "Please write it in the <b>medical record</b>.", "Vui lòng ghi việc đó vào hồ sơ bệnh án.", "カルテ", "karute"),
  ("ward round", "/ˈwɔːd raʊnd/", "n", "buổi đi buồng (bác sĩ thăm khám)", "The <b>ward round</b> starts at 8 a.m.", "Bác sĩ đi buồng lúc 8 giờ sáng.", "回診", "kaishin"),
  ("escalate", "/ˈeskəleɪt/", "v", "báo cáo lên cấp trên, chuyển lên xử lý", "If her oxygen level drops, <b>escalate</b> it to the doctor immediately.", "Nếu SpO2 của bà ấy giảm, báo ngay lên bác sĩ."),
  ("doctor's orders", "/ˌdɒktəz ˈɔːdəz/", "n", "y lệnh của bác sĩ", "Please follow the <b>doctor's orders</b> in the chart.", "Vui lòng thực hiện theo y lệnh bác sĩ trong bệnh án.", "医師の指示", "ishi no shiji"),
  ("on call", "/ˌɒn ˈkɔːl/", "adj", "trực (sẵn sàng khi được gọi)", "Dr Minh is <b>on call</b> tonight.", "Tối nay bác sĩ Minh trực."),
  ("observation", "/ˌɒbzəˈveɪʃn/", "n", "theo dõi (sinh hiệu, tình trạng)", "Please do his <b>observations</b> every four hours.", "Vui lòng đo và theo dõi sinh hiệu cho ông ấy mỗi bốn giờ."),
  ("stable", "/ˈsteɪbl/", "adj", "ổn định", "The patient in bed 3 is <b>stable</b> and sleeping well.", "Bệnh nhân giường 3 ổn định và ngủ tốt.", "安定した", "antei shita"),
  ("deteriorate", "/dɪˈtɪəriəreɪt/", "v", "diễn biến xấu đi", "Call the doctor if the patient starts to <b>deteriorate</b>.", "Gọi bác sĩ nếu bệnh nhân có dấu hiệu xấu đi."),
  ("monitor", "/ˈmɒnɪtə/", "v", "theo dõi sát", "Please <b>monitor</b> her temperature tonight.", "Vui lòng theo dõi sát nhiệt độ của bà ấy tối nay."),
 ],
 "phrases": [
  ("Let me give you the update on my patients.", "Em xin cập nhật tình hình các bệnh nhân của em."),
  ("Mr Kim in bed 4 had a fever at 2 a.m. The doctor was informed.", "Ông Kim giường 4 sốt lúc 2 giờ sáng. Đã báo bác sĩ."),
  ("She's stable, and her pain is under control.", "Bà ấy ổn định, cơn đau đã được kiểm soát."),
  ("Please keep an eye on his blood pressure.", "Vui lòng để ý huyết áp của ông ấy."),
  ("Doctor, I'm worried about the patient in bed 7.", "Bác sĩ ơi, em lo cho bệnh nhân giường 7."),
  ("Could you come and see him, please?", "Bác sĩ qua xem ông ấy giúp em được không ạ?"),
  ("Let me read the order back to you to make sure it's correct.", "Em xin đọc lại y lệnh để bác sĩ xác nhận là đúng."),
  ("Has the doctor seen the blood test results yet?", "Bác sĩ đã xem kết quả xét nghiệm máu chưa?"),
  ("I've written everything in the medical record.", "Em đã ghi đầy đủ vào hồ sơ bệnh án."),
  ("Is there anything else I need to know?", "Còn gì em cần biết nữa không ạ?"),
 ],
 "dialogues": [
  ("How was the night shift?", [
    ("Quiet overall. Six patients are stable. Mr Kim in bed 4 had a fever at 2 a.m., and Dr Minh saw him.", True, "Tóm tắt chung + con số + sự việc quan trọng và ai đã xử lý."),
    ("Everything OK, nothing.", False, "Quá sơ sài — giao ban phải có thông tin cụ thể từng bệnh nhân."),
    ("Bed 4 have fever, I don't know why.", False, "Sai chia ('had') và thiếu thông tin đã báo bác sĩ hay chưa."),
  ]),
  ("Doctor on the phone: What's the problem with the patient?", [
    ("This is Lan, nurse on Ward 3. Mr Wilson in bed 7 has a new fever and a fast pulse. Could you come and see him?", True, "Giới thiệu + bệnh nhân + thay đổi + yêu cầu rõ (kiểu SBAR)."),
    ("Doctor, bed 7 not good, come please.", False, "Thiếu thông tin cụ thể để bác sĩ đánh giá mức khẩn."),
    ("He is sick more than yesterday.", False, "Sai so sánh ('sicker') và không nêu dấu hiệu đo được."),
  ]),
  ("Give him the new medicine now.", [
    ("Sure. Just to confirm: which medicine, what dose, and how should I give it? I'll read it back to you.", True, "Hỏi đủ tên thuốc, liều, đường dùng rồi đọc lại y lệnh để xác nhận — thực hành an toàn."),
    ("OK, I give the normal dose.", False, "Tự đoán liều là sai nguyên tắc an toàn."),
    ("Which medicine? You say not clear.", False, "Sai ngữ pháp và thiếu lịch sự: 'Sorry, could you repeat that?'"),
  ]),
  ("Is there anyone I need to watch closely today?", [
    ("Yes, Mrs Ha in bed 2. Her oxygen level dropped last night. Please check it every two hours.", True, "Chỉ rõ bệnh nhân + lý do + việc cần làm."),
    ("No, all good, don't worry.", False, "Giao ban hời hợt, có thể bỏ sót nguy cơ."),
    ("Bed 2 oxygen low, watch.", False, "Thiếu động từ, câu cụt; không rõ mức độ và tần suất theo dõi."),
  ]),
  ("The patient's blood pressure is very low. What should we do?", [
    ("I'll page the doctor on call right now and stay with the patient.", True, "Báo bác sĩ trực ngay + không rời bệnh nhân."),
    ("Let's wait one hour and check again.", False, "Chờ đợi khi dấu hiệu bất thường là không an toàn."),
    ("Give him coffee, it goes up.", False, "Xử lý sai và không báo bác sĩ."),
  ]),
 ],
 "listen": [
  ("I'm on the night shift this week", ["night", "shift"], "lịch ca trực"),
  ("The ward round starts at eight", ["ward", "eight"], "giờ đi buồng"),
  ("Please monitor her temperature tonight", ["monitor", "temperature"], "dặn theo dõi"),
  ("Dr Minh is on call tonight", ["Minh", "call"], "bác sĩ trực"),
  ("I have six patients on this shift. Most of them are stable. The patient in bed four had a fever at two a.m.", ["six", "stable", "fever"], "giao ban đầu ca"),
  ("Mrs Ha's oxygen level dropped last night. The doctor saw her at three. Please check her every two hours.", ["oxygen", "doctor", "every"], "bệnh nhân cần theo dõi"),
 ],
})

# ───────────────────────── Vai trò (roles) ─────────────────────────
ROLES = {
 "nurse": {"label": "Điều dưỡng", "emoji": "🩺",
  "scenarios": [
   ("ns_admit", "Tiếp nhận bệnh nhân nhập viện", "You are a foreign patient being admitted to the ward. I am your nurse. Answer my questions about your name, allergies and current medicine. Ask about visiting hours and the call button."),
   ("ns_pain", "Bệnh nhân đau sau mổ", "You are a patient on the ward the day after surgery. Tell me you are in pain. Answer my questions about the pain score, and ask if you can have more medicine."),
   ("ns_doctor", "Gọi báo bác sĩ", "You are the doctor on call. I am a nurse phoning you about a patient whose condition has changed. Ask me clear questions about the patient's vital signs and what I need from you."),
   ("ns_handover", "Giao ban cuối ca", "You are the nurse starting the next shift. I will hand over my patients. Ask about any changes, pending tests and patients to watch."),
  ],
  "dialogues": [
   ("Nurse, can I have more painkillers?", [
     ("I'll check your chart and ask the doctor. How bad is the pain from 0 to 10?", True, "Không tự ý cho thuốc + kiểm tra y lệnh + đánh giá mức đau."),
     ("Sure, take two more.", False, "Tự ý cho thêm thuốc khi chưa có y lệnh — không an toàn."),
     ("No, you take already.", False, "Sai thì ('You've already had some') và cộc lốc.")]),
   ("Why do you keep asking my name?", [
     ("It's for your safety. We check your name before every medicine and test.", True, "Giải thích lý do an toàn một cách nhẹ nhàng."),
     ("Because I forget.", False, "Sai thì và làm bệnh nhân mất tin tưởng."),
     ("It's rule, just answer.", False, "Thiếu mạo từ ('the rule') và thiếu lịch sự.")]),
   ("I think I'm allergic to this.", [
     ("Thank you for telling me. I won't give it until I've checked with the doctor.", True, "Dừng ngay + kiểm tra với bác sĩ."),
     ("No, it's a normal medicine.", False, "Bỏ qua cảnh báo dị ứng — rất nguy hiểm."),
     ("You allergy before?", False, "Sai từ loại và cấu trúc: 'Have you had an allergy to it before?'")]),
   ("Can I get out of bed by myself?", [
     ("Not yet, please. Press the call button and I'll help you, so you don't fall.", True, "Hướng dẫn an toàn + lý do + cách gọi hỗ trợ."),
     ("Yes, no problem.", False, "Bỏ qua nguy cơ té ngã."),
     ("No! Don't!", False, "Quá gay gắt, thiếu giải thích.")]),
   ("Doctor: What's his blood pressure?", [
     ("It's 90 over 60, lower than this morning. His pulse is 110.", True, "Số liệu chính xác + so sánh diễn tiến + thông tin kèm theo."),
     ("It's low, quite low.", False, "Không có số cụ thể, bác sĩ khó đánh giá."),
     ("Ninety sixty, I think.", False, "Đọc không rõ ('90 over 60') và thiếu chắc chắn — hãy đo lại nếu chưa chắc.")]),
   ("How are you today, nurse?", [
     ("I'm fine, thank you. More importantly, how are you feeling this morning?", True, "Đáp lịch sự + chuyển sự chú ý về bệnh nhân."),
     ("Very tired, too many patients.", False, "Than phiền với bệnh nhân là thiếu chuyên nghiệp."),
     ("I'm fine. And you are fine?", False, "Sai cấu trúc câu hỏi: 'And how are you?'")]),
  ]},
 "reception": {"label": "Lễ tân phòng khám", "emoji": "🗂️",
  "scenarios": [
   ("rc_new", "Đăng ký bệnh nhân mới", "You are a foreign patient visiting the clinic for the first time with a sore throat. I am the receptionist. Give your details when I ask, and ask how long you will wait."),
   ("rc_book", "Đặt lịch qua điện thoại", "You are calling the clinic to book an appointment with a skin specialist next week. Ask about available times, the price and what to bring."),
   ("rc_insurance", "Hỏi về bảo hiểm", "You are an expat patient with international health insurance. Ask if the clinic can bill your insurance directly and what you need to pay today."),
   ("rc_wait", "Bệnh nhân chờ lâu", "You are a patient who has waited 90 minutes. Complain politely but firmly. Calm down if I apologise and tell you exactly what will happen next."),
  ],
  "dialogues": [
   ("Hello, I'd like to book an appointment.", [
     ("Of course. Which doctor would you like to see, and what day suits you?", True, "Đồng ý + hỏi hai thông tin cần để đặt lịch."),
     ("Book when?", False, "Cụt lủn, thiếu lịch sự."),
     ("OK, what is your problem?", False, "Hỏi sức khỏe qua điện thoại chung chung nghe đột ngột; nên hỏi bác sĩ/thời gian trước.")]),
   ("How much is a consultation?", [
     ("It's 500,000 dong with a general doctor. Tests are charged separately.", True, "Giá rõ + lưu ý chi phí phát sinh."),
     ("Not expensive, don't worry.", False, "Không cho con số cụ thể."),
     ("Consultation is 500 thousands.", False, "Sai: 'five hundred thousand' không có 's'; nên nói kèm đơn vị 'dong'.")]),
   ("Can I see the doctor now? It's urgent.", [
     ("I'm sorry you're not feeling well. Can you tell me briefly what's wrong? I'll ask the nurse to see you straight away.", True, "Đồng cảm + hỏi ngắn + chuyển điều dưỡng đánh giá mức khẩn."),
     ("Everyone is urgent. Please wait.", False, "Gạt đi — lễ tân không được tự đánh giá mức khẩn."),
     ("You wait, number 30.", False, "Cộc lốc, bỏ qua mức độ khẩn.")]),
   ("What do I need to bring tomorrow?", [
     ("Please bring your passport, your insurance card and any medicine you're taking.", True, "Liệt kê đầy đủ, rõ ràng."),
     ("Bring everything.", False, "Mơ hồ, bệnh nhân không biết mang gì."),
     ("You bring passport and insurance.", False, "Thiếu 'Please' và 'your', nghe như ra lệnh.")]),
   ("Can I change my appointment to Friday?", [
     ("Let me check. Yes, Dr Anna has a free slot at 10 a.m. on Friday. Shall I book it?", True, "Kiểm tra + phương án cụ thể + hỏi xác nhận."),
     ("Friday full already.", False, "Thiếu 'is' và chưa kiểm tra kỹ."),
     ("Yes, you come Friday.", False, "Chưa nêu giờ cụ thể, dễ gây nhầm lịch.")]),
   ("Can you tell me my wife's test results?", [
     ("I'm sorry, I can only share results with the patient. The doctor can talk to her, or to you if she agrees.", True, "Bảo mật thông tin bệnh nhân + giải thích lịch sự."),
     ("Sure, she is your wife, no problem.", False, "Vi phạm bảo mật thông tin bệnh nhân."),
     ("No, it's secret.", False, "Đúng nguyên tắc nhưng quá cộc, không đưa hướng giải quyết.")]),
  ]},
 "pharmacy": {"label": "Nhà thuốc · Dược", "emoji": "💊",
  "scenarios": [
   ("ph_rx", "Nhận đơn thuốc", "You are a foreign customer bringing a prescription to the pharmacy. I am the pharmacy staff. Answer my questions about allergies and other medicine, and ask how to take it."),
   ("ph_otc", "Hỏi mua thuốc không kê đơn", "You are a tourist with a cold asking for something to help. I am the pharmacy staff. Answer my questions. Ask for antibiotics, and accept my advice if I explain politely."),
   ("ph_side", "Phản ánh tác dụng phụ", "You are a customer who bought medicine yesterday and now feels a little sick. Ask me if you should stop taking it."),
   ("ph_stock", "Thuốc hết hàng", "You are a customer whose regular medicine is out of stock at the pharmacy. Ask what you can do and when it will arrive."),
  ],
  "dialogues": [
   ("Here's my prescription.", [
     ("Thank you. Before I prepare it, are you allergic to any medicine?", True, "Cảm ơn + hỏi dị ứng trước khi soạn thuốc."),
     ("OK, wait.", False, "Cộc và bỏ qua bước hỏi dị ứng."),
     ("Thank. You sit.", False, "Thiếu 's' và câu mệnh lệnh cụt.")]),
   ("Can I take this with alcohol?", [
     ("Let me check that with the pharmacist for you. Some medicines don't mix well with alcohol.", True, "Không đoán + hỏi dược sĩ + nhắc chung về rủi ro khi uống rượu bia."),
     ("A little beer is OK.", False, "Khuyên sai, có thể gây hại."),
     ("Why you drink when sick?", False, "Sai cấu trúc câu hỏi và mang tính phán xét.")]),
   ("How many times a day should I take this?", [
     ("It's written on the label, as your doctor prescribed. Let me go through it with you.", True, "Dựa vào đơn/nhãn + hướng dẫn cùng bệnh nhân."),
     ("Take when you feel bad.", False, "Tự đặt cách dùng, không theo đơn."),
     ("Many times is better.", False, "Nguy hiểm — khuyến khích dùng quá liều.")]),
   ("Do you have something for a headache?", [
     ("Before I suggest anything, do you have any allergies, or are you taking any other medicine?", True, "Hỏi dị ứng và thuốc đang dùng trước khi gợi ý thuốc."),
     ("Yes, this one, very strong.", False, "Không hỏi thông tin an toàn trước khi bán."),
     ("Headache is normal, drink water.", False, "Coi nhẹ triệu chứng, không tư vấn.")]),
   ("This medicine is out of stock? I need it today.", [
     ("I'm sorry. Our other branch has it. I can call them and ask them to keep one for you.", True, "Xin lỗi + giải pháp cụ thể."),
     ("No have, sorry.", False, "Dịch từng chữ: 'Sorry, we don't have it.' — và thiếu giải pháp."),
     ("Take another medicine, same same.", False, "Tự ý đổi thuốc kê đơn là không an toàn.")]),
   ("Is this medicine safe during pregnancy?", [
     ("That's an important question. Please check with your doctor or our pharmacist before taking it.", True, "Ghi nhận + chuyển đúng chuyên môn."),
     ("Yes, it's safe, I think.", False, "Đoán mò về vấn đề an toàn thai kỳ."),
     ("I don't know, you search online.", False, "Thiếu trách nhiệm và thiếu lịch sự — vấn đề an toàn phải hỏi chuyên môn.")]),
  ]},
 "care": {"label": "Chăm sóc · Hộ lý", "emoji": "🤝",
  "scenarios": [
   ("cr_morning", "Chăm sóc buổi sáng", "You are an elderly foreign patient in a care home. I am your care assistant helping you in the morning. Ask for help with washing and breakfast, and say you feel a bit weak."),
   ("cr_family", "Người nhà hỏi thăm", "You are the daughter of an elderly patient. Ask me how your mother ate and slept, and ask when you can talk to the nurse."),
   ("cr_refuse", "Bệnh nhân không chịu ăn", "You are an elderly patient who doesn't want to eat lunch because you feel sad. Open up only if I am patient and kind."),
   ("cr_move", "Hỗ trợ di chuyển", "You are a patient who needs help moving from the bed to a wheelchair. Tell me you are afraid of falling."),
  ],
  "dialogues": [
   ("I don't feel like eating today.", [
     ("That's OK. Would you like something small, like soup or fruit? I'll also tell the nurse.", True, "Tôn trọng + gợi ý nhẹ nhàng + báo điều dưỡng."),
     ("You must eat, eat now.", False, "Ép buộc, thiếu tôn trọng người bệnh."),
     ("Why you don't eat?", False, "Sai cấu trúc câu hỏi: 'Why don't you want to eat?'")]),
   ("Can you help me get into the wheelchair?", [
     ("Of course. Let me lock the brakes first. Hold my arm and stand up slowly with me.", True, "An toàn trước (khóa phanh) + hướng dẫn từng bước."),
     ("OK, jump in.", False, "Không an toàn, dễ gây ngã."),
     ("You can do yourself.", False, "Thiếu 'it by' ('do it by yourself') và từ chối hỗ trợ.")]),
   ("How did my mother sleep last night?", [
     ("She slept quite well and woke up once. The nurse can tell you more about her health.", True, "Thông tin trong phạm vi quan sát + chuyển điều dưỡng về chuyên môn."),
     ("She sleep good.", False, "Sai thì và từ loại: 'She slept well.'"),
     ("I don't know, not my shift.", False, "Nên nói 'Let me check the notes for you.'")]),
   ("I feel a bit dizzy.", [
     ("Please sit down and stay here. I'll call the nurse right now.", True, "Giữ an toàn + báo ngay điều dưỡng."),
     ("Walk a little, you will feel better.", False, "Nguy cơ té ngã khi đang chóng mặt."),
     ("It's normal for old people.", False, "Coi nhẹ triệu chứng và mang tính định kiến tuổi tác.")]),
   ("I want to wash by myself.", [
     ("Of course. I'll wait outside. Please use the handrail and call me if you need anything.", True, "Tôn trọng sự tự chủ + nhắc an toàn."),
     ("No, you are too old.", False, "Thiếu tôn trọng, định kiến tuổi tác."),
     ("OK, you wash, I go.", False, "Câu cụt; bỏ đi mà không dặn an toàn.")]),
   ("Can you open the window? It's hot.", [
     ("Sure. Is that better? I can also bring you some water.", True, "Đáp ứng + hỏi lại + chăm sóc thêm."),
     ("Hot? I feel cold.", False, "Lấy cảm giác của mình phủ nhận nhu cầu người bệnh."),
     ("Wait, I open.", False, "Thiếu 'will' và tân ngữ: 'I'll open it.'")]),
  ]},
}

PACK = {
 "id": "health",
 "label": "Y tế · Điều dưỡng",
 "short": "Y tế",
 "emoji": "🩺",
 "desc": "Điều dưỡng · lễ tân phòng khám · dược",
 "persona": "a Vietnamese nurse or clinic staff member",
 "counterpart": "a foreign patient or doctor",
 "context": "healthcare and clinics",
 "core": [10, 11],
 "report": {
  "title": "Giao ban 60 giây", "short": "Giao ban", "sub": "Nói như giao ban đầu ca 🎙️",
  "steps": [["Patients", "I have six patients. Most of them are stable …"], ["Changes", "At 2 a.m., the patient in bed 4 had …"], ["To watch", "Please check … every four hours."]],
  "kind": "nursing shift handover",
  "structure": "patients and status / changes during the shift / what to watch next",
  "sample": "I have six patients on this shift, and five of them are stable. At 2 a.m., Mr Kim in bed 4 had a fever. I informed Dr Minh, and a blood test was done. Please check his temperature every four hours and tell the doctor if it goes up again.",
 },
 "podcast": "Podcast y tế",
 "game_tag": "Game anime: đánh quái ca trực, hạ boss giờ cao điểm",
 "reverse_tag": "kiểu y tế",
 "jd_placeholder": "VD: Điều dưỡng khoa nội phòng khám quốc tế ở Hà Nội, bệnh nhân Hàn/Mỹ, đo sinh hiệu, giao ban với bác sĩ nước ngoài…",
 "rw_placeholder": "VD: bệnh nhân giường 4 sốt lúc 2 giờ sáng, cần báo bác sĩ trực",
 "quips": [
  "Checking vital signs…",
  "Name and date of birth, please!",
  "Any allergies?",
  "Hand hygiene first!",
  "Shift handover in 5!",
  "Deep breath, you're doing great!",
  "Calling the doctor!",
  "Safety first, always!",
  "Next patient, please!",
  "Coffee after the night shift…",
 ],
 "ai": [
  ("register", "Đăng ký khám", "You are a foreign patient at the clinic reception for the first time. I am the receptionist. Give your details when I ask, and ask about waiting time and the price."),
  ("symptoms", "Hỏi triệu chứng", "You are a patient with a cough and a mild fever. I am the nurse asking questions before you see the doctor. Answer my questions and mention one allergy only if I ask."),
  ("vitals", "Đo sinh hiệu", "You are a nervous patient. I am the nurse checking your blood pressure and temperature. Ask what I am doing and whether the numbers are OK."),
  ("pharmacy", "Nhà thuốc", "You are a tourist at a pharmacy with a prescription. Ask how to take the medicine and whether you can drink alcohol with it. Expect me to ask about allergies."),
  ("worried", "Người nhà lo lắng", "You are the worried son of a patient in the emergency room. Ask many questions about your mother. Calm down if I am kind, honest and tell you who will update you."),
  ("insurance", "Bảo hiểm & viện phí", "You are an expat patient checking out. Ask why the bill is high, whether your insurance covers it and ask for an itemised bill and a medical certificate."),
  ("doctor", "Báo cáo bác sĩ", "You are a foreign doctor on call. I am a nurse calling you about a patient whose condition has changed. Ask for vital signs and what I need from you."),
  ("handover", "Giao ban cuối ca", "You are the nurse starting the next shift. Ask me for a quick handover: my patients, changes during the shift and what to watch. Ask one follow-up question."),
 ],
 "rev": [
  ("Anh/chị có lịch hẹn trước không ạ?", "Do you have an appointment?"),
  ("Anh/chị điền giúp em phiếu này nhé.", "Could you fill in this form, please?"),
  ("Anh/chị có dị ứng thuốc nào không ạ?", "Are you allergic to any medicine?"),
  ("Anh/chị bị sốt từ khi nào ạ?", "When did the fever start?"),
  ("Em sẽ đo huyết áp cho anh/chị.", "I'm going to check your blood pressure."),
  ("Anh/chị xắn tay áo lên giúp em nhé.", "Could you roll up your sleeve, please?"),
  ("Sau 10 giờ tối anh/chị đừng ăn gì nhé.", "Please don't eat anything after 10 p.m."),
  ("Bác sĩ sẽ quyết định liều dùng.", "The doctor will decide the dosage."),
  ("Anh/chị bấm nút gọi nếu cần giúp nhé.", "Press the call button if you need help."),
  ("Em sẽ báo bác sĩ ngay.", "I'll tell the doctor right away."),
  ("Anh/chị cứ từ từ, không vội đâu ạ.", "Take your time. There's no rush."),
  ("Xe cứu thương đang tới.", "The ambulance is on its way."),
  ("Anh/chị thanh toán ở quầy thu ngân nhé.", "Please pay at the cashier."),
  ("Bệnh nhân giường 4 sốt lúc 2 giờ sáng.", "The patient in bed 4 had a fever at 2 a.m."),
 ],
 "reading": [
  {"t": "Clinic notice", "text": "SEN XANH INTERNATIONAL CLINIC\nOpening hours: Mon–Sat 7:30 a.m.–7 p.m., Sun 8 a.m.–12 p.m.\nWalk-in patients: please register before 6 p.m.\nPlease bring your passport and insurance card.\nFree interpreter service: English, Korean, Japanese (please ask at reception).", "q": [
    {"q": "Until what time can walk-in patients register on weekdays?", "o": ["12 p.m.", "6 p.m.", "7 p.m."], "a": 1},
    {"q": "What does the clinic offer for free?", "o": ["An interpreter", "A blood test", "Parking"], "a": 0}]},
  {"t": "Test preparation", "text": "BLOOD TEST – PATIENT INFORMATION\nYour test: Thursday, 7:30 a.m., Lab (2nd floor)\n• Do not eat for 8 hours before the test.\n• You may drink plain water.\n• Take your usual medicine only if your doctor says so.\n• Results: usually within 24 hours. The doctor will explain them to you.", "q": [
    {"q": "What can the patient drink before the test?", "o": ["Coffee", "Plain water", "Juice"], "a": 1},
    {"q": "Who will explain the results?", "o": ["The lab staff", "The receptionist", "The doctor"], "a": 2}]},
  {"t": "Medicine label", "text": "Patient: Anna Weber   DOB: 12/03/1988\nTake as directed by your doctor.\nTake after meals.\nDo not drink alcohol while taking this medicine.\nStore below 30°C, away from children.\nIf you notice a rash or feel unwell, stop and contact the clinic.", "q": [
    {"q": "When should the patient take this medicine?", "o": ["Before breakfast only", "After meals", "At bedtime only"], "a": 1},
    {"q": "What should she do if she gets a rash?", "o": ["Take more medicine", "Stop and contact the clinic", "Drink more water"], "a": 1}]},
  {"t": "Handover note", "text": "Ward 3 – Night shift handover (07:00)\nBed 2, Mrs Ha: oxygen level dropped to 91% at 1 a.m. Dr Minh saw her. Oxygen started. Now 96%. Check every 2 hours.\nBed 4, Mr Kim: fever 38.5°C at 2 a.m. Blood test done, results pending.\nBed 6, Mr Lee: fall risk – keep bed rails up.\nAll other patients stable.", "q": [
    {"q": "Which patient is waiting for test results?", "o": ["Mrs Ha", "Mr Kim", "Mr Lee"], "a": 1},
    {"q": "What should the day nurse do for Mr Lee?", "o": ["Keep the bed rails up", "Check oxygen every 2 hours", "Call the doctor at once"], "a": 0}]},
  {"t": "Insurance email", "text": "Dear Mr Tanaka,\nYour insurance company has approved the cost of your admission. The insurance covers 80% of the medical fees. Your co-payment is 20%, which you can pay at the cashier on discharge. Please keep all receipts.\nBest regards,\nAn Tâm Hospital – Patient Services", "q": [
    {"q": "How much does Mr Tanaka need to pay himself?", "o": ["0%", "20%", "80%"], "a": 1},
    {"q": "When can he pay?", "o": ["When he leaves the hospital", "Before admission", "Next month"], "a": 0}]},
 ],
 "events": [
  ("interview", "Phỏng vấn điều dưỡng quốc tế", "You are the nursing manager at an international hospital interviewing me for a nurse position. Ask about my experience, how I handle a difficult patient and how I communicate with doctors."),
  ("patient", "Đón bệnh nhân nước ngoài", "You are a foreign patient who speaks no Vietnamese arriving at the clinic with a high fever. Answer my questions and ask about the waiting time, costs and an interpreter."),
  ("doctor", "Làm việc với bác sĩ nước ngoài", "You are a visiting foreign doctor working with me for a week. Ask me about the ward routine, the patients and how to call for help."),
  ("audit", "Đoàn kiểm tra chất lượng", "You are an inspector from an international hospital quality programme. Ask me how we check patient identity, allergies and hand hygiene."),
  ("training", "Buổi đào tạo an toàn người bệnh", "You are a trainer running a patient safety workshop. Ask me to explain how I would report a patient whose condition is getting worse."),
  ("family", "Họp với người nhà bệnh nhân", "You are the adult child of an elderly foreign patient. Ask me about daily care, visiting hours and when you can speak to the doctor."),
  ("other", "Khác", ""),
 ],
 "roles": ROLES,
 "phases": PHASES,
}
