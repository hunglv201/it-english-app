# Kiểm duyệt `packs_src/extra/aviation.py` (v4.1, 2026-09-23)

Đã soát **305 mục**: 8 chặng (80 từ, 79 câu mẫu, 40 hội thoại, 48 bài nghe), 16 câu dịch ngược, 5 bài đọc (10 câu hỏi), 4 tình huống AI, 3 sự kiện, 6 quips, 4 vai (8 tình huống + 16 hội thoại).
`python3 packs_src/build.py aviation` chạy qua.

Nhìn chung nội dung tốt: IPA đúng kiểu Anh-Anh và có dấu nhấn, đáp án bài đọc đều đúng, số liệu khớp nhau (620 kg thực / 700 kg tính cước, múi giờ Tokyo +2 giờ so với Hà Nội, 7–14 ngày ≈ 2 tuần). Không có tên hãng hay mức phí thật. Hướng dẫn an toàn và sơ cứu đều đúng: cúi người về trước khi chảy máu cam, không đưa thuốc cá nhân, hỏi dị ứng trước, báo ngay khi có khói hoặc vết móp, dỡ hành lý của khách vắng mặt, không mở túi niêm phong. Không có liều thuốc.

## Lỗi đã sửa (3)

| Loại | Trước → Sau |
|---|---|
| Bài nghe (ô trống là từ chức năng) | "Do you have any allergies" ô trống `["have","allergies"]` → `["allergies"]` |
| Thực tế nghề / rõ nghĩa | "We'll be 20 minutes late because of traffic." → "…because of air traffic." |
| Hội thoại (câu đúng tự mâu thuẫn) | "…there are only a few seats left at this price." → "…and the cheaper seats have sold out." |

## Tiếng Nhật đã bỏ
Không bỏ từ nào. Các thuật ngữ đều là từ ngành hàng không Nhật dùng thật (運賃, 発券, スポット, ロードシート, ダイバート, お手回り品…), romaji khớp.

## Còn đáng lo
- `purser` → チーフパーサー: ở hãng Nhật, "パーサー" và "チーフパーサー" là hai cấp khác nhau. Giữ chữ "chief" vì nghĩa tiếng Việt là "tiếp viên trưởng".
- `defibrillator` → "AED|ē ī dī": phần tiếng Nhật là chữ Latin, nên cần xem hàm furigana `romajiToHira`/`jaRuby` có hiện đúng không.
