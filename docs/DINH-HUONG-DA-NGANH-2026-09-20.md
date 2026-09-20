# Định hướng: từ "IT English" sang tiếng Anh công việc đa ngành, cá nhân hoá

> Nghiên cứu 20/09/2026 · app đang ở v2.0.0.
> ✅ **Trạng thái: đã triển khai trong v3.0.0 (20/09/2026)** — chủ repo chọn: mặc định *Công sở chung*, 3 gói Khách sạn · Bán hàng · Nhà máy, đổi tên thành **Nói Nghề**. "Ngành khác" làm gọn: dùng gói Công sở + JD (AI tạo tình huống + 12 từ riêng) thay cho gói mini riêng.
> Câu hỏi: app không chỉ cho IT mà cho nhiều ngành, nhiều đối tượng; có cá nhân hoá; **nếu người dùng không chọn gì thì vẫn vào app mặc định được**.

**Trả lời ngắn: làm được, và nên làm theo kiểu "lõi chung + gói ngành".** Ai bỏ qua bước chọn thì vào ngay gói *Công sở chung*.
Người dùng cũ tự động giữ gói IT nên không mất tiến độ. Cách tổ chức hiện tại (dữ liệu sinh bằng Python, gói vai trò, cá nhân hoá theo JD, AI theo tình huống)
đã có sẵn gần đủ khung. Việc lớn nhất là **viết nội dung cho từng ngành**, còn code thì không khó.

---

## 1. Bối cảnh & bằng chứng

| Quan sát | Nguồn | Ý nghĩa cho app |
|---|---|---|
| Thị trường học tiếng Anh online VN ≈ 43 triệu USD (2025), tăng ~12%/năm tới 2034. Động lực chính là AI cá nhân hoá, học trên điện thoại và **nhu cầu của người đi làm** | IMARC | Người đi làm là tệp khách đang lớn, không chỉ dân IT |
| ~50% người VN học tiếng Anh để **thăng tiến/xin việc**. Kỹ năng muốn cải thiện nhất là **nói** | Q&Me (khảo sát cũ nhưng xu hướng vẫn đúng) | Thế mạnh "nói theo tình huống công việc" của app dùng được cho mọi ngành |
| Ngành tuyển mạnh nhờ FDI 2026: sản xuất/bán dẫn, năng lượng xanh, công nghệ/AI, tài chính, **logistics**, **TMĐT/bán lẻ**. Các vị trí này đều cần tiếng Anh | Reeracoen VN 2026 | Chọn các gói ngành đầu tiên theo danh sách này |
| Duolingo hỏi mục tiêu và trình độ ngay đầu, nhưng **cho học trước rồi mới bắt đăng ký**. Ai không muốn thi xếp lớp thì vào thẳng bài 101 | Appcues GoodUX | Onboarding ngắn, câu nào cũng bỏ qua được, luôn có đường vào mặc định |
| Praktika: bộ nhớ dài hạn (mục tiêu, lỗi hay mắc) giúp **tăng 24% giữ chân ngày 1** | OpenAI case study | Cá nhân hoá theo hành vi đáng làm hơn là hỏi thật nhiều ở onboarding |
| Speak, Duolingo, Memrise gần như không cá nhân hoá theo nghề. Loora có kịch bản công sở chung. Praktika cho tải tài liệu riêng lên | Issen 2026 | **Còn khoảng trống**: tiếng Anh *theo đúng ngành*, bằng tiếng Việt, có chấm lỗi. Đây là lợi thế nếu làm sâu từng ngành chứ không làm "chung chung" |

⚠️ **Phản biện:** "IT English" đang mạnh vì *rất ngách*. Nếu mở ra đa ngành mà thành app "tiếng Anh giao tiếp" chung chung thì sẽ đụng Duolingo/ELSA
và mất điểm khác biệt. Vì vậy mỗi gói ngành phải sâu như gói IT hiện tại (từ vựng, câu mẫu, hội thoại, đoạn họp, tình huống AI riêng),
chứ không chỉ đổi mỗi câu lệnh gửi AI.

---

## 2. Mô hình sản phẩm: 4 lớp cá nhân hoá

