# -*- coding: utf-8 -*-
# Gói "legal" — Luật · Hành chính công: pháp chế doanh nghiệp FDI, trợ lý công ty luật, cán bộ một cửa,
# phiên dịch / dịch thuật công chứng, nhân sự làm hồ sơ (visa, giấy phép lao động, đăng ký doanh nghiệp).
# Người đối diện: khách hàng nước ngoài, luật sư nước ngoài, người nước ngoài làm thủ tục.
# Nội dung cố ý KHÔNG khẳng định điều luật / mức phí / thời hạn cụ thể — nói chung "theo quy định hiện hành".
# Tên người / công ty đều tự đặt. Chặng lõi lấy từ office: 6 (Nhờ giúp & hỏi lại cho rõ), 3 (Email công việc).
# Schema: xem packs_src/README.md. Build: python3 packs_src/build.py legal

PHASES = []

# ───────────────────────── 0. Tiếp nhận hồ sơ một cửa ─────────────────────────
PHASES.append({
 "title": "Tiếp nhận hồ sơ một cửa",
 "vocab": [
  ("application form", "/ˌæplɪˈkeɪʃn ˌfɔːm/", "n", "tờ khai, đơn đề nghị", "Please fill in the <b>application form</b> in English or Vietnamese.", "Vui lòng điền tờ khai bằng tiếng Anh hoặc tiếng Việt.", "申請書", "shinseisho"),
  ("one-stop shop", "/ˌwʌn stɒp ˈʃɒp/", "n", "bộ phận một cửa (nơi nhận và trả hồ sơ)", "You can submit your papers at the <b>one-stop shop</b> on the ground floor.", "Anh có thể nộp giấy tờ ở bộ phận một cửa tầng trệt."),
  ("queue number", "/ˈkjuː ˌnʌmbə/", "n", "số thứ tự (chờ gọi)", "Please take a <b>queue number</b> and wait until it appears on the screen.", "Vui lòng lấy số thứ tự và chờ đến khi số hiện trên màn hình.", "整理番号", "seiri bangō"),
  ("dossier", "/ˈdɒsieɪ/", "n", "bộ hồ sơ", "Your <b>dossier</b> needs one more document.", "Bộ hồ sơ của anh cần thêm một giấy tờ nữa."),
  ("original", "/əˈrɪdʒənl/", "n", "bản gốc", "Please bring the <b>original</b> so I can compare it with the copy.", "Vui lòng mang bản gốc để tôi đối chiếu với bản sao.", "原本", "genpon"),
  ("photocopy", "/ˈfəʊtəʊkɒpi/", "n", "bản photo", "We need two <b>photocopies</b> of your passport.", "Chúng tôi cần hai bản photo hộ chiếu của anh.", "コピー", "kopī"),
  ("missing", "/ˈmɪsɪŋ/", "adj", "bị thiếu", "Your photo is <b>missing</b> from the form.", "Tờ khai của anh còn thiếu ảnh."),
  ("receipt", "/rɪˈsiːt/", "n", "giấy biên nhận (hồ sơ)", "Keep this <b>receipt</b>. You need it to collect the result.", "Giữ giấy biên nhận này. Anh cần nó để nhận kết quả.", "受付票", "uketsukehyō"),
  ("processing time", "/ˈprəʊsesɪŋ ˌtaɪm/", "n", "thời gian xử lý (hồ sơ)", "The <b>processing time</b> is written on your receipt.", "Thời gian xử lý được ghi trên giấy biên nhận của anh."),
  ("collect", "/kəˈlekt/", "v", "nhận, lấy (kết quả)", "You can <b>collect</b> the result at counter 3.", "Anh có thể nhận kết quả ở quầy số 3."),
 ],
 "phrases": [
  ("Good morning. How can I help you today?", "Chào anh/chị. Hôm nay tôi có thể giúp gì ạ?"),
  ("Please take a number and wait for your turn.", "Vui lòng lấy số và chờ đến lượt."),
  ("What kind of application are you making?", "Anh/chị đang làm thủ tục gì ạ?"),
  ("May I see your passport, please?", "Cho tôi xem hộ chiếu được không ạ?"),
  ("Your file is complete. Here is your receipt.", "Hồ sơ của anh đã đủ. Đây là giấy biên nhận."),
  ("I'm sorry, one document is missing.", "Xin lỗi, còn thiếu một giấy tờ."),
  ("Please sign here and write the date.", "Vui lòng ký ở đây và ghi ngày."),
  ("The result will be ready on the date on your receipt.", "Kết quả sẽ có vào ngày ghi trên giấy biên nhận."),
  ("Please bring the original and one copy.", "Vui lòng mang bản gốc và một bản sao."),
  ("You can also submit this online.", "Anh/chị cũng có thể nộp trực tuyến."),
 ],
 "dialogues": [
  ("Hi, I'd like to apply for a work permit. Where do I start?", [
    ("Welcome. Please take a number first. When your number is called, bring your passport and the forms to counter 2.", True, "Hướng dẫn từng bước rõ ràng, lịch sự."),
    ("You go counter 2.", False, "Thiếu 'to' ('go to counter 2') và cộc lốc — nên chào và hướng dẫn lấy số trước."),
    ("Work permit is not here, maybe.", False, "Trả lời mơ hồ — cán bộ một cửa cần chỉ đúng chỗ, đúng bước."),
  ]),
  ("Is my file complete?", [
    ("Almost. Everything is fine except the health certificate. Please bring it, and we can accept your file.", True, "Nói rõ thiếu gì + bước tiếp theo."),
    ("Not complete, you come back.", False, "Thiếu 'It's' và không nói thiếu giấy gì — khách phải đi lại nhiều lần."),
    ("Your file is lack one paper.", False, "Sai: 'lack' là động từ — nói 'Your file is missing one document'."),
  ]),
  ("When can I get the result?", [
    ("The date is on your receipt. Please come back on that day with the receipt and your passport.", True, "Chỉ vào biên nhận + nhắc mang giấy tờ khi nhận."),
    ("Maybe fast, maybe slow.", False, "Mơ hồ — hãy dựa vào ngày hẹn trên biên nhận."),
    ("You wait we call.", False, "Thiếu 'until' và 'you' ('Please wait until we call you') — nghe cộc."),
  ]),
  ("Can my assistant collect the result for me?", [
    ("Yes, but your assistant needs the receipt and a letter of authorization signed by you.", True, "Có điều kiện rõ ràng: biên nhận + giấy uỷ quyền."),
    ("Assistant can, no problem.", False, "Thiếu 'Your' và bỏ qua giấy uỷ quyền."),
    ("No, you must come yourself always.", False, "Khẳng định cứng nhắc, sai trật tự ('You must always come yourself')."),
  ]),
  ("Sorry, I don't read Vietnamese. What does this form say?", [
    ("No problem. This part is your personal information, and this part is about your company. I'll show you where to sign.", True, "Kiên nhẫn giải thích từng phần + hỗ trợ ký."),
    ("You must learn Vietnamese.", False, "Thiếu thiện chí — cán bộ một cửa cần hỗ trợ người nước ngoài."),
    ("This form is write about you.", False, "Sai cấu trúc ('This form is about you') và giải thích không rõ."),
  ]),
 ],
 "listen": [
  ("Please take a number and wait for your turn", ["number", "turn"], "lấy số thứ tự"),
  ("One document is missing from your file", ["document", "missing"], "báo thiếu giấy tờ"),
  ("Please bring the original and one copy", ["original", "copy"], "bản gốc và bản sao"),
  ("You can collect the result at counter three", ["collect", "three"], "nơi nhận kết quả"),
  ("Good morning. Your file is complete now. Here is your receipt with the date to collect the result.", ["complete", "receipt", "date"], "nhận hồ sơ đủ"),
  ("I'm sorry, your photo is missing. Please bring two photos tomorrow. You don't need to take a new number.", ["photo", "tomorrow", "number"], "báo thiếu ảnh"),
 ],
})

# ───────────────────────── 1. Giấy tờ, công chứng & dịch thuật ─────────────────────────
PHASES.append({
 "title": "Giấy tờ, công chứng & dịch thuật",
 "vocab": [
  ("notarize", "/ˈnəʊtəraɪz/", "v", "công chứng, chứng thực", "You need to <b>notarize</b> the copy of your degree.", "Anh cần công chứng bản sao bằng đại học.", "公証する", "kōshō suru"),
  ("certified copy", "/ˌsɜːtɪfaɪd ˈkɒpi/", "n", "bản sao chứng thực (bản sao y)", "Please submit a <b>certified copy</b> of your passport.", "Vui lòng nộp bản sao chứng thực hộ chiếu."),
  ("certified translation", "/ˌsɜːtɪfaɪd trænsˈleɪʃn/", "n", "bản dịch có chứng thực (dịch thuật công chứng)", "The authority needs a <b>certified translation</b> into Vietnamese.", "Cơ quan cần bản dịch sang tiếng Việt có chứng thực."),
  ("legalization", "/ˌliːɡəlaɪˈzeɪʃn/", "n", "hợp pháp hoá lãnh sự", "Documents from abroad usually need consular <b>legalization</b> first.", "Giấy tờ nước ngoài thường phải hợp pháp hoá lãnh sự trước."),
  ("consulate", "/ˈkɒnsjələt/", "n", "lãnh sự quán", "You can legalize the document at the Vietnamese <b>consulate</b> in your country.", "Anh có thể hợp pháp hoá giấy tờ ở lãnh sự quán Việt Nam tại nước anh.", "領事館", "ryōjikan"),
  ("notary office", "/ˈnəʊtəri ˌɒfɪs/", "n", "văn phòng công chứng", "The <b>notary office</b> is open on Saturday morning.", "Văn phòng công chứng làm việc sáng thứ Bảy."),
  ("signature", "/ˈsɪɡnətʃə/", "n", "chữ ký", "The <b>signature</b> on the contract doesn't match the passport.", "Chữ ký trên hợp đồng không khớp với hộ chiếu.", "署名", "shomei"),
  ("seal", "/siːl/", "n", "con dấu (công ty)", "The letter needs the company <b>seal</b> next to the director's signature.", "Thư cần đóng dấu công ty bên cạnh chữ ký của giám đốc."),
  ("valid", "/ˈvælɪd/", "adj", "còn hiệu lực, hợp lệ", "This health certificate is no longer <b>valid</b>.", "Giấy khám sức khoẻ này không còn hiệu lực nữa.", "有効", "yūkō"),
  ("birth certificate", "/ˈbɜːθ səˌtɪfɪkət/", "n", "giấy khai sinh", "For your son's visa, we need his <b>birth certificate</b>.", "Để làm visa cho con trai anh, chúng tôi cần giấy khai sinh của bé.", "出生証明書", "shusshō shōmeisho"),
 ],
 "phrases": [
  ("Is this a certified copy or a normal copy?", "Đây là bản sao chứng thực hay bản photo thường?"),
  ("This document needs to be translated into Vietnamese.", "Giấy tờ này cần được dịch sang tiếng Việt."),
  ("The translation must match the original exactly.", "Bản dịch phải khớp chính xác với bản gốc."),
  ("Documents from abroad usually need consular legalization.", "Giấy tờ nước ngoài thường cần hợp pháp hoá lãnh sự."),
  ("Please check the spelling of your name on the translation.", "Vui lòng kiểm tra chính tả tên anh/chị trên bản dịch."),
  ("How many copies do you need?", "Anh/chị cần bao nhiêu bản?"),
  ("The translation will be ready tomorrow afternoon.", "Bản dịch sẽ xong vào chiều mai."),
  ("Please bring your passport when you sign.", "Khi ký vui lòng mang theo hộ chiếu."),
  ("This stamp isn't clear. Can you get a new copy?", "Dấu này không rõ. Anh/chị lấy bản mới được không?"),
  ("Let me check which documents need legalization.", "Để tôi kiểm tra giấy tờ nào cần hợp pháp hoá."),
 ],
 "dialogues": [
  ("Do I need to translate my university degree?", [
    ("Yes. It must be translated into Vietnamese and certified. If it's from abroad, it usually needs legalization first.", True, "Trả lời rõ + thứ tự: hợp pháp hoá trước, rồi dịch và chứng thực."),
    ("Yes, you translate yourself is OK.", False, "Sai cấu trúc và sai thực tế — bản dịch nộp cơ quan thường phải có chứng thực."),
    ("Degree no need, I think.", False, "Thiếu động từ và mơ hồ — bằng cấp là giấy tờ quan trọng trong hồ sơ."),
  ]),
  ("The name on my translation is spelled wrong.", [
    ("I'm sorry about that. We'll correct it and give you a new copy this afternoon, free of charge.", True, "Xin lỗi + sửa + thời gian + không tính phí."),
    ("Small mistake, nobody check.", False, "Sai tên là lỗi nghiêm trọng — hồ sơ có thể bị trả lại; thiếu 's' ('checks')."),
    ("You write wrong on the form.", False, "Đổ lỗi cho khách, sai thì ('You wrote it wrong')."),
  ]),
  ("Can you notarize this copy now?", [
    ("Sure. Please show me the original so I can compare them. It takes about fifteen minutes.", True, "Đồng ý + cần bản gốc để đối chiếu + thời gian."),
    ("Notarize now cannot.", False, "Sai trật tự, cộc lốc, không nêu lý do hay hẹn giờ."),
    ("OK, no need original.", False, "Sai quy trình — chứng thực bản sao phải đối chiếu với bản gốc."),
  ]),
  ("What's the difference between a copy and a certified copy?", [
    ("A certified copy has an official stamp that says it matches the original. A normal copy doesn't.", True, "Giải thích đơn giản, đúng bản chất."),
    ("Certified copy is more expensive copy.", False, "Không giải thích được bản chất, thiếu mạo từ."),
    ("Same same, only stamp.", False, "'Same same' là lối nói kiểu Việt; thực tế giá trị pháp lý khác nhau."),
  ]),
  ("How long does the translation take?", [
    ("For a two-page document, we can finish by tomorrow noon. I'll call you when it's ready.", True, "Thời gian cụ thể + chủ động báo."),
    ("Very fast, don't worry.", False, "Mơ hồ, không có mốc thời gian."),
    ("It take one day.", False, "Thiếu 's': 'It takes one day.'"),
  ]),
 ],
 "listen": [
  ("Please bring the original to compare with the copy", ["original", "compare"], "đối chiếu bản gốc"),
  ("This document must be translated into Vietnamese", ["translated", "Vietnamese"], "yêu cầu dịch"),
  ("The signature does not match the passport", ["signature", "passport"], "chữ ký không khớp"),
  ("Your certified translation will be ready tomorrow", ["certified", "tomorrow"], "hẹn trả bản dịch"),
  ("Your degree is from abroad, so it needs legalization first. After that, we will translate it and certify the translation.", ["abroad", "legalization", "translate"], "quy trình giấy tờ nước ngoài"),
  ("Please check the spelling of your name. If it is correct, sign here. The copies will be ready at four.", ["spelling", "sign", "four"], "kiểm tra bản dịch"),
 ],
})

