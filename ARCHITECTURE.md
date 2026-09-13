# ARCHITECTURE — Cấu trúc code hệ thống

Tài liệu này mô tả cách app được tổ chức bên trong: luồng khởi động, mô hình dữ liệu,
lược đồ lưu trữ, các module chính, thuật toán ôn tập, và cách tích hợp AI. Dành cho
người muốn đọc / sửa / mở rộng code.

---

## 1. Tổng quan kiến trúc

App là **một trang HTML tĩnh**, không framework, không bước build. Toàn bộ chạy phía
client trong trình duyệt:

```
┌──────────────────────── index.html ────────────────────────┐
│  <head>   font Google + <style> (design system, CSS vars)   │
│  <body>                                                     │
│    .shell                                                   │
│      header.top   (logo </>, tên, streak, nút đổi theme)     │
│      main#main    (nơi mọi màn hình được render vào)         │
│      nav.tabs#tabs (5 tab dưới cùng)                        │
│    <script src="data.gen.js">    → window.DATA              │
│    <script src="phrases.gen.js"> → window.PHRASES           │
│    <script> ...toàn bộ logic app... </script>              │
└─────────────────────────────────────────────────────────────┘
```

**Nguyên tắc render:** không dùng Virtual DOM. Mỗi màn hình là một hàm `vXxx()` xoá sạch
`#main` rồi dựng lại DOM bằng helper `el(tag, class, html)`. Điều hướng qua `go(tabKey)`.

**Luồng dữ liệu một chiều đơn giản:**

```
Tương tác người dùng → cập nhật biến state / store → gọi lại hàm vXxx() → DOM vẽ lại
```

---

## 2. Nạp và khởi động

1. `data.gen.js` và `phrases.gen.js` chạy trước, gán `window.DATA` và `window.PHRASES`.
2. Script chính đọc chúng vào các hằng:
   ```js
   const D = window.DATA;
   const VOCAB = D.vocab, DIALOGUES = D.dialogues,
         DICTATION = D.listen, DAYS = D.days;
   const PHRASES = window.PHRASES || [];
   ```
3. Nạp `store` từ localStorage, chuẩn hoá các nhánh còn thiếu, tính lại streak.
4. Gọi `renderTabs()` + `go('home')` để vẽ màn hình đầu.

---

## 3. Mô hình dữ liệu (data.gen.js / phrases.gen.js)

Các file `*.gen.js` **được sinh ra** từ script Python — không sửa tay.

### `window.DATA`

| Trường | Kiểu | Ý nghĩa |
|---|---|---|
| `vocab` | `[]` | Danh sách từ vựng (370 từ). |
| `phrases` | `[]` | Mẫu câu theo ngày. |
| `dialogues` | `[]` | Hội thoại chọn-cách-đáp. |
| `listen` | `[]` | Bài nghe (câu + vị trí từ trống). |
| `days` | `[]` | 370 ngày, mỗi ngày trỏ tới các mục ở trên. |
| `phaseTitles` | `[]` | Tên các chặng chủ đề. |

**Một phần tử `vocab`:**
```js
{ t:"blocker", ipa:"/ˈblɒkər/", pos:"n",
  vi:"thứ chặn không cho làm tiếp",
  ex:"I have a <b>blocker</b> on this task.",   // <b> = từ được tô sáng
  exVi:"Task này mình đang bị chặn." }
```

**Một phần tử `dialogues`:**
```js
{ them:"Can you update me on the task?",
  opts:[ { t:"...", good:true,  fb:"phản hồi/giải thích" },
         { t:"...", good:false, fb:"..." } ] }
```

**Một phần tử `listen`:**
```js
{ s:["if","the","deploy","fails","we","roll","back"],  // câu tách từ
  blank:[3,6] }                                          // chỉ số từ bị ẩn
```

**Một phần tử `days`:**
```js
{ phase:0, title:"...", v:[0,1,2,...], ph:0, di:0, li:0 }
// v: mảng chỉ số vào VOCAB; ph/di/li: chỉ số vào phrases/dialogues/listen
```

### `window.PHRASES` (1000 câu)

```js
[ { name:"Chào hỏi & mở đầu ngày",
    items:[ { en:"Good morning, everyone.", vi:"Chào buổi sáng cả nhà." }, ... ] },
  ... ]  // 25 nhóm
```

---

## 4. Lược đồ lưu trữ (localStorage)

Toàn bộ tiến độ nằm trong **một khoá** duy nhất:

```
localStorage["it-english-v1"] = JSON.stringify(store)
```

```js
store = {
  srs:   { "<term>": { ease, int, reps, due } },   // trạng thái ôn tập từng từ
  stats: { done, lastDay, streak },                // tổng lượt + streak
  days:  { done: { "<n>": true }, cur },           // ngày đã học + ngày hiện tại
  today: { date: "YYYY-MM-DD", done: { vocab, listen, talk, phrases } },
  saved: [ { en, note } ]                          // câu đã lưu
}
```

- `load()` / `save()` bọc trong `try/catch` — nếu localStorage bị chặn, app vẫn chạy (mất lưu).
- **Streak** tính khi mở app: cùng ngày → giữ; đúng hôm qua → +1; cách quãng → reset về 1.
- `today` tự reset khi sang ngày mới (so `date`).

---

## 5. Các module chính trong `index.html`

