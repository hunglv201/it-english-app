# CLAUDE.md — Ngữ cảnh dự án cho phiên làm việc mới

> Đọc file này trước khi sửa gì. Mục tiêu: một phiên Claude/Cowork mới nắm được dự án trong 2 phút
> mà không cần lục lại lịch sử hội thoại. Cập nhật file này khi có thay đổi lớn về cấu trúc, pipeline hoặc quy ước.

## 1. Dự án là gì

**Nói Nghề** (tên cũ đến v2.0: *IT English*; repo/khoá localStorage vẫn giữ tên `it-english`) — bộ 3 sản phẩm web tĩnh
(vanilla HTML/CSS/JS, không framework, không build) giúp người Việt trình độ cơ bản luyện **tiếng Anh công việc theo ngành**
(v3.1: 9 ngành — Công sở chung (mặc định), IT, Khách sạn · Du lịch, Bán hàng · CSKH, Sản xuất · Nhà máy, Logistics · XNK, Tài chính · Kế toán, Marketing · TMĐT, Y tế · Điều dưỡng — và "Nghề của tôi" do AI tạo). Chủ repo: `hunglv201`. Ngôn ngữ giao tiếp với người dùng: **tiếng Việt**.

| Sản phẩm | File | URL Pages | Mô tả |
|---|---|---|---|
| **App học** | `index.html` (+ `data.gen.js`, `phrases.gen.js`, `sw.js`, `manifest.webmanifest`) | `https://hunglv201.github.io/it-english-app/` | Gói ngành (IT 370 ngày, các ngành khác 120 ngày), từ vựng SRS, câu thường dùng, nghe/shadowing, **Giao tiếp AI** (điểm nhấn), PWA offline. Version hiện tại **3.1.0** trên `main`; nhánh `feature/backend-v4` = **4.0.0** (backend Supabase, chưa merge) (`APP_VERSION` trong `index.html` + `CACHE` trong `sw.js`) |
| **Trang giới thiệu (showcase)** | `gioi-thieu.html` (**v3.0**, ảnh `img/showcase/v3/`) + lưu trữ `gioi-thieu-v2.html`, `gioi-thieu-v1.html` | `…/gioi-thieu.html` | Landing fullpage scroll-snap, nền particle-net, mục "Mới trong v3.0" (lưới 5 ngành), mục **Lịch sử phiên bản** (`#versions`). Dark-first. Quy ước version lớn: xem mục 7 |
| **Game "Nói Nghề Quest"** | `game/index.html` + `game/game.js` (+ bản sao `game/data.gen.js`, `game/phrases.gen.js`) | `…/game/` | Bản game anime **mobile-first**: RPG bản đồ ngày → quiz battle → boss visual novel, AFK idle (Mochi tự cày xu), Shop, huy hiệu, tab **Nói** 5 chế độ luyện nói. Dùng chung dữ liệu + AI key với app |

Ngoài Pages, cả 3 còn được publish làm **claude.ai Artifact** (xem mục 6).

## 2. Cấu trúc thư mục

