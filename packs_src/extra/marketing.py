# -*- coding: utf-8 -*-
# v4.1 — nội dung làm giàu cho gói marketing (nối vào cuối gói, xem build.py)
# Tên thương hiệu / sàn đều tự đặt (Bamboo Bites, Shopza…), dùng lại từ gói gốc.

PHASES = []

# ───────────────────────── 1. Email marketing & tự động hoá ─────────────────────────
PHASES.append({
 "title": "Email marketing & tự động hoá",
 "vocab": [
  ("newsletter", "/ˈnjuːzletə/", "n", "bản tin email định kỳ", "Our weekly <b>newsletter</b> goes out every Tuesday morning.", "Bản tin hằng tuần của mình được gửi đi vào sáng thứ Ba.", "メルマガ", "merumaga"),
  ("subscriber", "/səbˈskraɪbə/", "n", "người đăng ký nhận tin", "We now have 12,000 email <b>subscribers</b>.", "Hiện mình có 12.000 người đăng ký nhận email."),
  ("open rate", "/ˈəʊpən reɪt/", "n", "tỉ lệ mở email = số người mở ÷ số email gửi thành công", "The <b>open rate</b> for this email was 28%.", "Tỉ lệ mở của email này là 28%.", "開封率", "kaifūritsu"),
  ("subject line", "/ˈsʌbdʒekt laɪn/", "n", "tiêu đề email", "A short <b>subject line</b> usually gets more opens.", "Tiêu đề email ngắn thường được mở nhiều hơn.", "件名", "kenmei"),
  ("unsubscribe", "/ˌʌnsəbˈskraɪb/", "v", "huỷ đăng ký nhận tin", "About 50 people <b>unsubscribed</b> after the last email.", "Khoảng 50 người đã huỷ đăng ký sau email vừa rồi.", "配信停止", "haishin teishi"),
  ("mailing list", "/ˈmeɪlɪŋ lɪst/", "n", "danh sách nhận email", "Please clean the <b>mailing list</b> before the big send.", "Lọc lại danh sách nhận email trước đợt gửi lớn nhé."),
  ("automation", "/ˌɔːtəˈmeɪʃn/", "n", "tự động hoá (gửi email, tin nhắn theo kịch bản cài sẵn)", "The <b>automation</b> sends a reminder three days after sign-up.", "Luồng tự động gửi email nhắc ba ngày sau khi khách đăng ký."),
  ("abandoned cart", "/əˌbændənd ˈkɑːt/", "n", "giỏ hàng bị bỏ dở (khách thêm hàng nhưng không mua)", "We send an <b>abandoned cart</b> email one hour later.", "Một tiếng sau, mình gửi email nhắc giỏ hàng bị bỏ dở.", "カゴ落ち", "kago ochi"),
  ("opt in", "/ˌɒpt ˈɪn/", "phr v", "đồng ý nhận (email, tin nhắn quảng cáo)", "We only email customers who <b>opt in</b>.", "Mình chỉ gửi email cho khách đã đồng ý nhận tin."),
  ("spam folder", "/ˈspæm ˌfəʊldə/", "n", "hộp thư rác", "Some of our emails are going to the <b>spam folder</b>.", "Một số email của mình đang rơi vào hộp thư rác.", "迷惑メールフォルダ", "meiwaku mēru foruda"),
 ],
 "phrases": [
  ("The newsletter goes out at 9 a.m. every Tuesday.", "Bản tin được gửi lúc 9 giờ sáng thứ Ba hằng tuần."),
  ("Let's test two subject lines on a small group first.", "Mình thử hai tiêu đề trên một nhóm nhỏ trước nhé."),
  ("Our open rate is 25%, but very few people click.", "Tỉ lệ mở của mình là 25%, nhưng rất ít người nhấp."),
  ("Please send me a test email before the real send.", "Gửi em một email thử trước khi gửi thật nhé."),
  ("We should remove inactive subscribers from the list.", "Mình nên bỏ những người lâu không mở email khỏi danh sách."),
  ("The welcome email goes out right after sign-up.", "Email chào mừng được gửi ngay sau khi khách đăng ký."),
  ("Every email must have an unsubscribe link.", "Email nào cũng phải có link huỷ đăng ký."),
  ("Can we add the customer's first name to the greeting?", "Mình thêm tên khách vào lời chào được không?"),
  ("The abandoned cart email brought back 60 orders last week.", "Tuần trước email nhắc giỏ hàng kéo lại được 60 đơn."),
 ],
 "dialogues": [
  ("What was the open rate for yesterday's newsletter?", [
    ("It was 31%, a bit higher than usual. The new subject line worked well.", True, "Con số + so sánh + lý do ngắn gọn."),
    ("Open rate is 31% yesterday.", False, "Sai thì: nói về hôm qua dùng 'was': 'It was 31%.'"),
    ("Many people open, I think.", False, "Chỉ đoán, không có số — hỏi tỉ lệ thì trả lời bằng con số."),
  ]),
  ("Some customers say our emails go to spam. What can we do?", [
    ("We can remove old addresses from the list and send less often. I'll also check our sender settings with IT.", True, "Nêu hai giải pháp cụ thể + người phối hợp."),
    ("Customers should check spam folder.", False, "Đẩy việc cho khách; lại thiếu mạo từ: 'the spam folder'."),
    ("Spam is not our problem.", False, "Sai quan điểm — email vào thư rác thì mất doanh thu, phải tìm cách khắc phục."),
  ]),
  ("Can we email everyone who bought from us last year?", [
    ("Only the people who opted in. We can't send marketing emails without permission.", True, "Nhắc đúng nguyên tắc: chỉ gửi cho người đã đồng ý nhận tin."),
    ("Yes, we have their email, so we can.", False, "Có địa chỉ email chưa có nghĩa là được gửi quảng cáo — cần khách đồng ý."),
    ("Yes, we send all them.", False, "Sai: 'We'll send it to all of them.' — và chưa kiểm tra khách đã đồng ý nhận tin chưa."),
  ]),
  ("How does the abandoned cart automation work?", [
    ("If a customer leaves items in the cart, they get a reminder after one hour and a small voucher after one day.", True, "Giải thích từng bước, có mốc thời gian."),
    ("Customer leave cart, we send email.", False, "Thiếu 's' ('leaves'), thiếu mạo từ và mốc thời gian cụ thể."),
    ("It is automatic, so I don't know.", False, "Tự động không có nghĩa là không cần hiểu — người vận hành phải nắm luồng."),
  ]),
  ("Why did so many people unsubscribe this week?", [
    ("We sent five emails in five days. That's too many, so I'll go back to two a week.", True, "Nguyên nhân cụ thể + điều chỉnh tần suất gửi."),
    ("Because they don't like us anymore.", False, "Đoán cảm tính, không nhìn vào dữ liệu gửi."),
    ("Many people is unsubscribe because too much email.", False, "Sai ngữ pháp: 'Many people unsubscribed because we sent too many emails.'"),
  ]),
 ],
 "listen": [
  ("Our weekly newsletter goes out on Tuesday", ["newsletter", "Tuesday"], "lịch gửi bản tin"),
  ("The open rate was thirty-one percent", ["open", "thirty-one"], "tỉ lệ mở email"),
  ("Please check the subject line for typos", ["subject", "typos"], "kiểm tra tiêu đề email"),
  ("Every email needs an unsubscribe link", ["needs", "unsubscribe"], "quy định khi gửi email"),
  ("We set up a new automation last month. New subscribers get a welcome email on day one. On day three, they get a small voucher.", ["automation", "welcome", "voucher"], "luồng email tự động"),
  ("Our open rate is fine, but the click rate is low. I think the email is too long. Let's try one clear button next time.", ["fine", "long", "button"], "phân tích kết quả email"),
 ],
})

