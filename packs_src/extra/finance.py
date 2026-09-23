# -*- coding: utf-8 -*-
# v4.1 — nội dung làm giàu cho gói finance (nối vào cuối gói, xem build.py)
# Số liệu thuế/bảo hiểm/tài sản chỉ ở mức phổ thông (VN): BHXH người lao động 10,5% (8% + 1,5% + 1%),
# ngưỡng TSCĐ ≥ 30 triệu đồng & dùng > 1 năm, làm thêm ngày nghỉ hằng tuần ≥ 200%. Không thay tư vấn chuyên môn.

PHASES = []

# ───────────────────────── 10. Lương & bảo hiểm ─────────────────────────
PHASES.append({
 "title": "Lương & bảo hiểm",
 "vocab": [
  ("payroll", "/ˈpeɪrəʊl/", "n", "bảng lương; việc tính và chi lương", "We run <b>payroll</b> on the 25th of every month.", "Bên mình chạy lương vào ngày 25 hằng tháng.", "給与計算", "kyūyo keisan"),
  ("payslip", "/ˈpeɪslɪp/", "n", "phiếu lương", "You can download your <b>payslip</b> from the HR portal.", "Anh/chị có thể tải phiếu lương trên cổng thông tin nhân sự.", "給与明細", "kyūyo meisai"),
  ("gross salary", "/ˌɡrəʊs ˈsæləri/", "n", "lương gộp (trước thuế và bảo hiểm)", "Your <b>gross salary</b> is 25 million dong a month.", "Lương gộp của anh/chị là 25 triệu đồng mỗi tháng."),
  ("net pay", "/ˌnet ˈpeɪ/", "n", "lương thực nhận", "Your <b>net pay</b> is what you receive after tax and insurance.", "Lương thực nhận là số tiền anh/chị nhận sau khi trừ thuế và bảo hiểm.", "手取り", "tedori"),
  ("social insurance", "/ˌsəʊʃl ɪnˈʃʊərəns/", "n", "bảo hiểm xã hội", "Both the company and the employee pay <b>social insurance</b> every month.", "Hằng tháng cả công ty và người lao động đều đóng bảo hiểm xã hội.", "社会保険", "shakai hoken"),
  ("overtime pay", "/ˈəʊvətaɪm peɪ/", "n", "tiền làm thêm giờ", "<b>Overtime pay</b> on weekends is at least 200% of the normal rate.", "Tiền làm thêm vào ngày nghỉ hằng tuần ít nhất bằng 200% lương thường.", "残業代", "zangyōdai"),
  ("allowance", "/əˈlaʊəns/", "n", "phụ cấp", "Staff get a lunch <b>allowance</b> of 800,000 dong a month.", "Nhân viên được phụ cấp ăn trưa 800.000 đồng mỗi tháng.", "手当", "teate"),
  ("bonus", "/ˈbəʊnəs/", "n", "tiền thưởng", "The Tet <b>bonus</b> will be paid with January's salary.", "Thưởng Tết sẽ được trả cùng lương tháng Một.", "賞与", "shōyo"),
  ("dependant", "/dɪˈpendənt/", "n", "người phụ thuộc (để giảm trừ gia cảnh)", "You can register your son as a <b>dependant</b> to pay less tax.", "Anh/chị có thể đăng ký con trai là người phụ thuộc để được giảm thuế.", "扶養家族", "fuyō kazoku"),
  ("deduction", "/dɪˈdʌkʃn/", "n", "khoản khấu trừ (vào lương); khoản giảm trừ", "The <b>deductions</b> on your payslip are tax and insurance.", "Các khoản trừ trên phiếu lương là thuế và bảo hiểm.", "控除", "kōjo"),
 ],
 "phrases": [
  ("Salaries will be paid on Friday, the 25th.", "Lương sẽ được trả vào thứ Sáu, ngày 25."),
  ("Please send me the overtime hours by the 20th.", "Anh/chị gửi tôi số giờ làm thêm trước ngày 20 nhé."),
  ("Your payslip shows your gross salary and all deductions.", "Phiếu lương thể hiện lương gộp và tất cả các khoản trừ."),
  ("Employees pay 10.5% of their insured salary for insurance.", "Người lao động đóng bảo hiểm bằng 10,5% mức lương đóng bảo hiểm."),
  ("Please send your personal tax code so we can register your dependants.", "Anh/chị gửi mã số thuế cá nhân để bên mình đăng ký người phụ thuộc nhé."),
  ("The bonus is taxed together with your salary for that month.", "Tiền thưởng được tính thuế cùng lương của tháng đó."),
  ("I've checked your payslip, and the overtime was missing.", "Tôi đã kiểm tra phiếu lương, đúng là bị thiếu tiền làm thêm giờ."),
  ("We'll pay the difference in next month's payroll.", "Phần chênh lệch sẽ được trả trong kỳ lương tháng sau."),
  ("Payroll information is confidential, so I can't share it.", "Thông tin lương là bảo mật nên tôi không chia sẻ được."),
 ],
 "dialogues": [
  ("Why is my net pay lower this month?", [
    ("You took two days of unpaid leave in May, so they were deducted from this month's pay. I can send you the details.", True, "Nêu lý do cụ thể + đề nghị gửi chi tiết."),
    ("Because tax.", False, "Câu cụt, thiếu động từ; cần nói rõ khoản nào bị trừ và vì sao."),
    ("I don't know, maybe HR make mistake.", False, "Đổ lỗi khi chưa kiểm tra; sai ngữ pháp ('HR made a mistake')."),
  ]),
  ("My overtime isn't on my payslip.", [
    ("Sorry about that. Could you send me your approved overtime form? If it's correct, we'll add it to next month's pay.", True, "Xin lỗi + xin chứng từ đã duyệt + cách trả bù."),
    ("Overtime is not my job.", False, "Né tránh; kế toán lương cần kiểm tra giúp."),
    ("You no send the form.", False, "Sai ngữ pháp ('You didn't send the form') và nghe như trách móc."),
  ]),
  ("How much insurance do I pay each month?", [
    ("You pay 10.5% of your insured salary: 8% social, 1.5% health and 1% unemployment insurance.", True, "Tỷ lệ tổng + chi tiết từng loại bảo hiểm."),
    ("Insurance is 10.5, the law.", False, "Thiếu đơn vị %, thiếu căn cứ tính và câu không trọn ý."),
    ("Company pays all, you pay nothing.", False, "Sai thông tin: người lao động cũng phải đóng phần của mình."),
  ]),
  ("Can you tell me how much my manager earns?", [
    ("Sorry, I can't. Payroll information is confidential.", True, "Từ chối lịch sự + lý do bảo mật."),
    ("He earn more than you.", False, "Tiết lộ thông tin lương; sai chia động từ ('earns')."),
    ("Why you want to know?", False, "Sai trật tự câu hỏi ('Why do you want to know?') và chưa nêu quy định bảo mật."),
  ]),
  ("I had a baby last month. Can I pay less tax?", [
    ("Congratulations! Yes, you can register your baby as a dependant. Please send me the birth certificate.", True, "Chúc mừng + xác nhận + giấy tờ cần nộp."),
    ("Yes, less tax, no problem.", False, "Hứa chung chung, không nói thủ tục đăng ký người phụ thuộc."),
    ("Baby is not relate to tax.", False, "Sai kiến thức (con là người phụ thuộc) và sai ngữ pháp ('isn't related to')."),
  ]),
 ],
 "listen": [
  ("Salaries will be paid on the twenty-fifth", ["Salaries", "twenty-fifth"], "ngày trả lương"),
  ("Please check the deductions on your payslip", ["deductions", "payslip"], "kiểm tra phiếu lương"),
  ("Your overtime pay will be added next month", ["overtime", "added"], "trả bù tiền làm thêm"),
  ("You can register your children as dependants", ["register", "dependants"], "đăng ký người phụ thuộc"),
  ("Hi everyone, payroll closes on the 20th. Please send your overtime forms by then. Late forms will be paid next month.", ["closes", "overtime", "Late"], "thông báo chốt lương"),
  ("The Tet bonus will be paid on 15 January. It will be taxed with your January salary. Your payslip will show the details.", ["bonus", "taxed", "details"], "thông báo thưởng Tết"),
 ],
})