# ───────────────────────── 2. Visa & thẻ tạm trú ─────────────────────────
PHASES.append({
 "title": "Visa & thẻ tạm trú",
 "vocab": [
  ("visa", "/ˈviːzə/", "n", "thị thực (visa)", "Your <b>visa</b> expires at the end of this month.", "Visa của anh hết hạn vào cuối tháng này.", "ビザ", "biza"),
  ("temporary residence card", "/ˌtemprəri ˈrezɪdəns ˌkɑːd/", "n", "thẻ tạm trú", "With a <b>temporary residence card</b>, you don't need a new visa for each trip.", "Có thẻ tạm trú thì anh không cần xin visa mới cho mỗi lần đi lại."),
  ("sponsor", "/ˈspɒnsə/", "n/v", "bên bảo lãnh; bảo lãnh", "Your company is the <b>sponsor</b> for your visa.", "Công ty anh là bên bảo lãnh visa cho anh."),
  ("passport", "/ˈpɑːspɔːt/", "n", "hộ chiếu", "Your <b>passport</b> must be valid for longer than the visa.", "Hộ chiếu phải còn hạn lâu hơn visa.", "パスポート", "pasupōto"),
  ("expiry date", "/ɪkˈspaɪəri ˌdeɪt/", "n", "ngày hết hạn", "Please check the <b>expiry date</b> on your card.", "Vui lòng kiểm tra ngày hết hạn trên thẻ.", "有効期限", "yūkō kigen"),
  ("extension", "/ɪkˈstenʃn/", "n", "sự gia hạn", "We should apply for a visa <b>extension</b> before it expires.", "Mình nên xin gia hạn visa trước khi hết hạn.", "延長", "enchō"),
  ("entry", "/ˈentri/", "n", "sự nhập cảnh", "This visa is for a single <b>entry</b> only.", "Visa này chỉ nhập cảnh một lần.", "入国", "nyūkoku"),
  ("immigration office", "/ˌɪmɪˈɡreɪʃn ˌɒfɪs/", "n", "cơ quan quản lý xuất nhập cảnh", "We'll submit your file to the <b>immigration office</b> on Monday.", "Thứ Hai chúng tôi sẽ nộp hồ sơ của anh lên cơ quan xuất nhập cảnh."),
  ("overstay", "/ˌəʊvəˈsteɪ/", "v", "ở quá hạn (visa, thẻ)", "If you <b>overstay</b>, you may have problems when you leave.", "Nếu ở quá hạn, anh có thể gặp rắc rối khi xuất cảnh.", "オーバーステイ", "ōbāsutei"),
  ("dependant", "/dɪˈpendənt/", "n", "người phụ thuộc (vợ/chồng, con đi cùng)", "Can my wife apply as a <b>dependant</b>?", "Vợ tôi có thể xin theo diện người phụ thuộc không?"),
 ],
 "phrases": [
  ("Your visa expires on the 25th.", "Visa của anh hết hạn vào ngày 25."),
  ("Let's apply for the extension at least two weeks early.", "Mình nộp xin gia hạn sớm ít nhất hai tuần nhé."),
  ("We need your passport for a few working days.", "Chúng tôi cần giữ hộ chiếu của anh vài ngày làm việc."),
  ("Your company will be the sponsor.", "Công ty anh sẽ là bên bảo lãnh."),
  ("How long is your passport still valid?", "Hộ chiếu của anh còn hạn bao lâu?"),
  ("Please don't book any trips while we hold your passport.", "Trong thời gian chúng tôi giữ hộ chiếu, anh đừng đặt chuyến đi nào nhé."),
  ("Your family can apply as dependants.", "Gia đình anh có thể nộp theo diện người phụ thuộc."),
  ("The requirements depend on current regulations.", "Yêu cầu tuỳ theo quy định hiện hành."),
  ("I'll send you a reminder one month before the expiry date.", "Tôi sẽ nhắc anh trước ngày hết hạn một tháng."),
  ("Please scan your passport and your current visa.", "Anh scan giúp hộ chiếu và visa hiện tại nhé."),
 ],
 "dialogues": [
  ("My visa expires next Friday. Is that a problem?", [
    ("It's very close, so let's start today. Please send me a scan of your passport this morning, and I'll prepare the extension file.", True, "Nhận ra việc gấp + hành động ngay + việc cụ thể."),
    ("Friday is still long, relax.", False, "Chủ quan — hồ sơ cần thời gian xử lý, dễ bị ở quá hạn."),
    ("Your visa is expire, you must go home.", False, "Sai ngữ pháp ('is expiring') và kết luận vội, làm khách hoảng."),
  ]),
  ("Can I travel to Singapore while you're processing my card?", [
    ("I'm afraid not. The immigration office keeps your passport during processing. Could you travel after you get it back?", True, "Từ chối lịch sự + lý do + gợi ý."),
    ("Yes, go, no problem.", False, "Sai thực tế — hộ chiếu đang được cơ quan giữ để xử lý."),
    ("You cannot travel because passport.", False, "Câu cụt — đúng là 'because we need your passport'."),
  ]),
  ("What documents do you need for my wife's visa?", [
    ("Her passport, a photo and your marriage certificate, translated and certified. I'll email you the full list.", True, "Liệt kê chính + gửi danh sách đầy đủ bằng văn bản."),
    ("Many documents, I send later.", False, "Mơ hồ, thiếu 'will' ('I'll send them later')."),
    ("Wife need passport only.", False, "Thiếu 'Your', thiếu 's' ('Your wife needs') và thiếu giấy tờ chứng minh quan hệ."),
  ]),
  ("How long will my temporary residence card be valid?", [
    ("It depends on your work permit and current regulations. It usually can't be longer than your permit, but I'll confirm the exact date.", True, "Nêu nguyên tắc chung + hẹn xác nhận, không khẳng định bừa."),
    ("Five years sure.", False, "Khẳng định bừa con số — thời hạn phụ thuộc diện và giấy phép."),
    ("Card valid long time.", False, "Thiếu động từ ('is valid') và không có thông tin cụ thể."),
  ]),
  ("I lost my passport. What should I do?", [
    ("First, please report it to the local police and contact your embassy for a new passport. Then we'll update your visa or card.", True, "Các bước theo thứ tự rõ ràng."),
    ("Why you lose it?", False, "Sai cấu trúc ('Why did you lose it?') và trách khách thay vì giúp."),
    ("No passport, no visa, sorry.", False, "Cộc lốc, không hướng dẫn gì."),
  ]),
 ],
 "listen": [
  ("Your visa expires at the end of this month", ["visa", "expires"], "nhắc hết hạn visa"),
  ("Your company will be the sponsor", ["company", "sponsor"], "bên bảo lãnh"),
  ("Please check the expiry date on your card", ["expiry", "card"], "kiểm tra ngày hết hạn"),
  ("We need your passport for a few working days", ["passport", "working"], "giữ hộ chiếu"),
  ("Your card expires in six weeks. We should start the extension now. Please send me your passport and your work permit.", ["six", "extension", "permit"], "nhắc gia hạn thẻ"),
  ("Your file is at the immigration office. They will keep your passport until the card is ready. Please do not book any flights yet.", ["immigration", "keep", "flights"], "hồ sơ đang xử lý"),
 ],
})