# ───────────────────────── 2. SEO & website ─────────────────────────
PHASES.append({
 "title": "SEO & website",
 "vocab": [
  ("keyword", "/ˈkiːwɜːd/", "n", "từ khoá", "'Healthy snacks' is our main <b>keyword</b>.", "'Đồ ăn vặt lành mạnh' là từ khoá chính của mình.", "キーワード", "kīwādo"),
  ("search engine", "/ˈsɜːtʃ ˌendʒɪn/", "n", "công cụ tìm kiếm", "Most visitors find us through a <b>search engine</b>.", "Phần lớn khách tìm thấy mình qua công cụ tìm kiếm.", "検索エンジン", "kensaku enjin"),
  ("ranking", "/ˈræŋkɪŋ/", "n", "thứ hạng (trên trang kết quả tìm kiếm)", "Our <b>ranking</b> for 'bamboo straws' went up to number three.", "Thứ hạng của mình cho từ khoá 'ống hút tre' đã lên vị trí số ba.", "検索順位", "kensaku jun'i"),
  ("organic traffic", "/ɔːˌɡænɪk ˈtræfɪk/", "n", "lượt truy cập tự nhiên (không phải trả tiền quảng cáo)", "<b>Organic traffic</b> grew by 40% after we started the blog.", "Lượt truy cập tự nhiên tăng 40% sau khi mình bắt đầu viết blog."),
  ("backlink", "/ˈbæklɪŋk/", "n", "liên kết từ trang khác trỏ về website mình", "A <b>backlink</b> from a big news site helps a lot.", "Một liên kết từ trang báo lớn trỏ về giúp ích rất nhiều.", "被リンク", "hirinku"),
  ("meta description", "/ˌmetə dɪˈskrɪpʃn/", "n", "đoạn mô tả ngắn hiện dưới tiêu đề trên kết quả tìm kiếm", "Keep the <b>meta description</b> under 160 characters.", "Giữ đoạn mô tả meta dưới 160 ký tự."),
  ("page speed", "/ˈpeɪdʒ spiːd/", "n", "tốc độ tải trang", "Big images are hurting our <b>page speed</b>.", "Ảnh dung lượng lớn đang làm chậm tốc độ tải trang."),
  ("homepage", "/ˈhəʊmpeɪdʒ/", "n", "trang chủ website", "Let's put the new collection on the <b>homepage</b>.", "Mình đưa bộ sưu tập mới lên trang chủ nhé.", "トップページ", "toppu pēji"),
  ("blog post", "/ˈblɒɡ pəʊst/", "n", "bài viết blog", "We publish two <b>blog posts</b> a week.", "Mỗi tuần mình đăng hai bài blog."),
  ("search volume", "/ˈsɜːtʃ ˌvɒljuːm/", "n", "lượng tìm kiếm (số lần một từ khoá được tìm mỗi tháng)", "This keyword has a high <b>search volume</b> in December.", "Từ khoá này có lượng tìm kiếm cao vào tháng Mười Hai.", "検索ボリューム", "kensaku boryūmu"),
 ],
 "phrases": [
  ("We're on page one for 'bamboo straws'.", "Mình đang ở trang một cho từ khoá 'ống hút tre'."),
  ("Organic traffic is up 20% this quarter.", "Lượt truy cập tự nhiên quý này tăng 20%."),
  ("Which keywords bring us the most sales?", "Những từ khoá nào mang lại nhiều doanh số nhất?"),
  ("Let's write a blog post that answers this question.", "Mình viết một bài blog trả lời câu hỏi này nhé."),
  ("The site takes six seconds to load on mobile.", "Trang mất sáu giây để tải trên điện thoại."),
  ("Please compress the images before you upload them.", "Nén ảnh trước khi tải lên giúp em nhé."),
  ("SEO takes time. We usually see results in three to six months.", "SEO cần thời gian. Thường ba đến sáu tháng mới thấy kết quả."),
  ("Every page needs its own title and meta description.", "Trang nào cũng cần tiêu đề và đoạn mô tả riêng."),
  ("We lost some rankings after the website update.", "Sau khi cập nhật website, mình bị tụt một số thứ hạng."),
 ],
 "dialogues": [
  ("Why is our organic traffic going down?", [
    ("We lost rankings for two main keywords after the site update. I'm checking the broken links now.", True, "Nguyên nhân cụ thể + đang xử lý."),
    ("Because the search engine change something.", False, "Sai thì ('changed') và đổ lỗi mơ hồ, chưa xem dữ liệu."),
    ("Traffic down, I don't know why.", False, "Thiếu động từ ('Traffic is down'); nếu chưa rõ, nói 'Let me check and get back to you.'"),
  ]),
  ("Can we be number one on search next week?", [
    ("Honestly, that's not realistic. SEO usually takes a few months, but we can run search ads in the meantime.", True, "Trung thực về thời gian + phương án ngắn hạn."),
    ("Yes, sure, no problem.", False, "Hứa bừa — không ai đảm bảo được hạng một chỉ sau một tuần."),
    ("Next week cannot, SEO is slow.", False, "Thiếu chủ ngữ, cộc lốc: 'We can't do it by next week.'"),
  ]),
  ("Which keyword should we focus on?", [
    ("'Bamboo straws for cafés'. The search volume is smaller, but people who search for it are ready to buy.", True, "Chọn từ khoá + lý do về ý định mua."),
    ("'Straw', because many people search.", False, "Từ khoá quá rộng: khó lên hạng và ít người mua thật."),
    ("Keyword is many, we use all.", False, "Sai cấu trúc ('There are many keywords') và không chọn được trọng tâm."),
  ]),
  ("The homepage is very slow. What's the problem?", [
    ("The banner images are too big. If we compress them, the page should load in about two seconds.", True, "Nguyên nhân + giải pháp + kết quả dự kiến."),
    ("Maybe internet of customer is slow.", False, "Dịch từng chữ ('the customer's internet') và đổ lỗi cho khách."),
    ("It slow because many picture.", False, "Thiếu 'is' và số nhiều: 'It's slow because the pictures are too big.'"),
  ]),
  ("Can you write the meta description for the new product page?", [
    ("Sure. I'll keep it under 160 characters and include the main keyword.", True, "Nhận việc + nêu đúng tiêu chí SEO."),
    ("Sure, I write long so it has many keyword.", False, "Nhồi từ khoá là sai SEO; lại thiếu 'will' và 's'."),
    ("What is meta? I never do.", False, "Chưa biết thì hỏi lịch sự: 'I've never done it. Could you show me an example?'"),
  ]),
 ],
 "listen": [
  ("Our main keyword is healthy snacks", ["keyword", "healthy"], "từ khoá chính"),
  ("We are now on page one of the search results", ["page", "results"], "thứ hạng tìm kiếm"),
  ("Organic traffic went up twenty percent", ["Organic", "twenty"], "lượt truy cập tự nhiên"),
  ("Please compress the images on the homepage", ["compress", "homepage"], "tốc độ tải trang"),
  ("We publish two blog posts every week. Each post answers one customer question. This brings us more organic traffic.", ["publish", "question", "traffic"], "kế hoạch viết blog"),
  ("The homepage takes six seconds to load. Most visitors leave before that. Let's make the images smaller.", ["six", "leave", "smaller"], "vấn đề tốc độ trang"),
 ],
})

