# -*- coding: utf-8 -*-
# Gói "construction" — Xây dựng · Kỹ thuật: kỹ sư hiện trường, QA/QC, an toàn (HSE), điều phối dự án, kỹ thuật MEP.
# Người học làm việc với chủ đầu tư, tư vấn, tổng thầu / nhà thầu phụ nước ngoài (nhiều dự án vốn Nhật, Hàn ở Việt Nam).
# Tên người / dự án đều là tên tự đặt. Chặng lõi lấy từ office: 3 (Email công việc), 11 (Phỏng vấn & phát triển sự nghiệp).
# Schema: xem packs_src/README.md. Build: python3 packs_src/build.py construction

PHASES = []

# ───────────────────────── 0. An toàn công trường & đồ bảo hộ ─────────────────────────
PHASES.append({
 "title": "An toàn công trường & đồ bảo hộ",
 "vocab": [
  ("hard hat", "/ˌhɑːd ˈhæt/", "n", "mũ bảo hộ", "Wear your <b>hard hat</b> at all times on site.", "Luôn đội mũ bảo hộ khi ở công trường.", "ヘルメット", "herumetto"),
  ("safety boots", "/ˈseɪfti ˌbuːts/", "n", "giày bảo hộ", "Sandals are not allowed. Please wear <b>safety boots</b>.", "Không được đi dép. Vui lòng mang giày bảo hộ.", "安全靴", "anzengutsu"),
  ("toolbox talk", "/ˈtuːlbɒks ˌtɔːk/", "n", "buổi nhắc an toàn ngắn đầu ca (họp an toàn tại chỗ)", "Today's <b>toolbox talk</b> is about working in hot weather.", "Buổi nhắc an toàn hôm nay nói về làm việc khi trời nóng.", "ツールボックスミーティング", "tsūru bokkusu mītingu"),
  ("hazard", "/ˈhæzəd/", "n", "mối nguy", "Loose cables on the floor are a trip <b>hazard</b>.", "Dây điện vương trên sàn là mối nguy gây vấp ngã.", "危険源", "kikengen"),
  ("near miss", "/ˌnɪə ˈmɪs/", "n", "sự cố suýt gây tai nạn", "A brick fell next to a worker — please report this <b>near miss</b>.", "Một viên gạch rơi sát chỗ công nhân — hãy báo sự cố suýt tai nạn này.", "ヒヤリハット", "hiyari hatto"),
  ("barrier", "/ˈbæriə/", "n", "rào chắn", "Put a <b>barrier</b> around the open hole.", "Đặt rào chắn quanh cái hố đang để hở."),
  ("housekeeping", "/ˈhaʊskiːpɪŋ/", "n", "giữ công trường gọn gàng, sạch sẽ", "Good <b>housekeeping</b> prevents many accidents.", "Giữ công trường gọn gàng giúp tránh được nhiều tai nạn.", "整理整頓", "seiri seiton"),
  ("violation", "/ˌvaɪəˈleɪʃn/", "n", "sự vi phạm (quy định)", "Working at height without a harness is a serious safety <b>violation</b>.", "Làm việc trên cao không đeo dây an toàn là vi phạm an toàn nghiêm trọng.", "違反", "ihan"),
  ("permit to work", "/ˌpɜːmɪt tə ˈwɜːk/", "n", "giấy phép làm việc (cho công việc nguy hiểm như hàn, cắt)", "Welding in this area needs a <b>permit to work</b>.", "Hàn ở khu vực này phải có giấy phép làm việc."),
  ("assembly point", "/əˈsembli ˌpɔɪnt/", "n", "điểm tập trung (khi sơ tán)", "If the alarm sounds, go to the <b>assembly point</b> near the gate.", "Nếu chuông báo động kêu, hãy đến điểm tập trung gần cổng."),
 ],
 "phrases": [
  ("Please wear your hard hat and safety boots on site.", "Vui lòng đội mũ bảo hộ và mang giày bảo hộ trong công trường."),
  ("Today's toolbox talk is about working at height.", "Buổi nhắc an toàn hôm nay nói về làm việc trên cao."),
  ("Please sign the attendance sheet after the talk.", "Nghe xong nhớ ký vào danh sách tham dự nhé."),
  ("Keep the walkway clear of materials.", "Không để vật tư chắn lối đi."),
  ("This area is closed. Please use the other entrance.", "Khu vực này đang đóng. Vui lòng đi lối khác."),
  ("I'd like to report a near miss at Block B.", "Tôi muốn báo một sự cố suýt tai nạn ở khối B."),
  ("You need a permit before you start welding.", "Phải có giấy phép rồi mới được bắt đầu hàn."),
  ("If you see something unsafe, stop and tell your supervisor.", "Thấy gì không an toàn thì dừng lại và báo giám sát."),
  ("Where is the nearest fire extinguisher?", "Bình chữa cháy gần nhất ở đâu?"),
  ("Nobody gets hurt today — that's our goal.", "Hôm nay không ai bị thương — đó là mục tiêu của chúng ta."),
 ],
 "dialogues": [
  ("Why isn't that worker wearing a hard hat?", [
    ("Sorry, I'll stop him now and make sure he puts it on.", True, "Xin lỗi + xử lý ngay — đúng thái độ khi bị nhắc về an toàn."),
    ("He is here only five minutes, no problem.", False, "Sai trật tự, thiếu 'for' ('He's only here for five minutes') và coi nhẹ an toàn — vật rơi có thể trúng đầu bất cứ lúc nào."),
    ("Hard hat is hot, he don't like.", False, "Sai chia động từ ('doesn't like it') và bào chữa thay vì sửa sai."),
  ]),
  ("What's the topic of today's toolbox talk?", [
    ("Housekeeping. Yesterday a worker tripped on a cable, so we'll talk about keeping walkways clear.", True, "Chủ đề + lý do thực tế + nội dung chính."),
    ("Toolbox talk is about the tools.", False, "Hiểu sai: toolbox talk là buổi nhắc an toàn ngắn, không phải buổi nói về dụng cụ."),
    ("Same same every day.", False, "Nói kiểu 'same same' và không nêu chủ đề — buổi nhắc an toàn cần nội dung cụ thể."),
  ]),
  ("There's a big hole near the stairs with no cover.", [
    ("Thanks. I'll put a barrier around it now and ask the team to cover it today.", True, "Cảm ơn + rào chắn ngay + khắc phục triệt để."),
    ("Everybody can see it, it's OK.", False, "Sai về an toàn — hố để hở không che chắn rất dễ gây ngã."),
    ("Not my team make the hole.", False, "Sai ngữ pháp ('My team didn't make it') và đùn đẩy — thấy mối nguy thì phải xử lý hoặc báo ngay."),
  ]),
  ("Can my team start welding on the third floor now?", [
    ("Not yet. You need a hot work permit first, and there must be a fire extinguisher nearby.", True, "Trả lời rõ + điều kiện an toàn đúng quy trình."),
    ("Yes, go ahead, just be careful.", False, "Cho làm khi chưa có giấy phép và biện pháp phòng cháy — sai quy trình."),
    ("Welding need permit maybe.", False, "Thiếu 's' ('needs a permit') và 'maybe' — về an toàn phải trả lời chắc chắn."),
  ]),
  ("What should we do if the fire alarm goes off?", [
    ("Stop work, leave by the nearest exit and go to the assembly point near the main gate.", True, "Đủ 3 bước: dừng việc – thoát ra – đến điểm tập trung."),
    ("Run fast, anywhere.", False, "Cộc lốc và sai — phải đến điểm tập trung để điểm danh."),
    ("First finish the work, then go.", False, "Nguy hiểm — khi có báo động phải dừng việc ngay."),
  ]),
 ],
 "listen": [
  ("Please wear your hard hat at all times on site", ["hard", "hat"], "nhắc đồ bảo hộ"),
  ("Keep the walkway clear of materials", ["walkway", "clear"], "giữ lối đi thông thoáng"),
  ("You need a permit before you start welding", ["permit", "welding"], "giấy phép làm việc"),
  ("The assembly point is near the main gate", ["assembly", "gate"], "điểm tập trung"),
  ("Good morning, everyone. Yesterday a worker tripped on a cable near the stairs. Please keep cables off the walkway and report every near miss.", ["tripped", "cables", "report"], "buổi nhắc an toàn đầu ngày"),
  ("This is a site alarm. Stop your work and leave by the nearest exit. Go to the assembly point and wait for your foreman.", ["alarm", "exit", "foreman"], "thông báo sơ tán"),
 ],
})

# ───────────────────────── 1. Làm việc trên cao & cẩu lắp ─────────────────────────
PHASES.append({
 "title": "Làm việc trên cao & cẩu lắp",
 "vocab": [
  ("scaffolding", "/ˈskæfəldɪŋ/", "n", "giàn giáo", "Don't use the <b>scaffolding</b> until it has a green tag.", "Chưa có thẻ xanh thì không được dùng giàn giáo.", "足場", "ashiba"),
  ("harness", "/ˈhɑːnɪs/", "n", "dây an toàn toàn thân", "On this site, wear a <b>harness</b> above two metres and clip it to an anchor point.", "Ở công trường này, làm việc cao trên hai mét phải đeo dây an toàn và móc vào điểm neo.", "フルハーネス", "furu hānesu"),
  ("guardrail", "/ˈɡɑːdreɪl/", "n", "lan can bảo vệ", "The <b>guardrail</b> on the edge of the slab is missing.", "Lan can ở mép sàn bị thiếu.", "手すり", "tesuri"),
  ("fall", "/fɔːl/", "n/v", "sự rơi, ngã (từ trên cao); rơi, ngã", "<b>Falls</b> from height are one of the main causes of death on construction sites.", "Ngã từ trên cao là một trong những nguyên nhân gây tử vong hàng đầu ở công trường.", "墜落", "tsuiraku"),
  ("crane", "/kreɪn/", "n", "cần cẩu", "The tower <b>crane</b> will lift the steel beams this afternoon.", "Chiều nay cẩu tháp sẽ cẩu các dầm thép.", "クレーン", "kurēn"),
  ("lifting plan", "/ˈlɪftɪŋ ˌplæn/", "n", "kế hoạch (biện pháp) cẩu lắp", "Heavy lifts need an approved <b>lifting plan</b>.", "Cẩu hàng nặng phải có kế hoạch cẩu lắp được duyệt."),
  ("suspended load", "/səˌspendɪd ˈləʊd/", "n", "vật đang được cẩu (treo lơ lửng)", "Never stand under a <b>suspended load</b>.", "Tuyệt đối không đứng dưới vật đang cẩu.", "吊り荷", "tsurini"),
  ("rigging", "/ˈrɪɡɪŋ/", "n", "công tác móc cáp, buộc hàng để cẩu", "Only trained workers can do the <b>rigging</b>.", "Chỉ công nhân đã được đào tạo mới được móc cáp, buộc hàng.", "玉掛け", "tamakake"),
  ("signalman", "/ˈsɪɡnəlmən/", "n", "người xi nhan (ra tín hiệu) cho cẩu", "The crane operator can't see the load, so he follows the <b>signalman</b>.", "Người lái cẩu không nhìn thấy hàng nên làm theo tín hiệu của người xi nhan.", "合図者", "aizusha"),
  ("ladder", "/ˈlædə/", "n", "cái thang", "Keep three points of contact when you climb a <b>ladder</b>.", "Khi leo thang luôn giữ ba điểm tiếp xúc.", "はしご", "hashigo"),
 ],
 "phrases": [
  ("Always clip your harness to an anchor point.", "Luôn móc dây an toàn vào điểm neo."),
  ("Has this scaffolding been checked today?", "Giàn giáo này hôm nay đã được kiểm tra chưa?"),
  ("Please don't use this scaffolding. It has a red tag.", "Đừng dùng giàn giáo này. Nó đang treo thẻ đỏ."),
  ("Stay out of the lifting area.", "Không vào khu vực đang cẩu."),
  ("Stop the lift! The wind is too strong.", "Dừng cẩu! Gió mạnh quá."),
  ("Tie your tools so they can't fall.", "Buộc dụng cụ lại để không bị rơi."),
  ("The guardrail is missing on the east side.", "Lan can phía đông bị thiếu."),
  ("Who is the signalman for this lift?", "Ai là người xi nhan cho lần cẩu này?"),
  ("This load is too heavy for this crane.", "Hàng này quá nặng so với sức nâng của cẩu."),
  ("Please check the slings before every lift.", "Kiểm tra cáp cẩu trước mỗi lần cẩu."),
 ],
 "dialogues": [
  ("I'm only going up for two minutes. Do I need my harness?", [
    ("Yes. Above two metres, you must wear it and clip it on — even for two minutes.", True, "Trả lời chắc chắn + quy tắc rõ ràng; ngã chỉ cần một giây."),
    ("Two minutes is OK, go quickly.", False, "Sai về an toàn — làm nhanh không làm giảm nguy cơ ngã."),
    ("You no need if careful.", False, "Sai ngữ pháp ('You don't need it') và khuyên sai về an toàn."),
  ]),
  ("The wind is getting very strong. Should we continue the lift?", [
    ("No. Let's stop and lower the load safely. We'll wait until the wind drops.", True, "Dừng đúng lúc + hạ hàng an toàn + chờ gió giảm."),
    ("Continue, we are behind schedule.", False, "Đặt tiến độ lên trên an toàn — gió mạnh làm hàng xoay, va đập, có thể rơi."),
    ("Wind is strong very.", False, "Sai trật tự từ ('very strong') và không trả lời có nên tiếp tục không."),
  ]),
  ("This scaffolding has a red tag. Can we use it?", [
    ("No, a red tag means it's not safe. Let's ask the scaffolding team to check and fix it first.", True, "Hiểu đúng ý nghĩa thẻ đỏ + bước xử lý."),
    ("The tag is old, just use it.", False, "Tự ý bỏ qua thẻ cảnh báo — rất nguy hiểm."),
    ("I don't know what mean red.", False, "Sai cấu trúc ('what red means') — thẻ đỏ = không được dùng, phải nắm rõ."),
  ]),
  ("Why did you stop the crane?", [
    ("Two workers walked under the load, so I stopped the lift until they left the area.", True, "Nêu lý do rõ ràng, đúng nguyên tắc không ai đứng dưới hàng đang cẩu."),
    ("Because crane stop.", False, "Câu cụt, thiếu mạo từ, sai thì ('I stopped it') và không giải thích lý do."),
    ("I stop because I want.", False, "Sai thì ('stopped') và không nêu lý do an toàn."),
  ]),
  ("Who can do the rigging for this lift?", [
    ("Tùng and Phát. They're both trained and certified riggers.", True, "Tên cụ thể + căn cứ đã được đào tạo, có chứng chỉ."),
    ("Anybody can, it's easy.", False, "Móc cáp phải do người được đào tạo — buộc sai có thể làm rơi hàng."),
    ("Tùng can maybe, I will see.", False, "Mơ hồ, thiếu chắc chắn — cần phân công người có chứng chỉ."),
  ]),
 ],
 "listen": [
  ("Never stand under a suspended load", ["stand", "load"], "nguyên tắc khi cẩu"),
  ("Always clip your harness to an anchor point", ["harness", "anchor"], "dây an toàn"),
  ("Stop the lift because the wind is too strong", ["lift", "wind"], "dừng cẩu vì gió"),
  ("Keep three points of contact on the ladder", ["three", "ladder"], "leo thang an toàn"),
  ("Attention, please. The tower crane will lift steel beams from two to four. Stay out of the lifting area and follow the signalman.", ["beams", "area", "signalman"], "thông báo cẩu lắp"),
  ("The guardrail on the fifth floor is missing. Please do not work near the edge. The scaffolding team will fix it this morning.", ["guardrail", "edge", "morning"], "báo thiếu lan can"),
 ],
})