# ───────────────────────── 11. Tài sản cố định & khấu hao ─────────────────────────
PHASES.append({
 "title": "Tài sản cố định & khấu hao",
 "vocab": [
  ("fixed asset", "/ˌfɪkst ˈæset/", "n", "tài sản cố định", "This laptop costs under 30 million dong, so we don't record it as a <b>fixed asset</b>.", "Laptop này dưới 30 triệu đồng nên mình không ghi nhận là tài sản cố định.", "固定資産", "kotei shisan"),
  ("useful life", "/ˌjuːsfl ˈlaɪf/", "n", "thời gian sử dụng hữu ích (thời gian trích khấu hao)", "The <b>useful life</b> of this truck is eight years.", "Thời gian sử dụng của xe tải này là tám năm.", "耐用年数", "taiyō nensū"),
  ("straight-line", "/ˌstreɪt ˈlaɪn/", "adj", "(khấu hao) theo đường thẳng", "We use the <b>straight-line</b> method for all our machines.", "Bên mình khấu hao theo đường thẳng cho tất cả máy móc.", "定額法", "teigakuhō"),
  ("asset register", "/ˈæset ˌredʒɪstə/", "n", "sổ theo dõi tài sản cố định", "Please add the new packing machine to the <b>asset register</b>.", "Anh/chị thêm máy đóng gói mới vào sổ theo dõi tài sản nhé.", "固定資産台帳", "kotei shisan daichō"),
  ("asset tag", "/ˈæset tæɡ/", "n", "tem mã tài sản", "Every laptop has an <b>asset tag</b> with a barcode.", "Mỗi laptop đều có tem mã tài sản kèm mã vạch."),
  ("net book value", "/ˌnet bʊk ˈvæljuː/", "n", "giá trị còn lại (trên sổ sách)", "The <b>net book value</b> of the old car is 120 million dong.", "Giá trị còn lại của chiếc xe cũ là 120 triệu đồng.", "帳簿価額", "chōbo kagaku"),
  ("residual value", "/rɪˌzɪdjuəl ˈvæljuː/", "n", "giá trị thanh lý ước tính", "We expect a <b>residual value</b> of about 10% after five years.", "Mình ước tính giá trị thanh lý khoảng 10% sau năm năm.", "残存価額", "zanzon kagaku"),
  ("capitalise", "/ˈkæpɪtəlaɪz/", "v", "ghi tăng vào nguyên giá tài sản (vốn hoá)", "We can <b>capitalise</b> the installation cost with the machine.", "Chi phí lắp đặt được ghi tăng vào nguyên giá của máy.", "資産計上する", "shisan keijō suru"),
  ("disposal", "/dɪˈspəʊzl/", "n", "thanh lý, nhượng bán tài sản", "The <b>disposal</b> of the old forklift needs the director's approval.", "Thanh lý xe nâng cũ cần giám đốc phê duyệt."),
  ("write off", "/ˌraɪt ˈɒf/", "v", "xoá sổ, ghi giảm toàn bộ", "We had to <b>write off</b> the broken scanner.", "Bên mình phải ghi giảm chiếc máy scan bị hỏng."),
 ],
 "phrases": [
  ("Items of 30 million dong or more that last over a year are fixed assets.", "Tài sản từ 30 triệu đồng trở lên và dùng trên một năm là tài sản cố định."),
  ("Please send me the invoice and the handover record for the new machine.", "Anh/chị gửi tôi hoá đơn và biên bản bàn giao của máy mới nhé."),
  ("We'll start depreciating it from the day it's put into use.", "Mình bắt đầu trích khấu hao từ ngày đưa vào sử dụng."),
  ("The asset register doesn't match the physical count.", "Sổ theo dõi tài sản không khớp với kết quả kiểm kê thực tế."),
  ("Three laptops on the list are missing.", "Ba laptop trong danh sách không tìm thấy."),
  ("This repair doesn't extend the machine's life, so it's an expense.", "Khoản sửa chữa này không kéo dài tuổi thọ máy nên tính vào chi phí."),
  ("We need a disposal form signed by the director.", "Mình cần biên bản thanh lý có chữ ký giám đốc."),
  ("The machine is fully depreciated, but we still use it.", "Máy đã khấu hao hết nhưng vẫn đang dùng."),
  ("Please put an asset tag on every new laptop.", "Anh/chị dán tem mã tài sản lên mỗi laptop mới nhé."),
 ],
 "dialogues": [
  ("Should we record this new air conditioner as a fixed asset?", [
    ("It cost 18 million dong, which is below 30 million. So we'll treat it as a tool and spread the cost over two years.", True, "Nêu ngưỡng ghi nhận TSCĐ + cách xử lý thay thế (công cụ dụng cụ, phân bổ)."),
    ("Yes, all machines are fixed asset.", False, "Sai: còn tuỳ giá trị và thời gian sử dụng; thiếu số nhiều ('assets')."),
    ("Up to you, both are OK.", False, "Né tránh; phân loại tài sản phải theo tiêu chuẩn, không tuỳ ý."),
  ]),
  ("Can we capitalise the delivery and installation costs?", [
    ("Yes. Costs to get the machine ready for use are part of its cost, so we'll add them to the asset.", True, "Đúng nguyên tắc: chi phí đưa tài sản vào trạng thái sẵn sàng sử dụng được tính vào nguyên giá."),
    ("No, only the machine price.", False, "Sai nguyên tắc: chi phí vận chuyển, lắp đặt được tính vào nguyên giá."),
    ("Yes, can.", False, "Thiếu chủ ngữ và không giải thích: 'Yes, we can, because…'"),
  ]),
  ("Three laptops are missing from the asset count.", [
    ("Let's check with IT first. They may be with staff working from home. If we can't find them, we'll report it to the director.", True, "Hướng kiểm tra + bước tiếp theo nếu vẫn không tìm thấy."),
    ("Just delete them from the register.", False, "Xoá sổ khi chưa điều tra và chưa được duyệt là sai kiểm soát."),
    ("Missing is normal, many companies same.", False, "Xem nhẹ mất mát tài sản; câu thiếu động từ."),
  ]),
  ("Why is depreciation still running on the old truck? We sold it in March.", [
    ("You're right. The disposal wasn't recorded. I'll record it now and reverse the depreciation after March.", True, "Thừa nhận + ghi nhận thanh lý + điều chỉnh khấu hao."),
    ("The system calculate automatic.", False, "Đổ cho hệ thống; sai ngữ pháp ('calculates it automatically')."),
    ("Because nobody tell me.", False, "Sai thì ('told') và chưa đưa cách khắc phục."),
  ]),
  ("What's the net book value of the old forklift?", [
    ("It cost 300 million dong, and 240 million has been depreciated. So the net book value is 60 million.", True, "Nguyên giá − khấu hao luỹ kế = giá trị còn lại, trình bày rõ."),
    ("It's old, so zero.", False, "Đoán theo cảm tính; phải tính từ sổ sách."),
    ("Net book value is 300 million.", False, "Nhầm nguyên giá với giá trị còn lại."),
  ]),
 ],
 "listen": [
  ("Please add the new machine to the asset register", ["machine", "register"], "ghi tăng tài sản"),
  ("The useful life of this truck is eight years", ["useful", "eight"], "thời gian khấu hao"),
  ("We use the straight-line method for machines", ["straight-line", "method"], "phương pháp khấu hao"),
  ("Three laptops were missing from the count", ["laptops", "missing"], "kiểm kê tài sản"),
  ("The new packing machine arrived on 3 June. It cost 900 million dong. We'll depreciate it over ten years from the day it's put into use.", ["packing", "cost", "ten"], "ghi nhận tài sản mới"),
  ("We'd like to sell the old forklift. Its net book value is 60 million dong. Please sign the disposal form by Friday.", ["sell", "value", "disposal"], "đề nghị thanh lý"),
 ],
})