# ───────────────────────── 3. Video & livestream bán hàng ─────────────────────────
PHASES.append({
 "title": "Video & livestream bán hàng",
 "vocab": [
  ("script", "/skrɪpt/", "n", "kịch bản", "Please send me the <b>script</b> for tonight's show.", "Gửi em kịch bản buổi phát tối nay nhé.", "台本", "daihon"),
  ("host", "/həʊst/", "n/v", "người dẫn; dẫn (chương trình, livestream)", "Our <b>host</b> knows every product very well.", "Người dẫn của mình rất rành từng sản phẩm."),
  ("viewer", "/ˈvjuːə/", "n", "người xem", "We had 3,000 <b>viewers</b> at the peak.", "Lúc đông nhất mình có 3.000 người xem.", "視聴者", "shichōsha"),
  ("thumbnail", "/ˈθʌmneɪl/", "n", "ảnh bìa (ảnh thu nhỏ) của video", "A bright <b>thumbnail</b> gets more clicks.", "Ảnh bìa sáng màu thu hút nhiều lượt nhấp hơn.", "サムネイル", "samuneiru"),
  ("hook", "/hʊk/", "n", "đoạn mở đầu 'câu' người xem (vài giây đầu video)", "The first three seconds need a strong <b>hook</b>.", "Ba giây đầu cần một đoạn mở thật cuốn."),
  ("watch time", "/ˈwɒtʃ taɪm/", "n", "thời lượng xem", "Average <b>watch time</b> is only eight seconds.", "Thời lượng xem trung bình chỉ có tám giây.", "視聴時間", "shichō jikan"),
  ("voice-over", "/ˈvɔɪs əʊvə/", "n", "lời thuyết minh, lồng tiếng", "Let's add a <b>voice-over</b> in Vietnamese.", "Mình thêm lời thuyết minh tiếng Việt nhé.", "ナレーション", "narēshon"),
  ("subtitle", "/ˈsʌbtaɪtl/", "n", "phụ đề", "Many people watch without sound, so add <b>subtitles</b>.", "Nhiều người xem không bật tiếng, nên hãy thêm phụ đề.", "字幕", "jimaku"),
  ("giveaway", "/ˈɡɪvəweɪ/", "n", "quà tặng miễn phí, minigame tặng quà", "We do a <b>giveaway</b> every 15 minutes to keep viewers watching.", "Cứ 15 phút mình tặng quà một lần để giữ chân người xem."),
  ("pin", "/pɪn/", "v", "ghim (bình luận, sản phẩm)", "Please <b>pin</b> the voucher at the top of the chat.", "Ghim voucher lên đầu khung chat giúp em nhé."),
 ],
 "phrases": [
  ("We go live at 8 tonight. Please be ready by 7:30.", "Tối nay 8 giờ mình lên sóng. Mọi người sẵn sàng trước 7 rưỡi nhé."),
  ("Let's start with the best-seller to warm up the audience.", "Mình mở đầu bằng sản phẩm bán chạy nhất để hâm nóng không khí."),
  ("Can you pin the product link now?", "Bạn ghim link sản phẩm lên ngay được không?"),
  ("Please read the comments and answer questions about sizes.", "Đọc bình luận và trả lời các câu hỏi về size giúp mình nhé."),
  ("The first three seconds decide if people keep watching.", "Ba giây đầu quyết định người ta có xem tiếp hay không."),
  ("We'll cut the long livestream into five short clips.", "Mình sẽ cắt buổi livestream dài thành năm clip ngắn."),
  ("The sound is too low. Can you move the mic closer?", "Tiếng nhỏ quá. Bạn đưa mic lại gần hơn được không?"),
  ("We sold 400 units during the two-hour livestream.", "Mình bán được 400 sản phẩm trong buổi livestream hai tiếng."),
  ("Let's do a giveaway when we reach 1,000 viewers.", "Khi đạt 1.000 người xem thì mình tặng quà nhé."),
 ],
 "dialogues": [
  ("Viewers are dropping. What should we do?", [
    ("Let's announce a giveaway in five minutes and show the flash deal now.", True, "Hành động nhanh, cụ thể để kéo người xem lại."),
    ("Viewers drop because they busy.", False, "Thiếu 'are' ('they're busy') và chỉ đoán, không đưa giải pháp."),
    ("Don't worry, continue.", False, "Cộc lốc và bỏ qua vấn đề đang diễn ra."),
  ]),
  ("Is the script ready for tonight?", [
    ("Yes. I've sent it to the host. It has the product order, the key points and the voucher times.", True, "Xác nhận + đã gửi cho ai + nội dung chính."),
    ("Script is ready since yesterday.", False, "Sai thì và thiếu mạo từ: 'The script has been ready since yesterday.'"),
    ("No need script, the host can talk.", False, "Thiếu 'for a' ('No need for a script'); không có kịch bản dễ quên sản phẩm, giờ tung voucher."),
  ]),
  ("A viewer asks if the jacket is waterproof. Is it?", [
    ("It's water-resistant, not fully waterproof. Let's say that clearly so customers aren't disappointed.", True, "Trả lời trung thực, không nói quá công dụng."),
    ("Just say yes, then they will buy.", False, "Nói sai công dụng là lừa khách, dễ bị trả hàng và đánh giá xấu."),
    ("I think is waterproof maybe.", False, "Thiếu chủ ngữ 'it' và không chắc — phải kiểm tra thông tin sản phẩm trước."),
  ]),
  ("Why is the watch time on our videos so short?", [
    ("Our intros are too slow. We should show the product in the first three seconds.", True, "Chỉ ra điểm yếu cụ thể + cách sửa."),
    ("Because video is too long, people is bored.", False, "Sai chia ('people are bored'), thiếu mạo từ; chưa chỉ ra đoạn nào gây chán."),
    ("Watch time short is normal.", False, "Trật tự từ kiểu Việt ('Short watch time is normal') và né vấn đề."),
  ]),
  ("Can we use the livestream clips in our ads?", [
    ("Yes, if the host agrees. I'll cut three short clips with subtitles by Thursday.", True, "Đồng ý có điều kiện (quyền hình ảnh) + kế hoạch cụ thể."),
    ("Yes, we can using them.", False, "Sau 'can' dùng động từ nguyên thể: 'we can use them'."),
    ("Clips is ours, no need to ask.", False, "Sai chia ('are') và bỏ qua quyền hình ảnh của người dẫn."),
  ]),
 ],
 "listen": [
  ("We go live at eight tonight", ["live", "eight"], "giờ lên sóng"),
  ("Please pin the voucher in the chat", ["pin", "chat"], "ghim voucher"),
  ("The first three seconds need a strong hook", ["seconds", "hook"], "mở đầu video"),
  ("Add subtitles because many people watch without sound", ["subtitles", "sound"], "phụ đề video"),
  ("We had three thousand viewers at the peak. We sold five hundred bags in two hours. Next time we need more stock.", ["viewers", "bags", "stock"], "tổng kết livestream"),
  ("Welcome back, everyone! Today we have a giveaway every fifteen minutes. Stay with us and comment your size.", ["giveaway", "fifteen", "size"], "lời mở đầu livestream"),
 ],
})

# ───────────────────────── 4. Thương hiệu & nhận diện ─────────────────────────
PHASES.append({
 "title": "Thương hiệu & nhận diện",
 "vocab": [
  ("brand identity", "/ˌbrænd aɪˈdentəti/", "n", "bộ nhận diện thương hiệu", "Our new <b>brand identity</b> uses green and white.", "Bộ nhận diện thương hiệu mới dùng màu xanh lá và trắng."),
  ("logo", "/ˈləʊɡəʊ/", "n", "logo, biểu tượng thương hiệu", "Don't change the colour of the <b>logo</b>.", "Đừng đổi màu logo.", "ロゴ", "rogo"),
  ("tone of voice", "/ˌtəʊn əv ˈvɔɪs/", "n", "giọng điệu thương hiệu (cách nói, cách viết)", "Our <b>tone of voice</b> is friendly but not silly.", "Giọng điệu của mình thân thiện nhưng không nhí nhố."),
  ("positioning", "/pəˈzɪʃənɪŋ/", "n", "định vị thương hiệu", "Our <b>positioning</b> is 'premium but affordable'.", "Định vị của mình là 'cao cấp nhưng vừa túi tiền'.", "ポジショニング", "pojishoningu"),
  ("colour palette", "/ˈkʌlə ˌpælət/", "n", "bảng màu", "The <b>colour palette</b> has three main colours.", "Bảng màu có ba màu chính."),
  ("font", "/fɒnt/", "n", "phông chữ", "Please use our brand <b>font</b> on all posters.", "Dùng phông chữ thương hiệu trên mọi poster nhé.", "フォント", "fonto"),
  ("rebrand", "/ˌriːˈbrænd/", "v/n", "làm mới thương hiệu (đổi tên, logo, hình ảnh)", "The company <b>rebranded</b> after ten years.", "Sau mười năm, công ty đã làm mới thương hiệu."),
  ("packaging", "/ˈpækɪdʒɪŋ/", "n", "bao bì", "The new <b>packaging</b> is easier to open.", "Bao bì mới dễ mở hơn.", "パッケージ", "pakkēji"),
  ("consistent", "/kənˈsɪstənt/", "adj", "nhất quán, đồng bộ", "Our look should be <b>consistent</b> on every channel.", "Hình ảnh của mình phải đồng bộ trên mọi kênh."),
  ("mascot", "/ˈmæskɒt/", "n", "linh vật", "Kids love our panda <b>mascot</b>.", "Trẻ con rất thích linh vật gấu trúc của mình.", "マスコット", "masukotto"),
 ],
 "phrases": [
  ("This colour doesn't match our brand.", "Màu này không hợp với thương hiệu mình."),
  ("Please use the logo file from the shared folder.", "Dùng file logo trong thư mục chung nhé."),
  ("Our tone is warm and simple, like talking to a friend.", "Giọng điệu của mình ấm áp, đơn giản, như nói chuyện với bạn bè."),
  ("Let's keep the look consistent across all channels.", "Mình giữ hình ảnh đồng bộ trên mọi kênh nhé."),
  ("The logo needs more space around it.", "Logo cần thêm khoảng trống xung quanh."),
  ("Customers should recognise us without reading the name.", "Khách phải nhận ra mình mà không cần đọc tên."),
  ("We're changing the packaging, not the product.", "Mình đổi bao bì, không đổi sản phẩm."),
  ("Who approves the final design?", "Ai là người duyệt bản thiết kế cuối?"),
  ("How do we want people to feel about the brand?", "Mình muốn khách cảm nhận thế nào về thương hiệu?"),
 ],
 "dialogues": [
  ("Can we make the logo red for the Tết posters?", [
    ("We shouldn't change the logo colour. How about a red background with the white logo?", True, "Giữ quy chuẩn logo + đề xuất cách khác vẫn đúng ý Tết."),
    ("Yes, red is lucky, change it.", False, "Tự ý đổi màu logo phá vỡ nhận diện; câu lại cộc."),
    ("Logo cannot change, rule is rule.", False, "Cần bị động ('The logo can't be changed') và từ chối cứng nhắc, không đưa phương án."),
  ]),
  ("How would you describe our tone of voice?", [
    ("Friendly and simple. We talk like a helpful friend, not like a salesperson.", True, "Mô tả bằng tính từ rõ ràng + so sánh dễ hiểu."),
    ("Our tone is very beautiful.", False, "Dùng sai từ: giọng điệu không 'beautiful' — dùng 'friendly', 'warm', 'professional'…"),
    ("Tone is voice of the brand.", False, "Chỉ định nghĩa lại từ, không trả lời câu hỏi; thiếu mạo từ."),
  ]),
  ("The new packaging looks great, but customers can't find us on the shelf.", [
    ("Good point. The old yellow was easy to spot. Let's make the logo bigger and bring back some yellow.", True, "Ghi nhận + phân tích nguyên nhân + đề xuất điều chỉnh."),
    ("Customers need time to get used.", False, "Thiếu 'to it' ('get used to it') và bỏ qua ảnh hưởng tới doanh số."),
    ("I think packaging is not the problem.", False, "Phủ nhận khi chưa kiểm tra; thiếu mạo từ 'the packaging'."),
  ]),
  ("Why do we need to rebrand?", [
    ("Our look feels old to younger customers, and our sales in that group are falling.", True, "Lý do dựa trên khách hàng + số liệu kinh doanh."),
    ("Because the boss want new logo.", False, "Sai chia ('wants'), thiếu 'a' và lý do chủ quan."),
    ("For more beautiful.", False, "Dịch từng chữ 'cho đẹp hơn': nên nói 'To look more modern.' kèm lý do kinh doanh."),
  ]),
  ("The agency used a different font in this banner.", [
    ("Thanks for spotting that. I'll ask them to change it to our brand font today.", True, "Cảm ơn người phát hiện + xử lý ngay trong ngày."),
    ("It's OK, nobody see the font.", False, "Sai chia ('nobody sees') và coi nhẹ sự nhất quán thương hiệu."),
    ("Agency always make mistake.", False, "Sai ngữ pháp ('The agency always makes mistakes') và đổ lỗi chung chung."),
  ]),
 ],
 "listen": [
  ("Please use the logo from the shared folder", ["logo", "shared"], "dùng file logo"),
  ("Our tone of voice is warm and friendly", ["tone", "friendly"], "giọng điệu thương hiệu"),
  ("The new packaging is easier to open", ["packaging", "open"], "bao bì mới"),
  ("Keep the colours consistent on every channel", ["colours", "consistent"], "đồng bộ hình ảnh"),
  ("Our positioning is simple. We are premium but affordable. Every design must show that.", ["positioning", "affordable", "design"], "định vị thương hiệu"),
  ("We're going to rebrand next year. The logo will be simpler. The colour palette will be brighter.", ["rebrand", "simpler", "brighter"], "kế hoạch làm mới thương hiệu"),
 ],
})