# ───────────────────────── 2. Giao ban & tiến độ thi công ─────────────────────────
PHASES.append({
 "title": "Giao ban & tiến độ thi công",
 "vocab": [
  ("progress", "/ˈprəʊɡres/", "n", "tiến độ, tiến triển (công việc đã làm được)", "Let's check the <b>progress</b> on Block A.", "Mình xem tiến độ khối A nhé.", "進捗", "shinchoku"),
  ("schedule", "/ˈʃedjuːl/", "n", "tiến độ (kế hoạch thời gian), lịch", "We're two days behind <b>schedule</b> on the fourth floor.", "Tầng bốn đang chậm hai ngày so với tiến độ.", "工程", "kōtei"),
  ("milestone", "/ˈmaɪlstəʊn/", "n", "mốc tiến độ quan trọng", "Finishing the roof slab is our next <b>milestone</b>.", "Hoàn thành sàn mái là mốc tiến độ tiếp theo của mình."),
  ("manpower", "/ˈmænpaʊə/", "n", "nhân lực, số công nhân", "We need more <b>manpower</b> to finish the walls this week.", "Tuần này cần thêm nhân lực để làm xong tường."),
  ("subcontractor", "/ˌsʌbkənˈtræktə/", "n", "nhà thầu phụ", "The painting <b>subcontractor</b> starts on Monday.", "Nhà thầu phụ sơn bắt đầu vào thứ Hai.", "協力会社", "kyōryoku gaisha"),
  ("main contractor", "/ˌmeɪn kənˈtræktə/", "n", "tổng thầu, nhà thầu chính", "All subcontractors report to the <b>main contractor</b>.", "Tất cả nhà thầu phụ báo cáo cho tổng thầu.", "元請け", "motouke"),
  ("foreman", "/ˈfɔːmən/", "n", "đội trưởng, tổ trưởng thi công", "Ask the <b>foreman</b> how many workers he has today.", "Hỏi đội trưởng xem hôm nay có bao nhiêu công nhân.", "職長", "shokuchō"),
  ("delay", "/dɪˈleɪ/", "n/v", "sự chậm trễ; làm chậm", "The rain caused a two-day <b>delay</b>.", "Mưa làm chậm tiến độ hai ngày.", "遅れ", "okure"),
  ("catch up", "/ˌkætʃ ˈʌp/", "phr v", "đuổi kịp, bù lại tiến độ", "We'll work on Sunday to <b>catch up</b>.", "Chủ nhật tụi mình sẽ làm để bù tiến độ.", "挽回する", "bankai suru"),
  ("daily report", "/ˌdeɪli rɪˈpɔːt/", "n", "báo cáo ngày (nhật ký công trường)", "Please send the <b>daily report</b> before 6 p.m.", "Gửi báo cáo ngày trước 6 giờ chiều nhé.", "日報", "nippō"),
 ],
 "phrases": [
  ("We finished the fourth-floor slab today.", "Hôm nay tụi mình đã xong sàn tầng bốn."),
  ("Block A is on schedule.", "Khối A đang đúng tiến độ."),
  ("We're three days behind schedule because of the rain.", "Tụi mình chậm ba ngày so với tiến độ vì mưa."),
  ("We have 45 workers on site today.", "Hôm nay có 45 công nhân trên công trường."),
  ("The tiling team needs two more workers.", "Tổ ốp lát cần thêm hai người."),
  ("How can we catch up by the end of the month?", "Làm sao để bù kịp tiến độ trước cuối tháng?"),
  ("We'll add a night shift for the next three days.", "Ba ngày tới mình sẽ thêm ca đêm."),
  ("The next milestone is the roof slab on June 20.", "Mốc tiếp theo là sàn mái vào ngày 20/6."),
  ("What's the plan for tomorrow?", "Kế hoạch ngày mai thế nào?"),
  ("I'll update the schedule and send it this afternoon.", "Chiều nay tôi sẽ cập nhật tiến độ và gửi đi."),
 ],
 "dialogues": [
  ("How's the progress on Block B?", [
    ("The walls on the third floor are 80 percent done. We'll finish them on Thursday.", True, "Hạng mục + phần trăm + ngày dự kiến xong."),
    ("Block B is progress good.", False, "Sai ngữ pháp ('Block B is going well') và không có số liệu."),
    ("Workers are working hard.", False, "Chung chung, không nói được tiến độ đến đâu."),
  ]),
  ("Why are we behind schedule?", [
    ("The steel delivery was four days late, so the columns started late. We're adding workers to catch up.", True, "Nguyên nhân cụ thể + hệ quả + cách bù tiến độ."),
    ("Because the subcontractor is lazy.", False, "Đổ lỗi cảm tính, không có dữ liệu hay giải pháp."),
    ("We are behind because we are late.", False, "Lặp lại câu hỏi, không giải thích gì."),
  ]),
  ("How many workers do you have today?", [
    ("Forty-two. The formwork team is five people short, so I've asked their foreman for more.", True, "Con số + chỗ thiếu + đã làm gì."),
    ("Today have 42 people.", False, "Thiếu chủ ngữ: 'We have 42 workers today.'"),
    ("Enough, I think.", False, "Mơ hồ — giao ban cần con số chính xác."),
  ]),
  ("Can we finish the roof slab by June 20?", [
    ("It's possible if the concrete arrives on time. I'll confirm after I talk to the supplier this afternoon.", True, "Nêu điều kiện + hẹn giờ xác nhận, không hứa vội."),
    ("Yes, 100 percent, no problem.", False, "Hứa chắc khi chưa kiểm tra vật tư và nhân lực."),
    ("Cannot, too fast.", False, "Thiếu chủ ngữ, cộc lốc, không đưa phương án."),
  ]),
  ("What's the plan for tomorrow?", [
    ("We'll pour the columns on the fifth floor in the morning and start the slab formwork after lunch.", True, "Việc cụ thể + vị trí + thời gian."),
    ("Tomorrow we continue.", False, "Quá chung chung — tiếp tục việc gì, ở đâu?"),
    ("Tomorrow we will poured the columns.", False, "Sau 'will' dùng động từ nguyên mẫu: 'we will pour'."),
  ]),
 ],
 "listen": [
  ("We are two days behind schedule on Block A", ["behind", "schedule"], "báo chậm tiến độ"),
  ("We have forty workers on site today", ["forty", "workers"], "báo nhân lực"),
  ("The next milestone is the roof slab", ["milestone", "roof"], "mốc tiến độ"),
  ("Please send the daily report before six", ["daily", "six"], "nhắc báo cáo ngày"),
  ("Good morning, team. We finished the fourth-floor slab yesterday. Today we will start the walls, and the painters will arrive at ten.", ["finished", "walls", "painters"], "họp giao ban sáng"),
  ("We lost two days because of the rain. To catch up, we will work on Sunday. I will update the schedule tonight.", ["rain", "Sunday", "update"], "kế hoạch bù tiến độ"),
 ],
})

