# -*- coding: utf-8 -*-
# v4.1 — nội dung làm giàu cho gói construction (nối vào cuối gói, xem build.py)
# 8 chặng mới: khảo sát & mặt bằng · đào đất & móng · hoàn thiện · hợp đồng & thanh toán ·
# nhà thầu phụ & điều phối · máy thi công · họp chủ đầu tư/tư vấn · phòng cháy & sơ cứu.
# Tên người là tên tự đặt.

PHASES = []

# ───────────────────────── A. Khảo sát, đo đạc & mặt bằng ─────────────────────────
PHASES.append({
 "title": "Khảo sát, đo đạc & mặt bằng",
 "vocab": [
  ("survey", "/ˈsɜːveɪ/", "n/v", "sự khảo sát, đo đạc; khảo sát, đo đạc", "The <b>survey</b> team will check the ground levels this morning.", "Sáng nay đội trắc đạc sẽ kiểm tra cao độ mặt đất.", "測量", "sokuryō"),
  ("surveyor", "/səˈveɪə/", "n", "kỹ sư / nhân viên trắc đạc", "Ask the <b>surveyor</b> to mark the column positions.", "Nhờ bên trắc đạc đánh dấu vị trí cột."),
  ("total station", "/ˌtəʊtl ˈsteɪʃn/", "n", "máy toàn đạc", "We use a <b>total station</b> to set out the grid lines.", "Tụi mình dùng máy toàn đạc để định vị các trục.", "トータルステーション", "tōtaru sutēshon"),
  ("setting out", "/ˌsetɪŋ ˈaʊt/", "n", "công tác định vị (tim, trục, vị trí) ra thực địa", "Please check the <b>setting out</b> before the excavator starts.", "Kiểm tra lại công tác định vị trước khi máy đào bắt đầu nhé.", "墨出し", "sumidashi"),
  ("benchmark", "/ˈbentʃmɑːk/", "n", "mốc cao độ chuẩn", "All levels on this site come from the <b>benchmark</b> near the gate.", "Mọi cao độ ở công trường này đều dẫn từ mốc chuẩn gần cổng.", "ベンチマーク", "benchimāku"),
  ("coordinates", "/kəʊˈɔːdɪnəts/", "n", "tọa độ", "The <b>coordinates</b> of this corner don't match the site plan.", "Tọa độ góc này không khớp với mặt bằng tổng thể.", "座標", "zahyō"),
  ("elevation", "/ˌelɪˈveɪʃn/", "n", "cao độ (so với mốc chuẩn)", "The finished floor <b>elevation</b> is plus 0.45 metres.", "Cao độ hoàn thiện sàn là +0,45 mét."),
  ("site boundary", "/ˌsaɪt ˈbaʊndri/", "n", "ranh giới khu đất", "The fence must stay inside the <b>site boundary</b>.", "Hàng rào phải nằm trong ranh giới khu đất.", "敷地境界", "shikichi kyōkai"),
  ("site layout", "/ˌsaɪt ˈleɪaʊt/", "n", "bố trí mặt bằng công trường (lán trại, bãi vật tư, đường tạm)", "The <b>site layout</b> shows where the crane and the storage areas go.", "Bản bố trí mặt bằng thể hiện chỗ đặt cẩu và các bãi vật tư."),
  ("hoarding", "/ˈhɔːdɪŋ/", "n", "hàng rào tôn bao quanh công trường", "Part of the <b>hoarding</b> fell down in the wind last night.", "Tối qua gió làm đổ một đoạn hàng rào tôn.", "仮囲い", "karigakoi"),
 ],
 "phrases": [
  ("The surveyor will set out the grid lines tomorrow morning.", "Sáng mai bên trắc đạc sẽ định vị các trục."),
  ("Please don't move the survey pegs.", "Đừng làm xê dịch cọc mốc trắc đạc nhé."),
  ("All levels come from the benchmark near the main gate.", "Mọi cao độ đều dẫn từ mốc chuẩn gần cổng chính."),
  ("Can you check the level of this slab again?", "Anh đo lại cao độ sàn này giúp tôi được không?"),
  ("This column is 20 millimetres off the grid line.", "Cột này lệch trục 20 mi-li-mét."),
  ("The fence is outside the site boundary.", "Hàng rào đang nằm ngoài ranh giới khu đất."),
  ("Where should we put the site office?", "Mình đặt văn phòng công trường ở đâu?"),
  ("We need a temporary road for the concrete trucks.", "Cần một con đường tạm cho xe bê tông."),
  ("Please send me the survey results by email.", "Gửi kết quả đo cho tôi qua email nhé."),
  ("Let's check the existing ground before we start.", "Mình kiểm tra hiện trạng mặt bằng trước khi làm nhé."),
 ],
 "dialogues": [
  ("The column at grid B2 is 30 millimetres off. Who set it out?", [
    ("Our surveyor did. I'll ask him to check it again with the total station this morning.", True, "Trả lời thẳng + hành động kiểm tra lại cụ thể."),
    ("30 millimetres is small, nobody see.", False, "Sai động từ ('nobody will see it') và xem nhẹ sai lệch — phải so với dung sai cho phép."),
    ("Not me set out.", False, "Sai cấu trúc ('I didn't set it out') và chỉ lo chối, không xử lý."),
  ]),
  ("Where do the levels on this site come from?", [
    ("From the benchmark next to the main gate. Its level is plus 5.20 metres.", True, "Nêu đúng mốc chuẩn + giá trị cao độ."),
    ("From the drawing, I think.", False, "Sai — cao độ ngoài thực địa phải dẫn từ mốc chuẩn, không phải 'từ bản vẽ'."),
    ("Levels come from surveyor.", False, "Thiếu mạo từ ('the surveyor') và không nói là mốc nào."),
  ]),
  ("Can we put the site office near the gate?", [
    ("Yes, but it must stay outside the crane's lifting area. I'll mark the spot on the site layout.", True, "Đồng ý có điều kiện an toàn (ngoài vùng cẩu) + cập nhật bản bố trí mặt bằng."),
    ("Anywhere is OK, you choose.", False, "Trả lời cho qua — vị trí lán trại phải theo bố trí mặt bằng và vùng an toàn của cẩu."),
    ("Office near gate is good, because near.", False, "Thiếu mạo từ, lý do vòng vo ('because near') — không có căn cứ."),
  ]),
  ("I think our fence is on the neighbour's land.", [
    ("Let's stop and ask the surveyor to check the site boundary before we build the rest of the fence.", True, "Dừng lại + đo kiểm tra ranh giới trước khi làm tiếp."),
    ("Neighbour not complain, so it's fine.", False, "Thiếu trợ động từ ('hasn't complained') và chủ quan — lấn ranh dễ gây tranh chấp."),
    ("We moved it already yesterday maybe.", False, "Mơ hồ, sai trật tự — không giải quyết đúng vấn đề."),
  ]),
  ("When will the survey results be ready?", [
    ("The surveyor will finish on site today, so I'll send you the report tomorrow afternoon.", True, "Mốc thời gian rõ + lý do."),
    ("Result ready soon soon.", False, "Lặp từ kiểu tiếng Việt ('sắp sắp'), thiếu động từ ('will be ready')."),
    ("Yesterday he measure already.", False, "Sai thì ('measured') và không trả lời khi nào có kết quả."),
  ]),
 ],
 "listen": [
  ("The surveyor will set out the grid lines tomorrow", ["surveyor", "grid"], "định vị trục"),
  ("All levels come from the benchmark near the gate", ["levels", "benchmark"], "mốc cao độ"),
  ("This column is twenty millimetres off the grid line", ["column", "twenty"], "cột lệch trục"),
  ("Please do not move the survey pegs", ["move", "pegs"], "giữ cọc mốc"),
  ("Good morning. The survey team will check the site boundary today. Please do not park trucks near the fence until they finish.", ["boundary", "park", "fence"], "thông báo đo ranh giới"),
  ("We checked the slab levels this morning. Two corners are fifteen millimetres too high. The surveyor will mark them in red.", ["levels", "corners", "red"], "báo kết quả đo cao độ"),
 ],
})

