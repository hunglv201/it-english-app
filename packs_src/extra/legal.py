# -*- coding: utf-8 -*-
# v4.1 — nội dung làm giàu cho gói legal (nối vào cuối gói, xem build.py)
# 8 chặng mới: email & công văn · tuân thủ & chính sách nội bộ · dữ liệu cá nhân · lao động & nội quy ·
# sở hữu trí tuệ cơ bản · tranh chấp & hoà giải · thuế & hoá đơn (thủ tục) · phiên dịch trong buổi làm việc.
# Không khẳng định điều luật / mức phạt / thời hạn cụ thể. Tên người, công ty là tên tự đặt.

PHASES = []

# ───────────────────────── A. Email & công văn pháp lý ─────────────────────────
PHASES.append({
 "title": "Email & công văn pháp lý",
 "vocab": [
  ("attachment", "/əˈtætʃmənt/", "n", "tệp đính kèm", "Please find the draft in the <b>attachment</b>.", "Bản dự thảo nằm trong tệp đính kèm.", "添付ファイル", "tenpu fairu"),
  ("regarding", "/rɪˈɡɑːdɪŋ/", "prep", "về việc, liên quan đến", "I'm writing <b>regarding</b> your work permit renewal.", "Tôi viết thư về việc gia hạn giấy phép lao động của anh."),
  ("enclosed", "/ɪnˈkləʊzd/", "adj", "được gửi kèm (theo thư)", "The signed contract is <b>enclosed</b>.", "Hợp đồng đã ký được gửi kèm theo.", "同封の", "dōfū no"),
  ("follow up", "/ˌfɒləʊ ˈʌp/", "phr v", "hỏi lại, theo dõi tiếp", "I'm writing to <b>follow up</b> on my email from last week.", "Tôi viết thư để hỏi lại về email tuần trước."),
  ("official letter", "/əˌfɪʃl ˈletə/", "n", "công văn", "The authority sent an <b>official letter</b> asking for more documents.", "Cơ quan gửi công văn yêu cầu bổ sung giấy tờ.", "公文書", "kōbunsho"),
  ("notice", "/ˈnəʊtɪs/", "n", "thông báo (chính thức)", "We received a <b>notice</b> from the tax office.", "Chúng tôi nhận được thông báo từ cơ quan thuế.", "通知", "tsūchi"),
  ("acknowledge", "/əkˈnɒlɪdʒ/", "v", "xác nhận (đã nhận)", "Please <b>acknowledge</b> receipt of this email.", "Vui lòng xác nhận đã nhận email này."),
  ("cc", "/ˌsiː ˈsiː/", "v", "đồng gửi (cc)", "Please <b>cc</b> our lawyer on all emails.", "Vui lòng cc luật sư của chúng tôi trong mọi email."),
  ("formal", "/ˈfɔːml/", "adj", "trang trọng", "Use a <b>formal</b> tone when you write to the authority.", "Dùng giọng trang trọng khi viết cho cơ quan nhà nước."),
  ("disclaimer", "/dɪsˈkleɪmə/", "n", "tuyên bố miễn trừ (cuối email)", "Our email <b>disclaimer</b> says the message is confidential.", "Tuyên bố miễn trừ trong email của chúng tôi ghi rằng thư này là thông tin mật.", "免責事項", "menseki jikō"),
 ],
 "phrases": [
  ("I'm writing regarding your visa extension.", "Tôi viết thư về việc gia hạn visa của anh."),
  ("Please find the signed contract attached.", "Hợp đồng đã ký được đính kèm."),
  ("Could you confirm receipt of this email?", "Anh xác nhận giúp đã nhận email này nhé?"),
  ("I'm following up on my email from Monday.", "Tôi hỏi lại về email hôm thứ Hai."),
  ("We look forward to your reply.", "Chúng tôi mong nhận được phản hồi của anh."),
  ("Please let us know if you have any questions.", "Nếu có câu hỏi, vui lòng cho chúng tôi biết."),
  ("I've copied our lawyer on this email.", "Tôi đã cc luật sư của chúng tôi trong email này."),
  ("We received an official letter from the authority today.", "Hôm nay chúng tôi nhận được công văn của cơ quan."),
  ("Please reply by 5 p.m. on Thursday.", "Vui lòng phản hồi trước 5 giờ chiều thứ Năm."),
  ("Sorry for the late reply.", "Xin lỗi vì phản hồi trễ."),
 ],
 "dialogues": [
  ("How should I start an email to the foreign lawyer?", [
    ("Start with 'Dear Mr. Smith,' and then say why you're writing, for example 'I'm writing regarding the draft contract.'", True, "Chào trang trọng + nêu mục đích ngay câu đầu."),
    ("Hi bro, about contract…", False, "Quá suồng sã với luật sư đối tác."),
    ("I write this email for you know…", False, "Dịch từng chữ 'để anh biết' — nghe lủng củng; nên nêu thẳng mục đích."),
  ]),
  ("The client hasn't replied for a week. What should I do?", [
    ("Let's send a short follow-up email today and call them if there's no reply by Thursday.", True, "Nhắc lại lịch sự + mốc gọi điện."),
    ("Wait, maybe they busy.", False, "Thiếu 'are' và thụ động — có hạn chót thì phải chủ động nhắc."),
    ("Send email: why you not reply?", False, "Giọng trách móc, sai cấu trúc câu hỏi ('Why haven't you replied?')."),
  ]),
  ("We got an official letter from the labour department. What does it say?", [
    ("They're asking for two more documents for Mr. Lee's file, and the letter gives us ten working days to reply.", True, "Tóm tắt nội dung + hạn trả lời ghi trong công văn."),
    ("It says many things, very long.", False, "Không tóm tắt được ý chính."),
    ("Letter is Vietnamese, you cannot read.", False, "Không giúp — nên tóm tắt bằng tiếng Anh."),
  ]),
  ("Did you attach the file?", [
    ("Sorry, I forgot. I've just sent it again with the attachment.", True, "Xin lỗi ngắn + đã khắc phục."),
    ("I attach already, you check again.", False, "Sai thì ('I've attached it') và đổ cho người nhận."),
    ("File too big, cannot.", False, "Cộc, không đưa giải pháp (chia nhỏ file, gửi đường link)."),
  ]),
  ("Should I cc the director on this email?", [
    ("Yes, because it's about the contract deadline. But please keep the message short and clear.", True, "Trả lời + lý do + lưu ý."),
    ("Cc everybody, more safe.", False, "Cc tràn lan dễ lộ thông tin; sai so sánh ('safer')."),
    ("No, director don't read email.", False, "Sai 'doesn't' và phán đoán vô căn cứ."),
  ]),
 ],
 "listen": [
  ("Please find the signed contract attached", ["signed", "attached"], "gửi kèm hợp đồng"),
  ("I am writing regarding your visa extension", ["writing", "extension"], "mở đầu email"),
  ("Please confirm receipt of this email", ["confirm", "receipt"], "xác nhận đã nhận"),
  ("I have copied our lawyer on this email", ["copied", "lawyer"], "cc luật sư"),
  ("Thank you for your email. We have reviewed the draft. Our comments are in the attachment.", ["email", "reviewed", "attachment"], "trả lời email khách"),
  ("I am following up on my email from Monday. We still need your signed form. Could you send it by Thursday?", ["following", "signed", "Thursday"], "email nhắc lại"),
 ],
})

