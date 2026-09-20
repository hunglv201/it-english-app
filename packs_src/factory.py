# -*- coding: utf-8 -*-
# Gói "factory" — Sản xuất · Nhà máy (QA/QC, kỹ sư, tổ trưởng, kế hoạch ở nhà máy FDI Nhật/Hàn).
# Schema: xem packs_src/README.md. Build: python3 packs_src/build.py factory

PHASES = []

# ───────────────────────── 0. An toàn lao động ─────────────────────────
PHASES.append({
 "title": "An toàn lao động",
 "vocab": [
  ("safety", "/ˈseɪfti/", "n", "an toàn", "<b>Safety</b> first — always.", "An toàn là trên hết — luôn luôn.", "安全", "anzen"),
  ("PPE", "/ˌpiː piː ˈiː/", "n", "đồ bảo hộ lao động (personal protective equipment)", "Please wear your <b>PPE</b> before you enter the production area.", "Vui lòng mặc đồ bảo hộ trước khi vào khu vực sản xuất.", "保護具", "hogogu"),
  ("gloves", "/ɡlʌvz/", "n", "găng tay", "Wear cut-resistant <b>gloves</b> at this station.", "Ở công đoạn này phải đeo găng tay chống cắt.", "手袋", "tebukuro"),
  ("hazard", "/ˈhæzəd/", "n", "mối nguy hiểm", "Oil on the floor is a slip <b>hazard</b>.", "Dầu trên sàn là mối nguy gây trơn trượt.", "危険源", "kikengen"),
  ("emergency exit", "/ɪˈmɜːdʒənsi ˌeksɪt/", "n", "lối thoát hiểm", "Never block the <b>emergency exit</b>.", "Không bao giờ được chắn lối thoát hiểm.", "非常口", "hijōguchi"),
  ("fire extinguisher", "/ˈfaɪər ɪkˌstɪŋɡwɪʃə/", "n", "bình chữa cháy", "The <b>fire extinguisher</b> is next to the door.", "Bình chữa cháy ở cạnh cửa.", "消火器", "shōkaki"),
  ("near miss", "/ˌnɪə ˈmɪs/", "n", "sự cố suýt xảy ra tai nạn", "Please report every <b>near miss</b>, even small ones.", "Hãy báo mọi sự cố suýt xảy ra tai nạn, kể cả chuyện nhỏ.", "ヒヤリハット", "hiyari hatto"),
  ("lockout-tagout", "/ˌlɒkaʊt ˈtæɡaʊt/", "n", "khóa và treo thẻ cách ly nguồn (LOTO)", "Do <b>lockout-tagout</b> before you open the machine.", "Làm khóa – treo thẻ cách ly nguồn trước khi mở máy."),
  ("injury", "/ˈɪndʒəri/", "n", "chấn thương", "We had zero <b>injuries</b> this month.", "Tháng này không có ca chấn thương nào.", "怪我", "kega"),
  ("first aid", "/ˌfɜːst ˈeɪd/", "n", "sơ cứu", "The <b>first aid</b> kit is in the leader's office.", "Hộp sơ cứu ở phòng tổ trưởng.", "応急処置", "ōkyū shochi"),
 ],
 "phrases": [
  ("Please wear your safety glasses in this area.", "Khu vực này phải đeo kính bảo hộ."),
  ("Stop the machine first, then clean it.", "Dừng máy trước rồi mới vệ sinh."),
  ("Watch your step — the floor is wet.", "Cẩn thận bước chân — sàn đang ướt."),
  ("Don't put your hand inside the machine.", "Không được cho tay vào trong máy."),
  ("Where is the nearest emergency exit?", "Lối thoát hiểm gần nhất ở đâu?"),
  ("I'd like to report a near miss on Line 2.", "Tôi muốn báo một sự cố suýt xảy ra tai nạn ở chuyền 2."),
  ("Someone is hurt. Please call the nurse.", "Có người bị thương. Gọi y tá giúp với."),
  ("This area is for authorized staff only.", "Khu vực này chỉ dành cho người có phận sự."),
  ("We have a fire drill at 2 p.m. today.", "Chiều nay 2 giờ có diễn tập phòng cháy chữa cháy."),
  ("Safety first — if you're not sure, stop and ask.", "An toàn là trên hết — không chắc thì dừng lại và hỏi."),
 ],
 "dialogues": [
  ("Why aren't you wearing safety glasses?", [
    ("Sorry, I forgot. I'll put them on right now.", True, "Xin lỗi + sửa ngay — đúng thái độ khi bị nhắc về an toàn."),
    ("Because I not need, only five minutes.", False, "Thiếu 'do' ('I don't need them') và coi nhẹ an toàn — 5 phút cũng có thể gặp tai nạn."),
    ("The glasses is not mine.", False, "Sai chia động từ ('are') và né tránh, không sửa sai."),
  ]),
  ("There's oil on the floor near Machine 4.", [
    ("Thanks for telling me. I'll put a sign there and get it cleaned now.", True, "Cảm ơn + cảnh báo + xử lý ngay."),
    ("It is not my area.", False, "Đùn đẩy — thấy mối nguy thì ai cũng phải xử lý hoặc báo."),
    ("OK, clean later.", False, "Thiếu chủ ngữ, và để sau là nguy hiểm: dầu gây trơn trượt."),
  ]),
  ("What should I do if the fire alarm goes off?", [
    ("Stop your work, leave by the nearest exit and go to the meeting point outside.", True, "Hướng dẫn đủ 3 bước, rõ ràng."),
    ("You run.", False, "Quá cộc và thiếu thông tin: chạy đi đâu, tập trung ở đâu?"),
    ("The alarm is very loud.", False, "Không trả lời câu hỏi 'cần làm gì'."),
  ]),
  ("A worker cut his finger at Station 3.", [
    ("I'll bring the first aid kit now. Please call the nurse.", True, "Hành động ngay + phân công rõ."),
    ("Why he is not careful?", False, "Sai trật tự câu hỏi ('Why wasn't he careful?') và trách người lúc cần sơ cứu."),
    ("He cut finger yesterday also.", False, "Thiếu 'his' và lạc đề — cần xử lý ngay, không kể chuyện cũ."),
  ]),
  ("Can I clean the machine while it's running?", [
    ("No. Please stop it and do lockout-tagout first.", True, "Trả lời dứt khoát + đúng quy trình an toàn."),
    ("Yes, but careful.", False, "Sai về an toàn — không bao giờ vệ sinh khi máy đang chạy."),
    ("No can.", False, "Dịch từng chữ 'không được' — nên nói 'No, you can't.' và giải thích."),
  ]),
 ],
 "listen": [
  ("Please wear your safety glasses in this area", ["safety", "glasses"], "nhắc đồ bảo hộ"),
  ("Stop the machine before you clean it", ["Stop", "clean"], "quy tắc vệ sinh máy"),
  ("The fire extinguisher is next to the door", ["extinguisher", "door"], "vị trí bình chữa cháy"),
  ("Please report every near miss to your leader", ["report", "leader"], "báo sự cố suýt tai nạn"),
  ("Good morning, everyone. Yesterday someone slipped on oil near Line 3. If you see oil on the floor, please clean it up right away.", ["slipped", "floor", "clean"], "nhắc an toàn đầu ca"),
  ("This is a fire drill. Please stop your work and leave by the nearest exit. Meet at the parking area.", ["drill", "exit", "parking"], "thông báo diễn tập"),
 ],
})

# ───────────────────────── 1. Dây chuyền & quy trình sản xuất ─────────────────────────
PHASES.append({
 "title": "Dây chuyền & quy trình sản xuất",
 "vocab": [
  ("production line", "/prəˈdʌkʃn ˌlaɪn/", "n", "dây chuyền sản xuất, chuyền", "We have six <b>production lines</b> in this building.", "Tòa nhà này có sáu chuyền sản xuất.", "生産ライン", "seisan rain"),
  ("shift", "/ʃɪft/", "n", "ca làm việc", "I'm on the night <b>shift</b> this week.", "Tuần này tôi làm ca đêm."),
  ("cycle time", "/ˈsaɪkl ˌtaɪm/", "n", "thời gian chu kỳ (cho một sản phẩm)", "The <b>cycle time</b> is 45 seconds per unit.", "Thời gian chu kỳ là 45 giây mỗi sản phẩm."),
  ("output", "/ˈaʊtpʊt/", "n", "sản lượng", "Our <b>output</b> today is 1,200 pieces.", "Sản lượng hôm nay của tổ là 1.200 cái."),
  ("target", "/ˈtɑːɡɪt/", "n", "chỉ tiêu, mục tiêu", "We're 50 units below <b>target</b>.", "Tụi mình đang thiếu 50 sản phẩm so với chỉ tiêu.", "目標", "mokuhyō"),
  ("SOP", "/ˌes əʊ ˈpiː/", "n", "quy trình thao tác chuẩn", "Follow the <b>SOP</b> at every step.", "Làm đúng quy trình thao tác chuẩn ở từng bước.", "作業標準書", "sagyō hyōjunsho"),
  ("process", "/ˈprəʊses/", "n", "công đoạn, quy trình", "Painting is the next <b>process</b> after welding.", "Sơn là công đoạn tiếp theo sau hàn.", "工程", "kōtei"),
  ("assemble", "/əˈsembl/", "v", "lắp ráp", "This station <b>assembles</b> the main board.", "Công đoạn này lắp ráp bo mạch chính.", "組み立てる", "kumitateru"),
  ("raw material", "/ˌrɔː məˈtɪəriəl/", "n", "nguyên vật liệu", "The <b>raw material</b> arrives every Monday.", "Nguyên vật liệu về vào mỗi thứ Hai.", "原材料", "genzairyō"),
  ("changeover", "/ˈtʃeɪndʒəʊvə/", "n", "chuyển đổi mã hàng (thay khuôn, đổi model)", "The <b>changeover</b> to Model B takes 30 minutes.", "Chuyển đổi sang model B mất 30 phút.", "段取り替え", "dandorigae"),
 ],
 "phrases": [
  ("Line 2 is running normally.", "Chuyền 2 đang chạy bình thường."),
  ("We finished 800 pieces this morning.", "Sáng nay tụi mình làm xong 800 cái."),
  ("We're 50 units behind target.", "Tụi mình đang thiếu 50 sản phẩm so với chỉ tiêu."),
  ("The cycle time is too long at Station 5.", "Thời gian chu kỳ ở công đoạn 5 đang quá dài."),
  ("Please follow the SOP exactly.", "Hãy làm đúng theo SOP."),
  ("After assembly, the parts go to inspection.", "Sau khi lắp ráp, hàng được chuyển sang kiểm tra."),
  ("We'll change over to Model B after lunch.", "Sau giờ ăn trưa mình sẽ chuyển sang model B."),
  ("The night shift starts at 10 p.m.", "Ca đêm bắt đầu lúc 10 giờ tối."),
  ("We're waiting for materials from the warehouse.", "Tụi mình đang chờ vật tư từ kho."),
  ("Can you move two workers to Line 3?", "Anh chuyển giúp hai công nhân sang chuyền 3 được không?"),
 ],
 "dialogues": [
  ("How's Line 2 doing today?", [
    ("It's running well. We've made 600 pieces, and we're on target.", True, "Tình trạng + con số + so với chỉ tiêu."),
    ("Line 2 is run good.", False, "Sai dạng động từ: 'Line 2 is running well.'"),
    ("Workers are working.", False, "Quá chung chung, không có sản lượng hay tình trạng."),
  ]),
  ("What's the cycle time at this station?", [
    ("About 40 seconds per unit. The target is 36.", True, "Con số cụ thể + so với mục tiêu."),
    ("It is time for cycle.", False, "Hiểu sai thuật ngữ 'cycle time' (thời gian chu kỳ)."),
    ("Very fast.", False, "Mơ hồ — chuyên gia cần con số."),
  ]),
  ("Why is Station 4 waiting?", [
    ("Station 3 is slower today, so parts are coming late. We're checking the reason now.", True, "Nêu nguyên nhân trực tiếp + đang làm gì."),
    ("Because Station 3 workers are lazy.", False, "Đổ lỗi cho người khi chưa tìm nguyên nhân thật."),
    ("Station 4 wait parts.", False, "Thiếu 'is … for': 'Station 4 is waiting for parts.'"),
  ]),
  ("When will you change over to Model B?", [
    ("After lunch, at one o'clock. It'll take about 30 minutes.", True, "Thời điểm + thời gian chuyển đổi."),
    ("We change Model B after lunch maybe.", False, "Thiếu 'will'/'over to', thêm 'maybe' nghe thiếu chắc chắn."),
    ("Model B is new model.", False, "Không trả lời câu hỏi 'khi nào'."),
  ]),
  ("Can you add one more worker to Line 3?", [
    ("Yes, I'll move Hùng from Line 1. He knows this process.", True, "Đồng ý + nói rõ chuyển ai và vì sao."),
    ("OK, I will adding.", False, "Sau 'will' dùng động từ nguyên mẫu: 'I'll add one.'"),
    ("No people.", False, "Cộc lốc; nên giải thích: 'Sorry, we're short of people today.'"),
  ]),
 ],
 "listen": [
  ("Line two is running on target today", ["running", "target"], "tình trạng chuyền"),
  ("The cycle time at this station is forty seconds", ["cycle", "seconds"], "thời gian chu kỳ"),
  ("The night shift starts at ten o'clock", ["night", "ten"], "giờ vào ca"),
  ("We will change over to Model B after lunch", ["change", "lunch"], "đổi mã hàng"),
  ("Good morning, team. Our target today is one thousand two hundred pieces. We will start Model B after lunch.", ["target", "hundred", "lunch"], "họp đầu ca"),
  ("Station three is slow today. Parts are coming late to Station four. Please check the SOP again.", ["slow", "late", "SOP"], "báo công đoạn chậm"),
 ],
})