```
it-english-app/
├── index.html            # App: toàn bộ UI + logic (HTML/CSS/JS 1 file, ~220 KB)
├── data.gen.js           # gói IT: window.DATA — sinh từ gen_data.py, KHÔNG sửa tay
├── packs/<id>.gen.js     # gói ngành office/hotel/sales/factory/logistics/finance/marketing/health (window.PACK + DATA + PHRASES + ROLES) — sinh từ packs_src/build.py
├── packs/custom.js       # VIẾT TAY: ghép store.customPack ("Nghề của tôi", AI tạo) vào đầu gói office khi track='custom'
├── packs_src/            # nguồn gói ngành: <id>.py (PACK), build.py (kiểm tra chặt + sinh), README.md (SCHEMA + quy tắc nội dung)
├── phrases.gen.js        # window.PHRASES — sinh từ phrases_data.py, KHÔNG sửa tay
├── gen_data.py / phases_extra.py / phrases_data.py   # nguồn sinh dữ liệu (Python 3, không lib ngoài)
├── roles_data.py         # -> roles.gen.js (window.ROLES: 7 vai Dev/QA/DevOps/BA/PM/Designer/Data — tình huống AI + hội thoại chọn đáp)
├── content_extra.py      # nội dung bổ sung v2.0: +3 hội thoại & +2 đoạn họp nghe cho mỗi chặng (gen_data.py ghép vào)
├── ja_data.py            # thuật ngữ tiếng Nhật; gen_data.py ghép vào vocab[].ja = "日本語|romaji"
│                         # ⚠ mọi script sinh *.gen.js TỰ copy sang game/ — không copy tay
├── img/showcase/*.webp   # 17 ảnh của gioi-thieu-v1.html (bản lưu trữ)
├── img/showcase/v2/*.webp # 25 ảnh của gioi-thieu-v2.html (lưu trữ)
├── img/showcase/v3/*.webp # 33 ảnh của gioi-thieu.html v3.0 (540×1169, chụp bằng Playwright + AI giả, nhiều ngành)
├── tests/                # Playwright mobile: lib.mjs + a…i.mjs, run.sh (xem tests/README.md) — g.mjs: đa ngành · i.mjs: tài khoản/đồng bộ (server giả cloud-fake.mjs) · sync-core.test.mjs (node)
├── cloud-config.js       # v4.0: url + anonKey Supabase (công khai). ĐỂ TRỐNG = tắt máy chủ, app chạy như v3.1
├── sync-core.js          # v4.0: hàm thuần làm phẳng store ↔ path→value, diff, luật gộp (giống nn_resolve SQL)
├── cloud.js              # v4.0: window.NNCloud — khách tự động, Google, đồng bộ offline-first, AI qua server, báo lỗi
├── vendor/supabase.min.js # supabase-js tự host (chỉ tải khi cloud-config có url)
├── supabase/             # v4.0: migrations/ (0001 users · 0002 sync · 0003 reports/ai/stats), functions/ (ai, delete-account), queries/admin.sql, tests/db_test.sh
├── chinh-sach.html · dieu-khoan.html · xoa-du-lieu.html  # v4.0: trang pháp lý (cần điền email liên hệ)
├── sw.js                 # service worker; CACHE = 'it-english-v<version>' — bump cùng version app
├── manifest.webmanifest, icon-192.png, icon-512.png  # PWA
├── gioi-thieu.html       # Showcase v3.0 (standalone, có doctype/head/favicon)
├── gioi-thieu-v2.html    # Showcase v2.0 lưu trữ
├── gioi-thieu-v1.html    # Showcase v1 lưu trữ (noindex, thanh "Bản lưu trữ" ở đáy)
├── CHANGELOG.md          # lịch sử phiên bản đầy đủ (showcase link tới)
├── game/
│   ├── index.html        # CSS theme anime (Fredoka/Nunito/IBM Plex Mono) + khung HTML
│   ├── game.js           # Toàn bộ logic game (IIFE, ~100 KB)
│   ├── data.gen.js, phrases.gen.js, roles.gen.js   # bản sao do script sinh tự copy
│   └── packs/<id>.gen.js  # bản sao gói ngành (build.py tự copy)
├── docs/
│   ├── it-english-showcase.html      # bản showcase dùng cho Artifact (không doctype/head/body)
│   ├── demo/giao-tiep-ai-demo.mp4    # video demo luồng Giao tiếp AI (không tiếng)
│   ├── design/, bgchooser.html
│   ├── REVIEW-2026-09-13.md          # review UX/thị trường (mã A1…E16), phần 'Còn lại' đã lạc hậu
│   ├── DINH-HUONG-DA-NGANH-2026-09-20.md  # định hướng v3.0 đa ngành (đã làm)
│   ├── BACKEND-PLAN.md               # kế hoạch backend Supabase (server-first, offline, đăng nhập Google, bảng, RLS, ước lượng)
│   ├── BACKEND.md                    # ⭐ v4.0 (nhánh feature/backend-v4): cách đồng bộ chạy + dựng project + vận hành + kiểm thử
│   ├── TINH-NANG-MOI-2026-09-23.md   # ⭐ nghiên cứu tính năng mới (giữ chân, đối thủ, lớp học, tiếng Nhật) + lộ trình đợt A–D
│   ├── BACKLOG.md                    # ⭐ việc để sau (kiểm tra trình độ, tiếng Nhật chính, lớp học…)
│   ├── review/*.md                   # nhật ký kiểm duyệt nội dung từng gói (v3.1)
│   └── REVIEW-2026-09-20.md          # ⭐ rà soát kỹ thuật + tổng hợp hướng cải tiến + kế hoạch 3 đợt — ĐỌC TRƯỚC KHI CHỌN VIỆC
├── push.sh               # push bằng token trong .env (gitignored)
├── README.md             # tài liệu người dùng
├── ARCHITECTURE.md       # kiến trúc chi tiết của APP (state, SRS, module)
└── CLAUDE.md             # file này
```