```
Lớp 0  Mặc định (không chọn gì)   → gói "Công sở chung", A2, ngày 1
Lớp 1  Chọn NGÀNH                 → gói ngành: từ vựng, chặng, hội thoại, bài nghe, tình huống AI
Lớp 2  Chọn VAI + MỤC TIÊU        → ưu tiên chặng, tình huống, người AI đóng vai (khách, sếp, đối tác…)
Lớp 3  Dán JD / mô tả công việc   → AI tạo tình huống + 20–30 từ riêng (mở rộng tính năng JD hiện có)
Lớp 4  Học từ hành vi             → từ hay sai, tình huống hay luyện, lỗi hay mắc (đã có một phần: SRS, game ưu tiên từ sai)
```

Mỗi lớp đều không bắt buộc. Người dùng có thể dừng ở lớp 0 mà app vẫn đầy đủ tính năng.

### Đối tượng & gói đề xuất (ưu tiên cho thị trường VN)

| # | Gói | Ví dụ vai | Người AI đóng vai | Ưu tiên |
|---|---|---|---|---|
| 0 | 🏢 **Công sở chung** (mặc định) | nhân viên văn phòng | đồng nghiệp, sếp | **Bắt buộc** |
| 1 | 💻 IT & phần mềm (hiện có) | Dev, QA, DevOps, BA, PM, Designer, Data | đồng nghiệp, khách hàng nước ngoài | Có sẵn |
| 2 | 🏨 Khách sạn · nhà hàng · du lịch | lễ tân, phục vụ, hướng dẫn viên | khách nước ngoài | Cao |
| 3 | 🎧 Bán hàng · CSKH · call center | sale, CS, telesales | khách hàng qua điện thoại/chat | Cao |
| 4 | 🏭 Sản xuất · nhà máy FDI | QA/QC, kỹ sư, tổ trưởng | chuyên gia nước ngoài, auditor | Cao |
| 5 | 🚚 Logistics · xuất nhập khẩu | chứng từ, mua hàng, kho | forwarder, nhà cung cấp | Vừa |
| 6 | 💰 Tài chính · ngân hàng · kế toán | kế toán, giao dịch viên, kiểm toán | khách hàng, auditor | Vừa |
| 7 | 📣 Marketing · TMĐT | marketer, vận hành shop | agency, đối tác, KOL | Vừa |
| 8 | 🩺 Y tế · điều dưỡng | điều dưỡng, lễ tân phòng khám | bệnh nhân nước ngoài | Sau |
| 9 | 🎓 Sinh viên · đi tìm việc | ứng viên | nhà tuyển dụng | Vừa (dùng được chặng Phỏng vấn) |
| ✎ | **Ngành khác** (tự gõ) | bất kỳ | AI tự chọn | Làm bằng AI, không cần viết tay |

Tiếng Nhật đi kèm (thuật ngữ Nhật cạnh từ tiếng Anh) nên giữ như một **tuỳ chọn độc lập với ngành**, vì người làm cho công ty Nhật có mặt ở mọi ngành.

---

## 3. Onboarding: cho phép bỏ qua, luôn có đường vào mặc định

```
Mở app lần đầu
 ├─ Màn 1: "Bạn dùng tiếng Anh cho công việc gì?"   [lưới 9 ô ngành + "Ngành khác…"]
 │         nút phụ: "Bỏ qua — học tiếng Anh công sở chung ›"   ← MẶC ĐỊNH
 ├─ Màn 2 (nếu đã chọn ngành): vai trong ngành (chip) · bỏ qua được
 └─ Màn 3: trình độ (màn xếp lớp hiện có: Mới / Cơ bản / Khá) · bỏ qua = A2, ngày 1
→ Vào "Hôm nay" ngay, không cần đăng ký (app vốn không có tài khoản)
```

Quy tắc đề xuất:
- **Tối đa 3 màn, màn nào cũng bỏ qua được.** Bỏ qua ở màn 1 là vào luôn gói *Công sở chung*, cấp A2, ngày 1.
- **Hỏi dần sau đó (progressive profiling):** sau ngày học thứ 3, thẻ nhỏ trên *Hôm nay* hỏi "Bạn làm ngành gì? Bài sẽ sát công việc hơn". Tắt được và không hiện lại.
- Đổi ngành bất cứ lúc nào ở **Tôi › Cá nhân hoá**. Tiến độ, streak, SRS từ, câu đã lưu **giữ nguyên**, chỉ lộ trình và gợi ý thay đổi.
- **Người dùng cũ** (đã có dữ liệu `it-english-v1`) được gán `track:'it'` nên không bị hỏi lại và không mất gì.
- Link chia sẻ theo ngành để đưa đúng người: `?track=hotel` sẽ chọn sẵn gói (dùng cho trang giới thiệu hoặc gửi bạn bè).