# ───────────────────────── 12. Dòng tiền & quản lý quỹ ─────────────────────────
PHASES.append({
 "title": "Dòng tiền & quản lý quỹ",
 "vocab": [
  ("liquidity", "/lɪˈkwɪdəti/", "n", "khả năng thanh khoản", "We need enough <b>liquidity</b> to pay salaries and suppliers.", "Mình cần đủ thanh khoản để trả lương và nhà cung cấp.", "流動性", "ryūdōsei"),
  ("working capital", "/ˌwɜːkɪŋ ˈkæpɪtl/", "n", "vốn lưu động", "High stock levels tie up our <b>working capital</b>.", "Tồn kho cao làm kẹt vốn lưu động.", "運転資金", "unten shikin"),
  ("cash position", "/ˈkæʃ pəˌzɪʃn/", "n", "tình hình số dư tiền hiện có", "Please send me our <b>cash position</b> every Monday morning.", "Sáng thứ Hai hằng tuần gửi tôi tình hình số dư tiền nhé."),
  ("inflow", "/ˈɪnfləʊ/", "n", "dòng tiền vào", "The biggest <b>inflow</b> this week is 3 billion dong from our main customer.", "Khoản tiền vào lớn nhất tuần này là 3 tỷ đồng từ khách hàng chính."),
  ("outflow", "/ˈaʊtfləʊ/", "n", "dòng tiền ra", "Salaries are our largest monthly <b>outflow</b>.", "Lương là khoản chi ra lớn nhất hằng tháng."),
  ("shortfall", "/ˈʃɔːtfɔːl/", "n", "khoản thiếu hụt", "We expect a cash <b>shortfall</b> of 2 billion dong at the end of July.", "Mình dự kiến thiếu hụt 2 tỷ đồng tiền vào cuối tháng Bảy.", "資金不足", "shikin busoku"),
  ("surplus", "/ˈsɜːpləs/", "n", "khoản dư, thặng dư", "We can put the cash <b>surplus</b> into a one-month deposit.", "Mình có thể gửi khoản tiền dư vào kỳ hạn một tháng."),
  ("idle cash", "/ˌaɪdl ˈkæʃ/", "n", "tiền nhàn rỗi", "Don't leave <b>idle cash</b> in the current account for months.", "Đừng để tiền nhàn rỗi nằm trong tài khoản thanh toán hàng tháng trời."),
  ("cash count", "/ˈkæʃ kaʊnt/", "n", "kiểm quỹ tiền mặt", "We do a surprise <b>cash count</b> every quarter.", "Mỗi quý bên mình kiểm quỹ tiền mặt đột xuất một lần."),
  ("signatory", "/ˈsɪɡnətəri/", "n", "người có quyền ký (chứng từ, tài khoản)", "Each bank payment needs two <b>signatories</b>.", "Mỗi lệnh chi qua ngân hàng cần hai người ký."),
 ],
 "phrases": [
  ("Our cash position today is 12 billion dong.", "Số dư tiền hôm nay của mình là 12 tỷ đồng."),
  ("We have enough cash for the next six weeks.", "Mình đủ tiền cho sáu tuần tới."),
  ("We expect a shortfall in the last week of July.", "Dự kiến tuần cuối tháng Bảy mình sẽ thiếu tiền."),
  ("Can we delay some supplier payments by a week?", "Mình lùi một số khoản trả nhà cung cấp một tuần được không?"),
  ("We could use the bank overdraft for a few days.", "Mình có thể dùng hạn mức thấu chi ngân hàng vài ngày."),
  ("The cash forecast is updated every Friday.", "Dự báo dòng tiền được cập nhật vào thứ Sáu hằng tuần."),
  ("Collecting from customers faster will improve our working capital.", "Thu tiền khách nhanh hơn sẽ cải thiện vốn lưu động."),
  ("The cash count matches the cash book.", "Kiểm quỹ khớp với sổ quỹ tiền mặt."),
  ("Let's move the surplus into a short-term deposit.", "Mình chuyển khoản tiền dư sang tiền gửi ngắn hạn nhé."),
 ],
 "dialogues": [
  ("Do we have enough cash to pay salaries next week?", [
    ("Yes. We have 9 billion dong now, and salaries are about 6 billion. After that, cash will be tight until the 10th.", True, "Trả lời có/không + số liệu + cảnh báo giai đoạn căng."),
    ("I think yes, maybe enough.", False, "Mơ hồ; câu hỏi về lương cần câu trả lời chắc chắn bằng số."),
    ("Cash have 9 billion.", False, "Dịch từng chữ 'tiền có 9 tỷ': 'We have 9 billion dong in cash.'"),
  ]),
  ("Why is there a shortfall at the end of July?", [
    ("Two big customers will pay late, and the import tax for the new machine is due on the 28th.", True, "Nêu hai nguyên nhân cụ thể: tiền vào chậm + khoản chi lớn đến hạn."),
    ("Because money go out more than in.", False, "Hiển nhiên, không chỉ ra nguyên nhân; sai chia động từ ('goes')."),
    ("July is always bad month.", False, "Chung chung, thiếu mạo từ ('a bad month') và không có số liệu."),
  ]),
  ("We have 20 billion dong sitting in the current account. Any ideas?", [
    ("We only need about 8 billion for the next month. We could put 10 billion into a one-month deposit and keep the rest as a buffer.", True, "Tính nhu cầu tiền + đề xuất gửi kỳ hạn ngắn + giữ dự phòng."),
    ("Let's invest all in stocks, the return is high.", False, "Rủi ro cao, trái nguyên tắc quản lý quỹ: an toàn và thanh khoản trước."),
    ("Keep it, money in bank is safe.", False, "Bỏ lỡ cơ hội sinh lời; tiền nhàn rỗi nên được sử dụng hợp lý."),
  ]),
  ("The cash count is 2 million dong short.", [
    ("Let's count it again together and check today's cash vouchers before we report it.", True, "Kiểm đếm lại + đối chiếu phiếu thu/chi trước khi báo cáo."),
    ("Small amount, I put my money in.", False, "Tự bù tiền để che chênh lệch là sai quy trình — phải lập biên bản và tìm nguyên nhân."),
    ("Not my fault, I don't touch.", False, "Phủ nhận khi chưa kiểm tra; sai thì và thiếu tân ngữ ('I didn't touch it')."),
  ]),
  ("Can we pay this supplier today? It's 3 billion dong.", [
    ("We have enough cash, but a payment this size needs a second signatory. I'll ask the CFO to sign it this morning.", True, "Kiểm tra số dư + tuân thủ quy định ký duyệt."),
    ("Yes, I send now.", False, "Thiếu 'will' và bỏ qua bước phê duyệt khoản chi lớn."),
    ("Today no, bank is close.", False, "Sai từ loại ('closed'), thiếu mạo từ, không đưa phương án."),
  ]),
 ],
 "listen": [
  ("Our cash position today is twelve billion dong", ["position", "twelve"], "số dư tiền"),
  ("We expect a shortfall at the end of July", ["expect", "shortfall"], "thiếu hụt tiền"),
  ("Salaries are our biggest outflow every month", ["Salaries", "outflow"], "khoản chi lớn"),
  ("Every bank payment needs two signatories", ["payment", "signatories"], "quy định ký"),
  ("Here's this week's cash update. We received four billion dong from customers. Next week we'll pay six billion, so the balance will go down.", ["received", "customers", "balance"], "cập nhật dòng tiền tuần"),
  ("We have some idle cash this month. I suggest a one-month deposit. We'll still keep enough for salaries.", ["idle", "deposit", "salaries"], "đề xuất gửi tiền nhàn rỗi"),
 ],
})

# ───────────────────────── 13. Tính giá thành ─────────────────────────
PHASES.append({
 "title": "Tính giá thành",
 "vocab": [
  ("unit cost", "/ˌjuːnɪt ˈkɒst/", "n", "giá thành đơn vị", "The <b>unit cost</b> of this chair is 450,000 dong.", "Giá thành mỗi chiếc ghế này là 450.000 đồng."),
  ("cost of goods sold", "/ˌkɒst əv ˌɡʊdz ˈsəʊld/", "n", "giá vốn hàng bán (COGS)", "<b>Cost of goods sold</b> went up because steel prices rose.", "Giá vốn hàng bán tăng vì giá thép tăng.", "売上原価", "uriage genka"),
  ("direct material", "/dəˌrekt məˈtɪəriəl/", "n", "nguyên vật liệu trực tiếp", "<b>Direct material</b> is about 60% of our product cost.", "Nguyên vật liệu trực tiếp chiếm khoảng 60% giá thành.", "直接材料費", "chokusetsu zairyōhi"),
  ("direct labour", "/dəˌrekt ˈleɪbə/", "n", "nhân công trực tiếp", "<b>Direct labour</b> includes the wages of production workers.", "Nhân công trực tiếp gồm lương công nhân sản xuất.", "直接労務費", "chokusetsu rōmuhi"),
  ("overhead", "/ˈəʊvəhed/", "n", "chi phí chung (sản xuất chung)", "Factory electricity is part of production <b>overhead</b>.", "Tiền điện nhà máy thuộc chi phí sản xuất chung.", "間接費", "kansetsuhi"),
  ("standard cost", "/ˌstændəd ˈkɒst/", "n", "giá thành định mức", "The actual cost was 5% higher than the <b>standard cost</b>.", "Giá thành thực tế cao hơn định mức 5%.", "標準原価", "hyōjun genka"),
  ("work in progress", "/ˌwɜːk ɪn ˈprəʊɡres/", "n", "sản phẩm dở dang", "At month-end, we had 2,000 units in <b>work in progress</b>.", "Cuối tháng còn 2.000 sản phẩm dở dang.", "仕掛品", "shikakarihin"),
  ("bill of materials", "/ˌbɪl əv məˈtɪəriəlz/", "n", "định mức nguyên vật liệu (BOM)", "Please update the <b>bill of materials</b> after the design change.", "Sau khi đổi thiết kế, anh/chị cập nhật lại định mức nguyên vật liệu nhé.", "部品表", "buhinhyō"),
  ("scrap", "/skræp/", "n", "phế liệu, hàng hỏng (trong sản xuất)", "<b>Scrap</b> was 4% this month, higher than normal.", "Tháng này tỷ lệ hàng hỏng là 4%, cao hơn bình thường."),
  ("weighted average", "/ˌweɪtɪd ˈævərɪdʒ/", "n", "bình quân gia quyền", "We value stock using the <b>weighted average</b> method.", "Bên mình tính giá xuất kho theo phương pháp bình quân gia quyền."),
 ],
 "phrases": [
  ("The unit cost went up by 6% this quarter.", "Giá thành đơn vị quý này tăng 6%."),
  ("Material prices are the main reason for the increase.", "Giá nguyên vật liệu là lý do chính làm giá thành tăng."),
  ("We allocate overhead by machine hours.", "Bên mình phân bổ chi phí chung theo giờ máy."),
  ("Actual usage was higher than the bill of materials.", "Lượng dùng thực tế cao hơn định mức."),
  ("Could production send me the output report by the 2nd?", "Bên sản xuất gửi tôi báo cáo sản lượng trước ngày 2 được không?"),
  ("The standard cost needs to be updated for next year.", "Giá thành định mức cần được cập nhật cho năm sau."),
  ("If output is lower, the fixed cost per unit goes up.", "Sản lượng thấp thì định phí trên mỗi sản phẩm tăng."),
  ("Scrap costs us about 300 million dong a month.", "Hàng hỏng làm mình tốn khoảng 300 triệu đồng mỗi tháng."),
  ("Let's compare the actual cost with the standard cost.", "Mình so sánh giá thành thực tế với định mức nhé."),
 ],
 "dialogues": [
  ("Why did the unit cost go up this month?", [
    ("Output fell by 20% because of the holiday, so fixed overhead was spread over fewer units.", True, "Giải thích đúng: sản lượng giảm → định phí trên mỗi sản phẩm tăng."),
    ("Because cost is up.", False, "Lặp lại câu hỏi, không nêu nguyên nhân."),
    ("Production team work slow.", False, "Đổ lỗi không có số liệu; sai ngữ pháp ('works slowly')."),
  ]),
  ("What's included in the product cost?", [
    ("Direct material, direct labour and production overhead, like factory electricity and machine depreciation.", True, "Liệt kê đủ ba khoản mục giá thành + ví dụ."),
    ("Only material, because labour is salary.", False, "Sai kiến thức: nhân công trực tiếp cũng là một phần giá thành."),
    ("Everything, also sales and office costs.", False, "Sai: chi phí bán hàng và quản lý không tính vào giá thành sản xuất."),
  ]),
  ("Material usage is 8% above the BOM. What happened?", [
    ("I checked with production. The new supplier's fabric had more defects, so we used more to cut the same number of pieces.", True, "Đã kiểm tra + nguyên nhân gốc cụ thể."),
    ("BOM is wrong, I think.", False, "Đoán mò khi chưa kiểm tra với bộ phận sản xuất."),
    ("8% only, not big.", False, "Xem nhẹ chênh lệch; thiếu động từ ('It's only 8%')."),
  ]),
  ("Can we lower the price and still make money?", [
    ("Our unit cost is 450,000 dong. At 500,000, we'd still have a 10% margin, but anything lower would be risky.", True, "Dựa vào giá thành để tính biên lãi, chỉ rõ mức giá sàn."),
    ("Yes, of course, any price is OK.", False, "Hứa không có căn cứ giá thành."),
    ("I not sure the cost.", False, "Thiếu động từ ('I'm not sure about the cost') và không đề nghị kiểm tra."),
  ]),
  ("How do you value the materials we issue to production?", [
    ("We use the monthly weighted average method, based on opening stock and all purchases in the month.", True, "Nêu phương pháp + căn cứ tính ngắn gọn."),
    ("We use the price we like.", False, "Sai nguyên tắc: phương pháp tính giá phải nhất quán."),
    ("Stock value is same the invoice.", False, "Sai ngữ pháp ('the same as') và chưa nêu phương pháp tính giá."),
  ]),
 ],
 "listen": [
  ("The unit cost went up by six percent", ["unit", "six"], "giá thành tăng"),
  ("Direct material is sixty percent of the cost", ["material", "sixty"], "cơ cấu giá thành"),
  ("Please update the bill of materials", ["update", "materials"], "cập nhật BOM"),
  ("Scrap was higher than normal this month", ["Scrap", "normal"], "hàng hỏng"),
  ("Here's the cost report for May. Material usage was five percent above standard. The main reason was a batch of poor-quality fabric.", ["cost", "standard", "batch"], "báo cáo giá thành"),
  ("Output was low in February because of Tet. So each unit carried more overhead. The unit cost should go back to normal in March.", ["Output", "overhead", "March"], "giải thích giá thành tháng Tết"),
 ],
})