# ───────────────────────── 3. Bản vẽ, RFI & thay đổi thiết kế ─────────────────────────
PHASES.append({
 "title": "Bản vẽ, RFI & thay đổi thiết kế",
 "vocab": [
  ("drawing", "/ˈdrɔːɪŋ/", "n", "bản vẽ", "Please check the size on the <b>drawing</b> first.", "Kiểm tra kích thước trên bản vẽ trước nhé.", "図面", "zumen"),
  ("shop drawing", "/ˈʃɒp ˌdrɔːɪŋ/", "n", "bản vẽ triển khai thi công (shop drawing)", "The contractor must submit <b>shop drawings</b> for approval.", "Nhà thầu phải trình bản vẽ shop để duyệt.", "施工図", "sekōzu"),
  ("revision", "/rɪˈvɪʒn/", "n", "lần sửa đổi, phiên bản (Rev.)", "Are you using the latest <b>revision</b>? This one is Rev C.", "Anh có đang dùng bản sửa đổi mới nhất không? Bản này là Rev C.", "改訂", "kaitei"),
  ("RFI", "/ˌɑːr ef ˈaɪ/", "n", "phiếu yêu cầu làm rõ thông tin (request for information)", "The two drawings don't match, so I'll send an <b>RFI</b>.", "Hai bản vẽ không khớp nhau nên tôi sẽ gửi RFI.", "質疑書", "shitsugisho"),
  ("specification", "/ˌspesɪfɪˈkeɪʃn/", "n", "chỉ dẫn kỹ thuật (spec)", "The <b>specification</b> says the floor tiles must be 60 by 60 centimetres.", "Chỉ dẫn kỹ thuật yêu cầu gạch lát nền phải là 60x60 cm.", "仕様書", "shiyōsho"),
  ("dimension", "/daɪˈmenʃn/", "n", "kích thước", "This <b>dimension</b> is missing on the drawing.", "Bản vẽ bị thiếu kích thước này.", "寸法", "sunpō"),
  ("clash", "/klæʃ/", "n/v", "va chạm, xung đột (giữa các hệ, ví dụ ống và dầm); bị vướng", "There's a <b>clash</b> between the duct and the beam.", "Ống gió và dầm bị vướng nhau.", "干渉", "kanshō"),
  ("design change", "/dɪˈzaɪn ˌtʃeɪndʒ/", "n", "thay đổi thiết kế", "The client asked for a <b>design change</b> in the lobby.", "Chủ đầu tư yêu cầu thay đổi thiết kế ở sảnh.", "設計変更", "sekkei henkō"),
  ("approve", "/əˈpruːv/", "v", "phê duyệt", "The consultant <b>approved</b> the shop drawing yesterday.", "Hôm qua tư vấn đã duyệt bản vẽ shop.", "承認する", "shōnin suru"),
  ("grid line", "/ˈɡrɪd ˌlaɪn/", "n", "trục (trên lưới trục của bản vẽ)", "The column is on <b>grid line</b> C.", "Cột nằm trên trục C.", "通り芯", "tōrishin"),
 ],
 "phrases": [
  ("Which revision are you using?", "Anh đang dùng bản sửa đổi nào?"),
  ("This drawing is out of date. Please use Rev D.", "Bản vẽ này cũ rồi. Hãy dùng Rev D."),
  ("The architectural and structural drawings don't match.", "Bản vẽ kiến trúc và bản vẽ kết cấu không khớp nhau."),
  ("I'll send an RFI to the consultant today.", "Hôm nay tôi sẽ gửi RFI cho tư vấn."),
  ("We can't continue until we get an answer.", "Chưa có trả lời thì chưa làm tiếp được."),
  ("Could you show me on the drawing?", "Anh chỉ giúp tôi trên bản vẽ được không?"),
  ("The pipe clashes with the beam at grid line 5.", "Ống bị vướng dầm ở trục 5."),
  ("Is this change approved in writing?", "Thay đổi này đã được duyệt bằng văn bản chưa?"),
  ("Please mark the change on the drawing.", "Hãy ghi chú phần thay đổi lên bản vẽ."),
  ("This design change will affect the cost and the schedule.", "Thay đổi thiết kế này sẽ ảnh hưởng đến chi phí và tiến độ."),
 ],
 "dialogues": [
  ("The window opening in your wall is different from the drawing.", [
    ("Let me check. We used Rev B, but Rev C changed the size. I'll correct it.", True, "Kiểm tra + tìm ra nguyên nhân (sai phiên bản) + sửa."),
    ("The drawing is wrong, not us.", False, "Đổ lỗi khi chưa kiểm tra phiên bản bản vẽ."),
    ("Small different, no problem.", False, "Sai từ loại ('a small difference') và xem nhẹ sai khác so với bản vẽ."),
  ]),
  ("The duct clashes with the beam. What should we do?", [
    ("Let's stop that section and send an RFI with photos to the consultant. Our team can work in another area in the meantime.", True, "Dừng đúng chỗ + gửi RFI kèm ảnh + không để đội ngồi chờ."),
    ("Just cut a small hole in the beam.", False, "Rất nguy hiểm — không bao giờ tự ý đục, cắt kết cấu khi chưa có thiết kế duyệt."),
    ("I don't know, ask the designer yourself.", False, "Đùn đẩy — người phát hiện nên gửi RFI theo quy trình."),
  ]),
  ("Can you start the lobby ceiling today?", [
    ("Not yet. The ceiling design is changing, and we're still waiting for the new drawing.", True, "Trả lời + lý do (chờ bản vẽ mới)."),
    ("Yes, we start, later change again.", False, "Làm theo bản vẽ sắp đổi thì sẽ phải phá ra làm lại, tốn tiền."),
    ("Lobby ceiling is not start.", False, "Sai ngữ pháp ('hasn't started') và chưa nói lý do."),
  ]),
  ("The client wants to move this wall 50 centimetres. Can your team do it now?", [
    ("We can, but we need the change approved in writing first. It may also affect the cost.", True, "Đồng ý có điều kiện: phải có văn bản duyệt + nhắc ảnh hưởng chi phí."),
    ("OK, we move now, no need paper.", False, "Làm thay đổi khi chưa có văn bản — dễ tranh chấp chi phí về sau."),
    ("Wall cannot move.", False, "Từ chối cộc lốc, không giải thích hay đưa hướng xử lý."),
  ]),
  ("When will we get an answer to our RFI?", [
    ("The consultant said by Friday. If it's later, the ceiling work will be delayed, so I'll remind them on Wednesday.", True, "Mốc thời gian + rủi ro + chủ động nhắc."),
    ("Maybe next week, maybe next month.", False, "Mơ hồ — cần mốc thời gian cụ thể và theo dõi."),
    ("I sent already, now wait.", False, "Sai ngữ pháp ('I've already sent it') và bị động, không theo dõi."),
  ]),
 ],
 "listen": [
  ("Please use the latest revision of the drawing", ["latest", "revision"], "dùng bản vẽ mới nhất"),
  ("I will send an RFI to the consultant today", ["RFI", "consultant"], "gửi RFI"),
  ("The pipe clashes with the beam at grid line five", ["clashes", "beam"], "phát hiện va chạm"),
  ("This change must be approved in writing", ["approved", "writing"], "duyệt thay đổi"),
  ("The wall on grid line C is thirty centimetres too long. We used an old drawing. Please check the revision before you start work.", ["thirty", "old", "revision"], "sai vì dùng bản vẽ cũ"),
  ("The client wants a design change in the lobby. The new drawing will come on Friday. Please stop the ceiling work until then.", ["lobby", "Friday", "ceiling"], "thông báo thay đổi thiết kế"),
 ],
})

# ───────────────────────── 4. Vật tư & giao hàng công trường ─────────────────────────
PHASES.append({
 "title": "Vật tư & giao hàng công trường",
 "vocab": [
  ("submittal", "/səbˈmɪtl/", "n", "hồ sơ trình duyệt (vật tư, mẫu, bản vẽ)", "The tile <b>submittal</b> is still waiting for approval.", "Hồ sơ trình duyệt gạch vẫn đang chờ duyệt."),
  ("delivery", "/dɪˈlɪvəri/", "n", "việc giao hàng (vật tư vào công trường)", "The steel <b>delivery</b> is coming at 7 a.m. tomorrow.", "Thép sẽ được giao lúc 7 giờ sáng mai.", "搬入", "hannyū"),
  ("delivery note", "/dɪˈlɪvəri ˌnəʊt/", "n", "phiếu giao hàng", "Check the <b>delivery note</b> before you sign it.", "Kiểm tra phiếu giao hàng trước khi ký.", "納品書", "nōhinsho"),
  ("quantity", "/ˈkwɒntəti/", "n", "số lượng, khối lượng", "The <b>quantity</b> on the truck doesn't match the order.", "Số lượng trên xe không khớp với đơn đặt hàng.", "数量", "sūryō"),
  ("storage area", "/ˈstɔːrɪdʒ ˌeəriə/", "n", "bãi tập kết, khu chứa vật tư", "Keep the cement in the covered <b>storage area</b>.", "Để xi măng trong khu chứa vật tư có mái che.", "資材置き場", "shizai okiba"),
  ("cement", "/sɪˈment/", "n", "xi măng", "These <b>cement</b> bags got wet in the rain.", "Mấy bao xi măng này bị ướt mưa.", "セメント", "semento"),
  ("brick", "/brɪk/", "n", "gạch xây", "We need 20,000 more <b>bricks</b> for the fifth floor.", "Tầng năm cần thêm 20.000 viên gạch."),
  ("lead time", "/ˈliːd ˌtaɪm/", "n", "thời gian chờ hàng (từ lúc đặt đến lúc giao)", "The <b>lead time</b> for the imported elevators is twelve weeks.", "Thời gian chờ hàng của thang máy nhập khẩu là mười hai tuần.", "リードタイム", "rīdo taimu"),
  ("unload", "/ʌnˈləʊd/", "v", "dỡ hàng (xuống xe)", "Use the forklift to <b>unload</b> the pallets.", "Dùng xe nâng để dỡ các pallet xuống.", "荷下ろしする", "nioroshi suru"),
  ("damaged", "/ˈdæmɪdʒd/", "adj", "bị hư hỏng, bể vỡ", "Ten tiles were <b>damaged</b> during delivery.", "Mười viên gạch bị vỡ trong lúc giao hàng."),
 ],
 "phrases": [
  ("The delivery is late again. When will it arrive?", "Hàng lại giao trễ rồi. Khi nào mới tới?"),
  ("The truck is at the gate. Where should it unload?", "Xe đang ở cổng. Dỡ hàng ở đâu?"),
  ("The quantity doesn't match the delivery note.", "Số lượng không khớp với phiếu giao hàng."),
  ("Ten bags of cement are wet. We can't accept them.", "Mười bao xi măng bị ướt. Bên tôi không nhận mấy bao này."),
  ("Please take photos of the damaged items.", "Chụp ảnh giúp những món bị hư nhé."),
  ("Has the consultant approved this material?", "Tư vấn đã duyệt vật tư này chưa?"),
  ("This isn't the approved brand. Please don't use it.", "Đây không phải hãng đã được duyệt. Đừng dùng nhé."),
  ("Please store the cement off the ground and cover it.", "Để xi măng kê cao khỏi mặt đất và che lại."),
  ("We need the rebar by Thursday, or the slab will be late.", "Cần thép trước thứ Năm, nếu không sàn sẽ bị trễ."),
  ("Deliveries are only allowed from 7 to 11 a.m.", "Chỉ được giao hàng từ 7 đến 11 giờ sáng."),
 ],
 "dialogues": [
  ("The truck is here with the tiles. Can I unload now?", [
    ("Yes, please unload them in storage area 2. I'll check the quantity against the delivery note.", True, "Chỉ chỗ dỡ hàng + kiểm tra số lượng theo phiếu giao."),
    ("Put anywhere.", False, "Cộc và gây lộn xộn — vật tư phải để đúng khu tập kết."),
    ("Yes, unload, I sign now.", False, "Ký phiếu khi chưa kiểm tra số lượng và tình trạng hàng."),
  ]),
  ("Why is the rebar delivery late?", [
    ("The supplier's truck broke down. The new time is 2 p.m., so the rebar team will work on the columns this morning.", True, "Lý do + giờ giao mới + sắp xếp lại việc để không lãng phí."),
    ("Supplier always late, I don't know.", False, "Thiếu động từ ('The supplier is always late') và không có thông tin mới."),
    ("It will late two hours.", False, "Thiếu 'be': 'It will be two hours late.'"),
  ]),
  ("Some of the cement bags are wet.", [
    ("Please separate them and don't use them. I'll take photos and ask the supplier to replace them.", True, "Tách riêng + không dùng + ghi nhận bằng chứng + yêu cầu đổi."),
    ("Wet cement is OK, use it first.", False, "Sai kỹ thuật — xi măng bị ẩm, vón cục làm giảm chất lượng bê tông, vữa."),
    ("Rain make it wet.", False, "Chỉ nêu lý do, thiếu 's' ('makes') và không xử lý gì."),
  ]),
  ("Can we use these pipes? They're a different brand.", [
    ("Not yet. They're not the approved brand, so we need to send a submittal to the consultant first.", True, "Không dùng vật tư chưa duyệt + đúng quy trình trình duyệt."),
    ("Same same, just use.", False, "Dùng vật tư chưa duyệt — có thể bị tư vấn bắt tháo ra làm lại."),
    ("Who buy these pipes?", False, "Sai ngữ pháp ('Who bought…?') và chưa giải quyết câu hỏi."),
  ]),
  ("What's the lead time for the elevators?", [
    ("Twelve weeks from the order date, so we must order them by the end of this month.", True, "Con số + hệ quả cho kế hoạch đặt hàng."),
    ("Very long time.", False, "Mơ hồ, không có con số."),
    ("Elevator will lead twelve week.", False, "Dùng sai 'lead' như động từ và thiếu 's' số nhiều ('weeks')."),
  ]),
 ],
 "listen": [
  ("The steel delivery is coming at seven tomorrow", ["steel", "seven"], "lịch giao thép"),
  ("The quantity does not match the delivery note", ["quantity", "note"], "số lượng không khớp"),
  ("Please keep the cement off the ground", ["cement", "ground"], "bảo quản xi măng"),
  ("Ten tiles were damaged during delivery", ["tiles", "damaged"], "hàng bị vỡ"),
  ("Hello, this is the site office. The rebar truck is two hours late. Please call me with the new arrival time.", ["office", "late", "arrival"], "gọi hỏi xe thép trễ"),
  ("The tiles arrived this morning. Twenty boxes are broken. I have taken photos and sent them to the supplier.", ["arrived", "broken", "photos"], "báo hàng bể"),
 ],
})

