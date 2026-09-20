# Rà soát nội dung gói `logistics` và `finance` (2026-09-20)

Đã đọc hết từng dòng của `packs_src/logistics.py` và `packs_src/finance.py`: từ vựng, IPA, từ loại, nghĩa tiếng Việt, thuật ngữ tiếng Nhật, câu mẫu, hội thoại, bài nghe, vai, prompt AI, câu dịch ngược, bài đọc, sự kiện và câu mẫu báo cáo.
Cấu trúc và số lượng mục giữ nguyên. `python3 packs_src/build.py logistics finance` chạy qua.

Nhìn chung cả hai gói đã tốt. IPA đều có dấu nhấn, từ viết tắt đọc từng chữ cái, đáp án bài đọc đều đúng, bài nghe có đủ ô trống, không thấy lỗi dấu tiếng Việt. Phần sửa chủ yếu là:
- các con số thuế, phí, thời hạn nói quá chắc chắn (thuế suất VAT/TNDN, "thuế nhập khẩu bằng 0", "hãng tàu chịu trách nhiệm"),
- một số thuật ngữ tiếng Nhật chưa đúng nghĩa kế toán, ngân hàng,
- vài câu tiếng Anh chưa tự nhiên.

## Số chỗ sửa theo loại

| Loại | logistics | finance |
|---|---|---|
| Tiếng Anh (ngữ pháp, độ tự nhiên) | 6 | 8 |
| Tiếng Việt (nghĩa, nhận xét) | 8 | 7 |
| Tiếng Nhật (thuật ngữ, romaji) | 1 | 5 |
| Thực tế nghề, thuế, bỏ số liệu rủi ro | 8 | 11 |
| Hội thoại (đáp án sai chưa đủ sai) | 0 | 1 |
| **Tổng** | **23** | **32** |

## Các thay đổi chính