# ───────────────────────── 14. Mua hàng, hợp đồng & phê duyệt ─────────────────────────
PHASES.append({
 "title": "Mua hàng, hợp đồng & phê duyệt",
 "vocab": [
  ("purchase requisition", "/ˌpɜːtʃəs ˌrekwɪˈzɪʃn/", "n", "phiếu đề nghị mua hàng", "Please raise a <b>purchase requisition</b> before you contact suppliers.", "Anh/chị lập phiếu đề nghị mua hàng trước khi liên hệ nhà cung cấp nhé.", "購買依頼", "kōbai irai"),
  ("purchase order", "/ˈpɜːtʃəs ˌɔːdə/", "n", "đơn đặt hàng (PO)", "We can't pay without an approved <b>purchase order</b>.", "Không có PO đã duyệt thì bên mình không thanh toán được.", "発注書", "hacchūsho"),
  ("quotation", "/kwəʊˈteɪʃn/", "n", "báo giá", "Orders over 50 million dong need three <b>quotations</b>.", "Đơn hàng trên 50 triệu đồng cần ba báo giá.", "見積書", "mitsumorisho"),
  ("vendor", "/ˈvendə/", "n", "nhà cung cấp (trên hệ thống, hợp đồng)", "Is this company already an approved <b>vendor</b>?", "Công ty này đã là nhà cung cấp được duyệt chưa?", "仕入先", "shiiresaki"),
  ("payment terms", "/ˈpeɪmənt tɜːmz/", "n", "điều khoản thanh toán", "Our standard <b>payment terms</b> are 30 days from the invoice date.", "Điều khoản thanh toán chuẩn của bên mình là 30 ngày kể từ ngày hoá đơn.", "支払条件", "shiharai jōken"),
  ("advance payment", "/ədˌvɑːns ˈpeɪmənt/", "n", "tiền trả trước cho nhà cung cấp", "The supplier wants a 30% <b>advance payment</b> before production.", "Nhà cung cấp muốn được trả trước 30% trước khi sản xuất.", "前払金", "maebaraikin"),
  ("approval limit", "/əˈpruːvl ˌlɪmɪt/", "n", "hạn mức phê duyệt (thẩm quyền duyệt)", "My <b>approval limit</b> is 100 million dong.", "Hạn mức duyệt của tôi là 100 triệu đồng."),
  ("approval workflow", "/əˈpruːvl ˌwɜːkfləʊ/", "n", "luồng phê duyệt", "The request is stuck in the <b>approval workflow</b>.", "Đề nghị này đang bị kẹt trong luồng phê duyệt.", "承認フロー", "shōnin furō"),
  ("addendum", "/əˈdendəm/", "n", "phụ lục hợp đồng", "We need an <b>addendum</b> to change the delivery date.", "Mình cần làm phụ lục hợp đồng để đổi ngày giao hàng."),
  ("goods received note", "/ˌɡʊdz rɪˈsiːvd nəʊt/", "n", "phiếu nhập kho, biên bản nhận hàng (GRN)", "The warehouse hasn't sent the <b>goods received note</b> yet.", "Kho vẫn chưa gửi phiếu nhập kho."),
 ],
 "phrases": [
  ("Please get three quotations for anything over 50 million dong.", "Khoản nào trên 50 triệu đồng thì lấy ba báo giá nhé."),
  ("This PO is waiting for the director's approval.", "PO này đang chờ giám đốc duyệt."),
  ("The amount is over my approval limit, so it goes to the CFO.", "Số tiền vượt hạn mức duyệt của tôi nên phải chuyển lên giám đốc tài chính."),
  ("Can we change the payment terms to 45 days?", "Mình đổi điều khoản thanh toán thành 45 ngày được không?"),
  ("The contract says 30% in advance and 70% after delivery.", "Hợp đồng ghi trả trước 30%, 70% còn lại sau khi giao hàng."),
  ("We need an addendum if the price changes.", "Nếu giá thay đổi thì mình cần làm phụ lục hợp đồng."),
  ("Please don't order anything before the PO is approved.", "Vui lòng không đặt hàng khi PO chưa được duyệt."),
  ("Is this supplier set up in the system yet?", "Nhà cung cấp này đã được tạo trên hệ thống chưa?"),
  ("Please ask the warehouse to confirm the goods received.", "Anh/chị nhờ kho xác nhận số hàng đã nhận nhé."),
 ],
 "dialogues": [
  ("I've already ordered the chairs. Can you create the PO now?", [
    ("I can, but next time please raise the requisition first. Ordering before approval is against our purchasing policy.", True, "Hỗ trợ nhưng nhắc lại đúng quy trình."),
    ("OK, no problem, always like this.", False, "Dung túng việc sai quy trình (đặt hàng trước khi có PO)."),
    ("Why you order before?", False, "Sai trật tự câu hỏi ('Why did you order…?') và nghe trách móc."),
  ]),
  ("Why do I need three quotations? I trust this supplier.", [
    ("It's our policy for orders over 50 million dong. It helps us get a fair price and keeps the choice transparent.", True, "Nêu quy định + mục đích (giá hợp lý, minh bạch)."),
    ("Because trust is not enough.", False, "Nghe như nghi ngờ đồng nghiệp, không nêu quy định."),
    ("Three quotation is the rule.", False, "Thiếu số nhiều ('quotations') và không giải thích mục đích."),
  ]),
  ("The supplier wants 50% in advance. Is that OK?", [
    ("That's higher than our usual 30%. Let's ask for 30%, or a bank guarantee if they need more.", True, "So với mức chuẩn + đề xuất giảm rủi ro (bảo lãnh ngân hàng)."),
    ("Yes, pay them, they are nice.", False, "Chấp nhận rủi ro trả trước lớn mà không có bảo đảm."),
    ("50% is too many.", False, "Sai từ ('too much'/'too high') và không đưa phương án."),
  ]),
  ("My PO has been pending for a week. Can you approve it?", [
    ("It's over my approval limit, so it's with the CFO. I'll remind her today and let you know.", True, "Giải thích thẩm quyền + hành động hỗ trợ cụ thể."),
    ("OK, I approve it now for you.", False, "Duyệt vượt thẩm quyền là vi phạm kiểm soát."),
    ("Not my problem, wait.", False, "Cộc lốc, thiếu hợp tác."),
  ]),
  ("The supplier changed the price after we signed the contract.", [
    ("Then we need an addendum signed by both sides before we accept the new price.", True, "Đúng: thay đổi điều khoản phải có phụ lục hai bên ký."),
    ("OK, just pay the new price.", False, "Trả theo giá mới khi chưa có phụ lục là sai hợp đồng."),
    ("They can't change. Contract is contract.", False, "Cứng nhắc; nên nói cách xử lý: làm phụ lục hoặc giữ giá cũ."),
  ]),
 ],
 "listen": [
  ("This order needs three quotations", ["order", "quotations"], "quy định báo giá"),
  ("The PO is still waiting for approval", ["waiting", "approval"], "PO chờ duyệt"),
  ("Our payment terms are thirty days", ["terms", "thirty"], "điều khoản thanh toán"),
  ("We need an addendum to change the price", ["addendum", "price"], "phụ lục hợp đồng"),
  ("Hi Linh, your purchase requisition is approved. Please send the PO to the supplier today. Payment will be thirty days after delivery.", ["approved", "supplier", "delivery"], "báo duyệt đề nghị mua"),
  ("This PO is 250 million dong. It's over my limit, so it will go to the CFO. You should get an answer by Thursday.", ["limit", "CFO", "Thursday"], "giải thích luồng duyệt"),
 ],
})