# ───────────────────────── B. Tuân thủ & chính sách nội bộ ─────────────────────────
PHASES.append({
 "title": "Tuân thủ & chính sách nội bộ",
 "vocab": [
  ("compliance", "/kəmˈplaɪəns/", "n", "sự tuân thủ (pháp luật, quy định)", "The <b>compliance</b> team checks new suppliers.", "Nhóm tuân thủ kiểm tra các nhà cung cấp mới.", "コンプライアンス", "konpuraiansu"),
  ("policy", "/ˈpɒləsi/", "n", "chính sách, quy định (nội bộ)", "Our travel <b>policy</b> was updated last month.", "Chính sách công tác của mình được cập nhật tháng trước."),
  ("code of conduct", "/ˌkəʊd əv ˈkɒndʌkt/", "n", "bộ quy tắc ứng xử", "Every new employee must read the <b>code of conduct</b>.", "Mọi nhân viên mới phải đọc bộ quy tắc ứng xử.", "行動規範", "kōdō kihan"),
  ("gift", "/ɡɪft/", "n", "quà tặng", "Please report any <b>gift</b> above the limit.", "Vui lòng báo cáo mọi món quà vượt mức quy định.", "贈答品", "zōtōhin"),
  ("conflict of interest", "/ˌkɒnflɪkt əv ˈɪntrəst/", "n", "xung đột lợi ích", "My cousin owns this supplier, so it's a <b>conflict of interest</b>.", "Anh họ tôi làm chủ nhà cung cấp này nên đây là xung đột lợi ích.", "利益相反", "rieki sōhan"),
  ("bribery", "/ˈbraɪbəri/", "n", "hối lộ", "Our company has zero tolerance for <b>bribery</b>.", "Công ty chúng ta tuyệt đối không dung thứ hành vi hối lộ.", "贈賄", "zōwai"),
  ("whistleblowing", "/ˈwɪslbləʊɪŋ/", "n", "tố giác (sai phạm) nội bộ", "You can use the <b>whistleblowing</b> hotline without giving your name.", "Anh có thể dùng đường dây tố giác nội bộ mà không cần nêu tên.", "内部通報", "naibu tsūhō"),
  ("audit", "/ˈɔːdɪt/", "n", "cuộc kiểm toán, đợt kiểm tra", "The internal <b>audit</b> starts next week.", "Đợt kiểm toán nội bộ bắt đầu tuần sau.", "監査", "kansa"),
  ("breach", "/briːtʃ/", "n", "sự vi phạm", "Sharing passwords is a <b>breach</b> of our IT policy.", "Chia sẻ mật khẩu là vi phạm chính sách CNTT của mình.", "違反", "ihan"),
  ("red flag", "/ˌred ˈflæɡ/", "n", "dấu hiệu đáng ngờ, cảnh báo", "A supplier asking for cash payment is a <b>red flag</b>.", "Nhà cung cấp đòi trả tiền mặt là một dấu hiệu đáng ngờ."),
 ],
 "phrases": [
  ("Please read and sign the code of conduct.", "Vui lòng đọc và ký bộ quy tắc ứng xử."),
  ("Does this gift follow our policy?", "Món quà này có đúng chính sách không?"),
  ("I need to declare a conflict of interest.", "Tôi cần khai báo một xung đột lợi ích."),
  ("We never pay money to speed up a procedure.", "Chúng ta không bao giờ chi tiền để làm thủ tục nhanh hơn."),
  ("Please check this supplier before we sign.", "Vui lòng kiểm tra nhà cung cấp này trước khi ký."),
  ("The compliance training is required for all staff.", "Đào tạo tuân thủ là bắt buộc với mọi nhân viên."),
  ("If you see something wrong, please report it.", "Nếu thấy điều gì sai, vui lòng báo cáo."),
  ("All reports are kept confidential.", "Mọi báo cáo đều được giữ bí mật."),
  ("Let me check the policy and get back to you.", "Để tôi xem chính sách rồi trả lời anh."),
  ("We'll update the policy when the new regulation takes effect.", "Chúng ta sẽ cập nhật chính sách khi quy định mới có hiệu lực."),
 ],
 "dialogues": [
  ("An officer said he can make our licence faster for some 'coffee money'. What should I do?", [
    ("Please don't pay anything. Say our policy doesn't allow it, and report it to the compliance team today.", True, "Từ chối + dựa vào chính sách + báo cáo."),
    ("Pay a little, it's normal here.", False, "Vi phạm nghiêm trọng chính sách chống hối lộ."),
    ("You decide yourself.", False, "Bỏ mặc đồng nghiệp trước rủi ro tuân thủ."),
  ]),
  ("My brother's company wants to be our supplier. Is that OK?", [
    ("It may be possible, but you must declare the conflict of interest and stay out of the decision.", True, "Không cấm tuyệt đối nhưng nêu điều kiện: khai báo + không tham gia quyết định."),
    ("Yes, family is best supplier.", False, "Bỏ qua xung đột lợi ích."),
    ("No, never, it's crime.", False, "Khẳng định quá mức, thiếu mạo từ ('a crime')."),
  ]),
  ("Do I have to do the compliance training? I'm very busy.", [
    ("Yes, it's required for everyone. It takes about 30 minutes online, and you can do it this week.", True, "Khẳng định bắt buộc + giảm lo ngại bằng thông tin cụ thể."),
    ("Busy people no need.", False, "Sai — đào tạo bắt buộc áp dụng cho mọi người."),
    ("If you want, you do.", False, "Coi nhẹ quy định, thiếu 'can'."),
  ]),
  ("The supplier wants us to pay into a personal account. Is that a problem?", [
    ("Yes, it's a red flag. We should only pay into the company bank account in the contract.", True, "Nhận ra dấu hiệu đáng ngờ + nguyên tắc thanh toán."),
    ("No problem, money is money.", False, "Bỏ qua rủi ro gian lận."),
    ("Maybe personal account is cheaper.", False, "Lý do không liên quan và nguy hiểm."),
  ]),
  ("Can I report a problem without giving my name?", [
    ("Yes. You can use the whistleblowing hotline or email, and your report will be kept confidential.", True, "Trả lời + kênh cụ thể + cam kết bảo mật."),
    ("No, you must tell name.", False, "Sai với chính sách tố giác ẩn danh phổ biến; thiếu 'your'."),
    ("Don't report, it's dangerous.", False, "Khuyên sai, làm nản lòng người báo cáo."),
  ]),
 ],
 "listen": [
  ("Please read the code of conduct this week", ["code", "conduct"], "đọc quy tắc ứng xử"),
  ("We never pay money to speed up a procedure", ["never", "procedure"], "chống hối lộ"),
  ("You must declare any conflict of interest", ["declare", "interest"], "khai báo xung đột lợi ích"),
  ("A request for cash payment is a red flag", ["cash", "flag"], "dấu hiệu đáng ngờ"),
  ("The compliance training is now online. It takes about thirty minutes. Please finish it before the end of the month.", ["training", "thirty", "month"], "nhắc đào tạo tuân thủ"),
  ("A supplier offered me an expensive gift. I did not accept it. I have reported it to the compliance team.", ["expensive", "accept", "reported"], "báo cáo quà tặng"),
 ],
})

# ───────────────────────── C. Dữ liệu cá nhân ─────────────────────────
PHASES.append({
 "title": "Dữ liệu cá nhân",
 "vocab": [
  ("personal data", "/ˌpɜːsənl ˈdeɪtə/", "n", "dữ liệu cá nhân", "Passport numbers are <b>personal data</b>.", "Số hộ chiếu là dữ liệu cá nhân.", "個人情報", "kojin jōhō"),
  ("consent", "/kənˈsent/", "n", "sự đồng ý", "We need the employee's <b>consent</b> before we share the file.", "Cần có sự đồng ý của nhân viên trước khi chia sẻ hồ sơ.", "同意", "dōi"),
  ("data subject", "/ˈdeɪtə ˌsʌbdʒɪkt/", "n", "chủ thể dữ liệu (người có dữ liệu)", "The <b>data subject</b> can ask to see their data.", "Chủ thể dữ liệu có thể yêu cầu xem dữ liệu của mình."),
  ("purpose", "/ˈpɜːpəs/", "n", "mục đích", "Only use the data for the <b>purpose</b> you told the customer.", "Chỉ dùng dữ liệu đúng mục đích đã thông báo cho khách.", "目的", "mokuteki"),
  ("retention", "/rɪˈtenʃn/", "n", "việc lưu giữ (thời hạn lưu trữ)", "What is the <b>retention</b> period for old CVs?", "Thời hạn lưu giữ hồ sơ ứng viên cũ là bao lâu?", "保存", "hozon"),
  ("delete", "/dɪˈliːt/", "v", "xoá", "Please <b>delete</b> the old files from your laptop.", "Vui lòng xoá các file cũ khỏi máy tính.", "削除する", "sakujo suru"),
  ("privacy notice", "/ˈprɪvəsi ˌnəʊtɪs/", "n", "thông báo về quyền riêng tư, xử lý dữ liệu", "Our <b>privacy notice</b> explains how we use your data.", "Thông báo quyền riêng tư của chúng tôi giải thích cách chúng tôi dùng dữ liệu của anh."),
  ("cross-border transfer", "/ˌkrɒs ˈbɔːdə ˌtrænsfɜː/", "n", "chuyển dữ liệu ra nước ngoài", "Sending staff data to head office abroad is a <b>cross-border transfer</b>.", "Gửi dữ liệu nhân viên về công ty mẹ ở nước ngoài là chuyển dữ liệu ra nước ngoài."),
  ("data breach", "/ˈdeɪtə ˌbriːtʃ/", "n", "sự cố lộ lọt dữ liệu", "We must report the <b>data breach</b> quickly.", "Chúng ta phải báo cáo sự cố lộ dữ liệu thật nhanh.", "情報漏えい", "jōhō rōei"),
  ("anonymize", "/əˈnɒnɪmaɪz/", "v", "ẩn danh hoá (bỏ thông tin nhận diện)", "Please <b>anonymize</b> the names before you share the survey.", "Vui lòng ẩn danh tên trước khi chia sẻ khảo sát.", "匿名化する", "tokumeika suru"),
 ],
 "phrases": [
  ("We need your consent to process your personal data.", "Chúng tôi cần sự đồng ý của anh để xử lý dữ liệu cá nhân."),
  ("Why do you need my passport number?", "Sao anh cần số hộ chiếu của tôi?"),
  ("We only use it for your visa application.", "Chúng tôi chỉ dùng nó cho hồ sơ visa của anh."),
  ("Please don't send ID photos in the group chat.", "Vui lòng không gửi ảnh giấy tờ tuỳ thân vào nhóm chat."),
  ("Only HR can see salary data.", "Chỉ phòng nhân sự được xem dữ liệu lương."),
  ("We'll delete the files when we no longer need them.", "Chúng tôi sẽ xoá file khi không còn cần nữa."),
  ("Can I see what data you have about me?", "Tôi có thể xem các anh đang giữ dữ liệu gì về tôi không?"),
  ("Let's check the rules for sending data to head office.", "Mình kiểm tra quy định về gửi dữ liệu cho công ty mẹ nhé."),
  ("We need to report this data breach today.", "Hôm nay mình phải báo cáo sự cố lộ dữ liệu này."),
  ("Please lock the cabinet with the employee files.", "Vui lòng khoá tủ chứa hồ sơ nhân viên."),
 ],
 "dialogues": [
  ("Why do you need a copy of my passport?", [
    ("We need it for your work permit and visa files. We'll keep it secure and only share it with the authority.", True, "Nêu mục đích + cam kết bảo mật + phạm vi chia sẻ."),
    ("Because everybody give us.", False, "Sai 's' ('gives') và không nêu mục đích."),
    ("No reason, just give.", False, "Thiếu tôn trọng quyền của chủ thể dữ liệu."),
  ]),
  ("Head office in Seoul wants all employee data. Can we just send it?", [
    ("Not straight away. This is a cross-border transfer, so we need to check the current rules and employee consent first.", True, "Nhận diện chuyển dữ liệu ra nước ngoài + kiểm tra quy định + sự đồng ý."),
    ("Yes, head office is same company.", False, "Công ty mẹ ở nước ngoài vẫn là pháp nhân khác — cần kiểm tra quy định."),
    ("Send it by personal email, it's faster.", False, "Gửi dữ liệu nhạy cảm qua email cá nhân rất rủi ro."),
  ]),
  ("A candidate asked us to delete her CV. What should we do?", [
    ("Let's delete it from our system and email her to confirm it's done.", True, "Thực hiện + xác nhận lại với ứng viên."),
    ("Keep it, maybe we need later.", False, "Bỏ qua yêu cầu của chủ thể dữ liệu, thiếu 'it'."),
    ("CV is our data, not hers.", False, "Sai — CV chứa dữ liệu cá nhân của ứng viên."),
  ]),
  ("I lost a USB stick with staff files on the bus.", [
    ("Thanks for telling me right away. Let's report it as a data breach now and list which files were on it.", True, "Ghi nhận + báo sự cố + xác định phạm vi."),
    ("Maybe somebody give it back.", False, "Chủ quan, sai ngữ pháp ('will give it back')."),
    ("Buy a new USB.", False, "Không xử lý rủi ro lộ dữ liệu."),
  ]),
  ("Can I post the team photo with everyone's names on our website?", [
    ("Please ask everyone first. If someone doesn't agree, we'll use the photo without names.", True, "Xin đồng ý + phương án thay thế."),
    ("Sure, photo is public.", False, "Thiếu mạo từ và bỏ qua sự đồng ý."),
    ("No photo ever.", False, "Cấm tuyệt đối không cần thiết."),
  ]),
 ],
 "listen": [
  ("We need your consent to use your data", ["consent", "data"], "xin sự đồng ý"),
  ("Only HR can see salary data", ["HR", "salary"], "phân quyền dữ liệu"),
  ("Please delete the old files from your laptop", ["delete", "laptop"], "xoá dữ liệu cũ"),
  ("Do not send passport photos in the group chat", ["passport", "group"], "nhắc bảo mật"),
  ("We use your passport number only for your visa. We will not share it with anyone else. You can ask to see your data at any time.", ["only", "share", "ask"], "giải thích mục đích"),
  ("A laptop with staff files was lost yesterday. We are treating this as a data breach. Please change your passwords today.", ["lost", "breach", "passwords"], "thông báo sự cố"),
 ],
})