# ───────────────────────── 3. Giấy phép lao động ─────────────────────────
PHASES.append({
 "title": "Giấy phép lao động",
 "vocab": [
  ("work permit", "/ˈwɜːk ˌpɜːmɪt/", "n", "giấy phép lao động", "Foreign employees need a <b>work permit</b> unless they are exempt.", "Người lao động nước ngoài cần giấy phép lao động, trừ trường hợp được miễn.", "労働許可証", "rōdō kyokashō"),
  ("exemption", "/ɪɡˈzempʃn/", "n", "sự miễn (trường hợp không cần giấy phép)", "Let's check whether he qualifies for an <b>exemption</b>.", "Mình kiểm tra xem anh ấy có thuộc diện được miễn không.", "免除", "menjo"),
  ("expert", "/ˈekspɜːt/", "n", "chuyên gia", "She will apply as an <b>expert</b>, so we need proof of her experience.", "Chị ấy nộp theo diện chuyên gia nên cần giấy tờ chứng minh kinh nghiệm.", "専門家", "senmonka"),
  ("degree", "/dɪˈɡriː/", "n", "bằng (đại học)", "Please send a copy of your university <b>degree</b>.", "Vui lòng gửi bản sao bằng đại học.", "学位", "gakui"),
  ("work experience", "/ˈwɜːk ɪkˌspɪəriəns/", "n", "kinh nghiệm làm việc", "We need a letter from your old employer about your <b>work experience</b>.", "Chúng tôi cần thư của công ty cũ xác nhận kinh nghiệm làm việc của anh.", "職歴", "shokureki"),
  ("health certificate", "/ˈhelθ səˌtɪfɪkət/", "n", "giấy khám sức khoẻ", "The <b>health certificate</b> must be from an approved hospital.", "Giấy khám sức khoẻ phải do bệnh viện đủ điều kiện cấp.", "健康診断書", "kenkō shindansho"),
  ("criminal record check", "/ˌkrɪmɪnl ˈrekɔːd ˌtʃek/", "n", "phiếu lý lịch tư pháp", "Apply for a <b>criminal record check</b> in your home country early. It can take weeks.", "Hãy xin phiếu lý lịch tư pháp ở nước anh sớm. Có thể mất vài tuần."),
  ("job position", "/ˈdʒɒb pəˌzɪʃn/", "n", "vị trí công việc", "The <b>job position</b> on the permit must match the contract.", "Vị trí công việc trên giấy phép phải khớp với hợp đồng."),
  ("labour department", "/ˈleɪbə dɪˌpɑːtmənt/", "n", "cơ quan quản lý lao động (địa phương)", "We'll submit the file to the local <b>labour department</b>.", "Chúng tôi sẽ nộp hồ sơ cho cơ quan quản lý lao động địa phương."),
  ("renew", "/rɪˈnjuː/", "v", "gia hạn, cấp lại", "We need to <b>renew</b> his work permit before it expires.", "Mình cần gia hạn giấy phép lao động cho anh ấy trước khi hết hạn.", "更新する", "kōshin suru"),
 ],
 "phrases": [
  ("Do you have a work permit or an exemption?", "Anh có giấy phép lao động hay giấy xác nhận miễn không?"),
  ("Please send us your degree and your work experience letters.", "Vui lòng gửi bằng cấp và thư xác nhận kinh nghiệm."),
  ("Your health check must be done at an approved hospital.", "Anh phải khám sức khoẻ ở bệnh viện đủ điều kiện."),
  ("The job title must be the same in every document.", "Chức danh phải giống nhau trên mọi giấy tờ."),
  ("The criminal record check can take a few weeks.", "Phiếu lý lịch tư pháp có thể mất vài tuần."),
  ("We'll submit the file once all documents are ready.", "Chúng tôi sẽ nộp hồ sơ khi đủ giấy tờ."),
  ("Please don't start work before the permit is issued.", "Vui lòng đừng bắt đầu làm việc trước khi được cấp giấy phép."),
  ("Your permit expires in three months, so let's prepare the renewal.", "Giấy phép của anh hết hạn trong ba tháng nữa, mình chuẩn bị hồ sơ gia hạn nhé."),
  ("I'll check the latest requirements with the labour department.", "Tôi sẽ kiểm tra yêu cầu mới nhất với cơ quan lao động."),
 ],
 "dialogues": [
  ("Can I start working next Monday? My permit isn't ready yet.", [
    ("I'm sorry, but you should wait until the permit is issued. I'll follow up on the file and update you every two days.", True, "Nêu nguyên tắc + hỗ trợ theo dõi + cập nhật đều."),
    ("Yes, work first, permit later.", False, "Sai quy định — làm việc khi chưa có giấy phép gây rủi ro cho cả công ty."),
    ("Your permit not ready, so no.", False, "Thiếu 'is' và cộc — nên giải thích và hẹn cập nhật."),
  ]),
  ("Why do you need a letter from my old company?", [
    ("It proves your work experience. The authority needs it to approve you as an expert.", True, "Giải thích mục đích ngắn gọn."),
    ("Because government want.", False, "Thiếu mạo từ, thiếu 's' ('the government wants it') và không giải thích."),
    ("I don't know, just give me.", False, "Thiếu tân ngữ ('give it to me') và không thuyết phục."),
  ]),
  ("My degree is in marketing, but my job is IT manager. Is that OK?", [
    ("It may be a problem, because the degree and the job should match. Let me check other options, like using your work experience.", True, "Nêu rủi ro thật + hướng xử lý khác."),
    ("No problem, nobody check.", False, "Chủ quan — cơ quan có xem xét sự phù hợp; thiếu 's' ('checks')."),
    ("Degree wrong, cannot.", False, "Cộc lốc, không đưa phương án."),
  ]),
  ("Do I need a work permit for a three-day business trip?", [
    ("It depends on what you'll do here. Short meetings may not need one, but I'll check the current rules and confirm today.", True, "Không khẳng định vội + hẹn xác nhận theo quy định hiện hành."),
    ("Three days is short, no need anything.", False, "Khẳng định bừa — phải kiểm tra mục đích và quy định."),
    ("You need, of course.", False, "Thiếu tân ngữ ('You need one') và cũng khẳng định vội."),
  ]),
  ("Where is my work permit now?", [
    ("We submitted it on the 5th, and it's being reviewed. The expected result date is the 20th. I'll tell you if they ask for more documents.", True, "Ngày nộp + trạng thái + ngày dự kiến + cam kết báo."),
    ("It's in the government.", False, "Mơ hồ, sai giới từ — nên nói rõ tình trạng và ngày dự kiến."),
    ("I submit already, you wait.", False, "Sai thì ('I've submitted it') và thiếu thông tin."),
  ]),
 ],
 "listen": [
  ("Please send us a copy of your degree", ["copy", "degree"], "xin bằng cấp"),
  ("The job position must match the contract", ["position", "contract"], "khớp vị trí công việc"),
  ("Do not start work before the permit is issued", ["start", "issued"], "chờ cấp phép"),
  ("We need to renew your work permit soon", ["renew", "soon"], "gia hạn giấy phép"),
  ("We submitted your work permit file this morning. The result is expected in about two weeks. I will email you when it is ready.", ["submitted", "weeks", "email"], "cập nhật hồ sơ"),
  ("Your criminal record check is still missing. Please apply for it in your home country now. It can take a long time.", ["criminal", "country", "long"], "nhắc lý lịch tư pháp"),
 ],
})

# ───────────────────────── 4. Đăng ký doanh nghiệp & đầu tư ─────────────────────────
PHASES.append({
 "title": "Đăng ký doanh nghiệp & đầu tư",
 "vocab": [
  ("business registration", "/ˈbɪznəs ˌredʒɪˈstreɪʃn/", "n", "(giấy) đăng ký doanh nghiệp", "The <b>business registration</b> shows the company's name and address.", "Giấy đăng ký doanh nghiệp thể hiện tên và địa chỉ công ty."),
  ("investment certificate", "/ɪnˈvestmənt səˌtɪfɪkət/", "n", "giấy chứng nhận đăng ký đầu tư", "Foreign investors often need an <b>investment certificate</b> first.", "Nhà đầu tư nước ngoài thường cần giấy chứng nhận đăng ký đầu tư trước."),
  ("charter capital", "/ˌtʃɑːtə ˈkæpɪtl/", "n", "vốn điều lệ", "The <b>charter capital</b> must be contributed on time.", "Vốn điều lệ phải được góp đúng hạn.", "資本金", "shihonkin"),
  ("legal representative", "/ˌliːɡl ˌreprɪˈzentətɪv/", "n", "người đại diện theo pháp luật", "Mr. Park is the <b>legal representative</b> of the company.", "Ông Park là người đại diện theo pháp luật của công ty."),
  ("shareholder", "/ˈʃeəhəʊldə/", "n", "cổ đông, thành viên góp vốn", "The <b>shareholders</b> will meet to approve the change.", "Các cổ đông sẽ họp để thông qua thay đổi.", "株主", "kabunushi"),
  ("company charter", "/ˌkʌmpəni ˈtʃɑːtə/", "n", "điều lệ công ty", "Please check the <b>company charter</b> before the meeting.", "Hãy xem điều lệ công ty trước buổi họp.", "定款", "teikan"),
  ("business line", "/ˈbɪznəs ˌlaɪn/", "n", "ngành nghề kinh doanh", "We want to add a new <b>business line</b>: software services.", "Chúng tôi muốn bổ sung ngành nghề kinh doanh mới: dịch vụ phần mềm."),
  ("head office", "/ˌhed ˈɒfɪs/", "n", "trụ sở chính", "The company is moving its <b>head office</b> to a new building.", "Công ty sắp chuyển trụ sở chính sang tòa nhà mới.", "本社", "honsha"),
  ("power of attorney", "/ˌpaʊər əv əˈtɜːni/", "n", "giấy uỷ quyền", "With a <b>power of attorney</b>, our lawyer can submit the file for you.", "Có giấy uỷ quyền thì luật sư của chúng tôi có thể nộp hồ sơ thay anh.", "委任状", "ininjō"),
  ("subsidiary", "/səbˈsɪdiəri/", "n", "công ty con", "The Vietnamese company is a <b>subsidiary</b> of a Korean group.", "Công ty Việt Nam là công ty con của một tập đoàn Hàn Quốc.", "子会社", "kogaisha"),
 ],
 "phrases": [
  ("What business lines do you want to register?", "Anh muốn đăng ký những ngành nghề kinh doanh nào?"),
  ("Who will be the legal representative?", "Ai sẽ là người đại diện theo pháp luật?"),
  ("How much charter capital are you planning?", "Anh dự kiến vốn điều lệ bao nhiêu?"),
  ("We need a lease contract for the head office.", "Cần có hợp đồng thuê địa điểm làm trụ sở chính."),
  ("Please sign the power of attorney so we can submit it for you.", "Anh ký giấy uỷ quyền để chúng tôi nộp thay nhé."),
  ("Changes to the company details must be registered.", "Thay đổi thông tin công ty phải được đăng ký."),
  ("Some business lines have extra conditions for foreign investors.", "Một số ngành nghề có điều kiện riêng với nhà đầu tư nước ngoài."),
  ("The new certificate is ready. I'll send you a scan today.", "Giấy chứng nhận mới đã có. Hôm nay tôi gửi anh bản scan."),
  ("Please check the English name of the company carefully.", "Anh kiểm tra kỹ tên tiếng Anh của công ty nhé."),
  ("We'll update the charter after the shareholders approve it.", "Chúng tôi sẽ cập nhật điều lệ sau khi cổ đông thông qua."),
 ],
 "dialogues": [
  ("We want to open a company in Vietnam. Where do we start?", [
    ("First, we'll check your business lines and choose the location. Then we'll prepare the investment and company registration files.", True, "Lộ trình rõ ràng theo từng bước."),
    ("Very easy, one week finish.", False, "Hứa bừa thời gian, sai ngữ pháp — thủ tục tuỳ ngành nghề và hồ sơ."),
    ("You start with money.", False, "Không trả lời đúng câu hỏi về thủ tục."),
  ]),
  ("Can we change the legal representative this month?", [
    ("Yes. We need the shareholders' decision and the new person's passport. Then we'll register the change.", True, "Đồng ý + giấy tờ cần + bước tiếp."),
    ("Change is easy, just tell me name.", False, "Thiếu mạo từ ('the name') và bỏ qua quyết định của cổ đông."),
    ("Legal representative cannot change.", False, "Sai — người đại diện có thể thay đổi theo thủ tục."),
  ]),
  ("Can we add 'trading' as a business line?", [
    ("Probably, but trading may have extra conditions for foreign-owned companies. I'll check and send you the steps by Thursday.", True, "Không khẳng định vội + nêu rủi ro + hẹn ngày."),
    ("Yes, add anything you want.", False, "Sai — một số ngành nghề có điều kiện riêng."),
    ("Trading is difficult, forget it.", False, "Bi quan vô căn cứ, không đưa hướng xử lý."),
  ]),
  ("Why do you need a power of attorney?", [
    ("So our team can submit and collect documents for you. You won't need to go to the office yourself.", True, "Giải thích lợi ích cho khách."),
    ("Because rule.", False, "Câu cụt, không giải thích."),
    ("For we can do instead you.", False, "Dịch từng chữ 'để… thay anh' — đúng là 'so we can do it for you'."),
  ]),
  ("Is our company name OK?", [
    ("The name looks fine, but another company has a very similar name. Let's prepare a second option just in case.", True, "Đánh giá + rủi ro + phương án dự phòng."),
    ("Name is beautiful.", False, "Nhận xét cảm tính, không trả lời về tính hợp lệ."),
    ("I think OK, we try.", False, "Thiếu 'it's' và chưa kiểm tra trùng tên."),
  ]),
 ],
 "listen": [
  ("Who will be the legal representative", ["legal", "representative"], "hỏi người đại diện"),
  ("We want to add a new business line", ["add", "line"], "bổ sung ngành nghề"),
  ("Please sign the power of attorney today", ["sign", "attorney"], "ký giấy uỷ quyền"),
  ("The head office will move next month", ["office", "move"], "chuyển trụ sở"),
  ("Your new certificate is ready. The company name and the business lines are correct. I will send you a scan this afternoon.", ["certificate", "correct", "scan"], "báo có giấy chứng nhận"),
  ("The shareholders approved the new charter capital. We will register the change this week. Please sign the forms by Wednesday.", ["approved", "register", "Wednesday"], "đăng ký thay đổi vốn"),
 ],
})