# ───────────────────────── 15. Hệ thống ERP & dữ liệu kế toán ─────────────────────────
PHASES.append({
 "title": "Hệ thống ERP & dữ liệu kế toán",
 "vocab": [
  ("chart of accounts", "/ˌtʃɑːt əv əˈkaʊnts/", "n", "hệ thống tài khoản kế toán", "Our <b>chart of accounts</b> follows the Vietnamese standard, with extra sub-accounts.", "Hệ thống tài khoản của mình theo chuẩn Việt Nam, có thêm tài khoản chi tiết.", "勘定科目表", "kanjō kamokuhyō"),
  ("master data", "/ˈmɑːstə ˌdeɪtə/", "n", "dữ liệu gốc, danh mục (khách hàng, nhà cung cấp…)", "Only two people can change vendor <b>master data</b>.", "Chỉ hai người được sửa danh mục nhà cung cấp.", "マスタデータ", "masuta dēta"),
  ("access rights", "/ˈækses raɪts/", "n", "quyền truy cập", "New staff get <b>access rights</b> after their manager approves.", "Nhân viên mới được cấp quyền truy cập sau khi quản lý duyệt.", "アクセス権限", "akusesu kengen"),
  ("data entry", "/ˈdeɪtə ˌentri/", "n", "nhập liệu", "Most errors come from manual <b>data entry</b>.", "Phần lớn lỗi đến từ nhập liệu thủ công."),
  ("posting date", "/ˈpəʊstɪŋ deɪt/", "n", "ngày hạch toán", "Check the <b>posting date</b> before you save the invoice.", "Kiểm tra ngày hạch toán trước khi lưu hoá đơn."),
  ("duplicate", "/ˈdjuːplɪkət/", "adj/n", "trùng lặp; bản trùng", "The system found a <b>duplicate</b> invoice from the same supplier.", "Hệ thống phát hiện một hoá đơn trùng của cùng nhà cung cấp."),
  ("opening balance", "/ˌəʊpənɪŋ ˈbæləns/", "n", "số dư đầu kỳ", "The <b>opening balance</b> must equal last year's closing balance.", "Số dư đầu kỳ phải bằng số dư cuối kỳ năm trước.", "期首残高", "kishu zandaka"),
  ("data migration", "/ˈdeɪtə maɪˌɡreɪʃn/", "n", "chuyển đổi dữ liệu (sang hệ thống mới)", "The <b>data migration</b> will happen over the New Year holiday.", "Dữ liệu sẽ được chuyển sang hệ thống mới trong kỳ nghỉ Tết Dương lịch.", "データ移行", "dēta ikō"),
  ("go-live", "/ˌɡəʊ ˈlaɪv/", "n", "thời điểm chạy chính thức (hệ thống mới)", "The <b>go-live</b> date for the new ERP is 1 January.", "Ngày chạy chính thức hệ thống ERP mới là 1/1.", "本番稼働", "honban kadō"),
  ("spreadsheet", "/ˈspredʃiːt/", "n", "bảng tính", "We still track small tools in a <b>spreadsheet</b>.", "Công cụ nhỏ bên mình vẫn theo dõi bằng bảng tính."),
 ],
 "phrases": [
  ("I don't have access rights to this report.", "Tôi chưa có quyền xem báo cáo này."),
  ("Could you create a new vendor code for this supplier?", "Anh/chị tạo giúp mã nhà cung cấp mới cho bên này nhé."),
  ("Please attach the scanned invoice to the entry.", "Vui lòng đính kèm bản scan hoá đơn vào bút toán."),
  ("The system won't let me post to a closed period.", "Hệ thống không cho hạch toán vào kỳ đã khoá."),
  ("I think this invoice was entered twice.", "Tôi nghĩ hoá đơn này bị nhập hai lần."),
  ("Which account should I use for this cost?", "Chi phí này tôi hạch toán vào tài khoản nào?"),
  ("Let's export the report and check it in a spreadsheet.", "Mình xuất báo cáo ra bảng tính để kiểm tra nhé."),
  ("The opening balances in the new system don't match.", "Số dư đầu kỳ trên hệ thống mới không khớp."),
  ("After go-live, all invoices must be entered in the new system.", "Sau khi chạy chính thức, mọi hoá đơn phải nhập trên hệ thống mới."),
 ],
 "dialogues": [
  ("The supplier says we paid the same invoice twice.", [
    ("I'll check now. If it's a duplicate, I'll ask them to refund it or deduct it from the next invoice.", True, "Kiểm tra ngay + hai phương án thu hồi tiền."),
    ("Impossible, system check duplicate.", False, "Khẳng định khi chưa kiểm tra; sai ngữ pháp ('the system checks for duplicates')."),
    ("Yes, sorry, I forget.", False, "Nhận lỗi khi chưa kiểm tra, sai thì ('I forgot') và chưa nói cách thu hồi tiền."),
  ]),
  ("Can you give me your password so I can post this entry?", [
    ("Sorry, I can't share my password. Let's ask the system admin to give you the right access.", True, "Từ chối chia sẻ mật khẩu + hướng xin quyền đúng cách."),
    ("OK, my password is on my desk.", False, "Chia sẻ mật khẩu vi phạm bảo mật và kiểm soát nội bộ."),
    ("No. Password is private, you know.", False, "Đúng nguyên tắc nhưng cộc lốc, không giúp giải quyết việc."),
  ]),
  ("Why don't the opening balances in the new system match?", [
    ("Some customer balances were migrated before we posted the last December entries. I'll post the adjustments and send you a reconciliation.", True, "Nguyên nhân + cách sửa + gửi bảng đối chiếu."),
    ("New system is bad.", False, "Đổ cho hệ thống, thiếu mạo từ, không phân tích."),
    ("Small difference, we can ignore.", False, "Sai: số dư đầu kỳ phải khớp hoàn toàn với số dư cuối kỳ trước."),
  ]),
  ("Which account should I use for printer ink?", [
    ("Use the office supplies account, and choose your department's cost centre.", True, "Chỉ đúng tài khoản + trung tâm chi phí."),
    ("Any account is OK.", False, "Hạch toán tuỳ ý làm sai báo cáo chi phí."),
    ("Printer is asset, so ink asset.", False, "Sai kiến thức (mực in là vật tư tiêu hao) và thiếu động từ."),
  ]),
  ("Can we go live on 1 January as planned?", [
    ("Almost. Data migration is done, but our user checks found two issues. If they're fixed by the 20th, we can go live on time.", True, "Tình trạng + vướng mắc + điều kiện để kịp tiến độ."),
    ("Yes, sure, no problem at all.", False, "Hứa chắc chắn khi còn lỗi chưa xử lý."),
    ("Maybe can, maybe cannot.", False, "Mơ hồ, thiếu chủ ngữ."),
  ]),
 ],
 "listen": [
  ("The go-live date is the first of January", ["go-live", "January"], "ngày chạy hệ thống"),
  ("I think this invoice was entered twice", ["invoice", "twice"], "nhập trùng"),
  ("Please check the posting date before saving", ["posting", "saving"], "ngày hạch toán"),
  ("I don't have access to this report", ["access", "report"], "quyền truy cập"),
  ("Hi team, the new system goes live on Monday. From that day, please enter all invoices there. The old system will be read-only.", ["Monday", "enter", "read-only"], "thông báo chạy hệ thống mới"),
  ("We found a duplicate payment to one supplier. The same invoice was entered with two different numbers. We've asked the supplier for a refund.", ["duplicate", "numbers", "refund"], "báo lỗi thanh toán trùng"),
 ],
})