# ───────────────────────── D. Lao động & nội quy ─────────────────────────
PHASES.append({
 "title": "Lao động & nội quy",
 "vocab": [
  ("labour contract", "/ˈleɪbə ˌkɒntrækt/", "n", "hợp đồng lao động", "Please sign two copies of the <b>labour contract</b>.", "Vui lòng ký hai bản hợp đồng lao động.", "労働契約書", "rōdō keiyakusho"),
  ("probation", "/prəˈbeɪʃn/", "n", "thời gian thử việc", "Her <b>probation</b> ends next month.", "Chị ấy hết thử việc vào tháng sau.", "試用期間", "shiyō kikan"),
  ("internal labour rules", "/ɪnˌtɜːnl ˈleɪbə ˌruːlz/", "n", "nội quy lao động", "The <b>internal labour rules</b> are on the notice board.", "Nội quy lao động được dán trên bảng tin.", "就業規則", "shūgyō kisoku"),
  ("social insurance", "/ˌsəʊʃl ɪnˈʃʊərəns/", "n", "bảo hiểm xã hội", "HR will register new staff for <b>social insurance</b>.", "Phòng nhân sự sẽ đăng ký bảo hiểm xã hội cho nhân viên mới.", "社会保険", "shakai hoken"),
  ("overtime", "/ˈəʊvətaɪm/", "n", "làm thêm giờ", "<b>Overtime</b> must be approved by your manager first.", "Làm thêm giờ phải được quản lý duyệt trước.", "残業", "zangyō"),
  ("annual leave", "/ˌænjuəl ˈliːv/", "n", "nghỉ phép năm", "How many days of <b>annual leave</b> do I have left?", "Tôi còn bao nhiêu ngày phép năm?", "年次有給休暇", "nenji yūkyū kyūka"),
  ("resignation", "/ˌrezɪɡˈneɪʃn/", "n", "sự xin nghỉ việc; đơn nghỉ việc", "He sent his <b>resignation</b> letter this morning.", "Sáng nay anh ấy đã gửi đơn xin nghỉ việc.", "退職", "taishoku"),
  ("notice period", "/ˈnəʊtɪs ˌpɪəriəd/", "n", "thời gian báo trước", "Your <b>notice period</b> depends on your contract type.", "Thời gian báo trước tuỳ vào loại hợp đồng của anh."),
  ("disciplinary action", "/ˌdɪsəˈplɪnəri ˌækʃn/", "n", "hình thức xử lý kỷ luật", "<b>Disciplinary action</b> must follow the internal labour rules.", "Việc xử lý kỷ luật phải theo đúng nội quy lao động.", "懲戒処分", "chōkai shobun"),
  ("payslip", "/ˈpeɪslɪp/", "n", "phiếu lương", "You can download your <b>payslip</b> from the HR system.", "Anh có thể tải phiếu lương từ hệ thống nhân sự.", "給与明細", "kyūyo meisai"),
 ],
 "phrases": [
  ("Your probation period starts on Monday.", "Thời gian thử việc của anh bắt đầu từ thứ Hai."),
  ("Please read the internal labour rules carefully.", "Vui lòng đọc kỹ nội quy lao động."),
  ("Overtime needs your manager's approval.", "Làm thêm giờ cần quản lý duyệt."),
  ("How many days of annual leave do I have?", "Tôi có bao nhiêu ngày phép năm?"),
  ("Please give written notice if you want to resign.", "Nếu muốn nghỉ việc, vui lòng báo trước bằng văn bản."),
  ("Your notice period is in your labour contract.", "Thời gian báo trước được ghi trong hợp đồng lao động."),
  ("We follow the labour law and our internal rules.", "Chúng tôi tuân thủ luật lao động và nội quy công ty."),
  ("Please check your payslip and tell me if anything is wrong.", "Vui lòng kiểm tra phiếu lương và báo tôi nếu có gì sai."),
  ("We need a meeting before any disciplinary action.", "Cần họp trước khi xử lý kỷ luật."),
  ("Let me check the rules for foreign employees.", "Để tôi kiểm tra quy định với nhân viên nước ngoài."),
 ],
 "dialogues": [
  ("Can we fire him today? He was late five times.", [
    ("We should follow the internal labour rules first: a written warning, a meeting and proper records. Let me check the steps with our lawyer.", True, "Nhắc quy trình kỷ luật + hỏi luật sư, không khẳng định vội."),
    ("Yes, fire now, easy.", False, "Sa thải vội dễ trái luật và gây tranh chấp."),
    ("He late, so bye bye.", False, "Thiếu động từ ('He was late') và thiếu chuyên nghiệp."),
  ]),
  ("How long is my probation?", [
    ("It's written in your offer letter and your labour contract. I'll check it now and email you the exact end date.", True, "Dẫn chứng tài liệu + gửi ngày chính xác."),
    ("Probation is two months for everybody.", False, "Khẳng định chung — thời gian thử việc tuỳ vị trí và thoả thuận."),
    ("Long time, don't worry.", False, "Mơ hồ, không có thông tin."),
  ]),
  ("I worked on Saturday. Will I get overtime pay?", [
    ("If your manager approved the overtime, yes. Please send me the approval, and I'll add it to this month's payroll.", True, "Điều kiện + bước cần làm + thời điểm xử lý."),
    ("Saturday is free work.", False, "Sai và gây hiểu lầm."),
    ("You not ask before, so no.", False, "Thiếu trợ động từ ('You didn't ask') và từ chối cứng nhắc."),
  ]),
  ("I want to resign. What should I do?", [
    ("Please send a written resignation to your manager and HR. We'll confirm your last working day based on your notice period.", True, "Hướng dẫn thủ tục + ngày làm việc cuối theo thời gian báo trước."),
    ("You go, no need anything.", False, "Sai — cần báo trước bằng văn bản."),
    ("Why you want to leave? Stay!", False, "Sai cấu trúc câu hỏi ('Why do you want…?') và không trả lời về thủ tục."),
  ]),
  ("My payslip is missing my travel allowance.", [
    ("Sorry about that. I'll check with payroll today, and if it's missing, we'll pay it this week.", True, "Xin lỗi + kiểm tra + phương án khắc phục."),
    ("Payslip is always correct.", False, "Phủ nhận khi chưa kiểm tra."),
    ("Allowance is not my job.", False, "Đùn đẩy trách nhiệm."),
  ]),
 ],
 "listen": [
  ("Your probation ends next month", ["probation", "month"], "hết thử việc"),
  ("Overtime needs your manager's approval", ["Overtime", "approval"], "duyệt làm thêm giờ"),
  ("Please read the internal labour rules", ["internal", "rules"], "đọc nội quy"),
  ("You can download your payslip from the system", ["download", "payslip"], "phiếu lương"),
  ("Thank you for your resignation letter. Your notice period is in your contract. HR will confirm your last working day this week.", ["resignation", "notice", "last"], "xác nhận nghỉ việc"),
  ("Before any disciplinary action, we will have a meeting. The employee can explain what happened. We will keep written records.", ["disciplinary", "explain", "records"], "quy trình kỷ luật"),
 ],
})