# ───────────────────────── B. Đào đất & móng ─────────────────────────
PHASES.append({
 "title": "Đào đất & móng",
 "vocab": [
  ("excavation", "/ˌekskəˈveɪʃn/", "n", "công tác đào đất; hố đào", "Put a barrier around the <b>excavation</b> before the end of the day.", "Làm rào chắn quanh hố đào trước khi hết ngày.", "掘削", "kussaku"),
  ("borehole", "/ˈbɔːhəʊl/", "n", "hố khoan khảo sát địa chất", "The soil report is based on six <b>boreholes</b>.", "Báo cáo địa chất dựa trên sáu hố khoan.", "ボーリング", "bōringu"),
  ("groundwater", "/ˈɡraʊndwɔːtə/", "n", "nước ngầm", "We hit <b>groundwater</b> at three metres, so we need a pump.", "Đào tới ba mét thì gặp nước ngầm nên phải có máy bơm.", "地下水", "chikasui"),
  ("shoring", "/ˈʃɔːrɪŋ/", "n", "hệ chống đỡ vách hố đào (cừ, thanh chống)", "The <b>shoring</b> must be installed before we dig deeper.", "Phải lắp hệ chống vách trước khi đào sâu thêm.", "山留め", "yamadome"),
  ("pile", "/paɪl/", "n", "cọc (móng)", "Two <b>piles</b> failed the load test.", "Hai cọc không đạt thí nghiệm thử tải.", "杭", "kui"),
  ("pile cap", "/ˈpaɪl ˌkæp/", "n", "đài cọc (đài móng)", "We'll cut the pile heads before we build the <b>pile cap</b>.", "Tụi mình sẽ đập đầu cọc trước khi làm đài cọc."),
  ("footing", "/ˈfʊtɪŋ/", "n", "móng (móng đơn, móng băng)", "The <b>footing</b> for this column is two metres by two metres.", "Móng của cột này có kích thước hai mét nhân hai mét.", "フーチング", "fūchingu"),
  ("blinding", "/ˈblaɪndɪŋ/", "n", "lớp bê tông lót (móng)", "Pour the <b>blinding</b> first, then fix the rebar.", "Đổ bê tông lót trước, rồi mới lắp cốt thép.", "捨てコンクリート", "sute konkurīto"),
  ("backfill", "/ˈbækfɪl/", "v/n", "lấp đất (lại hố móng); đất lấp", "Don't <b>backfill</b> until the consultant inspects the waterproofing.", "Tư vấn chưa nghiệm thu chống thấm thì chưa được lấp đất.", "埋め戻し", "umemodoshi"),
  ("compaction", "/kəmˈpækʃn/", "n", "sự đầm nén (đất)", "Place the soil in 300-millimetre layers and check the <b>compaction</b>.", "Đổ đất theo từng lớp 300 mi-li-mét và kiểm tra độ chặt.", "締固め", "shimekatame"),
 ],
 "phrases": [
  ("The excavation is four metres deep, so we need shoring.", "Hố đào sâu bốn mét nên phải có hệ chống vách."),
  ("Keep heavy trucks away from the edge of the excavation.", "Không cho xe tải nặng đi sát mép hố đào."),
  ("We found an old water pipe at 1.5 metres.", "Đào tới 1,5 mét thì gặp một đường ống nước cũ."),
  ("Please check for underground cables before you dig.", "Kiểm tra cáp ngầm trước khi đào nhé."),
  ("The pump runs all night to keep the pit dry.", "Máy bơm chạy suốt đêm để giữ hố móng khô."),
  ("Pile number 7 is 50 millimetres out of position.", "Cọc số 7 bị lệch vị trí 50 mi-li-mét."),
  ("The soil at the bottom is softer than the report says.", "Đất ở đáy hố yếu hơn so với báo cáo địa chất."),
  ("Could the geotechnical engineer check the bottom of the pit?", "Nhờ kỹ sư địa kỹ thuật kiểm tra đáy hố móng được không?"),
  ("We'll backfill in layers and test the compaction.", "Tụi tôi sẽ lấp đất theo từng lớp và thí nghiệm độ chặt."),
 ],
 "dialogues": [
  ("The excavation is getting deep. Is it safe to go down?", [
    ("Not yet. The shoring on the north side isn't finished. Please wait until it's installed and checked.", True, "Trả lời dứt khoát + lý do + điều kiện an toàn."),
    ("Yes, go quickly, the soil is hard.", False, "Nguy hiểm — vách hố đào chưa chống có thể sạt bất cứ lúc nào."),
    ("Deep is only three metre.", False, "Sai cấu trúc ('It's only three metres deep') và coi nhẹ nguy cơ sạt lở."),
  ]),
  ("We just hit a cable while digging!", [
    ("Stop the excavator and keep everyone away. I'll call the electrical team to isolate the power.", True, "Dừng máy + giữ khoảng cách + gọi đội điện cô lập nguồn — đúng thứ tự."),
    ("Pull the cable out and continue.", False, "Cực kỳ nguy hiểm — cáp có thể còn điện, phải dừng và cô lập nguồn."),
    ("Who is drive the excavator?", False, "Sai ngữ pháp ('Who is driving…?') và truy trách nhiệm trước khi xử lý an toàn."),
  ]),
  ("Why is the pit full of water this morning?", [
    ("We hit groundwater at three metres, and the pump stopped during the night. We're pumping it out now and adding a backup pump.", True, "Nguyên nhân + đang xử lý + phòng ngừa (thêm bơm dự phòng)."),
    ("Because rain maybe, or water.", False, "Đoán mò, thiếu chủ ngữ và động từ — cần nguyên nhân cụ thể."),
    ("Water come from under.", False, "Thiếu 's' ('comes'), mơ hồ và không nói cách xử lý."),
  ]),
  ("Can we pour the blinding today?", [
    ("Yes, after the consultant checks the bottom of the pit at 10. The soil must be clean and compacted.", True, "Đồng ý có điều kiện: nghiệm thu đáy hố + yêu cầu kỹ thuật."),
    ("Yes, pour now, check later.", False, "Sai quy trình — đáy hố phải được nghiệm thu trước khi đổ bê tông lót."),
    ("Blinding is not important, only thin.", False, "Sai — lớp lót giữ sạch đáy móng và tạo mặt phẳng để đặt thép."),
  ]),
  ("Pile 12 is 80 millimetres out of position. What now?", [
    ("Let's report it to the structural engineer with the survey data. He may need to change the pile cap design.", True, "Báo kỹ sư kết cấu + số liệu đo + hiểu hệ quả (có thể phải đổi thiết kế đài)."),
    ("Just bend the pile a little.", False, "Sai kỹ thuật nghiêm trọng — không được tự xử lý cọc lệch."),
    ("80 is OK, pile is strong.", False, "Thiếu đơn vị, thiếu mạo từ và tự quyết thay thiết kế — độ lệch phải do kỹ sư kết cấu đánh giá."),
  ]),
 ],
 "listen": [
  ("Keep heavy trucks away from the edge", ["trucks", "edge"], "tránh mép hố đào"),
  ("Check for underground cables before you dig", ["underground", "dig"], "dò cáp ngầm"),
  ("We hit groundwater at three metres", ["groundwater", "three"], "gặp nước ngầm"),
  ("Pour the blinding before you fix the rebar", ["blinding", "rebar"], "thứ tự làm móng"),
  ("Attention, please. The excavation on the east side is now four metres deep. Nobody goes down until the shoring is checked.", ["east", "deep", "shoring"], "cảnh báo hố đào"),
  ("The consultant checked the bottom of the pit this morning. The soil is good. We can pour the blinding after lunch.", ["bottom", "soil", "lunch"], "nghiệm thu đáy hố móng"),
 ],
})