| Nhóm | Hàm / biến tiêu biểu | Vai trò |
|---|---|---|
| Hạ tầng | `el()`, `$()`, `toast()`, `ICO` | Tạo DOM, chọn phần tử, thông báo, kho icon SVG. |
| Điều hướng | `TABS`, `renderTabs()`, `go(k)` | 5 tab dưới, chuyển màn hình. |
| Giọng nói | `speak()`, `pickVoice()`, `VOICE` | Đọc tiếng Anh (TTS), chọn giọng en-US. |
| SRS | `due()`, `grade()`, `learnedCount()` | Chọn từ tới hạn, chấm điểm, đếm từ đã thuộc. |
| Hôm nay | `vHome()`, `markToday()` | 4 việc/ngày, tiến độ, streak. |
| Lộ trình | `vRoadmap()`, `openDay()`, `dayGrid()` | 370 ngày theo chặng, mở chi tiết một ngày. |
| Từ vựng | `vVocab()`, `drawCard()`, `vQuizStart()`, `vList()` | Thẻ lật / kiểm tra / danh sách + lọc chủ đề. |
| Câu | `vPhrase()`, `startRandom()`, `toggleSaved()` | 1000 câu, luyện ngẫu nhiên, lưu câu. |
| Giao tiếp | `vTalkAI()`, `aiInit()`, `aiRules()`, `aiParse()` | Trò chuyện AI theo tình huống. |
| Nghe | `vListen()`, `lShadow()` | Chép chính tả + shadowing (chấm phát âm). |
| Theme | `#themeBtn`, thuộc tính `data-theme` | Sáng / tối / theo hệ thống. |

---

## 6. Thuật toán ôn tập SRS (SM-2 rút gọn)

Mỗi từ có `{ ease, int, reps, due }`. Khi người dùng chấm (`grade(term, g)`), với
`g`: `0=Ôn lại · 1=Khó · 2=Nhớ · 3=Dễ`:

- `g=0`: reset `reps=0`, `int=0` → từ quay lại sau ~1 phút.
- `g≥1`: `reps++`; khoảng lặp `int`: lần 1 → 1 ngày, lần 2 → 3 ngày, sau đó → `int × ease`.
- `ease` điều chỉnh: Khó `−0.15`, Dễ `+0.15`, tối thiểu `1.3`.
- `due = now + int ngày`. Từ được coi là **đã thuộc** khi `reps ≥ 2`.

`due()` trả về các từ có `due ≤ now` (hoặc chưa từng học) để đưa vào phiên ôn.

---

## 7. Tích hợp AI (hiện tại)

Phần Giao tiếp dùng **capability `sample`** của Artifact:

```js
aiSample = await window.claude.use('sample');   // chỉ tồn tại trong claude.ai
const reply = await aiSample.json(prompt, { modelTier:'quick' });
```

- `aiRules(scenario)` dựng system prompt: AI đóng vai đồng nghiệp, trả lời 1–2 câu
  tiếng Anh đơn giản, kết bằng câu hỏi, rồi thêm dòng `FIX:` sửa lỗi câu vừa rồi (tiếng Việt).
- `aiParse(text)` tách phần hội thoại và phần `FIX:` để hiển thị riêng.
- Nếu `window.claude` không tồn tại (chạy ngoài claude.ai), `aiInit()` trả `null` và app
  hiện thông báo — các phần khác không bị ảnh hưởng.

### Tích hợp Claude API (kế hoạch sau)

Để chạy AI ngoài claude.ai mà **không lộ API key**, cần một proxy nhỏ:

```
Browser (index.html)  ──POST /api/chat──►  Backend giữ ANTHROPIC_API_KEY
      ▲                                          │
      └──────────── JSON phản hồi ◄──────────────┘  gọi api.anthropic.com
```

Chỉ cần thay chỗ gọi `aiSample.json(...)` bằng `fetch('/api/chat', ...)`. Backend có thể
là một serverless function (Vercel/Cloudflare Workers) đọc key từ biến môi trường.
**Không** đặt key trong `index.html`.

---

## 8. Design system (CSS)

Khai báo bằng CSS variables trong `:root`, đảo màu cho tối bằng
`@media (prefers-color-scheme: dark)` và `:root[data-theme="dark"]`:

- Màu nhấn duy nhất: `--accent:#1b4dff` (sáng) / `#5b7cff` (tối), dùng tiết chế.
- Nền phẳng, viền mảnh 1px (`--line`), bo góc 12–16px, không gradient/không glass.
- Font: `--disp` (Bricolage Grotesque, tiêu đề) · `--sans` (Hanken Grotesk, nội dung)
  · `--mono` (IBM Plex Mono, thuật ngữ IT + nhãn nhỏ + streak).
- Animation nhẹ: `.view > *` trượt lên khi vào màn hình; tôn trọng
  `prefers-reduced-motion`.

---

## 9. Mở rộng thường gặp

- **Thêm bài học / chặng:** sửa `phases_extra.py` (mỗi chặng: 10 từ, 5 mẫu câu,
  2 hội thoại, 4 bài nghe) → chạy `python3 gen_data.py`.
- **Thêm nhóm câu:** sửa `phrases_data.py` → chạy `python3 phrases_data.py`.
- **Đổi số việc mỗi ngày:** sửa mảng `tasks` trong `vHome()`.
- **Đổi tình huống AI có sẵn:** sửa `AI_SCENARIOS` (thêm `{ k, l, s }`).
- **Reset tiến độ:** xoá khoá `it-english-v1` trong localStorage (DevTools → Application).

---

## 10. Giới hạn đã biết

- Tiến độ lưu **cục bộ theo trình duyệt** (localStorage) — không đồng bộ giữa máy/thiết bị.
- Chất lượng giọng đọc và độ chính xác chấm phát âm phụ thuộc Web Speech API của từng
  trình duyệt (Chrome tốt nhất).
- Phần AI cần claude.ai cho tới khi dựng backend proxy (mục 7).
