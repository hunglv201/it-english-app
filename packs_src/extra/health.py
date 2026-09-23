# -*- coding: utf-8 -*-
# v4.1 — nội dung làm giàu cho gói health (nối vào cuối gói, xem build.py)
# Tiếng Anh GIAO TIẾP cho nhân viên y tế, không phải phác đồ: không ghi liều thuốc; câu đúng luôn mô phỏng
# thực hành an toàn (báo bác sĩ, kiểm tra với chuyên môn, xác minh danh tính, phòng ngã, phòng sặc…).
EXTRA = {
 "phases": [
  # ───────────────────────── Nhi khoa & giao tiếp với phụ huynh ─────────────────────────
  {"title": "Nhi khoa & giao tiếp với phụ huynh",
   "vocab": [
    ("paediatric", "/ˌpiːdiˈætrɪk/", "adj", "(thuộc) nhi khoa", "The <b>paediatric</b> ward is on the third floor.", "Khoa nhi ở tầng ba."),
    ("vaccination", "/ˌvæksɪˈneɪʃn/", "n", "sự tiêm chủng, tiêm vắc-xin", "Her next <b>vaccination</b> is due in two months.", "Hai tháng nữa là đến lịch tiêm chủng tiếp theo của bé.", "予防接種", "yobō sesshu"),
    ("booster", "/ˈbuːstə/", "n", "mũi tiêm nhắc lại", "He needs a <b>booster</b> next year.", "Sang năm bé cần tiêm mũi nhắc lại.", "追加接種", "tsuika sesshu"),
    ("rash", "/ræʃ/", "n", "phát ban, nổi mẩn", "When did you first notice the <b>rash</b>?", "Anh/chị thấy bé nổi mẩn từ khi nào ạ?", "発疹", "hosshin"),
    ("dehydration", "/ˌdiːhaɪˈdreɪʃn/", "n", "mất nước", "Fewer wet nappies can be a sign of <b>dehydration</b>.", "Bé ít tè ướt tã có thể là dấu hiệu mất nước.", "脱水", "dassui"),
    ("newborn", "/ˈnjuːbɔːn/", "n/adj", "trẻ sơ sinh", "The midwife is checking the <b>newborn</b> now.", "Nữ hộ sinh đang kiểm tra cho bé sơ sinh.", "新生児", "shinseiji"),
    ("check-up", "/ˈtʃek ʌp/", "n", "buổi khám định kỳ, khám sức khỏe", "Please bring her back for a <b>check-up</b> in one month.", "Một tháng nữa anh/chị đưa bé quay lại khám định kỳ nhé.", "健診", "kenshin"),
    ("tummy", "/ˈtʌmi/", "n", "bụng (cách nói với trẻ con)", "Can you show me where your <b>tummy</b> hurts?", "Con chỉ cho cô chỗ bụng bị đau nhé?"),
    ("brave", "/breɪv/", "adj", "dũng cảm, giỏi", "You were so <b>brave</b> today!", "Hôm nay con dũng cảm lắm!"),
    ("guardian", "/ˈɡɑːdiən/", "n", "người giám hộ", "A parent or <b>guardian</b> must sign the form.", "Cha mẹ hoặc người giám hộ phải ký vào phiếu.", "保護者", "hogosha"),
   ],
   "phrases": [
    ("How old is your son?", "Bé nhà mình mấy tuổi rồi ạ?"),
    ("Is she eating and drinking normally?", "Bé có ăn uống bình thường không ạ?"),
    ("How many wet nappies has he had today?", "Hôm nay bé tè ướt mấy cái tã rồi ạ?"),
    ("Has she had all her vaccinations?", "Bé đã tiêm đủ các mũi chưa ạ?"),
    ("Could you hold him on your lap, please?", "Anh/chị bế bé ngồi trên đùi giúp em nhé."),
    ("This won't take long, sweetheart.", "Nhanh thôi con nhé."),
    ("You can stay with your child the whole time.", "Anh/chị có thể ở cạnh bé suốt lúc khám ạ."),
    ("Please bring her vaccination book next time.", "Lần sau anh/chị nhớ mang sổ tiêm chủng của bé nhé."),
    ("If he gets worse, please bring him back straight away.", "Nếu bé nặng hơn, anh/chị đưa bé quay lại ngay nhé."),
    ("Well done! Here's a sticker for you.", "Giỏi lắm! Cô tặng con một hình dán nè."),
   ],
   "dialogues": [
    ("My baby has a fever and won't drink.", [
      ("I'm sorry to hear that. How long has she had the fever? I'll ask the doctor to see her as soon as possible.", True, "Đồng cảm + hỏi thời gian sốt + xin bác sĩ khám sớm — trẻ nhỏ sốt, bỏ bú cần được xem ngay."),
      ("Baby fever is normal, don't worry.", False, "Coi nhẹ triệu chứng — trẻ sốt và bỏ bú cần bác sĩ khám."),
      ("How long she fever?", False, "Thiếu trợ động từ và động từ: 'How long has she had a fever?'"),
    ]),
    ("Will the injection hurt my son?", [
      ("He'll feel a quick sting, but it's over in a second. You can hold him and comfort him.", True, "Nói thật nhẹ nhàng + nhờ phụ huynh cùng trấn an bé."),
      ("No, children don't feel anything.", False, "Không trung thực — phụ huynh sẽ mất tin tưởng."),
      ("Little bit hurt, but he must be strong man.", False, "Thiếu chủ ngữ/động từ ('It'll hurt a little') và gây áp lực cho bé."),
    ]),
    ("Can I stay with her during the check?", [
      ("Of course. You can stay with her the whole time. Could you hold her on your lap?", True, "Đồng ý + nhờ phụ huynh bế bé để bé yên tâm."),
      ("No, parents go out.", False, "Cộc lốc như ra lệnh; thường phụ huynh được ở cạnh trẻ khi khám."),
      ("Yes, you can stay but no talk.", False, "Dịch từng chữ ('no talk' → 'please don't talk') và đặt điều kiện không cần thiết."),
    ]),
    ("He's had a rash on his arms since this morning.", [
      ("Thank you for telling me. Does he have a fever too? The doctor will look at the rash soon.", True, "Ghi nhận + hỏi triệu chứng kèm theo + để bác sĩ đánh giá."),
      ("It's allergy, give him cream.", False, "Tự chẩn đoán và tự khuyên dùng thuốc — việc của bác sĩ."),
      ("Rash since when? Morning?", False, "Hỏi cụt, hỏi lại điều phụ huynh vừa nói."),
    ]),
    ("She cried a lot. Is she OK?", [
      ("She was very brave. It's normal to cry after an injection. A cuddle will help her calm down.", True, "Khen bé + trấn an phụ huynh + gợi ý đơn giản."),
      ("Yes, she cry because she is weak.", False, "Sai thì ('cried') và nhận xét thiếu tế nhị."),
      ("Don't cry, don't cry.", False, "Không trả lời câu hỏi của phụ huynh."),
    ]),
   ],
   "listen": [
    ("The paediatric ward is on the third floor", ["paediatric", "third"], "chỉ đường khoa nhi"),
    ("Please bring her vaccination book next time", ["vaccination", "book"], "nhắc mang sổ tiêm chủng"),
    ("You were so brave today", ["brave", "today"], "khen bé"),
    ("Is he eating and drinking normally", ["eating", "drinking"], "hỏi ăn uống của trẻ"),
    ("Your daughter's temperature is a little high. The doctor will see her in ten minutes. You can hold her while you wait.", ["temperature", "minutes", "hold"], "báo phụ huynh trước khi khám"),
    ("Today he had his booster. He may be a little sleepy tonight. If you're worried, please call the clinic.", ["booster", "sleepy", "call"], "dặn phụ huynh sau tiêm"),
   ]},

  # ───────────────────────── Chăm sóc người cao tuổi ─────────────────────────
  {"title": "Chăm sóc người cao tuổi",
   "vocab": [
    ("dementia", "/dɪˈmenʃə/", "n", "sa sút trí tuệ", "Mrs Lee has <b>dementia</b>, so please speak slowly and use her name.", "Bà Lee bị sa sút trí tuệ, nên hãy nói chậm và gọi tên bà.", "認知症", "ninchishō"),
    ("walking frame", "/ˈwɔːkɪŋ freɪm/", "n", "khung tập đi", "Please keep your <b>walking frame</b> close to the bed.", "Bác để khung tập đi sát giường nhé.", "歩行器", "hokōki"),
    ("hearing aid", "/ˈhɪərɪŋ eɪd/", "n", "máy trợ thính", "Is your <b>hearing aid</b> switched on?", "Máy trợ thính của bác bật chưa ạ?", "補聴器", "hochōki"),
    ("dentures", "/ˈdentʃəz/", "n", "răng giả (hàm tháo lắp)", "Would you like me to clean your <b>dentures</b>?", "Bác có muốn cháu rửa răng giả giúp không ạ?", "入れ歯", "ireba"),
    ("incontinence", "/ɪnˈkɒntɪnəns/", "n", "tiểu tiện / đại tiện không tự chủ", "We use pads for residents with <b>incontinence</b>.", "Bên em dùng tấm lót cho người cao tuổi không tự chủ được tiểu tiện.", "失禁", "shikkin"),
    ("pressure sore", "/ˈpreʃə sɔː/", "n", "loét tì đè", "Check his heels for <b>pressure sores</b> every day.", "Kiểm tra gót chân ông mỗi ngày xem có loét tì đè không.", "褥瘡", "jokusō"),
    ("confused", "/kənˈfjuːzd/", "adj", "lú lẫn, không tỉnh táo như thường", "He seems more <b>confused</b> than yesterday.", "Ông có vẻ lú lẫn hơn hôm qua."),
    ("reposition", "/ˌriːpəˈzɪʃn/", "v", "đổi tư thế, xoay trở (người nằm lâu)", "We <b>reposition</b> her every two hours, as in her care plan.", "Bên em xoay trở cho bà hai giờ một lần, theo kế hoạch chăm sóc.", "体位変換", "taii henkan"),
    ("mobility", "/məʊˈbɪləti/", "n", "khả năng vận động, đi lại", "His <b>mobility</b> is better this week.", "Tuần này ông đi lại tốt hơn."),
    ("care plan", "/ˈkeə plæn/", "n", "kế hoạch chăm sóc", "Please read the <b>care plan</b> before you start.", "Vui lòng đọc kế hoạch chăm sóc trước khi bắt đầu.", "ケアプラン", "kea puran"),
   ],
   "phrases": [
    ("Good morning, Mr Park. It's Linh, your carer.", "Chào buổi sáng ông Park. Cháu là Linh, người chăm sóc ông đây ạ."),
    ("Can you hear me clearly?", "Bác nghe cháu nói rõ không ạ?"),
    ("Let's take it slowly. There's no hurry.", "Mình làm từ từ thôi bác. Không vội đâu ạ."),
    ("Would you like to sit by the window?", "Bác có muốn ngồi cạnh cửa sổ không ạ?"),
    ("Please hold the handrail.", "Bác vịn vào tay vịn nhé."),
    ("I'm going to turn you onto your side now. Is that OK?", "Bây giờ cháu xoay bác nằm nghiêng nhé. Được không ạ?"),
    ("Would you like to choose your clothes today?", "Hôm nay bác có muốn tự chọn quần áo không ạ?"),
    ("Your daughter is coming to visit this afternoon.", "Chiều nay con gái bác đến thăm đấy ạ."),
    ("I've noticed some redness on her heel. I'll tell the nurse.", "Cháu thấy gót chân bà hơi đỏ. Cháu sẽ báo điều dưỡng."),
   ],
   "dialogues": [
    ("Where am I? I want to go home.", [
      ("You're safe here, Mrs Lee. I'm Linh, and I'm looking after you today. Shall we have a cup of tea together?", True, "Trấn an + giới thiệu lại + chuyển hướng nhẹ nhàng — cách nói chuyện với người sa sút trí tuệ."),
      ("You live here already one year, you forget?", False, "Sai thì/trật tự ('You've lived here for a year') và tranh cãi làm người bệnh hoảng hơn."),
      ("You can't go home. Sit down.", False, "Mệnh lệnh cộc, không trấn an."),
    ]),
    ("Sorry, what did you say? I can't hear you.", [
      ("Sorry. Is your hearing aid on? I'll face you and speak more slowly.", True, "Kiểm tra máy trợ thính + nhìn thẳng + nói chậm — không cần hét."),
      ("I SAID IT'S LUNCH TIME!", False, "Hét lên nghe như bực bội; nên nói chậm, rõ và nhìn thẳng người nghe."),
      ("You deaf, I write for you.", False, "Thiếu 'are' và thiếu tôn trọng người cao tuổi."),
    ]),
    ("I can dress myself. I don't need help.", [
      ("Of course. I'll put your clothes here. Just call me if you need a hand.", True, "Tôn trọng sự tự lập + sẵn sàng hỗ trợ."),
      ("No, you are slow. I do it.", False, "Thiếu 'will' ('I'll do it') và làm người cao tuổi mất tự trọng."),
      ("OK, you do yourself.", False, "Thiếu tân ngữ ('do it yourself') và bỏ đi không dặn gì."),
    ]),
    ("Nurse, my father seems more confused today.", [
      ("Thank you for telling me. When did you first notice it? I'll check him and let the doctor know.", True, "Ghi nhận + hỏi thời điểm + báo bác sĩ — lú lẫn mới xuất hiện có thể là dấu hiệu bệnh."),
      ("Old people are always confused.", False, "Định kiến tuổi tác, bỏ qua một thay đổi quan trọng."),
      ("He confused because he is tired.", False, "Thiếu 'is' và tự đoán nguyên nhân thay bác sĩ."),
    ]),
    ("My back hurts from lying in bed all day.", [
      ("I'm sorry. Let me help you change position, and I'll check your skin at the same time.", True, "Đáp ứng + xoay trở + kiểm tra da phòng loét tì đè."),
      ("Lying is good, don't move.", False, "Sai — nằm yên một tư thế lâu dễ gây loét tì đè."),
      ("You turn yourself, please.", False, "Người nằm lâu thường cần hỗ trợ; nói vậy là bỏ mặc người bệnh."),
    ]),
   ],
   "listen": [
    ("Please keep your walking frame close to the bed", ["walking", "bed"], "nhắc để khung tập đi gần"),
    ("Is your hearing aid switched on", ["hearing", "switched"], "hỏi máy trợ thính"),
    ("Please read the care plan before you start", ["care", "plan"], "đọc kế hoạch chăm sóc"),
    ("He seems more confused than yesterday", ["confused", "yesterday"], "báo thay đổi tình trạng"),
    ("Mr Park needs help to walk. Please stay next to him and remind him to use his frame. He likes to walk after lunch.", ["help", "frame", "lunch"], "dặn hỗ trợ đi lại"),
    ("I turned Mrs Lee at ten. There's some redness on her left heel. Please tell the nurse and check it again at noon.", ["ten", "redness", "noon"], "báo da đỏ khi xoay trở"),
   ]},

  # ───────────────────────── Dinh dưỡng & ăn uống ─────────────────────────
  {"title": "Dinh dưỡng & ăn uống",
   "vocab": [
    ("appetite", "/ˈæpɪtaɪt/", "n", "cảm giác thèm ăn, ngon miệng", "How is your <b>appetite</b> today?", "Hôm nay anh/chị ăn có ngon miệng không ạ?", "食欲", "shokuyoku"),
    ("swallowing", "/ˈswɒləʊɪŋ/", "n", "sự nuốt", "Do you have any problems with <b>swallowing</b>?", "Anh/chị có bị khó nuốt không ạ?", "嚥下", "enge"),
    ("choking", "/ˈtʃəʊkɪŋ/", "n", "sự sặc, hóc, nghẹn", "Sit him up straight to lower the risk of <b>choking</b>.", "Đỡ ông ngồi thẳng để giảm nguy cơ bị sặc."),
    ("fluid intake", "/ˈfluːɪd ˌɪnteɪk/", "n", "lượng dịch (nước) uống vào", "Please write her <b>fluid intake</b> on the chart.", "Vui lòng ghi lượng nước bà uống vào phiếu theo dõi.", "水分摂取量", "suibun sesshuryō"),
    ("low-salt", "/ˌləʊ ˈsɔːlt/", "adj", "ít muối, ăn nhạt", "The doctor has put you on a <b>low-salt</b> diet.", "Bác sĩ cho anh/chị ăn theo chế độ ít muối.", "減塩", "gen'en"),
    ("thickener", "/ˈθɪkənə/", "n", "chất làm đặc (pha đồ uống cho người khó nuốt)", "Add <b>thickener</b> to his drinks, as the care plan says.", "Pha chất làm đặc vào đồ uống của ông theo đúng kế hoạch chăm sóc.", "とろみ剤", "toromizai"),
    ("dietitian", "/ˌdaɪəˈtɪʃn/", "n", "chuyên gia dinh dưỡng", "The <b>dietitian</b> will visit you this afternoon.", "Chiều nay chuyên gia dinh dưỡng sẽ đến gặp anh/chị.", "栄養士", "eiyōshi"),
    ("portion", "/ˈpɔːʃn/", "n", "khẩu phần, suất ăn", "Would you like a smaller <b>portion</b>?", "Anh/chị có muốn suất ăn nhỏ hơn không ạ?"),
    ("diabetic", "/ˌdaɪəˈbetɪk/", "adj", "(dành cho) người tiểu đường", "Mr Tan is on a <b>diabetic</b> diet.", "Ông Tan ăn theo chế độ cho người tiểu đường."),
    ("food chart", "/ˈfuːd tʃɑːt/", "n", "phiếu theo dõi ăn uống", "She ate half of her lunch. I've written it on the <b>food chart</b>.", "Bà ăn được nửa suất trưa. Em đã ghi vào phiếu theo dõi ăn uống."),
   ],
   "phrases": [
    ("Are you on a special diet?", "Anh/chị có đang ăn theo chế độ đặc biệt nào không ạ?"),
    ("Do you have any food allergies?", "Anh/chị có dị ứng thức ăn nào không ạ?"),
    ("Is there any food you don't eat?", "Có món nào anh/chị không ăn không ạ?"),
    ("Here's your lunch. It's the low-salt menu.", "Bữa trưa của anh/chị đây ạ. Đây là thực đơn ít muối."),
    ("Please sit up straight while you eat.", "Anh/chị ngồi thẳng lưng khi ăn nhé."),
    ("Take small bites and eat slowly.", "Anh/chị ăn từng miếng nhỏ và ăn chậm thôi ạ."),
    ("How much of your breakfast did you eat?", "Bữa sáng anh/chị ăn được bao nhiêu ạ?"),
    ("Please tell me each time you finish a drink.", "Mỗi lần uống hết một cốc, anh/chị báo em nhé."),
    ("Food from outside needs to be checked with the nurse first.", "Đồ ăn mang từ ngoài vào cần hỏi điều dưỡng trước ạ."),
    ("I'll ask the dietitian to come and see you.", "Em sẽ nhờ chuyên gia dinh dưỡng đến gặp anh/chị."),
   ],
   "dialogues": [
    ("Can my family bring me some food from home?", [
      ("Please check with me first. Some patients are on special diets, so I'll look at your notes.", True, "Không cấm ngay + kiểm tra chế độ ăn trong hồ sơ."),
      ("Yes, bring anything you like.", False, "Bỏ qua chế độ ăn bệnh lý — có thể gây hại."),
      ("No outside food, is rule.", False, "Thiếu chủ ngữ ('it's the rule') và từ chối không giải thích."),
    ]),
    ("He coughs every time he drinks water.", [
      ("Thank you for telling me. Please don't give him any more drinks for now. I'll tell the nurse so his swallowing can be checked.", True, "Tạm dừng cho uống + báo để đánh giá khả năng nuốt — ho khi uống có thể là dấu hiệu sặc."),
      ("Give him more water, he is thirsty.", False, "Nguy hiểm — ho khi uống có thể là sặc vào đường thở."),
      ("He drink too fast, that's all.", False, "Sai chia ('drinks') và tự kết luận, bỏ qua dấu hiệu khó nuốt."),
    ]),
    ("I'm not hungry. I don't want my lunch.", [
      ("That's OK. Would you like a smaller portion, or something else, like soup? I'll let the nurse know.", True, "Tôn trọng + gợi ý lựa chọn + báo điều dưỡng khi người bệnh ăn kém."),
      ("You must finish all, or you not get better.", False, "Ép buộc và thiếu trợ động từ ('or you won't get better')."),
      ("OK, no eat.", False, "Cộc lốc, dịch từng chữ; không tìm hiểu vì sao người bệnh bỏ ăn."),
    ]),
    ("Why is my food so bland?", [
      ("I understand. You're on a low-salt diet, as the doctor ordered. I can ask the dietitian about other ways to add flavour.", True, "Đồng cảm + giải thích lý do + hướng giải quyết."),
      ("Because the cook is bad.", False, "Đổ lỗi, thiếu chuyên nghiệp và không giải thích chế độ ăn."),
      ("Salt is not good, you cannot eat.", False, "Câu ghép cụt, thiếu tân ngữ ('eat it') và nghe như ra lệnh."),
    ]),
    ("How much did my mother eat today?", [
      ("She ate about half of her breakfast and most of her lunch. It's all on her food chart.", True, "Thông tin cụ thể + nguồn ghi chép."),
      ("She eat OK.", False, "Sai thì ('She ate') và quá chung chung."),
      ("I don't remember, many patients.", False, "Câu thứ hai thiếu chủ ngữ/động từ; nên xem phiếu theo dõi rồi trả lời."),
    ]),
   ],
   "listen": [
    ("How is your appetite today", ["appetite", "today"], "hỏi chuyện ăn uống"),
    ("Would you like a smaller portion", ["smaller", "portion"], "hỏi khẩu phần"),
    ("Please sit up straight while you eat", ["straight", "eat"], "tư thế khi ăn"),
    ("The dietitian will visit you this afternoon", ["dietitian", "afternoon"], "hẹn chuyên gia dinh dưỡng"),
    ("Mr Tan is on a diabetic diet. Please check with the nurse before you give him any snacks. Write everything he eats on the food chart.", ["diabetic", "snacks", "chart"], "dặn chế độ ăn tiểu đường"),
    ("Mrs Ha has problems with swallowing. Add thickener to her drinks, as her care plan says. Stay with her while she eats.", ["swallowing", "thickener", "eats"], "dặn chăm sóc người khó nuốt"),
   ]},

  # ───────────────────────── Vật lý trị liệu & phục hồi chức năng ─────────────────────────
  {"title": "Vật lý trị liệu & phục hồi chức năng",
   "vocab": [
    ("physiotherapy", "/ˌfɪziəʊˈθerəpi/", "n", "vật lý trị liệu", "Your <b>physiotherapy</b> session is at ten.", "Buổi vật lý trị liệu của anh/chị lúc mười giờ.", "理学療法", "rigaku ryōhō"),
    ("rehabilitation", "/ˌriːəˌbɪlɪˈteɪʃn/", "n", "phục hồi chức năng", "After the stroke, he started <b>rehabilitation</b> in our unit.", "Sau cơn đột quỵ, ông bắt đầu phục hồi chức năng ở khoa mình.", "リハビリ", "rihabiri"),
    ("range of motion", "/ˌreɪndʒ əv ˈməʊʃn/", "n", "tầm vận động (của khớp)", "We'll measure the <b>range of motion</b> in your shoulder.", "Bên em sẽ đo tầm vận động khớp vai của anh/chị.", "可動域", "kadōiki"),
    ("crutches", "/ˈkrʌtʃɪz/", "n", "nạng", "Let me show you how to use your <b>crutches</b> on the stairs.", "Để em chỉ anh/chị cách dùng nạng khi lên xuống cầu thang.", "松葉杖", "matsubazue"),
    ("walking stick", "/ˈwɔːkɪŋ stɪk/", "n", "gậy chống", "Hold the <b>walking stick</b> in your good hand.", "Anh/chị cầm gậy chống ở tay bên khỏe nhé.", "杖", "tsue"),
    ("stiff", "/stɪf/", "adj", "cứng, khó cử động", "My knee feels <b>stiff</b> in the morning.", "Buổi sáng đầu gối tôi thấy cứng."),
    ("strength", "/streŋθ/", "n", "sức mạnh (cơ), sức lực", "These exercises will build the <b>strength</b> in your legs.", "Các bài tập này sẽ tăng sức mạnh cơ chân."),
    ("balance", "/ˈbæləns/", "n", "thăng bằng", "Hold the chair if you lose your <b>balance</b>.", "Vịn vào ghế nếu anh/chị mất thăng bằng nhé."),
    ("sprain", "/spreɪn/", "n/v", "bong gân", "The doctor said it's a mild ankle <b>sprain</b>.", "Bác sĩ nói đây là bong gân cổ chân nhẹ.", "捻挫", "nenza"),
    ("repetition", "/ˌrepəˈtɪʃn/", "n", "số lần lặp (của một động tác tập)", "The physio will tell you how many <b>repetitions</b> to do.", "Chuyên viên vật lý trị liệu sẽ cho anh/chị biết mỗi động tác tập bao nhiêu lần."),
   ],
   "phrases": [
    ("Let's start with some gentle exercises.", "Mình bắt đầu với vài bài tập nhẹ nhàng nhé."),
    ("Tell me if it hurts, and we'll stop.", "Nếu đau thì anh/chị báo em, mình sẽ dừng."),
    ("Lift your leg slowly and hold it for five seconds.", "Nâng chân lên từ từ và giữ trong năm giây."),
    ("Breathe normally. Don't hold your breath.", "Anh/chị thở đều. Đừng nín thở nhé."),
    ("You're doing much better than last week.", "Anh/chị tiến bộ hơn tuần trước nhiều rồi."),
    ("Let's take a short break.", "Mình nghỉ một chút nhé."),
    ("Please do these exercises at home, as shown on the sheet.", "Anh/chị tập các bài này ở nhà theo đúng tờ hướng dẫn nhé."),
    ("Up with the good leg, down with the bad.", "Lên cầu thang thì bước chân khỏe trước, xuống thì bước chân đau trước."),
    ("I'll stand next to you in case you lose your balance.", "Em sẽ đứng cạnh phòng khi anh/chị mất thăng bằng."),
   ],
   "dialogues": [
    ("This exercise hurts my knee.", [
      ("Thank you for telling me. Let's stop and try a smaller movement. How bad is the pain?", True, "Dừng khi đau + điều chỉnh động tác + đánh giá mức đau."),
      ("No pain, no gain! Keep going.", False, "Ép tập khi đau có thể gây chấn thương thêm."),
      ("Your knee is weak, is normal.", False, "Thiếu chủ ngữ ('it's normal') và bỏ qua lời báo đau."),
    ]),
    ("How long until I can walk without crutches?", [
      ("It depends on how your leg heals. The doctor and the physio will check your progress every week.", True, "Trung thực, không hứa mốc thời gian + nói rõ ai sẽ đánh giá."),
      ("Two weeks, sure.", False, "Hứa mốc thời gian khi chưa có đánh giá chuyên môn."),
      ("When you walk good, you can.", False, "Sai từ loại ('walk well') và không trả lời rõ."),
    ]),
    ("I'm tired. Can I skip today's session?", [
      ("I understand. How about a shorter session today? Even ten minutes will help.", True, "Đồng cảm + thương lượng nhẹ nhàng + động viên."),
      ("No, you must do. Doctor said.", False, "Ép buộc, thiếu tân ngữ ('do it') và mạo từ ('The doctor said so')."),
      ("OK, skip. No problem.", False, "Đồng ý ngay, không động viên — người bệnh dễ bỏ tập."),
    ]),
    ("Which hand should I hold the stick in?", [
      ("Hold it in the hand on your good side, opposite your weak leg. That gives you more support.", True, "Hướng dẫn đúng kỹ thuật + lý do ngắn gọn."),
      ("Any hand, same same.", False, "Sai kỹ thuật và dùng 'same same' kiểu tiếng bồi."),
      ("You hold right hand.", False, "Thiếu giới từ ('in your right hand') và không giải thích."),
    ]),
    ("I feel like I'm not getting better.", [
      ("I know it feels slow. But last week you walked ten metres, and today you walked twenty. That's real progress.", True, "Đồng cảm + dẫn chứng tiến bộ cụ thể."),
      ("You are lazy, so slow.", False, "Chê bai người bệnh, làm mất động lực."),
      ("Yes, you not better.", False, "Thiếu động từ ('you aren't getting better') và làm người bệnh nản."),
    ]),
   ],
   "listen": [
    ("Your physiotherapy session is at ten", ["physiotherapy", "ten"], "báo giờ tập"),
    ("Hold the chair if you lose your balance", ["chair", "balance"], "nhắc an toàn khi tập"),
    ("Lift your leg slowly and hold it", ["Lift", "slowly"], "hướng dẫn động tác"),
    ("Tell me if it hurts, and we'll stop", ["hurts", "stop"], "dừng khi đau"),
    ("Let's practise the stairs today. Up with the good leg, down with the bad. I'll stay close to you.", ["stairs", "good", "close"], "tập lên cầu thang với nạng"),
    ("You did very well today. Please do the exercises at home, as shown on this sheet. Stop if you feel any sharp pain.", ["well", "sheet", "sharp"], "dặn tập ở nhà"),
   ]},

  # ───────────────────────── Phòng mổ & chăm sóc sau mổ ─────────────────────────
  {"title": "Phòng mổ & chăm sóc sau mổ",
   "vocab": [
    ("operating theatre", "/ˈɒpəreɪtɪŋ ˌθɪətə/", "n", "phòng mổ", "We'll take you to the <b>operating theatre</b> at nine.", "Chín giờ bên em sẽ đưa anh/chị vào phòng mổ.", "手術室", "shujutsushitsu"),
    ("anaesthetic", "/ˌænəsˈθetɪk/", "n", "thuốc gây mê / gây tê", "You'll have a general <b>anaesthetic</b>, so you'll be asleep.", "Anh/chị sẽ được gây mê toàn thân nên sẽ ngủ trong lúc mổ.", "麻酔", "masui"),
    ("surgeon", "/ˈsɜːdʒən/", "n", "bác sĩ phẫu thuật", "The <b>surgeon</b> will explain the operation to you.", "Bác sĩ phẫu thuật sẽ giải thích ca mổ cho anh/chị.", "外科医", "gekai"),
    ("nil by mouth", "/ˌnɪl baɪ ˈmaʊθ/", "adj", "nhịn ăn uống hoàn toàn", "You're <b>nil by mouth</b> from midnight, so no food or drink.", "Từ nửa đêm anh/chị phải nhịn ăn uống hoàn toàn.", "絶飲食", "zetsuinshoku"),
    ("jewellery", "/ˈdʒuːəlri/", "n", "đồ trang sức", "Please take off all your <b>jewellery</b> before surgery.", "Anh/chị vui lòng tháo hết trang sức trước khi mổ."),
    ("recovery room", "/rɪˈkʌvəri ruːm/", "n", "phòng hồi tỉnh", "After the operation, you'll wake up in the <b>recovery room</b>.", "Sau ca mổ, anh/chị sẽ tỉnh dậy ở phòng hồi tỉnh.", "回復室", "kaifukushitsu"),
    ("drowsy", "/ˈdraʊzi/", "adj", "lơ mơ, buồn ngủ", "You may feel <b>drowsy</b> for a few hours.", "Anh/chị có thể thấy lơ mơ trong vài giờ."),
    ("stitches", "/ˈstɪtʃɪz/", "n", "mũi khâu, đường chỉ khâu", "Keep your <b>stitches</b> clean and dry.", "Anh/chị giữ vết khâu sạch và khô nhé."),
    ("drain", "/dreɪn/", "n", "ống dẫn lưu", "Please don't pull the <b>drain</b> when you move.", "Anh/chị cẩn thận đừng kéo ống dẫn lưu khi cử động nhé.", "ドレーン", "dorēn"),
    ("catheter", "/ˈkæθɪtə/", "n", "ống thông (thường là ống thông tiểu)", "You have a <b>catheter</b>, so you don't need to get up to pass urine.", "Anh/chị đang đặt ống thông tiểu nên không cần dậy đi tiểu.", "カテーテル", "katēteru"),
   ],
   "phrases": [
    ("Have you had anything to eat or drink since midnight?", "Từ nửa đêm đến giờ anh/chị có ăn uống gì không ạ?"),
    ("Please take off your jewellery, glasses and dentures.", "Anh/chị vui lòng tháo trang sức, kính và răng giả ra ạ."),
    ("Can you tell me which operation you're having today?", "Anh/chị cho em biết hôm nay mình mổ gì ạ?"),
    ("Can you show me which knee you're having the operation on?", "Anh/chị chỉ giúp em bên gối nào sẽ mổ ạ?"),
    ("The surgeon will mark the area with a pen.", "Bác sĩ phẫu thuật sẽ đánh dấu vị trí mổ bằng bút."),
    ("The operation is over. You're in the recovery room.", "Ca mổ xong rồi ạ. Anh/chị đang ở phòng hồi tỉnh."),
    ("Try to breathe deeply and cough gently.", "Anh/chị cố hít thở sâu và ho nhẹ nhé."),
    ("Hold a pillow on your tummy when you cough.", "Khi ho, anh/chị ôm gối áp vào bụng nhé."),
    ("Please don't get up alone the first time.", "Lần đầu đứng dậy, anh/chị đừng tự đứng lên một mình nhé."),
    ("Your family can see you once you're back on the ward.", "Người nhà có thể gặp anh/chị khi anh/chị về lại khoa."),
   ],
   "dialogues": [
    ("I had a small cup of coffee this morning. Is that a problem?", [
      ("Thank you for telling me. I need to let the surgeon and the anaesthetic team know right away.", True, "Cảm ơn + báo ngay ê-kíp — ăn uống trước mổ ảnh hưởng đến an toàn gây mê."),
      ("Coffee is only water, no problem.", False, "Sai nguy hiểm — việc ăn uống trước mổ phải được báo cho ê-kíp."),
      ("Why you drink? I told you!", False, "Sai cấu trúc ('Why did you drink it?') và trách móc bệnh nhân."),
    ]),
    ("Do I have to take off my wedding ring?", [
      ("Yes, please. All jewellery needs to come off for your safety. We can keep it safe for you or give it to your family.", True, "Xác nhận + lý do an toàn + phương án cất giữ."),
      ("Yes, take off, we keep.", False, "Câu cụt, thiếu tân ngữ ('take it off', 'we'll keep it')."),
      ("No, ring is small, no problem.", False, "Sai quy trình an toàn trước mổ."),
    ]),
    ("Where am I? Is it over?", [
      ("Yes, the operation is over. You're in the recovery room. I'm your nurse, and I'm right here.", True, "Trả lời rõ + định hướng + trấn an."),
      ("Yes. Sleep more.", False, "Quá cụt, chưa định hướng cho người bệnh."),
      ("Operation finish already one hour.", False, "Dịch từng chữ: 'The operation finished an hour ago.'"),
    ]),
    ("I feel sick after the operation.", [
      ("I'm sorry. That can happen after an anaesthetic. I'll tell the doctor, and I'll bring you a bowl.", True, "Đồng cảm + giải thích ngắn + báo bác sĩ + hỗ trợ ngay."),
      ("Don't vomit, it hurts the wound.", False, "Yêu cầu vô lý, không giúp được người bệnh."),
      ("Is normal, no worry.", False, "Thiếu chủ ngữ ('It's normal') và không báo bác sĩ."),
    ]),
    ("Can I get up and walk now?", [
      ("Not on your own yet. Let me check your blood pressure first, and then I'll help you sit up slowly.", True, "An toàn: kiểm tra trước + hỗ trợ từng bước (phòng choáng, ngã)."),
      ("Yes, walk to the toilet yourself.", False, "Nguy cơ choáng, ngã khi đứng dậy lần đầu sau mổ."),
      ("You cannot walk, you just operate.", False, "Sai: 'You've just had an operation' ('operate' là việc bác sĩ làm)."),
    ]),
   ],
   "listen": [
    ("You're nil by mouth from midnight", ["nil", "midnight"], "dặn nhịn ăn uống trước mổ"),
    ("Please take off all your jewellery", ["take", "jewellery"], "tháo trang sức"),
    ("You may feel drowsy for a few hours", ["drowsy", "hours"], "dặn sau gây mê"),
    ("Please don't pull the drain when you move", ["pull", "drain"], "cẩn thận ống dẫn lưu"),
    ("Your operation is at nine tomorrow. Please don't eat or drink after midnight. The surgeon will see you in the morning.", ["nine", "midnight", "surgeon"], "dặn trước ngày mổ"),
    ("The operation is over. You're in the recovery room now. Tell me if you have any pain.", ["over", "recovery", "pain"], "khi bệnh nhân tỉnh dậy"),
   ]},

  # ───────────────────────── Kiểm soát nhiễm khuẩn ─────────────────────────
  {"title": "Kiểm soát nhiễm khuẩn",
   "vocab": [
    ("hand hygiene", "/ˈhænd ˌhaɪdʒiːn/", "n", "vệ sinh tay", "Good <b>hand hygiene</b> stops infections from spreading.", "Vệ sinh tay tốt giúp ngăn nhiễm khuẩn lây lan.", "手指衛生", "shushi eisei"),
    ("gloves", "/ɡlʌvz/", "n", "găng tay", "Put on new <b>gloves</b> for each patient.", "Thay găng tay mới cho mỗi bệnh nhân.", "手袋", "tebukuro"),
    ("isolation", "/ˌaɪsəˈleɪʃn/", "n", "sự cách ly", "The patient in room 8 is in <b>isolation</b>.", "Bệnh nhân phòng 8 đang được cách ly.", "隔離", "kakuri"),
    ("infection", "/ɪnˈfekʃn/", "n", "sự nhiễm khuẩn, nhiễm trùng", "Redness and swelling can be signs of <b>infection</b>.", "Sưng đỏ có thể là dấu hiệu nhiễm trùng.", "感染", "kansen"),
    ("sanitiser", "/ˈsænɪtaɪzə/", "n", "dung dịch sát khuẩn tay", "There's hand <b>sanitiser</b> at the door of every room.", "Ở cửa mỗi phòng đều có dung dịch sát khuẩn tay."),
    ("contaminated", "/kənˈtæmɪneɪtɪd/", "adj", "bị nhiễm bẩn, nhiễm khuẩn", "Don't touch your face with <b>contaminated</b> gloves.", "Đừng chạm lên mặt khi đang đeo găng đã nhiễm bẩn."),
    ("sharps bin", "/ˈʃɑːps bɪn/", "n", "hộp đựng vật sắc nhọn", "Put used needles straight into the <b>sharps bin</b>.", "Bỏ kim đã dùng ngay vào hộp đựng vật sắc nhọn."),
    ("PPE", "/ˌpiː piː ˈiː/", "n", "phương tiện phòng hộ cá nhân (găng, khẩu trang, áo choàng…)", "Put on your <b>PPE</b> before you go into the room.", "Mặc đồ phòng hộ trước khi vào phòng.", "個人防護具", "kojin bōgogu"),
    ("disinfect", "/ˌdɪsɪnˈfekt/", "v", "khử khuẩn", "Please <b>disinfect</b> the bed rails after the patient leaves.", "Vui lòng khử khuẩn thanh chắn giường sau khi bệnh nhân rời đi.", "消毒する", "shōdoku suru"),
    ("needlestick injury", "/ˈniːdlstɪk ˌɪndʒəri/", "n", "tai nạn kim đâm", "Report any <b>needlestick injury</b> to your manager at once.", "Bị kim đâm thì phải báo ngay cho quản lý.", "針刺し事故", "harisashi jiko"),
   ],
   "phrases": [
    ("Please clean your hands before you go in.", "Anh/chị vui lòng sát khuẩn tay trước khi vào phòng ạ."),
    ("I'm just going to clean my hands first.", "Em sát khuẩn tay trước đã nhé."),
    ("This is an isolation room. Please wear a mask.", "Đây là phòng cách ly. Vui lòng đeo khẩu trang."),
    ("Visitors need to wear a gown and gloves in this room.", "Người thăm vào phòng này cần mặc áo choàng và đeo găng tay."),
    ("Please don't sit on the patient's bed.", "Vui lòng không ngồi lên giường bệnh nhân."),
    ("Never recap a used needle.", "Tuyệt đối không đậy nắp lại kim đã dùng."),
    ("Take off your gloves and clean your hands.", "Tháo găng rồi vệ sinh tay."),
    ("If you have a cough, please wear a mask in the waiting room.", "Nếu bị ho, anh/chị vui lòng đeo khẩu trang trong phòng chờ."),
    ("I'll clean the equipment before the next patient.", "Em sẽ lau khử khuẩn dụng cụ trước khi dùng cho bệnh nhân tiếp theo."),
   ],
   "dialogues": [
    ("Why do I have to wear a mask to visit my dad?", [
      ("It protects your dad and the other patients from infections. Thank you for helping us.", True, "Giải thích lý do ngắn gọn + cảm ơn sự hợp tác."),
      ("Because rule. Everybody wear.", False, "Thiếu 'it's the' và 's' ('everybody wears one'); không giải thích."),
      ("If you don't wear, go home.", False, "Đe dọa, thiếu tân ngữ ('wear one') và thiếu lịch sự."),
    ]),
    ("Nurse, did you clean your hands?", [
      ("Good question. Yes, but I'll clean them again now, in front of you. Thank you for asking.", True, "Đón nhận câu hỏi tích cực + vệ sinh tay trước mặt người bệnh."),
      ("Of course, you don't trust me?", False, "Phản ứng tự ái — nên khuyến khích người bệnh nhắc nhở."),
      ("I clean already, don't worry.", False, "Sai thì và thiếu tân ngữ: 'I've already cleaned them.'"),
    ]),
    ("I just got a needlestick from a used needle.", [
      ("Wash it with soap and running water now. Then report it to the manager straight away. I'll look after your patients.", True, "Sơ cứu đúng (rửa bằng xà phòng dưới vòi nước) + báo cáo ngay + hỗ trợ đồng nghiệp."),
      ("Small injury, forget it.", False, "Sai nguy hiểm — tai nạn kim đâm phải được xử lý và báo cáo ngay."),
      ("You not careful. Why you do that?", False, "Trách móc thay vì giúp; thiếu động từ và sai cấu trúc câu hỏi."),
    ]),
    ("Can I go into the isolation room without a gown? I'm only giving him water.", [
      ("I'm sorry, no. Everyone needs PPE in that room, even for a short visit. Let me help you put it on.", True, "Giữ nguyên tắc cách ly + giúp mặc đồ phòng hộ."),
      ("OK, quick quick, no problem.", False, "Bỏ qua nguyên tắc cách ly."),
      ("No gown, no enter.", False, "Dịch từng chữ, cộc lốc; không hướng dẫn gì thêm."),
    ]),
    ("There's blood on the floor near bed 5.", [
      ("Thanks. I'll put up a sign and clean it with the spill kit. Please don't walk through it.", True, "Cảnh báo + xử lý bằng bộ dụng cụ tràn đổ + nhắc an toàn cho người khác."),
      ("Wipe with tissue, finished.", False, "Không dùng đồ phòng hộ/dụng cụ xử lý máu tràn đổ; câu cụt."),
      ("Not my job, call cleaner.", False, "Đẩy trách nhiệm, thiếu mạo từ ('the cleaner')."),
    ]),
   ],
   "listen": [
    ("Put on new gloves for each patient", ["gloves", "patient"], "thay găng"),
    ("The patient in room eight is in isolation", ["eight", "isolation"], "phòng cách ly"),
    ("Put used needles into the sharps bin", ["needles", "sharps"], "bỏ kim đúng chỗ"),
    ("Please clean your hands before you go in", ["clean", "hands"], "nhắc vệ sinh tay"),
    ("Room eight is an isolation room. Please put on a gown, gloves and a mask. Clean your hands when you come out.", ["isolation", "mask", "hands"], "dặn trước khi vào phòng cách ly"),
    ("Good morning, everyone. Our hand hygiene score went down this month. Please clean your hands before and after every patient.", ["hygiene", "score", "patient"], "họp nhanh đầu ca về vệ sinh tay"),
   ]},

  # ───────────────────────── Chẩn đoán hình ảnh ─────────────────────────
  {"title": "Chẩn đoán hình ảnh",
   "vocab": [
    ("MRI", "/ˌem ɑːr ˈaɪ/", "n", "chụp cộng hưởng từ", "Your <b>MRI</b> will take about thirty minutes.", "Chụp cộng hưởng từ mất khoảng ba mươi phút."),
    ("CT scan", "/ˌsiː ˈtiː skæn/", "n", "chụp cắt lớp vi tính (CT)", "The doctor has booked you a <b>CT scan</b> of your chest.", "Bác sĩ đã đặt lịch chụp CT ngực cho anh/chị."),
    ("contrast dye", "/ˈkɒntrɑːst daɪ/", "n", "thuốc cản quang", "You may feel warm when the <b>contrast dye</b> goes in.", "Anh/chị có thể thấy người nóng lên khi thuốc cản quang được tiêm vào.", "造影剤", "zōeizai"),
    ("radiographer", "/ˌreɪdiˈɒɡrəfə/", "n", "kỹ thuật viên chẩn đoán hình ảnh", "The <b>radiographer</b> will help you onto the table.", "Kỹ thuật viên sẽ giúp anh/chị lên bàn chụp.", "診療放射線技師", "shinryō hōshasen gishi"),
    ("radiologist", "/ˌreɪdiˈɒlədʒɪst/", "n", "bác sĩ chẩn đoán hình ảnh", "A <b>radiologist</b> will read your images and send a report.", "Bác sĩ chẩn đoán hình ảnh sẽ đọc phim và gửi kết quả.", "放射線科医", "hōshasenkai"),
    ("radiation", "/ˌreɪdiˈeɪʃn/", "n", "tia xạ, bức xạ", "An X-ray uses a very small amount of <b>radiation</b>.", "Chụp X-quang dùng một lượng tia xạ rất nhỏ.", "放射線", "hōshasen"),
    ("metal implant", "/ˌmetl ˈɪmplɑːnt/", "n", "vật cấy ghép kim loại (nẹp, vít…)", "Do you have any <b>metal implants</b> in your body?", "Trong người anh/chị có vật cấy ghép kim loại nào không ạ?"),
    ("pacemaker", "/ˈpeɪsmeɪkə/", "n", "máy tạo nhịp tim", "Please tell us if you have a <b>pacemaker</b>.", "Anh/chị vui lòng báo nếu có đặt máy tạo nhịp tim.", "ペースメーカー", "pēsumēkā"),
    ("claustrophobic", "/ˌklɔːstrəˈfəʊbɪk/", "adj", "sợ không gian hẹp, kín", "Some people feel <b>claustrophobic</b> in the MRI machine.", "Một số người thấy sợ khi nằm trong máy cộng hưởng từ."),
    ("lie still", "/ˌlaɪ ˈstɪl/", "v", "nằm yên", "Please <b>lie still</b> while the machine takes the pictures.", "Anh/chị nằm yên trong lúc máy chụp nhé."),
   ],
   "phrases": [
    ("Could you change into a gown and remove anything metal?", "Anh/chị thay áo choàng và tháo mọi đồ kim loại ra giúp em nhé."),
    ("Please take off your watch and earrings.", "Anh/chị tháo đồng hồ và hoa tai ra giúp em nhé."),
    ("Have you ever had surgery with metal plates or screws?", "Anh/chị đã từng mổ có đặt nẹp hay vít kim loại chưa ạ?"),
    ("Have you ever had a reaction to contrast dye?", "Anh/chị đã từng bị phản ứng với thuốc cản quang chưa ạ?"),
    ("The machine is quite noisy. Here are some earplugs.", "Máy chụp khá ồn. Đây là nút bịt tai cho anh/chị."),
    ("You can talk to us through the microphone at any time.", "Anh/chị có thể nói chuyện với bên em qua micro bất cứ lúc nào."),
    ("Press this button if you need to stop.", "Bấm nút này nếu anh/chị cần dừng lại."),
    ("Take a breath in and hold it… now breathe normally.", "Hít vào và nín thở… giờ thở bình thường ạ."),
    ("It's all finished. You can get dressed now.", "Xong rồi ạ. Anh/chị có thể thay đồ."),
    ("The doctor will explain the results at your next appointment.", "Bác sĩ sẽ giải thích kết quả ở lần hẹn tới."),
   ],
   "dialogues": [
    ("I have a metal plate in my leg. Is that OK for the MRI?", [
      ("Thank you for telling me. I'll check with the radiographer before we start. Do you know when it was put in?", True, "Ghi nhận + kiểm tra với kỹ thuật viên — kim loại trong người là vấn đề an toàn khi chụp MRI."),
      ("No problem, metal is OK.", False, "Khẳng định sai — mọi kim loại trong người phải được kiểm tra trước khi chụp MRI."),
      ("Metal? You cannot MRI.", False, "Dùng 'MRI' làm động từ ('have an MRI') và tự kết luận thay chuyên môn."),
    ]),
    ("I'm scared of small spaces.", [
      ("That's very common. You can talk to us through the microphone, and you can press the button to stop at any time.", True, "Bình thường hóa nỗi sợ + cho người bệnh cảm giác được kiểm soát."),
      ("Close your eyes, it's nothing.", False, "Gạt đi nỗi sợ, không đưa hỗ trợ cụ thể."),
      ("Why you scared? Machine is safe.", False, "Thiếu 'are' và mạo từ ('The machine'); không đồng cảm."),
    ]),
    ("I'm pregnant. Is the X-ray safe for my baby?", [
      ("Thank you for telling me. I'll let the doctor and the radiographer know before we do anything.", True, "Dừng lại + báo bác sĩ/kỹ thuật viên — không tự trả lời vấn đề an toàn thai kỳ."),
      ("X-ray is very small, no problem.", False, "Tự trấn an ngoài phạm vi chuyên môn — phải để bác sĩ quyết định."),
      ("You pregnant? Why you not say before?", False, "Thiếu 'are', sai cấu trúc ('Why didn't you tell us?') và trách móc."),
    ]),
    ("When will I get the results of my scan?", [
      ("A radiologist will read the images and send a report to your doctor. Your doctor will go over it with you.", True, "Giải thích quy trình + đúng người trả kết quả."),
      ("I see the images, everything is fine.", False, "Kỹ thuật viên/điều dưỡng không tự đọc kết quả; sai thì ('I saw')."),
      ("Results? Tomorrow or next week, maybe.", False, "Mơ hồ, không nói ai sẽ báo kết quả."),
    ]),
    ("The injection feels warm. Is something wrong?", [
      ("That warm feeling is common with contrast dye, and it goes away quickly. But tell me straight away if you feel itchy or short of breath.", True, "Giải thích + dặn dấu hiệu phản ứng cần báo ngay."),
      ("Don't move! Don't talk!", False, "Ra lệnh mà không trả lời câu hỏi của người bệnh."),
      ("Warm is normal, sleep.", False, "Câu cụt, không dặn dấu hiệu nguy hiểm."),
    ]),
   ],
   "listen": [
    ("Please lie still while the machine takes pictures", ["lie", "pictures"], "dặn nằm yên"),
    ("Do you have any metal implants", ["metal", "implants"], "hỏi kim loại trong người"),
    ("Your MRI will take about thirty minutes", ["MRI", "thirty"], "thời gian chụp"),
    ("Please tell us if you have a pacemaker", ["tell", "pacemaker"], "hỏi máy tạo nhịp tim"),
    ("The machine is quite noisy. Here are some earplugs. You can talk to us through the microphone at any time.", ["noisy", "earplugs", "microphone"], "trước khi chụp MRI"),
    ("I'm going to give you the contrast dye now. You may feel warm for a moment. Tell me if you feel itchy.", ["contrast", "warm", "itchy"], "tiêm thuốc cản quang"),
   ]},

  # ───────────────────────── Xuất viện & theo dõi tại nhà ─────────────────────────
  {"title": "Xuất viện & theo dõi tại nhà",
   "vocab": [
    ("follow-up", "/ˈfɒləʊ ʌp/", "n", "lần tái khám, theo dõi sau điều trị", "Your <b>follow-up</b> appointment is next Tuesday.", "Lịch tái khám của anh/chị là thứ Ba tuần sau."),
    ("discharge summary", "/ˈdɪstʃɑːdʒ ˌsʌməri/", "n", "bản tóm tắt ra viện", "Please give this <b>discharge summary</b> to your family doctor.", "Anh/chị đưa bản tóm tắt ra viện này cho bác sĩ gia đình nhé.", "退院サマリー", "taiin samarī"),
    ("warning signs", "/ˈwɔːnɪŋ saɪnz/", "n", "dấu hiệu cảnh báo", "If you notice any of these <b>warning signs</b>, come back straight away.", "Nếu thấy bất kỳ dấu hiệu cảnh báo nào trong số này, anh/chị quay lại viện ngay."),
    ("home care", "/ˌhəʊm ˈkeə/", "n", "chăm sóc tại nhà", "We can arrange <b>home care</b> for the first two weeks.", "Bên em có thể sắp xếp chăm sóc tại nhà trong hai tuần đầu.", "在宅ケア", "zaitaku kea"),
    ("caregiver", "/ˈkeəɡɪvə/", "n", "người chăm sóc (thường là người nhà)", "Who will be your main <b>caregiver</b> at home?", "Ở nhà ai sẽ là người chăm sóc chính cho anh/chị ạ?", "介護者", "kaigosha"),
    ("heal", "/hiːl/", "v", "lành (vết thương)", "The wound is <b>healing</b> well.", "Vết thương đang lành tốt."),
    ("worsen", "/ˈwɜːsn/", "v", "nặng hơn, xấu đi", "Call us if the pain <b>worsens</b>.", "Gọi cho bên em nếu cơn đau nặng hơn."),
    ("home visit", "/ˌhəʊm ˈvɪzɪt/", "n", "buổi thăm khám tại nhà", "The community nurse will make a <b>home visit</b> on Friday.", "Thứ Sáu điều dưỡng cộng đồng sẽ đến thăm khám tại nhà."),
    ("blood sugar", "/ˈblʌd ˌʃʊɡə/", "n", "đường huyết", "Please check your <b>blood sugar</b> as the doctor told you.", "Anh/chị đo đường huyết theo đúng lời bác sĩ dặn nhé.", "血糖", "kettō"),
    ("repeat prescription", "/rɪˌpiːt prɪˈskrɪpʃn/", "n", "đơn thuốc kê lại (cho thuốc dùng lâu dài)", "You can ask your family doctor for a <b>repeat prescription</b>.", "Anh/chị có thể xin bác sĩ gia đình kê lại đơn thuốc."),
   ],
   "phrases": [
    ("The doctor says you can go home today.", "Bác sĩ nói hôm nay anh/chị được về nhà rồi ạ."),
    ("Let's go through your discharge papers together.", "Mình cùng xem lại giấy tờ ra viện nhé."),
    ("Here's a list of your medicines. Please take them as prescribed.", "Đây là danh sách thuốc của anh/chị. Anh/chị dùng đúng theo đơn nhé."),
    ("Keep the wound clean and dry.", "Giữ vết thương sạch và khô."),
    ("Come back straight away if you have a fever or bleeding.", "Nếu sốt hoặc chảy máu, anh/chị quay lại viện ngay nhé."),
    ("Your follow-up appointment is on this card.", "Lịch tái khám có ghi trên thẻ này ạ."),
    ("Who will help you at home?", "Ở nhà ai sẽ giúp anh/chị ạ?"),
    ("Can you tell me in your own words how you'll look after the wound?", "Anh/chị nói lại theo cách của mình xem sẽ chăm sóc vết thương thế nào nhé?"),
    ("If you're not sure about anything, call this number.", "Nếu có gì chưa rõ, anh/chị gọi số này nhé."),
    ("We'll call you in two days to see how you're doing.", "Hai ngày nữa bên em sẽ gọi hỏi thăm anh/chị."),
   ],
   "dialogues": [
    ("Can I have a shower with this wound?", [
      ("Please follow the instructions on your discharge sheet. If you're not sure, I'll check with the doctor before you leave.", True, "Dựa vào hướng dẫn ra viện + hỏi bác sĩ khi chưa chắc."),
      ("Yes, shower, swim, everything OK.", False, "Tự cho phép khi chưa kiểm tra — vết thương có thể bị nhiễm trùng."),
      ("No water forever.", False, "Hướng dẫn sai và cực đoan; nên theo chỉ dẫn của bác sĩ."),
    ]),
    ("What should I do if the pain gets worse at home?", [
      ("Take your pain medicine as it says on the label. If the pain still gets worse, or you get a fever, call us or come back.", True, "Theo nhãn thuốc + nói rõ khi nào cần gọi hoặc quay lại."),
      ("Take more tablets, it's OK.", False, "Nguy hiểm — khuyến khích dùng quá liều."),
      ("Pain is normal, you just wait.", False, "Coi nhẹ triệu chứng, không nêu dấu hiệu cần quay lại."),
    ]),
    ("I think I understand. Can I go now?", [
      ("Almost. Just to be sure, can you tell me the warning signs we talked about?", True, "Hỏi lại để chắc người bệnh đã hiểu (phương pháp 'teach-back')."),
      ("Yes, bye bye.", False, "Không kiểm tra người bệnh đã hiểu hướng dẫn chưa."),
      ("You understand everything, right? OK go.", False, "Hỏi kiểu 'hiểu hết rồi chứ?' khiến người bệnh ngại hỏi lại; 'OK go' cộc lốc."),
    ]),
    ("Who can I call if I have questions at home?", [
      ("You can call the ward on this number at any time. It's also on your discharge sheet.", True, "Cho số liên lạc cụ thể + chỉ nơi có ghi lại."),
      ("Call hospital, somebody answer.", False, "Thiếu mạo từ, sai thì ('someone will answer') và không cho số cụ thể."),
      ("Don't call, come to hospital.", False, "Cộc và không hợp lý — nên cho số điện thoại hỗ trợ."),
    ]),
    ("My mother is going home tomorrow. What do I need to know?", [
      ("I'll go through her medicines, her wound care and the warning signs with you. Do you have time this afternoon?", True, "Lên kế hoạch hướng dẫn người chăm sóc + hỏi thời gian phù hợp."),
      ("Nothing, she is OK now.", False, "Bỏ qua việc hướng dẫn người chăm sóc — dễ dẫn đến phải nhập viện lại."),
      ("You read paper, all there.", False, "Thiếu mạo từ/động từ ('It's all on the paper') và đẩy việc cho người nhà tự đọc."),
    ]),
   ],
   "listen": [
    ("Your follow-up appointment is next Tuesday", ["follow-up", "Tuesday"], "lịch tái khám"),
    ("Keep the wound clean and dry", ["clean", "dry"], "chăm sóc vết thương"),
    ("Call us if the pain worsens", ["Call", "worsens"], "khi nào gọi lại"),
    ("Who will be your main caregiver at home", ["main", "caregiver"], "hỏi người chăm sóc"),
    ("You can go home today. Here are your medicines and your discharge summary. Please come back if you have a fever.", ["home", "summary", "fever"], "dặn khi ra viện"),
    ("Hello, this is Mai from Ward 5. I'm calling to see how you're doing at home. Is the wound healing well?", ["calling", "home", "healing"], "gọi điện theo dõi sau ra viện"),
   ]},
 ],

 "rev": [
  ("Bé nhà mình mấy tuổi rồi ạ?", "How old is your child?"),
  ("Con dũng cảm lắm!", "You were so brave!"),
  ("Bé đã tiêm đủ các mũi chưa ạ?", "Has your child had all the vaccinations?"),
  ("Bác nghe cháu nói rõ không ạ?", "Can you hear me clearly?"),
  ("Cháu sẽ xoay bác nằm nghiêng nhé.", "I'm going to turn you onto your side."),
  ("Anh/chị có bị khó nuốt không ạ?", "Do you have any trouble swallowing?"),
  ("Anh/chị ngồi thẳng lưng khi ăn nhé.", "Please sit up straight while you eat."),
  ("Nếu đau thì báo em, mình sẽ dừng.", "Tell me if it hurts, and we'll stop."),
  ("Anh/chị cầm gậy ở tay bên khỏe nhé.", "Hold the stick in your good hand."),
  ("Sau nửa đêm anh/chị đừng ăn uống gì nhé.", "Please don't eat or drink after midnight."),
  ("Anh/chị vui lòng tháo hết trang sức ra ạ.", "Please take off all your jewellery."),
  ("Em sát khuẩn tay trước đã nhé.", "Let me clean my hands first."),
  ("Anh/chị nằm yên nhé.", "Please lie still."),
  ("Trong người anh/chị có kim loại không ạ?", "Do you have any metal in your body?"),
  ("Lịch tái khám của anh/chị là thứ Ba tuần sau.", "Your follow-up is next Tuesday."),
  ("Nếu bị sốt, anh/chị quay lại viện ngay nhé.", "If you get a fever, please come back straight away."),
 ],

 "reading": [
  {"t": "Vaccination reminder", "text": "SEN XANH CLINIC – Child Health\nDear parent,\nYour child, Mia (2 years), is due for her next vaccination.\nDate: Saturday 14 March, 9:00–11:00 a.m.\nPlease bring her vaccination book.\nIf she has a fever on the day, please call us to change the date.\nTel: 028 3812 4567", "q": [
    {"q": "What should the parent bring?", "o": ["Her passport", "Her vaccination book", "A blood test result"], "a": 1},
    {"q": "What should the parent do if Mia has a fever that day?", "o": ["Call to change the date", "Come earlier", "Give her some medicine first"], "a": 0}]},
  {"t": "Isolation room sign", "text": "STOP – ISOLATION ROOM\nAll staff and visitors must:\n• Clean hands before entering and after leaving\n• Wear a gown, gloves and a mask\n• Speak to the nurse before entering\nNo children under 12.\nPlease do not bring food or flowers into this room.", "q": [
    {"q": "What must visitors do before they go in?", "o": ["Speak to the nurse", "Bring some flowers", "Take off their mask"], "a": 0},
    {"q": "Who cannot visit this room?", "o": ["Nurses", "Adult visitors", "Children under 12"], "a": 2}]},
  {"t": "MRI appointment letter", "text": "Dear Mr Garcia,\nYour MRI scan of the knee is booked for Monday 9 June at 2:30 p.m., Imaging Department, Ground Floor.\n• Please arrive 20 minutes early to fill in a safety form.\n• You can eat and drink as normal.\n• Tell us before your visit if you have a pacemaker or any metal in your body.\n• The scan takes about 30 minutes.\nImaging Department – An Tâm Hospital", "q": [
    {"q": "Why should Mr Garcia arrive early?", "o": ["To pay the bill", "To fill in a safety form", "To see the surgeon"], "a": 1},
    {"q": "What must he tell the hospital before his visit?", "o": ["If he has a pacemaker or metal in his body", "What he ate for lunch", "His blood pressure"], "a": 0}]},
  {"t": "Discharge instructions", "text": "Patient: Mr Okada   Ward 5\nGoing home: 12 May\n• Keep the wound clean and dry. Stitches out at the clinic on 20 May.\n• Take your medicines as shown on the labels.\n• Walk a little every day. No heavy lifting for 6 weeks.\n• Call 028 3812 7000 or come back if you have a fever, bleeding, or redness around the wound.\nFollow-up with Dr Hanh: 26 May, 9 a.m.", "q": [
    {"q": "When will the stitches come out?", "o": ["12 May", "20 May", "26 May"], "a": 1},
    {"q": "Which of these is a warning sign?", "o": ["Feeling a little tired", "Walking every day", "Redness around the wound"], "a": 2}]},
  {"t": "Patient diet card", "text": "WARD 3 – PATIENT DIET CARD\nBed 12: Mrs Nguyen Thi Lan\nDiet: soft, low-salt\nDrinks: thickened (see care plan)\nAllergy: peanuts\nAssistance: needs help to eat. Sit her upright. Stay with her during meals.\nRecord all food and drinks on the food chart.", "q": [
    {"q": "What is Mrs Lan allergic to?", "o": ["Milk", "Salt", "Peanuts"], "a": 2},
    {"q": "What should staff do at mealtimes?", "o": ["Stay with her while she eats", "Leave the tray and come back later", "Give her extra salt"], "a": 0}]},
 ],

 "ai": [
  ("child", "Khám cho trẻ nhỏ", "You are the worried parent of a 3-year-old with a fever and a rash. I am the nurse. Answer my questions about when it started, eating, drinking and vaccinations. Ask if your child needs to see the doctor today."),
  ("elderly", "Chăm sóc người cao tuổi", "You are an 82-year-old resident in a care home. You are a little hard of hearing and sometimes forget things. I am your carer. Ask me the same question twice, and ask for help with your hearing aid."),
  ("preop", "Chuẩn bị trước mổ", "You are a patient having knee surgery tomorrow. I am the nurse doing the pre-op check. Answer my questions about eating, jewellery and allergies. Ask what will happen when you wake up."),
  ("goinghome", "Hướng dẫn ra viện", "You are a patient going home after surgery. I am the nurse giving discharge instructions. Ask about the wound, having a shower and your follow-up. When I ask, repeat the warning signs back to me, but forget one."),
 ],

 "events": [
  ("vaccine", "Ngày tiêm chủng cho trẻ", "You are a parent bringing a baby to a vaccination day at the clinic. I am the nurse. Ask me which vaccine it is, whether it will hurt, and what to watch for at home."),
  ("abroad", "Ngày đầu làm việc ở nước ngoài", "You are a senior nurse at a hospital or care home abroad, showing me around on my first day. Explain the daily routine briefly, then ask me about my experience and what I need help with."),
  ("outbreak", "Họp phòng chống dịch trong khoa", "You are the infection control nurse running a short ward meeting about a flu outbreak. Ask me how I use PPE, when I clean my hands and what I tell visitors."),
 ],

 "quips": [
  "Gloves on, let's go!",
  "Clean hands, happy patients!",
  "Nil by mouth… but I'm hungry!",
  "Lie still… almost done!",
  "One more step, you've got this!",
  "Such a brave little patient!",
 ],

 "roles": {
  "nurse": {
   "scenarios": [
    ("ns_postop", "Bệnh nhân vừa mổ xong", "You are a patient who has just come back to the ward after an operation. You feel sleepy and a little sick, and you want to get up to use the toilet. I am your nurse."),
    ("ns_isolation", "Người nhà vào phòng cách ly", "You are a visitor who wants to go into an isolation room quickly without a gown or mask. I am the nurse. Argue a little, then agree if I explain kindly."),
   ],
   "dialogues": [
    ("Can you take this bandage off? It's itchy.", [
      ("I'm sorry it's itchy. Please try not to scratch it. Let me take a look, and I'll ask the doctor if we can change it.", True, "Đồng cảm + dặn không gãi + kiểm tra + hỏi bác sĩ."),
      ("OK, I take off now.", False, "Tự ý tháo băng khi chưa có chỉ định; thiếu 'will' và tân ngữ ('I'll take it off')."),
      ("Itchy is good, mean healing.", False, "Thiếu chủ ngữ/động từ ('It means it's healing') và tự kết luận."),
    ]),
    ("My father pulled out his drip. He's confused.", [
      ("Thank you for telling me. I'm coming now. I'll stop the bleeding, check that he's safe and then tell the doctor.", True, "Đến ngay + điều dưỡng tự cầm máu, kiểm tra an toàn người bệnh + báo bác sĩ."),
      ("Why you let him do that?", False, "Trách người nhà; sai cấu trúc câu hỏi ('Why did you let him…?')."),
      ("No problem, I put again later.", False, "Chậm xử lý; thiếu 'will' và tân ngữ ('I'll put it back')."),
    ]),
    ("I don't want the injection. I'm scared of needles.", [
      ("It's OK to feel scared. Can you tell me what worries you? I'll explain why the doctor ordered it, and then you can decide.", True, "Công nhận cảm xúc + giải thích + tôn trọng quyền quyết định của người bệnh."),
      ("You must have it, doctor said.", False, "Ép buộc — người bệnh có quyền được giải thích và từ chối; thiếu mạo từ ('the doctor')."),
      ("Needle small, not hurt.", False, "Thiếu động từ ('It's a small needle') và hứa không đau là không trung thực."),
    ]),
    ("Can you tell me my blood test results?", [
      ("The doctor will go through them with you on the ward round this morning. I'll remind her that you're waiting.", True, "Không tự giải thích kết quả + nói khi nào bác sĩ báo + nhắc bác sĩ giúp."),
      ("I saw them. Your sugar a bit high.", False, "Thiếu 'is' và điều dưỡng không nên tự giải thích kết quả thay bác sĩ."),
      ("Not my job, sorry.", False, "Đẩy trách nhiệm; nên cho biết khi nào bác sĩ sẽ báo kết quả."),
    ]),
   ]},
  "reception": {
   "scenarios": [
    ("rc_child", "Phụ huynh gọi vì con sốt", "You are a parent calling the clinic because your 2-year-old has had a fever since last night. I am the receptionist. Ask if you can come today and what to bring."),
    ("rc_followup", "Đặt lịch tái khám sau ra viện", "You are a patient who left hospital last week. Call the clinic to book a follow-up appointment and ask for a copy of your discharge summary."),
   ],
   "dialogues": [
    ("Do I need to bring my son's vaccination book?", [
      ("Yes, please. The nurse will check which vaccinations he's had.", True, "Xác nhận + lý do rõ ràng."),
      ("Yes, bring book.", False, "Câu cụt, thiếu 'please' và 'his'."),
      ("Book not important.", False, "Sai thông tin và thiếu động từ ('isn't')."),
    ]),
    ("My baby is only three months old and has a fever. Can we come now?", [
      ("Yes, please come now. I'll tell the nurse you're coming so she can see your baby first.", True, "Không hẹn muộn — trẻ nhỏ như vậy bị sốt cần được xem ngay; báo điều dưỡng ưu tiên."),
      ("Next appointment is Friday.", False, "Hẹn muộn với trẻ nhỏ đang sốt là không an toàn."),
      ("Give baby medicine and wait.", False, "Lễ tân không được khuyên dùng thuốc qua điện thoại."),
    ]),
    ("I left hospital last week. Can I have a copy of my discharge summary?", [
      ("Of course. May I see your ID first? Then I'll print a copy for you.", True, "Xác minh danh tính trước khi đưa hồ sơ + đáp ứng yêu cầu."),
      ("Sure, what name? I print now.", False, "Không xác minh danh tính; thiếu 'will' ('I'll print it')."),
      ("No, you already have it.", False, "Từ chối không lý do — người bệnh có quyền xin bản sao hồ sơ của mình."),
    ]),
    ("Is there a female doctor for children? My daughter is shy.", [
      ("Let me check. Dr Anna is free at 3 p.m. today. Would you like me to book her?", True, "Tôn trọng mong muốn + kiểm tra + đưa lựa chọn cụ thể."),
      ("Doctor is doctor, no matter.", False, "Gạt bỏ mong muốn chính đáng của phụ huynh."),
      ("Woman doctor not have today.", False, "Dịch từng chữ: 'There's no female doctor today.'"),
    ]),
   ]},
  "pharmacy": {
   "scenarios": [
    ("ph_child", "Mua thuốc cho trẻ em", "You are a parent asking for fever medicine for your 4-year-old. I am the pharmacy staff. Answer my questions about her age, weight and allergies, and ask how much to give."),
    ("ph_refill", "Hết thuốc dùng lâu dài", "You are an expat who has run out of your regular blood pressure medicine and has no new prescription. Ask me to sell you more, and accept my advice if I explain kindly."),
   ],
   "dialogues": [
    ("How much of this syrup should I give my daughter?", [
      ("For children, it depends on age and weight. May I ask how much she weighs? The pharmacist will then go through the label with you.", True, "Không tự đưa liều + liều trẻ em tính theo tuổi/cân nặng + dược sĩ hướng dẫn."),
      ("One big spoon, like adult.", False, "Nguy hiểm — liều trẻ em khác người lớn."),
      ("Give when she cry.", False, "Sai chia ('cries') và không hướng dẫn theo nhãn."),
    ]),
    ("I've run out of my blood pressure tablets. Can I buy more without a prescription?", [
      ("I'm sorry, we need a prescription for this medicine. There's a clinic next door, and they can see you today.", True, "Tuân thủ quy định + hướng giải quyết ngay trong ngày."),
      ("Sure, how many boxes?", False, "Bán thuốc kê đơn khi không có đơn là sai quy định."),
      ("No prescription, you stop the medicine.", False, "Khuyên ngừng thuốc huyết áp là nguy hiểm."),
    ]),
    ("Can I give my son my own cough medicine?", [
      ("Please don't. Some adult medicines aren't safe for children. Let me ask you a few questions, and the pharmacist can suggest something for his age.", True, "Cảnh báo an toàn + hỏi thông tin + để dược sĩ tư vấn."),
      ("Yes, half is OK for kids.", False, "Nguy hiểm — không tự chia liều thuốc người lớn cho trẻ."),
      ("Cough medicine all same.", False, "Thiếu động từ ('are all the same') và sai thông tin."),
    ]),
    ("Do you have gloves and hand sanitiser?", [
      ("Yes, they're in aisle two, next to the masks. I'll show you.", True, "Chỉ vị trí cụ thể + đề nghị dẫn đi."),
      ("Have, over there.", False, "Thiếu chủ ngữ và tân ngữ: 'Yes, we have them.'"),
      ("Sanitiser finish already.", False, "Dịch từng chữ 'hết rồi': 'Sorry, we've run out of sanitiser.'"),
    ]),
   ]},
  "care": {
   "scenarios": [
    ("cr_dementia", "Người sa sút trí tuệ đòi về nhà", "You are an elderly resident with dementia who keeps asking to go home to see your mother. I am your carer. Stay upset unless I am calm, kind and gently change the topic."),
    ("cr_meal", "Hỗ trợ bữa ăn", "You are an elderly patient with swallowing problems. I am helping you eat lunch. Say the food is too thick, and cough once while drinking."),
   ],
   "dialogues": [
    ("Can you take my dentures out? They hurt.", [
      ("Of course. Let me help you take them out, and I'll check your mouth for any sore spots. I'll tell the nurse too.", True, "Đáp ứng + kiểm tra miệng + báo điều dưỡng."),
      ("Dentures always hurt, is normal.", False, "Thiếu chủ ngữ ('it's normal') và coi nhẹ lời than phiền."),
      ("You take out yourself.", False, "Thiếu tân ngữ ('take them out') và bỏ mặc người bệnh."),
    ]),
    ("I've had an accident. I'm so embarrassed.", [
      ("It's OK, please don't worry. It happens. I'll close the curtain and help you get clean and comfortable.", True, "Giữ thể diện + riêng tư + hỗ trợ ngay."),
      ("Again? Why you not call me?", False, "Trách móc; sai cấu trúc câu hỏi ('Why didn't you call me?')."),
      ("Next time wear diaper.", False, "Thiếu mạo từ và làm người cao tuổi xấu hổ thêm."),
    ]),
    ("Can I go for a walk outside?", [
      ("Of course. Let's get your walking frame and your jacket. I'll walk with you.", True, "Đáp ứng + chuẩn bị dụng cụ + đi cùng để phòng ngã."),
      ("Outside is dangerous, stay here.", False, "Hạn chế không cần thiết, thiếu tôn trọng."),
      ("OK, you go, I busy.", False, "Thiếu 'am' và để người có nguy cơ ngã đi một mình."),
    ]),
    ("I don't like that new medicine. Can you throw it away?", [
      ("I understand. I can't throw it away, but I'll tell the nurse how you feel, and she can talk to the doctor.", True, "Tôn trọng ý kiến + đúng phạm vi của hộ lý + chuyển điều dưỡng."),
      ("OK, I throw away for you.", False, "Tự ý bỏ thuốc là vi phạm an toàn; thiếu 'will' và tân ngữ."),
      ("You must take, no choice.", False, "Ép buộc, thiếu tân ngữ ('take it') và không lắng nghe."),
    ]),
   ]},
 },
}