# ───────────────────────── C. Hoàn thiện: sơn, ốp lát, trần ─────────────────────────
PHASES.append({
 "title": "Hoàn thiện: sơn, ốp lát, trần",
 "vocab": [
  ("primer", "/ˈpraɪmə/", "n", "sơn lót", "Apply one coat of <b>primer</b> before the paint.", "Sơn một lớp sơn lót trước khi sơn phủ.", "下塗り", "shitanuri"),
  ("putty", "/ˈpʌti/", "n", "bột bả (mát tít)", "Fill the small holes with <b>putty</b> and sand the wall.", "Trám các lỗ nhỏ bằng bột bả rồi chà nhám tường.", "パテ", "pate"),
  ("coat", "/kəʊt/", "n", "lớp (sơn)", "The spec says two <b>coats</b> of paint on all walls.", "Chỉ dẫn kỹ thuật yêu cầu sơn hai lớp cho tất cả tường."),
  ("tile adhesive", "/ˈtaɪl ədˌhiːsɪv/", "n", "keo dán gạch", "Use <b>tile adhesive</b>, not cement mortar, for these large tiles.", "Dùng keo dán gạch, không dùng vữa xi măng cho loại gạch khổ lớn này."),
  ("grout", "/ɡraʊt/", "n", "keo (vữa) chà ron", "The <b>grout</b> in the bathroom must be grey, not white.", "Keo chà ron trong nhà vệ sinh phải màu xám, không phải màu trắng."),
  ("gypsum board", "/ˈdʒɪpsəm ˌbɔːd/", "n", "tấm thạch cao", "Store the <b>gypsum boards</b> flat and keep them dry.", "Để tấm thạch cao nằm phẳng và giữ khô.", "石膏ボード", "sekkō bōdo"),
  ("false ceiling", "/ˌfɔːls ˈsiːlɪŋ/", "n", "trần giả (trần treo, trần thạch cao)", "Leave an access panel in the <b>false ceiling</b> for the valves.", "Chừa lỗ thăm trên trần giả để tiếp cận các van."),
  ("skirting", "/ˈskɜːtɪŋ/", "n", "len chân tường", "Install the <b>skirting</b> after the floor tiles.", "Lắp len chân tường sau khi lát gạch nền.", "巾木", "habaki"),
  ("waterproofing", "/ˈwɔːtəpruːfɪŋ/", "n", "lớp (công tác) chống thấm", "Do a 24-hour flood test on the <b>waterproofing</b> before tiling.", "Ngâm nước thử lớp chống thấm 24 giờ trước khi lát gạch.", "防水", "bōsui"),
  ("mock-up", "/ˈmɒk ʌp/", "n", "mẫu thi công thử (phòng mẫu) để duyệt", "The client wants to see a <b>mock-up</b> of the bathroom first.", "Chủ đầu tư muốn xem phòng vệ sinh mẫu trước.", "モックアップ", "mokkuappu"),
 ],
 "phrases": [
  ("The walls are too wet to paint.", "Tường còn ẩm quá, chưa sơn được."),
  ("Please apply the primer before the first coat.", "Nhớ sơn lót trước lớp sơn đầu tiên nhé."),
  ("Is this the approved paint colour?", "Đây có phải màu sơn đã được duyệt không?"),
  ("These tiles aren't level. Please take them off and lay them again.", "Mấy viên gạch này không phẳng. Gỡ ra lát lại nhé."),
  ("The grout lines must be straight and even.", "Đường ron phải thẳng và đều."),
  ("We'll do a flood test before the tiling starts.", "Tụi tôi sẽ ngâm nước thử trước khi bắt đầu lát gạch."),
  ("Please protect the finished floor with boards.", "Nhớ che sàn đã hoàn thiện bằng tấm lót."),
  ("Leave an access panel for the valves.", "Chừa lỗ thăm để tiếp cận van."),
  ("The ceiling is 20 millimetres lower than the drawing.", "Trần thấp hơn bản vẽ 20 mi-li-mét."),
  ("Let's check the mock-up with the client on Friday.", "Thứ Sáu mình kiểm tra phòng mẫu cùng chủ đầu tư nhé."),
 ],
 "dialogues": [
  ("Can your team start painting this wall today?", [
    ("Not yet. The plaster is still wet. We'll check the moisture tomorrow and then apply the primer.", True, "Lý do kỹ thuật (tường còn ẩm) + bước tiếp theo."),
    ("Yes, paint now, it will dry later.", False, "Sơn lên tường còn ẩm sẽ bị phồng, bong tróc."),
    ("Wall still wet, cannot.", False, "Thiếu chủ ngữ và động từ ('The wall is still wet, so we can't') và không hẹn ngày."),
  ]),
  ("These floor tiles sound hollow when I tap them.", [
    ("You're right. There isn't enough adhesive under them. We'll take them off and lay them again.", True, "Thừa nhận + nguyên nhân (thiếu keo) + làm lại."),
    ("Sound is not important, it looks nice.", False, "Gạch bộp (rỗng bên dưới) dễ nứt, bong về sau — không thể bỏ qua."),
    ("Tile is hollow because tile is cheap.", False, "Đổ cho vật tư khi chưa kiểm tra, thiếu mạo từ."),
  ]),
  ("Why is water coming through the ceiling under the Level 5 bathroom?", [
    ("The waterproofing was damaged near the drain. We'll remove the tiles there, repair it and do a new flood test.", True, "Nguyên nhân + khắc phục + thử lại."),
    ("Maybe the neighbour pipe, not us.", False, "Đổ lỗi khi chưa kiểm tra; 'neighbour pipe' là dịch từng chữ."),
    ("We will tile again, water stop.", False, "Lát lại gạch không sửa được lớp chống thấm; sai ngữ pháp ('the water will stop')."),
  ]),
  ("The client doesn't like the paint colour in the mock-up.", [
    ("OK. Let's ask them to choose from the colour chart, and we'll paint a new sample before we do the whole floor.", True, "Tiếp nhận + để khách chọn + làm mẫu mới trước khi làm đại trà."),
    ("The colour is in the spec, they must accept.", False, "Cứng nhắc với khách — nên trao đổi, làm mẫu mới và ghi nhận thay đổi."),
    ("We paint all already, too late.", False, "Sai thì ('We've already painted everything') — làm đại trà trước khi duyệt mẫu là sai quy trình."),
  ]),
  ("Can we close the false ceiling in the corridor?", [
    ("Yes, the MEP inspection passed yesterday. Please leave access panels at the valves, as shown on the drawing.", True, "Cho phép + căn cứ + nhắc chừa lỗ thăm."),
    ("Close it, if problem we cut later.", False, "Thiếu chủ ngữ và chấp nhận cắt trần về sau — tốn công, xấu hoàn thiện."),
    ("Ceiling close is tomorrow maybe.", False, "Sai cấu trúc, mơ hồ, không có căn cứ."),
  ]),
 ],
 "listen": [
  ("The walls are too wet to paint", ["wet", "paint"], "tường còn ẩm"),
  ("Apply the primer before the first coat", ["primer", "coat"], "sơn lót"),
  ("The grout lines must be straight", ["grout", "straight"], "đường ron"),
  ("Leave an access panel in the ceiling", ["access", "panel"], "chừa lỗ thăm"),
  ("The flood test in bathroom three passed. There was no leak after twenty-four hours. The tilers can start tomorrow.", ["flood", "leak", "tilers"], "kết quả ngâm nước thử"),
  ("The client checked the mock-up this morning. She wants darker grout in the kitchen. Please wait before you tile the other units.", ["mock-up", "darker", "units"], "góp ý phòng mẫu"),
 ],
})

# ───────────────────────── D. Hợp đồng, khối lượng & thanh toán ─────────────────────────
PHASES.append({
 "title": "Hợp đồng, khối lượng & thanh toán",
 "vocab": [
  ("contract", "/ˈkɒntrækt/", "n", "hợp đồng", "The <b>contract</b> says the handover date is 30 November.", "Hợp đồng ghi ngày bàn giao là 30/11.", "契約", "keiyaku"),
  ("scope of work", "/ˌskəʊp əv ˈwɜːk/", "n", "phạm vi công việc", "Painting the fence is not in our <b>scope of work</b>.", "Sơn hàng rào không nằm trong phạm vi công việc của bên tôi."),
  ("bill of quantities", "/ˌbɪl əv ˈkwɒntətiz/", "n", "bảng khối lượng (BOQ)", "Please check the concrete volume against the <b>bill of quantities</b>.", "Kiểm tra khối lượng bê tông so với bảng khối lượng nhé."),
  ("unit rate", "/ˌjuːnɪt ˈreɪt/", "n", "đơn giá", "The <b>unit rate</b> for brickwork includes labour and materials.", "Đơn giá xây gạch đã gồm nhân công và vật tư.", "単価", "tanka"),
  ("variation order", "/ˌveəriˈeɪʃn ˌɔːdə/", "n", "lệnh thay đổi (việc phát sinh) được duyệt, VO", "Extra work needs a signed <b>variation order</b>.", "Việc phát sinh phải có lệnh thay đổi đã ký."),
  ("quantity surveyor", "/ˈkwɒntəti səˌveɪə/", "n", "kỹ sư khối lượng – dự toán (QS)", "Our <b>quantity surveyor</b> will measure the finished work on Friday.", "Thứ Sáu kỹ sư QS bên mình sẽ đo khối lượng đã làm."),
  ("interim payment", "/ˌɪntərɪm ˈpeɪmənt/", "n", "thanh toán giai đoạn (theo khối lượng hoàn thành)", "We submit the <b>interim payment</b> application on the 25th of every month.", "Ngày 25 hằng tháng bên mình nộp hồ sơ đề nghị thanh toán giai đoạn.", "出来高払い", "dekidaka barai"),
  ("invoice", "/ˈɪnvɔɪs/", "n", "hóa đơn", "The <b>invoice</b> has the wrong tax number.", "Hóa đơn bị ghi sai mã số thuế.", "請求書", "seikyūsho"),
  ("retention", "/rɪˈtenʃn/", "n", "tiền giữ lại (bảo lưu, trả sau bàn giao / hết bảo hành)", "The client keeps 5 percent <b>retention</b> from each payment.", "Chủ đầu tư giữ lại 5% của mỗi đợt thanh toán."),
  ("extension of time", "/ɪkˌstenʃn əv ˈtaɪm/", "n", "gia hạn thời gian hoàn thành (EOT)", "We'll ask for an <b>extension of time</b> because of the design changes.", "Bên mình sẽ xin gia hạn thời gian vì có thay đổi thiết kế.", "工期延長", "kōki enchō"),
 ],
 "phrases": [
  ("Is this work included in the contract?", "Phần việc này có trong hợp đồng không?"),
  ("This is extra work. We need a variation order first.", "Đây là việc phát sinh. Phải có lệnh thay đổi trước."),
  ("Could you confirm the instruction in writing?", "Anh xác nhận chỉ thị này bằng văn bản giúp tôi được không?"),
  ("The quantity on site is higher than in the BOQ.", "Khối lượng thực tế cao hơn trong BOQ."),
  ("Let's measure it together on Friday.", "Thứ Sáu mình cùng đo nhé."),
  ("We've sent the payment application for May.", "Bên tôi đã gửi hồ sơ đề nghị thanh toán tháng Năm."),
  ("When can we expect the payment?", "Khi nào bên tôi nhận được thanh toán?"),
  ("The payment is two weeks late.", "Thanh toán đang trễ hai tuần."),
  ("Please sign the measurement sheet.", "Anh ký giúp biên bản đo khối lượng nhé."),
  ("The unit rate for this item is in the contract.", "Đơn giá của hạng mục này có trong hợp đồng."),
 ],
 "dialogues": [
  ("The client asked us to add two more windows. Can we start?", [
    ("Not yet. It's extra work, so we need a signed variation order with the cost first.", True, "Việc ngoài hợp đồng phải có lệnh thay đổi được ký kèm chi phí."),
    ("Yes, client is boss, do it now.", False, "Làm phát sinh khi chưa có văn bản — dễ không được thanh toán."),
    ("Two window is small, free.", False, "Thiếu 's' ('two windows') và tự ý làm miễn phí, không theo hợp đồng."),
  ]),
  ("Your payment application shows 1,200 cubic metres of concrete. Our figure is 1,100.", [
    ("Let's measure it together on site and compare it with the drawings. I'll bring our records.", True, "Đề xuất cùng đo đối chiếu + mang hồ sơ — cách xử lý chênh lệch khối lượng chuẩn."),
    ("Our number is right, your number is wrong.", False, "Khẳng định cảm tính, không đưa căn cứ."),
    ("OK, 1,100, no problem.", False, "Chấp nhận ngay khi chưa kiểm tra — công ty có thể mất tiền."),
  ]),
  ("When will we get paid for April?", [
    ("The consultant approved the application last week. The client should pay within 14 days, so around the 20th.", True, "Tình trạng hồ sơ + thời hạn theo hợp đồng + ngày dự kiến."),
    ("Payment is slow, I don't know why.", False, "Than phiền, không có thông tin."),
    ("Maybe money come next month.", False, "Thiếu 's' ('comes') và quá mơ hồ."),
  ]),
  ("Is cleaning the windows in your scope of work?", [
    ("Yes. Final cleaning is in section 4 of our contract, and that includes the windows.", True, "Trả lời + căn cứ hợp đồng cụ thể."),
    ("Scope is many things, I think yes.", False, "Mơ hồ — phải dựa vào hợp đồng."),
    ("Window is not our, I think.", False, "Sai ngữ pháp ('not ours') và không kiểm tra hợp đồng."),
  ]),
  ("The rain stopped us for five days. What should we do?", [
    ("Let's check the contract, keep the daily reports as evidence and ask for an extension of time.", True, "Căn cứ hợp đồng + bằng chứng (nhật ký) + xin gia hạn."),
    ("Nothing, just work faster.", False, "Bỏ qua quyền xin gia hạn — có thể bị phạt chậm tiến độ."),
    ("Rain is not our fault, so no need do anything.", False, "Sai ngữ pháp ('no need to do') và bị động — phải thông báo, xin gia hạn đúng hạn."),
  ]),
 ],
 "listen": [
  ("This is extra work so we need a variation order", ["extra", "variation"], "việc phát sinh"),
  ("Please confirm the instruction in writing", ["confirm", "writing"], "xác nhận bằng văn bản"),
  ("The payment for April is two weeks late", ["payment", "late"], "thanh toán trễ"),
  ("Let us measure the work together on Friday", ["measure", "Friday"], "cùng đo khối lượng"),
  ("Our quantity surveyor will visit the site on Thursday. He will measure the brickwork on Levels three and four. Please prepare the drawings.", ["Thursday", "brickwork", "drawings"], "hẹn đo khối lượng"),
  ("We sent the payment application for May last week. The consultant approved most items. Two items need more photos.", ["application", "approved", "photos"], "tình trạng hồ sơ thanh toán"),
 ],
})