## 3. Dữ liệu & lưu trữ

**Gói ngành (v3.0)** — `<head>` của `index.html` và `game/index.html` có script nạp gói bằng `document.write`:
`store.cfg.track` (hoặc `?track=`) → `it` nạp `data/phrases/roles.gen.js`, còn lại nạp `packs/<id>.gen.js`. Người dùng cũ có tiến độ mà chưa có
`track` → `it`; người mới → `office`. Trong app: `TRACK`, `TRK` (meta trong hằng `TRACKS`: emoji, nhãn, vai, `them`), `PACK` (`null` = IT),
`who()` (persona cho mọi prompt AI; `store.cfg.persona` từ JD ghi đè), `REPORT` (báo cáo 60s theo ngành), `AI_SCENARIOS/READING/EVENT_TYPES/REV`
lấy từ `PACK` nếu có. Đổi ngành: `switchTrack(id)` → lưu + tải lại; tiến độ lộ trình từng ngành cất ở `store.trackDays[track]={days,focus}`
(`store.daysTrack` = ngành đang giữ `store.days`). Làm quen: `onboardModal(step)` (3 bước, đều bỏ qua được), `trackPicker()`, `trackNudge()`.
**v3.1**: `track='custom'` = office.gen.js + packs/custom.js (đọc `store.customPack` do `cpGenerate()` tạo: 3 chặng, validate bằng `cpFixPhase`). Báo lỗi nội dung: `reportBtn(kind,obj)` → `store.reports[]` → GitHub issue (`reportIssueUrl`). Rảnh tay: `hf` + `hfGo()` (vòng lặp `hfSpeakP`→`hfListenP`→`wordMatch`, dừng khi rời màn `.hfv`). Ảnh → bài học: `vPhoto`/`phGo` + `aiVisionJson` (claude.ai `sample({images})`, Gemini `inline_data`, Claude API `image`; `providerChat(opts.image, opts.maxTokens)`).
**v4.0 (nhánh `feature/backend-v4`)**: `save()` gọi `NNCloud.touch()`; `cloudBoot()` bind hook (getStore/saveStore/onPulled…) rồi `NNCloud.init()`. Dữ liệu học = bản đồ phẳng (`NNSync.toFlat/fromFlat`), đẩy lô `apply_changes` so với `shadow` (meta ở localStorage `noinghe-cloud-v1`), kéo `get_state` khi `rev` đổi. Không đồng bộ: `store.ai` (key), `convos[].turns`, `cfg.voiceName/remind`. AI: `aiInit()` bước 3 dùng `cloudAdapter()` khi không có key riêng. Màn `vAccount` (`go('account')`). Chi tiết: `docs/BACKEND.md`.
**Đợt B (nhánh `feature/noi-tot-hon`)**: `aiTargets`/`pickTargets()`/`targetsRule()` (từ mục tiêu vào `aiRules`, `targetsCheck` khi gửi → `grade`/`psrsGrade` nếu tới hạn) · `twHtml()` + `twOpen()` (chạm từ trong bóng AI; `dictFind` tra gói trước, AI sau, cache `aiCacheGet`) · `looksVietnamese`→`aiViToEn` · `xScenarios()` (x_interview/x_meeting/x_present, `X_RUBRIC` trong `aiReview`) · `nearMark`/`wNear` + `lTokens(diff,heard)` + `[data-say]` (chạm nghe chậm) · `vAudit`/`auStats`/`auAnalyze` (`go('audit')`, `store.audits`) · `weekendShield`, `store.stats.broke/repairAt/perfect`, `repairCard`/`doRepair`, `celebrate()`.
Thêm ngành mới: viết `packs_src/<id>.py` theo SCHEMA → `python3 packs_src/build.py <id>` → thêm id vào `ORDER` (build.py), `TRACKS` + map
`T` trong 2 script nạp (app + game), `GTRACKS` trong game.js, placeholder/hint theo ngành (tìm `({office:` trong index.html), `sw.js` ASSETS, test `tests/h.mjs`. Quy trình nội dung: agent viết theo README → **agent khác kiểm duyệt** (log vào `docs/review/`) → build.