# ───────────────────────── 5. Hợp đồng cơ bản ─────────────────────────
PHASES.append({
 "title": "Hợp đồng cơ bản",
 "vocab": [
  ("contract", "/ˈkɒntrækt/", "n", "hợp đồng", "Please read the <b>contract</b> before you sign it.", "Vui lòng đọc hợp đồng trước khi ký.", "契約書", "keiyakusho"),
  ("party", "/ˈpɑːti/", "n", "bên (trong hợp đồng)", "Both <b>parties</b> agreed to the new date.", "Cả hai bên đã đồng ý với ngày mới.", "当事者", "tōjisha"),
  ("clause", "/klɔːz/", "n", "điều khoản", "<b>Clause</b> 5 is about payment.", "Điều 5 nói về thanh toán.", "条項", "jōkō"),
  ("term", "/tɜːm/", "n", "thời hạn (hợp đồng)", "The <b>term</b> of the contract is two years.", "Thời hạn hợp đồng là hai năm.", "期間", "kikan"),
  ("sign", "/saɪn/", "v", "ký", "The director will <b>sign</b> the contract on Friday.", "Thứ Sáu giám đốc sẽ ký hợp đồng.", "署名する", "shomei suru"),
  ("effective date", "/ɪˈfektɪv ˌdeɪt/", "n", "ngày có hiệu lực", "The <b>effective date</b> is 1 July.", "Ngày có hiệu lực là 1/7.", "発効日", "hakkōbi"),
  ("obligation", "/ˌɒblɪˈɡeɪʃn/", "n", "nghĩa vụ", "Delivery on time is the seller's main <b>obligation</b>.", "Giao hàng đúng hạn là nghĩa vụ chính của bên bán.", "義務", "gimu"),
  ("terminate", "/ˈtɜːmɪneɪt/", "v", "chấm dứt (hợp đồng)", "Either party can <b>terminate</b> the contract with 30 days' notice.", "Mỗi bên có thể chấm dứt hợp đồng khi báo trước 30 ngày."),
  ("annex", "/ˈæneks/", "n", "phụ lục (hợp đồng)", "The price list is in <b>Annex</b> 1.", "Bảng giá nằm ở Phụ lục 1."),
  ("bilingual", "/baɪˈlɪŋɡwəl/", "adj", "song ngữ", "We'll prepare a <b>bilingual</b> contract in English and Vietnamese.", "Chúng tôi sẽ soạn hợp đồng song ngữ Anh – Việt."),
 ],
 "phrases": [
  ("Who are the parties to this contract?", "Các bên trong hợp đồng này là ai?"),
  ("The contract is in English and Vietnamese.", "Hợp đồng bằng tiếng Anh và tiếng Việt."),
  ("Which language prevails if the two versions are different?", "Nếu hai ngôn ngữ khác nhau thì bản nào được ưu tiên?"),
  ("The payment terms are in Clause 4.", "Điều khoản thanh toán nằm ở Điều 4."),
  ("Please initial every page and sign the last page.", "Vui lòng ký nháy từng trang và ký trang cuối."),
  ("The contract starts on the effective date, not the signing date.", "Hợp đồng bắt đầu từ ngày có hiệu lực, không phải ngày ký."),
  ("We'll send two originals by courier.", "Chúng tôi sẽ gửi hai bản gốc qua chuyển phát."),
  ("Any change must be made in a written annex.", "Mọi thay đổi phải được lập thành phụ lục bằng văn bản."),
  ("Has the other party signed yet?", "Bên kia đã ký chưa?"),
  ("I'll check the seal and the signature before we file it.", "Tôi sẽ kiểm tra dấu và chữ ký trước khi lưu hồ sơ."),
 ],
 "dialogues": [
  ("Can you send me the contract to sign?", [
    ("Sure. I'll email you the final version today. Please check your company name and address before signing.", True, "Đồng ý + thời gian + nhắc kiểm tra thông tin."),
    ("OK, I send you now contract.", False, "Sai trật tự và thiếu 'will' ('I'll send you the contract now')."),
    ("Contract is not finish.", False, "Sai ngữ pháp ('isn't finished') và không nói khi nào xong."),
  ]),
  ("The English and Vietnamese versions say different things in Clause 7.", [
    ("Thanks for spotting that. I'll fix the translation and check which language prevails under the contract.", True, "Cảm ơn + sửa + kiểm tra điều khoản ngôn ngữ ưu tiên."),
    ("Small different, it's fine.", False, "Sai từ loại ('difference') và xem nhẹ — sai khác bản dịch dễ gây tranh chấp."),
    ("Vietnamese is always correct.", False, "Khẳng định bừa — phải xem điều khoản ưu tiên ngôn ngữ trong hợp đồng."),
  ]),
  ("When does the contract start?", [
    ("On the effective date in Clause 2, which is 1 August, not the day we sign.", True, "Chỉ đúng điều khoản + ngày cụ thể + phân biệt với ngày ký."),
    ("When we sign, I think.", False, "Không chắc chắn và có thể sai — nên kiểm tra điều khoản hiệu lực."),
    ("Contract start August.", False, "Thiếu 's' và giới từ ('It starts in August')."),
  ]),
  ("Can we terminate early if they deliver late?", [
    ("Possibly. Clause 9 allows termination for a serious breach, but we must send a written notice first. I'll ask our lawyer to confirm.", True, "Chỉ điều khoản + điều kiện thủ tục + hỏi luật sư, không khẳng định vội."),
    ("Yes, stop anytime you want.", False, "Sai — chấm dứt phải theo điều khoản và thủ tục thông báo."),
    ("Late is small, cannot stop.", False, "Sai ngữ pháp và kết luận vội khi chưa đọc hợp đồng."),
  ]),
  ("Do we need to sign every page?", [
    ("Please initial every page and sign the last page. It shows that no page was changed.", True, "Hướng dẫn + lý do đơn giản."),
    ("Yes, sign sign all.", False, "Lặp từ kiểu tiếng Việt, không phân biệt ký nháy và ký chính."),
    ("No need, one sign enough.", False, "Thiếu động từ và dùng sai 'sign' (danh từ là 'signature')."),
  ]),
 ],
 "listen": [
  ("Please read the contract before you sign it", ["read", "sign"], "đọc trước khi ký"),
  ("The payment terms are in clause four", ["payment", "clause"], "điều khoản thanh toán"),
  ("The effective date is the first of July", ["effective", "July"], "ngày có hiệu lực"),
  ("The price list is in the annex", ["price", "annex"], "phụ lục giá"),
  ("This is a bilingual contract. If the two versions are different, the English version prevails. Please check both carefully.", ["bilingual", "English", "carefully"], "hợp đồng song ngữ"),
  ("The other party signed the contract yesterday. We will send you two originals by courier. Please sign and return one copy.", ["yesterday", "originals", "return"], "gửi bản gốc"),
 ],
})

# ───────────────────────── 6. Rà soát & đàm phán hợp đồng ─────────────────────────
PHASES.append({
 "title": "Rà soát & đàm phán hợp đồng",
 "vocab": [
  ("draft", "/drɑːft/", "n", "bản dự thảo", "Here is the first <b>draft</b> of the service agreement.", "Đây là bản dự thảo đầu tiên của hợp đồng dịch vụ.", "草案", "sōan"),
  ("redline", "/ˈredlaɪn/", "n/v", "bản đánh dấu sửa đổi; đánh dấu sửa đổi", "Please send us a <b>redline</b> so we can see your changes.", "Vui lòng gửi bản đánh dấu sửa đổi để chúng tôi thấy phần thay đổi."),
  ("track changes", "/ˌtræk ˈtʃeɪndʒɪz/", "n", "chế độ theo dõi thay đổi (trong file văn bản)", "Please turn on <b>track changes</b> before you edit the file.", "Vui lòng bật chế độ theo dõi thay đổi trước khi sửa file."),
  ("governing law", "/ˌɡʌvənɪŋ ˈlɔː/", "n", "luật áp dụng (điều chỉnh hợp đồng)", "The <b>governing law</b> of this contract is Vietnamese law.", "Luật áp dụng cho hợp đồng này là luật Việt Nam.", "準拠法", "junkyohō"),
  ("liability", "/ˌlaɪəˈbɪləti/", "n", "trách nhiệm (pháp lý, bồi thường)", "They want to limit their <b>liability</b> to the contract value.", "Họ muốn giới hạn trách nhiệm ở mức giá trị hợp đồng.", "責任", "sekinin"),
  ("penalty", "/ˈpenəlti/", "n", "khoản phạt (vi phạm hợp đồng)", "The <b>penalty</b> for late delivery is in Clause 10.", "Mức phạt giao hàng trễ nằm ở Điều 10.", "違約金", "iyakukin"),
  ("compensation", "/ˌkɒmpenˈseɪʃn/", "n", "khoản bồi thường", "The buyer asked for <b>compensation</b> for the damaged goods.", "Bên mua yêu cầu bồi thường cho hàng bị hư hỏng.", "損害賠償", "songai baishō"),
  ("force majeure", "/ˌfɔːs mæˈʒɜː/", "n", "sự kiện bất khả kháng", "A typhoon may be a <b>force majeure</b> event.", "Bão có thể là một sự kiện bất khả kháng.", "不可抗力", "fukakōryoku"),
  ("negotiate", "/nɪˈɡəʊʃieɪt/", "v", "đàm phán, thương lượng", "We need to <b>negotiate</b> the payment terms again.", "Mình cần đàm phán lại điều khoản thanh toán.", "交渉する", "kōshō suru"),
  ("final version", "/ˌfaɪnl ˈvɜːʃn/", "n", "bản cuối cùng (bản chốt)", "Is this the <b>final version</b>, or are there more changes?", "Đây là bản chốt chưa, hay còn sửa nữa?", "最終版", "saishūban"),
 ],
 "phrases": [
  ("I've reviewed the draft and added some comments.", "Tôi đã rà soát bản dự thảo và thêm một số góp ý."),
  ("Please see my comments in the margin.", "Vui lòng xem góp ý của tôi ở lề."),
  ("Could you send the redline, not a clean copy?", "Anh gửi bản có đánh dấu sửa đổi được không, đừng gửi bản sạch?"),
  ("We can't accept unlimited liability.", "Chúng tôi không thể chấp nhận trách nhiệm không giới hạn."),
  ("Can we agree on a cap for the penalty?", "Mình thống nhất mức trần cho khoản phạt được không?"),
  ("This clause isn't clear. What does it mean in practice?", "Điều khoản này chưa rõ. Trên thực tế nó có nghĩa là gì?"),
  ("We suggest changing 30 days to 45 days.", "Chúng tôi đề xuất đổi 30 ngày thành 45 ngày."),
  ("Let me check this point with our legal manager.", "Để tôi kiểm tra điểm này với trưởng phòng pháp chế."),
  ("Is this the final version for signing?", "Đây là bản cuối để ký chưa?"),
  ("We accept all changes except Clause 12.", "Chúng tôi chấp nhận mọi thay đổi trừ Điều 12."),
 ],
 "dialogues": [
  ("Have you reviewed our draft?", [
    ("Yes. Overall it's fine. We have three comments, mainly on liability and payment. I'll send the redline today.", True, "Tóm tắt + số lượng góp ý + trọng tâm + thời gian."),
    ("Yes, I review already, many problem.", False, "Sai thì ('I've reviewed it') và 'many problems' mơ hồ, nghe tiêu cực."),
    ("Not yet, too long.", False, "Cộc lốc và không hẹn khi nào xong."),
  ]),
  ("Why did you delete the force majeure clause?", [
    ("We didn't mean to delete it. It was a mistake in the file. I'll put it back and send a new redline.", True, "Nhận lỗi + sửa + gửi lại bản đánh dấu."),
    ("Force majeure is not important.", False, "Sai — điều khoản bất khả kháng rất quan trọng khi có sự cố ngoài ý muốn."),
    ("I don't delete, maybe computer.", False, "Sai thì ('I didn't delete it') và đổ lỗi cho máy."),
  ]),
  ("We want a penalty of 20 percent for late delivery.", [
    ("That's quite high for us. Could we discuss a lower rate? I'll also check the legal limit under current regulations.", True, "Phản hồi lịch sự + đề xuất + nhắc kiểm tra giới hạn luật định."),
    ("No, too much, we don't agree.", False, "Từ chối cộc, không mở đường đàm phán."),
    ("OK, 20 percent no problem.", False, "Đồng ý vội khi chưa đánh giá rủi ro và quy định."),
  ]),
  ("Which governing law do you prefer?", [
    ("We'd prefer Vietnamese law, because the work happens in Vietnam. But we're open to discussing it.", True, "Nêu ưu tiên + lý do + sẵn sàng thương lượng."),
    ("Law of Vietnam is best law.", False, "Nói chung chung, thiếu lý do thuyết phục."),
    ("Any law OK.", False, "Buông lỏng một điểm quan trọng của hợp đồng."),
  ]),
  ("Can we sign today?", [
    ("Almost. We still need to agree on Clause 12. If we fix it this morning, we can sign this afternoon.", True, "Nêu điểm còn vướng + điều kiện + thời gian."),
    ("Sign today cannot, maybe.", False, "Sai trật tự từ và mơ hồ."),
    ("Yes, sign now, fix later.", False, "Ký trước sửa sau rất rủi ro về pháp lý."),
  ]),
 ],
 "listen": [
  ("Please turn on track changes before you edit", ["track", "edit"], "bật theo dõi thay đổi"),
  ("We cannot accept unlimited liability", ["accept", "liability"], "giới hạn trách nhiệm"),
  ("The governing law is Vietnamese law", ["governing", "Vietnamese"], "luật áp dụng"),
  ("Is this the final version for signing", ["final", "signing"], "hỏi bản chốt"),
  ("I have reviewed the draft. Most clauses are fine. We only have comments on the penalty and the payment terms.", ["reviewed", "penalty", "payment"], "phản hồi dự thảo"),
  ("Thank you for your redline. We accept your changes to Clause five. However, we need more time to review the liability cap.", ["redline", "accept", "cap"], "trả lời bản sửa"),
 ],
})