# ───────────────────────── 5. Bê tông, cốt thép & kết cấu ─────────────────────────
PHASES.append({
 "title": "Bê tông, cốt thép & kết cấu",
 "vocab": [
  ("concrete", "/ˈkɒŋkriːt/", "n", "bê tông", "The first <b>concrete</b> truck arrives at six.", "Xe bê tông đầu tiên đến lúc sáu giờ.", "コンクリート", "konkurīto"),
  ("pour", "/pɔː/", "v/n", "đổ (bê tông); đợt đổ bê tông", "We'll <b>pour</b> the slab tomorrow morning.", "Sáng mai tụi mình đổ sàn.", "打設する", "dasetsu suru"),
  ("formwork", "/ˈfɔːmwɜːk/", "n", "cốp pha", "Check the <b>formwork</b> before the pour.", "Kiểm tra cốp pha trước khi đổ bê tông.", "型枠", "katawaku"),
  ("rebar", "/ˈriːbɑː/", "n", "cốt thép, thép thanh", "The <b>rebar</b> spacing is 200 millimetres.", "Khoảng cách thép là 200 mi-li-mét.", "鉄筋", "tekkin"),
  ("curing", "/ˈkjʊərɪŋ/", "n", "bảo dưỡng bê tông (giữ ẩm)", "<b>Curing</b> is important: keep the slab wet for at least seven days.", "Bảo dưỡng rất quan trọng: giữ ẩm sàn ít nhất bảy ngày.", "養生", "yōjō"),
  ("slump test", "/ˈslʌmp ˌtest/", "n", "thí nghiệm độ sụt (bê tông)", "Do a <b>slump test</b> on every truck.", "Làm thí nghiệm độ sụt cho từng xe.", "スランプ試験", "suranpu shiken"),
  ("concrete cover", "/ˌkɒŋkriːt ˈkʌvə/", "n", "lớp bê tông bảo vệ (cốt thép)", "Use spacers to keep 25 millimetres of <b>concrete cover</b>.", "Dùng con kê để đảm bảo lớp bê tông bảo vệ 25 mi-li-mét.", "かぶり厚さ", "kaburi atsusa"),
  ("column", "/ˈkɒləm/", "n", "cột", "The <b>columns</b> on the sixth floor are ready for inspection.", "Các cột tầng sáu đã sẵn sàng để nghiệm thu.", "柱", "hashira"),
  ("beam", "/biːm/", "n", "dầm", "Don't remove the props under this <b>beam</b> yet.", "Chưa được tháo cây chống dưới dầm này.", "梁", "hari"),
  ("slab", "/slæb/", "n", "sàn (bê tông)", "The <b>slab</b> is 150 millimetres thick.", "Sàn dày 150 mi-li-mét.", "スラブ", "surabu"),
 ],
 "phrases": [
  ("The concrete pour starts at 6 a.m.", "Đổ bê tông bắt đầu lúc 6 giờ sáng."),
  ("Has the formwork been checked and approved?", "Cốp pha đã được kiểm tra và duyệt chưa?"),
  ("The rebar spacing is wrong here. Please fix it before the pour.", "Khoảng cách thép chỗ này sai. Sửa trước khi đổ nhé."),
  ("The slump is 12 centimetres. That's within spec.", "Độ sụt 12 cm. Nằm trong tiêu chuẩn."),
  ("Please don't add water to the concrete.", "Không được thêm nước vào bê tông."),
  ("We'll take cube samples for the strength test.", "Mình sẽ lấy mẫu lập phương để thí nghiệm cường độ."),
  ("Keep the slab wet for at least seven days.", "Giữ ẩm sàn ít nhất bảy ngày."),
  ("Don't remove the formwork until the engineer says it's OK.", "Kỹ sư chưa cho phép thì chưa được tháo cốp pha."),
  ("We need 60 cubic metres of concrete for this slab.", "Sàn này cần 60 mét khối bê tông."),
  ("There's a crack in this column. Let's ask the structural engineer.", "Cột này bị nứt. Mình hỏi kỹ sư kết cấu nhé."),
 ],
 "dialogues": [
  ("The concrete is too stiff. Can we add some water?", [
    ("No. Adding water makes the concrete weaker. Let's do a slump test, and if it fails, we'll reject the truck.", True, "Từ chối dứt khoát + lý do kỹ thuật + đúng quy trình (thử độ sụt, trả xe)."),
    ("OK, a little water only.", False, "Sai kỹ thuật — thêm nước làm giảm cường độ bê tông, lỗi rất hay gặp."),
    ("Concrete stiff is normal.", False, "Sai trật tự từ ('Stiff concrete…') và bỏ qua kiểm tra chất lượng."),
  ]),
  ("Is everything ready for tomorrow's pour?", [
    ("Almost. The formwork and rebar passed inspection. We're just waiting for the pump company to confirm.", True, "Tình trạng từng hạng mục + việc còn chờ."),
    ("Ready, ready.", False, "Trả lời vội, không nói rõ đã kiểm tra những gì."),
    ("Tomorrow we pour, I think OK.", False, "Thiếu chắc chắn và thiếu động từ ('I think it's OK')."),
  ]),
  ("When can we remove the formwork from this slab?", [
    ("When the concrete reaches the required strength. We'll check the cube test results and ask the engineer first.", True, "Đúng nguyên tắc: tháo cốp pha khi đủ cường độ và có kỹ sư đồng ý."),
    ("Tomorrow, because we need the formwork for the next floor.", False, "Đặt tiến độ lên trên an toàn — tháo cốp pha sớm có thể làm sập sàn."),
    ("When it dry.", False, "Thiếu động từ ('when it's dry') và sai — khô bề mặt không có nghĩa là đủ cường độ."),
  ]),
  ("The rebar spacing here is 250, but the drawing says 200.", [
    ("You're right. We'll add bars to fix the spacing before the pour and ask you to check again.", True, "Thừa nhận + sửa trước khi đổ + mời kiểm tra lại."),
    ("250 or 200, same strong.", False, "Sai kỹ thuật và ngữ pháp — phải làm đúng bản vẽ."),
    ("The workers did it, not me.", False, "Đổ lỗi, không đưa hướng khắc phục."),
  ]),
  ("How many trucks of concrete do we need?", [
    ("About ten. The slab needs 70 cubic metres, and each truck carries seven.", True, "Con số + cách tính rõ ràng."),
    ("Many trucks.", False, "Mơ hồ, không có con số."),
    ("We need concrete 70.", False, "Sai trật tự, thiếu đơn vị: '70 cubic metres of concrete'."),
  ]),
 ],
 "listen": [
  ("The concrete pour starts at six tomorrow", ["pour", "six"], "giờ đổ bê tông"),
  ("Please do not add water to the concrete", ["add", "water"], "cấm thêm nước"),
  ("Check the formwork before the pour", ["formwork", "pour"], "kiểm tra cốp pha"),
  ("Keep the slab wet for seven days", ["wet", "seven"], "bảo dưỡng bê tông"),
  ("The first truck has arrived. The slump is ten centimetres, so it is within spec. Please start the pump.", ["truck", "slump", "pump"], "bắt đầu đổ bê tông"),
  ("We found a problem with the rebar on the sixth floor. The spacing is too wide. We will fix it before the pour.", ["rebar", "spacing", "fix"], "sửa cốt thép trước khi đổ"),
 ],
})

# ───────────────────────── 6. Kiểm tra, nghiệm thu & NCR ─────────────────────────
PHASES.append({
 "title": "Kiểm tra, nghiệm thu & NCR",
 "vocab": [
  ("inspection request", "/ɪnˈspekʃn rɪˌkwest/", "n", "phiếu yêu cầu nghiệm thu", "I'll send the <b>inspection request</b> for the sixth-floor columns today.", "Hôm nay tôi sẽ gửi phiếu yêu cầu nghiệm thu cột tầng sáu."),
  ("hold point", "/ˈhəʊld ˌpɔɪnt/", "n", "điểm dừng chờ nghiệm thu (chưa nghiệm thu thì không được làm tiếp)", "Rebar inspection is a <b>hold point</b> — no pour before approval.", "Nghiệm thu cốt thép là điểm dừng — chưa duyệt thì không được đổ bê tông."),
  ("NCR", "/ˌen siː ˈɑː/", "n", "phiếu báo không phù hợp (non-conformance report)", "The consultant issued an <b>NCR</b> for the cracked wall.", "Tư vấn đã ra phiếu NCR cho bức tường bị nứt.", "不適合報告書", "futekigō hōkokusho"),
  ("checklist", "/ˈtʃeklɪst/", "n", "bảng kiểm (checklist)", "Use the <b>checklist</b> when you check the formwork.", "Dùng bảng kiểm khi kiểm tra cốp pha.", "チェックリスト", "chekku risuto"),
  ("rework", "/ˌriːˈwɜːk/", "v", "làm lại (phần làm sai)", "We have to <b>rework</b> the plaster on this wall.", "Tụi mình phải làm lại lớp trát trên bức tường này.", "手直しする", "tenaoshi suru"),
  ("crack", "/kræk/", "n", "vết nứt", "There's a small <b>crack</b> in the wall near the window.", "Có một vết nứt nhỏ trên tường gần cửa sổ.", "ひび割れ", "hibiware"),
  ("witness", "/ˈwɪtnəs/", "v", "chứng kiến, có mặt khi kiểm tra/thí nghiệm", "The consultant will <b>witness</b> the pressure test.", "Tư vấn sẽ có mặt chứng kiến buổi thử áp lực.", "立ち会う", "tachiau"),
  ("method statement", "/ˈmeθəd ˌsteɪtmənt/", "n", "biện pháp thi công (văn bản)", "Please submit the <b>method statement</b> before you start the work.", "Vui lòng nộp biện pháp thi công trước khi bắt đầu.", "施工要領書", "sekō yōryōsho"),
  ("comply", "/kəmˈplaɪ/", "v", "tuân thủ, đáp ứng (yêu cầu)", "This work doesn't <b>comply</b> with the specification.", "Phần việc này không đáp ứng chỉ dẫn kỹ thuật."),
  ("close out", "/ˌkləʊz ˈaʊt/", "phr v", "đóng (phiếu NCR, hồ sơ sau khi khắc phục xong)", "We can <b>close out</b> the NCR after the rework is approved.", "Sau khi phần làm lại được duyệt thì mình đóng được phiếu NCR."),
 ],
 "phrases": [
  ("The columns on Level 6 are ready for inspection.", "Cột tầng 6 đã sẵn sàng nghiệm thu."),
  ("Could you inspect the rebar at 2 p.m. today?", "Anh nghiệm thu cốt thép lúc 2 giờ chiều nay được không?"),
  ("We checked everything with the checklist.", "Tụi tôi đã kiểm tra hết theo bảng kiểm."),
  ("The inspection passed. We can pour tomorrow.", "Nghiệm thu đạt. Mai đổ được rồi."),
  ("The consultant rejected the plastering on the third floor.", "Tư vấn không chấp nhận phần trát tầng ba."),
  ("What do we need to do to close out this NCR?", "Mình cần làm gì để đóng phiếu NCR này?"),
  ("We'll finish the rework by Thursday and ask for a re-inspection.", "Tụi tôi sẽ làm lại xong trước thứ Năm và mời nghiệm thu lại."),
  ("This doesn't comply with the approved method statement.", "Việc này làm không đúng biện pháp thi công đã duyệt."),
  ("Could you sign the inspection form, please?", "Anh ký giúp biên bản nghiệm thu được không?"),
 ],
 "dialogues": [
  ("Are the columns ready for inspection?", [
    ("Yes. We've checked the rebar, the cover and the formwork with the checklist. You can inspect them at 2 p.m.", True, "Xác nhận + đã tự kiểm tra những gì + giờ hẹn."),
    ("Yes, I think ready.", False, "Thiếu chủ ngữ/động từ ('I think they're ready') và nghe như chưa tự kiểm tra."),
    ("Columns is ready yesterday.", False, "Sai chia động từ ('are') và sai thì."),
  ]),
  ("The concrete cover here is only 10 millimetres. The spec says 25.", [
    ("You're right. We'll add spacers now and ask you to check again before the pour.", True, "Thừa nhận + khắc phục cụ thể + mời kiểm tra lại."),
    ("10 millimetres is enough, no problem.", False, "Cãi lại tiêu chuẩn — lớp bảo vệ mỏng làm cốt thép dễ bị gỉ."),
    ("Please sign first, we fix later.", False, "Xin ký trước rồi mới sửa — sai quy trình, mất uy tín với tư vấn."),
  ]),
  ("Why did you pour the slab before the inspection?", [
    ("I'm sorry. The concrete arrived early and we didn't wait. I'll send you the photos and records, and we'll respect every hold point from now on.", True, "Nhận lỗi + cung cấp bằng chứng + cam kết tuân thủ điểm dừng."),
    ("Because the concrete came, cannot wait.", False, "Bào chữa, thiếu chủ ngữ — bỏ qua điểm dừng là lỗi nghiêm trọng."),
    ("Inspection is not important for slab.", False, "Sai hoàn toàn — nghiệm thu cốt thép trước khi đổ là bắt buộc."),
  ]),
  ("We've issued an NCR for the cracked wall.", [
    ("Thank you. We'll find the cause, send you a repair method by Friday and fix it after you approve it.", True, "Tiếp nhận + tìm nguyên nhân + đề xuất cách sửa + chờ duyệt."),
    ("The crack is small, no need NCR.", False, "Sai ngữ pháp ('There's no need for an NCR') và phản bác thay vì xử lý."),
    ("OK, we paint over it.", False, "Sơn phủ lên vết nứt là giấu lỗi, không khắc phục nguyên nhân."),
  ]),
  ("Can we close out the NCR?", [
    ("Yes. The rework is done, and the consultant approved it this morning. Here are the photos and the signed form.", True, "Xác nhận + căn cứ (đã duyệt) + hồ sơ kèm theo."),
    ("Yes, we fixed, I think.", False, "Thiếu 'it' và không chắc chắn — đóng NCR cần bằng chứng."),
    ("NCR close already long time.", False, "Sai ngữ pháp và không đưa hồ sơ."),
  ]),
 ],
 "listen": [
  ("The columns on level six are ready for inspection", ["columns", "inspection"], "mời nghiệm thu"),
  ("We checked the formwork with the checklist", ["formwork", "checklist"], "tự kiểm tra"),
  ("The consultant issued an NCR for this wall", ["issued", "wall"], "phiếu NCR"),
  ("We will finish the rework by Thursday", ["rework", "Thursday"], "hẹn làm lại"),
  ("The rebar inspection is at two o'clock. Please do not pour before the consultant signs the form. This is a hold point.", ["inspection", "signs", "hold"], "nhắc điểm dừng"),
  ("The consultant rejected the plaster on the third floor. The wall is not flat. We will rework it and ask for a new inspection on Friday.", ["rejected", "flat", "Friday"], "báo kết quả nghiệm thu"),
 ],
})