# ───────────────────────── E. Nhà thầu phụ & điều phối ─────────────────────────
PHASES.append({
 "title": "Nhà thầu phụ & điều phối",
 "vocab": [
  ("coordination", "/kəʊˌɔːdɪˈneɪʃn/", "n", "sự phối hợp", "Good <b>coordination</b> between teams saves a lot of time.", "Phối hợp tốt giữa các đội giúp tiết kiệm nhiều thời gian.", "調整", "chōsei"),
  ("interface", "/ˈɪntəfeɪs/", "n", "chỗ tiếp giáp giữa hai hạng mục (hai đội)", "Who is responsible for the <b>interface</b> between the wall and the window?", "Ai chịu trách nhiệm chỗ tiếp giáp giữa tường và cửa sổ?", "取り合い", "toriai"),
  ("look-ahead schedule", "/ˈlʊk əˌhed ˌʃedjuːl/", "n", "tiến độ cuốn chiếu (kế hoạch 2–3 tuần tới)", "Please send your three-week <b>look-ahead schedule</b> by Friday.", "Gửi tiến độ cuốn chiếu ba tuần trước thứ Sáu nhé."),
  ("work area", "/ˈwɜːk ˌeəriə/", "n", "khu vực (mặt bằng) thi công", "We'll hand over this <b>work area</b> to the painters on Monday.", "Thứ Hai mình sẽ giao khu vực này cho đội sơn."),
  ("trade", "/treɪd/", "n", "đội nghề, tổ chuyên môn (thợ điện, thợ sơn…)", "Five <b>trades</b> are working on Level 3 this week.", "Tuần này có năm đội nghề cùng làm ở tầng 3.", "職種", "shokushu"),
  ("sequence", "/ˈsiːkwəns/", "n", "trình tự (thi công)", "The <b>sequence</b> is wiring first, then the ceiling, then painting.", "Trình tự là đi dây trước, rồi làm trần, rồi mới sơn.", "手順", "tejun"),
  ("access", "/ˈækses/", "n", "lối vào; việc vào được (khu vực làm việc)", "The painters need <b>access</b> to Room 301 tomorrow.", "Mai đội sơn cần vào được phòng 301."),
  ("protection", "/prəˈtekʃn/", "n", "lớp che chắn bảo vệ (thành phẩm)", "Remove the floor <b>protection</b> just before the handover.", "Chỉ gỡ lớp che chắn sàn ngay trước khi bàn giao.", "養生", "yōjō"),
  ("back charge", "/ˈbæk ˌtʃɑːdʒ/", "n", "khoản trừ tiền (tính chi phí sửa chữa cho bên gây ra)", "If your team damages the tiles again, we'll issue a <b>back charge</b>.", "Nếu đội bên anh lại làm hỏng gạch, bên tôi sẽ trừ tiền sửa chữa."),
  ("idle", "/ˈaɪdl/", "adj", "phải ngồi chờ, không có việc (vì chưa có mặt bằng, vật tư)", "My workers were <b>idle</b> for half a day because the area wasn't ready.", "Công nhân của tôi phải ngồi chờ nửa ngày vì mặt bằng chưa sẵn sàng."),
 ],
 "phrases": [
  ("Which area can my team start on tomorrow?", "Ngày mai đội tôi bắt đầu được ở khu nào?"),
  ("Please finish the wiring before the ceiling team comes.", "Làm xong phần đi dây trước khi đội trần vào nhé."),
  ("Let's agree on the sequence for Level 5.", "Mình thống nhất trình tự thi công tầng 5 nhé."),
  ("Your team damaged the finished wall. Please repair it.", "Đội anh làm hỏng bức tường đã hoàn thiện. Sửa lại giúp nhé."),
  ("Please keep the floor protection in place.", "Giữ nguyên lớp che chắn sàn nhé."),
  ("The area is ready. You can start on Monday.", "Mặt bằng đã sẵn sàng. Thứ Hai đội anh vào làm được."),
  ("We need the scaffolding for two more days.", "Bên tôi cần giữ giàn giáo thêm hai ngày."),
  ("Please send your look-ahead schedule by Friday.", "Gửi tiến độ cuốn chiếu trước thứ Sáu nhé."),
  ("Who is responsible for cleaning this area?", "Ai chịu trách nhiệm dọn khu vực này?"),
  ("Let's solve this at the coordination meeting.", "Mình giải quyết việc này ở buổi họp phối hợp nhé."),
 ],
 "dialogues": [
  ("My team came to Level 4, but the area isn't ready. We lost half a day.", [
    ("I'm sorry. The plastering finished late. Your team can start in Room 402 now, and you'll have the rest of the floor tomorrow.", True, "Xin lỗi + lý do + phương án ngay để đội không phải chờ."),
    ("Not my problem, wait.", False, "Cộc lốc, đùn đẩy — nhà thầu chính phải lo mặt bằng cho nhà thầu phụ."),
    ("Your team come too early.", False, "Sai thì ('came') và đổ lỗi, không giải quyết."),
  ]),
  ("The electricians and the ceiling team both want to work in the corridor tomorrow.", [
    ("Let's put the electricians in the morning and the ceiling team after lunch. I'll tell both foremen today.", True, "Chia ca hợp lý (đi dây trước, làm trần sau) + chủ động báo cả hai bên."),
    ("Who comes first, works first.", False, "Để các đội tự tranh nhau — dễ xung đột, mất an toàn."),
    ("Corridor is small, cannot two team.", False, "Thiếu động từ, sai số nhiều ('two teams') và không có phương án."),
  ]),
  ("Who broke the tiles near the lift?", [
    ("The ceiling team did when they moved their boards. I've taken photos, and I'll discuss the repair cost with their manager.", True, "Xác định bên gây ra + bằng chứng + xử lý chi phí đúng mực."),
    ("I don't know, everybody walk here.", False, "Sai chia động từ ('walks') và không truy trách nhiệm."),
    ("Somebody bad, we never know.", False, "Buông xuôi — cần ghi nhận bằng chứng để xử lý chi phí."),
  ]),
  ("Can we remove the scaffolding on the north side?", [
    ("Please wait until Thursday. The painters still need it for the top two floors.", True, "Đề nghị chờ + lý do + mốc."),
    ("Yes, remove, painters can use ladder.", False, "Để thợ sơn mặt ngoài nhà cao tầng dùng thang là nguy hiểm."),
    ("Scaffolding is no need already.", False, "Sai ngữ pháp ('We don't need it anymore') và chưa hỏi các đội khác."),
  ]),
  ("What do you need from the other trades this week?", [
    ("We need the MEP team to finish the sleeves on Level 6 by Wednesday, so we can pour on Friday.", True, "Nêu rõ cần gì, của ai, hạn nào, vì sao."),
    ("Nothing, we are OK.", False, "Không nêu phụ thuộc — dễ bị động khi đội khác làm chậm."),
    ("Other team always slow, we need fast.", False, "Than phiền chung chung, sai ngữ pháp ('The other teams are always slow')."),
  ]),
 ],
 "listen": [
  ("Please finish the wiring before the ceiling team comes", ["wiring", "ceiling"], "trình tự thi công"),
  ("Keep the floor protection in place", ["floor", "protection"], "giữ lớp che chắn"),
  ("Your team can start on Level five on Monday", ["start", "Monday"], "giao mặt bằng"),
  ("Please send your look-ahead schedule by Friday", ["look-ahead", "Friday"], "nhắc gửi tiến độ"),
  ("Tomorrow morning the electricians will work in the corridor. The ceiling team can start there after lunch. Please do not block the stairs.", ["electricians", "lunch", "stairs"], "chia ca làm việc"),
  ("Some tiles near the lift were broken yesterday. The ceiling team moved boards without protection. They will pay for the repair.", ["broken", "protection", "repair"], "xử lý làm hỏng thành phẩm"),
 ],
})