**Gói IT (dữ liệu gốc):**

- `window.DATA`: `vocab[370]{t,ipa,pos,vi,ex,exVi}`, `days[370]{n,phase,title,v[],ph,di,li}`, `phaseTitles[37]`,
  `listen[222]{s[],blank[],hint,p?}` (`p:1` = đoạn họp 2–3 câu, 74 đoạn → app hiện nhiều ô điền), `dialogues[185]{them,opts[{t,good,fb}]}` (đáp án đúng đã xáo vị trí khi sinh), `phrases[185]{en,vi,note}`.
- `window.PHRASES`: 26 nhóm câu thường dùng. `window.ROLES`: {dev,qa,devops,ba,pm,designer,data} → {label,emoji,scenarios[{k:'r_…',l,s}],dialogues[]}.
- `vocab[].ja` (tuỳ chọn): thuật ngữ Nhật, hiện khi `store.cfg.showJa`.
- **localStorage**
  - App: key `it-english-v1` → `store` gồm `ai:{provider,key,model}`, `cfg{level,role,showJa,focus[],domain,jd,jdScenarios}`, `days.cur/done`, `srs` (từ), `psrs` (câu — L1), `standups[]`, `events[]`, `convos[]`, `saved[]`, streak…
  - Cache AI: key `it-english-aicache` (sp.json theo hash prompt, 150 mục, 30 ngày — N8). Sao lưu/khôi phục: Tôi › Sao lưu (K1).
  - Game: key `it-english-game-v1` → `G` (lv, xp, hp, coins, cleared, badges, items, up, idle, daily, talk{equipped,…}).
    Game **đọc** `it-english-v1` để lấy AI cfg, ngày đang học, `srs` (quái ưu tiên từ hay sai — G1), `cfg.role`/`cfg.showJa`; **ghi ngược** `days.done`.
    Game lưu `G.talk.log[]` (buổi Đấu thoại AI) → app nhập vào `store.convos` khi mở Lịch sử/Thống kê (G2).

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

## 5b. App — render & chuyển cảnh (quan trọng khi sửa UI)

- Mỗi màn là hàm `vXxx()` xoá `#main` rồi dựng lại; **cập nhật tại chỗ cũng gọi lại chính hàm đó**. Để không có cảm giác "tải lại cả màn":
  - Hiệu ứng `rise` của `.view>*` chỉ chạy khi `#main` có class `enter` (do `markEnter()` gắn 0.5s).
  - `go(k)` luôn cuộn lên đầu + `markEnter()`. Trong màn, dùng **`viewTop(key)`** thay cho `window.scrollTo(0,0)`: chỉ cuộn/hiệu ứng khi `key` đổi (vd `'rv'+rv.i` — sang câu mới), còn bấm nút/chấm điểm/bật tắt thì giữ nguyên vị trí.
  - Hiệu ứng vào của thẻ (`cardIn`/`flipReveal`) bọc bằng **`onceCls(slot,key,cls)`** để chỉ chạy khi đổi mục.