# ───────────────────────── 7. Hệ thống MEP (điện, nước, điều hòa) ─────────────────────────
PHASES.append({
 "title": "Hệ thống MEP (điện, nước, điều hòa)",
 "vocab": [
  ("MEP", "/ˌem iː ˈpiː/", "n", "cơ điện (M&E: điện, cấp thoát nước, điều hòa thông gió)", "The <b>MEP</b> team will start on the second floor next week.", "Tuần sau đội cơ điện bắt đầu làm tầng hai.", "設備", "setsubi"),
  ("wiring", "/ˈwaɪərɪŋ/", "n", "hệ thống dây điện, việc đi dây", "The <b>wiring</b> in the ceiling is finished.", "Phần đi dây trên trần đã xong.", "配線", "haisen"),
  ("piping", "/ˈpaɪpɪŋ/", "n", "hệ thống đường ống", "The water <b>piping</b> goes through this wall.", "Đường ống nước đi xuyên qua bức tường này.", "配管", "haikan"),
  ("duct", "/dʌkt/", "n", "ống gió (điều hòa, thông gió)", "The air-con <b>duct</b> is too low for the ceiling.", "Ống gió điều hòa thấp quá so với trần.", "ダクト", "dakuto"),
  ("sleeve", "/sliːv/", "n", "ống lồng chờ (đặt sẵn xuyên sàn, xuyên tường)", "Put the <b>sleeves</b> in before the concrete pour.", "Đặt ống lồng trước khi đổ bê tông.", "スリーブ", "surību"),
  ("pressure test", "/ˈpreʃə ˌtest/", "n", "thử áp lực (đường ống)", "The pipes passed the <b>pressure test</b>.", "Đường ống đã đạt thử áp lực.", "耐圧試験", "taiatsu shiken"),
  ("distribution board", "/ˌdɪstrɪˈbjuːʃn ˌbɔːd/", "n", "tủ điện phân phối", "Each floor has one <b>distribution board</b>.", "Mỗi tầng có một tủ điện phân phối.", "分電盤", "bundenban"),
  ("commissioning", "/kəˈmɪʃənɪŋ/", "n", "chạy thử và hiệu chỉnh hệ thống (trước bàn giao)", "The <b>commissioning</b> of the air-con system starts in May.", "Chạy thử hệ thống điều hòa bắt đầu vào tháng Năm.", "試運転調整", "shiunten chōsei"),
  ("isolate", "/ˈaɪsəleɪt/", "v", "cô lập, ngắt (nguồn điện, nước)", "<b>Isolate</b> the power before you open the board.", "Ngắt nguồn điện trước khi mở tủ."),
  ("leak", "/liːk/", "n/v", "chỗ rò rỉ; rò rỉ", "There's a water <b>leak</b> above the ceiling.", "Có chỗ rò nước phía trên trần.", "漏水", "rōsui"),
 ],
 "phrases": [
  ("The wiring on Level 3 is 70 percent done.", "Phần đi dây điện tầng 3 xong 70%."),
  ("The duct clashes with the sprinkler pipe here.", "Ống gió bị vướng ống sprinkler ở đây."),
  ("We need a sleeve here before the pour.", "Chỗ này cần đặt ống lồng trước khi đổ bê tông."),
  ("Please isolate the power and lock the board before you start.", "Ngắt điện và khóa tủ trước khi bắt đầu nhé."),
  ("Always test that the cable is dead before you touch it.", "Luôn đo kiểm tra dây đã hết điện trước khi chạm vào."),
  ("We'll do the pressure test at 10 bar for two hours.", "Tụi tôi sẽ thử áp lực 10 bar trong hai tiếng."),
  ("The pressure dropped, so there's a leak somewhere.", "Áp suất bị tụt, vậy là có chỗ rò."),
  ("Can we close the ceiling now?", "Giờ đóng trần được chưa?"),
  ("Not yet. The MEP inspection isn't finished.", "Chưa được. Nghiệm thu cơ điện chưa xong."),
  ("Commissioning will take about two weeks.", "Chạy thử hệ thống mất khoảng hai tuần."),
 ],
 "dialogues": [
  ("Can the ceiling team close the ceiling on Level 4?", [
    ("Not yet. The pressure test for the pipes is tomorrow. After it passes, they can close it.", True, "Trả lời + lý do + điều kiện để làm tiếp."),
    ("Yes, close it, we test later.", False, "Đóng trần trước khi thử áp — nếu rò thì phải phá trần ra, tốn công."),
    ("Ceiling team always hurry.", False, "Than phiền, thiếu động từ ('is always in a hurry') và không trả lời."),
  ]),
  ("The pressure dropped during the test. What does that mean?", [
    ("There's probably a leak. We'll check the joints one by one, fix it and test again.", True, "Nhận định + cách tìm lỗi + thử lại."),
    ("Pressure drop a little is normal.", False, "Sai ngữ pháp và bỏ qua dấu hiệu rò rỉ."),
    ("Maybe the gauge is broken, just sign.", False, "Đoán mò và xin ký cho qua — sai quy trình nghiệm thu."),
  ]),
  ("Can I work on this distribution board now?", [
    ("Only after it's isolated and locked off. Please test that it's dead before you touch anything.", True, "Đúng quy trình an toàn điện: cắt – khóa – đo kiểm tra."),
    ("Yes, just wear gloves.", False, "Rất nguy hiểm — găng tay không thay được việc cắt điện."),
    ("Power is off I think, go.", False, "Đoán là đã cắt điện — phải kiểm tra chắc chắn."),
  ]),
  ("The duct hits the beam here. Can you move it?", [
    ("We can lower it by 100 millimetres, but that affects the ceiling height. I'll send an RFI to confirm.", True, "Đưa phương án + nêu ảnh hưởng + xin xác nhận bằng RFI."),
    ("We make a hole in the beam, easy.", False, "Không được tự đục dầm — ảnh hưởng kết cấu."),
    ("Duct cannot move, sorry.", False, "Từ chối cộc lốc, không đề xuất phương án."),
  ]),
  ("When will the air-con system be ready?", [
    ("Installation will finish on May 10. Commissioning takes two weeks, so it'll be ready by May 24.", True, "Mốc lắp đặt + thời gian chạy thử + ngày sẵn sàng."),
    ("Soon, the team is fast.", False, "Mơ hồ, không có ngày cụ thể."),
    ("It ready end of May maybe.", False, "Thiếu động từ ('It will be ready') và thiếu chắc chắn."),
  ]),
 ],
 "listen": [
  ("Please isolate the power before you start", ["isolate", "power"], "ngắt điện an toàn"),
  ("The pipes passed the pressure test", ["passed", "pressure"], "kết quả thử áp"),
  ("We need a sleeve here before the pour", ["sleeve", "pour"], "đặt ống lồng"),
  ("There is a water leak above the ceiling", ["leak", "ceiling"], "phát hiện rò nước"),
  ("The pressure test on Level three failed. The pressure dropped after one hour. We are checking the joints now.", ["failed", "dropped", "joints"], "báo thử áp không đạt"),
  ("Do not close the ceiling on Level five yet. The wiring is not finished. The electricians will finish it by Friday.", ["close", "wiring", "electricians"], "nhắc chưa đóng trần"),
 ],
})