# ───────────────────────── 7. Bảo mật & NDA ─────────────────────────
PHASES.append({
 "title": "Bảo mật & NDA",
 "vocab": [
  ("confidential", "/ˌkɒnfɪˈdenʃl/", "adj", "mật, cần bảo mật", "This report is <b>confidential</b>. Please don't forward it.", "Báo cáo này là tài liệu mật. Vui lòng không chuyển tiếp.", "機密", "kimitsu"),
  ("NDA", "/ˌen diː ˈeɪ/", "n", "thoả thuận bảo mật (non-disclosure agreement)", "Please sign the <b>NDA</b> before we share the files.", "Vui lòng ký thoả thuận bảo mật trước khi chúng tôi chia sẻ tài liệu.", "秘密保持契約", "himitsu hoji keiyaku"),
  ("disclose", "/dɪsˈkləʊz/", "v", "tiết lộ, công bố", "You can't <b>disclose</b> our prices to other suppliers.", "Anh không được tiết lộ giá của chúng tôi cho nhà cung cấp khác.", "開示する", "kaiji suru"),
  ("third party", "/ˌθɜːd ˈpɑːti/", "n", "bên thứ ba", "Don't share client data with any <b>third party</b>.", "Không chia sẻ dữ liệu khách hàng với bất kỳ bên thứ ba nào.", "第三者", "daisansha"),
  ("need-to-know", "/ˌniːd tə ˈnəʊ/", "adj", "(nguyên tắc) chỉ người cần biết mới được biết", "Share the file on a <b>need-to-know</b> basis only.", "Chỉ chia sẻ tài liệu cho người cần biết."),
  ("access", "/ˈækses/", "n", "quyền truy cập", "Only the legal team has <b>access</b> to this folder.", "Chỉ nhóm pháp chế có quyền truy cập thư mục này.", "アクセス", "akusesu"),
  ("password-protected", "/ˈpɑːswɜːd prəˌtektɪd/", "adj", "có đặt mật khẩu", "Please send it as a <b>password-protected</b> file.", "Vui lòng gửi dưới dạng file có đặt mật khẩu."),
  ("leak", "/liːk/", "n/v", "sự rò rỉ; làm lộ (thông tin)", "Someone <b>leaked</b> the draft to a competitor.", "Ai đó đã làm lộ bản dự thảo cho đối thủ.", "漏洩", "rōei"),
  ("sensitive", "/ˈsensətɪv/", "adj", "nhạy cảm", "Salary data is very <b>sensitive</b>.", "Dữ liệu lương là thông tin rất nhạy cảm."),
  ("shred", "/ʃred/", "v", "huỷ (giấy tờ) bằng máy huỷ", "Please <b>shred</b> old copies. Don't throw them in the bin.", "Vui lòng huỷ các bản cũ bằng máy. Đừng vứt vào thùng rác."),
 ],
 "phrases": [
  ("Could you sign the NDA before the meeting?", "Anh ký thoả thuận bảo mật trước buổi họp được không?"),
  ("This information is confidential.", "Thông tin này là thông tin mật."),
  ("Please don't forward this email outside the company.", "Vui lòng không chuyển tiếp email này ra ngoài công ty."),
  ("I'll send the password in a separate message.", "Tôi sẽ gửi mật khẩu trong một tin nhắn riêng."),
  ("Who else has access to this folder?", "Ai khác có quyền truy cập thư mục này?"),
  ("Let's discuss this in a meeting room, not in the open office.", "Mình bàn việc này trong phòng họp, đừng ở khu làm việc chung."),
  ("Please lock your screen when you leave your desk.", "Vui lòng khoá màn hình khi rời bàn."),
  ("We need to report this leak right away.", "Mình cần báo ngay vụ lộ thông tin này."),
  ("The NDA covers our prices and our client list.", "Thoả thuận bảo mật bao gồm giá và danh sách khách hàng của chúng tôi."),
  ("How long does the confidentiality obligation last?", "Nghĩa vụ bảo mật kéo dài bao lâu?"),
 ],
 "dialogues": [
  ("Can I send the contract to my friend? He's a lawyer too.", [
    ("I'm sorry, but it's confidential. If you need outside advice, let's ask our law firm to review it under an NDA.", True, "Từ chối lịch sự + lý do + phương án đúng."),
    ("OK, friend is fine.", False, "Vi phạm bảo mật — người ngoài không được xem dù là bạn."),
    ("No! You crazy?", False, "Thô lỗ, thiếu động từ — cần từ chối lịch sự."),
  ]),
  ("I sent the file to the wrong person by mistake.", [
    ("Thanks for telling me quickly. Let's ask them to delete it, and I'll report it to our manager now.", True, "Ghi nhận + hạn chế thiệt hại + báo cáo đúng quy trình."),
    ("Don't worry, maybe he doesn't open.", False, "Chủ quan, thiếu 'it' — sự cố lộ thông tin phải xử lý ngay."),
    ("Why you so careless?", False, "Sai cấu trúc ('Why were you…?') và trách móc thay vì xử lý."),
  ]),
  ("Why do we need an NDA? We're just talking.", [
    ("Because we'll share prices and plans in the meeting. The NDA protects both companies.", True, "Lý do cụ thể + lợi ích hai bên."),
    ("Because our boss say.", False, "Sai chia động từ ('says so') và không giải thích."),
    ("NDA is normal, everybody sign.", False, "Thiếu 's' ('signs') và không nêu lý do."),
  ]),
  ("How should I send the salary file to the auditor?", [
    ("Please send it as a password-protected file, and give them the password by phone or in a separate message.", True, "Cách gửi an toàn + tách kênh gửi mật khẩu."),
    ("Just email, it's fast.", False, "Dữ liệu lương nhạy cảm — không gửi file không mật khẩu qua email."),
    ("Send with password in same email.", False, "Gửi mật khẩu cùng email thì mất tác dụng; thiếu mạo từ ('the same')."),
  ]),
  ("Can I throw these old contracts in the bin?", [
    ("No, please shred them. They have client names and prices.", True, "Hướng dẫn đúng + lý do."),
    ("Yes, old paper is rubbish.", False, "Tài liệu cũ vẫn chứa thông tin mật."),
    ("You keep all, never throw.", False, "Sai ngữ pháp và không đúng — tài liệu hết hạn lưu trữ cần huỷ đúng cách."),
  ]),
 ],
 "listen": [
  ("Please sign the NDA before the meeting", ["NDA", "meeting"], "ký thoả thuận bảo mật"),
  ("This report is confidential", ["report", "confidential"], "tài liệu mật"),
  ("Only the legal team has access to this folder", ["legal", "access"], "quyền truy cập"),
  ("Please shred the old copies", ["shred", "old"], "huỷ bản cũ"),
  ("I will send the file now. It is password-protected. The password will come in a separate message.", ["file", "password-protected", "separate"], "gửi file bảo mật"),
  ("Someone forwarded our draft to a supplier. Please do not share any more files. We will report this leak to the manager today.", ["forwarded", "share", "leak"], "sự cố lộ thông tin"),
 ],
})

