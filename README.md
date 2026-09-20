# Nói Nghề — Tiếng Anh đúng nghề của bạn

*(Tên cũ đến v2.0: IT English.)* Ứng dụng web giúp người Việt trình độ cơ bản luyện **tiếng Anh công việc theo ngành**:
🏢 Công sở chung (mặc định) · 💻 IT · 🏨 Khách sạn – Du lịch · 🎧 Bán hàng – CSKH · 🏭 Sản xuất – Nhà máy — hoặc tự tả nghề của bạn để AI tạo tình huống và từ vựng riêng. Chạy hoàn toàn trong trình duyệt, không cần server,
không cần tài khoản.

**Live demo:** https://hunglv201.github.io/it-english-app/
· 🎮 **Game:** https://hunglv201.github.io/it-english-app/game/
· 📖 **Trang giới thiệu (v3.0):** https://hunglv201.github.io/it-english-app/gioi-thieu.html · lưu trữ [v2.0](https://hunglv201.github.io/it-english-app/gioi-thieu-v2.html) · [v1](https://hunglv201.github.io/it-english-app/gioi-thieu-v1.html) · [lịch sử phiên bản](./CHANGELOG.md)

> Đang dùng Claude/Cowork để phát triển? Đọc [`CLAUDE.md`](./CLAUDE.md) — ngữ cảnh dự án, pipeline deploy, quy ước.

---

## Tính năng

- **Chọn ngành (v3.0)** — mở app lần đầu: ngành → vị trí → trình độ, bước nào cũng **bỏ qua được** (bỏ qua = *Công sở chung*). Đổi ngành bất cứ lúc nào bằng chip dưới tên app; tiến độ lộ trình giữ riêng từng ngành. Link `?track=hotel|sales|factory|office|it` mở sẵn một ngành.
- **Hôm nay** — bài học thích ứng mỗi ngày (4 việc ngắn, ~5 phút): ôn từ, nghe, trò chuyện AI, luyện câu. Có streak (chuỗi ngày) và thanh tiến độ.
- **Lộ trình theo ngành** — IT 370 ngày (185 hội thoại, 222 bài nghe); các ngành khác 12 chặng · 120 ngày (60 hội thoại, 72 bài nghe, 120 từ). Mỗi ngày gồm từ vựng, mẫu câu, hội thoại, bài nghe và phần luyện thêm với AI.
- **Từ vựng** — 3 chế độ: *thẻ lật* (phát âm + ví dụ), *kiểm tra* (trắc nghiệm 2 chiều Anh↔Việt), *danh sách* (tìm kiếm, lọc chủ đề). Ôn tập theo thuật toán **SRS (SM-2 rút gọn)**.
- **Câu thường dùng** — IT 1000 câu; các ngành khác ~720 câu (câu của ngành + ~610 câu công sở chung); lưu câu yêu thích để ôn lại.
- **Giao tiếp** — trò chuyện với AI theo tình huống của ngành bạn (nhận phòng, khách khiếu nại, báo máy hỏng, standup, code review…). AI đóng vai khách, đồng nghiệp, sếp hay chuyên gia, nói tiếng Anh đơn giản và **sửa lỗi** sau mỗi lượt. Có thể mô tả lĩnh vực của bạn để AI gợi ý tình huống riêng.
- **Nghe** — 2 chế độ: *chép chính tả* (điền từ trống) và *shadowing* (nhại lại, chấm phát âm qua mic theo %). Có 74 **đoạn họp dài 2–3 câu** (điền nhiều ô cùng lúc) giống cuộc họp thật.
- **Tự động chạy (autoplay)** — nút *Tự động* trong Từ vựng, Câu, Nghe: app tự đọc và tự chuyển sau số giây bạn đặt, học rảnh tay không cần bấm.
- **Cấu hình** — màn cài đặt (nút bánh răng ở header): chỉnh thời gian autoplay từng chức năng, bật/tắt tự đọc, chọn giao diện, và cấu hình AI.
- **Sáng / Tối / Theo hệ thống** — đổi ở header hoặc trong Cấu hình.

