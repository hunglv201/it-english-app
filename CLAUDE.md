# CLAUDE.md — Ngữ cảnh dự án cho phiên làm việc mới

> Đọc file này trước khi sửa gì. Mục tiêu: một phiên Claude/Cowork mới nắm được dự án trong 2 phút
> mà không cần lục lại lịch sử hội thoại. Cập nhật file này khi có thay đổi lớn về cấu trúc, pipeline hoặc quy ước.

## 1. Dự án là gì

**IT English** — bộ 3 sản phẩm web tĩnh (vanilla HTML/CSS/JS, không framework, không build) giúp người Việt
trình độ cơ bản luyện tiếng Anh IT / môi trường công sở. Chủ repo: `hunglv201`. Ngôn ngữ giao tiếp với người dùng: **tiếng Việt**.

| Sản phẩm | File | URL Pages | Mô tả |
|---|---|---|---|
| **App học** | `index.html` (+ `data.gen.js`, `phrases.gen.js`, `sw.js`, `manifest.webmanifest`) | `https://hunglv201.github.io/it-english-app/` | Lộ trình 370 ngày, từ vựng SRS, 1000 câu, nghe/shadowing, **Giao tiếp AI** (điểm nhấn), PWA offline. Version hiện tại **1.18.0** |
| **Trang giới thiệu (showcase)** | `gioi-thieu.html` (≈1.6 MB, ảnh JPEG inline) | `…/gioi-thieu.html` | Landing fullpage scroll-snap, nền particle-net, chữ chạy, 17 ảnh chụp màn hình có caption, tập trung vào tính năng AI. Dark-first, nền đen mặc định |
| **Game "IT English Quest"** | `game/index.html` + `game/game.js` (+ bản sao `game/data.gen.js`, `game/phrases.gen.js`) | `…/game/` | Bản game anime **mobile-first**: RPG bản đồ ngày → quiz battle → boss visual novel, AFK idle (Mochi tự cày xu), Shop, huy hiệu, tab **Nói** 5 chế độ luyện nói. Dùng chung dữ liệu + AI key với app |

Ngoài Pages, cả 3 còn được publish làm **claude.ai Artifact** (xem mục 6).

## 2. Cấu trúc thư mục

```
it-english-app/
├── index.html            # App: toàn bộ UI + logic (HTML/CSS/JS 1 file, ~220 KB)
├── data.gen.js           # window.DATA — sinh từ gen_data.py, KHÔNG sửa tay
├── phrases.gen.js        # window.PHRASES — sinh từ phrases_data.py, KHÔNG sửa tay
├── gen_data.py / phases_extra.py / phrases_data.py   # nguồn sinh dữ liệu (Python 3, không lib ngoài)
├── sw.js                 # service worker; CACHE = 'it-english-v<version>' — bump cùng version app
├── manifest.webmanifest, icon-192.png, icon-512.png  # PWA
├── gioi-thieu.html       # Showcase (standalone, có doctype/head/favicon)
├── game/
│   ├── index.html        # CSS theme anime (Fredoka/Nunito/IBM Plex Mono) + khung HTML
│   ├── game.js           # Toàn bộ logic game (IIFE, ~100 KB)
│   └── data.gen.js, phrases.gen.js   # bản sao của root (copy lại khi regen dữ liệu)
├── docs/
│   ├── it-english-showcase.html      # bản showcase dùng cho Artifact (không doctype/head/body)
│   ├── demo/giao-tiep-ai-demo.mp4    # video demo luồng Giao tiếp AI (không tiếng)
│   ├── design/, bgchooser.html, REVIEW-*.md
├── push.sh               # push bằng token trong .env (gitignored)
├── README.md             # tài liệu người dùng
├── ARCHITECTURE.md       # kiến trúc chi tiết của APP (state, SRS, module)
└── CLAUDE.md             # file này
```

## 3. Dữ liệu & lưu trữ