# ───────────────────────── 2. Kiểm tra chất lượng (QA/QC) ─────────────────────────
PHASES.append({
 "title": "Kiểm tra chất lượng (QA/QC)",
 "vocab": [
  ("defect", "/ˈdiːfekt/", "n", "lỗi, hàng lỗi", "We found three <b>defects</b> in this box.", "Tụi mình phát hiện ba cái lỗi trong thùng này.", "不良", "furyō"),
  ("inspection", "/ɪnˈspekʃn/", "n", "sự kiểm tra", "All parts need a visual <b>inspection</b>.", "Tất cả linh kiện phải kiểm tra ngoại quan.", "検査", "kensa"),
  ("yield", "/jiːld/", "n", "tỉ lệ đạt (hàng tốt)", "The <b>yield</b> on Line 1 is 98 percent.", "Tỉ lệ đạt của chuyền 1 là 98%.", "歩留まり", "budomari"),
  ("first article", "/ˌfɜːst ˈɑːtɪkl/", "n", "sản phẩm đầu tiên (hàng đầu lô/đầu ca, phải kiểm trước khi chạy hàng loạt)", "Please check the <b>first article</b> before mass production.", "Vui lòng kiểm tra sản phẩm đầu tiên trước khi sản xuất hàng loạt.", "初品", "shohin"),
  ("specification", "/ˌspesɪfɪˈkeɪʃn/", "n", "thông số kỹ thuật, tiêu chuẩn (spec)", "This size is out of <b>specification</b>.", "Kích thước này nằm ngoài tiêu chuẩn.", "仕様", "shiyō"),
  ("tolerance", "/ˈtɒlərəns/", "n", "dung sai", "The <b>tolerance</b> is plus or minus 0.05 mm.", "Dung sai là cộng trừ 0,05 mi-li-mét.", "公差", "kōsa"),
  ("sample", "/ˈsɑːmpl/", "n/v", "mẫu; lấy mẫu", "We check five <b>samples</b> every hour.", "Mỗi giờ tụi mình kiểm tra năm mẫu."),
  ("reject", "/rɪˈdʒekt/", "v", "loại, không chấp nhận (hàng)", "QC <b>rejected</b> the whole lot.", "QC đã loại cả lô."),
  ("lot", "/lɒt/", "n", "lô (hàng)", "Which <b>lot</b> number is this?", "Đây là lô số mấy?", "ロット", "rotto"),
  ("scratch", "/skrætʃ/", "n", "vết xước", "There's a small <b>scratch</b> on the cover.", "Có một vết xước nhỏ trên nắp.", "傷", "kizu"),
 ],
 "phrases": [
  ("This part is out of spec.", "Linh kiện này ngoài tiêu chuẩn."),
  ("The yield today is 97 percent.", "Tỉ lệ đạt hôm nay là 97%."),
  ("We found a scratch on the surface.", "Tụi mình phát hiện một vết xước trên bề mặt."),
  ("Please hold this lot. Don't ship it yet.", "Giữ lô này lại. Chưa được xuất."),
  ("The first article passed inspection.", "Sản phẩm đầu tiên đã đạt kiểm tra."),
  ("Can you measure it again, please?", "Anh đo lại giúp được không?"),
  ("How many pieces did you check?", "Bạn đã kiểm tra bao nhiêu cái?"),
  ("We need to do 100% inspection on this lot.", "Lô này cần kiểm tra 100%."),
  ("The defect rate went down from 3% to 1%.", "Tỉ lệ lỗi đã giảm từ 3% xuống 1%."),
 ],
 "dialogues": [
  ("What's the yield today?", [
    ("It's 97 percent. Most of the defects are scratches.", True, "Con số + loại lỗi chính."),
    ("Yield is good, no problem.", False, "Mơ hồ — QC phải báo con số cụ thể."),
    ("Today yield 97.", False, "Thiếu động từ và đơn vị: 'The yield is 97 percent today.'"),
  ]),
  ("Is this part OK?", [
    ("No. The length is 0.1 millimetres over the tolerance, so it's NG.", True, "Kết luận + số đo + so với dung sai."),
    ("I think OK maybe.", False, "Thiếu chủ ngữ/động từ và không chắc chắn — QC cần kết luận rõ."),
    ("The part is very beautiful.", False, "Dịch kiểu 'đẹp' — chất lượng phải đánh giá theo tiêu chuẩn, không theo cảm giác."),
  ]),
  ("We found defects in Lot 25. What should we do?", [
    ("Please hold the lot and check all the pieces. I'll inform the customer if needed.", True, "Giữ hàng + kiểm tra toàn bộ + báo khách hàng."),
    ("We ship first, check later.", False, "Sai về chất lượng: không được xuất hàng nghi lỗi."),
    ("Defects is normal.", False, "Sai chia động từ ('are') và coi nhẹ lỗi."),
  ]),
  ("Did the first article pass?", [
    ("Yes, it passed. All dimensions are within spec, so we can start production.", True, "Trả lời + căn cứ + bước tiếp theo."),
    ("Yes, it pass yesterday.", False, "Sai thì: 'It passed.'"),
    ("First article is first product.", False, "Giải thích lại thuật ngữ, không trả lời câu hỏi."),
  ]),
  ("How many samples do you check?", [
    ("Five pieces every hour, following the inspection standard.", True, "Số lượng + tần suất + theo tiêu chuẩn."),
    ("Many samples.", False, "Mơ hồ, không có con số."),
    ("I check sample one hour five.", False, "Dịch từng chữ, sai trật tự: 'five samples every hour'."),
  ]),
 ],
 "listen": [
  ("The yield on Line one is ninety-eight percent", ["yield", "percent"], "tỉ lệ đạt"),
  ("We found a small scratch on the cover", ["scratch", "cover"], "phát hiện lỗi"),
  ("Please hold this lot and do not ship it", ["hold", "ship"], "giữ lô hàng"),
  ("The first article passed inspection this morning", ["article", "inspection"], "kiểm tra hàng đầu"),
  ("QC checked fifty samples from Lot twelve. Three of them had scratches. We will do a full inspection today.", ["samples", "scratches", "full"], "báo kết quả kiểm tra"),
  ("This part is out of spec. The tolerance is plus or minus point one millimetre. Please measure it again.", ["part", "tolerance", "measure"], "hàng ngoài tiêu chuẩn"),
 ],
})