# ───────────────────────── F. Máy thi công & thiết bị ─────────────────────────
PHASES.append({
 "title": "Máy thi công & thiết bị",
 "vocab": [
  ("excavator", "/ˈekskəveɪtə/", "n", "máy đào", "The <b>excavator</b> will dig the footings on Monday.", "Thứ Hai máy đào sẽ đào hố móng.", "バックホウ", "bakkuhō"),
  ("forklift", "/ˈfɔːklɪft/", "n", "xe nâng", "Only licensed drivers can use the <b>forklift</b>.", "Chỉ người có chứng chỉ mới được lái xe nâng.", "フォークリフト", "fōkurifuto"),
  ("concrete pump", "/ˈkɒŋkriːt ˌpʌmp/", "n", "xe (máy) bơm bê tông", "The <b>concrete pump</b> needs a flat, firm place to stand.", "Xe bơm bê tông cần chỗ đứng bằng phẳng, nền chắc.", "ポンプ車", "ponpusha"),
  ("generator", "/ˈdʒenəreɪtə/", "n", "máy phát điện", "Keep the <b>generator</b> outside, away from the offices.", "Đặt máy phát điện ở ngoài trời, xa văn phòng.", "発電機", "hatsudenki"),
  ("operator", "/ˈɒpəreɪtə/", "n", "người vận hành (lái) máy", "The <b>operator</b> must check the machine before every shift.", "Người vận hành phải kiểm tra máy trước mỗi ca.", "オペレーター", "operētā"),
  ("pre-use check", "/ˌpriː ˈjuːs ˌtʃek/", "n", "kiểm tra máy trước khi sử dụng (đầu ca)", "Fill in the <b>pre-use check</b> form every morning.", "Sáng nào cũng phải điền phiếu kiểm tra máy trước khi dùng.", "始業点検", "shigyō tenken"),
  ("breakdown", "/ˈbreɪkdaʊn/", "n", "sự hỏng máy, sự cố máy", "A <b>breakdown</b> of the tower crane stopped all lifting today.", "Cẩu tháp bị hỏng nên hôm nay dừng hết việc cẩu.", "故障", "koshō"),
  ("maintenance", "/ˈmeɪntənəns/", "n", "sự bảo dưỡng, bảo trì", "The hoist is closed on Saturday for <b>maintenance</b>.", "Thứ Bảy vận thăng nghỉ để bảo dưỡng.", "メンテナンス", "mentenansu"),
  ("outrigger", "/ˈaʊtrɪɡə/", "n", "chân chống (của cẩu, xe bơm)", "Put steel plates under each <b>outrigger</b> on soft ground.", "Nền yếu thì kê tấm thép dưới mỗi chân chống.", "アウトリガー", "autorigā"),
  ("hire", "/ˈhaɪə/", "v", "thuê (máy móc, thiết bị)", "We'll <b>hire</b> a second excavator for two weeks.", "Mình sẽ thuê thêm một máy đào trong hai tuần."),
 ],
 "phrases": [
  ("The excavator broke down this morning.", "Sáng nay máy đào bị hỏng."),
  ("The mechanic will come at 2 p.m.", "2 giờ chiều thợ sửa máy sẽ tới."),
  ("Do you have a licence for this machine?", "Anh có chứng chỉ vận hành máy này không?"),
  ("Please do the pre-use check before you start.", "Kiểm tra máy trước khi bắt đầu nhé."),
  ("Keep out of the swing area of the excavator.", "Không đứng trong vùng quay của máy đào."),
  ("The reversing alarm isn't working. Please fix it today.", "Còi lùi bị hỏng. Sửa trong hôm nay nhé."),
  ("We need to hire a bigger pump for the basement.", "Cần thuê máy bơm lớn hơn cho tầng hầm."),
  ("Don't leave the key in the machine.", "Đừng để chìa khóa trên máy."),
  ("The generator is low on fuel.", "Máy phát sắp hết nhiên liệu."),
  ("Park the machines in the yard at the end of the day.", "Cuối ngày đưa máy về bãi."),
 ],
 "dialogues": [
  ("The excavator broke down. What's the plan?", [
    ("The mechanic will be here at 2 p.m. If he can't fix it today, we'll hire another one for tomorrow.", True, "Giờ sửa + phương án dự phòng."),
    ("Machine broke, no work today.", False, "Thiếu mạo từ và buông xuôi, không có phương án."),
    ("The operator break it, I think.", False, "Sai thì ('broke') và đoán mò đổ lỗi thay vì lên kế hoạch."),
  ]),
  ("Can this worker drive the forklift?", [
    ("No, he doesn't have a licence yet. Hòa can do it — he's certified.", True, "Từ chối + lý do (chưa có chứng chỉ) + người thay thế."),
    ("Yes, it's easy, like a motorbike.", False, "Xe nâng phải do người được đào tạo, có chứng chỉ lái — không 'dễ như xe máy'."),
    ("He can drive maybe, let him try.", False, "Cho thử khi chưa được đào tạo — rất nguy hiểm."),
  ]),
  ("Where should the concrete pump stand?", [
    ("Here, on the hard road. We'll put steel plates under the outriggers and keep it away from the power lines.", True, "Vị trí nền chắc + kê chân chống + tránh đường dây điện."),
    ("Anywhere near the building is OK.", False, "Sai — nền yếu hoặc gần dây điện có thể làm lật xe, gây điện giật."),
    ("Pump stand on the grass, more near.", False, "Sai ngữ pháp ('closer') và chọn nền cỏ mềm — chân chống dễ bị lún."),
  ]),
  ("The reversing alarm on the truck isn't working.", [
    ("Thanks. Let's stop using the truck until it's fixed. I'll call the rental company now.", True, "Cảm ơn + ngừng dùng + liên hệ sửa — đúng nguyên tắc an toàn."),
    ("Driver can look carefully, no alarm OK.", False, "Còi lùi là thiết bị an toàn bắt buộc — không thay bằng 'nhìn kỹ'."),
    ("Alarm is noisy, better no alarm.", False, "Sai về an toàn và sai ngữ pháp."),
  ]),
  ("Did the operator do the pre-use check today?", [
    ("Yes, he did it at 7 a.m. The form is signed. He found a small oil leak, and the mechanic fixed it.", True, "Xác nhận + hồ sơ + phát hiện và đã xử lý."),
    ("He check every day, I think.", False, "Thiếu 's' ('checks') và không chắc — cần phiếu kiểm tra có ký."),
    ("Machine is new, no need check.", False, "Máy mới cũng phải kiểm tra đầu ca; sai ngữ pháp ('no need to check')."),
  ]),
 ],
 "listen": [
  ("The excavator broke down this morning", ["excavator", "broke"], "báo hỏng máy"),
  ("Keep out of the swing area of the excavator", ["swing", "area"], "vùng quay của máy"),
  ("Do the pre-use check before you start", ["pre-use", "start"], "kiểm tra máy đầu ca"),
  ("The generator is low on fuel", ["generator", "fuel"], "máy phát sắp hết dầu"),
  ("The concrete pump will arrive at six. Please put steel plates under the outriggers. Keep it away from the power lines.", ["pump", "plates", "power"], "chuẩn bị chỗ đứng xe bơm"),
  ("The tower crane is closed for maintenance on Saturday. There will be no lifting that day. Please plan your deliveries for Friday.", ["maintenance", "lifting", "deliveries"], "lịch bảo dưỡng cẩu"),
 ],
})

