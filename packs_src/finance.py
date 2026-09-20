# -*- coding: utf-8 -*-
# Gói "finance" — Tài chính · Kế toán: kế toán, giao dịch viên ngân hàng, kiểm toán, phân tích tài chính (FP&A).
# Người học làm việc với sếp, kiểm toán viên, khách hàng nước ngoài. Tên công ty / ngân hàng đều là tên tự đặt.
# Nội dung thuế/kế toán chỉ ở mức phổ thông, trung lập; không thay cho tư vấn chuyên môn.
# Chặng lõi lấy từ office: 3 (Email công việc), 11 (Phỏng vấn & phát triển sự nghiệp).
# Schema: xem packs_src/README.md. Build: python3 packs_src/build.py finance

PHASES = []

# ───────────────────────── 0. Hoá đơn & thanh toán ─────────────────────────
PHASES.append({
 "title": "Hoá đơn & thanh toán",
 "vocab": [
  ("invoice", "/ˈɪnvɔɪs/", "n", "hoá đơn", "We haven't received your <b>invoice</b> for May yet.", "Bên tôi chưa nhận được hoá đơn tháng Năm của anh/chị.", "請求書", "seikyūsho"),
  ("due date", "/ˈdjuː deɪt/", "n", "hạn thanh toán", "The <b>due date</b> for this invoice is 30 June.", "Hạn thanh toán của hoá đơn này là 30/6.", "支払期日", "shiharai kijitsu"),
  ("payment run", "/ˈpeɪmənt rʌn/", "n", "đợt chi (thanh toán định kỳ cho nhà cung cấp)", "Your invoice will be paid in Friday's <b>payment run</b>.", "Hoá đơn của anh/chị sẽ được chi trong đợt thanh toán thứ Sáu."),
  ("remittance", "/rɪˈmɪtns/", "n", "khoản chuyển tiền; thông báo chuyển tiền", "Please find the <b>remittance</b> advice attached.", "Gửi anh/chị thông báo chuyển tiền đính kèm.", "送金", "sōkin"),
  ("e-invoice", "/ˈiː ˌɪnvɔɪs/", "n", "hoá đơn điện tử", "Please send the <b>e-invoice</b> to our accounting email.", "Anh/chị gửi hoá đơn điện tử về email kế toán bên tôi nhé."),
  ("three-way match", "/ˌθriː weɪ ˈmætʃ/", "n", "đối chiếu ba bên (PO – phiếu nhập – hoá đơn)", "We can't pay until the <b>three-way match</b> is complete.", "Chưa đối chiếu xong PO, phiếu nhập và hoá đơn thì chưa thanh toán được."),
  ("authorise", "/ˈɔːθəraɪz/", "v", "phê duyệt, cho phép (chi tiền)", "Only the CFO can <b>authorise</b> payments over 500 million dong.", "Chỉ giám đốc tài chính mới được duyệt chi trên 500 triệu đồng."),
  ("proof of payment", "/ˌpruːf əv ˈpeɪmənt/", "n", "chứng từ thanh toán (vd: uỷ nhiệm chi có xác nhận của ngân hàng)", "I'll email you the <b>proof of payment</b> this afternoon.", "Chiều nay tôi sẽ email chứng từ chuyển khoản (uỷ nhiệm chi) cho anh/chị."),
  ("partial payment", "/ˌpɑːʃl ˈpeɪmənt/", "n", "thanh toán một phần", "We received a <b>partial payment</b> of 60%.", "Bên mình đã nhận thanh toán một phần, 60%."),
  ("bank details", "/ˈbæŋk ˌdiːteɪlz/", "n", "thông tin tài khoản ngân hàng", "Please confirm any change to your <b>bank details</b> by phone.", "Mọi thay đổi thông tin tài khoản vui lòng xác nhận lại qua điện thoại."),
 ],
 "phrases": [
  ("Could you send us the invoice for this order?", "Anh/chị gửi giúp hoá đơn cho đơn hàng này nhé."),
  ("The invoice is due on the 30th.", "Hoá đơn đến hạn thanh toán vào ngày 30."),
  ("The payment has been made. Please find the proof of payment attached.", "Đã thanh toán rồi ạ. Gửi anh/chị chứng từ thanh toán đính kèm."),
  ("Your invoice is scheduled for next Friday's payment run.", "Hoá đơn của anh/chị đã được xếp vào đợt chi thứ Sáu tới."),
  ("The PO number is missing on the invoice.", "Hoá đơn bị thiếu số PO."),
  ("The amount on the invoice doesn't match the PO.", "Số tiền trên hoá đơn không khớp với PO."),
  ("Could you reissue the invoice with the correct tax code?", "Anh/chị xuất lại hoá đơn với mã số thuế đúng giúp nhé."),
  ("We need approval before we can release the payment.", "Mình cần được duyệt rồi mới chi được."),
  ("Please allow two to three working days for the transfer.", "Tiền chuyển khoản sẽ mất hai đến ba ngày làm việc."),
  ("For security, we always call to confirm new bank details.", "Để an toàn, bên tôi luôn gọi điện xác nhận thông tin tài khoản mới."),
 ],
 "dialogues": [
  ("Hi, when will you pay our invoice?", [
    ("It's due on 30 June, and it's scheduled for our payment run on the 28th.", True, "Trả lời bằng ngày cụ thể + đợt chi."),
    ("We pay soon, don't worry.", False, "Mơ hồ, thiếu 'will'; nhà cung cấp cần ngày cụ thể."),
    ("When we have money.", False, "Nghe như công ty gặp khó khăn tài chính — rất không chuyên nghiệp."),
  ]),
  ("We sent the invoice last week. Did you receive it?", [
    ("Yes, we did. But the PO number is missing, so could you reissue it?", True, "Xác nhận + chỉ lỗi + yêu cầu xuất lại."),
    ("Yes, receive.", False, "Thiếu chủ ngữ và sai thì: 'Yes, we received it.'"),
    ("Maybe. I have many invoices.", False, "Thiếu trách nhiệm; nên kiểm tra rồi trả lời."),
  ]),
  ("Can you send me the proof of payment?", [
    ("Sure. I'll email you the transfer confirmation from the bank in a few minutes.", True, "Đồng ý + chứng từ cụ thể + thời gian."),
    ("I paid already, you check your bank.", False, "Đẩy việc cho đối tác, thiếu hợp tác."),
    ("Proof is no need.", False, "Sai ngữ pháp và từ chối yêu cầu hợp lý."),
  ]),
  ("Our bank details have changed. Please pay to this new account.", [
    ("Thanks for letting us know. For security, I'll call your finance manager to confirm before we update it.", True, "Quy trình đúng: xác minh qua kênh khác để chống lừa đảo đổi tài khoản."),
    ("OK, I change now.", False, "Cập nhật ngay qua email là rủi ro lừa đảo lớn; thiếu 'will'."),
    ("Why you change?", False, "Sai trật tự câu hỏi ('Why did you change it?') và chưa xử lý đúng quy trình."),
  ]),
  ("Why was only half of the invoice paid?", [
    ("We've only received 50% of the goods so far. We'll pay the rest once the other half arrives.", True, "Giải thích lý do + khi nào trả phần còn lại."),
    ("Because half.", False, "Câu cụt, không giải thích."),
    ("Our boss want to pay half.", False, "Sai chia động từ ('wants') và không nêu lý do nghiệp vụ."),
  ]),
 ],
 "listen": [
  ("The invoice is due at the end of June", ["invoice", "June"], "hạn thanh toán"),
  ("Please find the proof of payment attached", ["proof", "attached"], "gửi chứng từ thanh toán"),
  ("The PO number is missing on this invoice", ["number", "missing"], "hoá đơn thiếu thông tin"),
  ("We pay suppliers every Friday", ["suppliers", "Friday"], "lịch chi"),
  ("Hi Mai, we received your invoice today. The amount doesn't match the PO. Could you check it and send a new one?", ["received", "amount", "check"], "email phản hồi hoá đơn sai"),
  ("Your payment was sent this morning. It usually takes two working days. I've attached the bank confirmation.", ["morning", "working", "confirmation"], "báo đã chuyển tiền"),
 ],
})

# ───────────────────────── 1. Công nợ phải thu · phải trả ─────────────────────────
PHASES.append({
 "title": "Công nợ phải thu · phải trả",
 "vocab": [
  ("accounts receivable", "/əˌkaʊnts rɪˈsiːvəbl/", "n", "công nợ phải thu (AR)", "Our <b>accounts receivable</b> went up to 8 billion dong.", "Công nợ phải thu của mình tăng lên 8 tỷ đồng.", "売掛金", "urikakekin"),
  ("accounts payable", "/əˌkaʊnts ˈpeɪəbl/", "n", "công nợ phải trả (AP)", "She works in <b>accounts payable</b> and pays our suppliers.", "Chị ấy làm kế toán công nợ phải trả, lo thanh toán cho nhà cung cấp.", "買掛金", "kaikakekin"),
  ("overdue", "/ˌəʊvəˈdjuː/", "adj", "quá hạn (thanh toán)", "This invoice is 45 days <b>overdue</b>.", "Hoá đơn này đã quá hạn 45 ngày."),
  ("aging report", "/ˈeɪdʒɪŋ rɪˌpɔːt/", "n", "báo cáo tuổi nợ", "The <b>aging report</b> shows three customers over 90 days.", "Báo cáo tuổi nợ cho thấy ba khách nợ quá 90 ngày."),
  ("payment reminder", "/ˈpeɪmənt rɪˌmaɪndə/", "n", "thư/tin nhắc thanh toán", "We sent a second <b>payment reminder</b> yesterday.", "Hôm qua bên mình đã gửi thư nhắc nợ lần hai.", "督促状", "tokusokujō"),
  ("credit limit", "/ˈkredɪt ˌlɪmɪt/", "n", "hạn mức công nợ (tín dụng)", "This customer has reached their <b>credit limit</b>.", "Khách này đã chạm hạn mức công nợ.", "与信限度額", "yoshin gendogaku"),
  ("credit note", "/ˈkredɪt nəʊt/", "n", "credit note, chứng từ ghi giảm công nợ", "We'll issue a <b>credit note</b> for the returned goods.", "Bên mình sẽ xuất credit note cho số hàng bị trả lại."),
  ("outstanding", "/aʊtˈstændɪŋ/", "adj", "còn nợ, chưa thanh toán", "The <b>outstanding</b> balance is 120 million dong.", "Số dư còn nợ là 120 triệu đồng."),
  ("bad debt", "/ˌbæd ˈdet/", "n", "nợ khó đòi", "We made a provision for <b>bad debt</b> this year.", "Năm nay bên mình đã trích lập dự phòng nợ khó đòi.", "貸倒れ", "kashidaore"),
  ("collect", "/kəˈlekt/", "v", "thu (tiền, nợ)", "We need to <b>collect</b> 2 billion dong before the month ends.", "Mình cần thu được 2 tỷ đồng trước cuối tháng.", "回収する", "kaishū suru"),
 ],
 "phrases": [
  ("According to our records, this invoice is 30 days overdue.", "Theo sổ sách bên tôi, hoá đơn này đã quá hạn 30 ngày."),
  ("Could you let us know when we can expect payment?", "Anh/chị cho biết khi nào bên tôi có thể nhận thanh toán ạ?"),
  ("Please see the statement of account attached.", "Gửi anh/chị bảng đối chiếu công nợ đính kèm."),
  ("Could you confirm the outstanding balance as of 31 May?", "Anh/chị xác nhận giúp số dư công nợ đến ngày 31/5 nhé."),
  ("If you have already paid, please ignore this reminder.", "Nếu anh/chị đã thanh toán, vui lòng bỏ qua thư nhắc này."),
  ("This customer is over their credit limit, so we need to hold new orders.", "Khách này vượt hạn mức công nợ nên mình phải tạm giữ đơn mới."),
  ("We'll issue a credit note for the price difference.", "Bên mình sẽ xuất credit note cho phần chênh lệch giá."),
  ("Our records show a different balance. Can we reconcile?", "Số dư bên tôi ghi nhận khác. Mình đối chiếu lại nhé?"),
  ("We can offer a payment plan over three months.", "Bên tôi có thể cho trả dần trong ba tháng."),
 ],
 "dialogues": [
  ("Hi, this is Anna from Solea Trading. You called about an invoice?", [
    ("Yes, thanks for calling back. Invoice 1245 was due on 15 May. Could you tell me when we can expect payment?", True, "Nói rõ số hoá đơn, hạn và hỏi lịch trả một cách lịch sự."),
    ("Yes. You pay late, why?", False, "Thiếu lịch sự, giọng trách móc; không nêu hoá đơn cụ thể."),
    ("Yes, you have debt with us.", False, "Dịch sát 'có nợ', nghe nặng nề: dùng 'outstanding invoice'."),
  ]),
  ("Sorry, our cash flow is tight this month.", [
    ("I understand. Could you pay half this week and the rest by the end of the month?", True, "Thông cảm + đề xuất phương án trả một phần."),
    ("That is your problem, not our problem.", False, "Cứng nhắc, làm xấu quan hệ khách hàng."),
    ("OK, pay when you can.", False, "Buông xuôi, không chốt mốc thời gian nào."),
  ]),
  ("Our balance is different from yours.", [
    ("Let's reconcile it. Could you send me your statement, and I'll compare it invoice by invoice?", True, "Đề xuất đối chiếu + cách làm cụ thể."),
    ("Our number is correct, yours is wrong.", False, "Khẳng định khi chưa kiểm tra, dễ gây tranh cãi."),
    ("Different how much?", False, "Câu hỏi kiểu Việt: 'How big is the difference?'"),
  ]),
  ("Why was our new order put on hold?", [
    ("Your account is over the credit limit. Once we receive payment for the overdue invoices, we'll release it.", True, "Giải thích lý do + điều kiện để giải phóng đơn."),
    ("Because you don't pay.", False, "Sai thì ('haven't paid') và nói thẳng gây mất lòng."),
    ("System hold, I don't know.", False, "Đổ cho hệ thống, không giải thích."),
  ]),
  ("Can you give us a credit note for the damaged goods?", [
    ("Yes. Once the warehouse confirms the return, we'll issue a credit note within two days.", True, "Đồng ý có điều kiện + thời gian cụ thể."),
    ("Credit note is difficult.", False, "Không trả lời rõ có hay không, không nêu lý do."),
    ("Yes, I give you now.", False, "Sai ngữ pháp và bỏ qua bước xác nhận hàng trả về."),
  ]),
 ],
 "listen": [
  ("This invoice is thirty days overdue", ["thirty", "overdue"], "hoá đơn quá hạn"),
  ("Please confirm the outstanding balance", ["confirm", "outstanding"], "xác nhận số dư"),
  ("The customer is over the credit limit", ["customer", "limit"], "vượt hạn mức"),
  ("We'll issue a credit note tomorrow", ["issue", "tomorrow"], "xuất credit note"),
  ("Dear customer, this is a friendly reminder. Invoice 1245 was due on 15 May. If you have already paid, please ignore this message.", ["reminder", "due", "ignore"], "thư nhắc thanh toán"),
  ("The aging report looks better this month. Only two customers are over sixty days. We collected four billion dong last week.", ["aging", "sixty", "collected"], "báo cáo công nợ"),
 ],
})