- Thành phần UI dùng chung (v1.22): `pinBar()` (thanh ghim đáy, nền đặc + dải mờ ::before), `.ptile/.pgrid` (ô Luyện), `.phtile/.phgrid` (lưới chặng), `aiWait(label,n)` (khung chờ AI, tự cuộn tới), `buzz(ok)` (rung), `paintOffline()` (dải offline), `body.kb` (bàn phím mở → ẩn tab, pinbar sát đáy qua visualViewport).
- Danh sách dài phải tải dần (xem `paintVL`: 30 mục + IntersectionObserver). Không đặt nút nổi đè nội dung.
- Không dùng thư viện diff DOM vì nhiều handler đóng (closure) vào chính node của nó (`b.onclick=…b.textContent=…`).

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
   - Game: `https://claude.ai/artifact/NkUhE8SvgU8UZTXsmbzS5G` — publish `scratchpad/gameart/index.html` (bản game/index.html **bỏ** doctype/html/head/body + script CSP; script nạp gói **thay bằng bản tạo `<script async=false>` động** — không dùng `document.write` trong artifact) với `root` + `files` gồm game.js, data/phrases/roles.gen.js và `packs/*.gen.js` + `packs/custom.js`, capability `sample`. Ngành chọn trong game › Hồ sơ › Ngành đang học.
   - Showcase: `e31f3307-4779-4d84-83cc-387be652b315` — file `docs/it-english-showcase.html`.
   - App: cũng có artifact riêng (tìm trong gallery).
6. Khi tăng version app: sửa chuỗi version trong `index.html` **và** `CACHE` trong `sw.js`.

## 7. Quy ước & ràng buộc

- Trả lời/commit bằng **tiếng Việt**; code/identifier tiếng Anh.
- Không thêm framework/build tool; giữ 1 file cho app, 2 file cho game.
- Không commit `.env`, `*.png` chụp màn hình, `*.mjs` test (đã gitignore).
- Commit có attribution: `Co-Authored-By: Claude … <noreply@anthropic.com>` + `Claude-Session: <link>` (theo reminder của phiên).
- **Version lớn (major, vd 2.0 → 3.0)**: (1) chép `gioi-thieu.html` hiện tại thành `gioi-thieu-v<N>.html` (thêm `noindex` + thanh `.archive-bar`), (2) chụp ảnh mới vào `img/showcase/v<N+1>/` (script mẫu: chụp bằng Playwright với store nạp sẵn + AI giả, ẩn toast), giữ nguyên ảnh cũ để bản lưu trữ không vỡ, (3) thêm mục vào timeline `#versions` của showcase + `CHANGELOG.md`, và thêm dòng mới vào menu chọn phiên bản `#vsel .vmenu` ở đầu **mọi** file `gioi-thieu*.html` (bản đang xem gắn `aria-current`), (4) bump `APP_VERSION` + `CACHE`. Version nhỏ chỉ cần ghi `CHANGELOG.md`.
- Người dùng hay xem trên **điện thoại** và **Claude desktop**: ưu tiên bố cục gọn, chữ không quá to, không cuộn thừa, animation nhẹ (đã có `prefers-reduced-motion`).

## 8. Lịch sử tóm tắt (mới → cũ)

- 09/2026 **v3.1.0**: +4 ngành (Logistics, Tài chính, Marketing, Y tế); kiểm duyệt chéo 8 gói (~205 sửa, `docs/review/`); ⚑ báo lỗi nội dung; luyện nói rảnh tay; "Nghề của tôi" (AI tạo gói 3 chặng); ảnh → bài học; game đổi ngành trong Hồ sơ. Test `h.mjs`.
- 09/2026 **v3.0.0 (major)**: đổi tên **Nói Nghề**; đa ngành (Công sở chung mặc định, IT, Khách sạn, Bán hàng, Nhà máy; 23 vai); làm quen 3 bước bỏ qua được; tiến độ riêng từng ngành; báo cáo 60s theo nghề; JD mọi ngành + 12 từ riêng; game theo ngành; showcase v3.0 (v2 lưu trữ). Nội dung 4 gói mới viết bởi subagent theo `packs_src/README.md`, build.py kiểm tra.
- 09/2026 **v2.0.0 (major)**: nội dung ×2 — 185 hội thoại chọn đáp (trước 74, sửa lỗi đáp án đúng luôn ở vị trí 1), 222 bài nghe gồm 74 đoạn họp 2–3 câu (điền nhiều ô, shadowing dài), thêm vai Designer & Data (7 vai); showcase v2.0 chụp lại 25 ảnh + mục Standup/Dịch ngược/Theo vai/Tiếng Nhật + lịch sử phiên bản, v1 lưu trữ ở `gioi-thieu-v1.html`; `CHANGELOG.md`.
- 09/2026 **v1.22.0**: nâng cấp UI/UX — bỏ nút AI nổi, Luyện 4 nhóm ô gọn, Lộ trình lưới 37 chặng, danh sách từ tải dần, Giao tiếp đưa chip tình huống lên đầu, Câu thường dùng gọn, thanh ghim nền đặc, báo offline, khung chờ AI, rung, vùng chạm 44px, bàn phím không che ô nhập.
- 09/2026 **v1.21.1**: cập nhật tại chỗ mượt — không chạy lại hiệu ứng/không nhảy đầu trang (`viewTop`, `onceCls`, `.main.enter`).
- 09/2026 **v1.21.0 (Đợt C)**: thuật ngữ Nhật, SRS câu, chọn đáp theo vai + cá nhân hoá JD, sự kiện, podcast, hỏi nhanh (nút ?), AI phân tích phát âm, ảnh chia sẻ PNG, cache AI + luật ngữ pháp offline, test vào repo, CSP khi tự host.
- 09/2026 **v1.20.0 (Đợt B)**: Standup 60 giây, Dịch ngược, biểu đồ tiến bộ, game ưu tiên từ hay sai + log đấu thoại, showcase 1.6 MB → 44 KB, badge icon.
- 09/2026 **v1.19.0 (Đợt A)**: chống chèn HTML (esc/cleanWord), sao lưu/khôi phục, script tự copy data sang game, meta/OG.

