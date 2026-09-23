# Nghiên cứu tính năng mới — Nói Nghề (23/09/2026)

> Phạm vi: giữ chân người học · nội dung & ngành mới · lớp học & xã hội · so sánh đối thủ.
> Nền: app v3.1 (`main`) + backend v4.0 (nhánh `feature/backend-v4`: tài khoản khách/Google, đồng bộ, AI qua server, thống kê).
> Ước lượng tính bằng **phiên làm việc với Claude** như các đợt trước. Nguồn ở cuối mỗi mục.

---

> **Trạng thái (23/09):** đã làm **đợt B** (B1–B5) và phần chạy trên máy của A3 + A6 (lá chắn cuối tuần, sửa chuỗi, chúc mừng, ngày hoàn hảo) — nhánh `feature/noi-tot-hon`, test `tests/j.mjs`. A1/A2/A4/A5 (Web Push, giờ nhắc thích ứng, kéo người vắng) chờ bật máy chủ v4.0.

## 0. Kết luận nhanh

1. **Việc đáng làm nhất là giữ chân người học, và phần lớn cần backend v4.0.** Nhắc học hiện là thông báo cục bộ, chỉ chạy khi app đang mở. **Web Push qua Supabase** là điều kiện để các cơ chế giữ chân khác có tác dụng.
2. **Phần Giao tiếp AI đã mạnh.** Đã có gợi ý cách trả lời, nhận xét cuối buổi, câu AI sửa đưa vào ôn SRS. Chỗ còn thiếu so với đối thủ tốt nhất (Langua, ELSA) là **khép vòng**: buổi chat sau phải *cố ý* dùng lại từ đang ôn. Ngoài ra còn thiếu **chấm phát âm tô màu từng từ** và **phân tích bản ghi bài nói thật**.
3. **Lớp học nên làm bản tối thiểu**: mã lớp, bảng xếp hạng tuần, người tạo lớp chỉ xem số tổng hợp. Chưa nên bán B2B cho công ty Nhật. Thị trường có thật nhưng chu kỳ bán hàng quá dài với một người làm; trước hết làm 1 pilot miễn phí để lấy case study.
4. **Tiếng Nhật: làm lớp trung gian, chưa làm nhánh đầy đủ.** Lớp trung gian gồm furigana, giọng đọc `ja-JP`, romaji và một module kính ngữ nơi làm việc. Đây là phép thử nhu cầu rẻ, chưa phải xây app thứ hai.
5. **Đừng bắt chước "năng lượng giới hạn lượt học" của Duolingo.** Cũng đừng dùng giọng dọa, gây tội lỗi khi nhắc học. "Miễn phí, không quảng cáo, không giới hạn lượt" là điểm khác biệt thật, nên nói to.

**Lộ trình đề xuất:**

| Đợt | Nội dung | Phiên |
|---|---|---|
| **A · Giữ chân** (sau khi bật v4.0) | Web Push + giờ nhắc thích ứng · sửa chuỗi + lá chắn cuối tuần · chúc mừng nối chuỗi · kéo người vắng ngày 1–4 · xin quyền đúng lúc + hướng dẫn cài iOS | ≈ 2,5 |
| **B · Nói tốt hơn** | Chat dùng lại từ đang ôn · chạm từ xem nghĩa trong hội thoại · phát âm tô màu từng từ · phân tích bản ghi thật · 3 chế độ phỏng vấn/họp/thuyết trình dùng chung mọi ngành | ≈ 2,5 |
| **C · Cùng nhau** | Mã lớp + bảng xếp hạng tuần theo nhóm nhỏ + màn người tạo lớp · học cặp với đồng nghiệp | ≈ 2,5 |
| **D · Nội dung** | Kiểm tra trình độ 3 phút · lớp tiếng Nhật trung gian · 2 ngành mới | ≈ 3 |

Tổng ≈ 10,5 phiên. Đợt A và C cần v4.0 đã bật. Đợt B và D chạy được cả khi không có máy chủ.