# ───────────────────────── 5. Sự kiện & activation ─────────────────────────
PHASES.append({
 "title": "Sự kiện & activation",
 "vocab": [
  ("venue", "/ˈvenjuː/", "n", "địa điểm tổ chức", "The <b>venue</b> can hold 300 people.", "Địa điểm này chứa được 300 người.", "会場", "kaijō"),
  ("booth", "/buːð/", "n", "gian hàng, quầy trưng bày (ở hội chợ, sự kiện)", "Our <b>booth</b> is next to the main entrance.", "Gian hàng của mình ở ngay cạnh lối vào chính.", "ブース", "būsu"),
  ("sampling", "/ˈsɑːmplɪŋ/", "n", "hoạt động phát mẫu thử", "We did <b>sampling</b> at five supermarkets last weekend.", "Cuối tuần rồi mình phát mẫu thử ở năm siêu thị.", "サンプリング", "sanpuringu"),
  ("activation", "/ˌæktɪˈveɪʃn/", "n", "hoạt động kích hoạt thương hiệu (cho khách trải nghiệm trực tiếp)", "The mall <b>activation</b> had a photo corner and free drinks.", "Hoạt động kích hoạt ở trung tâm thương mại có góc chụp ảnh và nước uống miễn phí."),
  ("attendee", "/əˌtenˈdiː/", "n", "người tham dự", "Every <b>attendee</b> gets a gift bag.", "Mỗi người tham dự được tặng một túi quà.", "来場者", "raijōsha"),
  ("run sheet", "/ˈrʌn ʃiːt/", "n", "kịch bản chạy chương trình (chi tiết theo từng giờ)", "According to the <b>run sheet</b>, the show starts at 9:15.", "Theo kịch bản chạy chương trình, chương trình bắt đầu lúc 9 giờ 15."),
  ("setup", "/ˈsetʌp/", "n", "khâu dựng, lắp đặt (sân khấu, gian hàng)", "<b>Setup</b> starts at 6 a.m. on Saturday.", "Khâu dựng bắt đầu lúc 6 giờ sáng thứ Bảy.", "設営", "setsuei"),
  ("MC", "/ˌem ˈsiː/", "n", "người dẫn chương trình", "The <b>MC</b> will introduce the new product at ten.", "MC sẽ giới thiệu sản phẩm mới lúc mười giờ.", "司会", "shikai"),
  ("foot traffic", "/ˈfʊt ˌtræfɪk/", "n", "lượng người qua lại (tại điểm bán, sự kiện)", "The mall has heavy <b>foot traffic</b> on Sunday afternoons.", "Chiều Chủ nhật trung tâm thương mại rất đông người qua lại."),
  ("backdrop", "/ˈbækdrɒp/", "n", "phông nền sân khấu (backdrop)", "The logo on the <b>backdrop</b> must be easy to see in photos.", "Logo trên backdrop phải dễ thấy khi lên ảnh."),
 ],
 "phrases": [
  ("Setup starts at 6 a.m., so please arrive on time.", "6 giờ sáng bắt đầu dựng, mọi người đến đúng giờ nhé."),
  ("Let's walk through the run sheet one more time.", "Mình rà lại kịch bản chương trình thêm một lần nữa nhé."),
  ("Who is in charge of the sound system?", "Ai phụ trách hệ thống âm thanh?"),
  ("We need a plan B if it rains.", "Mình cần phương án dự phòng nếu trời mưa."),
  ("How many samples do we have left?", "Mình còn bao nhiêu mẫu thử?"),
  ("Ask visitors to scan the QR code at the booth.", "Mời khách quét mã QR ở gian hàng nhé."),
  ("The event is running 15 minutes late.", "Chương trình đang chậm 15 phút."),
  ("Great job, everyone. We gave out 2,000 samples today.", "Mọi người làm tốt lắm. Hôm nay mình phát được 2.000 mẫu thử."),
  ("Has the venue confirmed the booking in writing?", "Bên địa điểm đã xác nhận đặt chỗ bằng văn bản chưa?"),
 ],
 "dialogues": [
  ("The weather forecast says rain on Saturday. Are we ready?", [
    ("Yes. The venue has an indoor hall, and we've booked it as a backup.", True, "Khẳng định + phương án dự phòng đã chốt."),
    ("Rain or not, we still do.", False, "Thiếu tân ngữ ('we'll still do it') và không có phương án dự phòng."),
    ("I hope no rain.", False, "Sai cấu trúc ('I hope it doesn't rain') — và hy vọng không phải là kế hoạch."),
  ]),
  ("How did the sampling go yesterday?", [
    ("Very well. We gave out 1,500 samples, and about 200 people scanned the QR code.", True, "Đánh giá chung + hai con số cụ thể."),
    ("It go very good.", False, "Sai thì và từ loại: 'It went very well.'"),
    ("Many people take, very crowded.", False, "Sai thì ('took'), thiếu số liệu cụ thể."),
  ]),
  ("The MC hasn't arrived, and we start in 20 minutes.", [
    ("I'll call him now. If he's not here in ten minutes, our brand manager can open the show.", True, "Hành động ngay + phương án dự phòng rõ ràng."),
    ("Wait more, maybe he come.", False, "Thiếu chủ ngữ, sai chia ('he'll come') và chỉ ngồi chờ."),
    ("Not my problem, I only do booth.", False, "Đẩy việc khi sự kiện gặp sự cố; thiếu mạo từ 'the booth'."),
  ]),
  ("Why is our booth so quiet?", [
    ("We're at the back of the hall. Let's move the sampling table to the aisle and ask two staff to invite people in.", True, "Nguyên nhân + hai hành động cụ thể."),
    ("Because people not interested.", False, "Thiếu 'are' và đổ lỗi cho khách."),
    ("Booth quiet is normal in the morning.", False, "Trật tự từ kiểu Việt ('It's normal for the booth to be quiet') và không đưa giải pháp."),
  ]),
  ("How many people came to the launch event?", [
    ("About 350 attendees, 50 more than we expected.", True, "Con số + so với kỳ vọng."),
    ("Have 350 people come.", False, "Dịch từng chữ 'có 350 người đến': 'About 350 people came.'"),
    ("Full, very full.", False, "Không có số liệu để báo cáo."),
  ]),
 ],
 "listen": [
  ("Setup starts at six on Saturday morning", ["Setup", "Saturday"], "giờ dựng sự kiện"),
  ("Our booth is next to the main entrance", ["booth", "entrance"], "vị trí gian hàng"),
  ("We gave out two thousand samples today", ["gave", "samples"], "kết quả phát mẫu thử"),
  ("Please check the run sheet before the show", ["run", "show"], "kịch bản chương trình"),
  ("The event starts at ten. The MC will open the show and introduce the product. Then we have a photo corner and free drinks.", ["MC", "introduce", "drinks"], "lịch trình sự kiện"),
  ("It might rain on Saturday. The venue has an indoor hall. We've booked it as a backup.", ["rain", "indoor", "backup"], "phương án dự phòng"),
 ],
})