# ───────────────────────── 2. Đối chiếu & khoá sổ cuối tháng ─────────────────────────
PHASES.append({
 "title": "Đối chiếu & khoá sổ cuối tháng",
 "vocab": [
  ("month-end closing", "/ˌmʌnθ end ˈkləʊzɪŋ/", "n", "khoá sổ cuối tháng", "<b>Month-end closing</b> must be finished by the third working day.", "Khoá sổ cuối tháng phải xong trước ngày làm việc thứ ba.", "月次決算", "getsuji kessan"),
  ("reconciliation", "/ˌrekənˌsɪliˈeɪʃn/", "n", "đối chiếu (số dư, sổ sách)", "I'm doing the bank <b>reconciliation</b> for May.", "Tôi đang đối chiếu sổ phụ ngân hàng tháng Năm.", "照合", "shōgō"),
  ("journal entry", "/ˈdʒɜːnl ˌentri/", "n", "bút toán", "Please post a <b>journal entry</b> for the rent.", "Anh/chị hạch toán giúp bút toán tiền thuê văn phòng nhé.", "仕訳", "shiwake"),
  ("accrual", "/əˈkruːəl/", "n", "khoản trích trước (chi phí phải trả)", "We need an <b>accrual</b> for the electricity bill.", "Mình cần trích trước chi phí tiền điện."),
  ("ledger", "/ˈledʒə/", "n", "sổ cái, sổ chi tiết", "The balance in the <b>ledger</b> is different from the bank.", "Số dư trên sổ cái khác với ngân hàng.", "元帳", "motochō"),
  ("trial balance", "/ˌtraɪəl ˈbæləns/", "n", "bảng cân đối số phát sinh", "The <b>trial balance</b> is ready for review.", "Bảng cân đối số phát sinh đã sẵn sàng để soát xét.", "試算表", "shisanhyō"),
  ("adjustment", "/əˈdʒʌstmənt/", "n", "(bút toán) điều chỉnh", "We made an <b>adjustment</b> for the exchange rate difference.", "Bên mình đã điều chỉnh phần chênh lệch tỷ giá."),
  ("cut-off", "/ˈkʌt ɒf/", "n", "ghi nhận đúng kỳ (cut-off)", "Check the <b>cut-off</b>: these goods arrived on 1 June, not in May.", "Kiểm tra cut-off nhé: hàng này về ngày 1/6 chứ không phải tháng Năm."),
  ("prepayment", "/ˌpriːˈpeɪmənt/", "n", "chi phí trả trước", "The annual insurance is a <b>prepayment</b>, so we spread it over 12 months.", "Bảo hiểm năm là chi phí trả trước nên mình phân bổ trong 12 tháng.", "前払費用", "maebarai hiyō"),
  ("post", "/pəʊst/", "v", "ghi sổ, hạch toán", "Have you <b>posted</b> all the invoices for May?", "Anh/chị đã hạch toán hết hoá đơn tháng Năm chưa?"),
 ],
 "phrases": [
  ("We're closing the books for May this week.", "Tuần này bên mình khoá sổ tháng Năm."),
  ("Please send me all your invoices by the 2nd.", "Anh/chị gửi tôi toàn bộ hoá đơn trước ngày 2 nhé."),
  ("The bank reconciliation is done, and everything matches.", "Đã đối chiếu ngân hàng xong, mọi thứ đều khớp."),
  ("There's a difference of 3 million dong. I'm still looking into it.", "Có chênh lệch 3 triệu đồng, tôi vẫn đang kiểm tra."),
  ("We need to accrue the expenses we haven't been invoiced for.", "Mình cần trích trước các chi phí chưa có hoá đơn."),
  ("Could you approve this journal entry?", "Anh/chị duyệt giúp bút toán này nhé."),
  ("This invoice belongs to June, not May.", "Hoá đơn này thuộc kỳ tháng Sáu, không phải tháng Năm."),
  ("The trial balance will be ready tomorrow afternoon.", "Chiều mai sẽ có bảng cân đối số phát sinh."),
  ("Once the period is closed, we can't post any more entries.", "Khi đã khoá kỳ thì không hạch toán thêm được nữa."),
 ],
 "dialogues": [
  ("Is the bank reconciliation finished?", [
    ("Almost. There's one difference of 3 million dong. I think it's a bank fee, and I'll confirm it this afternoon.", True, "Báo tình trạng + chênh lệch + giả thuyết + thời hạn."),
    ("Almost finish.", False, "Thiếu chủ ngữ/động từ: 'It's almost finished.'"),
    ("Yes, I change the number so it match.", False, "Sai nghiệp vụ nghiêm trọng: không được 'ép' số cho khớp; sai ngữ pháp."),
  ]),
  ("Why do we need to accrue this cost?", [
    ("We used the service in May, but the invoice will only come in June. So we record the cost in May.", True, "Giải thích đúng nguyên tắc dồn tích bằng câu đơn giản."),
    ("Because the boss say so.", False, "Không giải thích nghiệp vụ; sai chia động từ ('says')."),
    ("Because no invoice.", False, "Câu cụt, chưa nêu rõ nguyên tắc ghi nhận đúng kỳ."),
  ]),
  ("Can I still post this invoice to May?", [
    ("Sorry, May is already closed. We'll post it in June and note it in the report.", True, "Xin lỗi + quy định + phương án xử lý."),
    ("Yes, I open again for you.", False, "Mở lại kỳ đã khoá tuỳ tiện là sai kiểm soát; thiếu 'will'."),
    ("No. Why you send late?", False, "Cộc lốc, sai trật tự câu hỏi."),
  ]),
  ("When will the trial balance be ready?", [
    ("By tomorrow at 3 p.m. I'm just waiting for the last two accruals.", True, "Thời gian cụ thể + lý do còn chờ."),
    ("Tomorrow maybe, I try.", False, "Mơ hồ, thiếu 'will'."),
    ("It will ready tomorrow.", False, "Thiếu 'be': 'It will be ready tomorrow.'"),
  ]),
  ("This journal entry doesn't have any supporting documents.", [
    ("You're right. I'll attach the contract and the calculation before you approve it.", True, "Thừa nhận + bổ sung chứng từ cụ thể."),
    ("It's OK, small amount.", False, "Bỏ qua kiểm soát — mọi bút toán đều cần chứng từ."),
    ("I forget, sorry sorry.", False, "Sai thì ('I forgot') và chưa nói cách khắc phục."),
  ]),
 ],
 "listen": [
  ("We're closing the books for May this week", ["closing", "books"], "khoá sổ"),
  ("The bank reconciliation is finished", ["bank", "reconciliation"], "đối chiếu ngân hàng"),
  ("Please post this journal entry today", ["journal", "today"], "hạch toán"),
  ("The trial balance will be ready tomorrow", ["trial", "ready"], "bảng cân đối số phát sinh"),
  ("Hi team, month-end closing starts on Monday. Please send all invoices and expense claims by Friday. Late documents will go into next month.", ["Monday", "claims", "Late"], "thông báo khoá sổ"),
  ("I've finished the bank reconciliation. There's a small difference of two million dong. It looks like a bank fee from the 31st.", ["finished", "difference", "fee"], "báo kết quả đối chiếu"),
 ],
})