- `window.DATA`: `vocab[370]{t,ipa,pos,vi,ex,exVi}`, `days[370]{n,phase,title,v[],ph,di,li}`, `phaseTitles[37]`,
  `listen[148]{s[],blank[],hint}`, `dialogues[74]{them,opts[{t,good,fb}]}`, `phrases[185]{en,vi,note}`.
- `window.PHRASES`: 26 nhóm câu thường dùng.
- **localStorage**
  - App: key `it-english-v1` → `store` gồm `ai:{provider,key,model}`, `cfg.level`, `days.cur/done`, SRS, streak…
  - Game: key `it-english-game-v1` → `G` (lv, xp, hp, coins, cleared, badges, items, up, idle, daily, talk{equipped,…}).
    Game **đọc** `it-english-v1` để lấy AI cfg + ngày đang học, và **ghi ngược** `days.done` khi qua màn.

## 4. AI

- Nhà cung cấp: **Gemini** (`gemini-flash-lite-latest`, free), **Claude** (`claude-3-5-haiku-latest`), **Groq** (`llama-3.1-8b-instant`).
  Gọi thẳng từ trình duyệt bằng key người dùng dán vào (lưu localStorage, dùng chung app ↔ game).
- Khi chạy **trong claude.ai Artifact** → dùng `window.claude.use('sample')` (capability `sample`), không cần key.
  Thứ tự ưu tiên: `inClaude()` → key đã cấu hình → hiện sheet nhập key.
- Game: `aiCfg()`, `claudeSp()` (memo), `aiConfigured()`, `aiCall(system,msgs)`, `aiCallWith(cfg,…)`, `aiSetupSheet()` (Hồ sơ › Boss AI, có "Kiểm tra & lưu").
- Các prompt nằm ngay trong code (`aiRules`, `battleRules`, `SCEN`…). Yêu cầu chung: AI nói tiếng Anh đơn giản, sửa lỗi dạng `wrong => right ~ ghi chú tiếng Việt có dấu`.

## 5. Game — những điểm cần nhớ khi sửa

- **Mobile-first, chuẩn iPhone SE 375×667**: mọi màn (Bản đồ, Nói, Shop, Hồ sơ, các màn chơi) phải vừa 1 màn, không cuộn dọc.
  Bản đồ: `#main:not(.chatlay)` có `min-height` = màn hình, thẻ AFK `flex:1` giãn lấp chỗ trống; sân ≥100px thêm class `tall`, ≥170px `xl` (ResizeObserver `sizeArena`).
- Router: `TABS=[map,talk,shop,profile]`, `go(k)` (gỡ `infight`/`chatlay`, clear `mapTimer`, `stopSR()`, `animIn()` cho chuyển cảnh).
- Màn chơi kiểu chat: `main.classList.add('chatlay')`, nội dung `.fill` giãn, thanh hành động ghim đáy qua `botBar(node)` (chứa `talkBar()` mic+gõ+gửi, hoặc `nextBtn()`, hoặc `.choices`).
- Modal: `openModal(build,{closable})` — mặc định có nút ✕ + bấm nền để đóng; luồng bắt buộc (thắng/thua, boss, kết quả, hướng dẫn, chào mừng) dùng `openModalLocked`.
- Dock tab `.tabs` cố định đáy, ẩn bằng `body.infight`. Hiệu ứng: `#main.vin>*` (viewin), `.pop`, nhấn nút lún.
- Bài kiểm tra Playwright nằm ở scratchpad phiên cũ (không commit): stub `speechSynthesis` phải có `getVoices`, `onvoiceschanged`, `addEventListener`; hàm game nằm trong IIFE nên test qua click UI (`.tab`, `.tmode`, `.thero`, `.qchip`, `.node.cur`…).

## 6. Deploy — pipeline chuẩn

Repo git nằm trên **máy người dùng** (thư mục kết nối Cowork: `/Users/macbookpro/Desktop/me/it-english-app`, trong device shell là `$HOME/mnt/me/it-english-app`).