# ───────────────────────── 3. Máy móc, sự cố & bảo trì ─────────────────────────
PHASES.append({
 "title": "Máy móc, sự cố & bảo trì",
 "vocab": [
  ("downtime", "/ˈdaʊntaɪm/", "n", "thời gian dừng máy", "We had 40 minutes of <b>downtime</b> today.", "Hôm nay máy dừng tổng cộng 40 phút."),
  ("breakdown", "/ˈbreɪkdaʊn/", "n", "sự hỏng máy", "Machine 5 had a <b>breakdown</b> this morning.", "Sáng nay máy 5 bị hỏng.", "故障", "koshō"),
  ("maintenance", "/ˈmeɪntənəns/", "n", "bảo trì, bảo dưỡng", "The press is under <b>maintenance</b> until 3 p.m.", "Máy dập đang bảo trì đến 3 giờ chiều.", "保全", "hozen"),
  ("spare part", "/ˌspeə ˈpɑːt/", "n", "phụ tùng thay thế", "We don't have this <b>spare part</b> in stock.", "Trong kho không có phụ tùng này.", "予備品", "yobihin"),
  ("alarm", "/əˈlɑːm/", "n", "báo lỗi, đèn/còi báo động", "The machine stopped with an <b>alarm</b>.", "Máy dừng và báo lỗi."),
  ("sensor", "/ˈsensə/", "n", "cảm biến", "The <b>sensor</b> is dirty, so it can't detect the part.", "Cảm biến bị bẩn nên không nhận được linh kiện."),
  ("overheat", "/ˌəʊvəˈhiːt/", "v", "quá nhiệt, nóng quá mức", "The motor <b>overheated</b> after two hours.", "Mô-tơ bị quá nhiệt sau hai tiếng."),
  ("mold", "/məʊld/", "n", "khuôn (ép, đúc)", "We need to clean the <b>mold</b> every shift.", "Mỗi ca phải vệ sinh khuôn.", "金型", "kanagata"),
  ("vibration", "/vaɪˈbreɪʃn/", "n", "độ rung, sự rung", "There's a strange <b>vibration</b> in the motor.", "Mô-tơ rung bất thường.", "振動", "shindō"),
  ("leak", "/liːk/", "n/v", "sự rò rỉ; rò rỉ", "There's an oil <b>leak</b> under the machine.", "Có dầu rò rỉ dưới gầm máy.", "漏れ", "more"),
 ],
 "phrases": [
  ("Machine 3 stopped at 9:15.", "Máy 3 dừng lúc 9 giờ 15."),
  ("It shows alarm code E12.", "Máy hiện mã lỗi E12."),
  ("The maintenance team is checking it now.", "Tổ bảo trì đang kiểm tra."),
  ("We need to replace the belt.", "Cần thay dây curoa."),
  ("It'll take about one hour to repair.", "Sửa mất khoảng một tiếng."),
  ("We're waiting for a spare part.", "Đang chờ phụ tùng thay thế."),
  ("The machine is running again.", "Máy đã chạy lại."),
  ("Total downtime was 45 minutes.", "Tổng thời gian dừng máy là 45 phút."),
  ("Please don't restart it until I check.", "Đừng khởi động lại cho đến khi tôi kiểm tra."),
  ("We do preventive maintenance every Saturday.", "Thứ Bảy nào cũng bảo trì phòng ngừa."),
 ],
 "dialogues": [
  ("Why did Machine 3 stop?", [
    ("It shows an overheat alarm. The maintenance team is checking the motor now.", True, "Hiện tượng (mã báo lỗi) + ai đang xử lý."),
    ("Machine 3 is broken because it is old.", False, "Đoán nguyên nhân khi chưa kiểm tra — nên báo hiện tượng (mã lỗi) và ai đang xử lý."),
    ("It stop at nine.", False, "Sai thì ('stopped') và chưa trả lời lý do."),
  ]),
  ("How long will it take to repair?", [
    ("About two hours. We have to replace the bearing, and we have one in stock.", True, "Thời gian + việc cần làm + đã có phụ tùng."),
    ("Not long.", False, "Mơ hồ — bên kế hoạch cần con số."),
    ("Two hours maybe, maybe more, I don't know.", False, "Lộn xộn, thiếu chắc chắn; nên đưa một con số ước lượng rõ."),
  ]),
  ("Do we have the spare part?", [
    ("No, we don't. I ordered it this morning, and it'll arrive on Thursday.", True, "Trả lời + đã làm gì + khi nào có."),
    ("No have.", False, "Dịch từng chữ 'không có' — nên nói 'No, we don't have it.'"),
    ("Spare part is expensive.", False, "Không trả lời câu hỏi có hay không."),
  ]),
  ("Can we restart the line now?", [
    ("Not yet. Please wait ten minutes — we need to check the sensor first.", True, "Trả lời + thời gian + lý do."),
    ("Yes, restart, no problem, fast fast.", False, "Vội vàng, bỏ qua bước kiểm tra, nói không rõ ý."),
    ("I am not sure can.", False, "Sai ngữ pháp: 'I'm not sure we can.'"),
  ]),
  ("How much downtime did we have this week?", [
    ("Three hours in total. Most of it was from the mold problem on Tuesday.", True, "Tổng số + nguyên nhân chính."),
    ("Downtime have three hour.", False, "Sai ngữ pháp: 'We had three hours of downtime.'"),
    ("Not so much, the workers are careful.", False, "Mơ hồ và lạc đề."),
  ]),
 ],
 "listen": [
  ("Machine three stopped with an alarm at nine fifteen", ["stopped", "alarm"], "báo máy dừng"),
  ("We are waiting for a spare part", ["waiting", "spare"], "chờ phụ tùng"),
  ("There is an oil leak under the press", ["oil", "leak"], "phát hiện rò rỉ"),
  ("Total downtime today was forty-five minutes", ["downtime", "minutes"], "thời gian dừng máy"),
  ("The motor on Machine five is overheating. We have to stop it for one hour. The maintenance team is on the way.", ["overheating", "hour", "maintenance"], "báo sự cố máy"),
  ("We replaced the sensor and cleaned the mold. The machine is running again. Total downtime was fifty minutes.", ["sensor", "mold", "running"], "báo đã sửa xong"),
 ],
})

# ───────────────────────── 4. 5S & cải tiến (Kaizen) ─────────────────────────
PHASES.append({
 "title": "5S & cải tiến (Kaizen)",
 "vocab": [
  ("sort", "/sɔːt/", "v", "sàng lọc (S1 – Seiri): bỏ thứ không cần", "<b>Sort</b> the tools and remove what you don't use.", "Sàng lọc dụng cụ, bỏ những gì không dùng.", "整理", "seiri"),
  ("set in order", "/ˌset ɪn ˈɔːdə/", "phr", "sắp xếp (S2 – Seiton)", "<b>Set in order</b>: every tool has a fixed place.", "Sắp xếp: mỗi dụng cụ có một chỗ cố định.", "整頓", "seiton"),
  ("shine", "/ʃaɪn/", "v", "sạch sẽ (S3 – Seiso): vệ sinh và kiểm tra", "We <b>shine</b> our area for five minutes before each shift.", "Tổ mình vệ sinh khu vực năm phút trước mỗi ca.", "清掃", "seisō"),
  ("standardize", "/ˈstændədaɪz/", "v", "săn sóc (S4 – Seiketsu): tiêu chuẩn hóa", "Let's <b>standardize</b> the cleaning checklist for all lines.", "Mình chuẩn hóa bảng kiểm vệ sinh cho tất cả các chuyền nhé.", "清潔", "seiketsu"),
  ("sustain", "/səˈsteɪn/", "v", "sẵn sàng (S5 – Shitsuke): duy trì thành thói quen", "5S is easy to start but hard to <b>sustain</b>.", "5S dễ bắt đầu nhưng khó duy trì.", "躾", "shitsuke"),
  ("kaizen", "/ˈkaɪzen/", "n", "cải tiến liên tục", "Each team submits one <b>kaizen</b> idea a month.", "Mỗi tổ nộp một ý tưởng cải tiến mỗi tháng.", "改善", "kaizen"),
  ("waste", "/weɪst/", "n", "lãng phí", "Waiting time is a kind of <b>waste</b>.", "Thời gian chờ đợi là một loại lãng phí.", "無駄", "muda"),
  ("visual management", "/ˌvɪʒuəl ˈmænɪdʒmənt/", "n", "quản lý trực quan", "With <b>visual management</b>, anyone can see the line status.", "Nhờ quản lý trực quan, ai cũng thấy được tình trạng chuyền.", "見える化", "mieruka"),
  ("poka-yoke", "/ˌpəʊkə ˈjəʊkeɪ/", "n", "cơ cấu chống sai lỗi (chống nhầm)", "This <b>poka-yoke</b> stops the part if it's upside down.", "Cơ cấu chống sai này chặn linh kiện nếu bị lắp ngược.", "ポカヨケ", "pokayoke"),
  ("bottleneck", "/ˈbɒtlnek/", "n", "điểm nghẽn, công đoạn cổ chai", "Station 4 is the <b>bottleneck</b> of this line.", "Công đoạn 4 là điểm nghẽn của chuyền này."),
 ],
 "phrases": [
  ("Let's remove everything we don't need.", "Mình bỏ hết những thứ không cần dùng nhé."),
  ("Please put the tools back after use.", "Dùng xong nhớ để dụng cụ về chỗ cũ."),
  ("Every item needs a label and a fixed place.", "Mỗi món đồ cần có nhãn và chỗ để cố định."),
  ("I have a kaizen idea for Station 4.", "Em có một ý tưởng cải tiến cho công đoạn 4."),
  ("This change saves ten seconds per unit.", "Thay đổi này tiết kiệm được mười giây mỗi sản phẩm."),
  ("Workers walk too much here. It's a waste.", "Công nhân phải đi lại nhiều quá ở đây. Đó là lãng phí."),
  ("Before, it took five minutes. Now it takes two.", "Trước đây mất năm phút. Bây giờ chỉ mất hai phút."),
  ("Our 5S score went up to 85 points.", "Điểm 5S của tổ mình tăng lên 85 điểm."),
  ("Let's try it for one week and check the result.", "Mình thử một tuần rồi xem kết quả nhé."),
 ],
 "dialogues": [
  ("Why are these boxes on the floor?", [
    ("Sorry, they're empty boxes from this morning. I'll move them to the recycling area now.", True, "Xin lỗi + giải thích + xử lý ngay theo 5S."),
    ("Not my box.", False, "Đùn đẩy — 5S là trách nhiệm chung của cả khu vực."),
    ("Because no place for put.", False, "Thiếu chủ ngữ/động từ: 'Because there's no place to put them.'"),
  ]),
  ("Do you have any kaizen ideas for this station?", [
    ("Yes. If we move the parts box closer, the operator won't need to walk. We can save about eight seconds.", True, "Ý tưởng + lợi ích có con số."),
    ("Kaizen is very important.", False, "Nói chung chung, không đưa ra ý tưởng nào."),
    ("I think we should work harder.", False, "Kaizen là thay đổi cách làm, không phải bắt người làm vất vả hơn."),
  ]),
  ("What was the result of your kaizen?", [
    ("The cycle time went down from 50 to 42 seconds, and walking time is almost zero.", True, "So sánh trước – sau bằng con số."),
    ("The result very good, everyone happy.", False, "Thiếu 'is', không có số liệu."),
    ("We are change the layout.", False, "Sai ngữ pháp và không nói kết quả: 'We changed the layout.'"),
  ]),
  ("Where do these tools go?", [
    ("On the shadow board next to Station 2. Each tool has its own place.", True, "Chỉ chỗ cụ thể + nguyên tắc sắp xếp."),
    ("Anywhere is OK.", False, "Trái với 5S — dụng cụ phải có chỗ cố định."),
    ("Tools go to there.", False, "Thừa 'to' và mơ hồ: 'They go over there, on the board.'"),
  ]),
  ("Why is Station 4 always slow?", [
    ("It's the bottleneck. Screwing takes 55 seconds there, but the other stations take 40.", True, "Chỉ ra điểm nghẽn + số liệu so sánh."),
    ("Because the girl at Station 4 is slow.", False, "Đổ lỗi cho người — nên tìm nguyên nhân ở quy trình."),
    ("Station 4 slow always.", False, "Thiếu 'is' và sai trật tự: 'Station 4 is always slow.'"),
  ]),
 ],
 "listen": [
  ("Please put the tools back after use", ["tools", "back"], "nhắc 5S"),
  ("Every item needs a label and a fixed place", ["label", "fixed"], "sắp xếp"),
  ("This kaizen saves ten seconds per unit", ["kaizen", "seconds"], "kết quả cải tiến"),
  ("Station four is the bottleneck of this line", ["four", "bottleneck"], "điểm nghẽn"),
  ("Our 5S score this month is eighty points. The main problem is the tool area. Please clean it every Friday.", ["score", "tool", "Friday"], "kết quả chấm 5S"),
  ("Before, operators walked ten metres to get parts. Now the box is next to them. We saved about eight seconds.", ["walked", "box", "eight"], "báo cáo cải tiến"),
 ],
})