# ───────────────────────── 3. Chi phí & hoàn ứng ─────────────────────────
PHASES.append({
 "title": "Chi phí & hoàn ứng",
 "vocab": [
  ("expense claim", "/ɪkˈspens kleɪm/", "n", "đề nghị thanh toán chi phí", "Please submit your <b>expense claim</b> within 30 days.", "Vui lòng nộp đề nghị thanh toán chi phí trong vòng 30 ngày.", "経費精算", "keihi seisan"),
  ("cash advance", "/ˌkæʃ ədˈvɑːns/", "n", "khoản tạm ứng", "I'd like a <b>cash advance</b> for my business trip.", "Tôi muốn tạm ứng cho chuyến công tác.", "仮払金", "karibaraikin"),
  ("receipt", "/rɪˈsiːt/", "n", "hoá đơn, biên lai (chứng từ chi)", "Every expense needs a <b>receipt</b> or a VAT invoice.", "Mọi khoản chi đều cần biên lai hoặc hoá đơn GTGT.", "領収書", "ryōshūsho"),
  ("per diem", "/ˌpɜː ˈdiːem/", "n", "phụ cấp công tác theo ngày", "The <b>per diem</b> for trips abroad is 50 dollars.", "Phụ cấp công tác nước ngoài là 50 đô mỗi ngày.", "日当", "nittō"),
  ("cost centre", "/ˈkɒst ˌsentə/", "n", "trung tâm chi phí (bộ phận chịu chi phí)", "Which <b>cost centre</b> should I charge this to?", "Khoản này tôi tính vào trung tâm chi phí nào?", "コストセンター", "kosuto sentā"),
  ("entertainment expense", "/ˌentəˈteɪnmənt ɪkˌspens/", "n", "chi phí tiếp khách", "Write the client's name on every <b>entertainment expense</b>.", "Mọi khoản chi tiếp khách phải ghi rõ tên khách.", "交際費", "kōsaihi"),
  ("petty cash", "/ˌpeti ˈkæʃ/", "n", "quỹ tiền mặt chi tiêu nhỏ (petty cash)", "Small purchases are paid from <b>petty cash</b>.", "Các khoản mua lặt vặt được chi từ quỹ tiền mặt nhỏ.", "小口現金", "koguchi genkin"),
  ("expense policy", "/ɪkˈspens ˌpɒləsi/", "n", "quy chế chi tiêu", "Taxis after 10 p.m. are allowed under the <b>expense policy</b>.", "Theo quy chế chi tiêu, đi taxi sau 10 giờ tối được thanh toán."),
  ("mileage", "/ˈmaɪlɪdʒ/", "n", "chi phí đi lại tính theo quãng đường", "You can claim <b>mileage</b> if you use your own car.", "Nếu đi xe riêng thì được thanh toán tiền xăng theo số km."),
  ("settle", "/ˈsetl/", "v", "quyết toán, hoàn (tạm ứng)", "Please <b>settle</b> your cash advance within a week of returning.", "Vui lòng hoàn ứng trong vòng một tuần sau khi về."),
 ],
 "phrases": [
  ("Please attach the original receipts to your expense claim.", "Vui lòng đính kèm hoá đơn gốc vào đề nghị thanh toán."),
  ("This receipt doesn't have the company's tax code.", "Hoá đơn này không có mã số thuế công ty."),
  ("Your claim is over the limit in the expense policy.", "Khoản bạn đề nghị vượt hạn mức trong quy chế chi tiêu."),
  ("Could you tell me the purpose of this expense?", "Anh/chị cho biết mục đích của khoản chi này nhé."),
  ("I need your manager's approval before I can pay this.", "Tôi cần sếp của anh/chị duyệt rồi mới chi được."),
  ("You'll receive the money with your next salary.", "Anh/chị sẽ nhận khoản này cùng kỳ lương tới."),
  ("You still have an advance of 5 million dong to settle.", "Anh/chị vẫn còn 5 triệu tạm ứng chưa hoàn."),
  ("Hotel bills must show your name and the dates of stay.", "Hoá đơn khách sạn phải ghi tên anh/chị và ngày lưu trú."),
  ("Which cost centre should we charge this to?", "Khoản này mình hạch toán vào bộ phận nào?"),
 ],
 "dialogues": [
  ("Why was my expense claim rejected?", [
    ("Two receipts are missing, and the taxi cost is over the policy limit. Could you add the receipts and a short explanation?", True, "Nêu lý do cụ thể + hướng dẫn cách bổ sung."),
    ("Because wrong.", False, "Câu cụt, không nói sai ở đâu."),
    ("You spend too much money.", False, "Nghe như trách móc; sai thì ('spent') và thiếu lý do theo quy chế."),
  ]),
  ("I lost the receipt for my hotel. What should I do?", [
    ("Please ask the hotel for a copy of the invoice. If that's not possible, fill in the missing receipt form.", True, "Đưa hai phương án xử lý rõ ràng."),
    ("No receipt, no money.", False, "Cộc lốc, không hỗ trợ đồng nghiệp."),
    ("It's OK, I pay you anyway.", False, "Sai quy trình chứng từ; sai ngữ pháp ('I'll pay you')."),
  ]),
  ("Can I get a cash advance for my trip to Singapore?", [
    ("Sure. Please fill in the advance form, get your manager's approval, and send it by Wednesday.", True, "Đồng ý + các bước cụ thể + hạn nộp."),
    ("Yes, how much you want?", False, "Thiếu trợ động từ: 'How much do you need?' — và bỏ qua quy trình."),
    ("Advance is difficult, you pay first.", False, "Từ chối không có căn cứ quy chế."),
  ]),
  ("When will I get my money back?", [
    ("Your claim was approved yesterday, so you'll get it with this month's salary.", True, "Tình trạng + thời điểm nhận tiền."),
    ("Soon, be patient.", False, "Mơ hồ và hơi trịch thượng."),
    ("I don't know, accounting is busy.", False, "Né tránh, trong khi chính mình là kế toán."),
  ]),
  ("Is dinner with a client covered?", [
    ("Yes, it's an entertainment expense. Please write the client's name and company on the claim.", True, "Xác nhận + phân loại + yêu cầu thông tin cần thiết."),
    ("Yes, cover all.", False, "Thiếu chủ ngữ và 'all' là hứa quá mức, bỏ qua hạn mức."),
    ("Dinner is personal, no.", False, "Sai — tiếp khách vì công việc thường được thanh toán theo quy chế."),
  ]),
 ],
 "listen": [
  ("Please attach the original receipts", ["attach", "receipts"], "đính kèm hoá đơn"),
  ("Your expense claim has been approved", ["claim", "approved"], "đề nghị được duyệt"),
  ("Please settle your cash advance this week", ["settle", "advance"], "nhắc hoàn ứng"),
  ("The taxi cost is over the limit", ["taxi", "limit"], "vượt hạn mức"),
  ("Hi Nam, I've checked your expense claim. The hotel receipt is missing. Please send it by Friday so we can pay you this month.", ["checked", "hotel", "Friday"], "phản hồi đề nghị thanh toán"),
  ("For trips abroad, the per diem is fifty dollars a day. It covers meals and local transport. Hotels are paid separately.", ["abroad", "meals", "separately"], "quy chế công tác phí"),
 ],
})

# ───────────────────────── 4. Ngân sách & dự báo ─────────────────────────
PHASES.append({
 "title": "Ngân sách & dự báo",
 "vocab": [
  ("forecast", "/ˈfɔːkɑːst/", "n", "dự báo", "The latest <b>forecast</b> shows revenue slightly below plan.", "Dự báo mới nhất cho thấy doanh thu hơi thấp hơn kế hoạch.", "予測", "yosoku"),
  ("headcount", "/ˈhedkaʊnt/", "n", "số lượng nhân sự (định biên)", "<b>Headcount</b> will stay at 120 next year.", "Năm sau số lượng nhân sự vẫn giữ ở mức 120."),
  ("allocate", "/ˈæləkeɪt/", "v", "phân bổ", "We <b>allocate</b> IT costs to each department by headcount.", "Chi phí IT được phân bổ cho từng phòng theo số nhân sự.", "配賦する", "haifu suru"),
  ("overspend", "/ˌəʊvəˈspend/", "v", "chi vượt (ngân sách)", "Marketing <b>overspent</b> by 200 million dong in Q2.", "Quý 2 phòng marketing chi vượt 200 triệu đồng."),
  ("underspend", "/ˌʌndəˈspend/", "v", "chi thấp hơn (ngân sách)", "We <b>underspent</b> on training because two courses were cancelled.", "Chi đào tạo thấp hơn ngân sách vì hai khoá học bị huỷ."),
  ("assumption", "/əˈsʌmpʃn/", "n", "giả định", "Our main <b>assumption</b> is a 5% price increase.", "Giả định chính của mình là giá tăng 5%.", "前提", "zentei"),
  ("capex", "/ˈkæpeks/", "n", "chi phí đầu tư (CAPEX)", "The new machine is <b>capex</b>, not an operating cost.", "Máy mới là chi phí đầu tư, không phải chi phí hoạt động.", "設備投資", "setsubi tōshi"),
  ("opex", "/ˈəʊpeks/", "n", "chi phí hoạt động (OPEX)", "Rent and salaries are the biggest parts of <b>opex</b>.", "Tiền thuê và lương là phần lớn nhất của chi phí hoạt động."),
  ("full-year", "/ˌfʊl ˈjɪə/", "adj", "(cả) năm", "The <b>full-year</b> forecast is 150 billion dong.", "Dự báo cả năm là 150 tỷ đồng."),
  ("annual plan", "/ˌænjuəl ˈplæn/", "n", "kế hoạch năm", "Please send your department's <b>annual plan</b> by 15 October.", "Vui lòng gửi kế hoạch năm của phòng trước ngày 15/10.", "年度計画", "nendo keikaku"),
 ],
 "phrases": [
  ("We're 5% over budget this quarter.", "Quý này mình vượt ngân sách 5%."),
  ("We're still within budget for travel.", "Chi công tác vẫn nằm trong ngân sách."),
  ("Could you send me your budget request by Friday?", "Anh/chị gửi tôi đề xuất ngân sách trước thứ Sáu nhé."),
  ("What are the main assumptions behind this forecast?", "Dự báo này dựa trên những giả định chính nào?"),
  ("We've updated the full-year forecast.", "Bên mình đã cập nhật dự báo cả năm."),
  ("If sales drop by 10%, we'll need to cut costs.", "Nếu doanh số giảm 10%, mình sẽ phải cắt giảm chi phí."),
  ("This purchase isn't in the budget. Can we move it to next year?", "Khoản mua này không có trong ngân sách. Mình dời sang năm sau được không?"),
  ("Let's compare actual spending with the plan.", "Mình so sánh chi tiêu thực tế với kế hoạch nhé."),
  ("We need to allocate more money to marketing in Q4.", "Quý 4 mình cần phân bổ thêm tiền cho marketing."),
 ],
 "dialogues": [
  ("Are we still within budget?", [
    ("Not quite. We're 4% over, mainly because of higher shipping costs.", True, "Trả lời thẳng + con số + nguyên nhân chính."),
    ("Budget is OK I think.", False, "Mơ hồ ('I think'), thiếu số liệu cụ thể."),
    ("We over budget 4%.", False, "Thiếu động từ: 'We're 4% over budget.'"),
  ]),
  ("What's your forecast for Q4?", [
    ("We expect revenue of about 40 billion dong, based on the current order book.", True, "Con số + căn cứ dự báo."),
    ("Q4 will very good.", False, "Thiếu 'be' và không có số liệu."),
    ("Forecast is guess, I can't say.", False, "Né tránh — dự báo cần có con số và giả định rõ."),
  ]),
  ("Can we buy a new printer this month?", [
    ("It's not in this year's budget. If it's urgent, I can ask the CFO for approval.", True, "Nêu thực tế + phương án xin duyệt ngoại lệ."),
    ("No money, no printer.", False, "Cộc lốc, không đưa phương án."),
    ("Yes, buy anything you want.", False, "Hứa vượt quyền, bỏ qua kiểm soát ngân sách."),
  ]),
  ("Why did you change the full-year forecast?", [
    ("Two big customers delayed their orders to next year, so we reduced revenue by 8 billion dong.", True, "Nguyên nhân cụ thể + tác động bằng số."),
    ("Because the market is change.", False, "Sai ngữ pháp ('is changing') và quá chung chung."),
    ("The boss tell me change.", False, "Sai chia động từ và không giải thích nghiệp vụ."),
  ]),
  ("Is this new machine opex or capex?", [
    ("It's capex, because we'll use it for more than one year. We'll depreciate it over five years.", True, "Phân loại đúng + lý do + cách ghi nhận."),
    ("Opex, because we pay money.", False, "Sai kiến thức: tài sản dùng nhiều năm là capex."),
    ("Same, no difference.", False, "Sai — capex và opex ảnh hưởng báo cáo khác nhau."),
  ]),
 ],
 "listen": [
  ("We're five percent over budget this quarter", ["five", "budget"], "vượt ngân sách"),
  ("Please send your annual plan by October", ["annual", "October"], "hạn gửi kế hoạch năm"),
  ("The full-year forecast is one hundred billion dong", ["full-year", "hundred"], "dự báo cả năm"),
  ("Our main assumption is a price increase", ["assumption", "price"], "giả định"),
  ("We've updated the forecast for Q4. Revenue is down by six billion dong. The main reason is a delayed order from a big customer.", ["updated", "six", "delayed"], "cập nhật dự báo"),
  ("Marketing overspent in the first half. Travel is still within budget. So we'll move some money from travel to marketing.", ["overspent", "Travel", "move"], "điều chỉnh ngân sách"),
 ],
})