# ───────────────────────── 8. Thời tiết, sự cố & môi trường ─────────────────────────
PHASES.append({
 "title": "Thời tiết, sự cố & môi trường",
 "vocab": [
  ("forecast", "/ˈfɔːkɑːst/", "n", "dự báo (thời tiết)", "The <b>forecast</b> says heavy rain this afternoon.", "Dự báo chiều nay mưa to.", "天気予報", "tenki yohō"),
  ("typhoon", "/taɪˈfuːn/", "n", "bão lớn (bão nhiệt đới)", "A <b>typhoon</b> is coming, so we'll stop all crane work.", "Bão sắp tới nên tụi mình dừng mọi việc cẩu.", "台風", "taifū"),
  ("heatstroke", "/ˈhiːtstrəʊk/", "n", "sốc nhiệt, say nắng", "Drink water often to prevent <b>heatstroke</b>.", "Uống nước thường xuyên để tránh sốc nhiệt.", "熱中症", "netchūshō"),
  ("incident report", "/ˈɪnsɪdənt rɪˌpɔːt/", "n", "báo cáo sự cố", "Please write an <b>incident report</b> within 24 hours.", "Vui lòng viết báo cáo sự cố trong vòng 24 giờ.", "事故報告書", "jiko hōkokusho"),
  ("evacuate", "/ɪˈvækjueɪt/", "v", "sơ tán", "<b>Evacuate</b> the building when you hear the alarm.", "Nghe chuông báo động thì sơ tán khỏi tòa nhà.", "避難する", "hinan suru"),
  ("secure", "/sɪˈkjʊə/", "v", "chằng buộc, cố định cho chắc", "<b>Secure</b> all loose materials on the roof before the storm.", "Chằng buộc hết vật tư rời trên mái trước khi bão tới."),
  ("flooded", "/ˈflʌdɪd/", "adj", "bị ngập nước", "The basement is <b>flooded</b> after last night's rain.", "Tầng hầm bị ngập sau trận mưa đêm qua."),
  ("dust", "/dʌst/", "n", "bụi", "Spray water on the road to reduce <b>dust</b>.", "Tưới nước lên đường để giảm bụi.", "粉じん", "funjin"),
  ("noise", "/nɔɪz/", "n", "tiếng ồn", "No loud <b>noise</b> after 10 p.m. — the neighbours are sleeping.", "Không gây ồn lớn sau 10 giờ tối — hàng xóm đang ngủ.", "騒音", "sōon"),
  ("complaint", "/kəmˈplaɪnt/", "n", "lời phàn nàn, khiếu nại", "We got a <b>complaint</b> about dust from a neighbour.", "Tụi mình nhận được phàn nàn về bụi từ một hộ dân gần đó.", "苦情", "kujō"),
 ],
 "phrases": [
  ("Heavy rain is coming. Let's cover the fresh concrete.", "Sắp mưa to. Che bê tông mới đổ lại nhé."),
  ("We stopped work for two hours because of the storm.", "Tụi mình phải dừng làm hai tiếng vì mưa bão."),
  ("Crane work is stopped until the wind drops.", "Tạm dừng cẩu cho đến khi gió giảm."),
  ("It's very hot today. Take a break in the shade every hour.", "Hôm nay rất nóng. Cứ mỗi tiếng nghỉ trong bóng mát một lần."),
  ("A worker feels dizzy. Please take him to the shade and give him water.", "Có công nhân bị chóng mặt. Đưa anh ấy vào chỗ mát và cho uống nước."),
  ("Don't move him. Call the first aider and an ambulance.", "Đừng di chuyển anh ấy. Gọi người sơ cứu và xe cấp cứu."),
  ("Please pump the water out of the basement.", "Bơm nước ra khỏi tầng hầm nhé."),
  ("I'll write the incident report today.", "Hôm nay tôi sẽ viết báo cáo sự cố."),
  ("Please wash the wheels of every truck before it leaves the site.", "Rửa bánh xe tải trước khi xe ra khỏi công trường."),
  ("Sorry for the noise. We'll finish by 5 p.m. today.", "Xin lỗi vì tiếng ồn. Hôm nay tụi tôi sẽ xong trước 5 giờ chiều."),
 ],
 "dialogues": [
  ("A typhoon is coming tomorrow. What's your plan?", [
    ("Today we'll secure all loose materials and check the scaffolding. Tomorrow there will be no crane work and no work at height.", True, "Kế hoạch cụ thể: chằng buộc, kiểm tra giàn giáo, dừng cẩu và việc trên cao."),
    ("We continue work, typhoon maybe not come.", False, "Chủ quan với bão và sai ngữ pháp ('it may not come')."),
    ("Typhoon is very dangerous.", False, "Đúng nhưng không trả lời câu hỏi 'kế hoạch là gì'."),
  ]),
  ("A worker says he feels dizzy and sick in the heat.", [
    ("Let's move him to the shade, cool him down and give him water. Someone will stay with him, and if he doesn't feel better soon or gets confused, we'll call an ambulance.", True, "Sơ cứu đúng: đưa vào chỗ mát, làm mát, cho uống nước khi còn tỉnh, có người ở cạnh theo dõi; không đỡ nhanh hoặc lơ mơ thì gọi cấp cứu ngay."),
    ("Tell him drink coffee and continue.", False, "Sai về sức khỏe và ngữ pháp ('to drink') — không để người có dấu hiệu sốc nhiệt làm tiếp."),
    ("He is weak, change another worker.", False, "Bỏ mặc người bị nạn — cần sơ cứu ngay."),
  ]),
  ("A worker fell from a ladder. He says his back hurts.", [
    ("Don't move him. I'll call the first aider and an ambulance now.", True, "Đúng nguyên tắc: nghi chấn thương lưng thì không tự di chuyển nạn nhân, gọi sơ cứu và cấp cứu."),
    ("Help him stand up and walk to the office.", False, "Nguy hiểm — di chuyển người nghi chấn thương cột sống có thể làm nặng thêm."),
    ("Why he not careful?", False, "Sai ngữ pháp ('Why wasn't he careful?') và trách móc lúc cần cấp cứu."),
  ]),
  ("A neighbour complained about the dust.", [
    ("I'm sorry about that. We'll spray water on the road twice a day and cover the sand piles.", True, "Xin lỗi + biện pháp cụ thể để giảm bụi."),
    ("Construction always have dust.", False, "Sai chia động từ ('has') và coi nhẹ phàn nàn của người dân."),
    ("Not our dust, other site.", False, "Chối bỏ khi chưa kiểm tra."),
  ]),
  ("Why was there no work on site yesterday afternoon?", [
    ("We had heavy rain from 1 to 5 p.m., so we stopped all outside work. I've recorded it in the daily report.", True, "Nguyên nhân + thời gian + đã ghi nhật ký (quan trọng khi xin gia hạn)."),
    ("Rain, cannot work.", False, "Câu cụt, thiếu chủ ngữ và thông tin thời gian."),
    ("Workers go home because they want.", False, "Sai thì ('went') và không nêu lý do hợp lý."),
  ]),
 ],
 "listen": [
  ("The forecast says heavy rain this afternoon", ["forecast", "rain"], "dự báo thời tiết"),
  ("Drink water often to prevent heatstroke", ["water", "heatstroke"], "phòng sốc nhiệt"),
  ("The basement is flooded after the rain", ["basement", "flooded"], "tầng hầm ngập"),
  ("We got a complaint about the noise", ["complaint", "noise"], "phàn nàn của hàng xóm"),
  ("A typhoon is coming tomorrow night. Please secure all loose materials on the roof. There will be no crane work tomorrow.", ["typhoon", "secure", "crane"], "chuẩn bị đón bão"),
  ("A worker fell from a ladder at ten this morning. He hurt his arm and went to the hospital. Please write the incident report today.", ["ladder", "hospital", "incident"], "báo sự cố"),
 ],
})

# ───────────────────────── 9. Bàn giao & danh sách việc tồn ─────────────────────────
PHASES.append({
 "title": "Bàn giao & danh sách việc tồn",
 "vocab": [
  ("handover", "/ˈhændəʊvə/", "n", "bàn giao", "The <b>handover</b> to the client is on December 15.", "Bàn giao cho chủ đầu tư vào ngày 15/12.", "引き渡し", "hikiwatashi"),
  ("punch list", "/ˈpʌntʃ ˌlɪst/", "n", "danh sách lỗi tồn cần sửa trước bàn giao", "There are 120 items on the <b>punch list</b>.", "Danh sách lỗi tồn có 120 mục."),
  ("as-built drawing", "/ˌæz ˌbɪlt ˈdrɔːɪŋ/", "n", "bản vẽ hoàn công", "Please send the <b>as-built drawings</b> before the handover.", "Vui lòng gửi bản vẽ hoàn công trước khi bàn giao.", "竣工図", "shunkōzu"),
  ("defect", "/ˈdiːfekt/", "n", "lỗi, khuyết tật (hoàn thiện)", "The client found a <b>defect</b> in the bathroom tiles.", "Chủ đầu tư phát hiện lỗi ở gạch nhà vệ sinh.", "不具合", "fuguai"),
  ("warranty", "/ˈwɒrənti/", "n", "bảo hành", "The roof has a ten-year <b>warranty</b>.", "Mái được bảo hành mười năm.", "保証", "hoshō"),
  ("O&M manual", "/ˌəʊ ən ˈem ˌmænjuəl/", "n", "tài liệu hướng dẫn vận hành và bảo trì", "The <b>O&M manual</b> explains how to maintain the pumps.", "Tài liệu vận hành và bảo trì hướng dẫn cách bảo dưỡng máy bơm."),
  ("final inspection", "/ˌfaɪnl ɪnˈspekʃn/", "n", "nghiệm thu hoàn thành", "The <b>final inspection</b> is next Tuesday.", "Nghiệm thu hoàn thành vào thứ Ba tuần sau.", "竣工検査", "shunkō kensa"),
  ("touch up", "/ˌtʌtʃ ˈʌp/", "phr v", "sửa lại chỗ nhỏ, sơn dặm", "Please <b>touch up</b> the paint on this door.", "Sơn dặm lại cánh cửa này nhé."),
  ("completion", "/kəmˈpliːʃn/", "n", "sự hoàn thành (công trình)", "<b>Completion</b> is planned for the end of the year.", "Dự kiến hoàn thành công trình vào cuối năm.", "竣工", "shunkō"),
  ("walkthrough", "/ˈwɔːkθruː/", "n", "buổi đi kiểm tra một vòng (cùng chủ đầu tư, tư vấn)", "Let's do a <b>walkthrough</b> of Level 2 with the client.", "Mình đi kiểm tra một vòng tầng 2 cùng chủ đầu tư nhé."),
 ],
 "phrases": [
  ("We've fixed 90 of the 120 punch list items.", "Tụi tôi đã sửa xong 90 trên 120 mục tồn."),
  ("The remaining items will be done by Friday.", "Các mục còn lại sẽ xong trước thứ Sáu."),
  ("Could you walk through Level 3 with us tomorrow?", "Mai anh đi kiểm tra tầng 3 cùng tụi tôi được không?"),
  ("We'll touch up the paint before the handover.", "Tụi tôi sẽ sơn dặm trước khi bàn giao."),
  ("Here are the as-built drawings and the O&M manuals.", "Đây là bản vẽ hoàn công và tài liệu vận hành, bảo trì."),
  ("The warranty starts from the handover date.", "Bảo hành tính từ ngày bàn giao."),
  ("We'll train your staff to use the fire alarm system.", "Tụi tôi sẽ hướng dẫn nhân viên bên anh cách dùng hệ thống báo cháy."),
  ("If you find any defects, please let us know.", "Nếu phát hiện lỗi gì, anh báo tụi tôi nhé."),
  ("Thank you for your support on this project.", "Cảm ơn anh đã hỗ trợ trong suốt dự án."),
 ],
 "dialogues": [
  ("How many punch list items are still open?", [
    ("Thirty out of 120. Most of them are paint touch-ups, and we'll finish them by Friday.", True, "Con số + loại việc chính + hạn hoàn thành."),
    ("Still have many.", False, "Thiếu chủ ngữ và con số: 'There are still 30 items.'"),
    ("Almost finish, don't worry.", False, "Sai dạng từ ('almost finished') và mơ hồ."),
  ]),
  ("This door doesn't close properly.", [
    ("Thanks for pointing it out. I'll add it to the punch list, and our carpenter will fix it tomorrow.", True, "Cảm ơn + ghi vào danh sách + người sửa + thời gian."),
    ("It's OK, just push harder.", False, "Bắt khách tự xoay xở — không chấp nhận được với lỗi hoàn thiện."),
    ("Door is not our scope maybe.", False, "Né tránh khi chưa kiểm tra phạm vi, thiếu mạo từ."),
  ]),
  ("When will we get the as-built drawings?", [
    ("We'll send them one week before the handover, both as PDF files and in print.", True, "Thời điểm + hình thức giao."),
    ("After handover, when we free.", False, "Thiếu động từ ('when we're free') và nghe như không coi trọng."),
    ("As-built is same as design drawing.", False, "Sai — bản vẽ hoàn công thể hiện thực tế đã thi công, có thể khác thiết kế."),
  ]),
  ("A pipe is leaking under the sink. You handed over the building only a month ago.", [
    ("I'm sorry about that. It's under warranty, so we'll send a plumber today to fix it.", True, "Xin lỗi + xác nhận còn bảo hành + hành động ngay."),
    ("You use it wrong, not our problem.", False, "Đổ lỗi cho khách khi chưa kiểm tra."),
    ("Warranty is finish.", False, "Sai thông tin (mới một tháng) và sai ngữ pháp."),
  ]),
  ("Is the building ready for the final inspection?", [
    ("Almost. All systems passed commissioning. We just need to finish the final cleaning on Level 1 by Monday.", True, "Tình trạng + việc còn lại + hạn."),
    ("Ready 100 percent, sure.", False, "Hứa chắc mà không nói rõ căn cứ."),
    ("Final inspection is next week, right?", False, "Hỏi lại thay vì trả lời câu hỏi."),
  ]),
 ],
 "listen": [
  ("There are thirty items left on the punch list", ["thirty", "punch"], "việc tồn còn lại"),
  ("The handover to the client is next Friday", ["handover", "Friday"], "lịch bàn giao"),
  ("Please touch up the paint on this door", ["paint", "door"], "sơn dặm"),
  ("The warranty starts from the handover date", ["warranty", "date"], "bảo hành"),
  ("Tomorrow we will do a walkthrough with the client. Please clean Level two and remove all tools. We start at nine in the lobby.", ["walkthrough", "clean", "lobby"], "chuẩn bị đi kiểm tra cùng khách"),
  ("The final inspection passed today. We will hand over the keys and the manuals on Monday. Thank you, everyone, for your hard work.", ["passed", "keys", "manuals"], "thông báo nghiệm thu đạt"),
 ],
})

