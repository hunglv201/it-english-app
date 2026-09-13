# IT English — App luyện tiếng Anh IT cơ bản

Ứng dụng web cá nhân giúp luyện tiếng Anh chuyên ngành IT và môi trường làm việc,
dành cho người trình độ cơ bản. Chạy hoàn toàn trong trình duyệt, không cần server,
không cần tài khoản.

**Live demo:** https://hunglv201.github.io/it-english-app/

---

## Tính năng

- **Hôm nay** — bài học thích ứng mỗi ngày (4 việc ngắn, ~5 phút): ôn từ, nghe, trò chuyện AI, luyện câu. Có streak (chuỗi ngày) và thanh tiến độ.
- **Lộ trình 370 ngày** — chia theo chặng chủ đề; mỗi ngày gồm từ vựng, mẫu câu, hội thoại, bài nghe và phần luyện thêm với AI.
- **Từ vựng** — 3 chế độ: *thẻ lật* (phát âm + ví dụ), *kiểm tra* (trắc nghiệm 2 chiều Anh↔Việt), *danh sách* (tìm kiếm, lọc chủ đề). Ôn tập theo thuật toán **SRS (SM-2 rút gọn)**.
- **Câu thường dùng** — 1000 câu chia 25 nhóm; lưu câu yêu thích để ôn lại.
- **Giao tiếp** — trò chuyện với AI theo tình huống công việc (standup, báo blocker, code review, deploy…). AI đóng vai đồng nghiệp, nói tiếng Anh đơn giản và **sửa lỗi** sau mỗi lượt. Có thể mô tả lĩnh vực của bạn để AI gợi ý tình huống riêng.
- **Nghe** — 2 chế độ: *chép chính tả* (điền từ trống) và *shadowing* (nhại lại, chấm phát âm qua mic theo %).
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

Phần **Giao tiếp → Trò chuyện AI** hiện gọi Claude qua `window.claude.use('sample')`,
chỉ hoạt động khi app chạy **bên trong claude.ai**. Khi mở ngoài (GitHub Pages, `file://`,
host tĩnh khác) phần này tự hiển thị thông báo *"Cần mở app trong Claude"*; các tính năng
còn lại vẫn chạy đầy đủ.

**Kế hoạch (sau):** thay bằng Claude API dùng API key riêng. Không đặt key trực tiếp trong
`index.html` (lộ key) — cần một backend/proxy nhỏ giữ key và chuyển tiếp yêu cầu. Xem mục
*Tích hợp Claude API* trong [`ARCHITECTURE.md`](./ARCHITECTURE.md).

---

## Sinh lại dữ liệu

Chỉ cần Python 3, không phụ thuộc thư viện ngoài:

```bash
python3 gen_data.py      # -> data.gen.js     (cần phases_extra.py cùng thư mục)
python3 phrases_data.py  # -> phrases.gen.js
```

Muốn thêm/sửa bài học thì sửa các file `*.py` rồi chạy lại — **không sửa tay** file `*.gen.js`.

---

## Cấu trúc thư mục

```
it-english-app/
├── index.html          # App (giao diện + logic)
├── data.gen.js         # Dữ liệu 370 ngày (sinh ra, không sửa tay)
├── phrases.gen.js      # 1000 câu (sinh ra, không sửa tay)
├── gen_data.py         # Script sinh data.gen.js
├── phases_extra.py     # 27 chặng chủ đề mở rộng (nguồn cho gen_data.py)
├── phrases_data.py     # Script sinh phrases.gen.js
├── README.md
└── ARCHITECTURE.md     # Tài liệu kiến trúc / cấu trúc code
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