# ───────────────────────── 6. PR & xử lý khủng hoảng ─────────────────────────
PHASES.append({
 "title": "PR & xử lý khủng hoảng",
 "vocab": [
  ("press release", "/ˈpres rɪˌliːs/", "n", "thông cáo báo chí", "We'll send the <b>press release</b> to twenty news sites.", "Mình sẽ gửi thông cáo báo chí cho hai mươi trang tin.", "プレスリリース", "puresu rirīsu"),
  ("journalist", "/ˈdʒɜːnəlɪst/", "n", "nhà báo, phóng viên", "A <b>journalist</b> called to ask about the new factory.", "Một phóng viên gọi đến hỏi về nhà máy mới.", "記者", "kisha"),
  ("media coverage", "/ˌmiːdiə ˈkʌvərɪdʒ/", "n", "mức độ báo chí đưa tin", "The launch got great <b>media coverage</b>: 35 articles.", "Buổi ra mắt được báo chí đưa tin rất nhiều: 35 bài."),
  ("statement", "/ˈsteɪtmənt/", "n", "thông báo chính thức, tuyên bố", "We'll post an official <b>statement</b> within two hours.", "Trong vòng hai tiếng mình sẽ đăng thông báo chính thức.", "声明", "seimei"),
  ("spokesperson", "/ˈspəʊkspɜːsn/", "n", "người phát ngôn", "Only our <b>spokesperson</b> can talk to the media.", "Chỉ người phát ngôn mới được trả lời báo chí.", "広報担当者", "kōhō tantōsha"),
  ("crisis", "/ˈkraɪsɪs/", "n", "khủng hoảng", "A small issue can turn into a <b>crisis</b> if we reply badly.", "Trả lời không khéo thì chuyện nhỏ cũng thành khủng hoảng.", "危機", "kiki"),
  ("backlash", "/ˈbæklæʃ/", "n", "làn sóng phản đối, bị 'ném đá'", "The joke in the ad caused a big <b>backlash</b> online.", "Câu đùa trong quảng cáo khiến dân mạng phản ứng dữ dội.", "炎上", "enjō"),
  ("recall", "/ˈriːkɔːl/", "n", "đợt thu hồi sản phẩm", "The company announced a <b>recall</b> of 2,000 bottles.", "Công ty thông báo thu hồi 2.000 chai.", "リコール", "rikōru"),
  ("misinformation", "/ˌmɪsɪnfəˈmeɪʃn/", "n", "thông tin sai lệch", "Let's correct the <b>misinformation</b> with clear facts.", "Mình đính chính thông tin sai lệch bằng dữ kiện rõ ràng."),
  ("transparent", "/trænsˈpærənt/", "adj", "minh bạch", "We need to be <b>transparent</b> about what went wrong.", "Mình cần minh bạch về những gì đã sai."),
 ],
 "phrases": [
  ("We're aware of the issue, and we're looking into it.", "Bên mình đã nắm được vấn đề và đang kiểm tra."),
  ("Please don't talk to the media. Pass them to our spokesperson.", "Đừng tự trả lời báo chí. Chuyển họ cho người phát ngôn nhé."),
  ("Let's get the facts first before we say anything.", "Mình nắm rõ sự việc trước rồi mới lên tiếng."),
  ("We'll post a short statement within two hours.", "Trong vòng hai tiếng mình sẽ đăng một thông báo ngắn."),
  ("We're sorry, and here's what we're doing to fix it.", "Chúng tôi xin lỗi, và đây là những gì chúng tôi đang làm để khắc phục."),
  ("Customers can return the product for a full refund.", "Khách có thể trả sản phẩm và được hoàn tiền toàn bộ."),
  ("Let's check the comments every hour tonight.", "Tối nay mình theo dõi bình luận mỗi tiếng một lần nhé."),
  ("The press release goes out at 10 a.m. tomorrow.", "Thông cáo báo chí phát đi lúc 10 giờ sáng mai."),
  ("Which journalists should we invite to the launch?", "Mình nên mời những phóng viên nào đến buổi ra mắt?"),
 ],
 "dialogues": [
  ("A journalist is calling about the complaint. What should I say?", [
    ("Please take her number and say our spokesperson will call back within an hour.", True, "Đúng quy trình: không tự phát ngôn, chuyển cho người phát ngôn và hẹn giờ."),
    ("Tell her no comment and hang up.", False, "Cúp máy với báo chí dễ bị viết là né tránh."),
    ("You explain everything to her, is OK.", False, "Nhân viên không được tự phát ngôn; câu thiếu chủ ngữ: 'it's OK'."),
  ]),
  ("People are angry about the joke in our ad. What now?", [
    ("Let's pause the ad now, post a short apology and check how it got approved.", True, "Dừng nguồn gây phản ứng + xin lỗi + rà lại quy trình duyệt."),
    ("It's only a joke. They are too sensitive.", False, "Coi thường cảm xúc khách hàng sẽ làm khủng hoảng lớn hơn."),
    ("We delete all comment and wait.", False, "Xoá bình luận làm tình hình tệ hơn; lại thiếu 's' ('comments')."),
  ]),
  ("A post says our snacks made kids sick. Is it true?", [
    ("We don't know yet. We're checking the batch with the quality team. I'll update you by 3 p.m.", True, "Trung thực + đang kiểm tra + hẹn giờ cập nhật."),
    ("Of course not, our products are always safe.", False, "Phủ nhận khi chưa kiểm tra — nếu sai sẽ mất uy tín rất nặng."),
    ("Maybe true, maybe fake news.", False, "Thiếu chủ ngữ ('It may be true') và không có hành động kiểm tra."),
  ]),
  ("Should we recall the product?", [
    ("If the tests find a problem, yes. Customer safety comes first, and it's better to act early.", True, "Đặt an toàn của khách lên đầu, quyết định dựa trên kết quả kiểm tra."),
    ("Recall is very expensive, we don't.", False, "Đặt chi phí lên trên an toàn của khách; thiếu 'do it'."),
    ("No, people will forget soon.", False, "Né tránh trách nhiệm — sai nguyên tắc xử lý khủng hoảng."),
  ]),
  ("How did the press release do?", [
    ("Very well. Twelve news sites published it, and two journalists asked for interviews.", True, "Kết quả có số liệu về độ phủ."),
    ("It publish on many site.", False, "Sai bị động và số nhiều: 'It was published on many sites.'"),
    ("Good, but I didn't count.", False, "Thiếu số liệu — làm PR phải đo được mức độ đưa tin."),
  ]),
 ],
 "listen": [
  ("Our spokesperson will call you back", ["spokesperson", "back"], "chuyển cuộc gọi của báo chí"),
  ("We'll post a short statement tonight", ["statement", "tonight"], "thông báo chính thức"),
  ("The press release goes out tomorrow morning", ["press", "morning"], "lịch phát thông cáo"),
  ("Please don't reply to journalists yourself", ["reply", "journalists"], "quy tắc phát ngôn"),
  ("We are aware of the problem. We are checking the batch with our quality team. We will share an update by three o'clock.", ["aware", "batch", "update"], "thông báo ban đầu khi có sự cố"),
  ("The ad caused a backlash online. We paused it this morning. The statement will go out at noon.", ["backlash", "paused", "noon"], "cập nhật tình hình khủng hoảng"),
 ],
})