# ───────────────────────── 5. Báo cáo tài chính ─────────────────────────
PHASES.append({
 "title": "Báo cáo tài chính",
 "vocab": [
  ("balance sheet", "/ˈbæləns ʃiːt/", "n", "bảng cân đối kế toán", "The <b>balance sheet</b> shows what we own and what we owe.", "Bảng cân đối kế toán cho thấy mình có gì và nợ gì.", "貸借対照表", "taishaku taishōhyō"),
  ("income statement", "/ˈɪnkʌm ˌsteɪtmənt/", "n", "báo cáo kết quả kinh doanh (P&L)", "The <b>income statement</b> shows a profit of 5 billion dong.", "Báo cáo kết quả kinh doanh cho thấy lãi 5 tỷ đồng.", "損益計算書", "son'eki keisansho"),
  ("cash flow", "/ˈkæʃ fləʊ/", "n", "dòng tiền", "We're profitable, but our <b>cash flow</b> is weak.", "Công ty có lãi nhưng dòng tiền yếu.", "キャッシュフロー", "kyasshu furō"),
  ("revenue", "/ˈrevənjuː/", "n", "doanh thu", "<b>Revenue</b> grew by 12% compared with last year.", "Doanh thu tăng 12% so với năm ngoái.", "売上", "uriage"),
  ("gross margin", "/ˌɡrəʊs ˈmɑːdʒɪn/", "n", "biên lợi nhuận gộp", "Our <b>gross margin</b> fell from 35% to 31%.", "Biên lợi nhuận gộp giảm từ 35% xuống 31%.", "粗利率", "arariritsu"),
  ("net profit", "/ˌnet ˈprɒfɪt/", "n", "lợi nhuận ròng (sau thuế)", "<b>Net profit</b> for the year was 18 billion dong.", "Lợi nhuận ròng cả năm là 18 tỷ đồng.", "純利益", "junrieki"),
  ("asset", "/ˈæset/", "n", "tài sản", "Our biggest <b>asset</b> is the factory building.", "Tài sản lớn nhất của mình là nhà xưởng.", "資産", "shisan"),
  ("liability", "/ˌlaɪəˈbɪləti/", "n", "nợ phải trả", "Bank loans are shown as <b>liabilities</b>.", "Các khoản vay ngân hàng được ghi nhận là nợ phải trả.", "負債", "fusai"),
  ("depreciation", "/dɪˌpriːʃiˈeɪʃn/", "n", "khấu hao", "<b>Depreciation</b> on the new machines is 300 million dong a month.", "Khấu hao máy móc mới là 300 triệu đồng mỗi tháng.", "減価償却", "genka shōkyaku"),
  ("equity", "/ˈekwəti/", "n", "vốn chủ sở hữu", "Total assets equal liabilities plus <b>equity</b>.", "Tổng tài sản bằng nợ phải trả cộng vốn chủ sở hữu.", "自己資本", "jiko shihon"),
 ],
 "phrases": [
  ("Revenue for the quarter was 45 billion dong.", "Doanh thu quý là 45 tỷ đồng."),
  ("Net profit went up by 8% year on year.", "Lợi nhuận ròng tăng 8% so với cùng kỳ."),
  ("Gross margin dropped because material costs increased.", "Biên lợi nhuận gộp giảm do chi phí nguyên vật liệu tăng."),
  ("Cash flow from operations is positive this month.", "Dòng tiền từ hoạt động kinh doanh tháng này dương."),
  ("The draft financial statements are ready for your review.", "Bản nháp báo cáo tài chính đã sẵn sàng để anh/chị soát xét."),
  ("Most of the increase in assets is new equipment.", "Phần lớn tài sản tăng thêm là thiết bị mới."),
  ("We prepare the statements under Vietnamese Accounting Standards.", "Bên mình lập báo cáo theo Chuẩn mực Kế toán Việt Nam."),
  ("The group reports under IFRS, so we need some adjustments.", "Tập đoàn báo cáo theo IFRS nên mình cần một số điều chỉnh."),
  ("Let me walk you through the main numbers.", "Để tôi trình bày qua các số liệu chính."),
 ],
 "dialogues": [
  ("We made a profit. Why is our cash so low?", [
    ("Many customers haven't paid yet, and we bought a lot of stock. So profit is good, but cash is tied up.", True, "Giải thích khác biệt lợi nhuận và dòng tiền bằng lý do cụ thể."),
    ("Profit and cash is same thing.", False, "Sai kiến thức: lãi không đồng nghĩa có tiền; 'is' phải là 'are'."),
    ("Maybe the bank make mistake.", False, "Đổ lỗi vô căn cứ; sai chia động từ."),
  ]),
  ("Why did gross margin go down?", [
    ("Material prices rose by 10%, but we only increased our selling prices by 3%.", True, "Nguyên nhân rõ bằng số liệu so sánh."),
    ("Because cost up.", False, "Câu cụt thiếu động từ: 'Because costs went up.'"),
    ("Gross margin is not important, net profit is OK.", False, "Né câu hỏi của sếp."),
  ]),
  ("When will the financial statements be ready?", [
    ("The draft will be ready on Thursday, and the final version after your review next Monday.", True, "Mốc bản nháp + mốc bản cuối."),
    ("Thursday is ready.", False, "Dịch sát 'thứ Năm là xong': 'It'll be ready on Thursday.'"),
    ("When finish, I send.", False, "Thiếu chủ ngữ và không có thời gian cụ thể."),
  ]),
  ("What's the biggest item on the balance sheet?", [
    ("Fixed assets, mainly the factory and machines. They're about 60% of total assets.", True, "Trả lời cụ thể + tỷ trọng."),
    ("The biggest is many things.", False, "Không trả lời được câu hỏi."),
    ("Factory building is very big.", False, "Hiểu nhầm 'big' theo nghĩa kích thước, không nói giá trị."),
  ]),
  ("Why did depreciation increase this year?", [
    ("We bought two new production lines in January, so depreciation went up by about 3 billion dong.", True, "Nguyên nhân + tác động bằng số."),
    ("Because we buy machine.", False, "Sai thì ('bought') và thiếu số nhiều ('machines')."),
    ("Depreciation is automatic, I don't know.", False, "Né tránh; kế toán cần giải thích được biến động."),
  ]),
 ],
 "listen": [
  ("Revenue grew by twelve percent this year", ["Revenue", "twelve"], "tăng trưởng doanh thu"),
  ("Our gross margin fell to thirty-one percent", ["margin", "thirty-one"], "biên lợi nhuận"),
  ("Cash flow from operations is positive", ["Cash", "positive"], "dòng tiền"),
  ("The draft statements are ready for review", ["draft", "review"], "báo cáo nháp"),
  ("Let me walk you through the income statement. Revenue was up ten percent. But net profit was flat because of higher interest costs.", ["income", "flat", "interest"], "trình bày báo cáo KQKD"),
  ("On the balance sheet, total assets increased by twenty billion dong. Most of this is new equipment. We paid for it with a bank loan.", ["increased", "equipment", "loan"], "giải thích bảng cân đối"),
 ],
})

# ───────────────────────── 6. Kiểm toán & tuân thủ ─────────────────────────
PHASES.append({
 "title": "Kiểm toán & tuân thủ",
 "vocab": [
  ("audit", "/ˈɔːdɪt/", "n", "kiểm toán", "The year-end <b>audit</b> starts on 10 January.", "Kiểm toán cuối năm bắt đầu ngày 10/1.", "監査", "kansa"),
  ("external auditor", "/ɪkˌstɜːnl ˈɔːdɪtə/", "n", "kiểm toán viên độc lập", "The <b>external auditors</b> will be here for two weeks.", "Kiểm toán độc lập sẽ làm việc ở đây hai tuần.", "外部監査人", "gaibu kansanin"),
  ("internal control", "/ɪnˌtɜːnl kənˈtrəʊl/", "n", "kiểm soát nội bộ", "Good <b>internal controls</b> help prevent fraud.", "Kiểm soát nội bộ tốt giúp ngăn gian lận.", "内部統制", "naibu tōsei"),
  ("supporting documents", "/səˌpɔːtɪŋ ˈdɒkjumənts/", "n", "chứng từ kèm theo, chứng từ gốc", "Please prepare the <b>supporting documents</b> for these ten payments.", "Anh/chị chuẩn bị chứng từ kèm theo cho mười khoản chi này nhé.", "証憑", "shōhyō"),
  ("finding", "/ˈfaɪndɪŋ/", "n", "phát hiện (của kiểm toán)", "The auditors had three <b>findings</b> this year.", "Năm nay kiểm toán có ba phát hiện.", "指摘事項", "shiteki jikō"),
  ("sampling", "/ˈsɑːmplɪŋ/", "n", "chọn mẫu (kiểm tra)", "The auditors use <b>sampling</b> to test our invoices.", "Kiểm toán chọn mẫu để kiểm tra hoá đơn của mình.", "サンプリング", "sanpuringu"),
  ("comply", "/kəmˈplaɪ/", "v", "tuân thủ", "All payments must <b>comply</b> with the approval policy.", "Mọi khoản chi phải tuân thủ quy định phê duyệt.", "遵守する", "junshu suru"),
  ("segregation of duties", "/ˌseɡrɪˌɡeɪʃn əv ˈdjuːtiz/", "n", "phân tách nhiệm vụ (bất kiêm nhiệm)", "For <b>segregation of duties</b>, the person who records payments can't approve them.", "Để bất kiêm nhiệm, người ghi sổ khoản chi không được duyệt chi.", "職務分掌", "shokumu bunshō"),
  ("audit trail", "/ˈɔːdɪt treɪl/", "n", "dấu vết kiểm toán (lịch sử thay đổi)", "The system keeps an <b>audit trail</b> of every change.", "Hệ thống lưu lại dấu vết của mọi thay đổi."),
  ("management letter", "/ˈmænɪdʒmənt ˌletə/", "n", "thư quản lý (kiến nghị của kiểm toán)", "The auditors will send the <b>management letter</b> next month.", "Tháng sau kiểm toán sẽ gửi thư quản lý."),
 ],
 "phrases": [
  ("The auditors would like to see the contracts for these sales.", "Kiểm toán muốn xem hợp đồng của các khoản doanh thu này."),
  ("We'll send the documents you requested by Wednesday.", "Bên tôi sẽ gửi các chứng từ anh/chị yêu cầu trước thứ Tư."),
  ("Could you explain the reason for this large payment?", "Anh/chị giải thích giúp lý do của khoản chi lớn này nhé."),
  ("Here's the approval email for this transaction.", "Đây là email phê duyệt của giao dịch này."),
  ("I'm not sure. Let me check and get back to you today.", "Tôi chưa chắc, để tôi kiểm tra và phản hồi anh/chị trong hôm nay."),
  ("We've already fixed the issue from last year's audit.", "Bên mình đã khắc phục vấn đề từ đợt kiểm toán năm ngoái."),
  ("Who approved this journal entry?", "Ai đã duyệt bút toán này?"),
  ("We agree with the finding and will fix it by March.", "Bên tôi đồng ý với phát hiện và sẽ khắc phục trước tháng Ba."),
  ("All payments over 100 million dong need two signatures.", "Mọi khoản chi trên 100 triệu đồng cần hai chữ ký."),
 ],
 "dialogues": [
  ("Could you give us the supporting documents for these ten payments?", [
    ("Of course. I'll prepare the invoices, contracts and approvals and send them by tomorrow noon.", True, "Đồng ý + liệt kê chứng từ + hạn gửi."),
    ("All documents is in the system, you check.", False, "Sai chia động từ ('are') và đẩy việc cho kiểm toán."),
    ("Ten is too many, can you choose five?", False, "Mặc cả phạm vi chọn mẫu của kiểm toán là không phù hợp."),
  ]),
  ("Why does the same person record and approve payments?", [
    ("We're a small team, but you're right. From next month, the chief accountant will approve all payments.", True, "Thừa nhận + biện pháp khắc phục cụ thể."),
    ("Because she is very honest.", False, "Tin tưởng cá nhân không thay được kiểm soát nội bộ."),
    ("Always like that, no problem.", False, "Bỏ qua rủi ro về bất kiêm nhiệm."),
  ]),
  ("I can't find the approval for this payment.", [
    ("Let me check. It may be in the director's email. I'll send it to you this afternoon.", True, "Nhận kiểm tra + khả năng + thời hạn."),
    ("Approval not need for small payment.", False, "Sai ngữ pháp và có thể sai quy chế — cần kiểm tra trước khi trả lời."),
    ("I sign for you now.", False, "Ký bổ sung sau khi bị hỏi là làm giả chứng từ — tuyệt đối không."),
  ]),
  ("What happened with last year's audit findings?", [
    ("We've fixed two of them. The third one, about stock counts, will be finished in March.", True, "Tiến độ cụ thể từng phát hiện."),
    ("We fix already.", False, "Sai thì ('We've fixed them') và không nói chi tiết."),
    ("I forget what finding.", False, "Thiếu chuẩn bị; nên nói 'Let me check the status.'"),
  ]),
  ("This sale was recorded on 31 December, but the goods were delivered in January.", [
    ("You're right. It's a cut-off error. We'll move it to January and adjust the revenue.", True, "Thừa nhận lỗi đúng kỳ + điều chỉnh cụ thể."),
    ("Customer ordered in December, so OK.", False, "Sai nguyên tắc: doanh thu thường ghi nhận khi giao hàng (chuyển giao quyền kiểm soát), không phải khi khách đặt hàng."),
    ("Only one day different.", False, "Xem nhẹ lỗi ghi nhận sai kỳ."),
  ]),
 ],
 "listen": [
  ("The year-end audit starts in January", ["audit", "January"], "lịch kiểm toán"),
  ("Please prepare the supporting documents", ["prepare", "documents"], "chuẩn bị chứng từ"),
  ("The auditors had three findings this year", ["auditors", "findings"], "phát hiện kiểm toán"),
  ("Payments over one hundred million dong need two signatures", ["Payments", "signatures"], "quy định duyệt chi"),
  ("We've selected twenty invoices as a sample. Could you prepare the contracts and delivery notes by Wednesday?", ["selected", "sample", "Wednesday"], "kiểm toán yêu cầu chứng từ"),
  ("Our main finding is about approvals. Some payments were approved by only one person. We recommend two signatures for large payments.", ["approvals", "person", "recommend"], "kiểm toán nêu phát hiện"),
 ],
})