### Nhà cung cấp AI (khi chạy ngoài claude.ai)

Phần Giao tiếp hỗ trợ nhiều nhà cung cấp — vào **Giao tiếp → Cài đặt AI** (hoặc **Cấu hình**), chọn provider và dán API key của bạn (key lưu localStorage, chỉ trên máy bạn):

- **Google Gemini** — free tier, gọi thẳng từ trình duyệt.
- **Claude (Anthropic)** — chất lượng cao, tính phí theo dùng.
- **Groq** — free, nhanh (model Llama).

Khi mở app *bên trong* claude.ai thì tự dùng Claude sẵn có, không cần key.

### Học từ văn bản công việc (AI rút từ)

Vào **Từ vựng → ＋ Thêm từ công việc (AI)**: dán một đoạn tiếng Anh thật (tin nhắn Teams, mô tả PR, tài liệu) → AI rút thuật ngữ IT, tạo thẻ từ + câu ví dụ + nghĩa, và thêm vào chủ đề **“Của tôi”** để ôn cùng SRS.

### Tiến độ & Ôn từ hay sai

Nút **Tiến độ & thống kê** ở Hôm nay: streak, số từ đã thuộc, số ngày lộ trình, tổng lượt học, và danh sách **từ hay sai** (dựa trên điểm SRS) kèm nút *Ôn ngay*. Trong Từ vựng có thêm chủ đề **“Hay sai”** để dồn ôn những từ hay quên.

### Luyện nói theo công việc (v1.20–1.21)

- **Standup 60 giây** — ở Hôm nay: nói liền 3 ý (hôm qua · hôm nay · vướng gì), AI chấm 1–10, đưa bản chuẩn, chỉ lỗi và cho *Đọc lại* chấm %.
- **Dịch ngược** — cho câu tiếng Việt kiểu dev ("anh check giúp em cái PR này với"), bạn nói tiếng Anh, AI chấm theo *nghĩa* và gợi ý 2–3 cách nói tự nhiên.
- **Ôn câu (SRS)** — câu AI đã sửa cho bạn, câu dịch ngược/đọc theo điểm thấp tự vào hàng ôn cách quãng.
- **Chọn đáp theo vai trò** — 23 vai trong 5 ngành (Cài đặt › Ngành & vai trò), kèm tình huống AI riêng; game cũng dùng.
- **Cá nhân hoá bằng JD / tự tả công việc (mọi ngành)** — AI chọn ngành + vai, gợi ý chuyển gói hợp hơn, chặng nên ưu tiên, 3 tình huống luyện nói và 12 từ vựng riêng của nghề bạn.
- **Sự kiện sắp tới** — ghi sprint review/demo/phỏng vấn; trước 1 ngày app nhắc ở Hôm nay và mở tình huống luyện đúng chủ đề.
- **Podcast dev** — nghe thụ động ~5 phút (2 giọng hỏi–đáp, điều khiển từ màn khoá), cuối tập 3 câu kiểm tra.
- **Hỏi nhanh (nút ?)** — hỏi nghĩa/so sánh từ hoặc dán tin nhắn đồng nghiệp từ bất kỳ màn nào; lưu từ vào “Của tôi” một chạm.
- **AI phân tích phát âm** — sau khi đọc theo, AI chỉ từng từ sai + mẹo cho người Việt.
- **Thuật ngữ tiếng Nhật 🇯🇵** — bật trong Cài đặt › Học tập: 370 từ hiện thêm thuật ngữ Nhật + romaji (app & game).
- **Biểu đồ tiến bộ nói** + **ảnh chia sẻ PNG** thành tích (Thống kê, Tổng kết tuần, Tôi).

### Sao lưu tiến độ

**Tôi › Sao lưu tiến độ**: xuất một file `.json` gồm cả app và game, khôi phục trên máy khác (chọn file hoặc dán nội dung). Không có server nên nên sao lưu định kỳ.

### Luyện lại