# ───────────────────────── 7. Tối ưu chuyển đổi & A/B test ─────────────────────────
PHASES.append({
 "title": "Tối ưu chuyển đổi & A/B test",
 "vocab": [
  ("funnel", "/ˈfʌnl/", "n", "phễu (các bước từ lúc biết đến thương hiệu tới lúc mua)", "We lose most people in the middle of the <b>funnel</b>.", "Mình mất nhiều khách nhất ở giữa phễu.", "ファネル", "faneru"),
  ("drop-off", "/ˈdrɒp ɒf/", "n", "sự rời bỏ giữa chừng (ở một bước trong phễu)", "There's a big <b>drop-off</b> at the payment step.", "Khách rời bỏ rất nhiều ở bước thanh toán.", "離脱", "ridatsu"),
  ("variant", "/ˈveəriənt/", "n", "phiên bản (trong thử nghiệm)", "<b>Variant</b> B has a green button.", "Phiên bản B có nút màu xanh lá."),
  ("hypothesis", "/haɪˈpɒθəsɪs/", "n", "giả thuyết", "Our <b>hypothesis</b> is that a shorter form will get more sign-ups.", "Giả thuyết của mình là form ngắn hơn sẽ có nhiều lượt đăng ký hơn.", "仮説", "kasetsu"),
  ("sample size", "/ˈsɑːmpl saɪz/", "n", "cỡ mẫu (số người tham gia thử nghiệm)", "The <b>sample size</b> is too small to decide.", "Cỡ mẫu còn quá nhỏ để kết luận.", "サンプルサイズ", "sanpuru saizu"),
  ("significant", "/sɪɡˈnɪfɪkənt/", "adj", "có ý nghĩa thống kê (khác biệt đủ tin cậy, không phải do ngẫu nhiên)", "The difference is not <b>significant</b> yet.", "Chênh lệch này chưa có ý nghĩa thống kê."),
  ("heatmap", "/ˈhiːtmæp/", "n", "bản đồ nhiệt (cho thấy chỗ người dùng nhấp, cuộn nhiều)", "The <b>heatmap</b> shows that nobody scrolls to the bottom.", "Bản đồ nhiệt cho thấy không ai cuộn xuống cuối trang.", "ヒートマップ", "hīto mappu"),
  ("user journey", "/ˈjuːzə ˌdʒɜːni/", "n", "hành trình người dùng", "Let's map the <b>user journey</b> from the ad to payment.", "Mình vẽ lại hành trình người dùng từ quảng cáo đến thanh toán nhé."),
  ("friction", "/ˈfrɪkʃn/", "n", "điểm gây vướng, làm khách khó thao tác", "Asking for an account first adds <b>friction</b>.", "Bắt tạo tài khoản trước làm khách thêm vướng."),
  ("uplift", "/ˈʌplɪft/", "n", "mức tăng (so với bản gốc)", "The new page gave us a 12% <b>uplift</b> in orders.", "Trang mới giúp số đơn tăng 12% so với bản cũ."),
 ],
 "phrases": [
  ("Where exactly do people leave the funnel?", "Chính xác thì khách rời phễu ở bước nào?"),
  ("Let's test one change at a time.", "Mỗi lần mình chỉ thử một thay đổi thôi."),
  ("We need at least two weeks of data.", "Mình cần ít nhất hai tuần dữ liệu."),
  ("It's too early to call a winner.", "Còn quá sớm để chọn phiên bản thắng."),
  ("The payment page has too many steps.", "Trang thanh toán có quá nhiều bước."),
  ("What's our hypothesis for this test?", "Giả thuyết của mình cho thử nghiệm này là gì?"),
  ("The heatmap shows people click on the photo, not the button.", "Bản đồ nhiệt cho thấy khách nhấp vào ảnh chứ không nhấp vào nút."),
  ("Guest checkout could reduce the drop-off.", "Cho mua không cần tài khoản có thể giảm tỉ lệ bỏ dở."),
  ("The new version increased sign-ups by 15%.", "Phiên bản mới giúp lượt đăng ký tăng 15%."),
 ],
 "dialogues": [
  ("Variant B is winning after two days. Can we stop the test?", [
    ("Not yet. The sample size is still small. Let's wait until we have two full weeks.", True, "Giải thích lý do chưa kết luận + mốc thời gian."),
    ("Yes, B is win, stop now.", False, "Sai ngữ pháp ('B is winning'); dừng quá sớm dễ kết luận sai."),
    ("I don't know statistic.", False, "Thiếu 's' ('statistics') và né câu hỏi; nên nhờ người phân tích hỗ trợ."),
  ]),
  ("Where are we losing customers?", [
    ("Mostly at the payment step. About 60% leave when we ask them to create an account.", True, "Chỉ ra bước cụ thể + con số + nguyên nhân."),
    ("Customers lose at payment.", False, "Sai nghĩa: 'Customers lose' là khách bị thua; phải nói 'We lose customers at payment.'"),
    ("Everywhere a little.", False, "Mơ hồ, không chỉ ra bước có tỉ lệ rời bỏ cao nhất."),
  ]),
  ("What should we test next?", [
    ("A shorter sign-up form. My hypothesis is that fewer fields will mean more sign-ups.", True, "Đề xuất + giả thuyết rõ ràng."),
    ("We test everything together, faster.", False, "Thử nhiều thay đổi cùng lúc thì không biết thay đổi nào tạo ra kết quả."),
    ("Change color button, maybe good.", False, "Trật tự từ kiểu Việt ('change the button colour') và không có giả thuyết."),
  ]),
  ("The test showed no difference. Was it a waste of time?", [
    ("Not really. Now we know the price isn't the problem, so we can test the photos next.", True, "Rút ra bài học từ kết quả + bước tiếp theo."),
    ("Yes, waste, sorry.", False, "Cộc lốc và hiểu sai — 'không có khác biệt' vẫn là thông tin có giá trị."),
    ("The test is not success.", False, "Sai từ loại và thì: 'The test wasn't successful.' / 'It didn't show a difference.'"),
  ]),
  ("How much did the new product page improve sales?", [
    ("We saw a 9% uplift in orders over three weeks, and the result is significant.", True, "Con số + thời gian + độ tin cậy."),
    ("It improve many.", False, "Sai thì và từ: 'It improved sales a lot.' — và cần con số."),
    ("Sales up because new page beautiful.", False, "Thiếu động từ 'is' và giải thích cảm tính."),
  ]),
 ],
 "listen": [
  ("We lose most people at the payment step", ["lose", "payment"], "điểm rời bỏ trong phễu"),
  ("Variant B has a bigger button", ["Variant", "button"], "khác biệt giữa hai phiên bản"),
  ("It's too early to pick a winner", ["early", "winner"], "chưa kết luận thử nghiệm"),
  ("The heatmap shows nobody scrolls to the bottom", ["heatmap", "bottom"], "đọc bản đồ nhiệt"),
  ("Our hypothesis is simple. A shorter form will get more sign-ups. We'll run the test for two weeks.", ["hypothesis", "shorter", "weeks"], "đề xuất thử nghiệm"),
  ("The new payment page is live. Orders went up by nine percent. We don't ask for an account anymore.", ["live", "nine", "account"], "kết quả tối ưu trang"),
 ],
})

# ───────────────────────── 8. Ngân sách & kế hoạch năm ─────────────────────────
PHASES.append({
 "title": "Ngân sách & kế hoạch năm",
 "vocab": [
  ("annual plan", "/ˌænjuəl ˈplæn/", "n", "kế hoạch năm", "The <b>annual plan</b> is due at the end of November.", "Kế hoạch năm phải nộp vào cuối tháng Mười Một.", "年間計画", "nenkan keikaku"),
  ("forecast", "/ˈfɔːkɑːst/", "n/v", "dự báo", "Our sales <b>forecast</b> for next year is 12 billion dong.", "Dự báo doanh số năm sau của mình là 12 tỷ đồng.", "予測", "yosoku"),
  ("allocate", "/ˈæləkeɪt/", "v", "phân bổ (ngân sách, nguồn lực)", "We <b>allocate</b> 40% of the budget to video.", "Mình phân bổ 40% ngân sách cho video."),
  ("media plan", "/ˈmiːdiə plæn/", "n", "kế hoạch truyền thông (kênh, thời gian, ngân sách)", "The <b>media plan</b> shows which channels we use each month.", "Kế hoạch truyền thông cho thấy mỗi tháng mình dùng kênh nào.", "メディアプラン", "media puran"),
  ("quarter", "/ˈkwɔːtə/", "n", "quý", "We'll spend more in the fourth <b>quarter</b> because of the year-end sales.", "Quý bốn mình sẽ chi nhiều hơn vì có các đợt sale cuối năm.", "四半期", "shihanki"),
  ("ROI", "/ˌɑːr əʊ ˈaɪ/", "n", "tỉ suất hoàn vốn (return on investment) = (lợi nhuận thu về − chi phí) ÷ chi phí", "Email has the best <b>ROI</b> of all our channels.", "Email có tỉ suất hoàn vốn tốt nhất trong các kênh của mình.", "費用対効果", "hiyō tai kōka"),
  ("CPA", "/ˌsiː piː ˈeɪ/", "n", "chi phí cho mỗi khách/đơn có được (cost per acquisition) = chi phí ÷ số khách (đơn) mới", "Our <b>CPA</b> on search ads is 90,000 dong.", "CPA của quảng cáo tìm kiếm là 90.000 đồng."),
  ("overspend", "/ˌəʊvəˈspend/", "v", "chi vượt ngân sách", "We <b>overspent</b> on influencers in March.", "Tháng Ba mình chi vượt ngân sách cho influencer."),
  ("contingency", "/kənˈtɪndʒənsi/", "n", "khoản dự phòng", "Keep 10% of the budget as a <b>contingency</b>.", "Giữ 10% ngân sách làm khoản dự phòng."),
  ("sign off", "/ˌsaɪn ˈɒf/", "phr v", "ký duyệt, phê duyệt chính thức", "The CEO needs to <b>sign off</b> on the budget.", "Tổng giám đốc cần ký duyệt ngân sách.", "承認する", "shōnin suru"),
 ],
 "phrases": [
  ("Here's how we plan to split the budget next year.", "Đây là cách mình dự định chia ngân sách năm sau."),
  ("We want to move 20% from TV to online video.", "Mình muốn chuyển 20% ngân sách từ TV sang video online."),
  ("Which channel gave us the best ROI this year?", "Năm nay kênh nào cho tỉ suất hoàn vốn tốt nhất?"),
  ("We're 5% over budget this quarter.", "Quý này mình vượt ngân sách 5%."),
  ("Let's keep some money for things we can't plan.", "Mình giữ lại một ít tiền cho những việc không lường trước."),
  ("Q4 is our biggest season, so we'll spend more then.", "Quý 4 là mùa cao điểm nên mình sẽ chi nhiều hơn vào lúc đó."),
  ("Can you break the budget down by month?", "Bạn chia nhỏ ngân sách theo từng tháng được không?"),
  ("We need the final numbers by Friday for approval.", "Mình cần số liệu cuối trước thứ Sáu để trình duyệt."),
  ("If we cut the budget, we'll get fewer new customers.", "Nếu cắt ngân sách, mình sẽ có ít khách mới hơn."),
 ],
 "dialogues": [
  ("Why do you want more budget for search ads next year?", [
    ("Search has our lowest CPA, about 90,000 dong per customer. More budget there should bring the most new customers.", True, "Lập luận bằng chỉ số chi phí + kết quả kỳ vọng."),
    ("Because other team get more budget.", False, "So bì với nhóm khác không phải lý do; sai ngữ pháp ('other teams get')."),
    ("Search ads is good, trust me.", False, "Sai chia ('are') và không có số liệu chứng minh."),
  ]),
  ("We're over budget in March. What happened?", [
    ("We overspent on influencers for the launch. I'll cut paid posts in April to balance it.", True, "Nêu nguyên nhân + phương án bù lại."),
    ("March is special month.", False, "Thiếu mạo từ ('a special month') và không giải thích cụ thể."),
    ("I not know, finance team calculate.", False, "Thiếu trợ động từ ('I don't know') và đẩy việc cho phòng tài chính."),
  ]),
  ("Management wants to cut the marketing budget by 15%. What would you cut?", [
    ("I'd cut the channels with the lowest ROI first, like print ads, and protect search and email.", True, "Cắt theo hiệu quả, giữ lại kênh tốt."),
    ("Cut all channels 15%, same same.", False, "Cắt đều không dựa trên hiệu quả; 'same same' là kiểu nói tiếng Việt."),
    ("We cannot cut, marketing is important.", False, "Từ chối không có lập luận, thiếu tinh thần hợp tác."),
  ]),
  ("Do we need a contingency in the budget?", [
    ("Yes. I'd keep 10% for surprises, like a competitor's big sale.", True, "Đồng ý + mức cụ thể + ví dụ thực tế."),
    ("No need, we plan very careful.", False, "Sai từ loại ('carefully') và chủ quan — kế hoạch nào cũng cần dự phòng."),
    ("Yes, contingency is need.", False, "Sai cấu trúc: 'Yes, we need one.' / 'Yes, it's needed.'"),
  ]),
  ("When can the CEO sign off on the plan?", [
    ("After Thursday's review. If there are no big changes, we'll have approval on Friday.", True, "Mốc thời gian + điều kiện rõ ràng."),
    ("CEO sign when he free.", False, "Thiếu mạo từ và động từ: 'The CEO will sign it when he's free.' — và không có mốc."),
    ("Maybe next month, I'm not sure when.", False, "Mơ hồ — các nhóm cần mốc thời gian để lên kế hoạch."),
  ]),
 ],
 "listen": [
  ("The annual plan is due in November", ["annual", "November"], "hạn nộp kế hoạch năm"),
  ("We keep ten percent as a contingency", ["ten", "contingency"], "khoản dự phòng"),
  ("Email has the best ROI of all our channels", ["ROI", "channels"], "kênh hiệu quả nhất"),
  ("We are five percent over budget this quarter", ["budget", "quarter"], "tình hình ngân sách"),
  ("Next year's budget is ten billion dong. Forty percent goes to video. We will spend the most in the fourth quarter.", ["billion", "video", "fourth"], "tóm tắt ngân sách năm"),
  ("We overspent on influencers in March. In April we will spend less on paid posts. By June we should be back on budget.", ["overspent", "April", "June"], "điều chỉnh chi tiêu"),
 ],
})