# ───────────────────────── 7. Thuế cơ bản ─────────────────────────
PHASES.append({
 "title": "Thuế cơ bản",
 "vocab": [
  ("VAT", "/ˌviː eɪ ˈtiː/", "n", "thuế giá trị gia tăng (GTGT)", "Does this price include <b>VAT</b>?", "Giá này đã bao gồm thuế GTGT chưa?", "付加価値税", "fuka kachi zei"),
  ("corporate income tax", "/ˌkɔːpərət ˈɪnkʌm tæks/", "n", "thuế thu nhập doanh nghiệp (TNDN)", "We pay <b>corporate income tax</b> on our taxable profit.", "Công ty nộp thuế TNDN trên thu nhập chịu thuế.", "法人税", "hōjinzei"),
  ("personal income tax", "/ˌpɜːsənl ˈɪnkʌm tæks/", "n", "thuế thu nhập cá nhân (TNCN)", "We deduct <b>personal income tax</b> from salaries every month.", "Hằng tháng công ty khấu trừ thuế TNCN từ lương.", "個人所得税", "kojin shotokuzei"),
  ("tax return", "/ˈtæks rɪˌtɜːn/", "n", "tờ khai thuế", "We must submit every <b>tax return</b> on time.", "Mình phải nộp mọi tờ khai thuế đúng hạn.", "税務申告書", "zeimu shinkokusho"),
  ("withholding tax", "/wɪðˈhəʊldɪŋ tæks/", "n", "thuế khấu trừ tại nguồn (vd: thuế nhà thầu)", "We must pay <b>withholding tax</b> on this payment to the foreign supplier.", "Với khoản thanh toán này cho nhà cung cấp nước ngoài, mình phải khấu trừ và nộp thuế nhà thầu.", "源泉徴収税", "gensen chōshūzei"),
  ("deductible", "/dɪˈdʌktəbl/", "adj", "được trừ (khi tính thuế)", "This cost is not <b>deductible</b> without a valid invoice.", "Chi phí này không được trừ nếu không có hoá đơn hợp lệ."),
  ("input VAT", "/ˌɪnpʊt ˌviː eɪ ˈtiː/", "n", "thuế GTGT đầu vào", "We can claim the <b>input VAT</b> on these purchases.", "Mình được khấu trừ thuế GTGT đầu vào của các khoản mua này."),
  ("tax authority", "/ˈtæks ɔːˌθɒrəti/", "n", "cơ quan thuế", "The <b>tax authority</b> asked for more documents.", "Cơ quan thuế yêu cầu bổ sung hồ sơ.", "税務当局", "zeimu tōkyoku"),
  ("penalty", "/ˈpenəlti/", "n", "tiền phạt", "Late filing can lead to a <b>penalty</b>.", "Nộp tờ khai trễ có thể bị phạt."),
  ("file", "/faɪl/", "v", "nộp (tờ khai)", "We need to <b>file</b> the VAT return before the deadline.", "Mình phải nộp tờ khai GTGT trước hạn.", "申告する", "shinkoku suru"),
 ],
 "phrases": [
  ("The price is 10 million dong, excluding VAT.", "Giá là 10 triệu đồng, chưa bao gồm VAT."),
  ("We file the VAT return every month.", "Bên mình nộp tờ khai VAT theo tháng."),
  ("When is the deadline for the VAT return?", "Hạn nộp tờ khai VAT là khi nào?"),
  ("Without a valid VAT invoice, we can't claim the input VAT.", "Không có hoá đơn GTGT hợp lệ thì không được khấu trừ VAT đầu vào."),
  ("Is this expense deductible for corporate income tax?", "Chi phí này có được trừ khi tính thuế TNDN không?"),
  ("We need to pay withholding tax on payments to foreign contractors.", "Mình phải nộp thuế nhà thầu khi thanh toán cho nhà thầu nước ngoài."),
  ("The tax authority will review our records next month.", "Tháng sau cơ quan thuế sẽ kiểm tra sổ sách của mình."),
  ("I'd suggest we check this with our tax adviser.", "Tôi đề nghị mình hỏi lại tư vấn thuế về việc này."),
  ("We've finalised personal income tax for all employees.", "Bên mình đã quyết toán thuế TNCN cho toàn bộ nhân viên."),
 ],
 "dialogues": [
  ("Does your price include VAT?", [
    ("No, it doesn't. VAT will be added on the invoice, and I can send you the total amount today.", True, "Trả lời rõ + nói VAT cộng thêm trên hoá đơn + đề nghị gửi tổng tiền."),
    ("No include VAT.", False, "Dịch từng chữ: 'No, it doesn't include VAT.' / 'It's excluding VAT.'"),
    ("VAT is your problem.", False, "Thô lỗ, không cung cấp thông tin."),
  ]),
  ("Can we deduct this dinner for tax purposes?", [
    ("Only if we have a valid VAT invoice and it's clearly for business. I'll check the invoice.", True, "Nêu điều kiện chung + hành động kiểm tra."),
    ("Yes, all expenses can deduct.", False, "Sai kiến thức và sai ngữ pháp ('can be deducted')."),
    ("I don't know tax.", False, "Né tránh; kế toán nên kiểm tra hoặc hỏi tư vấn thuế."),
  ]),
  ("Why do we pay tax on this payment to a foreign company?", [
    ("It's foreign contractor tax. When a foreign company earns income from Vietnam, we withhold the tax and pay it for them.", True, "Giải thích đúng bản chất thuế nhà thầu bằng câu đơn giản."),
    ("Because Vietnam tax is high.", False, "Không giải thích được bản chất khoản thuế."),
    ("We don't need, it's their tax.", False, "Sai — bên Việt Nam thường có nghĩa vụ khấu trừ và nộp thay."),
  ]),
  ("When is the VAT return due?", [
    ("For monthly filing, it's usually due on the 20th of the following month. I'll put a reminder in the team calendar.", True, "Trả lời rõ hạn nộp theo tháng + chủ động đặt nhắc hạn."),
    ("Every month, sometime.", False, "Mơ hồ, dễ nộp trễ bị phạt."),
    ("It due 20.", False, "Thiếu động từ và giới từ: 'It's due on the 20th.'"),
  ]),
  ("The tax authority wants to review our records.", [
    ("OK. Let's prepare the invoices, contracts and tax returns, and ask our tax adviser to join the meeting.", True, "Bình tĩnh + chuẩn bị hồ sơ + mời tư vấn."),
    ("Oh no, we will be penalty!", False, "Hoảng loạn và dùng sai từ loại ('we'll get a penalty')."),
    ("Just say we are busy.", False, "Né tránh cơ quan thuế là rủi ro nghiêm trọng."),
  ]),
 ],
 "listen": [
  ("The price is ten million dong excluding VAT", ["ten", "excluding"], "giá chưa VAT"),
  ("We file the VAT return every month", ["file", "month"], "kỳ khai thuế"),
  ("This cost is not deductible without an invoice", ["deductible", "invoice"], "chi phí không được trừ"),
  ("The tax authority asked for more documents", ["authority", "documents"], "yêu cầu của cơ quan thuế"),
  ("Hi team, a reminder about VAT. The return for April is due on May 20. Please send me all purchase invoices by the 10th.", ["reminder", "April", "purchase"], "nhắc hạn khai thuế"),
  ("We're paying a foreign supplier for software. So we need to withhold contractor tax. I'll calculate it before the payment.", ["foreign", "withhold", "calculate"], "thuế nhà thầu"),
 ],
})

