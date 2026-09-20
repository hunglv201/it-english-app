# packs_src — nguồn các gói ngành (v3.0)

`python3 packs_src/build.py [id…]` → `packs/<id>.gen.js` (+ bản sao `game/packs/`). Script kiểm tra chặt, sai là dừng.
Gói **IT** không ở đây (vẫn là `data.gen.js` + `phrases.gen.js` + `roles.gen.js`).

## Schema một file `packs_src/<id>.py`

```python
PACK = {
 "id": "hotel",                        # trùng tên file
 "label": "Khách sạn · Du lịch",       # tên gói (tiếng Việt)
 "short": "Khách sạn",                 # tên ngắn (≤ 12 ký tự) cho chip/header
 "emoji": "🏨",
 "desc": "Lễ tân · nhà hàng · buồng phòng · tour",   # 1 dòng mô tả ở màn chọn ngành
 "persona": "a Vietnamese hotel and tourism worker",  # dùng trong prompt AI: "for <persona>"
 "counterpart": "a foreign hotel guest",              # người AI hay đóng vai nhất
 "context": "hotel and tourism",                      # "<context> workplace English"
 "core": [11, 10],                     # chặng lấy từ gói office (xem danh sách chặng office bên dưới)
 "report": {                           # màn "báo cáo nhanh 60 giây" (IT = Standup 60 giây)
   "title": "Giao ca 60 giây", "short": "Giao ca 60s", "sub": "Nói như lúc giao ca 🎙️",
   "steps": [["In my shift", "Two guests checked in …"], ["Pending", "Room 305 is waiting for …"], ["Notes", "Please call … / No issues."]],
   "kind": "shift handover report",                    # tiếng Anh, đưa vào prompt chấm
   "structure": "what happened / what is pending / notes for the next shift",
   "sample": "In my shift, ten guests checked in and two checked out. Room 305 is waiting for an extra bed. Please call the guest in room 210 at 8 a.m."},
 "podcast": "Podcast khách sạn",       # tên mục nghe thụ động
 "game_tag": "Game anime: đánh quái, hạ boss khách khó tính",
 "reverse_tag": "kiểu khách sạn",      # nhãn nhỏ cạnh câu dịch ngược riêng của ngành
 "jd_placeholder": "VD: Lễ tân khách sạn 4 sao ở Đà Nẵng, khách Hàn/Úc, check-in, đặt tour, xử lý phàn nàn…",
 "rw_placeholder": "VD: phòng 305 chưa dọn xong, khách chờ 30 phút",
 "quips": ["Checking in a guest…", …8–12 câu tiếng Anh ngắn, vui, đúng ngành — linh vật Mochi nói trong game],
 "ai": [ # 6–8 tình huống Giao tiếp AI: (key, nhãn VN ngắn, prompt EN: AI là ai + tình huống + nên hỏi gì)
   ("checkin", "Nhận phòng", "You are a foreign guest checking in at the hotel front desk. I am the receptionist. Give your name, ask about breakfast and Wi-Fi."), …],
 "rev": [ # ≥ 12 câu Việt → Anh (dịch ngược), câu nói thường ngày của nghề, ≤ 12 từ tiếng Anh
   ("Phòng của anh ở tầng năm.", "Your room is on the fifth floor."), …],
 "reading": [ # ≥ 5 bài đọc hiểu 30 giây: văn bản THẬT của nghề (email, tin nhắn, thông báo, phiếu, menu…)
   {"t": "Booking email", "text": "Dear team,\nI'd like to book …", "q": [
      {"q": "When does the guest arrive?", "o": ["Friday", "Monday", "Sunday"], "a": 0},   # đúng 3 lựa chọn, a = chỉ số đúng
      {"q": "…", "o": [...], "a": 2}]}, …],
 "events": [ # ≥ 5 loại sự kiện sắp tới để luyện trước: (key, nhãn VN, prompt EN) — thêm ("other","Khác","") ở cuối
   ("vip", "Đón đoàn khách VIP", "You are the tour leader of a VIP group arriving tomorrow. Ask me about rooms, schedule and special requests."), …, ("other", "Khác", "")],
 "roles": { # 3–5 vai trong ngành
   "reception": {"label": "Lễ tân", "emoji": "🛎️",
     "scenarios": [(key, nhãn VN, prompt EN) × 4],
     "dialogues": [(câu người kia nói, [(câu đáp, True/False, nhận xét VN) × 3]) × 6]},
   …},
 "phases": [ # 10 chặng riêng của ngành (office: 12)
   {"title": "Lễ tân – nhận phòng",
    "vocab": [ # đúng 10 từ: (từ, "/IPA/", loại, nghĩa VN, ví dụ EN có <b>từ</b>, dịch VN[, "日本語", "romaji"])
      ("reservation", "/ˌrezərˈveɪʃn/", "n", "đặt phòng trước", "Do you have a <b>reservation</b>?", "Anh/chị có đặt phòng trước không?", "予約", "yoyaku"), …],
    "phrases": [(EN, VN) × 8–10],       # câu mẫu hay dùng
    "dialogues": [(câu người kia nói, [(câu đáp, True/False, nhận xét VN) × 3]) × 5],
    "listen": [ # đúng 6: 4 câu ngắn (1–2 ô trống) + 2 ĐOẠN 2–3 câu như tình huống thật (đúng 3 ô trống)
      ("Your room is on the fifth floor", ["room", "fifth"], "phòng ở tầng mấy"), …,
      ("Good evening. Your room is ready. Breakfast is from six to ten in the restaurant.", ["ready", "Breakfast", "restaurant"], "nhận phòng buổi tối")]},
   …]
}
```