# ───────────────────────── 5. Kế hoạch sản xuất & tồn kho ─────────────────────────
PHASES.append({
 "title": "Kế hoạch sản xuất & tồn kho",
 "vocab": [
  ("inventory", "/ˈɪnvəntri/", "n", "tồn kho, hàng tồn", "We keep three days of <b>inventory</b> for this part.", "Mình giữ tồn kho ba ngày cho linh kiện này.", "在庫", "zaiko"),
  ("shortage", "/ˈʃɔːtɪdʒ/", "n", "sự thiếu hụt (vật tư, người)", "There's a <b>shortage</b> of screws on Line 2.", "Chuyền 2 đang thiếu ốc vít.", "欠品", "keppin"),
  ("kanban", "/ˈkɑːnbɑːn/", "n", "thẻ kanban (thẻ báo lấy hàng/làm hàng)", "Put the <b>kanban</b> in the box when it's empty.", "Hết hàng thì bỏ thẻ kanban vào hộp.", "かんばん", "kanban"),
  ("lead time", "/ˈliːd ˌtaɪm/", "n", "thời gian chờ hàng (từ lúc đặt đến lúc nhận)", "The <b>lead time</b> for this material is four weeks.", "Thời gian chờ hàng của vật tư này là bốn tuần.", "リードタイム", "rīdo taimu"),
  ("forecast", "/ˈfɔːkɑːst/", "n", "dự báo (nhu cầu, đơn hàng)", "The customer sent a new <b>forecast</b> for March.", "Khách hàng đã gửi dự báo mới cho tháng Ba.", "内示", "naiji"),
  ("warehouse", "/ˈweəhaʊs/", "n", "kho", "The finished goods are in <b>warehouse</b> B.", "Thành phẩm để ở kho B.", "倉庫", "sōko"),
  ("purchase order", "/ˈpɜːtʃəs ˌɔːdə/", "n", "đơn đặt hàng (PO)", "We received a <b>purchase order</b> for 5,000 units.", "Mình nhận được PO 5.000 sản phẩm.", "注文書", "chūmonsho"),
  ("supplier", "/səˈplaɪə/", "n", "nhà cung cấp", "The <b>supplier</b> will deliver on Friday.", "Nhà cung cấp sẽ giao hàng vào thứ Sáu.", "仕入先", "shiiresaki"),
  ("shipment", "/ˈʃɪpmənt/", "n", "lô hàng xuất, việc xuất hàng", "The next <b>shipment</b> leaves on the 15th.", "Lô hàng tiếp theo xuất ngày 15.", "出荷", "shukka"),
  ("capacity", "/kəˈpæsəti/", "n", "công suất, năng lực sản xuất", "Our <b>capacity</b> is 2,000 units a day.", "Công suất của mình là 2.000 sản phẩm một ngày.", "生産能力", "seisan nōryoku"),
 ],
 "phrases": [
  ("We have enough stock for three days.", "Tồn kho đủ dùng ba ngày."),
  ("We're short of screws for Line 2.", "Chuyền 2 đang thiếu ốc vít."),
  ("The supplier will deliver on Friday morning.", "Nhà cung cấp sẽ giao sáng thứ Sáu."),
  ("Can we move this order up to next week?", "Mình đưa đơn này lên sớm hơn, làm vào tuần sau được không?"),
  ("Our capacity is only 2,000 units a day.", "Công suất của mình chỉ 2.000 sản phẩm một ngày."),
  ("We need overtime on Saturday to meet the shipment date.", "Cần tăng ca thứ Bảy để kịp ngày xuất hàng."),
  ("I'll update the production plan this afternoon.", "Chiều nay tôi sẽ cập nhật kế hoạch sản xuất."),
  ("The shipment is ready and waiting for the truck.", "Hàng đã sẵn sàng, đang chờ xe."),
  ("Please check the stock in the system and on the shelf.", "Kiểm tra tồn kho cả trên hệ thống lẫn trên kệ nhé."),
 ],
 "dialogues": [
  ("Do we have enough material for next week?", [
    ("For most parts, yes. But we only have two days of screws, so I've asked the supplier to deliver early.", True, "Tình trạng + rủi ro + đã làm gì."),
    ("I think enough.", False, "Thiếu chủ ngữ ('I think we have enough') và chưa kiểm tra số liệu."),
    ("Material is in warehouse.", False, "Không trả lời 'đủ hay không', lại thiếu 'the'."),
  ]),
  ("The customer wants 1,000 more units by Friday. Can we do it?", [
    ("It's possible if we run overtime on Wednesday and Thursday. Let me check the materials and get back to you by 3 p.m.", True, "Điều kiện + hành động + hẹn giờ trả lời."),
    ("Yes yes, no problem.", False, "Hứa vội khi chưa kiểm tra công suất và vật tư."),
    ("Cannot, too many.", False, "Thiếu chủ ngữ, cộc lốc, không đưa phương án."),
  ]),
  ("When will the shipment be ready?", [
    ("It'll be packed by Thursday noon, and the truck comes at 3 p.m.", True, "Mốc thời gian rõ cho cả đóng gói và xe."),
    ("Shipment ready soon.", False, "Thiếu 'will be', và 'soon' quá mơ hồ."),
    ("It was ready tomorrow.", False, "Sai thì: 'It will be ready tomorrow.'"),
  ]),
  ("Why is there a shortage of this part?", [
    ("The supplier's delivery was two days late, and our real stock was lower than the system showed.", True, "Nêu hai nguyên nhân cụ thể, có dữ liệu."),
    ("Because warehouse staff don't care.", False, "Đổ lỗi cho người khi chưa có dữ liệu."),
    ("The part is short.", False, "Hiểu nhầm 'short' là 'ngắn' và không nêu lý do."),
  ]),
  ("What's the lead time for this material?", [
    ("Four weeks from the purchase order, so we need to order it by May 5.", True, "Con số + hệ quả cho kế hoạch."),
    ("Lead time is long long.", False, "Mơ hồ, lặp từ kiểu tiếng Việt ('lâu lâu')."),
    ("We will lead it in four weeks.", False, "Dùng sai 'lead' như động từ."),
  ]),
 ],
 "listen": [
  ("We have enough stock for three days", ["stock", "three"], "tồn kho"),
  ("The supplier will deliver on Friday morning", ["supplier", "Friday"], "lịch giao hàng"),
  ("We are short of screws for Line two", ["short", "screws"], "thiếu vật tư"),
  ("Our capacity is two thousand units a day", ["capacity", "thousand"], "công suất"),
  ("The customer increased the order by one thousand units. We need overtime on Saturday. I will update the plan today.", ["increased", "overtime", "plan"], "thay đổi kế hoạch"),
  ("The shipment for Korea is packed. The truck will come at three this afternoon. Please prepare the documents.", ["Korea", "truck", "documents"], "chuẩn bị xuất hàng"),
 ],
})

# ───────────────────────── 6. Báo cáo lỗi & phân tích nguyên nhân ─────────────────────────
PHASES.append({
 "title": "Báo cáo lỗi & phân tích nguyên nhân",
 "vocab": [
  ("root cause", "/ˌruːt ˈkɔːz/", "n", "nguyên nhân gốc", "We need to find the <b>root cause</b>, not just repair the part.", "Mình cần tìm nguyên nhân gốc, không chỉ sửa linh kiện.", "真因", "shin'in"),
  ("5 Whys", "/ˌfaɪv ˈwaɪz/", "n", "phương pháp 5 lần hỏi 'tại sao'", "Let's use the <b>5 Whys</b> to find the real reason.", "Mình dùng phương pháp 5 tại sao để tìm lý do thật.", "なぜなぜ分析", "naze naze bunseki"),
  ("corrective action", "/kəˈrektɪv ˈækʃn/", "n", "hành động khắc phục", "Please send the <b>corrective action</b> plan by Friday.", "Vui lòng gửi kế hoạch khắc phục trước thứ Sáu.", "是正処置", "zesei shochi"),
  ("countermeasure", "/ˈkaʊntəmeʒə/", "n", "đối sách, biện pháp xử lý", "Our <b>countermeasure</b> is a new jig at Station 3.", "Đối sách của tụi mình là đồ gá mới ở công đoạn 3.", "対策", "taisaku"),
  ("occur", "/əˈkɜː/", "v", "xảy ra, phát sinh", "The defect <b>occurred</b> on the night shift.", "Lỗi phát sinh ở ca đêm.", "発生する", "hassei suru"),
  ("containment", "/kənˈteɪnmənt/", "n", "khoanh vùng, cách ly hàng nghi lỗi", "Our <b>containment</b> action is to check all stock in the warehouse.", "Hành động khoanh vùng là kiểm tra toàn bộ hàng trong kho."),
  ("recurrence", "/rɪˈkʌrəns/", "n", "sự tái phát", "This countermeasure will stop <b>recurrence</b>.", "Đối sách này sẽ ngăn lỗi tái phát.", "再発", "saihatsu"),
  ("customer claim", "/ˈkʌstəmə ˌkleɪm/", "n", "khiếu nại chất lượng của khách hàng", "We got a <b>customer claim</b> about loose screws.", "Tụi mình nhận khiếu nại của khách về ốc bị lỏng.", "クレーム", "kurēmu"),
  ("fishbone diagram", "/ˈfɪʃbəʊn ˌdaɪəɡræm/", "n", "biểu đồ xương cá", "We drew a <b>fishbone diagram</b> with the team.", "Tụi mình cùng cả tổ vẽ biểu đồ xương cá.", "特性要因図", "tokusei yōinzu"),
  ("trace", "/treɪs/", "v", "truy vết, truy xuất", "We can <b>trace</b> the lot by its date code.", "Mình có thể truy vết lô hàng bằng mã ngày."),
 ],
 "phrases": [
  ("The defect occurred on May 10 on the night shift.", "Lỗi phát sinh ngày 10/5 ở ca đêm."),
  ("We found 25 NG pieces out of 1,000.", "Tụi mình phát hiện 25 cái NG trên 1.000 cái."),
  ("We've already separated all the suspect parts.", "Tụi mình đã tách riêng toàn bộ hàng nghi lỗi."),
  ("Why did it happen? Let's ask why again.", "Tại sao lại xảy ra? Mình hỏi 'tại sao' tiếp nhé."),
  ("The root cause is a worn jig.", "Nguyên nhân gốc là đồ gá bị mòn."),
  ("The operator didn't know the new standard.", "Công nhân chưa biết tiêu chuẩn mới."),
  ("As a countermeasure, we added a sensor.", "Đối sách là tụi mình đã lắp thêm cảm biến."),
  ("We'll check the result for two weeks.", "Tụi mình sẽ theo dõi kết quả trong hai tuần."),
  ("Let's focus on the process, not the person.", "Mình tập trung vào quy trình, không phải con người."),
 ],
 "dialogues": [
  ("What happened with Lot 45?", [
    ("We found loose screws in 12 pieces. It occurred on the night shift on Monday, and we've held the whole lot.", True, "Hiện tượng + số lượng + thời điểm + đã khoanh vùng."),
    ("Lot 45 have problem.", False, "Sai chia động từ ('has') và quá mơ hồ."),
    ("The night shift worker is careless.", False, "Đổ lỗi cho người trước khi phân tích nguyên nhân."),
  ]),
  ("What's the root cause?", [
    ("The screwdriver torque was set too low after maintenance, and nobody checked it at the start of the shift.", True, "Nguyên nhân kỹ thuật + lỗ hổng trong quy trình."),
    ("Root cause is mistake of worker.", False, "Dịch từng chữ và dừng ở 'lỗi con người' — phải hỏi tiếp 'tại sao'."),
    ("We don't know, maybe many reasons.", False, "Bỏ ngỏ — nên nói 'We're still analyzing. I'll update you by…'."),
  ]),
  ("What's your containment action?", [
    ("We're checking all the stock in our warehouse and at the customer. So far, 30 pieces are NG.", True, "Phạm vi khoanh vùng + kết quả tạm thời."),
    ("We will fix it next month.", False, "Khoanh vùng phải làm ngay, không phải tháng sau."),
    ("Containment is OK.", False, "Không nói cụ thể đã làm gì."),
  ]),
  ("How will you prevent recurrence?", [
    ("We'll add a torque check to the start-up checklist and train all operators this week.", True, "Đối sách cụ thể + đào tạo + thời hạn."),
    ("We will tell workers be careful.", False, "Sai ngữ pháp ('to be careful') và đối sách yếu — nhắc nhở không ngăn được tái phát."),
    ("It don't happen again.", False, "Sai ngữ pháp ('It won't happen') và chỉ là lời hứa suông."),
  ]),
  ("When can you send the corrective action report?", [
    ("We'll send the first version by Wednesday and the final one after two weeks of checking.", True, "Mốc thời gian rõ cho bản đầu và bản cuối."),
    ("Soon, we are busy now.", False, "Mơ hồ và nghe như không coi trọng khách hàng."),
    ("We send when finish.", False, "Thiếu thì tương lai và chủ ngữ, không có ngày: 'We'll send it by Wednesday.'"),
  ]),
 ],
 "listen": [
  ("The defect occurred on the night shift", ["defect", "night"], "thời điểm phát sinh lỗi"),
  ("We have separated all the suspect parts", ["separated", "suspect"], "khoanh vùng"),
  ("The root cause is a worn jig", ["root", "jig"], "nguyên nhân gốc"),
  ("Let's ask why five times", ["why", "five"], "5 tại sao"),
  ("We received a customer claim about loose screws. We checked the warehouse and found thirty bad pieces. All of them are on hold.", ["claim", "warehouse", "hold"], "báo khiếu nại khách hàng"),
  ("The torque was too low after maintenance. We added a check to the start-up list. We will watch the result for two weeks.", ["torque", "check", "weeks"], "báo đối sách"),
 ],
})

