# IT English — App luyện tiếng Anh IT cơ bản

Ứng dụng web cá nhân giúp luyện tiếng Anh chuyên ngành IT / môi trường làm việc:
lộ trình 370 ngày theo chủ đề, 1000 câu thường dùng, ôn từ vựng theo SRS,
luyện nghe (chép chính tả + shadowing chấm phát âm), và trò chuyện AI theo tình huống.

## Công nghệ

Web thuần một file, **không framework, không build tool**:

- `index.html` — toàn bộ giao diện + logic (HTML + CSS + JavaScript thuần).
- `data.gen.js` — dữ liệu bài học 370 ngày (sinh từ `gen_data.py`).
- `phrases.gen.js` — 1000 câu thường dùng (sinh từ `phrases_data.py`).

Bên trong trình duyệt dùng: Web Speech API (đọc tiếng Anh + chấm phát âm qua mic),
`localStorage` (lưu tiến độ, streak, SRS), font Google (Bricolage Grotesque +
Hanken Grotesk + IBM Plex Mono). Có chế độ sáng / tối / theo hệ thống.

## Chạy

Mở trực tiếp `index.html` bằng trình duyệt, hoặc chạy một web server tĩnh:

```bash
python3 -m http.server 8000
# rồi mở http://localhost:8000
```

## Trò chuyện AI

Phần **Giao tiếp → Trò chuyện AI** hiện gọi Claude qua `window.claude.use('sample')`,
chỉ hoạt động khi mở app bên trong claude.ai. Khi chạy ngoài (host tĩnh, mở file
trực tiếp), phần này tự hiển thị thông báo và các tính năng còn lại vẫn chạy đầy đủ.

> TODO (sau): thay bằng Claude API dùng API key riêng (cần backend nhỏ để giữ key,
> không đặt key trực tiếp trong `index.html`).

## Sinh lại dữ liệu

```bash
python3 gen_data.py      # -> data.gen.js  (cần phases_extra.py)
python3 phrases_data.py  # -> phrases.gen.js
```

## Push lên git

```bash
git init
git add .
git commit -m "IT English app"
git branch -M main
git remote add origin <URL_REPO_CUA_BAN>
git push -u origin main
```