# ───────────────────────── G. Họp với chủ đầu tư & tư vấn giám sát ─────────────────────────
PHASES.append({
 "title": "Họp với chủ đầu tư & tư vấn giám sát",
 "vocab": [
  ("client", "/ˈklaɪənt/", "n", "chủ đầu tư, khách hàng", "The <b>client</b> wants a progress update every Monday.", "Chủ đầu tư muốn được cập nhật tiến độ mỗi thứ Hai.", "発注者", "hatchūsha"),
  ("consultant", "/kənˈsʌltənt/", "n", "tư vấn (thiết kế, giám sát)", "The <b>consultant</b> will join the site meeting at 9.", "Tư vấn sẽ dự họp công trường lúc 9 giờ."),
  ("supervision", "/ˌsuːpəˈvɪʒn/", "n", "sự giám sát", "The <b>supervision</b> consultant checks our work every day.", "Tư vấn giám sát kiểm tra công việc của mình hằng ngày.", "監理", "kanri"),
  ("agenda", "/əˈdʒendə/", "n", "chương trình (nội dung) cuộc họp", "Please send the <b>agenda</b> one day before the meeting.", "Gửi nội dung cuộc họp trước một ngày nhé.", "議題", "gidai"),
  ("minutes", "/ˈmɪnɪts/", "n", "biên bản cuộc họp", "I'll send the <b>minutes</b> of today's meeting by tomorrow noon.", "Trước trưa mai tôi sẽ gửi biên bản cuộc họp hôm nay.", "議事録", "gijiroku"),
  ("action item", "/ˈækʃn ˌaɪtəm/", "n", "việc cần làm sau cuộc họp (có người phụ trách, có hạn)", "Each <b>action item</b> has an owner and a due date.", "Mỗi việc cần làm đều có người phụ trách và hạn chót."),
  ("site instruction", "/ˌsaɪt ɪnˈstrʌkʃn/", "n", "chỉ thị công trường (văn bản của tư vấn)", "The consultant issued a <b>site instruction</b> to move the door.", "Tư vấn đã ra chỉ thị công trường dời vị trí cửa.", "指示書", "shijisho"),
  ("concern", "/kənˈsɜːn/", "n", "mối lo ngại, điều đáng lo", "The client's main <b>concern</b> is the handover date.", "Điều chủ đầu tư lo nhất là ngày bàn giao."),
  ("recovery plan", "/rɪˈkʌvəri ˌplæn/", "n", "kế hoạch bù (khôi phục) tiến độ", "Please submit a <b>recovery plan</b> for the facade work by Friday.", "Vui lòng nộp kế hoạch bù tiến độ cho phần mặt dựng trước thứ Sáu."),
  ("sign off", "/ˌsaɪn ˈɒf/", "phr v", "ký chấp thuận, ký duyệt", "The client will <b>sign off</b> the mock-up after the walkthrough.", "Chủ đầu tư sẽ ký duyệt phòng mẫu sau buổi đi kiểm tra."),
 ],
 "phrases": [
  ("Let's start with the progress update.", "Mình bắt đầu với phần cập nhật tiến độ nhé."),
  ("Here are the photos from this week.", "Đây là ảnh công trường tuần này."),
  ("We're on schedule, except for the facade.", "Tụi tôi đang đúng tiến độ, trừ phần mặt dựng."),
  ("I understand your concern about the handover date.", "Tôi hiểu anh đang lo về ngày bàn giao."),
  ("Could you give us an answer by Friday?", "Anh trả lời giúp bên tôi trước thứ Sáu được không?"),
  ("We'll send a recovery plan by Wednesday.", "Bên tôi sẽ gửi kế hoạch bù tiến độ trước thứ Tư."),
  ("Let me check and get back to you tomorrow.", "Để tôi kiểm tra rồi mai trả lời anh nhé."),
  ("Can we add this to the action items?", "Mình thêm việc này vào danh sách việc cần làm nhé?"),
  ("I'll send the minutes by tomorrow noon.", "Trước trưa mai tôi sẽ gửi biên bản họp."),
  ("Is there anything else before we finish?", "Còn gì nữa không trước khi mình kết thúc?"),
 ],
 "dialogues": [
  ("The facade is two weeks behind. How will you catch up?", [
    ("We'll add a second team from next Monday and work on Sundays. I'll send a recovery plan by Wednesday.", True, "Biện pháp cụ thể + mốc + cam kết bằng văn bản."),
    ("We will try our best.", False, "Nghe lịch sự nhưng rỗng — chủ đầu tư cần biện pháp và con số."),
    ("Facade team is slow, not our fault.", False, "Đổ lỗi cho nhà thầu phụ — tổng thầu vẫn chịu trách nhiệm tiến độ."),
  ]),
  ("I'm worried about the quality of the plastering on Level 8.", [
    ("I understand. Let's walk through Level 8 together after the meeting, and we'll fix any problems you find.", True, "Ghi nhận mối lo + mời đi kiểm tra cùng + cam kết sửa."),
    ("Quality is good, don't worry.", False, "Gạt đi mối lo mà không có căn cứ."),
    ("Plaster is subcontractor do.", False, "Sai cấu trúc ('The subcontractor did the plastering') và né trách nhiệm."),
  ]),
  ("Can you answer our question about the lobby floor today?", [
    ("I'm not sure yet. Let me check with the designer and get back to you by tomorrow noon.", True, "Thành thật là chưa chắc + hẹn giờ trả lời cụ thể."),
    ("Yes, yes, OK.", False, "Nói 'yes' cho qua khi chưa có câu trả lời — dễ gây hiểu lầm."),
    ("Lobby floor I don't know who.", False, "Dịch từng chữ, câu vô nghĩa — nên nói 'I'm not sure. Let me check.'"),
  ]),
  ("The consultant says your team poured without his approval.", [
    ("That's right, and I'm sorry. From now on, I'll send every inspection request one day before the pour.", True, "Nhận lỗi + biện pháp cụ thể để không lặp lại."),
    ("He was not here, so we poured.", False, "Bào chữa — tư vấn chưa có mặt thì phải chờ, không được đổ."),
    ("Consultant always make trouble.", False, "Thiếu 's' ('makes'), thiếu mạo từ và thái độ đối đầu với tư vấn."),
  ]),
  ("Who will send the minutes?", [
    ("I will. I'll send them by tomorrow noon with the list of action items and owners.", True, "Nhận việc + hạn + nội dung."),
    ("Minutes is not important.", False, "Sai chia động từ ('are') và sai — biên bản là căn cứ khi có tranh chấp."),
    ("Somebody will send, maybe you.", False, "Đùn việc, thiếu tân ngữ ('send them')."),
  ]),
 ],
 "listen": [
  ("Let us start with the progress update", ["progress", "update"], "mở đầu cuộc họp"),
  ("I will send the minutes by tomorrow noon", ["minutes", "noon"], "hẹn gửi biên bản"),
  ("We will send a recovery plan by Wednesday", ["recovery", "Wednesday"], "kế hoạch bù tiến độ"),
  ("I understand your concern about the handover date", ["concern", "handover"], "ghi nhận mối lo"),
  ("Thank you for coming. Today we will talk about progress, safety and the facade delay. Let us start with the photos from this week.", ["safety", "facade", "photos"], "mở đầu họp với chủ đầu tư"),
  ("The consultant issued a site instruction yesterday. The kitchen door will move thirty centimetres. We need the new drawing before we start.", ["instruction", "kitchen", "drawing"], "báo chỉ thị công trường"),
 ],
})

# ───────────────────────── H. Phòng cháy & sơ cứu công trường ─────────────────────────
PHASES.append({
 "title": "Phòng cháy & sơ cứu công trường",
 "vocab": [
  ("fire extinguisher", "/ˈfaɪər ɪkˌstɪŋɡwɪʃə/", "n", "bình chữa cháy", "Keep a <b>fire extinguisher</b> within reach when you weld.", "Khi hàn phải để bình chữa cháy trong tầm tay.", "消火器", "shōkaki"),
  ("hot work", "/ˌhɒt ˈwɜːk/", "n", "công việc có lửa, tia lửa (hàn, cắt, mài)", "All <b>hot work</b> needs a permit and a fire watch.", "Mọi công việc có lửa đều cần giấy phép và người canh lửa."),
  ("fire watch", "/ˈfaɪə ˌwɒtʃ/", "n", "người canh lửa (khi làm việc có lửa)", "The <b>fire watch</b> stays for 30 minutes after the welding stops.", "Người canh lửa ở lại 30 phút sau khi ngừng hàn."),
  ("flammable", "/ˈflæməbl/", "adj", "dễ cháy", "Store <b>flammable</b> materials away from the welding area.", "Để vật liệu dễ cháy xa khu vực hàn.", "可燃性", "kanensei"),
  ("spark", "/spɑːk/", "n", "tia lửa", "Use a fire blanket to stop <b>sparks</b> from falling to the floor below.", "Dùng tấm chống cháy để tia lửa không rơi xuống tầng dưới.", "火花", "hibana"),
  ("fire drill", "/ˈfaɪə ˌdrɪl/", "n", "buổi diễn tập phòng cháy, sơ tán", "We'll have a <b>fire drill</b> next Tuesday at 10 a.m.", "Thứ Ba tuần sau lúc 10 giờ sáng sẽ diễn tập PCCC.", "避難訓練", "hinan kunren"),
  ("first aid kit", "/ˌfɜːst ˈeɪd ˌkɪt/", "n", "hộp (túi) sơ cứu", "There's a <b>first aid kit</b> in every site office.", "Văn phòng công trường nào cũng có hộp sơ cứu.", "救急箱", "kyūkyūbako"),
  ("first aider", "/ˌfɜːst ˈeɪdə/", "n", "người sơ cứu (đã được đào tạo)", "The names of the <b>first aiders</b> are on the notice board.", "Tên những người sơ cứu có trên bảng thông báo."),
  ("bleeding", "/ˈbliːdɪŋ/", "n", "sự chảy máu", "Press hard on the cut with a clean cloth to stop the <b>bleeding</b>.", "Ấn chặt miếng vải sạch lên vết cắt để cầm máu.", "出血", "shukketsu"),
  ("unconscious", "/ʌnˈkɒnʃəs/", "adj", "bất tỉnh", "If someone is <b>unconscious</b>, call an ambulance at once and check their breathing.", "Nếu có người bất tỉnh, gọi cấp cứu ngay và kiểm tra hơi thở.", "意識不明", "ishiki fumei"),
 ],
 "phrases": [
  ("Is there a fire extinguisher near the welding area?", "Gần khu vực hàn có bình chữa cháy không?"),
  ("Remove all flammable materials before you start.", "Dọn hết vật liệu dễ cháy trước khi bắt đầu."),
  ("The fire watch must stay for 30 minutes after the work.", "Người canh lửa phải ở lại 30 phút sau khi xong việc."),
  ("Don't use water on an electrical fire.", "Không dùng nước dập đám cháy điện."),
  ("Smoking is only allowed in the smoking area.", "Chỉ được hút thuốc ở khu vực quy định."),
  ("Call the first aider! Someone is hurt on Level 3.", "Gọi người sơ cứu! Có người bị thương ở tầng 3."),
  ("Press on the cut to stop the bleeding.", "Ấn lên vết cắt để cầm máu."),
  ("Cool the burn under running water for 20 minutes.", "Làm mát vết bỏng dưới vòi nước chảy 20 phút."),
  ("He's unconscious. Call an ambulance now!", "Anh ấy bất tỉnh rồi. Gọi cấp cứu ngay!"),
  ("The first aid kit is almost empty. Please refill it.", "Hộp sơ cứu sắp hết đồ rồi. Bổ sung giúp nhé."),
 ],
 "dialogues": [
  ("We finished welding. Can the fire watch go home now?", [
    ("Not yet. He must stay for 30 minutes and check for smoke or hot spots before he leaves.", True, "Đúng quy định: canh lửa thêm sau khi ngừng hàn vì tàn lửa có thể âm ỉ."),
    ("Yes, welding finished, fire finished.", False, "Sai — tàn lửa có thể âm ỉ rồi bùng cháy sau khi ngừng hàn."),
    ("He can go, I watch maybe.", False, "Mơ hồ ('maybe'), thiếu 'will' — phải phân công rõ ràng."),
  ]),
  ("A small fire started in the electrical room!", [
    ("Raise the alarm and use the CO2 extinguisher, not water. If it gets bigger, evacuate and call the fire service.", True, "Báo động + đúng loại bình (CO2 cho đám cháy điện) + biết khi nào phải sơ tán."),
    ("Quick, throw water on it!", False, "Nguy hiểm — nước dẫn điện, có thể bị điện giật."),
    ("Fire is small, finish work first.", False, "Coi thường — đám cháy nhỏ lan rất nhanh."),
  ]),
  ("A worker cut his hand badly on a steel sheet.", [
    ("Press a clean cloth hard on the cut and raise his hand. I'll call the first aider and take him to the clinic.", True, "Sơ cứu đúng: ấn chặt cầm máu, nâng cao tay, gọi người sơ cứu, đưa đi khám."),
    ("Wash it with petrol and continue.", False, "Sai và nguy hiểm — không bao giờ rửa vết thương bằng xăng dầu."),
    ("Small cut, he is strong man.", False, "Thiếu mạo từ ('a strong man') và coi nhẹ vết thương sâu."),
  ]),
  ("Hot metal fell on a worker's arm. It's burned.", [
    ("Cool the burn under clean running water for 20 minutes, and don't put ice or oil on it. I'll call the first aider.", True, "Sơ cứu bỏng đúng: nước sạch mát 20 phút, không chườm đá, không bôi dầu."),
    ("Put toothpaste on it, it's good.", False, "Mẹo dân gian sai — kem đánh răng làm vết bỏng dễ nhiễm trùng và khó xử lý hơn."),
    ("Burn is not serious, no need water.", False, "Sai ngữ pháp ('no need for water') và bỏ qua bước làm mát quan trọng nhất."),
  ]),
  ("Someone fell down and he isn't answering me!", [
    ("Call an ambulance now and get the first aider. Check if he's breathing, and don't move him unless he's in danger.", True, "Gọi cấp cứu + người sơ cứu + kiểm tra hơi thở + không di chuyển nếu không cần."),
    ("Pour water on his face to wake him up.", False, "Sai — mất thời gian và có thể gây sặc; phải gọi cấp cứu và kiểm tra hơi thở."),
    ("Wait, maybe he is sleeping.", False, "Chần chừ nguy hiểm — người bất tỉnh cần cấp cứu ngay."),
  ]),
 ],
 "listen": [
  ("Remove all flammable materials before you start", ["flammable", "materials"], "chuẩn bị trước khi hàn"),
  ("Do not use water on an electrical fire", ["water", "electrical"], "chữa cháy điện"),
  ("Press on the cut to stop the bleeding", ["cut", "bleeding"], "cầm máu"),
  ("The first aid kit is in the site office", ["kit", "office"], "hộp sơ cứu ở đâu"),
  ("There will be a fire drill on Tuesday at ten. When you hear the alarm, stop work and go to the assembly point. Do not use the hoist.", ["drill", "alarm", "hoist"], "thông báo diễn tập"),
  ("A worker burned his arm during welding. We cooled it with water for twenty minutes. He is now at the clinic.", ["burned", "twenty", "clinic"], "báo sự cố bỏng"),
 ],
})