Cuối mỗi phiên (Từ vựng, Câu, một Ngày trong lộ trình) đều có nút **↻ Luyện lại** (và *Luyện lại tự động* cho Từ vựng/Câu).

### Cài như app (PWA, offline)

Khi mở qua HTTPS (GitHub Pages), app có thể **cài ra màn hình chính** điện thoại/desktop và **chạy offline** (service worker cache app + dữ liệu). Trên điện thoại: mở site → menu trình duyệt → *Thêm vào màn hình chính*. Phần này tự tắt khi mở trong claude.ai.

---

## Công nghệ

Web tĩnh **một trang, không framework, không build tool** — chỉ HTML + CSS + JavaScript thuần (vanilla).

| Thành phần | Vai trò |
|---|---|
| `index.html` | Toàn bộ giao diện + logic (HTML, CSS trong `<style>`, JS trong `<script>`). |
| `data.gen.js` | Dữ liệu bài học 370 ngày. Sinh tự động từ `gen_data.py`. |
| `phrases.gen.js` | 1000 câu thường dùng. Sinh tự động từ `phrases_data.py`. |

**API trình duyệt dùng bên trong:**
- **Web Speech API** — `speechSynthesis` (đọc tiếng Anh), `SpeechRecognition` (chấm phát âm).
- **localStorage** — lưu tiến độ học (streak, SRS, câu đã lưu, việc hôm nay).
- **`window.claude.use('sample')`** — gọi Claude cho phần Trò chuyện AI (chỉ khi mở trong claude.ai).

**Font:** Bricolage Grotesque (tiêu đề) · Hanken Grotesk (nội dung) · IBM Plex Mono (thuật ngữ IT). Màu chủ đạo: trắng + xanh `#1b4dff`.

> Chi tiết kiến trúc, luồng dữ liệu và cách mở rộng: xem [`ARCHITECTURE.md`](./ARCHITECTURE.md).

---

## Chạy tại máy

Mở trực tiếp `index.html`, hoặc chạy một web server tĩnh (khuyến nghị):

```bash
python3 -m http.server 8000
# mở http://localhost:8000
```

> **Lưu ý:** một số trình duyệt chặn micro/loa khi mở bằng `file://`. Dùng `http://localhost`
> để phần Nghe / chấm phát âm hoạt động ổn định.

---

## Trò chuyện AI

Phần **Giao tiếp** (và Boss AI / Đấu thoại trong game) gọi AI theo thứ tự:

1. Mở **bên trong claude.ai** (Artifact) → dùng Claude sẵn có qua `window.claude.use('sample')`, không cần key.
2. Mở ngoài (GitHub Pages, localhost) → dùng **API key của bạn** (Gemini / Claude / Groq), gọi thẳng từ trình duyệt.
   Key lưu `localStorage`, dùng chung giữa app và game. Chưa có key thì app hiện hướng dẫn nhập.

> Key nằm phía client nên chỉ nên dùng key cá nhân (free tier). Kế hoạch sau: backend/proxy giữ key — xem `ARCHITECTURE.md`.

---

## 🎮 Nói Nghề Quest (game)

Bản game anime dùng **chung dữ liệu và AI key** với app, thiết kế **mobile-first** (vừa 1 màn iPhone SE, không cuộn):

- **Bản đồ** — mỗi ngày lộ trình là một màn: 3 con Bug (từ vựng · ngữ pháp · nghe) + 1 Boss (visual novel). Trả lời đúng gây sát thương + combo, sai mất HP.
- **AFK / Mochi tự cày** — vắng mặt vẫn tích xu & XP (tối đa 8h, nâng cấp được), có sân đánh animation và Mochi "nói" những câu bạn đã luyện.
- **Nói** — 5 chế độ luyện nói: Đấu thoại AI (AI chấm thành sát thương), Đọc theo nhịp (mic chấm từng từ), Chuyện văn phòng (VN 5 cảnh · 3 kết cục), Phản xạ 5 giây, Trang bị cho Mochi.
- **Hằng ngày / Shop / Huy hiệu / Hồ sơ** — rương ngày, nhiệm vụ, nâng cấp, vật phẩm, thống kê, cài AI key ngay trong game.

