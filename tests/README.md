# Test mobile (Playwright)

Chạy toàn bộ: `tests/run.sh` (tự bật server tĩnh cổng 8765). Ảnh chụp lưu ở `tests/shots/` (không commit).

| File | Kiểm tra |
|---|---|
| `a.mjs` | Đợt A — T1 chống chèn HTML từ AI/người dùng, làm sạch “Của tôi”, K1 sao lưu/khôi phục |
| `b.mjs` | Đợt B — Standup 60s, Dịch ngược, biểu đồ tiến bộ, game ưu tiên từ hay sai, log đấu thoại, showcase tải ảnh |
| `d.mjs` | Cập nhật tại chỗ không chạy lại hiệu ứng / không nhảy lên đầu trang; chỉ khi vào màn mới |
| `c.mjs` | Đợt C — tiếng Nhật, SRS câu, chọn đáp theo vai, cá nhân hoá JD, sự kiện, podcast, hỏi nhanh, ảnh chia sẻ, cache AI + luật ngữ pháp offline, game theo vai |

`lib.mjs`: viewport 375×667, chặn Google Fonts, giả `speechSynthesis`, giả AI qua `window.claude.use('sample')` (hàm `ai`/`aiJson` truyền vào), nạp sẵn `localStorage`.
Biến môi trường: `BASE_URL`, `CHROMIUM_PATH`, `PLAYWRIGHT_MODULE`, `SHOTS_DIR`.
Mỗi test in `ERRORS: none` khi không có lỗi JS/console.