# ───────────────────────── 8. Họp với luật sư nước ngoài ─────────────────────────
PHASES.append({
 "title": "Họp với luật sư nước ngoài",
 "vocab": [
  ("counsel", "/ˈkaʊnsl/", "n", "luật sư (tư vấn)", "Our outside <b>counsel</b> will join the call from Singapore.", "Luật sư tư vấn bên ngoài của chúng tôi sẽ tham gia cuộc gọi từ Singapore."),
  ("client", "/ˈklaɪənt/", "n", "khách hàng (của công ty luật)", "The <b>client</b> wants an answer by Friday.", "Khách hàng muốn có câu trả lời trước thứ Sáu.", "依頼者", "iraisha"),
  ("legal opinion", "/ˌliːɡl əˈpɪnjən/", "n", "ý kiến pháp lý (bằng văn bản)", "The bank asked for a <b>legal opinion</b> on the loan.", "Ngân hàng yêu cầu ý kiến pháp lý về khoản vay.", "法律意見書", "hōritsu ikensho"),
  ("fee quote", "/ˈfiː ˌkwəʊt/", "n", "báo phí (dịch vụ)", "Could you send us a <b>fee quote</b> for this work?", "Anh gửi báo phí cho công việc này được không?"),
  ("conflict check", "/ˈkɒnflɪkt ˌtʃek/", "n", "kiểm tra xung đột lợi ích (trước khi nhận vụ việc)", "We need to run a <b>conflict check</b> before we accept the case.", "Chúng tôi cần kiểm tra xung đột lợi ích trước khi nhận vụ việc."),
  ("engagement letter", "/ɪnˈɡeɪdʒmənt ˌletə/", "n", "thư thoả thuận dịch vụ pháp lý", "Please sign the <b>engagement letter</b> so we can start.", "Vui lòng ký thư thoả thuận dịch vụ để chúng tôi bắt đầu."),
  ("jurisdiction", "/ˌdʒʊərɪsˈdɪkʃn/", "n", "thẩm quyền; hệ thống pháp luật (nước, khu vực)", "The answer depends on the <b>jurisdiction</b>.", "Câu trả lời tuỳ thuộc vào hệ thống pháp luật nào áp dụng.", "管轄", "kankatsu"),
  ("local law", "/ˌləʊkl ˈlɔː/", "n", "luật sở tại (luật Việt Nam)", "Please check this point under <b>local law</b>.", "Vui lòng kiểm tra điểm này theo luật sở tại."),
  ("billable hours", "/ˌbɪləbl ˈaʊəz/", "n", "số giờ tính phí", "Please record your <b>billable hours</b> every day.", "Vui lòng ghi lại số giờ tính phí mỗi ngày."),
  ("practice area", "/ˈpræktɪs ˌeəriə/", "n", "lĩnh vực hành nghề", "Our main <b>practice areas</b> are corporate and labour law.", "Lĩnh vực hành nghề chính của chúng tôi là luật doanh nghiệp và lao động."),
 ],
 "phrases": [
  ("Thank you for joining the call.", "Cảm ơn anh/chị đã tham gia cuộc gọi."),
  ("Let me introduce our team.", "Để tôi giới thiệu nhóm của chúng tôi."),
  ("Could you explain how this works under your law?", "Anh giải thích giúp theo luật bên anh thì việc này thế nào?"),
  ("Under Vietnamese law, the process is a bit different.", "Theo luật Việt Nam, quy trình hơi khác."),
  ("Could you repeat the last point more slowly?", "Anh nhắc lại ý cuối chậm hơn được không?"),
  ("Let me confirm the next steps.", "Để tôi xác nhận các bước tiếp theo."),
  ("We'll send you a short summary after the call.", "Sau cuộc gọi chúng tôi sẽ gửi anh bản tóm tắt ngắn."),
  ("Could you send us a fee quote by Friday?", "Anh gửi báo phí trước thứ Sáu được không?"),
  ("I'm not sure about that. Let me check and get back to you.", "Tôi chưa chắc điểm đó. Để tôi kiểm tra rồi trả lời anh."),
  ("Who will be our main contact?", "Ai sẽ là đầu mối liên hệ chính?"),
 ],
 "dialogues": [
  ("Can you explain the approval process in Vietnam?", [
    ("Sure. In short, there are three steps: the investment registration, the company registration and then the other licences. I'll send you a timeline after the call.", True, "Tóm tắt theo bước + gửi văn bản sau."),
    ("It's very complicated, you cannot understand.", False, "Thiếu tôn trọng — hãy giải thích đơn giản."),
    ("Process is long long.", False, "Lặp từ kiểu tiếng Việt, không có thông tin."),
  ]),
  ("Is this clause enforceable in Vietnam?", [
    ("I'm not sure yet. Let me check with our senior lawyer and get back to you by tomorrow.", True, "Trung thực khi chưa chắc + hẹn thời gian — tránh khẳng định pháp lý vội."),
    ("Yes, 100 percent.", False, "Khẳng định chắc chắn khi chưa kiểm tra — rủi ro nghề nghiệp."),
    ("I don't know that.", False, "Trả lời cụt, không đề nghị kiểm tra."),
  ]),
  ("Can we have a fee quote before we start?", [
    ("Of course. After the conflict check, we'll send you a fee quote and an engagement letter.", True, "Đồng ý + đúng trình tự nghề (kiểm tra xung đột → báo phí → thư thoả thuận)."),
    ("Fee is cheap, don't worry.", False, "Không đáp ứng yêu cầu báo phí bằng văn bản."),
    ("We start first, fee later.", False, "Sai trình tự — khách cần biết phí trước."),
  ]),
  ("Sorry, could you speak a bit more slowly? The connection is bad.", [
    ("Of course, sorry about that. I'll speak more slowly and type the key points in the chat.", True, "Xin lỗi + điều chỉnh + hỗ trợ bằng chữ."),
    ("OK, I speak slow.", False, "Thiếu 'will' và sai từ loại ('I'll speak more slowly')."),
    ("My English is bad, sorry sorry.", False, "Tự hạ mình và lặp từ — chỉ cần điều chỉnh tốc độ."),
  ]),
  ("What are the next steps?", [
    ("We'll send the summary today. You'll review the draft by Wednesday, and we'll meet again on Friday.", True, "Việc + người làm + hạn cho từng bước."),
    ("Next step we do more.", False, "Mơ hồ, sai trật tự."),
    ("I will think and tell you.", False, "Không chốt được bước tiếp theo."),
  ]),
 ],
 "listen": [
  ("Thank you for joining the call today", ["joining", "call"], "mở đầu cuộc gọi"),
  ("We need to run a conflict check first", ["conflict", "check"], "kiểm tra xung đột lợi ích"),
  ("Please sign the engagement letter so we can start", ["engagement", "start"], "thư thoả thuận dịch vụ"),
  ("Could you send us a fee quote", ["fee", "quote"], "xin báo phí"),
  ("Let me confirm the next steps. We will send a summary today. Your team will review the draft by Wednesday.", ["confirm", "summary", "Wednesday"], "chốt bước tiếp theo"),
  ("I am not sure how this works under local law. Let me check with our partner. I will get back to you tomorrow.", ["local", "partner", "tomorrow"], "trả lời khi chưa chắc"),
 ],
})

# ───────────────────────── 9. Hạn chót & nhắc hạn ─────────────────────────
PHASES.append({
 "title": "Hạn chót & nhắc hạn",
 "vocab": [
  ("deadline", "/ˈdedlaɪn/", "n", "hạn chót", "The <b>deadline</b> for the annual report is next Friday.", "Hạn chót nộp báo cáo năm là thứ Sáu tuần sau.", "締め切り", "shimekiri"),
  ("due date", "/ˈdjuː ˌdeɪt/", "n", "ngày đến hạn", "The <b>due date</b> is in the tracker.", "Ngày đến hạn có trong bảng theo dõi.", "期日", "kijitsu"),
  ("reminder", "/rɪˈmaɪndə/", "n", "lời nhắc", "I'll set a <b>reminder</b> one month before the permit expires.", "Tôi sẽ đặt lời nhắc trước khi giấy phép hết hạn một tháng.", "リマインダー", "rimaindā"),
  ("filing", "/ˈfaɪlɪŋ/", "n", "việc nộp hồ sơ, báo cáo (cho cơ quan nhà nước)", "This <b>filing</b> must be done online.", "Hồ sơ này phải nộp trực tuyến.", "届出", "todokede"),
  ("submit", "/səbˈmɪt/", "v", "nộp", "Please <b>submit</b> the form by 5 p.m.", "Vui lòng nộp tờ khai trước 5 giờ chiều.", "提出する", "teishutsu suru"),
  ("late submission", "/ˌleɪt səbˈmɪʃn/", "n", "việc nộp muộn", "A <b>late submission</b> may lead to a fine.", "Nộp muộn có thể bị phạt."),
  ("working day", "/ˈwɜːkɪŋ ˌdeɪ/", "n", "ngày làm việc", "The result will be ready in five <b>working days</b>, not counting weekends.", "Kết quả có sau năm ngày làm việc, không tính cuối tuần.", "営業日", "eigyōbi"),
  ("annual report", "/ˌænjuəl rɪˈpɔːt/", "n", "báo cáo năm (định kỳ)", "Foreign-owned companies have several <b>annual reports</b> to file.", "Doanh nghiệp vốn nước ngoài có nhiều loại báo cáo năm phải nộp.", "年次報告", "nenji hōkoku"),
  ("tracker", "/ˈtrækə/", "n", "bảng theo dõi", "I update the deadline <b>tracker</b> every Monday.", "Thứ Hai nào tôi cũng cập nhật bảng theo dõi hạn."),
  ("timeline", "/ˈtaɪmlaɪn/", "n", "mốc thời gian, lịch trình", "Here is the <b>timeline</b> for the licence renewal.", "Đây là lịch trình gia hạn giấy phép."),
 ],
 "phrases": [
  ("The deadline is this Friday.", "Hạn chót là thứ Sáu này."),
  ("We have three filings due this month.", "Tháng này có ba hồ sơ đến hạn nộp."),
  ("I'll send you a reminder two weeks before.", "Tôi sẽ nhắc anh trước hai tuần."),
  ("Can we ask for more time if we're late?", "Nếu trễ thì mình có xin thêm thời gian được không?"),
  ("Please count working days, not calendar days.", "Vui lòng tính ngày làm việc, không phải ngày lịch."),
  ("Public holidays are not working days.", "Ngày lễ không phải ngày làm việc."),
  ("Let's submit it two days early, just in case.", "Mình nộp sớm hai ngày cho chắc."),
  ("I've added this deadline to the tracker.", "Tôi đã thêm hạn này vào bảng theo dõi."),
  ("What happens if we miss the deadline?", "Nếu lỡ hạn thì sao?"),
  ("We submitted it on time. Here's the confirmation.", "Chúng tôi đã nộp đúng hạn. Đây là xác nhận."),
 ],
 "dialogues": [
  ("When is the deadline for the work permit renewal?", [
    ("It must be submitted within a set period before it expires. I'll check the exact rule and put the date in the tracker.", True, "Nêu nguyên tắc chung (nộp trong khoảng thời gian luật định trước khi hết hạn) + kiểm tra quy định + ghi vào bảng theo dõi."),
    ("Before it expire, anytime.", False, "Thiếu 's' ('expires') và sai — phải nộp trước một khoảng thời gian theo quy định."),
    ("Deadline is when you remember.", False, "Vô trách nhiệm, không có mốc cụ thể."),
  ]),
  ("We missed the filing deadline yesterday. What now?", [
    ("Let's submit it today and explain the reason in writing. I'll also check with our lawyer if there's any penalty.", True, "Khắc phục ngay + giải trình + kiểm tra hậu quả với luật sư."),
    ("Nobody will know, forget it.", False, "Che giấu vi phạm — rủi ro lớn hơn khi bị kiểm tra."),
    ("It's not my fault, I was busy.", False, "Bào chữa thay vì giải quyết."),
  ]),
  ("Does 'ten working days' include Saturday?", [
    ("No. Working days are usually Monday to Friday, and public holidays don't count.", True, "Giải thích rõ cách tính ngày làm việc."),
    ("Yes, every day is working day.", False, "Sai khái niệm, thiếu mạo từ ('a working day')."),
    ("Maybe include, maybe not.", False, "Mơ hồ, sai ngữ pháp."),
  ]),
  ("Can you remind me about the visa renewal?", [
    ("Sure. I'll send you a reminder one month before the expiry date and again one week before.", True, "Đồng ý + lịch nhắc cụ thể hai lần."),
    ("OK, I remember for you.", False, "Dùng sai 'remember' — đúng là 'remind'."),
    ("You should remember yourself.", False, "Thiếu hợp tác và sai ('remember it yourself')."),
  ]),
  ("Are we on track for the month-end filings?", [
    ("Yes. Two are submitted, and the last one is ready. I'll submit it tomorrow morning.", True, "Tình trạng từng hồ sơ + việc còn lại + thời gian."),
    ("On track, on track.", False, "Lặp từ, không có chi tiết."),
    ("I think yes, but I don't check.", False, "Sai thì ('I haven't checked') và chưa kiểm tra mà đã trả lời."),
  ]),
 ],
 "listen": [
  ("The deadline for this report is next Friday", ["deadline", "Friday"], "hạn nộp báo cáo"),
  ("Please count working days, not calendar days", ["working", "calendar"], "cách tính ngày"),
  ("I will send you a reminder next week", ["reminder", "week"], "hẹn nhắc"),
  ("We submitted the form on time", ["submitted", "time"], "báo đã nộp"),
  ("This month we have three filings. Two are already submitted. The last one is due on the twenty-eighth.", ["filings", "submitted", "due"], "tình trạng hồ sơ trong tháng"),
  ("Your work permit expires in two months. We need your documents by next week. Please do not miss this deadline.", ["expires", "documents", "miss"], "nhắc gia hạn giấy phép"),
 ],
})