# ───────────────────────── 7. Làm việc với chuyên gia nước ngoài ─────────────────────────
PHASES.append({
 "title": "Làm việc với chuyên gia nước ngoài",
 "vocab": [
  ("expert", "/ˈekspɜːt/", "n", "chuyên gia", "An <b>expert</b> from Japan will visit Line 3 next week.", "Tuần sau một chuyên gia từ Nhật sẽ xuống chuyền 3."),
  ("interpreter", "/ɪnˈtɜːprɪtə/", "n", "phiên dịch viên", "Can we talk without an <b>interpreter</b>?", "Mình nói chuyện không cần phiên dịch được không?", "通訳", "tsūyaku"),
  ("drawing", "/ˈdrɔːɪŋ/", "n", "bản vẽ (kỹ thuật)", "Please check the size on the <b>drawing</b>.", "Vui lòng kiểm tra kích thước trên bản vẽ.", "図面", "zumen"),
  ("requirement", "/rɪˈkwaɪəmənt/", "n", "yêu cầu", "The customer has a new <b>requirement</b> for packing.", "Khách hàng có yêu cầu mới về đóng gói.", "要求", "yōkyū"),
  ("feedback", "/ˈfiːdbæk/", "n", "nhận xét, góp ý", "Thank you for your <b>feedback</b> on our line.", "Cảm ơn anh đã góp ý về chuyền của chúng tôi."),
  ("demonstrate", "/ˈdemənstreɪt/", "v", "làm mẫu, trình diễn", "Could you <b>demonstrate</b> the new method?", "Anh làm mẫu cách làm mới được không?"),
  ("sign off", "/ˌsaɪn ˈɒf/", "phr v", "ký duyệt, chấp thuận", "The expert has to <b>sign off</b> on the new process.", "Chuyên gia phải ký duyệt quy trình mới."),
  ("consult", "/kənˈsʌlt/", "v", "hỏi ý kiến, bàn bạc", "Please <b>consult</b> me before you change anything.", "Trước khi thay đổi gì thì hỏi ý kiến tôi nhé.", "相談する", "sōdan suru"),
  ("shop floor", "/ˌʃɒp ˈflɔː/", "n", "xưởng, hiện trường sản xuất", "Let's go to the <b>shop floor</b> and see the problem.", "Mình xuống xưởng xem vấn đề tận nơi nhé.", "現場", "genba"),
  ("trial run", "/ˌtraɪəl ˈrʌn/", "n", "chạy thử", "We'll do a <b>trial run</b> with 50 pieces.", "Tụi mình sẽ chạy thử 50 sản phẩm."),
 ],
 "phrases": [
  ("Could you speak a little more slowly, please?", "Anh nói chậm hơn một chút được không ạ?"),
  ("Just to check — you want us to change the jig, right?", "Để xác nhận lại, anh muốn tụi em thay đồ gá, đúng không ạ?"),
  ("Could you show me on the drawing?", "Anh chỉ giúp em trên bản vẽ được không?"),
  ("Let me check with my manager and get back to you.", "Để em hỏi lại quản lý rồi báo anh."),
  ("Could you write down the number for me?", "Anh ghi giúp em con số đó được không?"),
  ("Let's go to the line and look at it together.", "Mình xuống chuyền cùng xem nhé."),
  ("Thank you for your advice. We'll try it tomorrow.", "Cảm ơn lời khuyên của anh. Mai tụi em sẽ thử."),
  ("In our factory, we usually do it this way because…", "Ở nhà máy mình, tụi em thường làm cách này vì…"),
  ("Sorry, I don't fully understand. Do you mean the upper part?", "Xin lỗi, em chưa hiểu hết. Ý anh là phần phía trên phải không?"),
 ],
 "dialogues": [
  ("Please change the pressure to 0.5 megapascals.", [
    ("Just to check — 0.5 megapascals for all three machines, right?", True, "Nhắc lại con số để xác nhận — rất quan trọng với thông số máy."),
    ("Yes, yes.", False, "Nói 'yes' khi chưa chắc đã hiểu — lỗi rất hay gặp, dễ dẫn đến sai sót."),
    ("OK, I change pressure.", False, "Thiếu 'will'/'the' và không xác nhận lại con số."),
  ]),
  ("Why do you do it this way?", [
    ("Because the SOP says so. But if you have a better method, we'd like to learn.", True, "Giải thích + cởi mở học hỏi."),
    ("We always do like this.", False, "Thiếu 'it' và không phải lý do — chuyên gia muốn biết 'tại sao'."),
    ("Is not my decision.", False, "Thiếu chủ ngữ ('It's') và đùn đẩy."),
  ]),
  ("Do you have any questions about the new method?", [
    ("Yes, one question. What should we do if the part is a little bent?", True, "Hỏi lại cụ thể thay vì im lặng."),
    ("No question, I understand all.", False, "Nói hiểu hết dù chưa chắc — nên hỏi lại điểm chưa rõ."),
    ("What is method?", False, "Thiếu 'the' và câu hỏi quá chung — nên chỉ rõ phần chưa hiểu."),
  ]),
  ("I think Station 3 needs a new jig.", [
    ("I agree. Could you show me your idea on the drawing? Then I'll ask maintenance to make it.", True, "Đồng ý + hỏi chi tiết + bước tiếp theo."),
    ("New jig is expensive, cannot.", False, "Từ chối cộc lốc, thiếu chủ ngữ; nên nêu lo ngại một cách lịch sự."),
    ("You are right always.", False, "Sai trật tự từ ('always right') và chỉ chiều ý, không góp ý kiến."),
  ]),
  ("Can we change the process today?", [
    ("I'm afraid we need approval first. Let me consult my manager and get back to you after lunch.", True, "Từ chối khéo + lý do + hẹn giờ trả lời."),
    ("No, cannot change.", False, "Cộc lốc, thiếu chủ ngữ và lý do."),
    ("Yes, we change now, no need to ask.", False, "Đổi quy trình khi chưa được duyệt — rủi ro chất lượng."),
  ]),
 ],
 "listen": [
  ("Could you speak a little more slowly please", ["speak", "slowly"], "nhờ nói chậm"),
  ("Let's go to the shop floor and see", ["shop", "floor"], "xuống hiện trường"),
  ("Please show me the size on the drawing", ["size", "drawing"], "hỏi bản vẽ"),
  ("We will do a trial run with fifty pieces", ["trial", "fifty"], "chạy thử"),
  ("Tomorrow our expert Tanaka will visit Line three. He wants to see the new jig. Please prepare the drawing and the data.", ["visit", "jig", "data"], "chuẩn bị đón chuyên gia"),
  ("Thank you for your advice. We tried the new method this morning. The cycle time went down by five seconds.", ["advice", "method", "five"], "báo kết quả cho chuyên gia"),
 ],
})