- 09/2026 (v1.18.1): app — màn "chào mừng trở lại" khi vắng >24h (tóm tắt thời gian vắng,
  trạng thái streak, nút "Học nhanh 2 phút giữ streak"), thẻ "Mochi đang giữ N xu" ở trang
  Hôm nay đọc từ localStorage game để kéo người dùng sang chơi Game.
- 09/2026: game hoàn thiện mobile-first (map 1 màn, Nói/Shop/Hồ sơ gọn, màn chơi kiểu chat, AFK giãn + Mochi nói câu đã học, sheet có ✕, chuyển cảnh mượt).
- Game: tab Nói (Đấu thoại AI, Đọc theo nhịp, Chuyện văn phòng VN, Phản xạ 5s, Trang bị Mochi), AFK idle, Shop, nhập AI key trong game.
- Game khởi tạo: RPG map + quiz battle + boss VN; app v1.18.0 thêm nút "🎮 IT English Quest".
- Favicon logo cho app + showcase; showcase: CTA thẻ kính, nền đen mặc định, particle-net, fullpage scroll, chữ chạy.
- App v1.17.x: "Nghe hết" hội thoại có xướng vai, header Giao tiếp 1 hàng, video demo.

## 9. Ý tưởng còn mở (chưa làm)

📋 **Việc để sau: [`docs/BACKLOG.md`](docs/BACKLOG.md)** (kiểm tra trình độ 3 phút, tiếng Nhật công sở làm ngôn ngữ chính, lớp học doanh nghiệp, ngành mới…).

✅ **v3.0 đa ngành** đã làm (D0–D5 trong [`docs/DINH-HUONG-DA-NGANH-2026-09-20.md`](docs/DINH-HUONG-DA-NGANH-2026-09-20.md)). Tiếp theo có thể: gói Logistics · Tài chính · Marketing–TMĐT · Y tế; nhờ người trong nghề đọc duyệt nội dung các gói mới; thêm tiếng Nhật cho câu mẫu.

Đợt A/B/C trong [`docs/REVIEW-2026-09-20.md`](docs/REVIEW-2026-09-20.md) **đã làm xong** (v1.19–1.21, xem mục "Trạng thái" cuối file đó). Còn lại:

- **G3** thêm boss/nhân vật, kết cục mới cho Chuyện văn phòng.
- **E7** bài đọc ký hiệu kỹ thuật.
- **K4 / E16** backend/proxy giữ key + đồng bộ đa thiết bị (chỉ khi có người dùng thật ngoài chủ repo).
- Podcast: SpeechSynthesis dừng khi khoá màn hình trên iOS — cân nhắc ghi sẵn audio.
- Mở rộng `ja_data.py` cho câu thường dùng; thêm vai trò (Designer, Data).