# ───────────────────────── Vai: tình huống + hội thoại mới ─────────────────────────
ROLES_X = {
 "site": {
  "scenarios": [
   ("st_area", "Giao mặt bằng cho nhà thầu phụ", "You are the foreman of a tiling subcontractor. Your team arrived on Level 6, but the area is not ready. I am the site engineer. Complain about your idle workers, then agree on a new start date with me."),
   ("st_meeting", "Chủ trì họp công trường", "You are the client's representative at the weekly site meeting. I lead the meeting. Ask about progress, one delay and last week's action items, and ask who will send the minutes."),
  ],
  "dialogues": [
   ("The painters say they can't start because the scaffolding is in the way.", [
     ("I'll ask the scaffolding team to move it to the west side this morning, so the painters can start after lunch.", True, "Gỡ vướng mặt bằng + thời gian cụ thể."),
     ("Painters always complain.", False, "Phán xét chung chung, không giải quyết."),
     ("Scaffolding stay there, painters wait.", False, "Thiếu 's' ('stays') và để đội sơn ngồi chờ không lý do.")]),
   ("What are the action items from last week's meeting?", [
     ("There were four. Three are closed. The last one, the RFI about the lobby floor, is still waiting for the designer.", True, "Số lượng + tình trạng + việc còn treo và lý do."),
     ("Many items, I forgot.", False, "Không chuẩn bị — người điều phối phải nắm danh sách việc."),
     ("Action items is done all.", False, "Sai chia động từ và trật tự ('All the action items are done').")]),
   ("Can we start the excavation on Monday?", [
     ("Yes, if the surveyor finishes the setting out on Friday and the shoring design is approved.", True, "Đồng ý có điều kiện rõ ràng."),
     ("Yes, dig first, survey later.", False, "Sai trình tự — phải định vị trước rồi mới đào."),
     ("Monday excavator maybe come.", False, "Thiếu động từ, mơ hồ.")]),
   ("The client wants to change the lobby tiles. What should I tell the tiling team?", [
     ("Ask them to stop the lobby for now and move to Level 3. We'll restart after the variation order is signed.", True, "Dừng khu bị thay đổi + chuyển đội sang chỗ khác + chờ văn bản."),
     ("Tell them continue, maybe client change mind again.", False, "Làm tiếp hạng mục sắp đổi thì phải phá ra làm lại; sai ngữ pháp ('to continue')."),
     ("Tiling team go home.", False, "Cho đội nghỉ không cần thiết, sai ngữ pháp — nên chuyển đội sang khu khác.")]),
  ]},
 "qaqc": {
  "scenarios": [
   ("qc_mockup", "Duyệt phòng mẫu với khách", "You are the client's interior designer checking the bathroom mock-up. Point out two problems: uneven grout lines and the wrong skirting colour. Ask me when the corrected mock-up will be ready."),
   ("qc_pile", "Báo cọc không đạt", "You are the consultant's geotechnical engineer. One pile failed the load test. Ask me about the test result, the pile position and what we propose to do."),
  ],
  "dialogues": [
   ("How do you check the waterproofing in the bathrooms?", [
     ("We do a 24-hour flood test. The consultant checks the water level before and after, and we sign the form together.", True, "Phương pháp + có tư vấn chứng kiến + biên bản."),
     ("We look, if no water, OK.", False, "Kiểm tra bằng mắt, không có quy trình và biên bản."),
     ("Waterproofing is very good brand, no need check.", False, "Hãng tốt không thay được việc thử nghiệm; sai ngữ pháp ('no need to check').")]),
   ("The paint on this wall looks patchy.", [
     ("You're right. The second coat is too thin here. We'll apply another coat and ask you to check again tomorrow.", True, "Xác nhận + nguyên nhân + khắc phục + mời kiểm tra lại."),
     ("From far away, it looks OK.", False, "Né lỗi — không thể bảo khách đứng xa để không thấy lỗi."),
     ("Painter is new, sorry sorry.", False, "Xin lỗi lặp kiểu tiếng Việt, thiếu mạo từ, không có cách khắc phục.")]),
   ("Did you check the compaction of the backfill?", [
     ("Yes. We tested every 300-millimetre layer, and all results are above 95 percent. The reports are in the QC file.", True, "Xác nhận + tần suất + kết quả (độ chặt K95 thường gặp) + hồ sơ."),
     ("Yes, the roller went many times.", False, "Lu nhiều lần không phải là kết quả thí nghiệm — cần số liệu."),
     ("Compaction I will check tomorrow maybe.", False, "Chưa kiểm tra nhưng không nói rõ, lại 'maybe'.")]),
   ("The gypsum boards on site got wet. Can we use them?", [
     ("No. Wet boards can bend and grow mould. Let's put them aside, and I'll ask the supplier to replace them.", True, "Từ chối + lý do kỹ thuật + xử lý."),
     ("Yes, dry them in the sun first.", False, "Tấm thạch cao đã ngấm nước bị giảm chất lượng — không dùng lại."),
     ("Board wet little, OK.", False, "Sai ngữ pháp ('a little wet') và chấp nhận vật tư lỗi.")]),
  ]},
 "hse": {
  "scenarios": [
   ("hs_hotwork", "Cấp giấy phép làm việc có lửa", "You are a welding subcontractor foreman. You want to start welding on Level 9 now. I am the HSE officer. Answer my questions about flammable materials, the fire extinguisher and the fire watch."),
   ("hs_firstaid", "Xử lý tai nạn nhỏ", "You are a foreign site manager. A worker cut his hand ten minutes ago. Ask me what happened, what first aid he got and whether he needs to go to hospital."),
  ],
  "dialogues": [
   ("Can we store the paint thinner in the site office?", [
     ("No, it's flammable. Please keep it in the chemical store, away from heat and sparks.", True, "Từ chối + lý do + nơi cất đúng."),
     ("Yes, the office has air-con, it's cool.", False, "Chất dễ cháy không để trong văn phòng dù có điều hòa."),
     ("Thinner is small bottle, no problem.", False, "Thiếu mạo từ và coi nhẹ chất dễ cháy.")]),
   ("Why do we need a fire drill? Everyone knows the way out.", [
     ("Because people panic in a real fire. The drill helps us check the alarm, the routes and how long it takes to count everyone.", True, "Giải thích mục đích diễn tập rõ ràng."),
     ("Because head office say so.", False, "Sai chia động từ ('says') và không giải thích lợi ích."),
     ("Drill is waste time, but we must.", False, "Thiếu 'a … of' ('a waste of time') và tự phủ nhận ý nghĩa diễn tập.")]),
   ("The first aid kit on Level 5 is almost empty.", [
     ("Thanks for telling me. I'll refill it today and check the other kits this week.", True, "Cảm ơn + hành động + kiểm tra rộng hơn."),
     ("Use the kit on Level 4.", False, "Chữa cháy tạm — hộp sơ cứu ở từng tầng phải luôn đủ đồ."),
     ("Who use all the kit?", False, "Sai thì ('Who used…?') và truy lỗi thay vì bổ sung.")]),
   ("Do we have enough first aiders on site?", [
     ("Yes. We have six trained first aiders for 150 workers, with at least one on each shift. Their names are on the notice board.", True, "Con số + phân bổ theo ca + thông tin công khai."),
     ("Everybody can do first aid.", False, "Sai — sơ cứu cần người được đào tạo."),
     ("First aider is enough, I think.", False, "Mơ hồ, không có con số.")]),
  ]},
 "mep": {
  "scenarios": [
   ("mp_generator", "Mất điện công trường", "You are the project manager. The site power went off, and the concrete pour is at 2 p.m. Ask me about the generator, how long it can run and whether the pour can go ahead."),
   ("mp_extra", "Báo việc phát sinh MEP", "You are the client's representative. You want ten more power sockets in the office area. I am the MEP engineer. Ask how long it takes, what it costs and what I need from you before we start."),
  ],
  "dialogues": [
   ("The generator stopped during the night shift.", [
     ("I'll check the fuel and the oil level first. If it's a bigger problem, I'll call the rental company this morning.", True, "Kiểm tra theo thứ tự + phương án gọi hỗ trợ."),
     ("Generator is old, buy new one.", False, "Kết luận vội, thiếu mạo từ — phải kiểm tra trước."),
     ("Night shift stop, no problem.", False, "Coi nhẹ — mất điện ban đêm ảnh hưởng an toàn và tiến độ.")]),
   ("Can we put in the sockets before the plastering?", [
     ("Yes, the conduits and boxes must go in first. We'll finish Level 4 by Wednesday, and then the plasterers can start.", True, "Đúng trình tự (đi ống, đặt đế âm trước khi trát) + hạn + bàn giao cho đội sau."),
     ("After plaster, we cut the wall.", False, "Trát xong mới đục tường là lãng phí, xấu hoàn thiện."),
     ("Socket and plaster same time.", False, "Thiếu động từ và không khả thi — hai đội sẽ vướng nhau.")]),
   ("Where should we put the temporary distribution board?", [
     ("Near the stair core, on a stand with a cover and a lock, and away from wet areas.", True, "Vị trí + điều kiện an toàn điện (có che, có khóa, tránh nước)."),
     ("On the floor anywhere, easy to use.", False, "Tủ điện đặt dưới sàn dễ bị ngập, va chạm — nguy hiểm."),
     ("Board put in the toilet, near water.", False, "Sai ngữ pháp và rất nguy hiểm — điện gần nước.")]),
   ("The client wants ten more sockets. Can you add them today?", [
     ("We can, but it's extra work. I'll send the price and a variation order today, and we'll start after it's signed.", True, "Đồng ý có điều kiện văn bản + chi phí."),
     ("Yes, free, small thing.", False, "Làm miễn phí khi chưa có văn bản — công ty chịu thiệt."),
     ("No, sockets is finish.", False, "Sai ngữ pháp ('are finished') và từ chối cứng nhắc.")]),
  ]},
}