# ───────────────────────── 8. Audit & khách hàng thăm nhà máy ─────────────────────────
PHASES.append({
 "title": "Audit & khách hàng thăm nhà máy",
 "vocab": [
  ("audit", "/ˈɔːdɪt/", "n/v", "đánh giá (audit)", "The customer <b>audit</b> is next Tuesday.", "Buổi audit của khách hàng là thứ Ba tuần sau.", "監査", "kansa"),
  ("auditor", "/ˈɔːdɪtə/", "n", "chuyên gia đánh giá", "The <b>auditor</b> wants to see the training records.", "Chuyên gia đánh giá muốn xem hồ sơ đào tạo.", "監査員", "kansain"),
  ("nonconformity", "/ˌnɒnkənˈfɔːməti/", "n", "điểm không phù hợp", "The audit found two minor <b>nonconformities</b>.", "Buổi audit phát hiện hai điểm không phù hợp nhẹ.", "不適合", "futekigō"),
  ("evidence", "/ˈevɪdəns/", "n", "bằng chứng", "Can you show me <b>evidence</b> of the daily check?", "Anh cho tôi xem bằng chứng của việc kiểm tra hằng ngày được không?"),
  ("record", "/ˈrekɔːd/", "n", "hồ sơ, bản ghi", "We keep inspection <b>records</b> for three years.", "Tụi mình lưu hồ sơ kiểm tra ba năm.", "記録", "kiroku"),
  ("certificate", "/səˈtɪfɪkət/", "n", "giấy chứng nhận", "Our ISO 9001 <b>certificate</b> is valid until 2027.", "Chứng nhận ISO 9001 của mình còn hiệu lực đến năm 2027."),
  ("visitor badge", "/ˈvɪzɪtə ˌbædʒ/", "n", "thẻ khách", "Please wear your <b>visitor badge</b> at all times.", "Vui lòng đeo thẻ khách suốt thời gian ở nhà máy."),
  ("factory tour", "/ˈfæktri ˌtʊə/", "n", "chuyến tham quan nhà máy", "The <b>factory tour</b> takes about 40 minutes.", "Chuyến tham quan nhà máy mất khoảng 40 phút."),
  ("compliance", "/kəmˈplaɪəns/", "n", "sự tuân thủ (quy định, luật)", "The audit checks <b>compliance</b> with labour laws.", "Buổi audit kiểm tra việc tuân thủ luật lao động."),
  ("calibration", "/ˌkælɪˈbreɪʃn/", "n", "hiệu chuẩn (thiết bị đo)", "This gauge is due for <b>calibration</b> next month.", "Thước đo này đến hạn hiệu chuẩn vào tháng sau.", "校正", "kōsei"),
 ],
 "phrases": [
  ("Welcome to our factory. I'll show you around.", "Chào mừng quý khách đến nhà máy. Tôi sẽ dẫn quý khách đi tham quan."),
  ("Please wear this visitor badge and safety shoes.", "Vui lòng đeo thẻ khách và mang giày bảo hộ."),
  ("Please don't take photos in this area.", "Vui lòng không chụp ảnh ở khu vực này."),
  ("This is our final inspection area.", "Đây là khu vực kiểm tra cuối (OQC)."),
  ("Here is the record for last month.", "Đây là hồ sơ của tháng trước."),
  ("Let me find that document. One moment, please.", "Để tôi tìm tài liệu đó. Xin chờ một chút."),
  ("We'll send you the corrective action report within two weeks.", "Chúng tôi sẽ gửi báo cáo hành động khắc phục trong vòng hai tuần."),
  ("All our gauges are calibrated every year.", "Tất cả thiết bị đo đều được hiệu chuẩn hằng năm."),
  ("Do you have any questions before we go to the line?", "Quý khách có câu hỏi gì trước khi mình xuống chuyền không ạ?"),
 ],
 "dialogues": [
  ("Can I see the training records for this operator?", [
    ("Of course. Here's her training record and her skill certificate for this station.", True, "Đồng ý + đưa đúng hồ sơ được hỏi."),
    ("Records is in office, very far.", False, "Sai chia động từ ('are') và có vẻ né tránh."),
    ("She is very good, no need to check.", False, "Không đưa bằng chứng — auditor cần hồ sơ, không cần lời khen."),
  ]),
  ("This gauge has no calibration label.", [
    ("You're right, thank you. I'll stop using it now and check the calibration record.", True, "Thừa nhận + ngừng dùng + kiểm tra hồ sơ."),
    ("It is OK, the gauge is new.", False, "Bào chữa — thiết bị mới cũng phải có nhãn hiệu chuẩn."),
    ("Label lost maybe.", False, "Thiếu chủ ngữ/động từ, đoán mò."),
  ]),
  ("How do you control NG parts?", [
    ("We put them in the red box, label them and record them. QC decides what to do within 24 hours.", True, "Quy trình rõ theo từng bước + thời hạn."),
    ("We throw away.", False, "Thiếu tân ngữ ('throw them away') và không có kiểm soát, hồ sơ."),
    ("We don't have NG parts.", False, "Không thực tế và không trả lời câu hỏi về quy trình."),
  ]),
  ("Can I take a photo of this machine?", [
    ("I'm sorry, photos aren't allowed in this area. I can send you an approved picture later.", True, "Từ chối lịch sự + phương án thay thế."),
    ("No photo!", False, "Quá cộc với khách hàng."),
    ("Yes, take many.", False, "Vi phạm quy định bảo mật của nhà máy."),
  ]),
  ("We found one minor nonconformity in the warehouse.", [
    ("Thank you for pointing it out. Could you explain the details? We'll send a corrective action plan by Friday.", True, "Cảm ơn + hỏi chi tiết + cam kết thời hạn."),
    ("It is only minor, not important.", False, "Xem nhẹ phát hiện của auditor — gây ấn tượng xấu."),
    ("Warehouse team fault, not QC.", False, "Đổ lỗi cho bộ phận khác, thiếu động từ."),
  ]),
 ],
 "listen": [
  ("Please wear this visitor badge at all times", ["visitor", "badge"], "đón khách"),
  ("The customer audit is next Tuesday", ["audit", "Tuesday"], "lịch audit"),
  ("Here is the calibration record for this gauge", ["calibration", "gauge"], "đưa hồ sơ"),
  ("Please don't take photos in this area", ["photos", "area"], "quy định chụp ảnh"),
  ("Welcome to our factory. First, we'll visit the assembly line. After that, we'll go to the final inspection area.", ["factory", "assembly", "inspection"], "dẫn khách tham quan"),
  ("The audit found two minor nonconformities. One was in the warehouse. We will send the corrective action plan by Friday.", ["minor", "warehouse", "Friday"], "tổng kết audit"),
 ],
})

# ───────────────────────── 9. Đào tạo & hướng dẫn công nhân ─────────────────────────
PHASES.append({
 "title": "Đào tạo & hướng dẫn công nhân",
 "vocab": [
  ("trainee", "/ˌtreɪˈniː/", "n", "học viên, người học việc", "Each <b>trainee</b> works with a senior operator.", "Mỗi học viên làm cùng một công nhân lâu năm.", "研修生", "kenshūsei"),
  ("operator", "/ˈɒpəreɪtə/", "n", "công nhân vận hành, người đứng máy", "This station needs two <b>operators</b>.", "Công đoạn này cần hai công nhân.", "作業者", "sagyōsha"),
  ("on-the-job training", "/ˌɒn ðə ˈdʒɒb ˈtreɪnɪŋ/", "n", "đào tạo tại chỗ (OJT)", "New workers get two weeks of <b>on-the-job training</b>.", "Công nhân mới được đào tạo tại chỗ hai tuần."),
  ("skill matrix", "/ˈskɪl ˌmeɪtrɪks/", "n", "bảng ma trận kỹ năng", "The <b>skill matrix</b> shows who can work at each station.", "Bảng ma trận kỹ năng cho biết ai làm được ở từng công đoạn.", "星取表", "hoshitorihyō"),
  ("certify", "/ˈsɜːtɪfaɪ/", "v", "công nhận (tay nghề), cấp chứng nhận", "Lan was <b>certified</b> for soldering last week.", "Tuần trước Lan được công nhận tay nghề hàn thiếc."),
  ("step by step", "/ˌstep baɪ ˈstep/", "adv", "từng bước một", "I'll show you <b>step by step</b>.", "Tôi sẽ chỉ cho bạn từng bước."),
  ("key point", "/ˌkiː ˈpɔɪnt/", "n", "điểm mấu chốt (của thao tác)", "The <b>key point</b> is to hold the part with two hands.", "Điểm mấu chốt là giữ linh kiện bằng hai tay.", "急所", "kyūsho"),
  ("multi-skilled worker", "/ˌmʌltiˈskɪld ˈwɜːkə/", "n", "công nhân đa kỹ năng", "We need more <b>multi-skilled workers</b> for the night shift.", "Ca đêm cần thêm công nhân đa kỹ năng.", "多能工", "tanōkō"),
  ("observe", "/əbˈzɜːv/", "v", "quan sát", "First, <b>observe</b> me, then try it yourself.", "Đầu tiên bạn quan sát tôi, sau đó tự làm thử."),
  ("practice", "/ˈpræktɪs/", "v/n", "luyện tập, thực hành", "Please <b>practice</b> on the sample parts first.", "Hãy thực hành trên linh kiện mẫu trước."),
 ],
 "phrases": [
  ("Watch me first. Then you try.", "Xem tôi làm trước. Sau đó bạn làm thử."),
  ("Hold the part like this, with both hands.", "Cầm linh kiện như thế này, bằng cả hai tay."),
  ("This is the key point: check the direction.", "Đây là điểm mấu chốt: kiểm tra chiều lắp."),
  ("Can you show me how you do it?", "Bạn làm thử cho tôi xem được không?"),
  ("Good job. Just a little slower here.", "Tốt lắm. Chỗ này làm chậm lại một chút."),
  ("If you're not sure, stop and call me.", "Nếu không chắc thì dừng lại và gọi tôi."),
  ("Do you have any questions so far?", "Đến đây bạn có câu hỏi gì không?"),
  ("Tomorrow you'll work at this station on your own.", "Ngày mai bạn sẽ tự làm ở công đoạn này."),
  ("She passed the skill test for Station 5.", "Cô ấy đã đạt bài kiểm tra tay nghề công đoạn 5."),
 ],
 "dialogues": [
  ("I'm new here. What should I do first?", [
    ("Welcome! First, read the SOP with me. Then watch me for one hour before you try.", True, "Chào đón + các bước rõ ràng, có thứ tự."),
    ("You just do same other people.", False, "Thiếu 'the … as' và hướng dẫn mơ hồ — người mới cần từng bước cụ thể."),
    ("Very easy, no need to learn.", False, "Coi nhẹ đào tạo — dễ gây lỗi và tai nạn."),
  ]),
  ("Am I doing it right?", [
    ("Almost. Just turn the part the other way — the arrow must face up.", True, "Nhận xét + chỉ lỗi cụ thể + cách làm đúng."),
    ("No, wrong, do again.", False, "Cộc lốc, không nói sai ở đâu."),
    ("You are doing wrong always.", False, "Sai trật tự từ và làm người học mất tự tin."),
  ]),
  ("How long does it take to train a new operator?", [
    ("About two weeks. After that, we test their skill and update the skill matrix.", True, "Thời gian + bước đánh giá sau đào tạo."),
    ("It take long time.", False, "Thiếu 's' và 'a' ('It takes a long time'), lại không có con số."),
    ("Depends person maybe.", False, "Thiếu 'It' và 'on' ('It depends on the person'), lại mơ hồ; nên nêu thời gian tiêu chuẩn trước."),
  ]),
  ("Who can work at Station 5 tomorrow?", [
    ("Hà and Tuấn. They're both certified for Station 5 on the skill matrix.", True, "Tên cụ thể + căn cứ trên ma trận kỹ năng."),
    ("Anyone can, it's easy.", False, "Không kiểm tra tay nghề — rủi ro chất lượng."),
    ("Hà can work maybe, I think.", False, "Thiếu chắc chắn; nên xem bảng kỹ năng rồi trả lời."),
  ]),
  ("The trainee made three defects this morning.", [
    ("Thanks for telling me. I'll watch her work this afternoon and explain the key point again.", True, "Nhận thông tin + hành động hỗ trợ cụ thể."),
    ("She is not smart.", False, "Đổ lỗi, xúc phạm — vấn đề thường nằm ở cách hướng dẫn."),
    ("New people make defect is normal.", False, "Sai ngữ pháp và coi nhẹ lỗi."),
  ]),
 ],
 "listen": [
  ("Watch me first and then you try", ["Watch", "try"], "hướng dẫn thao tác"),
  ("The key point is to check the direction", ["key", "direction"], "điểm mấu chốt"),
  ("If you are not sure, stop and call me", ["sure", "call"], "nhắc người mới"),
  ("She passed the skill test for Station five", ["passed", "skill"], "đánh giá tay nghề"),
  ("Today you will learn the job at Station two. First, read the SOP with me. Then practice on ten sample parts.", ["learn", "read", "practice"], "buổi đào tạo đầu tiên"),
  ("Good job, Hùng. Your speed is fine now. Tomorrow you will work on your own.", ["speed", "Tomorrow", "own"], "khen và giao việc cho học viên"),
 ],
})