# ───────────────────────── Vai trò: nội dung nối thêm ─────────────────────────
ROLES = {
 "digital": {
  "scenarios": [
   ("dg_email", "Tối ưu luồng email tự động", "You are my foreign CRM manager. Our abandoned cart emails bring very few orders. Ask me how the flow works now and what I will change: timing, subject lines or vouchers."),
   ("dg_cro", "Đề xuất sửa trang thanh toán", "You are the product owner of our online store. I want to remove the 'create an account' step at checkout. Ask about the data behind my idea, the risks and how we will test it."),
  ],
  "dialogues": [
   ("How many orders did the abandoned cart email bring last month?", [
     ("About 180 orders. That's 6% of all our online sales.", True, "Con số + tỉ trọng trên tổng doanh số."),
     ("It bring 180 orders.", False, "Sai thì: 'It brought 180 orders last month.'"),
     ("Some orders, not many.", False, "Mơ hồ, không có con số.")]),
   ("Should we send the reminder after one hour or one day?", [
     ("Let's test both. I think one hour will work better, because people still remember the product.", True, "Đề xuất thử nghiệm + giả thuyết có lý do."),
     ("One day is more polite, I think so.", False, "Sau câu khẳng định chỉ nói 'I think', không thêm 'so'; lại không dựa trên dữ liệu."),
     ("Whatever, both same.", False, "Cộc lốc, thiếu tinh thần tối ưu.")]),
   ("Our organic traffic dropped this week. Is it because of our ads?", [
     ("Probably not. Paid ads don't change organic rankings. I'll check if any pages broke after the update.", True, "Sửa hiểu lầm + hướng kiểm tra cụ thể."),
     ("Yes, maybe ads make traffic go down.", False, "Sai kiến thức: quảng cáo trả phí không làm tụt thứ hạng tự nhiên."),
     ("I not sure about it.", False, "Thiếu động từ 'am': 'I'm not sure.' — và nên nói sẽ kiểm tra.")]),
   ("Can you show the funnel in the weekly report?", [
     ("Sure. I'll show each step from ad click to payment, with the drop-off at each step.", True, "Nhận việc + mô tả cách trình bày."),
     ("Sure, I will showing it.", False, "Sau 'will' dùng nguyên thể: 'I'll show it.'"),
     ("Funnel is difficult to show.", False, "Né việc; thiếu mạo từ 'The funnel'.")]),
  ]},
 "content": {
  "scenarios": [
   ("ct_script", "Duyệt kịch bản video ngắn", "You are my foreign creative lead. Review my script for a 30-second product video. Ask about the hook in the first three seconds, the subtitles and the call to action."),
   ("ct_pr", "Soạn thông báo khi bị phản ứng", "You are the head of communications. Our latest post caused a backlash online. Ask me to draft a short public statement, and check that it is honest, calm and clear."),
  ],
  "dialogues": [
   ("Can you write the first line of the video script?", [
     ("How about: 'Still eating instant noodles at your desk?' It speaks to our customers' pain point.", True, "Đưa câu mở cụ thể + lý do bám insight."),
     ("OK, first line I write later.", False, "Trật tự từ kiểu Việt và thiếu 'will': 'I'll write it later.' — tốt hơn là gợi ý luôn."),
     ("First line is not important.", False, "Sai nghề — câu mở quyết định người xem có ở lại không.")]),
   ("Our post is getting angry comments. Should we delete it?", [
     ("Not yet. Let's pin a short reply, explain what we meant and say sorry if we were wrong.", True, "Không xoá vội, phản hồi minh bạch."),
     ("Yes, delete fast, nobody will know.", False, "Xoá vội vẫn bị chụp màn hình, phản ứng còn mạnh hơn."),
     ("I think should we delete.", False, "Sai trật tự: 'I think we should delete it.'")]),
   ("Does this caption match our tone of voice?", [
     ("Mostly, but 'Buy now or regret it!' sounds too pushy. Let's make it friendlier.", True, "Nhận xét cụ thể + hướng sửa."),
     ("Yes, is match.", False, "Thiếu chủ ngữ và sai động từ: 'Yes, it matches.'"),
     ("Tone is not problem, only sell.", False, "Bỏ qua quy chuẩn thương hiệu; thiếu mạo từ, câu cụt.")]),
   ("Can we reuse the livestream video on our channel?", [
     ("Yes. I'll cut the best two minutes and add subtitles.", True, "Đồng ý + cách xử lý cụ thể."),
     ("Yes, we upload all two hours.", False, "Video hai tiếng ít người xem hết; thiếu 'will' và nên cắt ngắn."),
     ("Can, but who cut?", False, "Thiếu chủ ngữ, câu cộc: 'Yes, but who will edit it?'")]),
  ]},
 "ecom": {
  "scenarios": [
   ("ec_live", "Livestream bán hàng trên sàn", "You are my foreign e-commerce manager. I will host a two-hour livestream on the Shopza marketplace tonight. Ask about the product order, vouchers, giveaways and what I will do if stock runs out."),
   ("ec_recall", "Dừng bán lô hàng lỗi", "You are my manager. A batch of our products may be faulty. Ask me how I will stop sales on the marketplaces, what we will tell customers who already bought it and how refunds will work."),
  ],
  "dialogues": [
   ("The air fryer sold out during the livestream. What now?", [
     ("I'll tell viewers it's sold out, move to the next product and offer pre-orders for next week.", True, "Minh bạch với người xem + chuyển hướng + giữ doanh số."),
     ("Continue sell, we deliver later.", False, "Bán khi đã hết hàng dễ giao trễ, huỷ đơn; câu thiếu chủ ngữ và sai 'keep selling'."),
     ("Sold out, finish live.", False, "Dừng live đột ngột làm mất khách; câu cộc lốc.")]),
   ("How many viewers did we have at the peak?", [
     ("About 2,800, around 9 p.m. when we started the giveaway.", True, "Con số + thời điểm + lý do."),
     ("Peak is 2,800 people watch.", False, "Sai cấu trúc: 'At the peak, 2,800 people were watching.'"),
     ("Many, the chat was very fast.", False, "Không có số liệu cụ thể.")]),
   ("We need to stop selling batch 0925. How fast can you do it?", [
     ("I can hide all the listings on both marketplaces within 30 minutes.", True, "Mốc thời gian cụ thể + phạm vi rõ ràng."),
     ("Why stop? It still sell well.", False, "Đặt doanh số lên trên an toàn; sai chia ('It's still selling well')."),
     ("I try, but I don't know how long.", False, "Thiếu 'will' ('I'll try') và mơ hồ.")]),
   ("A customer asks why she can't find our product anymore.", [
     ("Let's tell her we paused sales for a quality check, and she can get a full refund if she bought that batch.", True, "Minh bạch + thông tin hoàn tiền."),
     ("Tell her the product is out of stock.", False, "Nói sai sự thật với khách, mất uy tín nếu bị lộ."),
     ("Don't reply, wait boss.", False, "Thiếu 'for the' ('wait for the boss') và bỏ mặc khách.")]),
  ]},
 "brand": {
  "scenarios": [
   ("br_event", "Chốt kế hoạch sự kiện với khách", "You are a foreign client. Our agency is running your brand's weekend activation at a shopping mall. Ask about the venue, the run sheet, the sampling target and the plan if it rains."),
   ("br_cut", "Khách cắt ngân sách giữa chừng", "You are a client who must cut the campaign budget by 30% next month. Ask me what we can still deliver and how the results will change. Accept if my plan is clear."),
  ],
  "dialogues": [
   ("Can you send me the run sheet for Saturday?", [
     ("Sure. I'll send it by 5 p.m. today, with every staff member's role and timing.", True, "Hẹn giờ gửi + nội dung kèm theo."),
     ("Sure, I send you now now.", False, "Lặp 'now now' kiểu tiếng Việt và thiếu 'will': 'I'll send it right now.'"),
     ("Run sheet is not finish.", False, "Sai: 'The run sheet isn't finished yet.' — và cần hẹn giờ gửi.")]),
   ("We have to cut the budget by 30%. What can you still do?", [
     ("We can keep the videos and the main influencer, but we'd have to drop the event. Reach will be about 25% lower.", True, "Nêu giữ gì, bỏ gì + ảnh hưởng dự kiến."),
     ("Same work, less money is impossible.", False, "Từ chối mà không đưa phương án nào."),
     ("OK, we do everything same.", False, "Hứa làm như cũ với ít tiền hơn là không thực tế; sai 'the same'.")]),
   ("Our new logo looks a lot like a competitor's. Is that a problem?", [
     ("It could be. Let's ask the legal team to check before we print anything.", True, "Thận trọng + kiểm tra pháp lý trước khi in."),
     ("No problem, many logos look same.", False, "Rủi ro pháp lý; thiếu 'the' ('look the same')."),
     ("I think no one notice.", False, "Sai chia ('notices') và chủ quan.")]),
   ("How many people visited the booth last weekend?", [
     ("About 1,200, and 300 of them joined our member list.", True, "Con số + kết quả thu được."),
     ("Have 1,200 people visit.", False, "Dịch từng chữ 'có 1.200 người': 'About 1,200 people visited.'"),
     ("Very crowded, I can't count.", False, "Không có số liệu để báo cáo khách.")]),
  ]},
}