EXTRA = {
 "phases": PHASES,
 "rev": [
  ("Đừng làm xê dịch cọc mốc.", "Don't move the survey pegs."),
  ("Cột này lệch trục 20 mi-li-mét.", "This column is 20 millimetres off the grid line."),
  ("Hố đào sâu nên phải chống vách.", "The excavation is deep, so we need shoring."),
  ("Kiểm tra cáp ngầm trước khi đào.", "Check for underground cables before you dig."),
  ("Tường còn ẩm, chưa sơn được.", "The wall is still wet. We can't paint it yet."),
  ("Mấy viên gạch này bị bộp, phải lát lại.", "These tiles sound hollow. We need to lay them again."),
  ("Việc này phát sinh, cần có lệnh thay đổi.", "This is extra work. We need a variation order."),
  ("Thứ Sáu mình cùng đo khối lượng nhé.", "Let's measure the work together on Friday."),
  ("Thanh toán tháng Tư đang trễ hai tuần.", "The April payment is two weeks late."),
  ("Mặt bằng tầng 5 đã sẵn sàng cho đội anh.", "Level 5 is ready for your team."),
  ("Đội tôi phải ngồi chờ nửa ngày.", "My team was idle for half a day."),
  ("Sáng nay máy đào bị hỏng.", "The excavator broke down this morning."),
  ("Anh có chứng chỉ lái xe nâng không?", "Do you have a forklift licence?"),
  ("Để tôi kiểm tra rồi trả lời anh sau.", "Let me check and get back to you."),
  ("Trước trưa mai tôi sẽ gửi biên bản họp.", "I'll send the minutes by tomorrow noon."),
  ("Không dùng nước dập đám cháy điện.", "Don't use water on an electrical fire."),
 ],
 "reading": [
  {"t": "Survey check message", "text": "Site group chat – 08:15\nSurveyor (Long): I checked the Level 3 column formwork with the total station. 22 of 24 are OK. C5 is 18 mm off grid line C, and D2 is 25 mm off grid line 2. The tolerance is ±5 mm. Please fix C5 and D2 before the pour. I'll check them again at 14:00.", "q": [
    {"q": "How many columns are out of tolerance?", "o": ["Two", "Twenty-two", "Twenty-four"], "a": 0},
    {"q": "What will the surveyor do at 14:00?", "o": ["Pour the columns", "Check the two columns again", "Remove the formwork"], "a": 1}]},
  {"t": "Payment email", "text": "Dear Mr. Minh,\nWe have checked your Interim Payment Application No. 7 (May). Approved amount: 4.2 billion VND. We did not approve item 3.4 (extra brickwork, 380 million VND) because there is no signed variation order. Please submit the VO, and we will review this item next month.\nBest regards,\nQS Team, Supervision Consultant", "q": [
    {"q": "Why was item 3.4 not approved?", "o": ["The quantity was wrong", "There is no signed variation order", "The work is not finished"], "a": 1},
    {"q": "What should the contractor do?", "o": ["Submit the variation order", "Stop the brickwork", "Send a new invoice today"], "a": 0}]},
  {"t": "Level 6 work sequence", "text": "LEVEL 6 – WORK SEQUENCE (Week 32)\nMon–Tue: MEP – ceiling wiring and pipes\nWed: Pressure test (consultant to witness, 9:00)\nThu–Fri: Ceiling team – gypsum boards\nNote: Painters start on Level 6 next Monday. Keep the floor protection in place. Any damage will be back-charged.", "q": [
    {"q": "When can the ceiling team start?", "o": ["Monday", "Wednesday", "Thursday"], "a": 2},
    {"q": "What happens if a team damages the floor?", "o": ["It pays for the repair", "It must work on Sunday", "It must leave the site"], "a": 0}]},
  {"t": "Pre-use check form", "text": "DAILY PRE-USE CHECK – Excavator EX-02\nDate: 12 Aug     Operator: Tài\nTracks: OK\nLights: OK\nReversing alarm: NOT WORKING\nOil leak: none\nResult: DO NOT USE. Reported to the equipment manager at 07:10.", "q": [
    {"q": "What is wrong with the excavator?", "o": ["It has an oil leak", "The reversing alarm doesn't work", "The lights are broken"], "a": 1},
    {"q": "Can the operator use it before it is fixed?", "o": ["Yes, but slowly", "Yes, in the morning only", "No"], "a": 2}]},
  {"t": "Hot work permit", "text": "HOT WORK PERMIT No. HW-118\nWork: welding handrails, Level 9 stairs\nTime: 13:00–16:00, 20 Aug\nConditions: remove flammable materials within 10 m; fire extinguisher at the work area; fire blanket under the welding point.\nFire watch: Quân – stays until 16:30\nApproved by: HSE Officer", "q": [
    {"q": "Until what time must the fire watch stay?", "o": ["16:00", "16:30", "13:00"], "a": 1},
    {"q": "What must be removed before welding?", "o": ["Flammable materials within 10 m", "All workers on Level 9", "The fire blanket"], "a": 0}]},
 ],
 "ai": [
  ("survey", "Báo sai lệch trắc đạc", "You are the consultant's surveyor. You found that two columns are out of position. I am the site engineer. Tell me the numbers, ask how it happened and how we will fix it."),
  ("variation", "Thương lượng việc phát sinh", "You are the client's representative. You ask me to add extra windows in the lobby and want us to start today. I am the contractor's engineer. Listen to my answer about the variation order and the cost, and ask how long it will take."),
  ("payment", "Hỏi thanh toán trễ", "You are the client's finance manager. Our interim payment is two weeks late. I call to ask why and when we will be paid. Explain a small problem with the documents and agree on a date."),
  ("breakdown", "Máy thi công bị hỏng", "You are a foreign project manager. The only excavator on site broke down this morning. Ask me what happened, how long the repair will take and what our backup plan is."),
 ],
 "events": [
  ("kickoff", "Họp khởi động dự án", "You are the client's project director at the kick-off meeting for a new building project next week. Ask me about our team, the site layout, the schedule and how we will report progress."),
  ("fire_drill", "Diễn tập PCCC", "You are a fire safety officer from head office coming to watch our fire drill tomorrow. Ask about the alarm, the escape routes, the assembly point and how we count the workers."),
  ("payment_meeting", "Họp đối chiếu khối lượng, thanh toán", "You are the client's quantity surveyor. We have a meeting next week to agree on this month's payment. Ask about quantities that don't match the BOQ and about extra work without a variation order."),
 ],
 "quips": [
  "Measure twice, pour once!",
  "Primer first, then paint!",
  "No VO, no extra work!",
  "Pre-use check: done!",
  "Fire watch on duty!",
  "Shoring first, then dig!",
 ],
 "roles": ROLES_X,
}