# ───────────────────────── E. Sở hữu trí tuệ cơ bản ─────────────────────────
PHASES.append({
 "title": "Sở hữu trí tuệ cơ bản",
 "vocab": [
  ("trademark", "/ˈtreɪdmɑːk/", "n", "nhãn hiệu", "We should register our <b>trademark</b> in Vietnam early.", "Mình nên đăng ký nhãn hiệu ở Việt Nam sớm.", "商標", "shōhyō"),
  ("patent", "/ˈpætnt/", "n", "bằng sáng chế", "They have a <b>patent</b> for this machine.", "Họ có bằng sáng chế cho chiếc máy này.", "特許", "tokkyo"),
  ("copyright", "/ˈkɒpiraɪt/", "n", "quyền tác giả, bản quyền", "Who owns the <b>copyright</b> in the training videos?", "Ai giữ quyền tác giả đối với các video đào tạo?", "著作権", "chosakuken"),
  ("logo", "/ˈləʊɡəʊ/", "n", "logo, biểu trưng", "Our <b>logo</b> is part of the trademark application.", "Logo của mình nằm trong đơn đăng ký nhãn hiệu.", "ロゴ", "rogo"),
  ("register", "/ˈredʒɪstə/", "v", "đăng ký (bảo hộ)", "It's better to <b>register</b> the brand before you launch.", "Nên đăng ký thương hiệu trước khi ra mắt.", "登録する", "tōroku suru"),
  ("infringe", "/ɪnˈfrɪndʒ/", "v", "xâm phạm (quyền)", "This shop's logo may <b>infringe</b> our trademark.", "Logo của cửa hàng này có thể xâm phạm nhãn hiệu của mình.", "侵害する", "shingai suru"),
  ("licence", "/ˈlaɪsns/", "n", "giấy phép sử dụng (li-xăng)", "The partner needs a <b>licence</b> to use our logo.", "Đối tác cần được cấp phép để dùng logo của mình.", "ライセンス", "raisensu"),
  ("owner", "/ˈəʊnə/", "n", "chủ sở hữu", "The company is the <b>owner</b> of the software.", "Công ty là chủ sở hữu phần mềm.", "所有者", "shoyūsha"),
  ("counterfeit", "/ˈkaʊntəfɪt/", "adj", "giả, giả mạo", "We found <b>counterfeit</b> products online.", "Chúng tôi phát hiện hàng giả trên mạng."),
  ("trade secret", "/ˌtreɪd ˈsiːkrət/", "n", "bí mật kinh doanh", "The recipe is a <b>trade secret</b>.", "Công thức này là bí mật kinh doanh.", "営業秘密", "eigyō himitsu"),
 ],
 "phrases": [
  ("Have you registered your trademark in Vietnam?", "Anh đã đăng ký nhãn hiệu ở Việt Nam chưa?"),
  ("A trademark in another country may not protect you here.", "Nhãn hiệu ở nước khác có thể không bảo hộ anh ở đây."),
  ("Let's do a search before we file the application.", "Mình tra cứu trước khi nộp đơn nhé."),
  ("Who owns the copyright in this design?", "Ai giữ quyền tác giả của thiết kế này?"),
  ("We need a licence agreement to use their logo.", "Mình cần hợp đồng li-xăng để dùng logo của họ."),
  ("This product looks like a copy of ours.", "Sản phẩm này trông như bản sao của mình."),
  ("Please keep screenshots and the website link.", "Vui lòng giữ ảnh chụp màn hình và đường link trang web."),
  ("Employees must not take trade secrets when they leave.", "Nhân viên không được mang bí mật kinh doanh đi khi nghỉ việc."),
  ("Registration can take a long time, so let's file early.", "Đăng ký có thể mất nhiều thời gian nên mình nộp sớm nhé."),
  ("I'll ask our IP lawyer for advice.", "Tôi sẽ hỏi ý kiến luật sư sở hữu trí tuệ."),
 ],
 "dialogues": [
  ("We already have a trademark in Japan. Are we protected in Vietnam?", [
    ("Not necessarily. Trademark protection usually works country by country, so let's check and register it here if needed.", True, "Giải thích nguyên tắc theo lãnh thổ + hành động."),
    ("Yes, Japan trademark is world trademark.", False, "Sai — nhãn hiệu thường chỉ được bảo hộ theo từng quốc gia."),
    ("Trademark no need in Vietnam.", False, "Sai và thiếu động từ."),
  ]),
  ("A local shop is using a logo very similar to ours.", [
    ("Please send me photos and the shop's address. I'll check our registration and discuss the next steps with our IP lawyer.", True, "Thu thập bằng chứng + kiểm tra + hỏi chuyên gia."),
    ("Go to the shop and shout at them.", False, "Xử lý cảm tính, không đúng quy trình pháp lý."),
    ("Similar is OK, not same.", False, "Chủ quan — tương tự gây nhầm lẫn vẫn có thể là xâm phạm."),
  ]),
  ("A designer made our new logo. Who owns it?", [
    ("It depends on the contract. Let me check if it says the copyright is transferred to us.", True, "Dẫn về hợp đồng + kiểm tra điều khoản chuyển giao."),
    ("We paid, so we own, of course.", False, "Không phải cứ trả tiền là đã được chuyển giao quyền."),
    ("Designer own, sorry.", False, "Kết luận vội, thiếu 's' ('owns it')."),
  ]),
  ("Can our partner use our logo on their website?", [
    ("Yes, but we should sign a short licence agreement first, with rules on how they can use it.", True, "Đồng ý có điều kiện + văn bản."),
    ("Sure, free advertising.", False, "Bỏ qua việc kiểm soát cách dùng nhãn hiệu."),
    ("Logo is secret, no.", False, "Sai khái niệm — logo không phải bí mật."),
  ]),
  ("A former employee took our client list to a competitor.", [
    ("That's serious. Let's collect the evidence, check his NDA and labour contract, and talk to our lawyer today.", True, "Đánh giá mức độ + thu thập bằng chứng + kiểm tra hợp đồng + luật sư."),
    ("Forget it, clients choose freely.", False, "Bỏ qua vi phạm bí mật kinh doanh."),
    ("Call him and threaten him.", False, "Đe doạ là sai và có thể gây rủi ro pháp lý."),
  ]),
 ],
 "listen": [
  ("We should register our trademark early", ["register", "trademark"], "đăng ký nhãn hiệu"),
  ("This product may infringe our patent", ["infringe", "patent"], "xâm phạm sáng chế"),
  ("Who owns the copyright in this video", ["owns", "copyright"], "quyền tác giả"),
  ("Please keep the screenshots and the links", ["screenshots", "links"], "giữ bằng chứng"),
  ("We found counterfeit products on a shopping website. The logo looks like ours. Please send the links to the legal team.", ["counterfeit", "logo", "links"], "phát hiện hàng giả"),
  ("Our partner wants to use our logo. We will sign a licence agreement first. It will explain how they can use it.", ["partner", "licence", "explain"], "cấp phép dùng logo"),
 ],
})