EXTRA = {
 "phases": PHASES,
 "rev": [
  ("Tỉ lệ mở email tuần này là 30%.", "This week's email open rate is 30%."),
  ("Mình chỉ gửi email cho khách đã đồng ý nhận tin.", "We only email customers who opted in."),
  ("Trang chủ tải quá chậm trên điện thoại.", "The homepage loads too slowly on mobile."),
  ("Từ khoá này có lượng tìm kiếm cao.", "This keyword has a high search volume."),
  ("Tối nay 8 giờ mình lên sóng.", "We go live at 8 tonight."),
  ("Ghim voucher lên khung chat giúp em nhé.", "Please pin the voucher in the chat."),
  ("Đừng đổi màu logo.", "Don't change the colour of the logo."),
  ("Hình ảnh phải đồng bộ trên mọi kênh.", "Our look must be consistent on every channel."),
  ("Gian hàng của mình ở cạnh lối vào chính.", "Our booth is next to the main entrance."),
  ("Mình cần phương án dự phòng nếu trời mưa.", "We need a plan B if it rains."),
  ("Chỉ người phát ngôn được trả lời báo chí.", "Only our spokesperson can talk to the media."),
  ("Bên mình đang kiểm tra sự việc.", "We're looking into it."),
  ("Còn quá sớm để chọn phiên bản thắng.", "It's too early to pick a winner."),
  ("Khách rời bỏ nhiều nhất ở bước thanh toán.", "Most customers leave at the payment step."),
  ("Quý này mình vượt ngân sách 5%.", "We're 5% over budget this quarter."),
  ("Tổng giám đốc cần duyệt kế hoạch trước thứ Sáu.", "The CEO needs to sign off on the plan by Friday."),
 ],
 "reading": [
  {"t": "Email campaign report", "text": "Email report – 'Mid-Autumn Gift Box' (sent 10 Sept)\nSent: 18,400 | Delivered: 18,050\nOpen rate: 27% (last campaign: 22%)\nClick rate: 3.1%\nUnsubscribes: 64\nOrders from email: 212\nNote: Subject line B ('Your gift box is waiting') won the test and was sent to the rest of the list.", "q": [
    {"q": "Which number is compared with the last campaign?", "o": ["The open rate", "The number of unsubscribes", "The number of orders"], "a": 0},
    {"q": "What happened with subject line B?", "o": ["It was not used", "It won and went to the rest of the list", "It went to the spam folder"], "a": 1}]},
  {"t": "Livestream run sheet", "text": "LIVESTREAM RUN SHEET – Friday, 8:00–10:00 p.m.\n7:30 Host and camera check\n8:00 Welcome + pin voucher LIVE50 (50,000 dong off, min. spend 300,000 dong)\n8:15 Product 1: rice cooker (live demo)\n8:45 Giveaway #1: comment to win\n9:00 Product 2: air fryer\n9:40 Last call: the voucher ends at 10:00 p.m.", "q": [
    {"q": "When does the voucher end?", "o": ["At 8:00 p.m.", "At 9:40 p.m.", "At 10:00 p.m."], "a": 2},
    {"q": "What must viewers do to win the first giveaway?", "o": ["Share the video", "Leave a comment", "Buy the air fryer"], "a": 1}]},
  {"t": "Email from the event team", "text": "Hi team,\nHere is the final info for the Green Living Fair:\n- Booth 24, Hall B (near the main entrance)\n- Setup: Friday, 2–6 p.m. Please wear the green team T-shirt.\n- Fair hours: Saturday and Sunday, 9 a.m.–8 p.m.\n- Sampling target: 3,000 cups of tea. Ask visitors to scan the QR code to get a voucher.\n- Any power problems: go to the venue info desk.\nThanks,\nLan", "q": [
    {"q": "When is the setup?", "o": ["Friday afternoon", "Saturday morning", "Sunday evening"], "a": 0},
    {"q": "What do visitors get if they scan the QR code?", "o": ["A free T-shirt", "A voucher", "A booth ticket"], "a": 1}]},
  {"t": "Official statement", "text": "Statement from Bamboo Bites – 14 October\nWe are aware of posts saying that some bags of our mango crackers had a strange smell. Customer safety is our top priority. We have stopped selling batch 0925 while our quality team checks it. Customers who bought this batch can return it at any store for a full refund. We will share the test results by 18 October.", "q": [
    {"q": "What has the company done so far?", "o": ["Closed all its stores", "Stopped selling one batch", "Changed the recipe"], "a": 1},
    {"q": "When will the company share the test results?", "o": ["By 14 October", "By 18 October", "Next month"], "a": 1}]},
  {"t": "Annual budget draft", "text": "2027 Marketing budget – draft v2 (for sign-off)\nTotal: 6 billion dong\nPaid social 35% | Search ads 25% | Influencers 15% | Events 10% | Email 5% | Contingency 10%\nBiggest spend: Q4 (11.11 and 12.12 sales)\nChanges from v1: events cut from 15% to 10%; contingency added.\nPlease send comments by 28 November.", "q": [
    {"q": "Which channel gets the biggest share?", "o": ["Search ads", "Paid social", "Influencers"], "a": 1},
    {"q": "What changed from version 1?", "o": ["Events got less money", "Search ads were removed", "The total budget doubled"], "a": 0}]},
 ],
 "ai": [
  ("email", "Báo cáo email marketing", "You are my foreign marketing manager. Ask me about our last email campaign: open rate, clicks, unsubscribes and orders. Ask what I will test in the next email."),
  ("seo", "Họp về SEO website", "You are the head of digital at our company. Our organic traffic dropped 25% this month. Ask me what happened, which pages were affected and what my plan is."),
  ("crisis", "Xử lý khủng hoảng truyền thông", "You are the brand director. A customer's post saying our product is unsafe is spreading fast. Ask me what we know, what we will say publicly and how fast we can respond."),
  ("budget", "Bảo vệ ngân sách năm", "You are the CFO of a consumer brand. Review my marketing budget for next year. Ask why each channel gets its share and what ROI I expect, and push back on one line."),
 ],
 "events": [
  ("fair", "Hội chợ triển lãm", "You are a foreign visitor at our booth at a trade fair. Ask about our products, prices for bulk orders and whether we can ship abroad. Be friendly but in a hurry."),
  ("press", "Họp báo ra mắt", "You are a journalist at our product launch press event. Ask me about the new product, the price and where people can buy it, then ask one tricky question about a past customer complaint."),
  ("planning", "Họp kế hoạch marketing năm", "You are my regional director at the annual planning meeting. Ask about my goals for next year, the budget split, the biggest risks and how I will measure success."),
 ],
 "quips": [
  "Open rate is up!",
  "Don't forget to pin the voucher!",
  "Page one on search!",
  "Stay calm and check the facts.",
  "Variant B for the win!",
  "Is that in the budget?",
 ],
 "roles": ROLES,
}