| Gói | Mục | Trước | Sau | Lý do |
|---|---|---|---|---|
| logistics | Hội thoại thuế (chặng 2) | "…the import duty is zero. We'll only pay 10% VAT." | "…the import duty for this item is zero, but we still have to pay import VAT." | Thuế suất VAT có thể thay đổi (từng có giai đoạn giảm còn 8%), nên bỏ con số cụ thể |
| logistics | import duty (ví dụ) | "With a valid C/O, the import duty is zero." | "…the import duty can be lower." | Có C/O chưa chắc thuế bằng 0, tuỳ mặt hàng và hiệp định |
| logistics | liable | "The carrier is liable for damage…" | "The carrier may be liable…" | Trách nhiệm của hãng tàu có giới hạn và nhiều trường hợp được miễn |
| logistics | survey report | "…within 30 days" | "…to process our claim" | Thời hạn nộp khác nhau theo từng hợp đồng bảo hiểm |
| logistics | Vai Chứng từ: C/O | "We can issue Form D. It usually takes three working days after the B/L date." | "We can apply for Form D, and I'll send you a copy as soon as it's issued." | Người xuất khẩu chỉ xin cấp C/O, cơ quan có thẩm quyền mới cấp. Thời gian cấp không cố định |
| logistics | Vai Chứng từ: telex release | "You can pick up the goods with a copy." | "Then you can get the goods without the original B/L." | Nói đúng bản chất của điện giao hàng |
| logistics | import permit | "Medical equipment needs an import permit." | "Some medical equipment needs…" | Không phải mọi thiết bị y tế đều cần giấy phép |
| logistics | Hội thoại kiểm hoá | "It's a random check…" | "It may be a random check…" | Nhân viên không biết chắc lý do hải quan chọn kiểm hoá |
| logistics | commercial invoice (JA) | インボイス "invoisu" | "inboisu" | Romaji Hepburn đúng của イン**ボ**イス |
| logistics | container (VN) | "container, công" | "container, cont" | Dân trong nghề nói "cont", không nói "công" |
| logistics | booking (ví dụ) | "…two containers next Friday" | "…two containers on next Friday's vessel" | Booking là đặt chỗ trên một chuyến tàu cụ thể |
| logistics | Bài nghe chặng 2 | "has cleared customs this morning" | "cleared customs this morning" | Đã có mốc thời gian cụ thể thì dùng quá khứ đơn |
| logistics | Nhận xét "combine is cheaper" | "Thiếu chủ ngữ phù hợp" | "Sai dạng từ… 'Combining them is cheaper.'" | Nói đúng loại lỗi (động từ không đứng làm chủ ngữ) |
| logistics | lead time (VN) | "thời gian từ lúc đặt đến lúc có hàng" | "thời gian chờ hàng (từ lúc đặt đến lúc có hàng)" | Tên gọi ngắn, quen dùng trong nghề |
| logistics | Câu mẫu vendor | "higher than other vendors" | "higher than other vendors' prices" | So sánh đúng: giá với giá |
| finance | corporate income tax | "The standard CIT rate is 20%." | "We pay corporate income tax on our taxable profit." | Bỏ thuế suất cụ thể vì dễ lỗi thời (luật thuế TNDN mới có nhiều mức) |
| finance | Hội thoại VAT | "Is your price including VAT? … With 10% VAT, the total is 11 million dong." | "Does your price include VAT? … VAT will be added on the invoice…" | Câu hỏi tự nhiên hơn. Bỏ mức 10% cố định |
| finance | VAT (ví dụ) | "Is this price including VAT?" | "Does this price include VAT?" | Tiếng Anh tự nhiên |
| finance | tax return | "We submit the VAT tax return every month." | "We must submit every tax return on time." | "VAT tax" bị lặp nghĩa. Công ty có thể khai theo quý, không phải lúc nào cũng theo tháng |
| finance | file / câu mẫu hạn nộp | "file the VAT return by the 20th" / "…due on the 20th." | "…before the deadline" / "When is the deadline for the VAT return?" | Bớt con số ngày cụ thể. Chỉ giữ một chỗ trong hội thoại, có kèm "for monthly filing… usually" |
| finance | prepayment | 前払金 "maebaraikin", VN "khoản trả trước" | 前払費用 "maebarai hiyō", VN "chi phí trả trước" | Bảo hiểm trả trước là chi phí trả trước. 前払金 là tiền ứng trước cho nhà cung cấp |
| finance | allocate (JA) | 配分する | 配賦する (haifu suru) | Thuật ngữ kế toán Nhật cho phân bổ chi phí về bộ phận |
| finance | wire transfer (JA) | 振込 "furikomi" | 電信送金 "denshin sōkin" | 振込 là chuyển khoản trong nước. Chuyển tiền quốc tế bằng điện là 電信送金 |
| finance | deposit (JA) | 預金 (danh từ) | 入金する "nyūkin suru" | Câu ví dụ dùng động từ "deposit" |
| finance | personal income tax (JA) | 所得税 | 個人所得税 "kojin shotokuzei" | Phân biệt rõ với thuế TNDN |
| finance | Mở tài khoản cho người nước ngoài (2 chỗ) | "visa or work permit" | "visa or temporary residence card" | Giấy phép lao động không phải giấy tờ tuỳ thân. Ngân hàng yêu cầu thị thực hoặc thẻ tạm trú |
| finance | Vai Ngân hàng: đáp án sai | "Yes, you can send." (câu đúng, chỉ thiếu ý) | "Yes, you can sending." | Đáp án sai phải sai rõ ràng |
| finance | Tỷ giá | "Our buying rate is on the screen." | "Today's rates are on the screen… in dong" | Khách chuyển USD ra nước ngoài thì ngân hàng bán ngoại tệ, không phải mua |
| finance | Tất toán sớm | "non-term interest rate" | "demand deposit rate" | "non-term" là tiếng Anh kiểu Việt. Thuật ngữ đúng là *demand deposit* (không kỳ hạn) |
| finance | Vai Kế toán: hoá đơn gốc | "Our tax rules require original invoices…" | "We need a valid invoice or receipt… may not be deductible" | Hiện nay dùng hoá đơn điện tử, không còn "hoá đơn gốc" giấy. Tránh nói quá tuyệt đối |
| finance | Vai Kiểm toán | "There's no loss" | "We didn't find any loss" | Kiểm toán viên chỉ nói điều mình đã kiểm tra |
| finance | Nhận xét cut-off | "doanh thu ghi nhận khi giao hàng" | "…thường ghi nhận khi giao hàng (chuyển giao quyền kiểm soát)" | Đúng nguyên tắc, không tuyệt đối hoá |
| finance | Bài đọc thư nhắc nợ | "please ignore this email and send us the proof of payment" | "please send us the proof of payment" | Câu gốc mâu thuẫn ("bỏ qua" rồi lại "gửi") |
| finance | withholding tax (dịch VN) | "…cho nhà thầu nước ngoài này mình phải nộp thuế nhà thầu" | "…cho nhà cung cấp nước ngoài, mình phải khấu trừ và nộp thuế nhà thầu" | Dịch sát câu tiếng Anh và đúng bản chất khấu trừ |
| finance | Bài nghe (3 câu) | "one hundred billion", "ten million", "one hundred million" | thêm "dong" | Số tiền phải có đơn vị |
| finance | favourable (dịch VN) | "Chi phí nhân sự thấp hơn kế hoạch 1 tỷ đồng." | "…có chênh lệch có lợi 1 tỷ đồng (thấp hơn kế hoạch)" | Dịch sát nghĩa "favourable variance" |
| finance | proof of payment (VN) | "uỷ nhiệm chi" | "chứng từ chuyển khoản (uỷ nhiệm chi)"; "uỷ nhiệm chi có xác nhận của ngân hàng" | Chứng từ thanh toán là bản đã có xác nhận của ngân hàng |

## Giữ nguyên có cân nhắc
- Incoterms (FOB, CIF, EXW, DAP): trách nhiệm, thời điểm chuyển rủi ro và việc bảo hiểm CIF do người bán mua đều đúng theo Incoterms 2020.
- Hạn nộp tờ khai VAT theo tháng là "ngày 20 tháng sau": vẫn đúng theo Luật Quản lý thuế hiện hành. Chỉ giữ ở một hội thoại (có "for monthly filing… usually") và một đoạn nghe.
- Các mức phí, lãi suất ở phần ngân hàng (0,2%, 5%/năm) và cước tàu là số liệu của công ty hoặc ngân hàng tự đặt trong ví dụ, không phải quy định. Giữ lại.