# ───────────────────────── 16. Vay, đầu tư & lãi suất ─────────────────────────
PHASES.append({
 "title": "Vay, đầu tư & lãi suất",
 "vocab": [
  ("principal", "/ˈprɪnsəpl/", "n", "tiền gốc (khoản vay)", "We repay the <b>principal</b> in 12 monthly payments.", "Bên mình trả gốc thành 12 kỳ hằng tháng.", "元金", "gankin"),
  ("repayment", "/rɪˈpeɪmənt/", "n", "khoản trả nợ; việc trả nợ", "The next loan <b>repayment</b> is due on 25 August.", "Kỳ trả nợ vay tiếp theo đến hạn ngày 25/8.", "返済", "hensai"),
  ("collateral", "/kəˈlætərəl/", "n", "tài sản bảo đảm (thế chấp)", "The bank wants the factory as <b>collateral</b>.", "Ngân hàng muốn lấy nhà xưởng làm tài sản bảo đảm.", "担保", "tanpo"),
  ("overdraft", "/ˈəʊvədrɑːft/", "n", "thấu chi", "We used the <b>overdraft</b> for three days last month.", "Tháng trước mình dùng thấu chi ba ngày.", "当座貸越", "tōza kashikoshi"),
  ("credit facility", "/ˈkredɪt fəˌsɪləti/", "n", "hạn mức tín dụng (ngân hàng cấp)", "Our <b>credit facility</b> with the bank is 50 billion dong.", "Hạn mức tín dụng của mình với ngân hàng là 50 tỷ đồng.", "融資枠", "yūshi waku"),
  ("floating rate", "/ˌfləʊtɪŋ ˈreɪt/", "n", "lãi suất thả nổi", "With a <b>floating rate</b>, our interest cost can go up.", "Với lãi suất thả nổi, chi phí lãi vay có thể tăng.", "変動金利", "hendō kinri"),
  ("fixed rate", "/ˌfɪkst ˈreɪt/", "n", "lãi suất cố định", "The loan has a <b>fixed rate</b> for the first 12 months.", "Khoản vay có lãi suất cố định trong 12 tháng đầu.", "固定金利", "kotei kinri"),
  ("maturity", "/məˈtʃʊərəti/", "n", "(ngày) đáo hạn", "The loan's <b>maturity</b> date is 30 June 2028.", "Khoản vay đáo hạn ngày 30/6/2028."),
  ("grace period", "/ˈɡreɪs ˌpɪəriəd/", "n", "thời gian ân hạn (chưa phải trả gốc)", "There's a six-month <b>grace period</b> before we start paying the principal.", "Có sáu tháng ân hạn trước khi bắt đầu trả gốc.", "据置期間", "sueoki kikan"),
  ("return on investment", "/rɪˌtɜːn ɒn ɪnˈvestmənt/", "n", "tỷ suất sinh lời trên vốn đầu tư (ROI)", "The new warehouse has a <b>return on investment</b> of 15% a year.", "Kho mới có tỷ suất sinh lời 15%/năm.", "投資利益率", "tōshi riekiritsu"),
 ],
 "phrases": [
  ("The loan is 20 billion dong over five years.", "Khoản vay 20 tỷ đồng trong năm năm."),
  ("The interest rate is fixed for the first year, then floating.", "Lãi suất cố định năm đầu, sau đó thả nổi."),
  ("We pay interest monthly and the principal every quarter.", "Mình trả lãi hằng tháng và trả gốc mỗi quý."),
  ("The bank needs our latest financial statements for the loan.", "Ngân hàng cần báo cáo tài chính gần nhất để xét khoản vay."),
  ("How much of the credit facility have we used?", "Mình đã dùng bao nhiêu hạn mức tín dụng rồi?"),
  ("If rates go up by 1%, our interest cost rises by 200 million dong.", "Nếu lãi suất tăng 1%, chi phí lãi vay tăng 200 triệu đồng."),
  ("Can we repay part of the loan early without a fee?", "Mình trả trước một phần khoản vay mà không mất phí được không?"),
  ("The payback period for this project is about four years.", "Thời gian hoàn vốn của dự án này khoảng bốn năm."),
  ("Let's compare the offers from the two banks.", "Mình so sánh đề xuất của hai ngân hàng nhé."),
 ],
 "dialogues": [
  ("Which bank offer is better?", [
    ("The first bank has a lower rate, but the second has no early repayment fee. If we plan to repay early, the second is cheaper overall.", True, "So sánh hai tiêu chí + kết luận theo kế hoạch trả nợ."),
    ("The first bank, because it's more famous.", False, "Chọn theo cảm tính, không dựa vào chi phí vay."),
    ("Both same, choose any.", False, "Thiếu động từ ('They're the same') và không phân tích điều khoản."),
  ]),
  ("Should we choose a fixed or floating rate?", [
    ("Rates may go up next year, so a fixed rate gives us more certainty, even if it starts a bit higher.", True, "Nhận định + lý do + nêu đánh đổi."),
    ("Floating, because floating is lower always.", False, "Sai: lãi thả nổi không phải lúc nào cũng thấp hơn; sai vị trí trạng từ ('always lower')."),
    ("I don't know rate.", False, "Né tránh, thiếu mạo từ; nên đưa phân tích sơ bộ."),
  ]),
  ("What does the bank need for the loan application?", [
    ("Our audited financial statements for the last two years, a cash flow forecast and the documents for the collateral.", True, "Liệt kê hồ sơ cụ thể."),
    ("Many documents, I will ask later.", False, "Mơ hồ, chưa chuẩn bị gì."),
    ("Bank need everything.", False, "Sai chia động từ ('needs'), thiếu mạo từ và không cụ thể."),
  ]),
  ("When do we start paying back the principal?", [
    ("There's a six-month grace period, so the first principal payment is in March. Until then, we only pay interest.", True, "Ân hạn + mốc trả gốc + nghĩa vụ trong thời gian ân hạn."),
    ("Six month later.", False, "Thiếu động từ và số nhiều ('in six months')."),
    ("We don't pay anything in grace period.", False, "Sai: trong thời gian ân hạn gốc thường vẫn phải trả lãi."),
  ]),
  ("Is this new warehouse a good investment?", [
    ("The return on investment is about 15% a year, which is higher than our 9% borrowing cost. So it makes sense.", True, "So sánh ROI với chi phí vốn — lập luận đúng."),
    ("Yes, warehouse is always good.", False, "Kết luận chung chung, thiếu mạo từ, không có số."),
    ("The ROI is high, 15, very good.", False, "Thiếu đơn vị và không so sánh với chi phí vốn."),
  ]),
 ],
 "listen": [
  ("The next repayment is due on the twenty-fifth", ["repayment", "twenty-fifth"], "lịch trả nợ"),
  ("The bank wants the factory as collateral", ["bank", "collateral"], "tài sản bảo đảm"),
  ("The rate is fixed for the first year", ["fixed", "year"], "lãi suất cố định"),
  ("We used the overdraft for three days", ["overdraft", "three"], "thấu chi"),
  ("Our credit facility is fifty billion dong. We've used thirty billion so far. So we still have twenty billion available.", ["facility", "used", "available"], "tình hình hạn mức tín dụng"),
  ("The bank has raised the floating rate by half a percent. Our monthly interest will go up. I'll update the cash forecast today.", ["floating", "interest", "forecast"], "báo tăng lãi suất"),
 ],
})

# ───────────────────────── 17. Phân tích biến động & giải trình số liệu ─────────────────────────
PHASES.append({
 "title": "Phân tích biến động & giải trình",
 "vocab": [
  ("fluctuation", "/ˌflʌktʃuˈeɪʃn/", "n", "biến động (lên xuống)", "Please explain any <b>fluctuation</b> over 10% in the balance sheet.", "Vui lòng giải trình mọi biến động trên 10% trong bảng cân đối.", "変動", "hendō"),
  ("month-on-month", "/ˌmʌnθ ɒn ˈmʌnθ/", "adj/adv", "so với tháng trước", "Utility costs rose 15% <b>month-on-month</b>.", "Chi phí điện nước tăng 15% so với tháng trước.", "前月比", "zengetsuhi"),
  ("threshold", "/ˈθreʃhəʊld/", "n", "ngưỡng", "We explain every variance above the <b>threshold</b> of 50 million dong.", "Mình giải trình mọi chênh lệch vượt ngưỡng 50 triệu đồng."),
  ("root cause", "/ˌruːt ˈkɔːz/", "n", "nguyên nhân gốc", "We need to find the <b>root cause</b>, not just fix the number.", "Mình cần tìm nguyên nhân gốc, không chỉ sửa con số.", "根本原因", "konpon gen'in"),
  ("commentary", "/ˈkɒməntri/", "n", "phần giải trình, thuyết minh (kèm số liệu)", "Please add a short <b>commentary</b> under each chart.", "Anh/chị thêm phần giải trình ngắn dưới mỗi biểu đồ nhé."),
  ("spike", "/spaɪk/", "n", "(sự) tăng đột biến", "There was a <b>spike</b> in freight costs in October.", "Chi phí vận chuyển tăng đột biến vào tháng Mười."),
  ("offset", "/ˌɒfˈset/", "v", "bù lại, bù trừ", "Higher sales were <b>offset</b> by higher material costs.", "Phần doanh số tăng thêm bị chi phí nguyên vật liệu tăng bù trừ mất."),
  ("reclassify", "/ˌriːˈklæsɪfaɪ/", "v", "hạch toán lại sang tài khoản đúng (phân loại lại)", "We'll <b>reclassify</b> this cost from marketing to training.", "Mình sẽ chuyển khoản chi này từ chi phí marketing sang chi phí đào tạo.", "振り替える", "furikaeru"),
  ("seasonal", "/ˈsiːzənl/", "adj", "theo mùa vụ", "The drop in February is <b>seasonal</b>. It happens every year because of Tet.", "Mức giảm tháng Hai mang tính mùa vụ, năm nào cũng vậy vì Tết."),
  ("flag", "/flæɡ/", "v", "đánh dấu, lưu ý (để xem xét)", "I've <b>flagged</b> three accounts with big changes.", "Tôi đã đánh dấu ba tài khoản có biến động lớn."),
 ],
 "phrases": [
  ("Could you explain why this account went up so much?", "Anh/chị giải thích giúp vì sao tài khoản này tăng nhiều vậy?"),
  ("Costs rose 12% month-on-month, mainly because of the new warehouse.", "Chi phí tăng 12% so với tháng trước, chủ yếu do kho mới."),
  ("The increase is seasonal. We see it every December.", "Mức tăng này mang tính mùa vụ, tháng Mười Hai năm nào cũng vậy."),
  ("Part of the increase is offset by lower freight costs.", "Một phần mức tăng được bù lại nhờ chi phí vận chuyển giảm."),
  ("This cost was booked to the wrong account. We'll reclassify it.", "Khoản này bị hạch toán nhầm tài khoản, mình sẽ chuyển lại."),
  ("I've flagged the items above the threshold.", "Tôi đã đánh dấu các khoản vượt ngưỡng."),
  ("Let's find the root cause before we make any adjustment.", "Mình tìm nguyên nhân gốc trước khi điều chỉnh nhé."),
  ("Without the one-off, costs would be flat.", "Nếu bỏ khoản phát sinh một lần thì chi phí gần như không đổi."),
  ("I'll add a short commentary to the report.", "Tôi sẽ thêm phần giải trình ngắn vào báo cáo."),
 ],
 "dialogues": [
  ("Why did utilities jump 30% month-on-month?", [
    ("We ran a second shift for three weeks to finish a big order. The spike should end next month.", True, "Nguyên nhân cụ thể + dự báo khi nào hết."),
    ("Because weather is hot, I guess.", False, "Đoán mò, thiếu mạo từ; cần kiểm tra số liệu thực tế."),
    ("Utilities up, electricity up.", False, "Thiếu động từ, lặp lại thông tin mà không giải thích."),
  ]),
  ("Revenue went up, but profit didn't. Why?", [
    ("Higher sales were offset by a 10% increase in material prices, so the margin fell.", True, "Dùng 'offset' đúng + nguyên nhân + tác động."),
    ("Profit is not follow revenue.", False, "Sai ngữ pháp ('doesn't follow') và không giải thích."),
    ("The accountant made mistake maybe.", False, "Đổ lỗi vô căn cứ, thiếu mạo từ ('a mistake')."),
  ]),
  ("Training costs are zero, but marketing is way over budget.", [
    ("I checked. A training invoice was booked to marketing by mistake. I'll reclassify it this afternoon.", True, "Kiểm tra + phát hiện hạch toán nhầm + hành động sửa."),
    ("Maybe marketing spend more money.", False, "Chưa kiểm tra; sai thì ('spent')."),
    ("Zero is good, we save money.", False, "Hiểu sai: số 0 bất thường là dấu hiệu cần kiểm tra."),
  ]),
  ("Do I need to explain every small change?", [
    ("No, only changes above the threshold: 10% and 50 million dong. The rest can go in one line.", True, "Nêu rõ ngưỡng giải trình + cách xử lý phần còn lại."),
    ("Yes, every dong must explain.", False, "Quá mức cần thiết và sai dạng bị động ('must be explained')."),
    ("No, nobody reads it.", False, "Thái độ xem nhẹ báo cáo."),
  ]),
  ("Sales always drop in February. Should we worry?", [
    ("Not really. It's seasonal because of Tet. Compared with last February, we're actually 5% higher.", True, "Nhận định mùa vụ + so sánh cùng kỳ để chứng minh."),
    ("Yes, very worry.", False, "Sai từ loại ('very worried') và không có căn cứ."),
    ("February is short month, so.", False, "Câu bỏ lửng, thiếu mạo từ, chưa có số liệu."),
  ]),
 ],
 "listen": [
  ("Costs rose twelve percent month-on-month", ["Costs", "month-on-month"], "so với tháng trước"),
  ("We'll reclassify this cost to training", ["reclassify", "training"], "hạch toán lại"),
  ("I've flagged three accounts for review", ["flagged", "accounts"], "đánh dấu tài khoản"),
  ("The drop in February is seasonal", ["drop", "seasonal"], "biến động mùa vụ"),
  ("Freight costs had a spike in October. A large order was shipped by air. We don't expect this to happen again.", ["spike", "air", "expect"], "giải trình chi phí vận chuyển"),
  ("Please explain all changes above the threshold. Focus on the root cause. Keep each comment to two or three lines.", ["threshold", "root", "comment"], "hướng dẫn giải trình"),
 ],
})