# ───────────────────────── F. Tranh chấp & hoà giải ─────────────────────────
PHASES.append({
 "title": "Tranh chấp & hoà giải",
 "vocab": [
  ("dispute", "/dɪˈspjuːt/", "n", "tranh chấp", "We have a <b>dispute</b> with a supplier about late delivery.", "Chúng tôi có tranh chấp với nhà cung cấp về việc giao hàng trễ.", "紛争", "funsō"),
  ("mediation", "/ˌmiːdiˈeɪʃn/", "n", "hoà giải (có bên thứ ba)", "Both sides agreed to try <b>mediation</b> first.", "Hai bên đồng ý thử hoà giải trước.", "調停", "chōtei"),
  ("arbitration", "/ˌɑːbɪˈtreɪʃn/", "n", "trọng tài (thương mại)", "The contract says disputes go to <b>arbitration</b>.", "Hợp đồng quy định tranh chấp sẽ giải quyết bằng trọng tài.", "仲裁", "chūsai"),
  ("claim", "/kleɪm/", "n", "yêu cầu (bồi thường, thanh toán)", "The buyer made a <b>claim</b> for the damaged goods.", "Bên mua đưa ra yêu cầu bồi thường cho hàng bị hư.", "請求", "seikyū"),
  ("settlement", "/ˈsetlmənt/", "n", "thoả thuận giải quyết (dàn xếp)", "We reached a <b>settlement</b> after two meetings.", "Sau hai buổi họp, chúng tôi đạt được thoả thuận giải quyết.", "和解", "wakai"),
  ("evidence", "/ˈevɪdəns/", "n", "bằng chứng", "Please keep all emails as <b>evidence</b>.", "Vui lòng giữ lại mọi email làm bằng chứng.", "証拠", "shōko"),
  ("court", "/kɔːt/", "n", "toà án", "We want to avoid going to <b>court</b>.", "Chúng tôi muốn tránh phải ra toà.", "裁判所", "saibansho"),
  ("demand letter", "/dɪˈmɑːnd ˌletə/", "n", "thư yêu cầu (thanh toán, khắc phục)", "Our lawyer sent a <b>demand letter</b> to the customer.", "Luật sư của chúng tôi đã gửi thư yêu cầu cho khách hàng."),
  ("complaint", "/kəmˈpleɪnt/", "n", "khiếu nại, lời phàn nàn", "We received a written <b>complaint</b> from a customer.", "Chúng tôi nhận được khiếu nại bằng văn bản từ một khách hàng.", "苦情", "kujō"),
  ("amicably", "/ˈæmɪkəbli/", "adv", "một cách thiện chí, hoà nhã", "Let's try to solve this <b>amicably</b>.", "Mình thử giải quyết việc này một cách thiện chí nhé."),
 ],
 "phrases": [
  ("We'd like to solve this amicably.", "Chúng tôi muốn giải quyết việc này một cách thiện chí."),
  ("Could you explain your claim in writing?", "Anh trình bày yêu cầu bằng văn bản được không?"),
  ("Please keep all emails and messages as evidence.", "Vui lòng giữ lại mọi email và tin nhắn làm bằng chứng."),
  ("What does the contract say about disputes?", "Hợp đồng nói gì về giải quyết tranh chấp?"),
  ("Let's try mediation before arbitration.", "Mình thử hoà giải trước khi ra trọng tài."),
  ("We don't agree with the amount, but we're open to discussion.", "Chúng tôi không đồng ý với số tiền nhưng sẵn sàng trao đổi."),
  ("Please don't admit anything before you talk to our lawyer.", "Đừng thừa nhận gì trước khi nói chuyện với luật sư của mình."),
  ("We've received a demand letter from their lawyer.", "Chúng tôi đã nhận thư yêu cầu từ luật sư bên họ."),
  ("Can we agree on a payment plan?", "Mình thống nhất kế hoạch trả dần được không?"),
  ("Let's put the settlement in writing.", "Mình lập thoả thuận giải quyết bằng văn bản nhé."),
 ],
 "dialogues": [
  ("The customer refuses to pay. Should we sue them?", [
    ("Let's try a demand letter and a meeting first. Court takes time and money, so it should be our last option.", True, "Đề xuất từng bước + lý do kinh tế."),
    ("Yes, sue now, teach them.", False, "Cảm tính, bỏ qua các bước thương lượng, hoà giải."),
    ("Forget the money.", False, "Bỏ quyền lợi công ty quá dễ dàng."),
  ]),
  ("Their lawyer called me. What should I say?", [
    ("Please be polite, but don't admit anything. Say our lawyer will contact them, and send me their details.", True, "Lịch sự + không thừa nhận + chuyển cho luật sư."),
    ("Tell him everything, be honest.", False, "Nói hết khi chưa có tư vấn có thể gây bất lợi."),
    ("Don't answer phone ever.", False, "Né tránh hoàn toàn, thiếu 'the'."),
  ]),
  ("What does our contract say about disputes?", [
    ("Clause 15 says we try to negotiate for 30 days first, and then we go to arbitration in Vietnam.", True, "Chỉ điều khoản + trình tự cụ thể."),
    ("I think court, maybe.", False, "Không kiểm tra hợp đồng, mơ hồ."),
    ("Contract say nothing.", False, "Sai 's' ('says') và nghe như chưa đọc."),
  ]),
  ("They offered to pay 70 percent. Should we accept?", [
    ("It could be a good deal if they pay quickly. Let me compare it with the cost of arbitration and ask the director.", True, "Cân nhắc lợi ích + so sánh chi phí + xin ý kiến người quyết định."),
    ("No, 100 percent or nothing.", False, "Cứng nhắc, đóng đường thương lượng."),
    ("OK, accept, I'm tired.", False, "Quyết định theo cảm xúc, vượt thẩm quyền."),
  ]),
  ("A customer sent an angry complaint about our service.", [
    ("Let's reply today, thank them for the feedback, and offer a call to understand the problem.", True, "Phản hồi nhanh + thái độ cầu thị + đề xuất trao đổi."),
    ("Ignore it, angry customers always complain.", False, "Bỏ qua khiếu nại dễ biến thành tranh chấp."),
    ("Reply: you are wrong.", False, "Đối đầu, làm căng thẳng thêm."),
  ]),
 ],
 "listen": [
  ("We would like to solve this amicably", ["solve", "amicably"], "giải quyết thiện chí"),
  ("Please keep all emails as evidence", ["emails", "evidence"], "giữ bằng chứng"),
  ("Both sides agreed to try mediation", ["sides", "mediation"], "đồng ý hoà giải"),
  ("We received a demand letter today", ["demand", "today"], "nhận thư yêu cầu"),
  ("The contract says we must negotiate first. If that fails, the dispute goes to arbitration. We want to avoid court.", ["negotiate", "arbitration", "court"], "điều khoản tranh chấp"),
  ("We reached a settlement this morning. They will pay in three parts. Our lawyer will prepare the written agreement.", ["settlement", "three", "agreement"], "đạt thoả thuận"),
 ],
})

