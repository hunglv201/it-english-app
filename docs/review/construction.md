# Rà soát nội dung gói `construction` (2026-09-23)

Đã rà từng dòng của `packs_src/construction.py`: từ vựng, IPA, từ loại, nghĩa tiếng Việt, thuật ngữ Nhật, câu mẫu, hội thoại, bài nghe, vai, bài đọc, dịch ngược, sự kiện, prompt AI và câu mẫu báo cáo. Cấu trúc và số lượng giữ nguyên. `python3 packs_src/build.py construction` chạy qua.

Gói viết khá chắc: đáp án hội thoại/bài đọc đều đúng, nội dung an toàn (cắt – khóa – đo điện, không đứng dưới hàng cẩu, không thêm nước vào bê tông, không di chuyển người nghi chấn thương lưng, không tự đục dầm, điểm dừng nghiệm thu) đều đúng hướng. Không có tên công ty thật.

## Số chỗ đã sửa

| Nhóm | Số chỗ |
|---|---|
| Tiếng Anh (ngữ pháp, độ tự nhiên) | 3 |
| An toàn / số liệu (con số là ví dụ, không phải quy định; sơ cứu) | 4 |
| IPA | 1 |
| Tiếng Việt (nghĩa, độ tự nhiên) | 4 |
| Tiếng Nhật | 1 |
| Bài nghe (ô trống) | 2 |
| Hội thoại (nhận xét) | 1 |
| **Tổng** | **16** |

Không thấy lỗi ở: đáp án bài đọc, số ô trống, từ vựng trùng, các cặp tiếng Nhật còn lại (ヘルメット, 安全靴, TBM ツールボックスミーティング, 危険源, ヒヤリハット, 整理整頓, 足場, フルハーネス, 墜落, 吊り荷, 玉掛け, 合図者, 進捗, 工程, 協力会社, 元請け, 職長, 挽回, 日報, 図面, 施工図, 質疑書, 仕様書, 寸法, 干渉, 設計変更, 通り芯, 搬入, 納品書, 資材置き場, 打設, 型枠, 鉄筋, 養生, スランプ試験, かぶり厚さ, 柱, 梁, 不適合報告書, 手直し, 立ち会う, 設備, 配線, 配管, スリーブ, 耐圧試験, 分電盤, 試運転調整, 漏水, 熱中症, 粉じん, 騒音, 苦情, 引き渡し, 竣工図, 竣工検査, 竣工, 不具合).

## Danh sách thay đổi

| # | Nhóm | Trước | Sau | Lý do |
|---|---|---|---|---|
| 1 | An toàn/số liệu | harness: "Above two metres, wear a harness…" | "On this site, wear a harness above two metres…" (+ VN "Ở công trường này…") | Mốc 2 m trình bày như quy định của công trường, không như luật chung |
| 2 | An toàn/số liệu | fall: "Falls from height are the main cause of death…" | "…one of the main causes of death…" | Tránh khẳng định thống kê tuyệt đối |
| 3 | An toàn/số liệu | Sốc nhiệt, câu đúng: "…If he gets worse, we'll call an ambulance." | "…Someone will stay with him, and if he doesn't feel better soon or gets confused, we'll call an ambulance." + nhận xét | Câu cũ để chờ "nặng hơn" mới gọi cấp cứu; lơ mơ là dấu hiệu say nắng nặng, phải gọi ngay, và không để nạn nhân một mình |
| 4 | An toàn/số liệu | Vệ sinh lọc điều hòa: "Every month." | "About once a month, or more often in a dusty area." + nhận xét nêu lịch theo tài liệu O&M | Con số là mức thường gặp, không phải quy định |
| 5 | Tiếng Anh | Bài nghe: "Nobody can work near the edge." | "Please do not work near the edge." | "can" nghe như "không ai làm được"; câu mới là lệnh cấm rõ ràng |
| 6 | Tiếng Anh | "Please wash the truck wheels before they leave the site." | "Please wash the wheels of every truck before it leaves the site." (+ VN "bánh xe tải") | "they" chỉ nhầm sang bánh xe |
| 7 | Tiếng Anh | Prompt AI: "You are a supplier's sales staff." | "You are a salesperson at a steel supplier." | "staff" là danh từ tập hợp, không dùng cho một người |
| 8 | IPA | as-built drawing /ˌæz bɪlt ˈdrɔːɪŋ/ | /ˌæz ˌbɪlt ˈdrɔːɪŋ/ | Thiếu dấu nhấn phụ (Cambridge: as-built /ˌæzˈbɪlt/) |
| 9 | Tiếng Việt | "Mười bao xi măng bị ướt. Tụi tôi không nhận được." | "…Bên tôi không nhận mấy bao này." | "không nhận được" dễ hiểu thành "chưa nhận được hàng" |
| 10 | Tiếng Việt | comply: "không đạt theo chỉ dẫn kỹ thuật" | "không đáp ứng chỉ dẫn kỹ thuật" | Tự nhiên hơn, khớp nghĩa "comply" |
| 11 | Tiếng Việt | "Việc này không làm đúng biện pháp thi công đã duyệt." | "Việc này làm không đúng…" | Sai trật tự từ |
| 12 | Tiếng Việt | typhoon: "bão (bão lớn)" | "bão lớn (bão nhiệt đới)" | Câu cũ lặp nghĩa |
| 13 | Tiếng Nhật | method statement → 施工計画書 (sekō keikakusho) | 施工要領書 (sekō yōryōsho) | 施工計画書 là kế hoạch thi công tổng thể; biện pháp cho một công việc cụ thể là 施工要領書 |
| 14 | Bài nghe | "Check the formwork before the pour" ô trống Check/formwork | formwork/pour | "Check" ít giá trị; "pour" là thuật ngữ cần nghe |
| 15 | Bài nghe | Đoạn nghiệm thu đạt: ô trống "hard" (hard work) | "manuals" | "hard" là từ chung chung; "manuals" là nội dung bàn giao |
| 16 | Hội thoại | Nhận xét "Because crane stop." | Thêm lỗi sai thì ("I stopped it") | Nhận xét cũ chưa nêu lỗi thì |

## Còn nghi ngờ (chưa sửa)

- Lớp bê tông bảo vệ: từ vựng/hội thoại dùng 25 mm, bài đọc email QA dùng 40 mm cho cột tầng 6. Không sai (khác cấu kiện, là spec giả định của dự án), nhưng người học có thể thấy lệch. Nếu muốn thống nhất thì đổi hội thoại chặng 6 thành "…The spec says 40." cho khớp cột.
- 7 ngày đạt "68% cường độ thiết kế là bình thường": đúng với xi măng thông thường (khoảng 65–70%), nhưng tùy cấp phối. Nhận xét đã ghi "thường", giữ nguyên.
- "signalman" (người xi nhan): Anh-Anh hay dùng "banksman"/"signaller". Giữ vì dễ hiểu và phổ biến ở dự án châu Á.
- 手すり cho guardrail: đúng ở giàn giáo/mép sàn, dù văn bản an toàn Nhật hay viết 手すり/墜落防止手すり. Giữ.
- 耐圧試験 cho thử áp đường ống nước: công trường Nhật cũng hay nói 水圧試験. Cả hai đều dùng, giữ.
- Nên nhờ một kỹ sư xây dựng đang làm với tổng thầu Nhật/Hàn đọc lại chặng MEP và QA/QC.