1. Sửa code (nếu làm trong cloud: `cp` sang `/mnt/user-data/outputs/it-english-app/...` rồi `device_commit_files`).
   ⚠️ Commit file lên máy hay **trễ**: sau khi ghi, `sleep` vài giây rồi `grep -c` một chuỗi mới để xác nhận; nếu = 0 thì commit lại file đó.
2. `git add … && git commit` (message tiếng Việt, prefix `feat(game):`, `fix:`, `docs(showcase):`, `v1.x.y:`…).
3. Push **cả 2 nhánh**: `git push <url-có-token> HEAD:main HEAD:feature/ai-integration`.
   Token GitHub nằm trong `.env` (gitignored) → dùng `./push.sh "msg"` hoặc đọc `GITHUB_TOKEN` từ `.env`. **Không bao giờ** in/commit token hay API key.
4. Pages build tự chạy từ `main` (legacy, root `/`); có thể kích hoạt thêm bằng `POST /repos/hunglv201/it-english-app/pages/builds` (trả 201).
   Shell cloud/device **không** truy cập được `github.io` (proxy chặn) → kiểm tra bằng API `pages/builds/latest` (status `built`, đúng commit).
5. Artifact claude.ai (đọc `action:list` để lấy URL nếu cần):
   - Game: `b021f5f2-79f1-4ce0-8d44-2336124b7183` — publish `scratchpad/gameart/index.html` (bản game/index.html **bỏ** doctype/html/head/body, giữ `<title>`, `<link>`, `<style>`) với `root` + `files:{"game.js":"game.js"}`, capability `sample`.
   - Showcase: `e31f3307-4779-4d84-83cc-387be652b315` — file `docs/it-english-showcase.html`.
   - App: cũng có artifact riêng (tìm trong gallery).
6. Khi tăng version app: sửa chuỗi version trong `index.html` **và** `CACHE` trong `sw.js`.

## 7. Quy ước & ràng buộc

- Trả lời/commit bằng **tiếng Việt**; code/identifier tiếng Anh.
- Không thêm framework/build tool; giữ 1 file cho app, 2 file cho game.
- Không commit `.env`, `*.png` chụp màn hình, `*.mjs` test (đã gitignore).
- Commit có attribution: `Co-Authored-By: Claude … <noreply@anthropic.com>` + `Claude-Session: <link>` (theo reminder của phiên).
- Người dùng hay xem trên **điện thoại** và **Claude desktop**: ưu tiên bố cục gọn, chữ không quá to, không cuộn thừa, animation nhẹ (đã có `prefers-reduced-motion`).

## 8. Lịch sử tóm tắt (mới → cũ)

- 09/2026: game hoàn thiện mobile-first (map 1 màn, Nói/Shop/Hồ sơ gọn, màn chơi kiểu chat, AFK giãn + Mochi nói câu đã học, sheet có ✕, chuyển cảnh mượt).
- Game: tab Nói (Đấu thoại AI, Đọc theo nhịp, Chuyện văn phòng VN, Phản xạ 5s, Trang bị Mochi), AFK idle, Shop, nhập AI key trong game.
- Game khởi tạo: RPG map + quiz battle + boss VN; app v1.18.0 thêm nút "🎮 IT English Quest".
- Favicon logo cho app + showcase; showcase: CTA thẻ kính, nền đen mặc định, particle-net, fullpage scroll, chữ chạy.
- App v1.17.x: "Nghe hết" hội thoại có xướng vai, header Giao tiếp 1 hàng, video demo.

## 9. Ý tưởng còn mở (chưa làm)

- Backend/proxy giữ API key (thay vì key phía client).
- Đồng bộ tiến độ đa thiết bị (hiện chỉ localStorage).
- Thêm boss/nhân vật, nhiều kết cục hơn cho Chuyện văn phòng; bảng xếp hạng.