EXTRA = {
 "phases": PHASES,
 "rev": [
  ("Phiếu lương của anh/chị có trên cổng nhân sự.", "Your payslip is on the HR portal."),
  ("Tiền làm thêm giờ sẽ được trả vào tháng sau.", "Your overtime will be paid next month."),
  ("Thông tin lương là bảo mật.", "Payroll information is confidential."),
  ("Máy mới được khấu hao trong mười năm.", "The new machine is depreciated over ten years."),
  ("Kiểm kê không thấy ba laptop.", "Three laptops are missing from the asset count."),
  ("Tuần cuối tháng Bảy mình sẽ thiếu tiền.", "We'll be short of cash in the last week of July."),
  ("Mỗi lệnh chi cần hai người ký.", "Each payment needs two signatories."),
  ("Giá thành đơn vị tăng 6%.", "The unit cost went up by 6%."),
  ("Lượng dùng thực tế cao hơn định mức.", "Actual usage was higher than the standard."),
  ("Đơn hàng này cần ba báo giá.", "This order needs three quotations."),
  ("Số tiền vượt hạn mức duyệt của tôi.", "The amount is over my approval limit."),
  ("Hoá đơn này bị nhập hai lần.", "This invoice was entered twice."),
  ("Tôi chưa có quyền xem báo cáo này.", "I don't have access to this report."),
  ("Lãi suất cố định trong năm đầu.", "The rate is fixed for the first year."),
  ("Khoản này bị hạch toán nhầm tài khoản.", "This cost was booked to the wrong account."),
  ("Mức giảm này mang tính mùa vụ.", "This drop is seasonal."),
 ],
 "reading": [
  {"t": "Payslip", "text": "PAYSLIP – JUNE\nEmployee: Tran Minh Khoa\nGross salary: 20,000,000 VND\nOvertime (8 hours): 1,500,000 VND\nSocial, health & unemployment insurance (10.5%): -2,100,000 VND\nPersonal income tax: -450,000 VND\nNet pay: 18,950,000 VND\nPayment date: 25 June", "q": [
    {"q": "How much is Khoa's net pay?", "o": ["20,000,000 VND", "18,950,000 VND", "21,500,000 VND"], "a": 1},
    {"q": "What is the 2,100,000 VND deduction for?", "o": ["Personal income tax", "Overtime", "Insurance"], "a": 2}]},
  {"t": "Purchase approval limits", "text": "PURCHASE APPROVAL LIMITS\nUp to 20 million VND: Department Manager\n20–200 million VND: Finance Manager\nOver 200 million VND: CFO\nOrders over 50 million VND need three quotations.\nNo order may be placed before the PO is approved.", "q": [
    {"q": "Who approves a 150 million VND order?", "o": ["Department Manager", "Finance Manager", "CFO"], "a": 1},
    {"q": "When can you place an order with a supplier?", "o": ["When you get one quotation", "After the PO is approved", "After the goods arrive"], "a": 1}]},
  {"t": "Loan repayment notice", "text": "Subject: Loan repayment notice – Contract LN-3381\nDear Customer,\nYour next repayment is due on 25 August:\n- Principal: 500,000,000 VND\n- Interest: 86,000,000 VND\nPlease make sure there is enough money in your current account by 24 August. Late payments will be charged penalty interest.\nCredit Department", "q": [
    {"q": "What is the total amount due on 25 August?", "o": ["500,000,000 VND", "586,000,000 VND", "86,000,000 VND"], "a": 1},
    {"q": "By when should the money be in the account?", "o": ["24 August", "25 August", "31 August"], "a": 0}]},
  {"t": "ERP go-live email", "text": "Subject: New ERP go-live – what you need to do\nHi all,\nThe new ERP system goes live on 5 January.\n- 29–31 December: old system closed for data migration\n- From 5 January: enter all invoices and POs in the new system only\n- Your login details will be sent by email on 2 January\nQuestions? Please contact the finance systems team.\nThanks,\nHuong", "q": [
    {"q": "Why is the old system closed at the end of December?", "o": ["For the holiday", "For data migration", "For the audit"], "a": 1},
    {"q": "When will users get their login details?", "o": ["29 December", "2 January", "5 January"], "a": 1}]},
  {"t": "Cost commentary", "text": "COST COMMENTARY – OCTOBER\nFreight: +320 million VND vs budget. One urgent order was shipped by air. One-off; no repeat expected.\nUtilities: +12% month-on-month because of the second shift. Expected to return to normal in December.\nTraining: 0 VND vs budget of 150 million VND. The training invoice was booked to Marketing by mistake and will be reclassified.", "q": [
    {"q": "Why were freight costs higher than budget?", "o": ["Fuel prices rose", "An order was shipped by air", "A new carrier was used"], "a": 1},
    {"q": "What will happen to the training invoice?", "o": ["It will be paid again", "It will be moved to the right account", "It will be deleted"], "a": 1}]},
 ],
 "ai": [
  ("payroll", "Nhân viên thắc mắc lương", "You are a foreign employee. Your net pay this month is lower than you expected. Ask me, the payroll accountant, to explain the deductions on your payslip and ask about your overtime."),
  ("loan", "Làm việc với ngân hàng về khoản vay", "You are a relationship manager at a bank. Our company wants a 20 billion dong loan for a new warehouse. Ask me about the purpose, our cash flow, collateral and how we will repay."),
  ("costing", "Giải thích giá thành tăng", "You are the foreign factory director. The unit cost of our main product rose 8% this quarter. Ask me why, which cost items changed and what we can do."),
  ("purchase", "Đặt hàng sai quy trình", "You are a foreign department manager. You ordered new equipment before the PO was approved and now want finance to pay the supplier quickly. Push a little, then accept the process."),
 ],
 "events": [
  ("tet_bonus", "Tính lương thưởng Tết", "You are my foreign HR director. We are preparing the Tet bonus payroll. Ask me about the timeline, how the bonus will be taxed and what employees will see on their payslips."),
  ("asset_count", "Kiểm kê tài sản cuối năm", "You are my foreign finance manager. We will do the year-end fixed asset count next week. Ask me about the plan, who will count, and what we will do with missing or broken assets."),
  ("loan_renewal", "Gia hạn hạn mức tín dụng", "You are a bank credit officer. Our credit facility is up for renewal next month. Ask me about our latest results, our cash flow forecast and any changes in our business."),
 ],
 "quips": [
  "Payroll sent on time!",
  "Overheads under control!",
  "No duplicates today!",
  "Cash in, cash out!",
  "Depreciating slowly…",
  "Three quotes, please!",
 ],
 "roles": {
  "accountant": {
   "scenarios": [
    ("ac_payslip", "Đồng nghiệp hỏi về phiếu lương", "You are a foreign colleague. Your overtime is missing from your payslip and your insurance deduction looks high. Ask me to check and explain."),
    ("ac_asset", "Ghi nhận tài sản mới", "You are the foreign factory manager. You bought a new machine. Ask how it will be recorded and depreciated, and what documents finance needs from you."),
   ],
   "dialogues": [
    ("Can you pay this supplier today? The PO isn't approved yet.", [
      ("Sorry, I can't pay without an approved PO. I'll remind the approver now so we can pay it in the next run.", True, "Tuân thủ quy trình + hỗ trợ đẩy nhanh."),
      ("OK, I pay first, approve later.", False, "Chi trước duyệt sau là sai kiểm soát; thiếu 'will'."),
      ("PO no approve, cannot.", False, "Cộc lốc, sai ngữ pháp ('The PO isn't approved, so I can't')."),
    ]),
    ("Why is the new printer not in the asset register?", [
      ("It cost 12 million dong, which is under the 30 million threshold. So we recorded it as a tool, not a fixed asset.", True, "Giải thích ngưỡng ghi nhận TSCĐ rõ ràng."),
      ("I forget to add.", False, "Sai thì ('I forgot') và thực ra khoản này không cần ghi TSCĐ."),
      ("Printer is small, no need.", False, "Lý do sai: tiêu chí là giá trị và thời gian sử dụng, không phải kích thước."),
    ]),
    ("How many hours of overtime were paid this month?", [
      ("Eight hours, at 150% of your hourly rate. It's on line three of your payslip.", True, "Số giờ + mức tính + chỉ chỗ xem."),
      ("Some hours, check yourself.", False, "Mơ hồ, đẩy việc cho đồng nghiệp."),
      ("You get eight hour.", False, "Sai thì và số nhiều ('You were paid for eight hours')."),
    ]),
    ("Can I post this invoice to the rent account? I'm not sure.", [
      ("Let me see the invoice. It's for office cleaning, so please use the cleaning services account instead.", True, "Kiểm tra chứng từ + chỉ tài khoản đúng."),
      ("Any account, it's the same.", False, "Hạch toán tuỳ ý làm sai báo cáo."),
      ("If not sure, don't post never.", False, "Phủ định kép sai ngữ pháp và không giúp giải quyết."),
    ]),
   ]},
  "banking": {
   "scenarios": [
    ("bk_loan", "Doanh nghiệp nhỏ hỏi vay vốn", "You are the foreign owner of a small company in Vietnam. You want a working capital loan. Ask me about the interest rate, collateral, documents and how long approval takes."),
    ("bk_rate", "Khách hỏi lãi suất thả nổi", "You are a customer with a home loan. Your monthly payment went up. Ask me why, and ask about switching to a fixed rate."),
   ],
   "dialogues": [
    ("What documents do you need for a business loan?", [
      ("Your business licence, financial statements for the last two years, a cash flow plan and documents for the collateral.", True, "Liệt kê hồ sơ đầy đủ, rõ ràng."),
      ("Many documents, come back later.", False, "Mơ hồ, khách không chuẩn bị được."),
      ("Need licence and something.", False, "Thiếu chủ ngữ, thông tin không đầy đủ."),
    ]),
    ("Why did my monthly payment go up?", [
      ("Your loan has a floating rate, and it went up by 0.5% this quarter. I can show you the new schedule.", True, "Giải thích lãi thả nổi + đề nghị xem lịch trả nợ mới."),
      ("Because the rate up.", False, "Thiếu động từ ('went up') và chưa giải thích loại lãi suất."),
      ("All customers pay more, normal.", False, "Qua loa, không giải thích cho khách."),
    ]),
    ("Can I repay my loan early?", [
      ("Yes, you can. There's a 1% early repayment fee in the first three years. After that, it's free.", True, "Xác nhận + mức phí + điều kiện miễn phí."),
      ("Yes, anytime, free.", False, "Hứa sai nếu hợp đồng có phí trả nợ trước hạn."),
      ("Why you want pay early?", False, "Sai trật tự câu hỏi và nghe tò mò không cần thiết."),
    ]),
    ("Do I need collateral for this loan?", [
      ("For this amount, yes. We usually accept property or a term deposit as collateral.", True, "Trả lời rõ + loại tài sản bảo đảm thường chấp nhận."),
      ("No need, we trust you.", False, "Sai quy trình tín dụng; không được hứa trước."),
      ("Collateral is must.", False, "Sai ngữ pháp ('is required') và không nói loại tài sản."),
    ]),
   ]},
  "audit": {
   "scenarios": [
    ("au_assets", "Kiểm tra tài sản cố định", "You are the client's chief accountant. I am the auditor checking fixed assets. I found assets in the register that we couldn't see during the count. Explain and agree on next steps."),
    ("au_payroll", "Kiểm tra bảng lương", "You are the client's HR manager. I am the auditor testing payroll. Ask why I need employee contracts and bank transfer records, and how you should send confidential data."),
   ],
   "dialogues": [
    ("Why do you need to see the machines? The register is correct.", [
      ("We need to check that the assets really exist and are in use. It only takes about an hour.", True, "Giải thích mục đích kiểm tra hiện vật + thời gian ngắn."),
      ("Because register can be fake.", False, "Nghe như buộc tội khách hàng; thiếu mạo từ."),
      ("Rule of audit, sorry.", False, "Cộc lốc, không giải thích mục đích."),
    ]),
    ("How should we send you the payroll file? It's confidential.", [
      ("Please upload it to our secure portal with a password, and send the password separately.", True, "Hướng dẫn gửi dữ liệu nhạy cảm an toàn."),
      ("Just email it, it's fine.", False, "Gửi dữ liệu lương qua email không bảo vệ là rủi ro bảo mật."),
      ("Print and give me on the table.", False, "Sai ngữ pháp và dễ lộ thông tin."),
    ]),
    ("This machine is fully depreciated. Is that a problem?", [
      ("Not by itself. But if you still use it, we may ask you to review the useful life of similar machines.", True, "Trả lời chừng mực + khuyến nghị xem lại thời gian sử dụng."),
      ("Yes, big problem, you must fix.", False, "Phóng đại vấn đề, thiếu tân ngữ."),
      ("No, depreciation is not important.", False, "Xem nhẹ, sai tư duy kiểm toán."),
    ]),
    ("Why are you asking about these two employees?", [
      ("They were still on the payroll after they left in March. We'd like to see their termination papers and last payments.", True, "Nêu phát hiện cụ thể + chứng từ cần xem, giọng trung lập."),
      ("Because maybe fraud.", False, "Kết luận vội; thiếu chủ ngữ và động từ."),
      ("Just checking, no reason.", False, "Không minh bạch; kiểm toán nên nói rõ vấn đề đã phát hiện."),
    ]),
   ]},
  "fpa": {
   "scenarios": [
    ("fp_cash", "Dự báo dòng tiền với CFO", "You are the foreign CFO. I present the 13-week cash forecast. Ask about the lowest cash point, big payments and how we will cover any shortfall."),
    ("fp_costing", "Giải trình giá thành sản phẩm", "You are the foreign general manager. Our product unit cost rose this quarter. Ask me about material, labour and overhead, and what actions we propose."),
   ],
   "dialogues": [
    ("When is our lowest cash point this quarter?", [
      ("In week 9, when we pay the import tax. The balance drops to about 2 billion dong, so we may need the overdraft for a few days.", True, "Thời điểm + nguyên nhân + mức số dư + phương án."),
      ("Lowest is week 9 maybe.", False, "Mơ hồ, thiếu số liệu và phương án xử lý."),
      ("Don't worry, we always have money.", False, "Chủ quan, không dựa trên dự báo."),
    ]),
    ("Why did the unit cost rise 8%?", [
      ("Material prices rose 5%, and output fell 10%, so fixed overhead per unit went up.", True, "Tách hai nguyên nhân: giá vật tư và định phí trên đơn vị."),
      ("Everything is more expensive now.", False, "Chung chung, không phân tích."),
      ("Because production make less.", False, "Sai thì ('made less') và chưa giải thích cơ chế định phí."),
    ]),
    ("Should we use the overdraft or delay supplier payments?", [
      ("The overdraft would cost about 5 million dong in interest for the week. Delaying payments is free, but it could hurt our supplier relationships. I'd use the overdraft.", True, "So sánh chi phí và rủi ro hai phương án + khuyến nghị."),
      ("Delay all suppliers, it's free.", False, "Chỉ nhìn chi phí, bỏ qua rủi ro quan hệ với nhà cung cấp."),
      ("I don't know, you decide.", False, "FP&A cần đưa phân tích và khuyến nghị, không đẩy lại cho sếp."),
    ]),
    ("Can you add commentary to the dashboard?", [
      ("Sure. I'll add two or three lines for each chart, focusing on the main drivers.", True, "Đồng ý + cách trình bày cụ thể."),
      ("The numbers speak themselves.", False, "Sai giới từ ('speak for themselves') và từ chối giải trình."),
      ("Yes, I write long for you.", False, "Sai ngữ pháp; giải trình dài không giúp người đọc."),
    ]),
   ]},
 },
}