# ───────────────────────── Vai trong ngành ─────────────────────────
ROLES = {
 "site": {"label": "Kỹ sư hiện trường · Điều phối", "emoji": "👷",
  "scenarios": [
   ("st_pm", "Báo tiến độ cho PM nước ngoài", "You are a foreign project manager. I am the site engineer. Ask about today's progress, the number of workers and any delays, and ask how we will catch up."),
   ("st_sub", "Nhắc nhà thầu phụ", "You are the foreman of a subcontractor. Your team is behind schedule and your area is messy. I am the site engineer from the main contractor. Give excuses at first, then agree to a plan."),
   ("st_rfi", "Hỏi tư vấn về bản vẽ", "You are the design consultant. I call about a clash between a duct and a beam. Ask for the grid line, photos and my suggestion, then promise a date for your answer."),
   ("st_client", "Đón chủ đầu tư thăm công trường", "You are a Japanese client representative visiting the site. Speak simple English. Ask about progress, safety and quality, and ask one difficult question about the schedule."),
  ],
  "dialogues": [
   ("Where are we with the fifth floor?", [
     ("The columns are done, and the slab formwork is 60 percent finished. We plan to pour on Saturday.", True, "Hạng mục + tiến độ + mốc tiếp theo."),
     ("Fifth floor is doing.", False, "Sai cấu trúc ('Work on the fifth floor is in progress') và không có số liệu."),
     ("Very busy, many work.", False, "Than bận, sai ngữ pháp ('a lot of work') và không trả lời.")]),
   ("Your subcontractor's area is very messy.", [
     ("Sorry about that. I'll talk to their foreman now, and they'll clean it before lunch.", True, "Nhận trách nhiệm quản lý + hành động + hạn."),
     ("Not my people, it's the subcontractor.", False, "Đùn đẩy — nhà thầu chính chịu trách nhiệm cả công trường."),
     ("Construction site always dirty.", False, "Thiếu động từ ('is always dirty') và coi nhẹ vệ sinh công trường.")]),
   ("Can we pour the slab on Saturday?", [
     ("Yes, if the rebar inspection passes on Friday. I've booked the concrete and the pump for 6 a.m.", True, "Nêu điều kiện (điểm dừng nghiệm thu) + đã chuẩn bị."),
     ("Yes, pour first, inspect after.", False, "Sai quy trình — phải nghiệm thu cốt thép trước khi đổ."),
     ("Saturday maybe rain, I don't know.", False, "Mơ hồ, sai ngữ pháp ('it may rain') và không có kế hoạch.")]),
   ("The client wants to know why we're behind.", [
     ("We lost three days to rain and one day to a late steel delivery. With Sunday work, we'll catch up by the 20th.", True, "Nguyên nhân có số liệu + kế hoạch bù + mốc."),
     ("Tell client weather is bad.", False, "Thiếu mạo từ và quá sơ sài để báo chủ đầu tư."),
     ("We are not behind, we are only late.", False, "Tự mâu thuẫn, né tránh.")]),
   ("Did you check the method statement for the excavation?", [
     ("Yes. I checked it with the HSE officer, and we added a barrier around the edge.", True, "Xác nhận + phối hợp an toàn + điều chỉnh cụ thể."),
     ("Yes, I check it tomorrow.", False, "Tự mâu thuẫn: 'Yes' (đã kiểm) nhưng lại 'tomorrow'; sai thì."),
     ("Method is same last project.", False, "Thiếu 'the … as' và không kiểm tra theo điều kiện thực tế.")]),
   ("I need the daily report by 6 p.m.", [
     ("No problem. I'll send it by 5:30 with photos of today's work.", True, "Đồng ý + giờ gửi + nội dung kèm theo."),
     ("OK, I send.", False, "Thiếu 'will' và 'it': 'OK, I'll send it.'"),
     ("Today too busy, tomorrow.", False, "Thiếu chủ ngữ/động từ và trễ hạn không lý do.")]),
  ]},
 "qaqc": {"label": "QA / QC", "emoji": "🔍",
  "scenarios": [
   ("qc_ir", "Mời tư vấn nghiệm thu", "You are the consultant's inspector. I call to ask you to inspect the rebar for a slab. Ask what is ready, whether we checked it ourselves and what time."),
   ("qc_ncr", "Nhận phiếu NCR", "You are the client's foreign QA manager. You issue an NCR for poor concrete (honeycombing) in a column. Ask for the cause, the repair method and the date."),
   ("qc_material", "Kiểm tra vật tư đầu vào", "You are a supplier's delivery driver. Some tiles in your truck are broken and the quantity is short. I am QC and I check the delivery. Try to make me sign quickly."),
   ("qc_test", "Báo kết quả thí nghiệm", "You are the project manager. The 7-day concrete cube result is lower than you expected. Ask me what it means and what we will do next."),
  ],
  "dialogues": [
   ("Are the tiles you received OK?", [
     ("Most are fine, but 15 boxes have broken tiles. I've taken photos and written it on the delivery note.", True, "Kết quả + số lượng lỗi + bằng chứng + ghi lên phiếu."),
     ("Tiles is OK I think.", False, "Sai chia động từ ('are') và nghe như chưa kiểm tra kỹ."),
     ("Supplier always bad quality.", False, "Nói chung chung, thiếu động từ, không có số liệu cụ thể.")]),
   ("The 7-day cube strength is a bit low. Should we worry?", [
     ("Not yet. It's 68 percent of the design strength, which is normal at 7 days. We'll check the 28-day result.", True, "Giải thích bằng số liệu + bước theo dõi tiếp (ở 7 ngày bê tông thường đạt khoảng 65–70% cường độ)."),
     ("Yes, break the slab now.", False, "Kết luận vội — cần chờ kết quả 28 ngày và đánh giá kỹ."),
     ("Low a little, no problem forever.", False, "Sai ngữ pháp và xem nhẹ — vẫn phải theo dõi kết quả 28 ngày.")]),
   ("Why did you reject this concrete truck?", [
     ("The slump was 20 centimetres, but the spec allows 12 plus or minus 2. I have the test record here.", True, "Căn cứ bằng số đo và tiêu chuẩn, có hồ sơ."),
     ("Because I don't like it.", False, "Cảm tính — QC phải dựa vào số liệu."),
     ("The concrete look not good.", False, "Thiếu 's' ('doesn't look good') và không có số liệu.")]),
   ("Who will witness the pressure test?", [
     ("The consultant's MEP engineer. The test is at 9 a.m. tomorrow, and I'll prepare the form.", True, "Người cụ thể + giờ + chuẩn bị biên bản."),
     ("Somebody from consultant, maybe.", False, "Mơ hồ, thiếu mạo từ — phải xác nhận trước người chứng kiến."),
     ("No need witness, we test ourselves.", False, "Sai quy trình — thử áp phải có tư vấn chứng kiến và ký.")]),
   ("Can you send me the inspection records for Level 4?", [
     ("Sure. I'll email you the signed checklists and photos this afternoon.", True, "Đồng ý + nội dung + thời gian."),
     ("Records is in the file.", False, "Sai chia động từ ('are') và không trả lời có gửi không."),
     ("Why you need?", False, "Sai cấu trúc câu hỏi ('Why do you need them?') và thiếu hợp tác.")]),
   ("The plaster on this wall isn't flat.", [
     ("You're right. We measured it, and it's out of tolerance. We'll rework it and ask you to check again on Friday.", True, "Xác nhận bằng đo đạc + làm lại + hẹn kiểm tra lại."),
     ("After paint, nobody can see.", False, "Che lấp lỗi — sơn không làm tường phẳng hơn."),
     ("The worker is new, sorry.", False, "Chỉ xin lỗi, đổ cho công nhân, không có cách khắc phục.")]),
  ]},
 "hse": {"label": "An toàn · HSE", "emoji": "🦺",
  "scenarios": [
   ("hs_induction", "Hướng dẫn an toàn cho người mới", "You are a new foreign engineer on your first day at the site. I am the HSE officer giving you a site induction. Ask about PPE, working at height and what to do in an emergency."),
   ("hs_stop", "Dừng công việc không an toàn", "You are a subcontractor foreman. Your worker is at a roof edge without a harness, and I stop the work. Argue that the job is quick, then agree to follow the rule."),
   ("hs_incident", "Báo cáo sự cố cho sếp", "You are a foreign project director. A worker was hurt this morning. Ask what happened, how he is, what the cause was and how we will stop it from happening again."),
   ("hs_audit", "Tiếp đoàn kiểm tra an toàn", "You are a safety auditor from the client. Walk the site with me. Ask about scaffolding checks, permits and training records, and point out one problem politely."),
  ],
  "dialogues": [
   ("Why did you stop my team?", [
     ("Two of your workers were on the scaffolding without harnesses. They can continue when they're clipped on.", True, "Nêu lý do cụ thể + điều kiện để làm tiếp."),
     ("Because I am safety officer, I can.", False, "Dùng quyền thay vì giải thích lý do, thiếu mạo từ ('the safety officer')."),
     ("Your team always no safety.", False, "Công kích chung chung, sai ngữ pháp.")]),
   ("What PPE do I need on this site?", [
     ("A hard hat, safety boots, a safety vest and safety glasses. Above two metres, you also need a harness.", True, "Liệt kê đủ + yêu cầu riêng khi làm trên cao."),
     ("Only hard hat is enough.", False, "Sai — thiếu nhiều đồ bảo hộ bắt buộc."),
     ("PPE is many things.", False, "Không trả lời cụ thể.")]),
   ("How is the injured worker?", [
     ("He has a cut on his hand. He got first aid and went to the clinic. He'll be back tomorrow.", True, "Tình trạng + đã xử lý gì + dự kiến."),
     ("He is OK, small small.", False, "Lặp từ kiểu tiếng Việt ('nhỏ nhỏ'), thiếu thông tin."),
     ("He is careless, so he hurt.", False, "Trách người bị nạn, sai ngữ pháp ('he got hurt').")]),
   ("What was the cause of the accident?", [
     ("A board on the scaffolding was loose, and the daily check missed it. We've fixed it and retrained the checkers.", True, "Nguyên nhân kỹ thuật + lỗ hổng quy trình + hành động khắc phục."),
     ("Bad luck.", False, "Không phải nguyên nhân — cần phân tích để phòng ngừa."),
     ("The worker fault only.", False, "Thiếu động từ và dừng ở lỗi con người, không tìm nguyên nhân hệ thống.")]),
   ("Can we skip the toolbox talk today? We're very busy.", [
     ("I understand, but it only takes ten minutes, and today we have crane work. Let's keep it short and clear.", True, "Thông cảm nhưng giữ nguyên tắc + lý do + cách dung hòa."),
     ("OK, skip it, no problem.", False, "Bỏ buổi nhắc an toàn vì bận — đúng lúc dễ xảy ra tai nạn."),
     ("You busy is not my problem.", False, "Sai ngữ pháp và thái độ đối đầu.")]),
   ("Is this scaffolding safe to use?", [
     ("Yes. It was inspected this morning and has a green tag. The next check is tomorrow.", True, "Căn cứ (đã kiểm tra, có thẻ xanh) + lịch kiểm tra tiếp."),
     ("Looks strong, I think safe.", False, "Đánh giá bằng mắt, thiếu chủ ngữ — phải dựa vào kiểm tra và thẻ."),
     ("Everyone uses it, so it is safe.", False, "Suy luận sai — nhiều người dùng không có nghĩa là an toàn.")]),
  ]},
 "mep": {"label": "Kỹ thuật MEP", "emoji": "⚡",
  "scenarios": [
   ("mp_clash", "Họp phối hợp MEP", "You are a foreign MEP coordinator. In a coordination meeting, ask me about a clash between my pipes and the air-con ducts, and agree on who will move."),
   ("mp_test", "Mời chứng kiến thử áp", "You are the consultant's MEP engineer. I invite you to witness a pressure test. Ask about the test pressure, the time and the area."),
   ("mp_ceiling", "Thương lượng với đội trần", "You are the ceiling subcontractor's foreman. You want to close the ceiling today, but my wiring is not finished. Push me, then agree on a new date."),
   ("mp_handover", "Hướng dẫn vận hành cho khách", "You are the client's building manager. I train you on the air-con system before handover. Ask how to turn it on, how often to clean the filters and who to call for problems."),
  ],
  "dialogues": [
   ("Your pipes clash with our ducts on Level 3.", [
     ("Let's check the drawings together. Our pipes are smaller, so we can move them down 150 millimetres if the ceiling height allows it.", True, "Phối hợp + đề xuất cụ thể + điều kiện."),
     ("Your ducts move, not my pipes.", False, "Sai cấu trúc ('You should move your ducts') và thái độ không hợp tác."),
     ("I don't know, ask designer.", False, "Đùn đẩy, thiếu mạo từ ('the designer').")]),
   ("Is the power off in this area?", [
     ("Yes. I isolated it at the main board and locked it. I also tested the cables — they're dead.", True, "Xác nhận + đã cắt, khóa, đo kiểm tra — đủ quy trình."),
     ("I think yes.", False, "Không chắc chắn về điện là nguy hiểm."),
     ("Power off already long time.", False, "Sai ngữ pháp và không có căn cứ kiểm tra.")]),
   ("What's the test pressure for these pipes?", [
     ("Ten bar for two hours, as the specification says. The consultant will witness it.", True, "Thông số + căn cứ + người chứng kiến."),
     ("High pressure, very strong.", False, "Mơ hồ, không có con số."),
     ("Pressure is ten.", False, "Thiếu đơn vị ('bar') và thời gian thử.")]),
   ("The fire alarm isn't working on Level 2.", [
     ("I'll check the panel and the wiring now and tell you what's wrong within an hour.", True, "Hành động ngay + hạn báo lại."),
     ("Maybe broken, wait for supplier.", False, "Bị động, thiếu chủ ngữ — hệ thống báo cháy không được để chờ."),
     ("Fire alarm not important now.", False, "Sai nghiêm trọng về an toàn và thiếu động từ.")]),
   ("How often should we clean the air-con filters?", [
     ("About once a month, or more often in a dusty area. Dirty filters make the system work harder and use more power.", True, "Tần suất thường gặp + lý do dễ hiểu (lịch thật theo tài liệu O&M của nhà sản xuất)."),
     ("When dirty.", False, "Câu cụt, không có tần suất cụ thể."),
     ("No need clean, it's new.", False, "Sai ngữ pháp và sai kỹ thuật — máy mới cũng phải vệ sinh lọc định kỳ.")]),
   ("Can we close the ceiling in Room 205?", [
     ("Yes. The wiring and the piping passed inspection yesterday, so you can close it now.", True, "Cho phép + căn cứ đã nghiệm thu."),
     ("Yes, close, maybe OK.", False, "Thiếu chắc chắn, không nêu căn cứ."),
     ("Room 205 is finish?", False, "Hỏi ngược lại, sai ngữ pháp ('finished').")]),
  ]},
}