# ───────────────────────── G. Thuế & hoá đơn (thủ tục) ─────────────────────────
PHASES.append({
 "title": "Thuế & hoá đơn (thủ tục)",
 "vocab": [
  ("tax code", "/ˈtæks ˌkəʊd/", "n", "mã số thuế", "Please write the company's <b>tax code</b> on the invoice.", "Vui lòng ghi mã số thuế công ty trên hoá đơn."),
  ("invoice", "/ˈɪnvɔɪs/", "n", "hoá đơn", "We'll issue the <b>invoice</b> after the service is completed.", "Chúng tôi sẽ xuất hoá đơn sau khi hoàn thành dịch vụ.", "請求書", "seikyūsho"),
  ("e-invoice", "/ˈiː ˌɪnvɔɪs/", "n", "hoá đơn điện tử", "You'll receive the <b>e-invoice</b> by email.", "Anh sẽ nhận hoá đơn điện tử qua email."),
  ("VAT", "/ˌviː eɪ ˈtiː/", "n", "thuế giá trị gia tăng (GTGT)", "Does this price include <b>VAT</b>?", "Giá này đã gồm thuế GTGT chưa?"),
  ("tax return", "/ˈtæks rɪˌtɜːn/", "n", "tờ khai thuế", "The accountant will file the <b>tax return</b> online.", "Kế toán sẽ nộp tờ khai thuế trực tuyến."),
  ("personal income tax", "/ˌpɜːsənl ˈɪnkʌm ˌtæks/", "n", "thuế thu nhập cá nhân", "Foreign staff may also pay <b>personal income tax</b> in Vietnam.", "Nhân viên nước ngoài cũng có thể phải nộp thuế thu nhập cá nhân ở Việt Nam.", "個人所得税", "kojin shotokuzei"),
  ("tax finalization", "/ˈtæks ˌfaɪnəlaɪˈzeɪʃn/", "n", "quyết toán thuế", "Before you leave Vietnam, please finish your <b>tax finalization</b>.", "Trước khi rời Việt Nam, anh vui lòng làm xong quyết toán thuế."),
  ("tax office", "/ˈtæks ˌɒfɪs/", "n", "cơ quan thuế", "The <b>tax office</b> asked for more documents.", "Cơ quan thuế yêu cầu thêm giấy tờ.", "税務署", "zeimusho"),
  ("withholding", "/wɪðˈhəʊldɪŋ/", "n", "việc khấu trừ (thuế) tại nguồn", "The company handles tax <b>withholding</b> from your salary.", "Công ty khấu trừ thuế từ lương của anh.", "源泉徴収", "gensen chōshū"),
  ("refund", "/ˈriːfʌnd/", "n", "khoản hoàn (thuế)", "You may get a tax <b>refund</b> if you paid too much.", "Anh có thể được hoàn thuế nếu đã nộp thừa.", "還付", "kanpu"),
 ],
 "phrases": [
  ("Could you send me your company's tax code?", "Anh gửi giúp mã số thuế công ty được không?"),
  ("Is this price before or after VAT?", "Giá này là trước hay sau thuế GTGT?"),
  ("The name on the invoice must match the contract.", "Tên trên hoá đơn phải khớp với hợp đồng."),
  ("We'll send the e-invoice to your email.", "Chúng tôi sẽ gửi hoá đơn điện tử vào email của anh."),
  ("The invoice has a mistake. Can you issue a corrected one?", "Hoá đơn bị sai. Anh xuất hoá đơn điều chỉnh được không?"),
  ("Your personal income tax is withheld from your salary.", "Thuế thu nhập cá nhân được khấu trừ từ lương của anh."),
  ("Please finish your tax finalization before you leave.", "Vui lòng quyết toán thuế trước khi rời đi."),
  ("Our accountant will handle the tax return.", "Kế toán của chúng tôi sẽ lo tờ khai thuế."),
  ("Tax rules can change, so let's check the latest version.", "Quy định thuế có thể thay đổi, nên mình kiểm tra bản mới nhất."),
  ("Please keep all invoices for the audit.", "Vui lòng giữ lại mọi hoá đơn cho đợt kiểm toán."),
 ],
 "dialogues": [
  ("The company name on my invoice is wrong.", [
    ("Sorry about that. Please send me the correct name and tax code, and we'll issue a corrected e-invoice today.", True, "Xin lỗi + thông tin cần + hành động + thời gian."),
    ("Small wrong, you can use.", False, "Hoá đơn sai thông tin có thể không được chấp nhận."),
    ("Invoice cannot change.", False, "Sai — hoá đơn sai có thể được điều chỉnh hoặc thay thế theo quy định."),
  ]),
  ("Do I need to pay tax in Vietnam? I'm only here for eight months.", [
    ("It depends on your tax residency and where you're paid. I'll ask our tax adviser to confirm your case.", True, "Nêu yếu tố quyết định + chuyển chuyên gia xác nhận, không khẳng định vội."),
    ("No, foreigners never pay.", False, "Sai hoàn toàn."),
    ("Yes, you pay double.", False, "Khẳng định bừa, gây hoảng."),
  ]),
  ("Does this quote include VAT?", [
    ("No, it's before VAT. The VAT will be added on the invoice.", True, "Rõ ràng: chưa gồm VAT + khi nào được cộng."),
    ("Maybe include, I think.", False, "Mơ hồ về giá — rất dễ tranh cãi."),
    ("VAT is government, not us.", False, "Không trả lời đúng câu hỏi."),
  ]),
  ("I'm leaving Vietnam next month. Is there anything I need to do about tax?", [
    ("Yes, you'll probably need to do your tax finalization. Let's start now, because it can take some time.", True, "Nhắc thủ tục + bắt đầu sớm."),
    ("No, just go.", False, "Bỏ qua nghĩa vụ quyết toán thuế."),
    ("Tax is company problem.", False, "Thiếu mạo từ và sai — cá nhân cũng có nghĩa vụ."),
  ]),
  ("The tax office sent us a notice. Is it serious?", [
    ("Let me read it first. If they're asking for documents, we'll reply before the deadline and ask our accountant to help.", True, "Đọc trước + xử lý theo nội dung + đúng hạn + phối hợp kế toán."),
    ("Tax office always scary, pay them.", False, "Hoảng loạn, không đọc nội dung."),
    ("Throw away, not important.", False, "Bỏ qua thông báo của cơ quan thuế là rủi ro lớn."),
  ]),
 ],
 "listen": [
  ("Please write the tax code on the invoice", ["tax", "invoice"], "ghi mã số thuế"),
  ("Does this price include VAT", ["price", "VAT"], "hỏi thuế GTGT"),
  ("You will receive the e-invoice by email", ["receive", "email"], "hoá đơn điện tử"),
  ("Please finish your tax finalization before you leave", ["finalization", "leave"], "quyết toán thuế"),
  ("The invoice has the wrong company name. We will issue a replacement invoice. You will receive it today.", ["wrong", "replacement", "today"], "sửa hoá đơn"),
  ("Your income tax is withheld from your salary every month. At the end of the year, we check the total. You may get a refund.", ["withheld", "total", "refund"], "giải thích khấu trừ thuế"),
 ],
})

# ───────────────────────── H. Phiên dịch trong buổi làm việc ─────────────────────────
PHASES.append({
 "title": "Phiên dịch trong buổi làm việc",
 "vocab": [
  ("interpreter", "/ɪnˈtɜːprɪtə/", "n", "phiên dịch viên", "The <b>interpreter</b> will sit next to the director.", "Phiên dịch viên sẽ ngồi cạnh giám đốc.", "通訳者", "tsūyakusha"),
  ("interpret", "/ɪnˈtɜːprɪt/", "v", "phiên dịch (nói)", "Could you <b>interpret</b> at our meeting with the authority?", "Anh phiên dịch cho buổi làm việc với cơ quan được không?", "通訳する", "tsūyaku suru"),
  ("consecutive", "/kənˈsekjətɪv/", "adj", "(dịch) nối tiếp — nói xong một đoạn rồi dịch", "We'll use <b>consecutive</b> interpreting, so please pause after each point.", "Mình dùng dịch nối tiếp nên vui lòng dừng sau mỗi ý.", "逐次通訳", "chikuji tsūyaku"),
  ("glossary", "/ˈɡlɒsəri/", "n", "bảng thuật ngữ", "Please send me a <b>glossary</b> before the meeting.", "Vui lòng gửi tôi bảng thuật ngữ trước buổi họp.", "用語集", "yōgoshū"),
  ("terminology", "/ˌtɜːmɪˈnɒlədʒi/", "n", "thuật ngữ (chuyên ngành)", "Legal <b>terminology</b> is hard to translate.", "Thuật ngữ pháp lý rất khó dịch.", "専門用語", "senmon yōgo"),
  ("pause", "/pɔːz/", "v/n", "dừng (một chút); quãng dừng", "Please <b>pause</b> after two or three sentences.", "Vui lòng dừng lại sau hai, ba câu."),
  ("paraphrase", "/ˈpærəfreɪz/", "v", "diễn đạt lại (bằng lời khác)", "If a joke doesn't work in Vietnamese, I'll <b>paraphrase</b> it.", "Nếu câu đùa không hợp tiếng Việt, tôi sẽ diễn đạt lại."),
  ("accurate", "/ˈækjərət/", "adj", "chính xác", "Numbers and dates must be <b>accurate</b>.", "Con số và ngày tháng phải chính xác.", "正確な", "seikaku na"),
  ("literal", "/ˈlɪtərəl/", "adj", "(dịch) sát nghĩa đen, từng chữ", "A <b>literal</b> translation sounds strange here.", "Dịch sát từng chữ ở đây nghe rất lạ.", "直訳の", "chokuyaku no"),
  ("neutral", "/ˈnjuːtrəl/", "adj", "trung lập, khách quan", "An interpreter must stay <b>neutral</b>.", "Phiên dịch viên phải giữ trung lập.", "中立", "chūritsu"),
 ],
 "phrases": [
  ("I'll interpret between English and Vietnamese today.", "Hôm nay tôi sẽ phiên dịch Anh – Việt."),
  ("Please speak in short sections and pause.", "Vui lòng nói từng đoạn ngắn và dừng lại."),
  ("Could you repeat the number, please?", "Anh nhắc lại con số giúp tôi được không?"),
  ("Could you send me the documents before the meeting?", "Anh gửi tài liệu cho tôi trước buổi họp được không?"),
  ("Let me check this term with you first.", "Để tôi kiểm tra thuật ngữ này với anh trước."),
  ("The officer is asking about your job title.", "Cán bộ đang hỏi về chức danh của anh."),
  ("There's no exact word for this in Vietnamese.", "Tiếng Việt không có từ tương đương chính xác."),
  ("I'll translate exactly what you say.", "Tôi sẽ dịch đúng những gì anh nói."),
  ("As the interpreter, I can't give advice.", "Là phiên dịch, tôi không thể đưa ra lời khuyên."),
  ("Shall I read the document aloud in English?", "Tôi đọc to tài liệu bằng tiếng Anh nhé?"),
 ],
 "dialogues": [
  ("What do you think we should do? You know the local rules.", [
    ("As the interpreter, I need to stay neutral. I can help you ask the officer or your lawyer that question.", True, "Giữ vai trò trung lập + giúp hỏi đúng người."),
    ("I think you should pay more money.", False, "Phiên dịch đưa lời khuyên — vượt vai trò, lại có thể sai."),
    ("I don't know, I only translate.", False, "Đúng vai nhưng cộc lốc — nên đề nghị giúp hỏi đúng người."),
  ]),
  ("Sorry, I'll talk for a few minutes now.", [
    ("That's fine. Could you pause after every two or three sentences, so I can interpret accurately?", True, "Lịch sự đề nghị ngắt đoạn vì độ chính xác."),
    ("Too long, I cannot.", False, "Cộc, không đề xuất cách làm."),
    ("OK, I remember all.", False, "Hứa nhớ hết dễ dẫn đến dịch thiếu ý."),
  ]),
  ("What did the officer just say? He talked for a long time.", [
    ("He said your file is complete, but the health certificate must be translated. He also asked when you can bring it.", True, "Dịch đủ ý chính + câu hỏi của cán bộ."),
    ("He say OK.", False, "Tóm tắt quá ngắn, bỏ sót thông tin, thiếu 's' ('says')."),
    ("Not important, don't worry.", False, "Phiên dịch tự lược bỏ nội dung là sai nguyên tắc."),
  ]),
  ("How do you say 'charter capital' in Vietnamese?", [
    ("It's 'vốn điều lệ'. I'll add it to our glossary for the meeting.", True, "Thuật ngữ chuẩn + cập nhật bảng thuật ngữ."),
    ("Charter is ship rental, capital is city.", False, "Dịch từng chữ, sai nghĩa pháp lý."),
    ("Vietnamese same English.", False, "Sai và thiếu động từ."),
  ]),
  ("The director made a joke. Did they understand?", [
    ("I paraphrased it, because the literal version wasn't funny in Vietnamese. They laughed, so I think it worked.", True, "Giải thích cách xử lý câu đùa + kết quả."),
    ("I skip it, joke is not important.", False, "Sai thì ('I skipped it') và tự bỏ nội dung."),
    ("Joke cannot translate.", False, "Sai bị động ('can't be translated') và bỏ cuộc."),
  ]),
 ],
 "listen": [
  ("Please pause after two or three sentences", ["pause", "sentences"], "đề nghị ngắt đoạn"),
  ("Could you send me the glossary before the meeting", ["glossary", "meeting"], "xin bảng thuật ngữ"),
  ("An interpreter must stay neutral", ["interpreter", "neutral"], "nguyên tắc trung lập"),
  ("Numbers and dates must be accurate", ["dates", "accurate"], "độ chính xác"),
  ("Good morning. I will interpret between English and Vietnamese today. Please speak in short sections so I can translate everything.", ["interpret", "short", "everything"], "giới thiệu vai phiên dịch"),
  ("The officer is asking about your job title. He says it is different on your contract. Could you explain this difference?", ["officer", "contract", "difference"], "dịch câu hỏi của cán bộ"),
 ],
})

