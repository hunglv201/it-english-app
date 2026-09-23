# Kiểm duyệt `packs_src/extra/factory.py` (v4.1, 2026-09-23)

Đã soát toàn bộ: 8 chặng (80 từ, 74 câu mẫu, 40 hội thoại, 48 bài nghe), 16 câu dịch ngược, 5 bài đọc (10 câu hỏi), 4 AI, 3 sự kiện, 6 quips, 4 vai (8 tình huống, 16 hội thoại). `python3 packs_src/build.py factory` chạy qua.

## Lỗi đã sửa (5)
- [Số liệu] Hội thoại "What's the diameter of this hole?": "It's 8 millimetres, plus 0.05, minus 0. I checked it on revision D." (mâu thuẫn với bài nghe/bài đọc: Rev. D = 8,2 mm ±0,05) → "It's 8.2 millimetres, plus or minus 0.05. I checked it on revision D."
- [Số liệu] Câu sai đi kèm: "Hole is 8." / "'The hole is 8 millimetres.'" → "Hole is 8.2." / "'The hole is 8.2 millimetres.'"
- [Tiếng Anh] "…so it's 0.03 over. It's NG." (NG là từ kiểu Nhật, người bản xứ không nói) → "…so it's 0.03 over. It's out of tolerance."
- [Tiếng Việt] Ví dụ "recycle": "Tụi mình tái chế toàn bộ khay nhựa." → "Nhà máy mình tái chế toàn bộ khay nhựa."
- [Tiếng Nhật] "PLC": bỏ シーケンサ/shīkensa (là nhãn hiệu đăng ký của một hãng, dù hay dùng như từ chung) → tuple 6 phần tử.

## Tiếng Nhật đã bỏ
- PLC — シーケンサ (shīkensa): lý do nhãn hiệu, xem trên. Các từ còn lại (寸法, ノギス, 限界ゲージ, 面粗さ, 受入検査, ミルシート, 先入れ先出し, 出荷検査, 設備総合効率, 時間稼働率, 性能稼働率, 工数, 手直し, 朝礼, 引き継ぎ, 点呼, 非常停止, ティーチングペンダント…) dùng thật, romaji khớp.