# ───────────────────────── Vai trong ngành ─────────────────────────
ROLES = {
 "qc": {"label": "QA / QC", "emoji": "🔍",
  "scenarios": [
   ("qc_ng", "Báo lỗi cho tổ trưởng", "You are a line leader. I am QC and I found a defect trend on your line this morning. Ask what the defect is, how many pieces are affected and what you should do now."),
   ("qc_customer", "Nghe khách báo lỗi", "You are a foreign customer's quality engineer. You call about bad parts you received. Ask about the lot, the quantity and when we will reply."),
   ("qc_fai", "Duyệt hàng đầu", "You are a production engineer. You need QC approval for the first article so the line can start. Ask me for the result and push a little because you are in a hurry."),
   ("qc_audit", "Trả lời auditor", "You are an auditor checking our inspection process. Ask about sampling, records and what happens to NG parts."),
  ],
  "dialogues": [
   ("Can we ship Lot 18 today?", [
     ("Not yet. We found two scratches in the samples, so we're checking 100 percent. I'll tell you by 4 p.m.", True, "Trả lời + lý do + mốc thời gian."),
     ("Maybe can, maybe cannot.", False, "Mơ hồ, thiếu chủ ngữ — bộ phận khác cần câu trả lời rõ."),
     ("You always want to ship fast.", False, "Trách móc người hỏi thay vì trả lời.")]),
   ("What's the defect rate this week?", [
     ("It's 1.2 percent, down from 1.8 last week. Scratches are still the top defect.", True, "Con số + so sánh + lỗi chính."),
     ("Defect rate is down little.", False, "Thiếu con số và thiếu 'a' ('down a little')."),
     ("I not calculate yet.", False, "Sai ngữ pháp: 'I haven't calculated it yet.'")]),
   ("The line leader says the part is OK. Why did you reject it?", [
     ("The height is 10.12 millimetres, and the spec is 10.00 plus or minus 0.05. I can show you the data.", True, "Căn cứ bằng số đo và tiêu chuẩn, bình tĩnh."),
     ("Because I am QC, I decide.", False, "Dùng quyền thay vì dữ liệu — dễ gây mâu thuẫn."),
     ("The line leader is wrong always.", False, "Sai trật tự từ ('always wrong') và công kích cá nhân.")]),
   ("Did you check the first article?", [
     ("Yes. All dimensions are OK, and the appearance is fine. You can start mass production.", True, "Kết quả + cho phép bước tiếp theo."),
     ("Yes, I checked it tomorrow.", False, "Sai thời gian: đã kiểm tra thì dùng 'this morning', không phải 'tomorrow'."),
     ("First article checking.", False, "Thiếu chủ ngữ/động từ — không rõ đã xong chưa.")]),
   ("How do you know which lot has the problem?", [
     ("We traced it by the date code on the label. All the bad pieces are from the night shift on May 3.", True, "Cách truy vết + kết quả cụ thể."),
     ("We know by feeling.", False, "Không có căn cứ — QC phải truy vết bằng dữ liệu."),
     ("Lot is on the label.", False, "Thiếu mạo từ và chưa trả lời lô nào có vấn đề.")]),
   ("Can you send me the inspection data?", [
     ("Sure. I'll email you the spreadsheet with all the measurements in ten minutes.", True, "Đồng ý + hình thức gửi + thời gian."),
     ("OK, I send.", False, "Thiếu 'will' và 'it': 'OK, I'll send it.'"),
     ("Data is secret.", False, "Cộc lốc và không hợp lý với người cần dữ liệu để xử lý.")]),
  ]},
 "engineer": {"label": "Kỹ sư sản xuất · Bảo trì", "emoji": "🔧",
  "scenarios": [
   ("en_down", "Báo máy dừng cho quản lý", "You are the production manager. I am the maintenance engineer. A machine stopped 30 minutes ago. Ask about the cause, the repair time and the spare parts."),
   ("en_expert", "Làm việc với chuyên gia Nhật", "You are a Japanese engineer who wants to change a machine setting. I need to understand your reason and the risk. Speak simply and answer my questions."),
   ("en_trial", "Báo kết quả chạy thử", "You are my manager. I did a trial run with a new jig. Ask about the cycle time, the quality result and whether we can use it on all lines."),
   ("en_vendor", "Gọi hãng máy hỗ trợ", "You are a service engineer from a foreign machine maker. I call because our machine shows an error code. Ask me for details and give simple steps to check."),
  ],
  "dialogues": [
   ("The press is making a strange noise. What's wrong?", [
     ("I think the bearing is worn. Let's stop the press now so I can check it safely.", True, "Nhận định có căn cứ + ưu tiên an toàn."),
     ("Is normal, old machine.", False, "Thiếu 'It' và bỏ qua dấu hiệu bất thường."),
     ("I don't know, ask maintenance.", False, "Đùn đẩy — kỹ sư nên kiểm tra hoặc cùng phối hợp.")]),
   ("When will Machine 2 be ready?", [
     ("By 2 p.m. We're replacing the motor now, and then we'll do a trial run.", True, "Giờ cụ thể + đang làm gì + bước kiểm tra."),
     ("It ready afternoon.", False, "Thiếu 'will be … in the' và không có giờ cụ thể."),
     ("When the part come.", False, "Câu cụt, thiếu 's' ('comes') và không có mốc thời gian.")]),
   ("Why do we need to stop the line on Saturday?", [
     ("For preventive maintenance. It stops breakdowns during the week, so we lose less time overall.", True, "Lý do + lợi ích rõ ràng."),
     ("Because the plan says.", False, "Câu thiếu ('the plan says so') và chưa giải thích lợi ích — người hỏi muốn biết 'để làm gì'."),
     ("Saturday is maintenance day, that's all.", False, "Cộc lốc, không thuyết phục.")]),
   ("Can the new jig reduce cycle time?", [
     ("Yes. In the trial run, it went down from 48 to 41 seconds, with no defects.", True, "Kết quả chạy thử bằng số + chất lượng."),
     ("Yes, it very fast.", False, "Thiếu động từ ('it's much faster') và không có số liệu."),
     ("I hope it can reduce.", False, "Chỉ là mong đợi, không có dữ liệu.")]),
   ("The alarm code is E-45. What does it mean?", [
     ("It means low air pressure. Please check the air valve behind the machine.", True, "Giải thích + hướng dẫn kiểm tra cụ thể."),
     ("E-45 is alarm.", False, "Nhắc lại câu hỏi, không giải thích gì."),
     ("Mean machine broken.", False, "Thiếu chủ ngữ/động từ, kết luận vội.")]),
   ("Did you change the machine setting yesterday?", [
     ("Yes, I changed the speed from 80 to 70 percent. I wrote it in the change record.", True, "Xác nhận + thông số cụ thể + có ghi hồ sơ."),
     ("Yes, I change a little.", False, "Sai thì ('changed') và không nói thông số."),
     ("No, maybe someone else.", False, "Né tránh, không kiểm tra hồ sơ.")]),
  ]},
 "leader": {"label": "Tổ trưởng · Giám sát", "emoji": "👷",
  "scenarios": [
   ("ld_meeting", "Họp đầu ca", "You are a foreign production manager joining my morning line meeting. Ask about today's target, the number of workers and today's safety point."),
   ("ld_behind", "Báo chậm tiến độ", "You are the production manager. My line is 150 units behind target at noon. Ask why and what my plan is to recover."),
   ("ld_worker", "Nhắc nhở công nhân", "You are an operator who is not wearing safety glasses. I am your line leader. At first give an excuse, then agree to follow the rule."),
   ("ld_kaizen", "Đề xuất cải tiến", "You are the factory manager. I have a kaizen idea for my line. Ask about the problem, the cost and the expected result."),
  ],
  "dialogues": [
   ("How many workers do you have today?", [
     ("Twenty-eight out of thirty. Two are on sick leave, so I've moved one person from Line 4.", True, "Số liệu + lý do + cách xử lý."),
     ("Today have 28 people.", False, "Thiếu chủ ngữ: 'We have 28 people today.'"),
     ("Not enough, very difficult.", False, "Than phiền, không có số liệu hay giải pháp.")]),
   ("Your line is behind target. What happened?", [
     ("We lost 40 minutes on the changeover this morning. We'll recover it with 30 minutes of overtime.", True, "Nguyên nhân + phương án bù sản lượng."),
     ("Workers is slow today.", False, "Sai chia động từ ('are') và đổ lỗi cho công nhân."),
     ("I don't know why.", False, "Tổ trưởng cần nắm và báo được nguyên nhân.")]),
   ("Why isn't this worker wearing gloves?", [
     ("Sorry, I'll talk to him now. I'll also check PPE at the start of every shift.", True, "Nhận trách nhiệm + xử lý ngay + phòng ngừa."),
     ("He forget, not my fault.", False, "Sai thì ('forgot') và đổ lỗi."),
     ("Gloves are finish.", False, "Sai ngữ pháp ('We've run out of gloves') — nếu hết thì phải báo ngay.")]),
   ("Can your line make 200 more units today?", [
     ("We can make 120 more with one hour of overtime. For 200, I'd need two more workers.", True, "Đưa con số khả thi + điều kiện."),
     ("OK, try my best.", False, "Hứa chung chung, thiếu chủ ngữ, không có con số."),
     ("No, impossible.", False, "Từ chối ngay, không đưa phương án.")]),
   ("What's today's safety point?", [
     ("Keep the walkway clear. Yesterday a trolley blocked the emergency exit.", True, "Nhắc cụ thể + ví dụ thực tế."),
     ("Safety is important.", False, "Quá chung chung, không có điểm cụ thể."),
     ("Same yesterday.", False, "Thiếu 'as' ('Same as yesterday') và không nêu nội dung.")]),
   ("Who will cover Station 3 during lunch?", [
     ("Nga will cover it. She's certified for Station 3.", True, "Người cụ thể + lý do có năng lực."),
     ("Somebody will.", False, "Mơ hồ — tổ trưởng phải phân công rõ."),
     ("Nga cover.", False, "Thiếu 'will': 'Nga will cover it.'")]),
  ]},
 "planner": {"label": "Kế hoạch · Kho · Mua hàng", "emoji": "📦",
  "scenarios": [
   ("pl_change", "Khách tăng đơn hàng", "You are a foreign customer. You want to increase next week's order by 30 percent. Ask if we can deliver on time and what we need from you."),
   ("pl_supplier", "Hối nhà cung cấp", "You are a supplier's salesperson. Your delivery of materials is three days late. I call to ask for the new date. Apologize and give a reason."),
   ("pl_short", "Báo thiếu vật tư", "You are the production manager. I report a shortage of a part for tomorrow's plan. Ask how serious it is and what my plan is."),
   ("pl_ship", "Xác nhận xuất hàng", "You are a logistics coordinator for a foreign customer. Ask me to confirm the shipment date, the quantity and the documents."),
  ],
  "dialogues": [
   ("Can you move our order to next Monday?", [
     ("Let me check our capacity and materials. I'll confirm by 5 p.m. today.", True, "Không hứa vội + hẹn giờ trả lời."),
     ("Yes, sure, no problem.", False, "Hứa ngay khi chưa kiểm tra công suất."),
     ("Cannot, plan is fixed.", False, "Cộc, thiếu chủ ngữ; nên kiểm tra trước khi trả lời.")]),
   ("Why is the delivery late?", [
     ("Our supplier delivered the resin three days late. We're running overtime, and the goods will ship on Thursday.", True, "Nguyên nhân + đang làm gì + ngày giao mới."),
     ("Because supplier fault.", False, "Thiếu động từ, chỉ đổ lỗi, không có ngày giao mới."),
     ("It was late because it is late.", False, "Không giải thích gì.")]),
   ("How much stock do we have for Part A?", [
     ("3,200 pieces. That's enough for about four days of production.", True, "Con số + quy đổi ra số ngày dùng."),
     ("Stock have many.", False, "Sai ngữ pháp và không có con số."),
     ("I think a lot, I will check maybe.", False, "Thiếu chắc chắn; nên kiểm tra trước rồi trả lời.")]),
   ("The supplier says the material will be one week late.", [
     ("Then let's ask them to send part of it by air. I'll also check if another supplier can help.", True, "Đưa hai phương án cụ thể."),
     ("OK, we wait.", False, "Bị động — trễ một tuần có thể làm dừng chuyền."),
     ("Supplier is bad, change now.", False, "Cảm tính, thiếu mạo từ; đổi nhà cung cấp cần đánh giá.")]),
   ("Is the shipment ready?", [
     ("Yes. 4,800 units are packed, and the invoice and packing list are ready.", True, "Xác nhận + số lượng + chứng từ."),
     ("Ready already all.", False, "Sai trật tự từ: 'Everything is ready.'"),
     ("Yes, it was ready next week.", False, "Sai thì: không dùng 'was' với 'next week'.")]),
   ("Why is the system stock different from the shelf?", [
     ("Some parts were used without a record. We'll do a stock count today and correct the system.", True, "Nguyên nhân + hành động cụ thể."),
     ("System is wrong, not us.", False, "Đổ lỗi cho hệ thống, thiếu mạo từ."),
     ("Different a little only.", False, "Sai trật tự và xem nhẹ chênh lệch tồn kho.")]),
  ]},
}