PACK = {
 "id": "construction",
 "label": "Xây dựng · Kỹ thuật",
 "short": "Xây dựng",
 "emoji": "🏗️",
 "desc": "Kỹ sư hiện trường · QA/QC · an toàn · MEP",
 "persona": "a Vietnamese construction and engineering worker",
 "counterpart": "a foreign project manager or consultant",
 "context": "construction and engineering",
 "core": [3, 11],
 "report": {
  "title": "Báo cáo công trường 60 giây", "short": "Báo cáo công trường", "sub": "Nói như họp giao ban cuối ngày 🎙️",
  "steps": [["Progress", "Today we poured the Level 7 slab …"], ["Issues", "The rebar arrived four hours late … / No safety issues."], ["Tomorrow", "Tomorrow we will start …"]],
  "kind": "daily site report",
  "structure": "progress today / issues and safety / plan for tomorrow",
  "sample": "Today we poured the Level 7 slab, 68 cubic metres, and finished the walls on Level 5. The rebar for Level 8 arrived four hours late, but there were no safety issues. Tomorrow we will start the Level 8 columns and keep curing the slab.",
 },
 "podcast": "Podcast công trường",
 "game_tag": "Game anime: đánh quái công trường, hạ boss tư vấn khó tính",
 "reverse_tag": "kiểu công trường",
 "jd_placeholder": "VD: Kỹ sư hiện trường cho tổng thầu Nhật ở Bình Dương, báo cáo tiến độ, làm việc với tư vấn, nghiệm thu, an toàn lao động…",
 "rw_placeholder": "VD: xe thép giao trễ 4 tiếng, tầng 8 chưa dựng cột kịp",
 "quips": [
  "Hard hat on!",
  "Safety first, schedule second!",
  "Clip on up high!",
  "Pour day — let's go!",
  "Check the latest revision!",
  "Never under the load!",
  "Slump test: pass!",
  "Punch list almost empty!",
  "Keep the walkway clear!",
  "Drink water, beat the heat!",
 ],
 "ai": [
  ("pm_update", "Báo tiến độ cho PM", "You are a foreign project manager at a construction site. I am a Vietnamese site engineer. Ask about today's progress, delays and the plan for tomorrow. Speak simple English."),
  ("toolbox", "Nói buổi nhắc an toàn", "You are a foreign HSE manager listening to my morning toolbox talk. After I speak, ask one question about today's hazards and one about PPE."),
  ("violation", "Nhắc vi phạm an toàn", "You are a subcontractor worker working at height without a harness. I am the safety officer. Give an excuse at first, then agree to wear it and clip on."),
  ("delivery", "Vật tư giao trễ", "You are a salesperson at a steel supplier. Your rebar delivery is one day late. I call to ask why and when it will arrive. Apologize and give a new time."),
  ("rfi", "Làm rõ bản vẽ với tư vấn", "You are the design consultant. I found that the architectural and structural drawings do not match. Ask me for details and tell me what to do next."),
  ("ncr", "Nhận phiếu NCR", "You are the client's quality engineer. You found a crack in a new wall and issue an NCR. Ask about the cause, the repair method and the date."),
  ("client_visit", "Chủ đầu tư thăm công trường", "You are a Japanese client representative visiting the site. Ask about progress, safety and quality, and ask one question about the handover date."),
  ("handover", "Đi kiểm tra trước bàn giao", "You are the client's building manager on a walkthrough before handover. Point out two defects and ask when they will be fixed and what documents you will get."),
 ],
 "rev": [
  ("Chúng ta đang chậm hai ngày so với tiến độ.", "We're two days behind schedule."),
  ("Vui lòng đội mũ bảo hộ.", "Please wear your hard hat."),
  ("Làm việc trên cao phải đeo dây an toàn.", "You must wear a harness when you work at height."),
  ("Không được đứng dưới vật đang cẩu.", "Don't stand under a suspended load."),
  ("Sáng mai 6 giờ đổ bê tông sàn.", "We'll pour the slab at 6 a.m. tomorrow."),
  ("Bản vẽ này cũ rồi.", "This drawing is out of date."),
  ("Tôi sẽ gửi RFI cho tư vấn.", "I'll send an RFI to the consultant."),
  ("Xe thép giao trễ ba tiếng.", "The rebar truck is three hours late."),
  ("Số lượng không khớp với phiếu giao hàng.", "The quantity doesn't match the delivery note."),
  ("Không được thêm nước vào bê tông.", "Don't add water to the concrete."),
  ("Cột tầng sáu đã sẵn sàng nghiệm thu.", "The sixth-floor columns are ready for inspection."),
  ("Ngắt điện trước khi mở tủ.", "Isolate the power before you open the board."),
  ("Sắp có bão, chằng buộc vật tư lại.", "A typhoon is coming. Secure the materials."),
  ("Còn 30 mục tồn trước khi bàn giao.", "We have 30 punch list items left before handover."),
 ],
 "reading": [
  {"t": "Daily site report", "text": "DAILY SITE REPORT – Tower B, 14 May\nWeather: sunny, 35°C\nWorkers on site: 86\nDone: Level 7 slab poured (68 m³)\nIssue: Rebar for the Level 8 columns arrived 4 hours late.\nTomorrow: start Level 8 columns. Continue curing the Level 7 slab.", "q": [
    {"q": "How much concrete was poured today?", "o": ["86 m³", "68 m³", "35 m³"], "a": 1},
    {"q": "What was the problem today?", "o": ["The rebar arrived late", "It rained all day", "A worker was injured"], "a": 0}]},
  {"t": "Safety notice", "text": "SAFETY NOTICE\nFrom Monday, a full-body harness is required for all work above 2 metres. Always clip on to an anchor point. Do not use any scaffolding without a green tag. Report any unsafe condition to the HSE office (ext. 105).", "q": [
    {"q": "When do workers need a harness?", "o": ["Only on the roof", "For all work above 2 metres", "Only when welding"], "a": 1},
    {"q": "What must scaffolding have before you use it?", "o": ["A red tag", "A new ladder", "A green tag"], "a": 2}]},
  {"t": "RFI", "text": "RFI No. 045\nTo: Design Consultant\nSubject: Duct and beam clash – Level 5, grid line C/4\nThe 600 mm air duct clashes with beam B12. We propose lowering the duct by 150 mm. The ceiling height will then be 2,700 mm. Please reply by 20 June. Ceiling work in this area is on hold until then.", "q": [
    {"q": "What is the problem?", "o": ["A duct hits a beam", "A pipe is leaking", "A beam is cracked"], "a": 0},
    {"q": "What happens until the consultant replies?", "o": ["The duct is removed", "Ceiling work in this area stops", "The beam is cut"], "a": 1}]},
  {"t": "Email from QA manager", "text": "Dear Mr. Khoa,\nDuring today's inspection, we found that the concrete cover to the Level 6 column rebar is only 10–15 mm. The specification requires 40 mm. Please do not pour these columns. Correct the cover and send a new inspection request.\nBest regards,\nS. Tanaka, QA Manager", "q": [
    {"q": "What is wrong?", "o": ["The formwork is broken", "The concrete is too weak", "The concrete cover is too thin"], "a": 2},
    {"q": "What must the contractor do next?", "o": ["Fix the cover and ask for a new inspection", "Pour the columns today", "Change the specification"], "a": 0}]},
  {"t": "Typhoon warning", "text": "TYPHOON WARNING\nA typhoon is expected on Thursday night. All crane work will stop from 12:00 on Thursday. Before 17:00 on Thursday, secure all loose materials and cover all open holes. The site will be closed on Friday. Check the site group chat for updates.", "q": [
    {"q": "When will crane work stop?", "o": ["Thursday at 12:00", "Thursday at 17:00", "Friday morning"], "a": 0},
    {"q": "What will happen on Friday?", "o": ["Work will start early", "The site will be closed", "The cranes will lift materials"], "a": 1}]},
 ],
 "events": [
  ("client_visit", "Chủ đầu tư thăm công trường", "You are the client's representative visiting our site next week. Ask about progress, safety, quality and any risks to the handover date."),
  ("inspection", "Buổi nghiệm thu quan trọng", "You are the consultant's inspector coming for an important inspection tomorrow. Ask what is ready and what we checked, and tell me what documents you need."),
  ("safety_audit", "Đoàn kiểm tra an toàn", "You are a safety auditor from head office visiting next week. Ask about our toolbox talks, working at height, permits and incident records."),
  ("coordination", "Họp phối hợp nhà thầu", "You are the project manager leading a coordination meeting with subcontractors. Ask about my team's progress, any clashes and what I need from other teams."),
  ("handover", "Bàn giao công trình", "You are the client's building manager. The handover is next month. Ask about the punch list, the as-built drawings, training and the warranty."),
  ("interview", "Phỏng vấn vị trí kỹ sư", "You are a project manager at a foreign construction company interviewing me for a site engineer job. Ask about my projects, a site problem I solved and how I keep the site safe."),
  ("other", "Khác", ""),
 ],
 "roles": ROLES,
 "phases": PHASES,
}