# ───────────────────────── Vai trong ngành ─────────────────────────
ROLES = {
 "inhouse": {"label": "Pháp chế doanh nghiệp", "emoji": "⚖️",
  "scenarios": [
   ("ih_review", "Góp ý hợp đồng cho sếp", "You are my foreign general director. I am the in-house legal officer. Ask me about the main risks in a new supplier contract and whether we can sign it this week."),
   ("ih_policy", "Giải thích chính sách quà tặng", "You are a foreign sales manager. A supplier wants to give you an expensive gift. Ask me what the company gift policy says and what you should do."),
   ("ih_permit", "Nhắc gia hạn giấy phép lao động", "You are a busy foreign engineer. Your work permit expires soon. I am the legal officer. Say you are too busy at first, then agree to send the documents by a date."),
   ("ih_nda", "Chuẩn bị NDA với đối tác", "You are a foreign business development manager. You will meet a new partner tomorrow and want to share prices. Ask me if we need an NDA and how fast I can prepare it."),
  ],
  "dialogues": [
   ("Can we sign this supplier contract today?", [
     ("Not yet. The payment and liability clauses are risky for us. I'll send my comments by noon, and we can sign after they agree.", True, "Nêu rủi ro chính + thời gian + điều kiện ký."),
     ("Yes, contract is standard.", False, "Thiếu mạo từ và cho ký khi chưa rà soát kỹ."),
     ("I don't read yet.", False, "Sai thì ('I haven't read it yet') và không hẹn thời gian.")]),
   ("A supplier sent me a very expensive watch. Can I keep it?", [
     ("I'm afraid not. Our gift policy doesn't allow expensive gifts. Please return it politely, and I'll help you write the note.", True, "Nêu chính sách + cách xử lý + hỗ trợ."),
     ("Keep it, nobody know.", False, "Vi phạm chính sách, thiếu 's' ('knows')."),
     ("Watch is nice, lucky you.", False, "Không trả lời câu hỏi về tuân thủ.")]),
   ("Do we need an NDA for tomorrow's meeting?", [
     ("Yes, because you'll share our prices. I can send a short NDA today, and they can sign it before the meeting.", True, "Có + lý do + giải pháp nhanh."),
     ("No need, they are nice people.", False, "Cảm tính — bảo mật không dựa vào 'người tốt'."),
     ("NDA take long time.", False, "Thiếu 's' ('takes') và không đưa giải pháp.")]),
   ("A labour inspector wants to visit next week. What should we prepare?", [
     ("Labour contracts, the internal labour rules, payroll and social insurance records. I'll make a checklist today.", True, "Liệt kê hồ sơ chính + lập danh sách kiểm tra."),
     ("Prepare coffee and fruit.", False, "Đùa không đúng lúc, không trả lời về hồ sơ."),
     ("Inspector come, we hide the files.", False, "Sai nghiêm trọng — che giấu hồ sơ là vi phạm.")]),
   ("Our work permit list is a mess. Whose permit expires first?", [
     ("Mr. Kim's permit expires in six weeks. I've started his renewal and put all the dates in the tracker.", True, "Thông tin cụ thể + đã hành động + công cụ theo dõi."),
     ("Many people expire soon.", False, "Mơ hồ; 'people expire' dùng sai — giấy phép mới hết hạn."),
     ("I will check someday.", False, "Không có thời hạn, thiếu trách nhiệm.")]),
   ("Just give me a quick answer. Is this legal or not?", [
     ("In general, it's possible, but it depends on the details. Let me check the current regulations and confirm by this afternoon.", True, "Trả lời có kiểm soát + hẹn giờ — không khẳng định pháp lý vội."),
     ("Legal, legal, go ahead.", False, "Lặp từ và khẳng định bừa."),
     ("Law is very difficult, I can't say.", False, "Né tránh, không đề nghị kiểm tra.")]),
  ]},
 "firm": {"label": "Trợ lý luật sư · Công ty luật", "emoji": "💼",
  "scenarios": [
   ("lf_intake", "Tiếp khách hàng mới", "You are a foreign investor calling a Vietnamese law firm for the first time. You want to open a small company. I am the legal assistant. Ask what we can help with, the steps and the fees."),
   ("lf_partner", "Báo cáo luật sư điều hành", "You are the foreign partner of our law firm. Ask me for an update on three client files, and ask what I need from you."),
   ("lf_docs", "Nhắc khách gửi giấy tờ", "You are a busy foreign client. You still haven't sent your documents for a company change. I call to remind you. Give excuses, then agree to a date."),
   ("lf_billing", "Giải thích phí dịch vụ", "You are a client who thinks our invoice is too high. Ask me to explain the hours and the extra work."),
  ],
  "dialogues": [
   ("Can you tell me the status of my file?", [
     ("Sure. We submitted it on Monday. The authority is reviewing it, and we expect the result next week.", True, "Ngày nộp + trạng thái + dự kiến."),
     ("Your file is processing.", False, "Sai bị động ('is being processed') và thiếu thông tin cụ thể."),
     ("I must ask lawyer.", False, "Thiếu mạo từ và không cập nhật gì.")]),
   ("Why is my invoice higher than the quote?", [
     ("The quote covered the registration only. The extra hours were for the two contract reviews you asked for in May. I'll send you the breakdown.", True, "Giải thích nguyên nhân + dẫn chứng + gửi chi tiết."),
     ("Because more work, more money.", False, "Cộc, thiếu giải thích cụ thể."),
     ("Invoice is correct, you must pay.", False, "Thiếu thiện chí, không giải thích.")]),
   ("Can I meet a lawyer tomorrow?", [
     ("Let me check. Ms. Hà is free at 10 a.m. or 3 p.m. Which time works for you?", True, "Kiểm tra + đưa lựa chọn cụ thể."),
     ("Lawyer busy, no.", False, "Cộc lốc, thiếu động từ."),
     ("Tomorrow maybe, you call again.", False, "Mơ hồ, bắt khách gọi lại.")]),
   ("Please prepare the documents for the client meeting.", [
     ("Will do. I'll print the draft, the timeline and the fee quote, and put them in the meeting room by 9.", True, "Nhận việc + liệt kê + thời gian."),
     ("OK, what documents?", False, "Hỏi lại vì chưa đọc hồ sơ — nên chủ động đề xuất."),
     ("I prepare already maybe.", False, "Mơ hồ, sai thì.")]),
   ("Did you run the conflict check for the new client?", [
     ("Yes. There's no conflict. The new client isn't related to any of our current cases.", True, "Xác nhận + kết quả rõ ràng."),
     ("Conflict? We have no fight.", False, "Hiểu sai 'conflict check' là cãi nhau — đây là kiểm tra xung đột lợi ích."),
     ("I will check after we start.", False, "Sai trình tự — phải kiểm tra trước khi nhận việc.")]),
   ("The client wants the draft today. Can we make it?", [
     ("We can send the first draft by 6 p.m., but the tax part needs one more day. I'll tell the client now.", True, "Cam kết thực tế + nêu phần cần thêm thời gian + chủ động báo khách."),
     ("Yes sure, no problem.", False, "Hứa vội khi chưa đánh giá khối lượng."),
     ("Today impossible.", False, "Cộc lốc, không đưa phương án.")]),
  ]},
 "onestop": {"label": "Cán bộ một cửa · Hồ sơ", "emoji": "🏛️",
  "scenarios": [
   ("os_workpermit", "Tiếp nhận hồ sơ giấy phép lao động", "You are a foreign engineer at the one-stop counter. You want to submit your work permit file. I am the officer. Your health certificate is too old. Ask what to do and when to come back."),
   ("os_card", "Người nước ngoài hỏi thẻ tạm trú", "You are a foreign teacher. You want a temporary residence card. I am the officer at the counter. Ask what documents you need and how long it takes."),
   ("os_upset", "Khách bực vì phải đi lại nhiều lần", "You are a foreign business owner. This is your third visit because of missing papers. You are upset. I am the officer. Let me explain and help you."),
   ("os_collect", "Trả kết quả hồ sơ", "You are a foreign manager coming to collect your company's registration result. You forgot your receipt. Ask me what you can do."),
  ],
  "dialogues": [
   ("This is my third time here. Why didn't you tell me everything last time?", [
     ("I'm really sorry. Let me check your whole file now and write down everything that's missing, so you only need to come back once.", True, "Xin lỗi chân thành + kiểm tra toàn bộ + danh sách bằng văn bản."),
     ("Not my fault, you bring wrong.", False, "Đổ lỗi, sai thì ('you brought the wrong papers')."),
     ("Rules change, I don't know.", False, "Né tránh trách nhiệm, không hỗ trợ.")]),
   ("Can I submit this without the translation?", [
     ("I'm sorry, but we need a certified Vietnamese translation. There's a translation office nearby if you need one.", True, "Từ chối lịch sự + gợi ý giải pháp."),
     ("No translation, no.", False, "Cộc lốc, không hướng dẫn."),
     ("OK, I translate for you.", False, "Cán bộ không thể tự dịch thay cho bản dịch có chứng thực.")]),
   ("I forgot my receipt. Can I still collect my result?", [
     ("Please show me your passport. I'll look up your file in the system, and you may need to sign a confirmation.", True, "Có hướng xử lý + xác minh danh tính."),
     ("No receipt, come back tomorrow.", False, "Cứng nhắc, chưa thử cách khác."),
     ("You careless, you lose.", False, "Thiếu động từ và trách khách.")]),
   ("How long will it take?", [
     ("The processing time is on your receipt. If there's any problem, we'll call the phone number on your form.", True, "Dựa vào biên nhận + cam kết liên hệ."),
     ("I don't know, it depends.", False, "Trả lời cụt, không cho thông tin."),
     ("Fast, you go home and wait.", False, "Mơ hồ, cộc lốc.")]),
   ("Can I pay the fee by card?", [
     ("Yes, you can pay by card or bank transfer at counter 5. Please keep the payment receipt.", True, "Trả lời + nơi thanh toán + nhắc giữ chứng từ."),
     ("Card no, cash only maybe.", False, "Mơ hồ, sai trật tự."),
     ("You ask the other counter.", False, "Đùn đẩy, không chỉ rõ quầy nào.")]),
   ("Is there anyone here who speaks English?", [
     ("I can help you in English. Please take a seat and tell me what you need.", True, "Chủ động hỗ trợ, thân thiện."),
     ("English little, wait.", False, "Cụt ngủn — nên nói 'I speak a little English. How can I help?'"),
     ("No, only Vietnamese here.", False, "Thiếu thiện chí — nên cố gắng hỗ trợ hoặc tìm người giúp.")]),
  ]},
 "translator": {"label": "Phiên dịch · Dịch thuật công chứng", "emoji": "🗣️",
  "scenarios": [
   ("tr_meeting", "Phiên dịch buổi họp", "You are a foreign director in a meeting with a Vietnamese partner. I am your interpreter. Speak in long sentences at first, then agree to pause after each point."),
   ("tr_notary", "Khách đến dịch công chứng", "You are a foreign customer at a translation and notary office. You need your degree and passport translated. Ask about the price, the time and whether you need to come back."),
   ("tr_term", "Làm rõ thuật ngữ với luật sư", "You are a foreign lawyer. I am translating your contract into Vietnamese. I ask you about two legal terms. Explain them simply."),
   ("tr_error", "Khách phát hiện bản dịch sai", "You are a foreign client. You found a wrong date in your translated document. You are worried because you must submit it tomorrow. Ask me to fix it quickly."),
  ],
  "dialogues": [
   ("Could you translate everything I say, word for word?", [
     ("I'll translate everything accurately. Sometimes I'll change the word order so it sounds natural in Vietnamese, but I won't change the meaning.", True, "Cam kết chính xác + giải thích cách dịch tự nhiên."),
     ("Word for word is impossible.", False, "Phủ nhận cụt, không giải thích."),
     ("Yes, I translate exactly every word.", False, "Dịch từng chữ thường làm câu tiếng Việt khó hiểu; thiếu 'will'.")]),
   ("How much is the translation of a two-page contract?", [
     ("It depends on the language and the number of words. For this one, I can give you a price in five minutes.", True, "Giải thích cách tính + báo giá nhanh."),
     ("Very cheap, don't worry.", False, "Không có giá cụ thể."),
     ("Price is many.", False, "Sai ngữ pháp và không trả lời.")]),
   ("What does 'force majeure' mean in Vietnamese?", [
     ("It's 'bất khả kháng' — events that nobody can control, like natural disasters.", True, "Thuật ngữ chuẩn + giải thích ngắn."),
     ("Force is strong, majeure is big.", False, "Dịch từng chữ, sai nghĩa pháp lý."),
     ("I don't know French.", False, "Né tránh — đây là thuật ngữ pháp lý phổ biến.")]),
   ("The date on this translation is wrong. I need it tomorrow.", [
     ("I'm very sorry. I'll correct it now and have it certified again. It will be ready by 4 p.m. today.", True, "Xin lỗi + sửa + chứng thực lại + hạn cụ thể."),
     ("Only one date wrong, it's OK.", False, "Sai ngày trên giấy tờ có thể khiến hồ sơ bị trả lại."),
     ("Tomorrow I fix.", False, "Trật tự từ kiểu Việt và không kịp hạn của khách.")]),
   ("Sorry, I talked for too long. Did you get all that?", [
     ("Most of it. Could you repeat the part about the payment date? I want to be accurate.", True, "Thẳng thắn + hỏi lại phần cụ thể vì độ chính xác."),
     ("Yes, yes, all.", False, "Giả vờ hiểu hết — dễ dịch thiếu ý."),
     ("You speak too long, I forget.", False, "Trách người nói, sai thì ('you spoke').")]),
   ("Can you sign the translation as the translator?", [
     ("Yes. I'll sign it, and then the notary office will certify my signature.", True, "Đúng quy trình: người dịch ký, rồi cơ quan chứng thực chữ ký."),
     ("I sign, then you sign, no need office.", False, "Bỏ qua bước chứng thực, sai ngữ pháp."),
     ("Signature is not my job.", False, "Sai — người dịch phải ký vào bản dịch.")]),
  ]},
}