---

## 1. Hiện trạng: app đã có gì (để không làm trùng)

| Nhóm | Đã có |
|---|---|
| Thói quen | Việc hôm nay (4 việc ~10 phút) · chuỗi ngày (tăng khi có **bất kỳ** hoạt động nào — đã là ngưỡng thấp) · đóng băng chuỗi (tối đa 2, tích từ lượt học) · tổng kết Chủ nhật · heatmap · biểu đồ tiến bộ · nhắc học cục bộ (chỉ khi app mở/quay lại tab) · chào mừng trở lại khi vắng >24h |
| Nói | Giao tiếp AI theo ngành + vai · **Gợi ý cách trả lời** giữa buổi · nhận xét cuối buổi · câu AI sửa → vào SRS câu (`psrsFromFix`) · Báo cáo 60 giây có chấm · rảnh tay · shadowing · AI phân tích phát âm |
| Nội dung | 9 ngành × 120 ngày (IT 370) · "Nghề của tôi" do AI tạo · ảnh → bài học · podcast · đọc hiểu · dịch ngược · thuật ngữ tiếng Nhật (chỉ nghĩa phụ) |
| Game | RPG bản đồ ngày, boss AI, xu AFK, huy hiệu |
| Máy chủ (v4.0) | Tài khoản, đồng bộ, AI có hạn mức, bảng `daily_activity`/`attempts_daily`, báo lỗi |

**Chưa có:** push thật, sửa chuỗi, bảng xếp hạng, bạn học, lớp học, chấm phát âm từng từ, phân tích bản ghi tải lên, kiểm tra trình độ, tiếng Nhật làm ngôn ngữ học.

---

## 2. Giữ chân người học

Số liệu chính đều từ nhóm tăng trưởng của Duolingo, nguồn công khai có đo A/B:

- **Tách chuỗi khỏi mục tiêu ngày** (1 bài là giữ chuỗi): +3,3% giữ chân ngày 14, +19% người mới có chuỗi. Người đạt chuỗi 7 ngày hoàn thành khoá **nhiều gấp 3,6 lần**. Hiệu ứng chúc mừng khi nối chuỗi: +1,7% giữ chân ngày 7 với người mới. ([Improving the streak](https://blog.duolingo.com/improving-the-streak/), [streak & habit](https://blog.duolingo.com/how-duolingo-streak-builds-habit/))
- **Cược chuỗi 7 ngày**: +14% ngày 7. **Lá chắn cuối tuần**: +4% quay lại sau 1 tuần, −5% mất chuỗi. Lượng người học mỗi ngày tụt 5–10% vào cuối tuần. ([Duolingo Streaks](https://blog.duolingo.com/how-streaks-keep-duolingo-learners-committed-to-their-language-goals/))
- **Giờ nhắc**: nhắc vào **23,5 giờ sau lần học đầu tiên hôm trước** hiệu quả hơn giờ người dùng tự chọn. Kéo người vắng hiệu quả nhất trong **3–4 ngày đầu**; sau ~7 ngày thì nên dừng. Tối ưu nội dung thông báo bằng thuật toán chỉ thêm ~2% ngày 7, tức nhắc đúng lúc quan trọng hơn câu chữ. ([Sub Club – Duolingo](https://subclub.com/episode/how-to-time-reactivation-campaigns-for-maximum-impact-jackson-shuttleworth-duolingo), [Yancey & Settles, KDD 2020](https://research.duolingo.com/papers/yancey.kdd20.pdf))
- **Bảng xếp hạng (league)**: +1/+2/+3% giữ chân ngày 1/7/14, **+17% thời gian học**. Đây là tính năng xã hội có hiệu ứng lớn nhất. ([Lenny's Newsletter](https://www.lennysnewsletter.com/p/the-secret-to-duolingos-growth))
- **Mặt trái**: nghiên cứu ACM L@S 2022 ghi nhận lo âu, tội lỗi, gian lận điểm và mất tự tin khi game hoá bị lạm dụng. Nguyên nhân là những cú hích thao túng (dark nudge) và bảng xếp hạng không công bằng. ([Lu & Ou 2022](https://arxiv.org/pdf/2203.16175))
- **Web Push trên PWA (2026)**:
  - iOS cần 16.4+ và **phải cài ra màn hình chính**. Hộp xin quyền chỉ được bật khi người dùng vừa bấm. Không có đồng bộ nền. Dữ liệu có thể bị xoá sau ~7 ngày không mở.
  - Android/Chrome đầy đủ, không cần cài.
  - Supabase làm được bằng Edge Function + `pg_cron`.
  - ([Pushpad](https://pushpad.xyz/blog/ios-special-requirements-for-web-push-notifications), [MagicBell](https://www.magicbell.com/blog/pwa-ios-limitations-safari-support-complete-guide), [Supabase schedule](https://supabase.com/docs/guides/functions/schedule-functions))

### Đề xuất (xếp theo lợi / công)

| # | Tính năng | Làm gì trong Nói Nghề | Công | Rủi ro / lưu ý |
|---|---|---|---|---|
| A1 | **Web Push thật** | Bảng `push_subscriptions` (VAPID) · Edge Function `send-reminders` · `pg_cron` 15 phút/lần · service worker nhận `push`. Thay nhắc cục bộ (giữ làm dự phòng khi không có máy chủ) | 1 | iOS chỉ chạy khi đã cài ra màn hình chính → cần A5 |
| A2 | **Giờ nhắc thích ứng** | Lưu giờ học đầu tiên mỗi ngày (đã có `daily_activity`, thêm cột `first_at`) → nhắc lúc +23,5h, kẹp trong 6:00–22:00. Người dùng vẫn đặt được giờ cố định | 0,3 | Tối đa **1 push/ngày**/người |
| A3 | **Sửa chuỗi + lá chắn cuối tuần** | Đứt chuỗi → trong 48h được sửa **1 lần/tháng**, trả bằng xu game (xu AFK có chỗ dùng có ích). Tuần học ≥5 ngày → tự có lá chắn Thứ Bảy | 0,4 | Sửa miễn phí vô hạn thì chuỗi mất ý nghĩa |
| A4 | **Kéo người vắng ngày 1–4** | Nhánh trong cron: N1 "chuỗi còn nguyên, 1 việc 2 phút" · N2 "đã dùng đóng băng" · N4 "bài nghe 1 phút ngành bạn" → **ngày 7 im hẳn** | 0,3 | Không dùng giọng dọa, gây tội lỗi |
| A5 | **Xin quyền đúng lúc + hướng dẫn cài** | Chỉ hỏi bật nhắc **sau khi xong ngày học đầu tiên** · trên iPhone hiện hướng dẫn "Thêm vào màn hình chính" (có ảnh) trước khi hỏi | 0,3 | Hỏi sớm dễ bị từ chối, mà từ chối thì không hỏi lại được |
| A6 | **Chúc mừng nối chuỗi + "ngày hoàn hảo"** | Hoạt ảnh nhẹ khi việc đầu tiên trong ngày nối chuỗi · đếm riêng ngày làm đủ 4 việc | 0,2 | Tôn trọng `prefers-reduced-motion` |
| A7 | **Cam kết 7 ngày (tuỳ chọn)** | Cược 50 xu: học đủ 7 ngày nhận 100 | 0,3 | Chỉ khi người dùng tự bật; thua chỉ mất xu cược |
| A8 | **Tổng kết tuần gửi ra ngoài app** | Tổng kết Chủ nhật sẵn có → push (hoặc email qua Resend khi đã có Google): tuần này vs tuần trước + 1 việc gợi ý | 0,3 | Tuần không học thì chỉ gửi 1 câu |
| A9 | **Chỉ số "học thật" nội bộ** | Admin theo dõi phút nói + câu đúng ngay lần đầu, song song chuỗi/xu (Duolingo phải tạo "Time Spent Learning Well" vì chỉ đo engagement thì tối ưu nhầm hướng) | 0,2 | Không hiện cho người học |

**Không làm:** giới hạn năng lượng/tim · bảng xếp hạng toàn cầu, tính từ trước tới nay, có rớt hạng ở bậc thấp nhất · nhắc quá 7 ngày cho người đã bỏ · đổ thêm công vào xu AFK trước khi làm A1–A4. Xu AFK không sinh thêm phút nói tiếng Anh.

---

## 3. So sánh đối thủ — tính năng đáng học

| Đối thủ | Điểm mạnh người dùng khen | Nói Nghề |
|---|---|---|
| **Langua** | Báo cáo sau hội thoại rất kỹ; từ sai trong chat → flashcard → **buổi sau ép dùng lại** | Có nhận xét + câu sửa vào SRS; **thiếu bước "ép dùng lại"** |
| **ELSA Speak** | Chấm **từng âm vị** xanh/vàng/đỏ, trọng âm, ngữ điệu; phân tích bài nói tải lên (từ đệm, tốc độ); 50+ ngành | Có AI phân tích phát âm dạng chữ; **thiếu tô màu + phân tích bản ghi thật** |
| **Duolingo Max** | Video call với nhân vật Lily; Adventures (tình huống có cốt truyện, sai thì nhân vật "lái" lại); DuoRadio | Có podcast + boss AI trong game; **thiếu nhân vật cố định**, nhiệm vụ công sở có cốt truyện |
| **Memrise MemBot** | Xin gợi ý/dịch giữa chừng, "không phải bài thi" | **Đã có** "Gợi ý cách trả lời" |
| **Loora / Speak** | Kịch bản phỏng vấn, họp, thuyết trình | Có chặng phỏng vấn trong lộ trình; **thiếu chế độ luyện riêng dùng chung mọi ngành** |
| **Praktika** | Avatar AI | Bị chê "kỳ quặc", không có chế độ chỉ âm thanh, không có SRS → **đừng làm avatar 3D** |
| **Cake** | Clip người thật, miễn phí, rất phổ biến ở VN | Vướng bản quyền video → bỏ qua |

Nguồn: [Langua – so sánh AI apps](https://languatalk.com/blog/whats-the-best-ai-for-language-learning/), [Praktika review](https://languatalk.com/blog/praktika-review/), [ELSA](https://www.aitools-directory.com/tools/elsa-speak-speaking-pronunciation-coach/), [Duolingo Adventures & Video Call](https://lingoly.io/duolingo-adventures-video-call/), [MemBot](https://www.memrise.com/blog/introducing-membot), [Talkio 2026](https://www.talkio.ai/blog/best-ai-language-speaking-practice-apps-in-2026), [Cake](https://fptshop.com.vn/tin-tuc/dien-may/ung-dung-cake-hoc-tieng-anh-hoan-toan-mien-phi-cai-thien-giao-tiep-nhanh-chong-174249), [Duolingo energy](https://duoplanet.com/duolingo-energy-system/).

### Đề xuất

| # | Tính năng | Làm gì | Công |
|---|---|---|---|
| B1 | **Chat dùng lại từ đang ôn** | Trước mỗi buổi Giao tiếp AI, lấy 5–8 từ/câu SRS **đến hạn hoặc hay sai** → đưa vào prompt ("dẫn dắt để người học dùng các cụm này"). Cuối buổi đánh dấu cụm nào đã dùng đúng → tính như một lần ôn "tốt" | 0,5 |
| B2 | **Chạm từ xem nghĩa trong hội thoại** | Chạm từ/câu trong lượt AI nói → nghĩa tiếng Việt + ví dụ (tra từ điển gói ngành trước, không có mới gọi AI, có cache) · "Lưu vào Của tôi" một chạm · cho phép gõ tiếng Việt khi bí → AI đưa câu tiếng Anh | 0,5 |
| B3 | **Phát âm tô màu từng từ** | Bản nhận giọng nói so với câu mẫu (`wordMatch` sẵn có) → mỗi từ xanh/vàng/đỏ; chạm từ đỏ → nghe mẫu chậm + IPA. Không cần model âm vị riêng | 0,5 |
| B4 | **Phân tích bài nói thật** | Ghi âm (≤2 phút) phần phát biểu họp thật → nhận giọng nói → AI đếm từ đệm, tốc độ (từ/phút), 3 lỗi + bản nói lại tự nhiên hơn. **Không lưu ghi âm** (chỉ xử lý trên máy + gửi văn bản) | 0,6 |
| B5 | **3 chế độ phỏng vấn / họp / thuyết trình** | Tình huống AI dùng chung mọi ngành, tham số theo `who()` + vai; có thang chấm riêng (cấu trúc STAR cho phỏng vấn, mở–thân–kết cho thuyết trình) | 0,4 |
| B6 | Nhân vật cố định theo ngành *(cân nhắc)* | Mỗi ngành 1–2 nhân vật 2D tĩnh có tên, tính cách, **nhớ những gì đã nói ở buổi trước** (tóm tắt 3 dòng lưu lại) — ví dụ "anh Tanaka, trưởng phòng người Nhật" | 0,5 |
| B7 | Nhiệm vụ công sở có cốt truyện *(cân nhắc)* | Nâng boss của game thành chuỗi nhiệm vụ: xin nghỉ phép → báo trễ deadline → xin lỗi khách; sai thì nhân vật dẫn lại bằng lời thoại. Công chủ yếu là viết nội dung | 1+ |
| B8 | Ước lượng trình độ quy về TOEIC *(cân nhắc)* | Điểm nội bộ từ SRS + điểm nói + nghe, ghi rõ "ước lượng" | 0,3 |

---

## 4. Nội dung & ngành mới

| # | Việc | Ghi chú | Công |
|---|---|---|---|
| D1 | **Kiểm tra trình độ 3 phút** (backlog #1) | Nghe 3 câu + nói 2 câu → xếp ngày bắt đầu; **bỏ qua được** (bằng chứng: đừng bắt làm bài kiểm tra dài ở màn làm quen, cái giữ người dùng là làm được 1 việc thật trong 2 phút đầu). Kèm câu hỏi "bạn thường học lúc nào?" — vừa là cam kết cụ thể "khi… thì…" (implementation intention, hiệu ứng d≈0,65), vừa là giờ nhắc ban đầu cho A2 ([meta-analysis](https://www.tandfonline.com/doi/abs/10.1080/10463283.2024.2334563)) | 0,5 |
| D2 | **Lớp tiếng Nhật trung gian** | `<ruby>` furigana + romaji + giọng `ja-JP` cho các từ đã có nghĩa tiếng Nhật; module nhỏ **kính ngữ & cụm cố định nơi làm việc** (chào, xin phép, báo cáo, họp). **Tiền xử lý khi build** (kuromoji/MeCab trong `packs_src`) → runtime 0 KB thư viện. Nhận giọng `ja-JP` chạy trên Chrome/Android, iOS Safari 14.5+; không có trên Firefox/Edge | 1–1,5 |
| D3 | 2 ngành mới | Xây dựng · Kỹ thuật, Hàng không (hoặc Giáo dục) — quy trình sẵn: agent viết → agent kiểm duyệt → build | 1 |
| — | Tiếng Nhật đầy đủ *(chưa nên)* | Viết lại nội dung 9 ngành bằng tiếng Nhật, kanji, kính ngữ theo thứ bậc ≈ **xây app thứ hai**. Chỉ làm khi D2 cho thấy nhiều người bật dùng | 5+ |

**Nhu cầu tiếng Nhật:**

- JLPT 7/2025 có 911.918 người đăng ký, **+14,9%**, là kỷ lục ([JLPT](https://www.jlpt.jp/about/pdf/2025julypr.pdf)).
- Việt Nam có 164.495 người học tiếng Nhật ([Japan Foundation 2024](https://www.jpf.go.jp/e/project/japanese/survey/result/information.html)).
- Trình duyệt: kuromoji.js cần từ điển ~4 MB, TinySegmenter ~25 KB nhưng không cho cách đọc ([kuromoji](https://github.com/takuyaa/kuromoji.js), [caniuse speech](https://caniuse.com/speech-recognition)).

---

## 5. Lớp học, xã hội, doanh nghiệp

**Cơ chế nào có tác dụng:**

- Bảng xếp hạng: +17% thời gian học, số người học "rất chăm" gấp 3.
- Tin nhắn từ bạn bè kéo người vắng quay lại tốt hơn mọi thông báo của app.
- Không có tác dụng: bộ đếm lượt kiểu game (trung tính), giới thiệu bạn (+3%).
- Chấm bài chéo và chat nhóm tốn công kiểm duyệt, lại cần lớp đủ đông mới "sống".
- ([Lenny's – Duolingo](https://www.lennysnewsletter.com/p/how-duolingo-reignited-user-growth), [Friend Streak](https://blog.duolingo.com/product-lessons-friend-streak/), [Duolingo for Schools](https://duolingoschools.zendesk.com/hc/en-us/articles/6892701653261-What-are-student-privacy-settings-and-how-can-I-adjust-them))

| # | Tính năng | Làm gì | Công |
|---|---|---|---|
| C1 | **Mã lớp + bảng xếp hạng tuần** | `classes`, `class_members` · vào lớp bằng RPC `join_class(code)` · điểm tuần tổng hợp bằng `pg_cron` (không truy vấn thời gian thực) · **biệt danh** thay tên thật · rời lớp bất cứ lúc nào · chỉ Google mới tạo được lớp (khách vào được) | 1 |
| C2 | **Màn người tạo lớp** | Chỉ **số tổng hợp**: ngày học tuần này, số việc, lần học gần nhất, ngành. **Không** cho xem câu trả lời, lỗi, ghi âm · xuất CSV | 0,5 |
| C3 | **Bảng xếp hạng nhóm nhỏ theo ngành** | Nhóm ~20 người cùng ngành, gần trình độ; bậc thấp nhất không rớt hạng; tắt được | 0,6 |
| C4 | **Học cặp với đồng nghiệp** | Link mời → chuỗi chung + nút "nhắc bạn" (1 push/ngày, đi qua A1) | 0,5 |

**Pháp lý khi người khác xem dữ liệu học viên** (Luật BVDLCN 2025 + NĐ 356/2025):

- **Đồng ý:** phải có đồng ý riêng khi vào lớp. Không tick sẵn, và phải lưu lại thời điểm đồng ý.
- **Thời hạn:** xử lý yêu cầu xoá trong 20 ngày. Nút xoá tài khoản đã có từ v4.0.
- **Ghi âm và dữ liệu hành vi:** không lưu ghi âm gắn với danh tính, không cho người tạo lớp xem chi tiết hành vi. Hai điều này giữ app trong diện **ân hạn 5 năm cho doanh nghiệp nhỏ** (dưới 100.000 hồ sơ, không xử lý dữ liệu nhạy cảm).
- **Máy chủ ở Singapore:** cần hồ sơ đánh giá chuyển dữ liệu ra nước ngoài. Công ty Nhật chắc chắn sẽ hỏi.
- *(Tham khảo, không phải tư vấn pháp lý.)*
- ([Vietnam Briefing](https://www.vietnam-briefing.com/news/vietnam-personal-data-protection-regulation-decree-356.html/), [EY](https://www.ey.com/en_vn/technical/tax/tax-and-law-updates/legal-alert-march-2026-decree-no-356-2025-nd-cp-providing-detailed-guidance-for-implementation-of-personal-data-protection-law), [Acclime](https://vietnam.acclime.com/news-insights/decree-356-turning-personal-data-protection-into-operational-obligations/))

**B2B công ty Nhật — chưa bán, nên chuẩn bị:**

- **Thị trường:**
  - Nhật có 5.512 dự án FDI tại VN, đứng thứ 3.
  - 67,5% doanh nghiệp Nhật báo lãi năm 2025, cao nhất từ 2009.
  - **48,2% nói tuyển người ngày càng khó**, nên bài toán nâng cấp người đang có là điểm đau thật.
  - ([LSQ Osaka](https://vnconsulate-osaka.org/en/node/494), [Báo Đầu tư – JETRO](https://baodautu.vn/nam-2025-675-doanh-nghiep-nhat-ban-dau-tu-tai-viet-nam-bao-lai-cao-nhat-ke-tu-nam-2009-d502336.html))
- **Giá đang trả:** tiếng Anh doanh nghiệp 3–10 triệu/người/khoá, workshop 10–45 triệu/buổi ([Optimus](https://optimus.edu.vn/bang-gia-dao-tao-tieng-anh-doanh-nghiep/), [MDT](https://www.mdttraining.vn/post/what-does-corporate-training-cost-in-vietnam-in-2026)).
- **Rào cản:**
  - Cần pháp nhân và hoá đơn VAT.
  - Duyệt nội bộ kiểu Nhật (稟議) chậm và cần tài liệu tiếng Nhật.
  - Phải qua kiểm tra bảo mật.
  - Công ty sợ người làm một mình bỏ dở sản phẩm.
- **Đường đi thực tế:** C1 + C2 → 1 pilot miễn phí với 1 công ty → case study → hợp tác với trung tâm đào tạo đã có hợp đồng, hoặc qua JCCI/JCCH. Chỉ lập pháp nhân và bảng giá khi có ≥2 công ty chủ động hỏi mua.

---

## 6. Giá tham khảo (nếu sau này cần thu tiền)

- **Giá niêm yết:** ELSA Premium 1 năm **799k** (gốc 2,7 triệu), Pro 1 năm 495k, trọn đời 3,3 triệu. Thực tế luôn giảm 50–70% ([ELSA VN](https://vn.elsaspeak.com/bao-gia-hoc-phi-elsa-speak/)).
- **Chợ tài khoản "nâng cấp":** ELSA ~360k, Duolingo Super ~220k/năm.
- **Mức người Việt sẵn lòng trả cho app học: ~200k–800k/năm**, xấp xỉ 1/5 giá quốc tế. Gói năm hoặc trọn đời bán chạy hơn thuê bao tháng.
- **Đối thủ đang siết bản miễn phí:** Duolingo giới hạn năng lượng, ELSA miễn phí 5 bài/ngày, Speak không có bản miễn phí.
- Vì vậy vị thế **miễn phí, không quảng cáo, không giới hạn lượt** (AI dùng key riêng hoặc hạn mức nhỏ) là lợi thế cạnh tranh thật.
- Nếu cần bù chi phí AI: gói "AI không giới hạn" theo năm, 199k–299k (bậc `ai_tier = 'plus'` đã có sẵn trong schema v4.0). Hoặc B2B theo đầu người.

---

## 7. Việc cụ thể cho phiên tới

1. **Bật v4.0** (điền `cloud-config.js`, dựng project theo `docs/BACKEND.md`). Đợt A và C phụ thuộc vào việc này.
2. **Nếu chưa bật máy chủ**: làm **B1 + B2 + B3** trước (≈ 1,5 phiên, chạy không cần máy chủ). Đây là phần tăng chất lượng nói rõ nhất so với đối thủ.
3. Sau khi bật: **A1 + A2 + A5** (≈ 1,6 phiên) → **A3 + A4 + A6** (≈ 0,9) → đo lại giữ chân ngày 1/7/30 bằng `admin_stats`.
4. Chuẩn bị C1/C2 song song với việc tìm 1 công ty Nhật chịu dùng thử.