# ───────────────────────── 8. Ngân hàng & giao dịch khách hàng ─────────────────────────
PHASES.append({
 "title": "Ngân hàng & giao dịch khách hàng",
 "vocab": [
  ("account holder", "/əˈkaʊnt ˌhəʊldə/", "n", "chủ tài khoản", "Only the <b>account holder</b> can close the account.", "Chỉ chủ tài khoản mới được đóng tài khoản.", "口座名義人", "kōza meiginin"),
  ("deposit", "/dɪˈpɒzɪt/", "v/n", "gửi tiền (vào tài khoản); khoản tiền gửi", "I'd like to <b>deposit</b> 20 million dong into my account.", "Tôi muốn nộp 20 triệu đồng vào tài khoản.", "入金する", "nyūkin suru"),
  ("withdraw", "/wɪðˈdrɔː/", "v", "rút tiền", "How much would you like to <b>withdraw</b> today?", "Hôm nay anh/chị muốn rút bao nhiêu ạ?", "引き出す", "hikidasu"),
  ("wire transfer", "/ˈwaɪə ˌtrænsfɜː/", "n", "chuyển khoản (điện chuyển tiền)", "An international <b>wire transfer</b> usually takes two to three working days.", "Chuyển tiền quốc tế thường mất hai đến ba ngày làm việc.", "電信送金", "denshin sōkin"),
  ("exchange rate", "/ɪksˈtʃeɪndʒ reɪt/", "n", "tỷ giá", "Today's <b>exchange rate</b> is on the screen.", "Tỷ giá hôm nay hiển thị trên màn hình ạ.", "為替レート", "kawase rēto"),
  ("interest rate", "/ˈɪntrəst reɪt/", "n", "lãi suất", "The <b>interest rate</b> for a 12-month deposit is 5% a year.", "Lãi suất tiền gửi 12 tháng là 5%/năm.", "金利", "kinri"),
  ("proof of identity", "/ˌpruːf əv aɪˈdentəti/", "n", "giấy tờ tuỳ thân", "Could I see your passport as <b>proof of identity</b>?", "Cho tôi xem hộ chiếu để xác minh danh tính nhé.", "本人確認書類", "honnin kakunin shorui"),
  ("term deposit", "/ˈtɜːm dɪˌpɒzɪt/", "n", "tiền gửi có kỳ hạn", "If you close the <b>term deposit</b> early, you'll get a lower rate.", "Nếu tất toán tiền gửi có kỳ hạn trước hạn, anh/chị sẽ nhận lãi suất thấp hơn.", "定期預金", "teiki yokin"),
  ("transaction fee", "/trænˈzækʃn fiː/", "n", "phí giao dịch", "There's a <b>transaction fee</b> of 50,000 dong.", "Có phí giao dịch 50.000 đồng.", "手数料", "tesūryō"),
  ("bank statement", "/ˈbæŋk ˌsteɪtmənt/", "n", "sao kê ngân hàng", "Can I get a <b>bank statement</b> for the last three months?", "Tôi lấy sao kê ba tháng gần nhất được không?"),
 ],
 "phrases": [
  ("How can I help you today?", "Hôm nay tôi có thể giúp gì cho anh/chị ạ?"),
  ("Could I see your passport, please?", "Cho tôi xem hộ chiếu của anh/chị được không ạ?"),
  ("Please fill in this form and sign here.", "Anh/chị điền mẫu này và ký vào đây giúp tôi."),
  ("The money will arrive in two to three working days.", "Tiền sẽ đến trong hai đến ba ngày làm việc."),
  ("Today's buying rate for US dollars is on the screen.", "Tỷ giá mua đô la Mỹ hôm nay hiển thị trên màn hình."),
  ("There's a fee of 0.2% for international transfers.", "Chuyển tiền quốc tế có phí 0,2%."),
  ("Please never share your OTP with anyone, even bank staff.", "Anh/chị tuyệt đối không cung cấp mã OTP cho ai, kể cả nhân viên ngân hàng."),
  ("For a transfer abroad, we need the purpose of payment and supporting documents.", "Chuyển tiền ra nước ngoài cần mục đích chuyển tiền và chứng từ kèm theo."),
  ("Would you like to open a term deposit?", "Anh/chị có muốn mở sổ tiết kiệm có kỳ hạn không ạ?"),
  ("Is there anything else I can help you with?", "Anh/chị cần tôi hỗ trợ gì thêm không ạ?"),
 ],
 "dialogues": [
  ("Hi, I'd like to open an account.", [
    ("Certainly. Could I see your passport and your visa or temporary residence card, please?", True, "Đồng ý + xin giấy tờ tuỳ thân lịch sự."),
    ("OK. Give passport.", False, "Mệnh lệnh cộc lốc, thiếu 'your' và 'please'."),
    ("You are foreigner, cannot.", False, "Sai thông tin và thiếu tôn trọng; người nước ngoài thường mở được khi đủ giấy tờ."),
  ]),
  ("How long does an international transfer take?", [
    ("Usually two to three working days, depending on the receiving bank.", True, "Thời gian + điều kiện ảnh hưởng."),
    ("It take two or three day.", False, "Sai chia động từ ('takes') và số nhiều ('days')."),
    ("Very fast, don't worry.", False, "Mơ hồ, khách không lên kế hoạch được."),
  ]),
  ("What's your interest rate for a 12-month deposit?", [
    ("It's 5% a year. If you withdraw before 12 months, you'll get a lower rate.", True, "Lãi suất + điều kiện rút trước hạn."),
    ("Interest is 5.", False, "Thiếu đơn vị, thiếu kỳ hạn tính lãi."),
    ("It's the best in Vietnam!", False, "Quảng cáo không có căn cứ, không trả lời số cụ thể."),
  ]),
  ("Someone from the bank called and asked for my OTP. Is that OK?", [
    ("No. The bank never asks for your OTP. Please don't share it, and let's lock your card now to be safe.", True, "Cảnh báo lừa đảo rõ ràng + hành động bảo vệ khách ngay."),
    ("Maybe it's our staff, you can give.", False, "Rất nguy hiểm — ngân hàng không bao giờ hỏi OTP."),
    ("I don't know who call you.", False, "Sai thì ('called') và bỏ lỡ việc cảnh báo khách."),
  ]),
  ("Why is there a fee on my transfer?", [
    ("International transfers have a 0.2% fee. The receiving bank may also charge a small fee.", True, "Giải thích phí của mình + khả năng phí ngân hàng nhận."),
    ("Because is bank rule.", False, "Thiếu chủ ngữ 'it': 'Because it's the bank's policy.' — lại chưa nói rõ mức phí."),
    ("All banks take fee, normal.", False, "Không giải thích cụ thể, nghe qua loa."),
  ]),
 ],
 "listen": [
  ("Could I see your passport please", ["see", "passport"], "xin giấy tờ"),
  ("The transfer will take two working days", ["transfer", "working"], "thời gian chuyển tiền"),
  ("Please never share your OTP with anyone", ["share", "OTP"], "cảnh báo bảo mật"),
  ("The interest rate is five percent a year", ["interest", "year"], "lãi suất"),
  ("To send money abroad, please fill in this form and bring your passport and the invoice. The fee is 0.2% of the amount.", ["abroad", "invoice", "fee"], "hướng dẫn chuyển tiền quốc tế"),
  ("Your term deposit ends next week. You can renew it at the same rate. Or you can move the money to your current account.", ["term", "renew", "current"], "tư vấn tiền gửi đến hạn"),
 ],
})

# ───────────────────────── 9. Họp số liệu với sếp nước ngoài ─────────────────────────
PHASES.append({
 "title": "Họp số liệu với sếp nước ngoài",
 "vocab": [
  ("variance", "/ˈveəriəns/", "n", "chênh lệch (so với kế hoạch)", "The biggest <b>variance</b> is in marketing costs.", "Chênh lệch lớn nhất nằm ở chi phí marketing.", "差異", "sai"),
  ("year-on-year", "/ˌjɪər ɒn ˈjɪə/", "adj/adv", "so với cùng kỳ năm trước", "Sales grew 9% <b>year-on-year</b>.", "Doanh số tăng 9% so với cùng kỳ.", "前年比", "zennenhi"),
  ("favourable", "/ˈfeɪvərəbl/", "adj", "tích cực, tốt hơn kế hoạch", "We have a <b>favourable</b> variance of 1 billion dong in staff costs.", "Chi phí nhân sự có chênh lệch có lợi 1 tỷ đồng (thấp hơn kế hoạch)."),
  ("one-off", "/ˌwʌn ˈɒf/", "adj", "phát sinh một lần, bất thường", "The repair was a <b>one-off</b> cost.", "Chi phí sửa chữa là khoản phát sinh một lần."),
  ("run rate", "/ˈrʌn reɪt/", "n", "mức hiện tại (ngoại suy cả năm)", "At the current <b>run rate</b>, we'll reach 120 billion dong this year.", "Với tốc độ hiện tại, năm nay mình sẽ đạt 120 tỷ đồng."),
  ("breakdown", "/ˈbreɪkdaʊn/", "n", "bảng chi tiết, phân tích chi tiết", "Could you send me a <b>breakdown</b> by customer?", "Anh/chị gửi tôi số liệu chi tiết theo từng khách hàng nhé.", "内訳", "uchiwake"),
  ("driver", "/ˈdraɪvə/", "n", "yếu tố tác động chính", "The main <b>driver</b> of the increase is higher volume.", "Yếu tố chính làm tăng là sản lượng cao hơn."),
  ("bottom line", "/ˌbɒtəm ˈlaɪn/", "n", "lợi nhuận cuối cùng; điểm mấu chốt", "The new contract will improve our <b>bottom line</b>.", "Hợp đồng mới sẽ cải thiện lợi nhuận của mình."),
  ("key takeaway", "/ˌkiː ˈteɪkəweɪ/", "n", "điểm chính cần nhớ", "The <b>key takeaway</b> is that costs are under control.", "Điểm chính là chi phí đang được kiểm soát."),
  ("timing difference", "/ˈtaɪmɪŋ ˌdɪfrəns/", "n", "chênh lệch do thời điểm (sẽ tự cân bằng)", "It's just a <b>timing difference</b>. The invoice will come next month.", "Đó chỉ là chênh lệch do thời điểm, tháng sau hoá đơn sẽ về."),
 ],
 "phrases": [
  ("Let me start with the key numbers.", "Tôi xin bắt đầu với các số liệu chính."),
  ("Revenue was 5% above plan.", "Doanh thu cao hơn kế hoạch 5%."),
  ("Costs were 3% higher than budget, mainly because of freight.", "Chi phí cao hơn ngân sách 3%, chủ yếu do cước vận chuyển."),
  ("This is a one-off cost, so it won't happen again next month.", "Đây là khoản phát sinh một lần nên tháng sau sẽ không lặp lại."),
  ("Compared with last year, profit is up 12%.", "So với năm ngoái, lợi nhuận tăng 12%."),
  ("The main driver is higher sales in the North.", "Yếu tố chính là doanh số miền Bắc tăng."),
  ("It's a timing difference. It will reverse next month.", "Đây là chênh lệch do thời điểm, tháng sau sẽ tự cân bằng."),
  ("I'll send you a detailed breakdown after the meeting.", "Sau cuộc họp tôi sẽ gửi anh/chị số liệu chi tiết."),
  ("The key takeaway is that cash is getting better.", "Điểm chính là dòng tiền đang cải thiện."),
  ("I don't have that number now, but I'll check and get back to you today.", "Hiện tôi chưa có số đó, tôi sẽ kiểm tra và báo lại anh/chị trong hôm nay."),
 ],
 "dialogues": [
  ("Can you walk me through this month's numbers?", [
    ("Sure. Revenue was 42 billion dong, 5% above plan. Costs were 2% over budget, mainly because of higher freight.", True, "Số liệu chính + so với kế hoạch + nguyên nhân — đúng kiểu báo cáo."),
    ("This month is good. Revenue up, cost up.", False, "Không có số, thiếu động từ, người nghe không hiểu gì thêm."),
    ("Sure. You can see in the file.", False, "Đẩy sếp tự đọc file thay vì trình bày."),
  ]),
  ("Why is marketing so far over budget?", [
    ("We ran the trade fair in May instead of June. It's a timing difference, so June will be lower.", True, "Giải thích nguyên nhân + chỉ rõ là chênh lệch thời điểm."),
    ("Marketing team spend too much.", False, "Đổ lỗi, sai chia động từ ('spent'), không nêu lý do."),
    ("I don't know, ask marketing.", False, "Né trách nhiệm phân tích số liệu."),
  ]),
  ("Is this repair cost going to happen every month?", [
    ("No, it's a one-off. Without it, we'd be 1% under budget.", True, "Trả lời có/không + tác động khi loại trừ khoản bất thường."),
    ("No, one time only I think.", False, "Thiếu chắc chắn và thiếu con số tác động."),
    ("Maybe yes, maybe no.", False, "Mơ hồ, không giúp sếp ra quyết định."),
  ]),
  ("What's the gross margin by product?", [
    ("I don't have the breakdown with me, but I'll send it to you by 3 p.m. today.", True, "Trung thực + hẹn thời gian gửi cụ thể."),
    ("About 30%, all products same.", False, "Đoán bừa số liệu trong họp là rất rủi ro."),
    ("I not prepare that.", False, "Sai ngữ pháp ('I didn't prepare that') và không đề xuất gửi sau."),
  ]),
  ("So what's the key message for the board?", [
    ("Sales are strong, but costs are rising. We need to review freight contracts before Q4.", True, "Thông điệp ngắn: tình hình + rủi ro + hành động."),
    ("Everything is OK.", False, "Quá chung chung, bỏ qua rủi ro chi phí."),
    ("Key message is many things.", False, "Không tóm tắt được, thiếu mạo từ."),
  ]),
 ],
 "listen": [
  ("Revenue was five percent above plan", ["Revenue", "plan"], "doanh thu so với kế hoạch"),
  ("This is a one-off repair cost", ["one-off", "repair"], "chi phí bất thường"),
  ("Profit grew nine percent year-on-year", ["Profit", "year-on-year"], "so với cùng kỳ"),
  ("I'll send you the breakdown after the meeting", ["breakdown", "meeting"], "hẹn gửi số chi tiết"),
  ("Let me start with the key numbers. Revenue was 42 billion dong. That's 5% above plan and 9% higher year-on-year.", ["key", "billion", "higher"], "mở đầu báo cáo tháng"),
  ("The main variance is in freight costs. Fuel prices went up in March. We're talking to two carriers to get better rates.", ["variance", "Fuel", "carriers"], "giải thích chênh lệch"),
 ],
})