---

## 4. Thiết kế kỹ thuật

### 4.1 Dữ liệu: lõi + gói, tải khi cần

```
data/core.gen.js           # Công sở chung: ~12 chặng, 150 từ, câu, hội thoại, đoạn họp, tình huống AI
data/packs/it.gen.js       # nội dung IT hiện tại (37 chặng) chuyển sang
data/packs/hotel.gen.js    # mỗi gói ~40–80 KB
...
packs_src/<id>.py          # nguồn Python cho từng gói (giống content_extra.py / roles_data.py)
```

Schema mỗi gói (mở rộng từ `ROLES` + `DATA` hiện có):

```js
PACK = { id:'hotel', label:'Khách sạn · du lịch', emoji:'🏨',
  persona:{ me:'a hotel front-desk receptionist', them:'a foreign guest' },   // dùng cho mọi prompt AI
  roles:{ reception:{label,emoji,scenarios[],dialogues[]}, … },
  vocab[], phaseTitles[], days-plan, phrases groups[], dialogues[], listen[] (có đoạn p:1),
  aiScenarios[{k,l,s}], jaTerms? }
```

- **Lộ trình ghép lúc chạy**: chặng của gói ngành xen kẽ chặng lõi (ví dụ 2 chặng ngành, 1 chặng lõi: email, họp, phỏng vấn, hành chính).
  Gói IT giữ nguyên 370 ngày. Gói mới bắt đầu khoảng 12 chặng × 10 ngày, cộng lõi là ~200 ngày, sau đó mở rộng dần.
- **Tải gói bằng `<script>` động** + service worker cache gói đang dùng, nên vẫn chạy offline. App chỉ tải lõi và gói đã chọn, không tăng dung lượng lần đầu.
- **Game** đọc gói đang chọn (chung key `store.cfg.track`). Bản đồ ngày lấy theo lộ trình đã ghép.

### 4.2 Chỗ trong code đang "cứng" theo IT (phải gỡ)

| Chỗ | Hiện tại | Sửa |
|---|---|---|
| Câu lệnh gửi AI | 17 chỗ ghi "Vietnamese (software) developer" | hàm `persona()` sinh từ gói + vai + JD |
| `AI_SCENARIOS` | tình huống dev cố định | lấy từ gói (`aiScenarios`) + vai |
| Standup 60s | chỉ hợp với dev | đổi thành "Báo cáo nhanh 60s": standup / bàn giao ca / báo cáo sale, tuỳ gói |
| Chữ trên giao diện, tên app, icon, OG | "IT English", "phòng tập nói cho dev" | tên chung + tên gói hiện ở header |
| `ROLES` | 7 vai IT | chuyển vào `packs/it` |
| Cá nhân hoá JD | chỉ chọn vai IT + chặng IT | AI chọn **ngành + vai**, gợi ý chuyển gói |

### 4.3 "Ngành khác": gói mini do AI tạo

Người dùng gõ "dược sĩ bệnh viện" hoặc "kỹ sư xây dựng", AI tạo gói mini trong một lần gọi: 30 từ (kèm IPA, nghĩa Việt, ví dụ), 6 tình huống AI, 10 câu mẫu, persona.
Gói này lưu localStorage, vào lộ trình dưới dạng 3 chặng ngắn ghép với lõi. Có nhãn *"AI tạo, chưa kiểm duyệt"*; người dùng báo lỗi được và tạo lại được.
Cách này phủ được phần đuôi dài các ngành mà không phải viết tay tất cả.

---

## 5. Kế hoạch & ước lượng

Đơn vị là **phiên làm việc với Claude** (1 phiên ≈ 1 lượt "làm đi" như các đợt A/B/C trước).

