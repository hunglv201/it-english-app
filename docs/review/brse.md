# Rà soát nội dung `ja/brse.js` (2026-09-23)

Người soát là biên tập viên độc lập, không phải người viết. Đã đọc hết **80/80 câu** (10 nhóm × 8) và 8 mẹo `JA_BRSE_TIPS`. Với mỗi câu đã soát đủ các trường: ja, ruby, kana, romaji, en, vi, when, level.
Cấu trúc, id nhóm và thứ tự giữ nguyên.

**Kiểm tra máy** (node, `new Function('window', src)(w)`):
- 10 nhóm × 8 câu. Đủ 8 trường. `level` chỉ có 尊敬語/謙譲語/丁寧語.
- Bỏ `<rt>…</rt>` và thẻ khỏi ruby thì ra đúng `ja` ở cả 80/80 câu.
- `<ruby>` chỉ bọc kanji, không có kanji nào thiếu furigana.
- Ghép cách đọc từ ruby (QA → キューエー, A → エー) thì khớp `kana` ở 80/80 câu.
- Chuyển kana sang romaji rồi so với trường romaji: 80/80 câu khớp. Chỉ khác ở những chỗ đúng quy ước: は đọc wa, を đọc o, trường âm viết ā/ū/ō, còn お+お trong お送り viết `ookuri` vì là ranh giới từ.

**Kính ngữ:** người công ty mình không kèm さん (田中, 佐藤); dùng 弊社/御社 đúng chỗ; không có kính ngữ kép sai (không có kiểu お～になられる, おっしゃられる).

## Danh sách sửa (7)

| Mục | Trước → Sau | Lý do |
|---|---|---|
| wabi #2 (ja/ruby/kana/romaji) | こちらは弊社の確認不足によるものです → 今回の件は弊社の確認不足によるものです | こちらは dùng để chỉ một sự việc thì gượng. 今回の件は là cách người Nhật hay nói khi xin lỗi |
| mail #1 level | 丁寧語 → 尊敬語 | ご返信 là hành động của khách, ở đây ご là kính ngữ tôn kính. Cách xếp này thống nhất với ご希望 (plan #7) |
| sou #5 vi | lùi hạn giao hàng → lùi hạn bàn giao (納期) | Dự án phần mềm dùng từ "bàn giao", không dùng "giao hàng" |
| plan #7 vi | thời hạn giao hàng → thời hạn bàn giao | Như trên |
| wabi #1 vi | việc giao hàng bị chậm → việc bàn giao bị chậm | Như trên |
| wabi #3 vi | chúng tôi sẽ giao → chúng tôi sẽ bàn giao | Như trên |
| plan #2 vi | Trước ngày mai tôi sẽ gửi… → Chậm nhất trong ngày mai tôi sẽ gửi… | 明日までに nghĩa là "hạn là ngày mai". Viết "trước ngày mai" dễ bị hiểu thành "trong hôm nay" |

## Điều còn lo (không sửa)

- **sou #1** ご相談させていただきたい và **plan #5** お見積もりをさせていただいても: một số sách coi ご～させていただく là 過剰敬語. Tuy vậy, trong công việc thực tế cách nói này rất phổ biến và được chấp nhận, nên giữ. Nếu muốn gọn hơn có thể viết ご相談したいことがあるのですが.
- **mtg #2** 届いておりますでしょうか, **uat #5** お願いできますでしょうか, **mail #5** いただけますでしょうか: dạng ～ますでしょうか bị một số người coi là thừa, nhưng rất thông dụng trong họp và email với khách, nên giữ.
- Cách xếp `level` cho các câu ～しております (dùng おります với vật/sự việc) chưa thống nhất hẳn. Câu có chủ thể là việc của mình ghi 謙譲語 (完了しております, 算出しております). Câu có chủ thể là hệ thống hay hiện tượng ghi 丁寧語 (発生しております, 稼働しております). Cả hai cách đều có lý, nên giữ nguyên.
- Tên riêng trong romaji viết thường (tanaka, satō, guen) cho thống nhất với `ja/keigo.js`.
- Phần `when` có nhắc tên công cụ thật (Backlog, Redmine, Slack, Teams, Chatwork). Đây chỉ là ví dụ về kênh liên lạc, không quảng cáo, nên giữ.
- Chưa có người Nhật bản ngữ đọc duyệt. Nên nhờ một BrSE/PM người Nhật xem lại 10–15 câu trang trọng nhất (nhóm wabi, uat).