Game theo ngành bạn đang học (quái, câu Mochi nói, Boss AI). Mở từ app (Luyện tập → *Nói Nghề Quest*) hoặc trực tiếp `/game/`.

---

## 📖 Trang giới thiệu

`gioi-thieu.html` — landing page fullpage (mỗi lần cuộn = 1 trang), nền particle chạy theo con trỏ, chữ chạy, 33 ảnh chụp màn hình (`img/showcase/v3/`), mục "Mới trong v3.0" (lưới 5 ngành), menu chọn phiên bản ở đầu trang và **Lịch sử phiên bản**. Mỗi version lớn giữ lại trang cũ làm bản lưu trữ (`gioi-thieu-v2.html`, `gioi-thieu-v1.html`). Deploy cùng Pages.

---

## Sinh lại dữ liệu

Chỉ cần Python 3, không phụ thuộc thư viện ngoài:

```bash
python3 gen_data.py      # -> data.gen.js     (cần phases_extra.py cùng thư mục)
python3 phrases_data.py  # -> phrases.gen.js
python3 roles_data.py    # -> roles.gen.js      (gói nội dung 7 vai)
```

Mỗi script tự copy file `*.gen.js` sang `game/`. Thuật ngữ tiếng Nhật nằm ở `ja_data.py` (gen_data.py đọc vào trường `ja`).

Muốn thêm/sửa bài học thì sửa các file `*.py` rồi chạy lại — **không sửa tay** file `*.gen.js`.

---

## Cấu trúc thư mục

```
it-english-app/
├── index.html          # App (giao diện + logic)
├── data.gen.js         # Dữ liệu 370 ngày (sinh ra, không sửa tay)
├── phrases.gen.js      # 1000 câu (sinh ra, không sửa tay)
├── packs/              # v3.0: gói ngành office/hotel/sales/factory (sinh từ packs_src/build.py)
├── packs_src/          # nguồn gói ngành + build.py + README (schema)
├── gen_data.py         # Script sinh data.gen.js
├── phases_extra.py     # 27 chặng chủ đề mở rộng (nguồn cho gen_data.py)
├── phrases_data.py     # Script sinh phrases.gen.js
├── roles_data.py       # Script sinh roles.gen.js (nội dung theo vai trò)
├── content_extra.py    # Hội thoại + đoạn họp bổ sung (v2.0), gen_data.py ghép vào
├── ja_data.py          # Thuật ngữ tiếng Nhật cho 370 từ
├── img/showcase/       # Ảnh chụp màn hình (WebP) của trang giới thiệu
├── tests/              # Test Playwright mobile (tests/run.sh)
├── sw.js, manifest.webmanifest, icon-*.png   # PWA
├── gioi-thieu.html     # Trang giới thiệu v2.0 (showcase)
├── gioi-thieu-v1.html  # Trang giới thiệu v1 (lưu trữ)
├── CHANGELOG.md        # Lịch sử phiên bản
├── game/               # Nói Nghề Quest: index.html (theme) + game.js (logic) + bản sao *.gen.js
├── docs/               # showcase bản artifact, video demo, review
├── push.sh             # push bằng token trong .env (không commit .env)
├── README.md
├── ARCHITECTURE.md     # Kiến trúc / cấu trúc code của app
└── CLAUDE.md           # Ngữ cảnh dự án cho phiên Claude/Cowork mới
```

---

## Triển khai (GitHub Pages)

Repo là site tĩnh, deploy thẳng bằng GitHub Pages:

1. **Settings → Pages** → *Build and deployment* → Source: **Deploy from a branch**.
2. Branch: `main`, thư mục `/ (root)` → **Save**.
3. Sau ~1 phút, site chạy tại `https://hunglv201.github.io/it-english-app/`.

---

## Giấy phép

Dự án cá nhân, dùng cho mục đích học tập.