| Đợt | Nội dung | Ước lượng | Kết quả thấy được |
|---|---|---|---|
| **D0 – Nền tảng** | Tách `DATA` thành lõi + `packs/it`, trình tải gói, `persona()` cho 17 prompt, `store.cfg.track` + chuyển dữ liệu người dùng cũ, test | 1 phiên | App y như cũ với người dùng IT, nhưng đã sẵn sàng thêm ngành |
| **D1 – Onboarding & mặc định** | 3 màn đều bỏ qua được, gói *Công sở chung* làm mặc định, Tôi › Cá nhân hoá, thẻ hỏi sau ngày 3, `?track=` | 0,5 phiên | Mục tiêu của yêu cầu này: không chọn thì vẫn vào app |
| **D2 – Nội dung lõi** | Công sở chung: 12 chặng, 150 từ, 40 hội thoại, 30 bài nghe/đoạn họp, 10 tình huống AI | 1 phiên | Người không chọn ngành có lộ trình tử tế |
| **D3 – 3 gói ưu tiên** | Khách sạn–du lịch, Bán hàng–CSKH, Sản xuất FDI (mỗi gói 12 chặng, 120 từ, 36 hội thoại, 24 nghe, 8 tình huống, 3–4 vai) | 0,5–1 phiên/gói | 4 ngành đầy đủ (IT + 3) |
| **D4 – Ngành khác (AI)** | Tạo gói mini, lưu, báo lỗi | 0,5 phiên | Phủ mọi ngành còn lại |
| **D5 – Thương hiệu & showcase v3** | Tên mới, icon, trang giới thiệu v3 (v2 vào lưu trữ, theo quy ước version lớn), game theo gói | 1 phiên | Ra mắt **v3.0** |
| Sau đó | Logistics, Tài chính, Marketing, Y tế, Sinh viên | 0,5–1 phiên/gói | Mở rộng dần |

**Tổng cho bản v3.0 (D0–D5): khoảng 5–6 phiên.** Nên làm theo thứ tự D0 → D1 → D2 trước, vì chỉ riêng ba đợt này đã đáp ứng được
"nhiều đối tượng + không chọn thì vào mặc định", sau đó mới thêm gói ngành.

---

## 6. Rủi ro & cách giảm

| Rủi ro | Giảm thiểu |
|---|---|
| Nội dung ngành mới kém sâu, sai thuật ngữ | Viết bằng file Python kiểm tra được (đáp án xáo, ô trống có thật, không trùng); mỗi gói có test schema; ưu tiên ngành mình hiểu rõ; nhờ người trong ngành đọc thử 1 chặng |
| Mất định vị ngách, thành app chung chung | Mỗi gói có tên, màu, persona riêng; trang giới thiệu nói rõ "tiếng Anh **theo đúng ngành của bạn**" |
| Người dùng IT hiện tại bị xáo trộn | Tự gán `track:'it'`, test hồi quy a–f phải qua 100% |
| Dung lượng / offline | Chỉ tải lõi + gói đang chọn; SW cache theo gói |
| Chi phí AI tăng (gói mini, persona dài) | Cache AI hiện có; gói mini chỉ tạo 1 lần |
| Không đo được hiệu quả (web tĩnh, không analytics) | Thống kê cục bộ (ngành được chọn, tỉ lệ bỏ qua onboarding), người dùng tự xem ở Tôi; có thể xuất khi cần |

---

## 7. Cần anh quyết định

1. **Gói mặc định khi bỏ qua:** *Công sở chung* (khuyên dùng, đúng định hướng đa ngành) hay giữ *IT* (nhanh hơn, không cần D2)?
2. **3 gói ngành làm trước:** đề xuất Khách sạn–du lịch · Bán hàng–CSKH · Sản xuất FDI.
3. **Tên app mới** khi bỏ chữ "IT" (ví dụ *WorkTalk English*, *Nói Tiếng Anh Công Việc*…) hoặc giữ tên, chỉ thêm gói.

## Nguồn

- [IMARC — Vietnam Digital English Language Learning Market](https://www.imarcgroup.com/vietnam-digital-english-language-learning-market)
- [Q&Me — English study practices in Vietnam](https://qandme.net/en/report/English-study-practices-in-Vietnam.html)
- [Reeracoen Vietnam — Xu hướng tuyển dụng 2026](https://www.reeracoen.com.vn/en/articles/xu-huong-tuyen-dung-viet-nam-2026-nganh-nao-se-dan-dau-khi-fdi-tang)
- [Appcues GoodUX — Duolingo onboarding](https://goodux.appcues.com/blog/duolingo-user-onboarding)
- [OpenAI — Inside Praktika's conversational approach](https://openai.com/index/praktika/)
- [Issen — Personalized language apps (05/2026)](https://www.issen.com/blog/best-personalized-language-learning-apps/)