# ───────────────────────── Vai trò (roles) ─────────────────────────
ROLES = {
 "accountant": {"label": "Kế toán", "emoji": "📒",
  "scenarios": [
   ("ac_supplier", "Nhà cung cấp đòi tiền", "You are a foreign supplier calling our accounting team. Your invoice is 20 days overdue. Ask politely but firmly when you will be paid."),
   ("ac_collect", "Gọi nhắc khách trả nợ", "You are the finance manager of a foreign customer. I call to remind you about two overdue invoices. Say your cash flow is tight and ask for more time."),
   ("ac_claim", "Nhân viên hỏi hoàn ứng", "You are a foreign colleague whose expense claim was rejected. Ask me why and what you need to do to get paid."),
   ("ac_close", "Sếp hỏi tiến độ khoá sổ", "You are my foreign finance manager. Ask about the status of month-end closing, any open reconciliations and when the trial balance will be ready."),
  ],
  "dialogues": [
   ("When will you pay our overdue invoice?", [
     ("I'm sorry for the delay. It's approved now and will go out in Friday's payment run.", True, "Xin lỗi + tình trạng + ngày chi cụ thể."),
     ("Our boss not sign yet.", False, "Thiếu trợ động từ ('hasn't signed') và đổ cho sếp."),
     ("Soon, maybe next month.", False, "Mơ hồ, làm nhà cung cấp mất niềm tin.")]),
   ("Can we have 30 more days to pay?", [
     ("I'll need to check with my manager. Could you pay half now and the rest in 30 days?", True, "Không hứa vượt quyền + đề xuất trả một phần."),
     ("OK, 60 days also fine.", False, "Tự gia hạn vượt quyền, gây rủi ro công nợ."),
     ("No. Pay now.", False, "Cứng nhắc, cộc lốc.")]),
   ("Why do you need the original receipts?", [
     ("We need a valid invoice or receipt for each expense. Without it, the cost may not be deductible for tax.", True, "Giải thích lý do theo quy định thuế, không nói quá tuyệt đối."),
     ("Because I need.", False, "Câu cụt, không giải thích."),
     ("Copy is not real.", False, "Nghe như nghi ngờ đồng nghiệp gian lận.")]),
   ("Is the bank reconciliation done?", [
     ("Yes, it's done. Everything matches except a 500,000 dong bank fee, which I've posted.", True, "Xác nhận + chênh lệch + đã xử lý."),
     ("Yes, finish.", False, "Thiếu chủ ngữ/động từ: 'Yes, it's finished.'"),
     ("Almost, only small difference, no matter.", False, "Xem nhẹ chênh lệch — mọi khoản lệch đều phải giải thích.")]),
   ("Can you post this invoice to last month?", [
     ("Sorry, last month is closed. I'll post it this month and add a note for the report.", True, "Tuân thủ khoá sổ + phương án."),
     ("OK, I open last month for you.", False, "Mở lại kỳ đã khoá tuỳ tiện là sai kiểm soát."),
     ("Why you always late?", False, "Trách móc, sai trật tự câu hỏi.")]),
   ("We've changed our bank account. Please pay the new one.", [
     ("Thanks. For security, we'll call your office on the number we have to confirm before updating.", True, "Xác minh qua kênh độc lập để chống lừa đảo."),
     ("OK, updated.", False, "Rủi ro lừa đảo đổi tài khoản — phải xác minh trước."),
     ("New account is not allowed.", False, "Từ chối sai; chỉ cần xác minh đúng quy trình.")]),
  ]},
 "banking": {"label": "Giao dịch viên ngân hàng", "emoji": "🏦",
  "scenarios": [
   ("bk_open", "Mở tài khoản cho người nước ngoài", "You are a foreigner working in Vietnam who wants to open a bank account. I am the bank teller. Ask what documents you need and how long it takes."),
   ("bk_transfer", "Chuyển tiền ra nước ngoài", "You are a foreign customer who wants to send 2,000 dollars to your family abroad. Ask about fees, the exchange rate, documents and timing."),
   ("bk_scam", "Khách nghi bị lừa đảo", "You are a worried customer. You received a call from someone saying they are from the bank and asking for your OTP. Ask me what to do."),
   ("bk_deposit", "Tư vấn tiền gửi", "You are a customer with 500 million dong to save. Ask me about term deposit rates, terms and what happens if you withdraw early."),
  ],
  "dialogues": [
   ("What do I need to open an account?", [
     ("Your passport and a valid visa or temporary residence card. It usually takes about 20 minutes.", True, "Liệt kê giấy tờ + thời gian xử lý."),
     ("Need passport.", False, "Thiếu chủ ngữ: 'You need your passport.'"),
     ("Many papers, very difficult.", False, "Mơ hồ, làm khách lo lắng.")]),
   ("Can I send money to my family abroad?", [
     ("Yes. Please fill in this form. The fee is 0.2%, and the money usually arrives in two to three days.", True, "Xác nhận + thủ tục + phí + thời gian."),
     ("Yes, you can sending.", False, "Sai dạng động từ ('you can send') và thiếu thông tin về thủ tục, phí, thời gian."),
     ("Foreigner cannot send money.", False, "Sai thông tin và thiếu mạo từ.")]),
   ("Someone called me and asked for my OTP.", [
     ("Please don't give it to anyone. The bank never asks for your OTP. Let's lock your card and check your recent transactions now.", True, "Cảnh báo + hành động bảo vệ ngay."),
     ("Maybe our staff, it's OK.", False, "Cực kỳ nguy hiểm — khuyến khích khách bị lừa."),
     ("That is not bank problem.", False, "Né trách nhiệm, sai ngữ pháp.")]),
   ("What's the exchange rate for US dollars today?", [
     ("Today's rates are on the screen. For 2,000 dollars, I can calculate the exact amount in dong for you.", True, "Chỉ nguồn tỷ giá + đề nghị tính cụ thể."),
     ("Rate change every day.", False, "Sai chia động từ ('changes') và không trả lời."),
     ("Very good rate today!", False, "Không có con số cụ thể.")]),
   ("Can I withdraw my term deposit early?", [
     ("Yes, you can, but you'll only get the demand deposit rate, which is much lower.", True, "Trả lời có + nói rõ thiệt hại lãi suất."),
     ("Yes, no problem, same interest.", False, "Sai thông tin — rút trước hạn thường mất lãi kỳ hạn."),
     ("No, cannot, wait until the end.", False, "Sai thông tin, thiếu chủ ngữ.")]),
   ("Why is my card blocked?", [
     ("I'm sorry. It was locked after three wrong PIN attempts. I can unlock it once I've checked your ID.", True, "Xin lỗi + lý do + cách xử lý kèm xác minh."),
     ("You enter wrong PIN.", False, "Sai thì ('entered') và nghe như trách khách."),
     ("System block, I don't know.", False, "Đổ cho hệ thống, không kiểm tra.")]),
  ]},
 "audit": {"label": "Kiểm toán", "emoji": "🔎",
  "scenarios": [
   ("au_kickoff", "Họp mở đầu kiểm toán", "You are the client's foreign CFO at the audit kickoff meeting. I am the audit senior. Ask about the timeline, what documents we need and who we will talk to."),
   ("au_request", "Yêu cầu chứng từ", "You are the client's chief accountant. I am the auditor asking for supporting documents for 15 payments. Ask why so many and how much time you have."),
   ("au_finding", "Trao đổi phát hiện kiểm toán", "You are the client's finance director. I am the auditor presenting a finding: one person records and approves payments. Push back a little, then agree on an action."),
   ("au_cutoff", "Lỗi ghi nhận sai kỳ", "You are the client's accountant. I am the auditor. I found a sale recorded in December but delivered in January. Explain your view and agree on the adjustment."),
  ],
  "dialogues": [
   ("How long will the audit take?", [
     ("About two weeks on site, and we'll send the draft report by the end of February.", True, "Thời gian tại hiện trường + mốc báo cáo."),
     ("Not long, don't worry.", False, "Mơ hồ, khách không chuẩn bị được."),
     ("It take two week.", False, "Sai chia động từ ('takes') và số nhiều ('weeks').")]),
   ("Why do you need so many documents?", [
     ("We test a sample of transactions to check they're real and correctly recorded. It's standard audit procedure.", True, "Giải thích mục đích chọn mẫu, giọng trung lập."),
     ("Because we don't trust you.", False, "Làm xấu quan hệ; kiểm toán là quy trình chuẩn, không phải nghi ngờ cá nhân."),
     ("Rule is rule.", False, "Cộc lốc, không giải thích.")]),
   ("Is this a serious finding?", [
     ("It's a medium-risk finding. We didn't find any loss, but we recommend a second approval for large payments.", True, "Mức độ + tác động + khuyến nghị."),
     ("Very serious, maybe fraud!", False, "Kết luận vội, không có căn cứ."),
     ("Not serious, forget it.", False, "Xem nhẹ, mất tính chuyên nghiệp của kiểm toán.")]),
   ("Can you remove this finding from the report?", [
     ("I understand your concern, but we need to report it. We can add your action plan to show it's being fixed.", True, "Giữ tính độc lập + đề xuất ghi nhận kế hoạch khắc phục."),
     ("OK, I remove for you.", False, "Vi phạm tính độc lập của kiểm toán."),
     ("No. Impossible.", False, "Đúng về nguyên tắc nhưng cộc lốc, không giải thích.")]),
   ("We can't find the contract for this payment.", [
     ("Could you check with the purchasing team? If there's no contract, please send the PO and the approval email.", True, "Đề xuất nơi tìm + chứng từ thay thế hợp lý."),
     ("No contract, big problem!", False, "Hoảng hốt, chưa tìm hướng giải quyết."),
     ("You make a new contract now.", False, "Gợi ý làm chứng từ mới sau sự việc là sai nghiêm trọng.")]),
   ("When will we get the management letter?", [
     ("We'll send a draft within two weeks after fieldwork ends, so you can add your comments.", True, "Thời gian + cơ hội phản hồi."),
     ("Later, when finish.", False, "Mơ hồ và thiếu chủ ngữ."),
     ("Management letter is not important.", False, "Sai — thư quản lý là kết quả quan trọng cho khách hàng.")]),
  ]},
 "fpa": {"label": "Phân tích tài chính (FP&A)", "emoji": "📈",
  "scenarios": [
   ("fp_monthly", "Báo cáo tháng với CFO", "You are the foreign CFO. I am the FP&A analyst presenting monthly results. Ask about revenue vs plan, the biggest cost variance and the full-year outlook."),
   ("fp_budget", "Làm ngân sách với trưởng phòng", "You are a foreign department head preparing next year's budget with me. Ask for 20% more budget and defend it when I ask about assumptions."),
   ("fp_forecast", "Giải thích thay đổi dự báo", "You are the regional finance director. Our full-year forecast dropped by 5%. Ask me why and what actions we are taking."),
   ("fp_capex", "Duyệt khoản đầu tư", "You are the foreign general manager. I present a request for a new machine costing 3 billion dong. Ask about payback, risks and alternatives."),
  ],
  "dialogues": [
   ("How did we do against plan this month?", [
     ("Revenue was 4% above plan, but profit was 2% below because of a one-off repair cost.", True, "So với kế hoạch cả doanh thu và lợi nhuận + nguyên nhân."),
     ("We did good, very good.", False, "Không có số; 'good' nên là 'well'."),
     ("Plan is plan, actual is actual.", False, "Không phân tích gì.")]),
   ("Why do you think we'll miss the full-year target?", [
     ("Two big orders moved to next year. At the current run rate, we'll reach about 95% of target.", True, "Nguyên nhân + ước lượng bằng run rate."),
     ("Because economy is bad.", False, "Chung chung, thiếu mạo từ ('the economy')."),
     ("I feel it.", False, "Dự báo phải dựa trên số liệu, không phải cảm giác.")]),
   ("I need 20% more budget next year.", [
     ("Could you share the main assumptions? For example, headcount and expected sales from the new product.", True, "Hỏi giả định cụ thể trước khi đánh giá."),
     ("20% is too much, no.", False, "Từ chối khi chưa xem căn cứ."),
     ("OK, I add for you.", False, "Đồng ý ngay, bỏ qua vai trò kiểm soát của FP&A.")]),
   ("What's the payback period for this machine?", [
     ("About three years. It saves around 1 billion dong a year in labour and scrap costs.", True, "Thời gian hoàn vốn + căn cứ tiết kiệm."),
     ("Payback is fast.", False, "Không có con số."),
     ("Three year.", False, "Thiếu 's' ('three years') và không nói căn cứ.")]),
   ("What are the main risks in this forecast?", [
     ("The biggest risk is the exchange rate. If the dollar rises 3%, our import costs go up by about 2 billion dong.", True, "Rủi ro chính + phân tích độ nhạy bằng số."),
     ("No risk, forecast is safe.", False, "Không thực tế — mọi dự báo đều có rủi ro."),
     ("Many risk, I cannot say.", False, "Sai số nhiều và né câu hỏi.")]),
   ("Can you send me the breakdown by region?", [
     ("Sure. I'll send it by noon tomorrow, with a short comment on each region.", True, "Đồng ý + hạn gửi + giá trị thêm."),
     ("Yes, I send.", False, "Thiếu 'will', thiếu tân ngữ và thời hạn."),
     ("Breakdown is in the big file, you find.", False, "Đẩy việc cho sếp.")]),
  ]},
}