PACK = {
 "id": "factory",
 "label": "Sản xuất · Nhà máy",
 "short": "Nhà máy",
 "emoji": "🏭",
 "desc": "QA/QC · kỹ sư · tổ trưởng · kế hoạch",
 "persona": "a Vietnamese factory engineer or supervisor",
 "counterpart": "a foreign expert or manager",
 "context": "manufacturing and factory",
 "core": [3, 11],
 "report": {
  "title": "Báo cáo ca 60 giây", "short": "Báo cáo ca", "sub": "Nói như họp cuối ca 🎙️",
  "steps": [["Output", "We made 1,150 units, target 1,200 …"], ["Issues", "Machine 3 stopped for … / No quality issues."], ["Plan", "The next shift will … / We will check …"]],
  "kind": "shift production report",
  "structure": "output vs target / quality or machine issues / plan and actions",
  "sample": "This shift we made 1,150 units against a target of 1,200, and the yield was 99 percent. Machine 3 stopped for 25 minutes because of a sensor alarm. Maintenance has cleaned the sensor, and the next shift will make up the 50 units.",
 },
 "podcast": "Podcast nhà máy",
 "game_tag": "Game anime: đánh quái hàng lỗi, hạ boss auditor khó tính",
 "reverse_tag": "kiểu nhà máy",
 "jd_placeholder": "VD: Kỹ sư QC nhà máy linh kiện điện tử Nhật ở Bắc Ninh, báo cáo lỗi, làm việc với chuyên gia Nhật, audit khách hàng…",
 "rw_placeholder": "VD: máy ép số 3 dừng 40 phút, ca sáng thiếu 200 sản phẩm so với chỉ tiêu",
 "quips": [
  "Safety first, then speed!",
  "Zero defects today!",
  "Kaizen time!",
  "Machine 3 is running again!",
  "Sort, set, shine!",
  "Ask why five times!",
  "Output on target!",
  "Gloves on, glasses on!",
  "First article: pass!",
  "Audit day? We're ready!",
 ],
 "ai": [
  ("expert", "Làm việc với chuyên gia", "You are a Japanese production expert visiting our line. You speak simple English. Ask me why the cycle time at Station 4 is long, and suggest one improvement."),
  ("breakdown", "Báo máy hỏng", "You are the production manager. I call to report that a machine on my line has stopped. Ask what happened, how long the repair will take and how much output we will lose."),
  ("defect", "Báo cáo hàng lỗi", "You are the QA manager. I found defects in a lot this morning. Ask what the defect is, how many pieces, what I did with the lot and what the next steps are."),
  ("audit", "Tiếp auditor", "You are a customer auditor visiting our factory. Ask me to show inspection records and calibration records, and point out one small problem politely."),
  ("claim", "Trả lời khiếu nại khách", "You are a foreign customer's quality engineer. You received parts with scratches. Ask me about the root cause, the containment action and when you will get the corrective action report."),
  ("plan", "Đổi kế hoạch sản xuất", "You are the sales manager. The customer wants 20 percent more units next week. Ask me if the factory has enough capacity, materials and workers, and what I need."),
  ("safety", "Hướng dẫn an toàn", "You are a new worker on your first day. I am the line leader. Ask me about the safety rules, the PPE you must wear and what to do in an emergency."),
  ("kaizen", "Trình bày cải tiến", "You are the factory director. I am presenting a kaizen idea for my line. Ask about the problem, the idea, the cost and the expected result in numbers."),
 ],
 "rev": [
  ("Máy số 3 đang dừng.", "Machine 3 has stopped."),
  ("Hôm nay chuyền mình đạt chỉ tiêu.", "Our line met the target today."),
  ("Lô này có năm cái bị lỗi.", "There are five defects in this lot."),
  ("Vui lòng đeo kính bảo hộ.", "Please wear your safety glasses."),
  ("Ca đêm thiếu hai người.", "The night shift is two people short."),
  ("Chúng tôi đang chờ phụ tùng thay thế.", "We're waiting for a spare part."),
  ("Tỉ lệ đạt tuần này là 98%.", "This week's yield is 98 percent."),
  ("Giữ lô này lại, chưa được xuất.", "Please hold this lot. Don't ship it yet."),
  ("Nguyên nhân gốc là đồ gá bị mòn.", "The root cause is a worn jig."),
  ("Anh chỉ trên bản vẽ giúp tôi được không?", "Could you show me on the drawing?"),
  ("Kho còn đủ hàng cho ba ngày.", "We have enough stock for three days."),
  ("Tuần sau khách hàng đến audit.", "The customer is coming for an audit next week."),
  ("Dùng xong nhớ để dụng cụ về chỗ cũ.", "Please put the tools back after use."),
  ("Bạn làm thử cho tôi xem.", "Show me how you do it."),
 ],
 "reading": [
  {"t": "Shift report", "text": "Line 2 – Day shift, May 14\nOutput: 1,150 / target 1,200\nYield: 98.5%\nIssue: Machine 3 stopped for 25 minutes (sensor alarm). Maintenance cleaned the sensor.\nNight shift: please check Machine 3 every two hours.", "q": [
    {"q": "Did the day shift reach the target?", "o": ["Yes, exactly", "No, it was 50 units short", "It made more than the target"], "a": 1},
    {"q": "What should the night shift do?", "o": ["Stop Machine 3", "Clean all the machines", "Check Machine 3 every two hours"], "a": 2}]},
  {"t": "Safety notice", "text": "SAFETY NOTICE\nFrom June 1, safety shoes are required in all production areas, including the warehouse. Visitors can borrow shoes at the security gate. If you see a hazard, report it to your line leader right away.", "q": [
    {"q": "Where are safety shoes required?", "o": ["Only on Line 1", "In all production areas and the warehouse", "Only in the office"], "a": 1},
    {"q": "What can visitors do?", "o": ["Borrow shoes at the security gate", "Stay in the office", "Buy new shoes"], "a": 0}]},
  {"t": "Customer email", "text": "Dear QA team,\nWe found scratches on 12 covers from Lot 2405-B. Please hold all stock of this lot and send us your containment action by tomorrow. The full corrective action report is due within 14 days.\nBest regards,\nK. Park, Supplier Quality", "q": [
    {"q": "What problem did the customer find?", "o": ["Missing screws", "Wrong color", "Scratches on covers"], "a": 2},
    {"q": "What must the factory send by tomorrow?", "o": ["The containment action", "The full report", "New covers"], "a": 0}]},
  {"t": "Maintenance notice", "text": "PREVENTIVE MAINTENANCE\nPress machines P1–P4 will be stopped on Saturday from 8 a.m. to 12 p.m. Please finish all Model C orders by Friday night. Spare parts have already arrived.\nContact: Tuấn (Maintenance), ext. 312", "q": [
    {"q": "When will the presses stop?", "o": ["Friday night", "Saturday morning", "All day Saturday"], "a": 1},
    {"q": "What should the lines do before that?", "o": ["Finish Model C orders", "Order spare parts", "Clean the presses"], "a": 0}]},
  {"t": "Audit agenda", "text": "Customer audit – Tuesday, 10 March\n9:00 Opening meeting (Room A)\n9:30 Factory tour: SMT line, final inspection, warehouse\n13:00 Document review: training and calibration records\n16:00 Closing meeting\nPlease wear visitor badges at all times.", "q": [
    {"q": "What will the auditors check after lunch?", "o": ["The warehouse", "The SMT line", "Training and calibration records"], "a": 2},
    {"q": "Where is the opening meeting?", "o": ["Room A", "The warehouse", "Final inspection"], "a": 0}]},
 ],
 "events": [
  ("audit", "Chuẩn bị audit khách hàng", "You are a customer auditor coming to our factory next week. Ask me how we control defects, where our records are and how we train new operators."),
  ("visit", "Đón khách tham quan nhà máy", "You are a foreign customer visiting our factory for the first time. Ask about our lines, capacity, quality results and safety rules during the tour."),
  ("expert", "Chuyên gia mới sang làm việc", "You are a production expert from Japan starting work at our factory next week. Ask me about the lines, the main problems and how the team works."),
  ("claim", "Họp về khiếu nại chất lượng", "You are the customer's quality manager in a meeting about a defect claim. Ask for the root cause, containment and corrective actions, with dates."),
  ("interview", "Phỏng vấn vị trí nhà máy", "You are the plant manager interviewing me for a QC or production engineer job. Ask about my experience, a problem I solved and how I work with foreign experts."),
  ("kaizen", "Thi cải tiến (kaizen)", "You are a judge at our factory's kaizen contest. Ask me to explain my improvement, the before-and-after numbers and how we will sustain it."),
  ("other", "Khác", ""),
 ],
 "roles": ROLES,
 "phases": PHASES,
}
