# Kiểm duyệt `phases_extra2.py` — 8 chặng IT làm giàu (v4.1, 2026-09-23)

Đã soát **232 mục**: 80 từ, 64 câu mẫu, 40 hội thoại, 48 bài nghe.
`python3 gen_data.py` chạy qua: days 450.

Nội dung đúng thực tế làm offshore với khách Nhật: 基本設計/詳細設計, QA表, 人月, 工数, 再発防止策, postmortem không đổ lỗi, không dán dữ liệu mật vào AI công khai. Hội thoại có 1 câu đúng rõ ràng, 2 câu sai là lỗi người Việt hay mắc, nhận xét đúng lỗi. Múi giờ nhất quán: 8 giờ sáng ở Việt Nam là 10 giờ ở Tokyo. Các ô trống bài nghe chỉ dính "." hoặc "," ở cuối từ. Từ vựng không trùng với 370 từ IT cũ.

## Lỗi đã sửa (4)

| Loại | Trước → Sau |
|---|---|
| Nghĩa tiếng Việt | offshore: "ở nước ngoài (đội làm thuê từ xa)" → "(đội) gia công phần mềm ở nước ngoài cho khách" |
| Tiếng Anh tự nhiên (bài nghe) | "Let us test the prototype with five users" → "Let's test the prototype with five users" |
| Dấu câu (bài nghe) | "The fix is on staging so please retest it" → "The fix is on staging, so please retest it" |
| Dấu câu (bài nghe) | "That method does not exist so it is a hallucination" → "That method does not exist, so it is a hallucination" |

## Tiếng Nhật đã bỏ
Không bỏ từ nào.

## Còn đáng lo
- Có nhắc tên công nghệ "Oracle" (3 chỗ). Gói IT cũ cũng đã dùng Docker, GitHub, Slack, Figma nên vẫn giữ. Nếu muốn áp chặt quy tắc "không thương hiệu thật" thì đổi thành "old database".
- Vài từ ghép tiếng Nhật dùng dạng danh từ cho động từ (recover → 復旧, generate → 生成, fine-tune → ファインチューニング). Cách này giống `ja_data.py` cũ (approve → 承認).