# ───────────────────────── Gói ─────────────────────────
PACK = {
 "id": "finance",
 "label": "Tài chính · Kế toán",
 "short": "Kế toán",
 "emoji": "💰",
 "desc": "Kế toán · ngân hàng · kiểm toán",
 "persona": "a Vietnamese accounting and finance worker",
 "counterpart": "a foreign manager, auditor or client",
 "context": "accounting and finance",
 "core": [3, 11],
 "report": {
  "title": "Báo cáo tài chính 60 giây", "short": "Báo cáo số liệu", "sub": "Nói như họp cuối tháng 🎙️",
  "steps": [["Numbers", "Revenue this month was … , … % above/below plan."], ["Variance", "Costs were … % over budget, mainly because …"], ["Actions", "Next month, we will …"]],
  "kind": "monthly finance update",
  "structure": "key numbers / variances and reasons / actions",
  "sample": "Revenue in March was 42 billion dong, 5% above plan, and gross margin was 32%. Operating costs were 3% over budget, mainly because of a one-off repair and higher freight costs. Next month, we will review the freight contracts and send a detailed cost breakdown to each department.",
 },
 "podcast": "Podcast kế toán",
 "game_tag": "Game anime: đánh quái số lệch, hạ boss kiểm toán",
 "reverse_tag": "kiểu kế toán",
 "jd_placeholder": "VD: Kế toán công nợ ở công ty Nhật tại Bình Dương, đối chiếu công nợ, khoá sổ tháng, làm việc với kiểm toán…",
 "rw_placeholder": "VD: sếp hỏi vì sao chi phí tháng này vượt ngân sách 8%",
 "quips": [
  "Debits equal credits!",
  "Books closed!",
  "Reconciled to the last dong!",
  "Where's the receipt?",
  "Invoice approved!",
  "Payment run done!",
  "The numbers never lie…",
  "Audit season again?",
  "Variance explained!",
  "Cash is king!",
 ],
 "ai": [
  ("invoice", "Hoá đơn sai với nhà cung cấp", "You are a foreign supplier. I am in accounts payable. I tell you your invoice doesn't match the PO. Ask what is wrong and when you will be paid after you reissue it."),
  ("collect", "Nhắc khách thanh toán", "You are the finance manager of a foreign customer with two overdue invoices. I call to remind you. Say you are waiting for approval and try to delay payment."),
  ("expense", "Giải thích đề nghị thanh toán", "You are a foreign colleague whose expense claim was rejected because of missing receipts and a taxi cost over the limit. Ask me to explain and ask for flexibility."),
  ("close", "Báo tiến độ khoá sổ", "You are my foreign finance manager. Ask me about month-end closing: open reconciliations, accruals and when the trial balance will be ready."),
  ("audit", "Làm việc với kiểm toán", "You are an external auditor. Ask me for supporting documents for five large payments and ask one difficult question about who approves payments."),
  ("bank", "Khách đến quầy ngân hàng", "You are a foreign customer at a bank counter. You want to send money abroad and ask about the fee, exchange rate and timing. Ask one question about a suspicious call you received."),
  ("variance", "Giải thích chênh lệch với sếp", "You are my foreign CFO. Ask me why costs are 6% over budget this month. Ask whether it is a one-off and what we will do."),
  ("budget", "Thương lượng ngân sách", "You are a foreign department head. Ask me, the finance analyst, for a bigger budget for next year. Defend your request when I ask about assumptions."),
 ],
 "rev": [
  ("Hoá đơn này đã quá hạn 30 ngày.", "This invoice is 30 days overdue."),
  ("Hoá đơn không khớp với PO.", "The invoice doesn't match the PO."),
  ("Tuần này mình khoá sổ tháng Năm.", "We're closing the books for May this week."),
  ("Anh/chị đính kèm hoá đơn gốc giúp nhé.", "Please attach the original receipts."),
  ("Chi phí vượt ngân sách 5%.", "Costs are 5% over budget."),
  ("Doanh thu cao hơn kế hoạch 3%.", "Revenue was 3% above plan."),
  ("Đây là khoản phát sinh một lần.", "This is a one-off cost."),
  ("Giá này chưa bao gồm VAT.", "This price doesn't include VAT."),
  ("Tôi sẽ gửi bảng chi tiết sau cuộc họp.", "I'll send the breakdown after the meeting."),
  ("Tiền sẽ đến trong hai ngày làm việc.", "The money will arrive in two working days."),
  ("Ngân hàng không bao giờ hỏi mã OTP.", "The bank never asks for your OTP."),
  ("Kiểm toán cần chứng từ của mười khoản chi.", "The auditors need documents for ten payments."),
  ("Đã đối chiếu ngân hàng xong.", "The bank reconciliation is done."),
  ("Mình cần trích trước chi phí tiền điện.", "We need to accrue the electricity cost."),
 ],
 "reading": [
  {"t": "Payment reminder", "text": "Subject: Friendly reminder – Invoice INV-2045\nDear Mr Lee,\nOur records show that invoice INV-2045 for 86,000,000 VND was due on 15 May and is still outstanding. If you have already paid, please send us the proof of payment. Otherwise, please let us know when we can expect payment.\nKind regards,\nThu Ha – Accounts Receivable", "q": [
    {"q": "What should Mr Lee do if he has already paid?", "o": ["Call Thu Ha", "Send the proof of payment", "Pay again"], "a": 1},
    {"q": "Which team does Thu Ha work in?", "o": ["Accounts Receivable", "Accounts Payable", "Audit"], "a": 0}]},
  {"t": "Month-end closing schedule", "text": "MAY CLOSING SCHEDULE\nDay 1 (3 June): all invoices and expense claims submitted\nDay 2 (4 June): accruals and bank reconciliations\nDay 3 (5 June): trial balance to Finance Manager\nDay 5 (7 June): management report to CFO\nDocuments received after Day 1 will be posted in June.", "q": [
    {"q": "When is the trial balance due?", "o": ["3 June", "5 June", "7 June"], "a": 1},
    {"q": "What happens to late documents?", "o": ["They are rejected", "They go into June", "The CFO approves them"], "a": 1}]},
  {"t": "Expense policy", "text": "TRAVEL EXPENSE POLICY (summary)\n- Per diem abroad: USD 50/day (meals and local transport)\n- Hotels: up to USD 120/night, paid by the company\n- Taxis after 22:00 are allowed with receipts\n- Claims must be submitted within 30 days of return\n- Cash advances must be settled within 7 days of return", "q": [
    {"q": "How long do you have to settle a cash advance?", "o": ["7 days", "30 days", "50 days"], "a": 0},
    {"q": "What does the per diem cover?", "o": ["Hotels", "Meals and local transport", "Flights"], "a": 1}]},
  {"t": "Audit request", "text": "Dear Ms Nguyen,\nAs part of our year-end audit, please provide the following by Wednesday 15 January:\n1. Contracts for the 12 sales in the attached list\n2. Bank statements for December\n3. Approval emails for payments over 500 million VND\nPlease contact me if any document is not available.\nBest regards,\nDaniel Park, Audit Senior", "q": [
    {"q": "Which bank statements does Daniel need?", "o": ["November", "December", "The whole year"], "a": 1},
    {"q": "Which payments need approval emails?", "o": ["All payments", "Payments over 500 million VND", "Payments to foreign suppliers"], "a": 1}]},
  {"t": "Bank security notice", "text": "SECURITY NOTICE\nOur bank will NEVER ask for your password or OTP by phone, SMS or email. If someone asks for them, do not share them. Call our 24/7 hotline immediately and we will lock your card. Always check the sender before clicking any link.", "q": [
    {"q": "What will the bank never ask for?", "o": ["Your address", "Your OTP", "Your ID card at the counter"], "a": 1},
    {"q": "What should you do if someone asks for your OTP?", "o": ["Share it quickly", "Call the bank's hotline", "Click the link"], "a": 1}]},
 ],
 "events": [
  ("audit", "Kiểm toán cuối năm", "You are an external auditor starting the year-end audit. Ask me about our revenue recognition, large payments, stock count and any changes this year."),
  ("review", "Họp kết quả quý với CFO", "You are the foreign CFO at the quarterly review. Ask me about revenue, margin, the biggest variances and our full-year forecast."),
  ("budgeting", "Mùa làm ngân sách", "You are my foreign finance director. We are preparing next year's budget. Ask about my assumptions, headcount and capex plans."),
  ("tax", "Cơ quan thuế kiểm tra", "You are a foreign general manager. The tax authority will review our records next week. Ask me what will happen and how we are preparing."),
  ("system", "Chuyển sang phần mềm kế toán mới", "You are a foreign project manager for our new accounting system. Ask me about our current process, month-end closing and what I need from the new system."),
  ("interview", "Phỏng vấn vị trí kế toán", "You are a hiring manager at a foreign company. Interview me for an accountant position. Ask about month-end closing, reconciliations and a mistake I found and fixed."),
  ("other", "Khác", ""),
 ],
 "roles": ROLES,
 "phases": PHASES,
}