PACK = {
 "id": "legal",
 "label": "Luật · Hành chính công",
 "short": "Pháp lý",
 "emoji": "⚖️",
 "desc": "Pháp chế · công ty luật · một cửa · phiên dịch công chứng",
 "persona": "a Vietnamese legal and public administration worker",
 "counterpart": "a foreign client, lawyer or applicant",
 "context": "legal and public administration",
 "core": [6, 3],
 "report": {
  "title": "Báo cáo hồ sơ 60 giây", "short": "Báo cáo hồ sơ", "sub": "Nói như lúc cập nhật cho sếp cuối ngày 🎙️",
  "steps": [["Files", "Today I submitted two work permit files …"], ["Pending", "Mr. Kim's file is still missing … / Nothing pending."], ["Deadlines", "Next week, three visas expire …"]],
  "kind": "legal file status update",
  "structure": "files handled today / what is pending or missing / upcoming deadlines",
  "sample": "Today I submitted two work permit files and reviewed one supplier contract. Mr. Kim's file is still missing his health certificate, and we are waiting for the partner's comments on the NDA. Next week, three visas expire, so I will send reminders on Monday.",
 },
 "podcast": "Podcast pháp lý",
 "game_tag": "Game anime: đánh quái giấy tờ, hạ boss hồ sơ thiếu",
 "reverse_tag": "kiểu pháp lý",
 "jd_placeholder": "VD: Pháp chế cho công ty FDI Hàn Quốc ở Bắc Ninh, làm giấy phép lao động, visa cho chuyên gia, rà soát hợp đồng…",
 "rw_placeholder": "VD: hồ sơ giấy phép lao động thiếu phiếu lý lịch tư pháp, visa hết hạn tuần sau",
 "quips": [
  "Original and one copy, please!",
  "Check the expiry date!",
  "Read before you sign!",
  "Deadline in the tracker!",
  "Track changes: on!",
  "Confidential — no forwarding!",
  "File complete, here's your receipt!",
  "Initial every page!",
  "Let me check and get back to you!",
  "No NDA, no secrets!",
 ],
 "ai": [
  ("counter", "Tiếp khách ở quầy một cửa", "You are a foreign resident at a one-stop public service counter. I am the officer. You want to submit a document, but you don't know which form to use. Ask simple questions about documents, time and fees."),
  ("workpermit", "Hồ sơ giấy phép lao động", "You are a foreign engineer who just joined a Vietnamese company. I am the HR and legal officer. Ask what documents you need for your work permit and how long it takes."),
  ("visa_ext", "Gia hạn visa gấp", "You are a foreign manager whose visa expires in ten days. You are worried. I am the company's legal assistant. Ask what we can do and whether you can travel next week."),
  ("contract_review", "Báo cáo rà soát hợp đồng", "You are my foreign director. I reviewed a service contract. Ask me about the main risks, the payment terms and whether we can sign it this week."),
  ("foreign_lawyer", "Họp với luật sư nước ngoài", "You are a lawyer from an overseas law firm. You call our Vietnamese team about a client's new company. Ask about the steps in Vietnam, the timeline and who will be the main contact."),
  ("nda", "Đối tác hỏi về NDA", "You are a manager at a foreign partner company. We sent you an NDA. Ask why you need to sign it, how long it lasts and whether you can change one clause."),
  ("translation", "Khách đặt dịch công chứng", "You are a foreign customer at a translation and notary office. You need your marriage certificate translated for a visa. Ask about the price, the time and what you need to bring."),
  ("deadline", "Nhắc hạn cho khách", "You are a busy foreign client. I call to remind you about a filing deadline next week. Say you forgot, ask what documents I need and agree on a date."),
 ],
 "rev": [
  ("Hồ sơ của anh còn thiếu một giấy tờ.", "Your file is missing one document."),
  ("Vui lòng mang bản gốc và một bản sao.", "Please bring the original and one copy."),
  ("Visa của anh hết hạn vào thứ Sáu tới.", "Your visa expires next Friday."),
  ("Công ty anh là bên bảo lãnh.", "Your company is the sponsor."),
  ("Chưa có giấy phép thì chưa được làm việc.", "You can't start work before the permit is issued."),
  ("Giấy tờ nước ngoài cần hợp pháp hoá lãnh sự.", "Foreign documents need consular legalization."),
  ("Tên trên bản dịch bị sai chính tả.", "The name on the translation is misspelled."),
  ("Anh ký nháy từng trang giúp tôi.", "Please initial every page."),
  ("Tôi đã rà soát bản dự thảo.", "I've reviewed the draft."),
  ("Vui lòng bật chế độ theo dõi thay đổi.", "Please turn on track changes."),
  ("Thông tin này là thông tin mật.", "This information is confidential."),
  ("Để tôi kiểm tra rồi trả lời anh.", "Let me check and get back to you."),
  ("Hạn chót là thứ Sáu này.", "The deadline is this Friday."),
  ("Kết quả có sau năm ngày làm việc.", "The result will be ready in five working days."),
 ],
 "reading": [
  {"t": "Receipt of application", "text": "RECEIPT OF APPLICATION\nApplicant: Kim Min-jun\nProcedure: Work permit (new)\nReceived: 12 March, 09:40\nDocuments: 7 of 8 — health certificate missing (please submit by 15 March)\nResult date: 26 March\nCollect at: Counter 3. Bring this receipt and your passport.", "q": [
    {"q": "Which document is missing?", "o": ["The passport", "The health certificate", "The degree"], "a": 1},
    {"q": "What must he bring to collect the result?", "o": ["The receipt and his passport", "Two photos", "His labour contract"], "a": 0}]},
  {"t": "Visa reminder email", "text": "Dear Mr. Lopez,\nThis is a reminder that your visa expires on 30 June. To apply for a temporary residence card, please send us by 10 June:\n- a scan of your passport\n- two passport photos\n- your signed application form\nThe immigration office will keep your passport for several working days. Please avoid travel from 12 to 25 June.\nBest regards,\nLegal Team", "q": [
    {"q": "When is the deadline to send the documents?", "o": ["30 June", "10 June", "25 June"], "a": 1},
    {"q": "Why should Mr. Lopez not travel in mid-June?", "o": ["His passport will be at the immigration office", "The office will be closed", "His visa has already expired"], "a": 0}]},
  {"t": "Contract review note", "text": "CONTRACT REVIEW – Supply Agreement with Blue River Trading\nSummary: low risk overall.\nIssue 1 (Clause 8): Liability is unlimited. Suggest a cap equal to the contract value.\nIssue 2 (Clause 11): The governing law is not stated. Suggest Vietnamese law.\nIssue 3 (Annex 2): The prices in USD and VND do not match.\nRecommendation: Sign after the supplier accepts these changes.", "q": [
    {"q": "What is the problem in Clause 8?", "o": ["The price is too high", "Liability has no limit", "The date is wrong"], "a": 1},
    {"q": "When does the reviewer recommend signing?", "o": ["Today", "Never", "After the supplier accepts the changes"], "a": 2}]},
  {"t": "NDA reminder", "text": "Hi team,\nWe will meet Green Valley Foods on Thursday. Before the meeting:\n1. They must sign our NDA (sent on Monday).\n2. Share only the summary slides, not the full price list.\n3. Send files as password-protected PDFs.\nPlease don't forward any files outside the company.\nThanks,\nLan – Legal", "q": [
    {"q": "What can the team share at the meeting?", "o": ["The full price list", "The summary slides", "The client list"], "a": 1},
    {"q": "How should files be sent?", "o": ["As password-protected PDFs", "By personal email", "On paper only"], "a": 0}]},
  {"t": "Deadline tracker", "text": "LEGAL DEADLINE TRACKER – October\n05 Oct: Labour report – SUBMITTED\n15 Oct: Work permit renewal, Mr. Tanaka – documents missing\n20 Oct: Trademark renewal – ready to file\n31 Oct: Visa expiry, Ms. Evans – extension submitted\nNote: Count working days only.", "q": [
    {"q": "Which task has missing documents?", "o": ["The trademark renewal", "The labour report", "Mr. Tanaka's work permit renewal"], "a": 2},
    {"q": "What is the status of Ms. Evans's visa?", "o": ["The extension is submitted", "It has already expired", "Nothing has been done"], "a": 0}]},
 ],
 "events": [
  ("client_meeting", "Họp khách hàng nước ngoài", "You are a foreign client meeting our legal team next week about opening a company in Vietnam. Ask about the steps, the timeline, the documents and the fees."),
  ("signing", "Buổi ký hợp đồng", "You are the foreign director of our partner company. We will sign a contract tomorrow. Ask about the final version, the bilingual text, who signs and how many originals we need."),
  ("negotiation", "Đàm phán điều khoản hợp đồng", "You are the partner's foreign lawyer. We will negotiate a supply contract next week. Push for a high penalty and unlimited liability, then agree to a compromise."),
  ("inspection", "Đoàn kiểm tra hồ sơ lao động", "You are an inspector from the local labour authority visiting our company next week. Ask about work permits for foreign staff, labour contracts and the internal labour rules."),
  ("interpreting", "Phiên dịch buổi làm việc quan trọng", "You are a foreign investor at an important meeting with a local authority tomorrow. I am your interpreter. Ask me how we will work together, then say one long point for me to interpret."),
  ("interview", "Phỏng vấn vị trí pháp chế", "You are the foreign HR director of an FDI company interviewing me for an in-house legal officer job. Ask about my experience with contracts, work permits and a difficult deadline I handled."),
  ("other", "Khác", ""),
 ],
 "roles": ROLES,
 "phases": PHASES,
}