# ───────────────────────── Vai: tình huống + hội thoại mới ─────────────────────────
ROLES_X = {
 "inhouse": {
  "scenarios": [
   ("ih_dispute", "Tư vấn sếp về tranh chấp", "You are my foreign general director. A customer hasn't paid for four months. Ask me about our options — a demand letter, mediation or court — and which one I recommend."),
   ("ih_data", "Chuyển dữ liệu nhân viên về công ty mẹ", "You are the HR manager at head office abroad. You want all employee data from the Vietnamese company by Friday. I am the in-house legal officer. Ask why I need more time and what I need from you."),
  ],
  "dialogues": [
   ("Head office wants the payroll file today. Can I just email it?", [
     ("Please wait. Salary data is sensitive, and it's going abroad. Let's use a password-protected file and check the transfer rules first.", True, "Nhận diện dữ liệu nhạy cảm + chuyển ra nước ngoài + cách gửi an toàn."),
     ("Yes, head office is our boss.", False, "Công ty mẹ vẫn phải tuân thủ quy định về dữ liệu."),
     ("Email it, fast is good.", False, "Coi nhẹ bảo mật dữ liệu lương.")]),
   ("A customer owes us two billion dong. What do you recommend?", [
     ("First, a demand letter with a clear deadline. If they don't pay, we can suggest mediation before arbitration or court.", True, "Lộ trình leo thang từng bước, hợp lý."),
     ("Go to court tomorrow.", False, "Bỏ qua các bước rẻ và nhanh hơn."),
     ("Wait, maybe they pay next year.", False, "Thụ động, rủi ro mất nợ; thiếu 'will'.")]),
   ("Is our new product name safe to use?", [
     ("I've done a quick search and found no similar trademark. I'll ask our IP lawyer to confirm, and then we can file the application.", True, "Đã tra cứu sơ bộ + chuyên gia xác nhận + nộp đơn."),
     ("Yes, name is new, I think.", False, "Chưa tra cứu, thiếu mạo từ."),
     ("Names are free for everybody.", False, "Sai — tên trùng nhãn hiệu đã đăng ký có thể bị coi là xâm phạm.")]),
   ("An employee reported that his manager asks suppliers for money.", [
     ("Thank you. We'll keep his name confidential, start an internal review and not tell the manager yet.", True, "Bảo vệ người tố giác + rà soát nội bộ + giữ bí mật."),
     ("Let's ask the manager first.", False, "Báo cho người bị tố trước dễ làm mất bằng chứng và gây trả đũa."),
     ("Maybe the employee is angry, ignore.", False, "Bỏ qua tố giác là sai quy trình tuân thủ.")]),
  ]},
 "firm": {
  "scenarios": [
   ("lf_ip", "Tư vấn nhãn hiệu cho khách", "You are a foreign startup founder. You found a local shop using a logo like yours. I am the legal assistant. Ask what we can do, what evidence you need and how long it takes."),
   ("lf_delay", "Báo trễ góp ý cho luật sư đối tác", "You are a lawyer at a partner firm abroad. You haven't received our comments on a draft. I call to explain the delay. Ask for a new date and a short summary of the main points."),
  ],
  "dialogues": [
   ("Can you summarize the partner's email for me?", [
     ("Sure. They accept most of our changes, but they want a higher liability cap, and they need our reply by Friday.", True, "Tóm tắt ý chính + điểm cần xử lý + hạn."),
     ("Email is long, many things.", False, "Không tóm tắt được."),
     ("They say OK all.", False, "Tóm tắt sai, bỏ sót điểm còn vướng.")]),
   ("The client asked if they will win the case. What should I say?", [
     ("Please don't promise anything. Say the lawyer will explain the risks after reviewing all the evidence.", True, "Không hứa kết quả + để luật sư đánh giá."),
     ("Tell them 100 percent win.", False, "Hứa kết quả vụ việc là sai đạo đức nghề nghiệp."),
     ("Say we will lose, maybe.", False, "Gây hoang mang, không có căn cứ.")]),
   ("Did you send the demand letter?", [
     ("Yes, it went out by courier and email this morning. I've saved the delivery receipt in the file.", True, "Xác nhận + kênh gửi + lưu bằng chứng."),
     ("I send yesterday maybe.", False, "Sai thì, không chắc chắn."),
     ("Letter is ready, not send.", False, "Sai ngữ pháp ('hasn't been sent') và không nói khi nào gửi.")]),
   ("The client's trademark application was refused. How do we tell them?", [
     ("Let's call them first and explain the reason simply. Then we'll email the options and the deadline to respond.", True, "Gọi trước + giải thích + văn bản nêu lựa chọn và thời hạn."),
     ("Email: refused, sorry.", False, "Quá cộc, thiếu phương án."),
     ("Don't tell them yet, wait.", False, "Giấu thông tin có thể làm lỡ hạn phản hồi.")]),
  ]},
 "onestop": {
  "scenarios": [
   ("os_tax", "Người nước ngoài hỏi mã số thuế", "You are a foreign employee at a public service counter. You need a personal tax code and don't know the steps. I am the officer. Ask what documents you need and whether your company can do it for you."),
   ("os_long", "Khách nói dài qua phiên dịch", "You are a foreign investor who came with an interpreter. You speak for a long time without pausing. I am the officer. Let me ask you to speak in short parts, and answer my questions."),
  ],
  "dialogues": [
   ("Can my company apply for my tax code?", [
     ("Yes, in most cases your company can do it for you. Please ask your HR team. They'll need a copy of your passport.", True, "Trả lời + hướng dẫn liên hệ + giấy tờ cần."),
     ("No, you must come every time.", False, "Khẳng định sai, thiếu hướng dẫn."),
     ("Tax code is not here, go away.", False, "Thô lỗ, không chỉ đúng nơi.")]),
   ("Why was my file sent back?", [
     ("The letter says your job title is different in two documents. If you correct it, you can submit again.", True, "Đọc lý do cụ thể + cách khắc phục."),
     ("Because your file bad.", False, "Thiếu động từ, không giải thích lý do."),
     ("I don't know, ask the boss.", False, "Đùn đẩy, không đọc thông báo.")]),
   ("Can I get a copy of this form in English?", [
     ("We only have the Vietnamese form, but I can explain each part in English and show you an example.", True, "Nói rõ giới hạn + hỗ trợ thay thế."),
     ("English no have.", False, "Dịch từng chữ 'không có' — đúng là 'We don't have it in English'."),
     ("Use phone translate yourself.", False, "Đẩy việc cho khách, thiếu hỗ trợ.")]),
   ("My interpreter isn't here yet. Can we start?", [
     ("Of course. I'll speak slowly, and when your interpreter arrives, she can check anything that's unclear.", True, "Linh hoạt + nói chậm + tận dụng phiên dịch khi đến."),
     ("No interpreter, no work.", False, "Cứng nhắc."),
     ("You wait outside.", False, "Cộc lốc, thiếu lịch sự.")]),
  ]},
 "translator": {
  "scenarios": [
   ("tr_authority", "Dịch buổi làm việc với cơ quan", "You are a local officer meeting a foreign investor. I am the interpreter. Ask several questions about the company's business lines and capital, and speak quickly at first."),
   ("tr_glossary", "Chuẩn bị thuật ngữ trước buổi họp", "You are a foreign lawyer. I will interpret at your meeting tomorrow. I ask for documents and a glossary. Explain three terms simply: charter capital, legal representative and power of attorney."),
  ],
  "dialogues": [
   ("Please don't translate that last part. It was just for you.", [
     ("I understand, but in the meeting I need to interpret everything that's said. Could we talk about it during the break?", True, "Giữ nguyên tắc dịch đầy đủ + gợi ý trao đổi riêng lúc nghỉ."),
     ("OK, I skip, no problem.", False, "Tự lược bỏ nội dung làm mất tính trung lập."),
     ("No! I must translate all!", False, "Đúng ý nhưng giọng gay gắt.")]),
   ("What's the Vietnamese for 'power of attorney'?", [
     ("It's 'giấy uỷ quyền'. In this contract, it means the director allows the lawyer to sign for him.", True, "Thuật ngữ chuẩn + giải thích theo ngữ cảnh."),
     ("Power is 'sức mạnh', so 'sức mạnh luật sư'.", False, "Dịch từng chữ, sai nghĩa hoàn toàn."),
     ("I don't know, skip it.", False, "Bỏ qua thuật ngữ quan trọng.")]),
   ("You translated '15' as '50'. Please be careful.", [
     ("I'm sorry, you're right. It's fifteen. I'll repeat the sentence correctly now.", True, "Xin lỗi + sửa ngay trước mọi người."),
     ("Fifteen, fifty, sound same.", False, "Bao biện — lỗi số liệu rất nghiêm trọng."),
     ("You speak not clear.", False, "Đổ lỗi, sai trật tự ('You didn't speak clearly').")]),
   ("Can you also give us your opinion on the offer?", [
     ("I'm sorry, as the interpreter I can't give an opinion. I'm happy to interpret your questions to the other side.", True, "Từ chối lịch sự, giữ vai trò trung lập."),
     ("I think the offer is bad.", False, "Vượt vai trò phiên dịch."),
     ("Opinion is extra money.", False, "Không chuyên nghiệp và sai vai trò.")]),
  ]},
}