### Chặng của gói `office` (các gói khác tham chiếu bằng chỉ số trong `core`)
0 Chào hỏi & làm quen · 1 Công việc hằng ngày & báo cáo · 2 Họp & trao đổi · 3 Email công việc · 4 Chat & tin nhắn công việc ·
5 Điện thoại & gọi video · 6 Nhờ giúp & hỏi lại cho rõ · 7 Kế hoạch, hạn chót & ưu tiên · 8 Sự cố, xin lỗi & giải quyết ·
9 Thuyết trình & số liệu · 10 Nghỉ phép & hành chính · 11 Phỏng vấn & phát triển sự nghiệp

### Quy tắc nội dung
- Người học: người Việt, tiếng Anh **A2–B1**; câu ngắn, tự nhiên, đúng như người bản xứ nói ở chỗ làm. Tiếng Việt **có dấu đầy đủ**, tự nhiên.
- Hội thoại chọn đáp: 1 câu đúng (tự nhiên, lịch sự, đủ ý) + 2 câu sai **kiểu lỗi người Việt hay mắc** (thiếu chủ ngữ/động từ, sai thì, dịch từng chữ, cộc lốc, không trả lời đúng câu hỏi). Nhận xét VN ngắn, chỉ rõ lỗi/cách sửa. Viết câu đúng ở **vị trí đầu** (build tự xáo).
- Bài nghe: từ trống là **từ nguyên vẹn có trong câu** (so khớp bỏ dấu câu, không phân biệt hoa thường); tránh ô trống là từ chức năng (the, a, is). Đoạn = 2–3 câu, ≥ 2 dấu câu kết thúc, đúng 3 ô trống.
- IPA kiểu Anh-Mỹ/Anh-Anh chuẩn từ điển (Cambridge/Oxford), có dấu nhấn ˈ.
- Không lặp từ vựng trong cùng gói. Không dùng tên thương hiệu thật.
- Tiếng Nhật (tuỳ chọn, phần tử 7–8 của từ): chỉ khi có thuật ngữ chuẩn dùng thật ở công ty Nhật; nếu không chắc thì bỏ (dùng tuple 6 phần tử).