EXTRA = {
 "phases": PHASES,
 "rev": [
  ("Tôi viết thư về việc gia hạn visa.", "I'm writing regarding the visa extension."),
  ("Hợp đồng đã ký được đính kèm.", "The signed contract is attached."),
  ("Vui lòng xác nhận đã nhận email này.", "Please confirm receipt of this email."),
  ("Món quà này có đúng chính sách không?", "Does this gift follow our policy?"),
  ("Tôi cần khai báo xung đột lợi ích.", "I need to declare a conflict of interest."),
  ("Chúng tôi cần sự đồng ý của anh.", "We need your consent."),
  ("Vui lòng không gửi ảnh hộ chiếu vào nhóm chat.", "Please don't send passport photos in the group chat."),
  ("Thời gian thử việc của anh là hai tháng.", "Your probation period is two months."),
  ("Làm thêm giờ cần quản lý duyệt trước.", "Overtime needs your manager's approval first."),
  ("Mình nên đăng ký nhãn hiệu sớm.", "We should register our trademark early."),
  ("Vui lòng giữ lại email làm bằng chứng.", "Please keep the emails as evidence."),
  ("Chúng tôi muốn giải quyết việc này một cách thiện chí.", "We'd like to solve this amicably."),
  ("Giá này đã gồm thuế GTGT chưa?", "Does this price include VAT?"),
  ("Tên công ty trên hoá đơn bị sai.", "The company name on the invoice is wrong."),
  ("Vui lòng dừng lại sau mỗi ý.", "Please pause after each point."),
  ("Là phiên dịch, tôi không thể đưa ra lời khuyên.", "As the interpreter, I can't give advice."),
 ],
 "reading": [
  {"t": "Official letter summary", "text": "OFFICIAL LETTER – summary for Mr. Park\nFrom: Local labour authority\nSubject: Work permit file of Mr. Lee Joon\nThe authority needs:\n1. A certified translation of the degree\n2. A new health certificate (the current one is too old)\nPlease submit within 10 working days from the date of the letter (8 May).", "q": [
    {"q": "What is wrong with the health certificate?", "o": ["It is too old", "It is not signed", "It is in English"], "a": 0},
    {"q": "What must be translated?", "o": ["The passport", "The degree", "The labour contract"], "a": 1}]},
  {"t": "Gift policy", "text": "GIFT POLICY (summary)\n- Small gifts, like calendars or food at Tết, are OK.\n- Gifts above the limit in the policy must be reported to Compliance within 3 days.\n- Never accept cash or vouchers.\n- Never give gifts to public officials to speed up a procedure.\nQuestions? Call the Compliance team (ext. 214).", "q": [
    {"q": "What should you do with a gift above the limit?", "o": ["Keep it quietly", "Report it to Compliance within 3 days", "Give it to a public official"], "a": 1},
    {"q": "Which gift is never allowed?", "o": ["A calendar", "Food at Tết", "Cash"], "a": 2}]},
  {"t": "Data breach message", "text": "Chat – HR group, 17:05\nMai: I sent the payroll file to the wrong email address by mistake. It has the names and salaries of 40 staff.\nTuấn (Legal): Thanks for telling us quickly. Please don't send anything else. I've asked the receiver to delete it. We will report this as a data breach and meet at 9:00 tomorrow.", "q": [
    {"q": "What information was in the file?", "o": ["Passport numbers", "Names and salaries", "Client prices"], "a": 1},
    {"q": "What will happen at 9:00 tomorrow?", "o": ["A meeting", "The payroll will be paid", "Mai will resign"], "a": 0}]},
  {"t": "Settlement terms", "text": "SETTLEMENT – key terms (draft)\nParties: Sunrise Packaging Co. and Delta Foods Ltd.\nAmount: 700 million VND (70% of the claim)\nPayment: in 3 parts – 30 June, 31 July, 31 August\nBoth parties will keep the settlement confidential.\nIf a payment is late, the full claim becomes due again.", "q": [
    {"q": "How many payments will there be?", "o": ["One", "Three", "Seven"], "a": 1},
    {"q": "What happens if a payment is late?", "o": ["The full claim becomes due again", "The settlement becomes public", "Nothing happens"], "a": 0}]},
  {"t": "Interpreter brief", "text": "INTERPRETER BRIEF\nMeeting: investor and local authority – company registration\nDate: Tuesday, 9:30, Room 2\nLanguages: English ↔ Vietnamese (consecutive)\nPlease read before the meeting: draft charter, glossary (sent today).\nNote: Mr. Evans speaks quickly. Ask him to pause after each point.", "q": [
    {"q": "What type of interpreting is needed?", "o": ["Consecutive", "Written only", "Sign language"], "a": 0},
    {"q": "What should the interpreter ask Mr. Evans to do?", "o": ["Speak Vietnamese", "Pause after each point", "Send the charter"], "a": 1}]},
 ],
 "ai": [
  ("official_letter", "Giải thích công văn", "You are a foreign factory director. The company received an official letter in Vietnamese from a local authority. I am the legal officer. Ask me what it says, how serious it is and what we must do by when."),
  ("data_request", "Nhân viên hỏi về dữ liệu cá nhân", "You are a foreign employee. You want to know what personal data the company keeps about you and why. I am the HR and legal officer. Then ask me to delete some old data."),
  ("debt_call", "Gọi điện đòi nợ khách hàng", "You are a foreign customer who hasn't paid an invoice for three months. I am the legal officer calling you. Give reasons at first, then agree to a payment plan."),
  ("interpret_officer", "Phiên dịch với cán bộ", "You are a foreign investor at a meeting with a local officer. I am your interpreter. Ask me for advice at first, then ask me to interpret your questions about the licence and the timeline."),
 ],
 "events": [
  ("mediation", "Buổi hoà giải tranh chấp", "You are the other party's manager at a mediation meeting next week about unpaid invoices. Explain your side, ask for a discount and agree to a payment plan if the offer is fair."),
  ("compliance_training", "Buổi đào tạo tuân thủ", "You are a foreign employee at the compliance training I will lead next week. Ask me questions about gifts, conflicts of interest and how to report a problem."),
  ("trademark", "Họp về đăng ký nhãn hiệu", "You are a foreign brand manager launching a product in Vietnam soon. Ask me about registering the trademark, the timeline and what to do if someone copies the logo."),
 ],
 "quips": [
  "Pause, then interpret!",
  "Consent first!",
  "Declare it, don't hide it!",
  "Solve it amicably!",
  "Tax code on the invoice!",
  "Follow up, politely!",
 ],
 "roles": ROLES_X,
}
