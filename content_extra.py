# -*- coding: utf-8 -*-
# v2.0 — nội dung bổ sung theo chặng (index = thứ tự trong PHASES + EXTRA).
# Mỗi chặng: +3 hội thoại chọn đáp, +2 bài nghe dạng ĐOẠN (2–3 câu, như đoạn họp thật).
# Hội thoại: (câu đồng nghiệp, [(câu trả lời, đúng?, phản hồi tiếng Việt) x3]) — thứ tự đáp án được xáo khi sinh dữ liệu.
# Bài nghe đoạn: (đoạn văn, [từ cần điền], gợi ý) — từ cần điền đứng giữa câu, không dính dấu ? ! '
C = {
0: {  # Công việc hằng ngày
 "dialogues": [
  ("What are you working on today?", [
    ("I'm fixing the search bug, then I'll review two PRs.", True, "Nêu việc chính + việc tiếp theo, đúng thì."),
    ("I working on search bug.", False, "Thiếu 'am': I'm working on…"),
    ("Today search, bug, review.", False, "Chỉ liệt kê từ, không thành câu.")]),
  ("Can you pick up this ticket?", [
    ("Sure, I can start after lunch.", True, "Nhận việc + mốc thời gian cụ thể."),
    ("Yes pick up.", False, "Cụt, lặp lại câu hỏi."),
    ("I can starting after lunch.", False, "Sau 'can' dùng động từ nguyên mẫu: I can start.")]),
  ("When will it be ready?", [
    ("It should be ready by Thursday afternoon.", True, "'should be ready by + thời điểm' — cách hẹn tự nhiên."),
    ("It ready Thursday.", False, "Thiếu động từ 'will be / should be'."),
    ("Maybe soon, I don't know when.", False, "Mơ hồ, không cho mốc thời gian.")]),
 ],
 "listen": [
  ("Morning everyone. Yesterday I finished the login page. Today I will start on the payment API.", ["finished", "login", "payment"], "standup buổi sáng"),
  ("I moved the ticket to in progress. It is bigger than we thought, so I need one more day.", ["ticket", "bigger", "more"], "cập nhật tiến độ"),
 ]},
1: {  # Git & quản lý mã
 "dialogues": [
  ("Did you push your branch?", [
    ("Not yet. I'll push it after I fix the tests.", True, "Trả lời trung thực + khi nào làm."),
    ("I didn't pushed it.", False, "Sau 'didn't' dùng nguyên mẫu: didn't push."),
    ("Push no, test fail.", False, "Không thành câu.")]),
  ("There's a merge conflict in the config file.", [
    ("I'll resolve it and ping you when it's done.", True, "Nhận xử lý + báo lại."),
    ("Conflict is not my fault.", False, "Phòng thủ, không giải quyết vấn đề."),
    ("I resolve it yesterday.", False, "Sai thì: I resolved it / I'll resolve it.")]),
  ("Which branch should I use for the hotfix?", [
    ("Please branch off main and name it hotfix/login-error.", True, "Chỉ dẫn rõ nhánh gốc + cách đặt tên."),
    ("Use any branch you like.", False, "Dễ gây lộn xộn repo."),
    ("Branch main hotfix name.", False, "Lủng củng, thiếu động từ.")]),
 ],
 "listen": [
  ("Please pull the latest changes before you start. I merged a big refactor this morning.", ["latest", "merged", "refactor"], "nhắc pull code mới"),
  ("My commit broke the build. I reverted it, and I will push a fixed version after lunch.", ["broke", "reverted", "fixed"], "báo lỗi build"),
 ]},
2: {  # Code review
 "dialogues": [
  ("Why did you use a global variable here?", [
    ("Good point. I'll move it into the service class.", True, "Tiếp nhận góp ý + cách sửa."),
    ("Because it works.", False, "Phòng thủ, không giải thích lý do kỹ thuật."),
    ("I use because easy.", False, "Sai thì và thiếu chủ ngữ phụ.")]),
  ("Could you split this PR into smaller ones?", [
    ("Sure. I'll separate the UI changes from the API changes.", True, "Đồng ý + nêu cách chia cụ thể."),
    ("No, it's fine like this.", False, "Từ chối không lý do."),
    ("I can split but not today maybe.", False, "Mơ hồ, lủng củng.")]),
  ("I left a few comments on your PR.", [
    ("Thanks! I'll go through them this afternoon.", True, "Cảm ơn + hẹn thời gian xử lý."),
    ("Why so many comments?", False, "Nghe có vẻ khó chịu."),
    ("Thanks, I read tomorrow.", False, "Sai thì: I'll read them tomorrow.")]),
 ],
 "listen": [
  ("The logic looks good to me. Just one small thing: please rename this function so it is easier to read.", ["logic", "rename", "easier"], "góp ý review"),
  ("I approved your pull request. Feel free to merge it after the tests pass.", ["approved", "merge", "tests"], "duyệt PR"),
 ]},
3: {  # Test & lỗi
 "dialogues": [
  ("The test is failing on CI but passing locally.", [
    ("It might be a timezone issue. Let me check the CI settings.", True, "Đưa giả thuyết + hành động tiếp."),
    ("It works on my machine.", False, "Câu đùa kinh điển, không giải quyết gì."),
    ("CI is wrong always.", False, "Đổ lỗi, sai trật tự từ.")]),
  ("Can you add a test for this edge case?", [
    ("Yes, I'll add one for an empty list too.", True, "Đồng ý + nghĩ thêm trường hợp liên quan."),
    ("Edge case never happen.", False, "Chủ quan, sai ngữ pháp (happens)."),
    ("I add test later maybe.", False, "Mơ hồ, sai thì.")]),
  ("How did you find this bug?", [
    ("A user reported it, and I reproduced it on staging.", True, "Kể lại rõ nguồn và cách tái hiện."),
    ("I find it by luck.", False, "Sai thì: I found it."),
    ("Bug come from user.", False, "Thiếu chia động từ và mạo từ.")]),
 ],
 "listen": [
  ("I can reproduce the bug on staging. It only happens when the cart is empty, so it is an edge case.", ["reproduce", "empty", "edge"], "mô tả bug"),
  ("Three tests are failing after your change. Could you take a look before the end of the day?", ["failing", "change", "end"], "báo test fail"),
 ]},
4: {  # Deploy & môi trường
 "dialogues": [
  ("Is it safe to deploy now?", [
    ("Yes, all checks passed and QA signed off.", True, "Trả lời kèm bằng chứng."),
    ("I think yes maybe.", False, "Thiếu tự tin, không có căn cứ."),
    ("Deploy is safe always.", False, "Chủ quan, sai trật tự từ.")]),
  ("Production is showing an error after the release.", [
    ("Let's roll back first, then investigate.", True, "Ưu tiên khôi phục dịch vụ trước."),
    ("It worked on staging.", False, "Không giúp xử lý sự cố."),
    ("Wait, I check code slowly.", False, "Chậm và sai ngữ pháp.")]),
  ("Which environment are you testing on?", [
    ("On the staging environment with production data.", True, "Nêu rõ môi trường + dữ liệu."),
    ("On environment.", False, "Không rõ môi trường nào."),
    ("I testing on stage.", False, "Thiếu 'am', dùng sai tên môi trường.")]),
 ],
 "listen": [
  ("We will deploy at five today. Please do not merge anything into main until the release is done.", ["deploy", "merge", "release"], "thông báo deploy"),
  ("The new version is on staging now. QA will test it tomorrow, and we plan to go live on Friday.", ["staging", "test", "live"], "lịch release"),
 ]},
5: {  # Cơ sở dữ liệu
 "dialogues": [
  ("This query is really slow.", [
    ("We should add an index on the user_id column.", True, "Chỉ ra nguyên nhân + giải pháp cụ thể."),
    ("Database is slow, not my query.", False, "Đổ lỗi, không phân tích."),
    ("Query slow because many data.", False, "Sai ngữ pháp: a lot of data.")]),
  ("Did you back up the table before the migration?", [
    ("Yes, I took a backup ten minutes ago.", True, "Xác nhận + thời điểm."),
    ("Backup is not needed.", False, "Rủi ro mất dữ liệu."),
    ("Yes I backup it.", False, "Sai thì: I backed it up.")]),
  ("Can I delete these old records?", [
    ("Please check with the data team first.", True, "Thận trọng với dữ liệu, hỏi đúng người."),
    ("Sure, delete everything.", False, "Nguy hiểm, không kiểm tra."),
    ("You can deleting it.", False, "Sau 'can' dùng nguyên mẫu.")]),
 ],
 "listen": [
  ("The migration adds a new column to the orders table. It takes about two minutes, so we will run it at night.", ["migration", "column", "night"], "kế hoạch migration"),
  ("I found duplicate records in the customer table. I will write a script to clean them up.", ["duplicate", "script", "clean"], "dọn dữ liệu"),
 ]},
6: {  # API & tích hợp
 "dialogues": [
  ("The API returns a 500 error.", [
    ("Let me check the server logs to find the cause.", True, "Hành động điều tra hợp lý."),
    ("It's the client's problem.", False, "Đổ lỗi khi chưa kiểm tra."),
    ("API error, I don't know.", False, "Không có hướng xử lý.")]),
  ("Can you share the API documentation?", [
    ("Sure, I'll send you the Swagger link.", True, "Đồng ý + cụ thể."),
    ("Documentation is in my head.", False, "Không có tài liệu — tệ cho team."),
    ("Yes, I share you.", False, "Thiếu tân ngữ: I'll share it with you.")]),
  ("Do we have a rate limit on this endpoint?", [
    ("Yes, 100 requests per minute per user.", True, "Trả lời bằng con số cụ thể."),
    ("Maybe some limit.", False, "Mơ hồ."),
    ("Limit is have.", False, "Sai ngữ pháp.")]),
 ],
 "listen": [
  ("The partner API changed its response format. Our integration is broken, so I am updating the parser now.", ["response", "integration", "parser"], "API đối tác đổi"),
  ("Please send the token in the header, not in the URL. It is safer and the logs will not show it.", ["token", "header", "safer"], "hướng dẫn gọi API"),
 ]},
7: {  # Họp & trao đổi
 "dialogues": [
  ("Can everyone see my screen?", [
    ("Yes, we can see it clearly.", True, "Xác nhận ngắn gọn, lịch sự."),
    ("Yes see.", False, "Cụt, thiếu chủ ngữ."),
    ("I can seeing it.", False, "Sau 'can' dùng nguyên mẫu.")]),
  ("Sorry, could you repeat that?", [
    ("Sure. I said the release will move to next Monday.", True, "Nhắc lại rõ ý chính."),
    ("I already said it.", False, "Thiếu kiên nhẫn."),
    ("Release move Monday.", False, "Thiếu động từ, khó hiểu.")]),
  ("Do we need a follow-up meeting?", [
    ("I think a quick 15-minute sync on Thursday is enough.", True, "Đề xuất cụ thể, tôn trọng thời gian."),
    ("Yes, a long meeting every day.", False, "Không hợp lý."),
    ("Meeting need, maybe.", False, "Lủng củng.")]),
 ],
 "listen": [
  ("Let's get started. Today we have three topics: the release date, the new design, and the budget.", ["started", "release", "budget"], "mở đầu cuộc họp"),
  ("To sum up, Linh will update the design, and I will send the meeting notes by this afternoon.", ["sum", "design", "notes"], "tóm tắt cuộc họp"),
 ]},
8: {  # Sự cố & vướng mắc
 "dialogues": [
  ("Are you stuck on something?", [
    ("Yes, I can't connect to the test database. Do you have a minute?", True, "Nêu rõ vướng mắc + nhờ giúp lịch sự."),
    ("No, everything is perfect.", False, "Giấu vấn đề làm chậm cả team."),
    ("Yes stuck database.", False, "Không thành câu.")]),
  ("How long has the service been down?", [
    ("About twenty minutes. We are restarting it now.", True, "Thời lượng + hành động hiện tại."),
    ("Long time.", False, "Không có thông tin."),
    ("It down since morning.", False, "Thiếu động từ: It has been down since…")]),
  ("Who should I escalate this to?", [
    ("Please contact the on-call engineer first, then the team lead.", True, "Chỉ đúng thứ tự leo thang."),
    ("Escalate to everyone.", False, "Gây ồn ào, không hiệu quả."),
    ("You escalate me.", False, "Sai cấu trúc: escalate it to me.")]),
 ],
 "listen": [
  ("I am blocked by a permission issue. I cannot access the server logs, so I cannot check the error.", ["blocked", "permission", "logs"], "báo bị chặn"),
  ("The site was down for fifteen minutes. We found the root cause and added an alert so it does not happen again.", ["down", "cause", "alert"], "báo cáo sự cố"),
 ]},
9: {  # Kế hoạch & ước lượng
 "dialogues": [
  ("How long will this feature take?", [
    ("About three days, including tests.", True, "Ước lượng + phạm vi."),
    ("Very fast, no problem.", False, "Không cho con số."),
    ("It take three days.", False, "Sai chia động từ: It will take.")]),
  ("Can we finish this before the sprint ends?", [
    ("Only if we move the export feature to the next sprint.", True, "Nêu điều kiện/đánh đổi."),
    ("Of course, easy.", False, "Hứa quá mức."),
    ("Finish maybe no.", False, "Lủng củng.")]),
  ("What are the risks for this plan?", [
    ("The main risk is the payment API. It isn't stable yet.", True, "Chỉ ra rủi ro chính + lý do."),
    ("No risks at all.", False, "Không thực tế."),
    ("Risk is many.", False, "Sai ngữ pháp, không cụ thể.")]),
 ],
 "listen": [
  ("I estimate five days for this task. Two days for the backend, two for the frontend, and one for testing.", ["estimate", "backend", "testing"], "chia ước lượng"),
  ("We are behind schedule by two days. I suggest we cut the report feature from this release.", ["behind", "suggest", "release"], "báo trễ tiến độ"),
 ]},
10: {  # Bảo mật cơ bản
 "dialogues": [
  ("I got a strange email asking for my password.", [
    ("Don't click anything. Please forward it to the security team.", True, "Hướng dẫn an toàn và đúng quy trình."),
    ("Just reply with your password.", False, "Rất nguy hiểm — lừa đảo phishing."),
    ("Maybe it is real, try.", False, "Chủ quan, có rủi ro.")]),
  ("Can I put the API key in the code?", [
    ("No, please use environment variables instead.", True, "Chuẩn bảo mật: không hard-code secret."),
    ("Yes, it's easier.", False, "Lộ secret khi push code."),
    ("Key in code is ok for me.", False, "Sai về bảo mật.")]),
  ("Did you enable two-factor authentication?", [
    ("Yes, I set it up yesterday.", True, "Xác nhận + thời điểm."),
    ("No, it's annoying.", False, "Thiếu ý thức bảo mật."),
    ("Yes I enable yesterday.", False, "Sai thì: I enabled it.")]),
 ],
 "listen": [
  ("We found a vulnerability in an old library. Please update it today and do not deploy before the patch.", ["vulnerability", "update", "patch"], "cảnh báo lỗ hổng"),
  ("Never share your password in chat. If you think someone knows it, change it right away.", ["share", "chat", "change"], "nhắc bảo mật"),
 ]},
11: {  # Cloud & hạ tầng
 "dialogues": [
  ("Why is our cloud bill so high this month?", [
    ("We forgot to stop some test servers. I'll shut them down today.", True, "Nguyên nhân + hành động."),
    ("Cloud is always expensive.", False, "Không phân tích."),
    ("Bill high because server many.", False, "Sai ngữ pháp.")]),
  ("Should we scale up before the campaign?", [
    ("Yes, let's add two more instances and enable auto-scaling.", True, "Đề xuất cụ thể."),
    ("No need, it will be fine.", False, "Chủ quan với lưu lượng lớn."),
    ("Scale yes maybe.", False, "Mơ hồ.")]),
  ("Which region is the server in?", [
    ("It's in Tokyo, close to our users.", True, "Trả lời + lý do."),
    ("Somewhere in Asia.", False, "Không chính xác."),
    ("Server is Tokyo region in.", False, "Sai trật tự từ.")]),
 ],
 "listen": [
  ("Traffic will double during the sale. We should add more instances and check the database connections.", ["double", "instances", "connections"], "chuẩn bị tải cao"),
  ("The storage is almost full. I will move old files to cheaper storage and set a cleanup rule.", ["storage", "cheaper", "rule"], "dọn lưu trữ"),
 ]},
12: {  # Frontend & giao diện
 "dialogues": [
  ("The button looks broken on mobile.", [
    ("I'll fix the layout for small screens.", True, "Nhận lỗi + cách sửa."),
    ("It's fine on my laptop.", False, "Bỏ qua người dùng mobile."),
    ("Mobile is not important.", False, "Sai ưu tiên sản phẩm.")]),
  ("Can we change the color to match the design?", [
    ("Sure, I'll use the color from the design system.", True, "Đúng quy trình dùng design system."),
    ("I like my color more.", False, "Không theo thiết kế chung."),
    ("Change color is hard.", False, "Không đúng sự thật, lủng củng.")]),
  ("The page takes a long time to load.", [
    ("The images are too big. I'll compress them and use lazy loading.", True, "Chẩn đoán + giải pháp."),
    ("Users can wait.", False, "Không quan tâm trải nghiệm."),
    ("Page slow, I don't know.", False, "Không có hướng xử lý.")]),
 ],
 "listen": [
  ("The new form is ready for review. I added validation for the email field and a loading state for the button.", ["form", "validation", "loading"], "báo xong form"),
  ("On small screens the menu overlaps the title. I will fix the breakpoint and test it on iPhone.", ["overlaps", "breakpoint", "test"], "lỗi giao diện mobile"),
 ]},
13: {  # Hiệu năng & tối ưu
 "dialogues": [
  ("Why is the dashboard so slow?", [
    ("It loads all data at once. We should add pagination.", True, "Nguyên nhân + giải pháp."),
    ("Because the server is old.", False, "Đoán không có căn cứ."),
    ("Dashboard slow always.", False, "Không phân tích.")]),
  ("Did the cache help?", [
    ("Yes, response time dropped from two seconds to 200 milliseconds.", True, "Trả lời bằng số liệu trước/sau."),
    ("Yes, faster a little maybe.", False, "Mơ hồ."),
    ("Cache help very.", False, "Sai ngữ pháp.")]),
  ("Where is the bottleneck?", [
    ("It's in the report query. It scans the whole table.", True, "Chỉ ra điểm nghẽn cụ thể."),
    ("Everywhere.", False, "Không có thông tin."),
    ("Bottleneck is at database maybe I think.", False, "Lủng củng, không chắc chắn.")]),
 ],
 "listen": [
  ("I profiled the page. Most of the time is spent in one query, so I will add an index and cache the result.", ["profiled", "query", "cache"], "phân tích hiệu năng"),
  ("After the change, memory usage went down by forty percent. The server is much more stable now.", ["memory", "forty", "stable"], "kết quả tối ưu"),
 ]},
14: {  # Logging & giám sát
 "dialogues": [
  ("Why didn't we get an alert?", [
    ("The threshold was too high. I'll lower it to 5% errors.", True, "Nguyên nhân + điều chỉnh cụ thể."),
    ("Alerts are useless.", False, "Tiêu cực, không giải quyết."),
    ("Alert no come.", False, "Sai ngữ pháp.")]),
  ("Can you add more logs to this function?", [
    ("Sure, I'll log the request ID and the response time.", True, "Nêu rõ log gì."),
    ("Logs are too much already.", False, "Từ chối không lý do."),
    ("I add logs everything.", False, "Log mọi thứ gây nhiễu, sai ngữ pháp.")]),
  ("Is the error rate normal now?", [
    ("Yes, it's back under 1% since noon.", True, "Số liệu + thời điểm."),
    ("I think normal.", False, "Không kiểm chứng."),
    ("Error rate is down go.", False, "Sai ngữ pháp.")]),
 ],
 "listen": [
  ("Please check the dashboard before each release. If the error rate goes above two percent, stop the deploy.", ["dashboard", "error", "stop"], "quy trình giám sát"),
  ("I added a request ID to every log line. Now we can trace one request across all services.", ["request", "trace", "services"], "cải thiện log"),
 ]},
15: {  # Docker & container
 "dialogues": [
  ("The container keeps restarting.", [
    ("It runs out of memory. Let's raise the limit to 1 GB.", True, "Nguyên nhân + cách sửa."),
    ("Just restart it again.", False, "Không xử lý gốc rễ."),
    ("Container restart many time.", False, "Sai ngữ pháp.")]),
  ("Why is the image so big?", [
    ("It includes the build tools. A multi-stage build will make it smaller.", True, "Giải thích + giải pháp."),
    ("Big images are normal.", False, "Không tối ưu."),
    ("Image big because.", False, "Câu chưa hoàn chỉnh.")]),
  ("How do I run the app locally?", [
    ("Just run docker compose up, and open port 3000.", True, "Hướng dẫn ngắn gọn, đủ bước."),
    ("It's difficult, ask someone else.", False, "Không hỗ trợ đồng nghiệp."),
    ("You run docker and it go.", False, "Mơ hồ, sai ngữ pháp.")]),
 ],
 "listen": [
  ("I updated the Dockerfile to use a smaller base image. The build is faster and the image is half the size.", ["Dockerfile", "base", "half"], "tối ưu image"),
  ("The service cannot connect to the database because the port is not exposed. Please check the compose file.", ["connect", "port", "compose"], "lỗi container"),
 ]},
16: {  # CI/CD
 "dialogues": [
  ("The pipeline failed again.", [
    ("It's a flaky test. I'll fix it and rerun the pipeline.", True, "Chẩn đoán + hành động."),
    ("Just skip the tests.", False, "Nguy hiểm cho chất lượng."),
    ("Pipeline fail always.", False, "Không có hướng xử lý.")]),
  ("Can we deploy automatically after merge?", [
    ("Yes, to staging. Production should still need approval.", True, "Tự động có kiểm soát."),
    ("Yes, straight to production.", False, "Rủi ro cao."),
    ("Deploy auto maybe yes.", False, "Mơ hồ.")]),
  ("How long does the build take?", [
    ("About eight minutes. Caching could cut it to three.", True, "Con số + đề xuất cải thiện."),
    ("Long.", False, "Không có thông tin."),
    ("Build take eight minute.", False, "Sai chia động từ và số nhiều.")]),
 ],
 "listen": [
  ("The pipeline has four stages: build, test, security scan, and deploy. Each stage must pass before the next one starts.", ["four", "scan", "pass"], "giải thích pipeline"),
  ("I added caching to the build step. Now the pipeline takes five minutes instead of twelve.", ["caching", "five", "instead"], "cải thiện CI"),
 ]},
17: {  # Agile & Scrum
 "dialogues": [
  ("What went well this sprint?", [
    ("We shipped the checkout flow on time, and the code reviews were faster.", True, "Cụ thể, có kết quả."),
    ("Everything, as always.", False, "Không có thông tin để học hỏi."),
    ("Sprint good.", False, "Quá chung chung.")]),
  ("How many story points is this?", [
    ("I'd say five. The API part is still unclear.", True, "Ước lượng + lý do."),
    ("One hundred.", False, "Không thực tế."),
    ("Point is five maybe I think.", False, "Lủng củng.")]),
  ("Can we add this to the current sprint?", [
    ("Let's discuss it with the product owner first.", True, "Tôn trọng quy trình Scrum."),
    ("Yes, add everything.", False, "Làm vỡ sprint."),
    ("Add sprint now.", False, "Không thành câu.")]),
 ],
 "listen": [
  ("In this retrospective, let's talk about what went well, what did not, and one thing we will change next sprint.", ["retrospective", "change", "sprint"], "mở đầu retro"),
  ("Our velocity dropped this sprint because two people were sick. We should plan fewer points next time.", ["velocity", "sick", "fewer"], "phân tích velocity"),
 ]},
18: {  # Onboarding & học việc
 "dialogues": [
  ("Do you have everything you need for your first week?", [
    ("Almost. I still don't have access to the staging server.", True, "Nêu rõ thứ còn thiếu."),
    ("Yes, I know everything already.", False, "Thiếu khiêm tốn, không thực tế."),
    ("I need access maybe something.", False, "Mơ hồ.")]),
  ("Is there anything you want to ask?", [
    ("Yes, who should I ask about the deployment process?", True, "Câu hỏi cụ thể, hữu ích."),
    ("No, nothing.", False, "Bỏ lỡ cơ hội học hỏi."),
    ("Who deploy ask?", False, "Sai trật tự từ.")]),
  ("How is your setup going?", [
    ("Good. The app runs locally, but some tests fail.", True, "Tiến độ + vấn đề còn lại."),
    ("Setup is hard, I give up.", False, "Tiêu cực."),
    ("Setup go good.", False, "Sai ngữ pháp.")]),
 ],
 "listen": [
  ("Welcome to the team. This week, please set up your laptop, read the onboarding guide, and fix one small bug.", ["Welcome", "guide", "small"], "chào đón người mới"),
  ("Your mentor is Minh. If you have questions, ask him in the team channel, not in private messages.", ["mentor", "questions", "channel"], "giới thiệu mentor"),
 ]},
19: {  # Tài liệu kỹ thuật
 "dialogues": [
  ("Where can I find the setup guide?", [
    ("It's in the README, under 'Getting started'.", True, "Chỉ đúng chỗ, cụ thể."),
    ("Somewhere in the wiki.", False, "Mơ hồ."),
    ("Guide is not exist.", False, "Sai ngữ pháp: doesn't exist.")]),
  ("The documentation is out of date.", [
    ("Thanks for noticing. I'll update it this week.", True, "Cảm ơn + nhận việc."),
    ("Nobody reads docs anyway.", False, "Tiêu cực."),
    ("I update docs someday.", False, "Mơ hồ, sai thì.")]),
  ("Can you add a diagram to explain the flow?", [
    ("Sure, I'll draw a sequence diagram for the login flow.", True, "Đồng ý + loại sơ đồ cụ thể."),
    ("The code explains itself.", False, "Không hỗ trợ người đọc."),
    ("Diagram is difficult draw.", False, "Sai ngữ pháp.")]),
 ],
 "listen": [
  ("I rewrote the API section of the documentation. Each endpoint now has an example request and response.", ["rewrote", "endpoint", "example"], "cập nhật tài liệu"),
  ("Before you merge, please update the changelog. Write one line about what changed and why.", ["changelog", "changed", "why"], "quy tắc changelog"),
 ]},
20: {  # Kiến trúc hệ thống
 "dialogues": [
  ("Why did we choose this architecture?", [
    ("It lets each team deploy independently.", True, "Nêu lợi ích chính."),
    ("Because it's popular.", False, "Lý do yếu."),
    ("Architecture good for us.", False, "Chung chung, sai ngữ pháp.")]),
  ("Is this design scalable?", [
    ("Yes, but the single database could become a bottleneck.", True, "Trả lời cân bằng, chỉ rủi ro."),
    ("It's perfect.", False, "Thiếu phản biện."),
    ("Scalable yes no maybe.", False, "Khó hiểu.")]),
  ("Can you explain the trade-off?", [
    ("It's faster to build now, but harder to change later.", True, "Nêu rõ hai mặt."),
    ("There is no trade-off.", False, "Mọi thiết kế đều có đánh đổi."),
    ("Trade-off is have.", False, "Sai ngữ pháp.")]),
 ],
 "listen": [
  ("We will split the system into three layers: the web layer, the service layer, and the data layer.", ["split", "service", "data"], "trình bày kiến trúc"),
  ("The main trade-off is cost. The new design is more reliable, but it needs two more servers.", ["trade-off", "reliable", "servers"], "đánh đổi thiết kế"),
 ]},
21: {  # Microservices
 "dialogues": [
  ("Which service owns the user data?", [
    ("The account service. Other services call its API.", True, "Rõ ràng về quyền sở hữu dữ liệu."),
    ("All services share it.", False, "Dễ gây phụ thuộc chéo."),
    ("User data is everywhere.", False, "Không rõ ràng.")]),
  ("What happens if the payment service is down?", [
    ("Orders go into a queue and we retry later.", True, "Giải thích cơ chế chịu lỗi."),
    ("Everything stops.", False, "Thiết kế kém chịu lỗi."),
    ("Payment down, order no.", False, "Không thành câu.")]),
  ("Should we split this service?", [
    ("Not yet. It's still small and one team owns it.", True, "Quyết định có lý do."),
    ("Yes, split everything.", False, "Tách quá mức."),
    ("Split maybe good maybe no.", False, "Mơ hồ.")]),
 ],
 "listen": [
  ("The order service calls the payment service through the gateway. If it times out, we retry three times.", ["gateway", "times", "retry"], "luồng giữa các service"),
  ("Each service has its own database. Do not read another service's tables directly; use its API.", ["own", "tables", "API"], "nguyên tắc microservices"),
 ]},
22: {  # Message queue & sự kiện
 "dialogues": [
  ("Why are messages stuck in the queue?", [
    ("The consumer crashed. I restarted it and it's catching up now.", True, "Nguyên nhân + trạng thái hiện tại."),
    ("Queues are always slow.", False, "Không phân tích."),
    ("Message stuck, I don't know why.", False, "Không có hướng xử lý.")]),
  ("Can the same event be processed twice?", [
    ("Yes, so our handler must be idempotent.", True, "Hiểu đúng rủi ro + giải pháp."),
    ("No, never.", False, "Sai — hầu hết queue giao ít nhất một lần."),
    ("Twice is maybe ok.", False, "Mơ hồ.")]),
  ("Who subscribes to this topic?", [
    ("The email service and the analytics service.", True, "Liệt kê cụ thể."),
    ("Everyone.", False, "Không chính xác."),
    ("Subscribe many service.", False, "Sai ngữ pháp.")]),
 ],
 "listen": [
  ("When an order is created, we publish an event. The email service sends a receipt and the stock service updates inventory.", ["publish", "receipt", "inventory"], "luồng sự kiện"),
  ("There are ten thousand messages in the queue. I added two more consumers, so it should be empty in an hour.", ["thousand", "consumers", "hour"], "xử lý tồn queue"),
 ]},
23: {  # Caching
 "dialogues": [
  ("Users see old prices after the update.", [
    ("The cache wasn't invalidated. I'll clear it and fix the logic.", True, "Nguyên nhân + sửa gốc."),
    ("They should refresh the page.", False, "Đẩy việc cho người dùng."),
    ("Price old because cache maybe.", False, "Lủng củng.")]),
  ("How long should we cache this data?", [
    ("Five minutes is fine. It doesn't change often.", True, "Con số + lý do."),
    ("Forever.", False, "Dữ liệu sẽ cũ."),
    ("Cache long time good.", False, "Mơ hồ, sai ngữ pháp.")]),
  ("What's our cache hit rate?", [
    ("About 85% this week, up from 60%.", True, "Số liệu + xu hướng."),
    ("High, I guess.", False, "Không kiểm chứng."),
    ("Hit rate is many.", False, "Sai ngữ pháp.")]),
 ],
 "listen": [
  ("We cache the product list for ten minutes. When an admin edits a product, we clear that key right away.", ["cache", "edits", "clear"], "chiến lược cache"),
  ("The cache hit rate is low because each key includes the user ID. Let's cache shared data without it.", ["rate", "user", "shared"], "phân tích cache"),
 ]},
24: {  # Xác thực & phân quyền
 "dialogues": [
  ("Why can't I access the admin page?", [
    ("Your account doesn't have the admin role. I'll ask the owner to grant it.", True, "Giải thích + cách xử lý."),
    ("The page is broken.", False, "Chẩn đoán sai."),
    ("You no have permission.", False, "Sai ngữ pháp: You don't have…")]),
  ("How long does the session last?", [
    ("Thirty minutes, then the token is refreshed automatically.", True, "Rõ thời gian + cơ chế."),
    ("Some time.", False, "Không có thông tin."),
    ("Session last long.", False, "Sai chia động từ.")]),
  ("Should we store the password in the database?", [
    ("Only a hashed version, never the plain password.", True, "Chuẩn bảo mật."),
    ("Yes, as plain text is easier.", False, "Nguy hiểm nghiêm trọng."),
    ("Password database ok.", False, "Không rõ, không an toàn.")]),
 ],
 "listen": [
  ("Users log in with their company account. After login, they get a token that expires in one hour.", ["company", "token", "expires"], "luồng đăng nhập"),
  ("Only managers can approve refunds. Please check the role on the server, not only in the UI.", ["managers", "role", "server"], "phân quyền"),
 ]},
25: {  # Mạng cơ bản
 "dialogues": [
  ("I can't reach the server from my laptop.", [
    ("Are you on the VPN? The server is only on the internal network.", True, "Hỏi đúng nguyên nhân phổ biến."),
    ("The server is dead.", False, "Kết luận vội."),
    ("Network is no.", False, "Không thành câu.")]),
  ("Why is the website slow in Europe?", [
    ("Our servers are in Asia. A CDN would help a lot.", True, "Nguyên nhân + giải pháp."),
    ("Europe internet is bad.", False, "Đổ lỗi, không đúng."),
    ("Slow because far maybe.", False, "Lủng củng.")]),
  ("Did you update the DNS record?", [
    ("Yes, but it may take up to an hour to propagate.", True, "Xác nhận + lưu ý thời gian."),
    ("DNS is updated immediately always.", False, "Không chính xác."),
    ("Yes I update.", False, "Sai thì: I updated it.")]),
 ],
 "listen": [
  ("The request goes through the load balancer to one of three servers. If one server fails, traffic moves to the others.", ["balancer", "fails", "traffic"], "cân bằng tải"),
  ("I changed the DNS record this morning. Some users may still see the old site for a few hours.", ["record", "users", "hours"], "đổi DNS"),
 ]},
26: {  # Linux & terminal
 "dialogues": [
  ("How do I check which process uses port 8080?", [
    ("Run lsof -i :8080, and you'll see the process ID.", True, "Lệnh cụ thể + kết quả mong đợi."),
    ("Restart your computer.", False, "Không giải quyết đúng câu hỏi."),
    ("Use command for check.", False, "Mơ hồ.")]),
  ("The disk on the server is full.", [
    ("Let's delete old log files and set up log rotation.", True, "Xử lý ngay + phòng ngừa."),
    ("Buy a bigger server.", False, "Tốn kém, chưa phân tích."),
    ("Disk full, delete all.", False, "Nguy hiểm, không rõ ràng.")]),
  ("Can I use sudo on the production server?", [
    ("Only for emergencies, and please write it in the log.", True, "Có quy tắc, có ghi lại."),
    ("Sure, anytime.", False, "Rủi ro bảo mật."),
    ("Sudo is ok always.", False, "Sai về quy trình.")]),
 ],
 "listen": [
  ("First, SSH into the server. Then go to the logs folder and search for the error with grep.", ["SSH", "folder", "grep"], "hướng dẫn tìm lỗi"),
  ("The script failed because it did not have permission to write the file. I fixed it with chmod.", ["script", "permission", "chmod"], "lỗi quyền file"),
 ]},
27: {  # Debug nâng cao
 "dialogues": [
  ("The bug only happens in production.", [
    ("Let's compare the configs and check the production logs.", True, "Hướng điều tra hợp lý."),
    ("Then we can't fix it.", False, "Bỏ cuộc sớm."),
    ("Production bug is magic.", False, "Không chuyên nghiệp.")]),
  ("Did you find the root cause?", [
    ("Yes, a null value from the old API. I added a check.", True, "Nguyên nhân gốc + cách sửa."),
    ("I restarted it and it works.", False, "Chưa tìm ra gốc rễ."),
    ("Root cause find yes.", False, "Sai trật tự từ.")]),
  ("How can I debug this memory leak?", [
    ("Take a heap snapshot before and after, then compare them.", True, "Kỹ thuật cụ thể."),
    ("Add more memory.", False, "Che giấu vấn đề."),
    ("Debug memory is hard, skip.", False, "Bỏ cuộc.")]),
 ],
 "listen": [
  ("I added a breakpoint and stepped through the code. The variable is empty because the API returns null for new users.", ["breakpoint", "empty", "null"], "debug từng bước"),
  ("The crash happens only when two requests arrive at the same time. It looks like a race condition.", ["crash", "same", "race"], "lỗi race condition"),
 ]},
28: {  # Refactoring & chất lượng code
 "dialogues": [
  ("Should we refactor this module now?", [
    ("Let's add tests first, then refactor step by step.", True, "An toàn: test trước, làm từng bước."),
    ("Let's rewrite everything from scratch.", False, "Rủi ro cao."),
    ("Refactor now all.", False, "Không rõ ràng.")]),
  ("This function is 300 lines long.", [
    ("I'll split it into smaller functions with clear names.", True, "Giải pháp cụ thể."),
    ("Long functions are fine.", False, "Khó bảo trì."),
    ("Function long, ok.", False, "Không có hướng cải thiện.")]),
  ("The linter shows 50 warnings.", [
    ("Most are unused imports. I'll clean them up today.", True, "Phân loại + hành động."),
    ("Just turn off the linter.", False, "Bỏ qua chất lượng code."),
    ("Warning is not important.", False, "Chủ quan.")]),
 ],
 "listen": [
  ("This refactor does not change any behavior. I only moved the validation code into its own module.", ["behavior", "validation", "module"], "mô tả refactor"),
  ("We have a lot of duplicate code in these three services. Let's move it into a shared library.", ["duplicate", "services", "library"], "đề xuất gom code"),
 ]},
29: {  # Dữ liệu & phân tích
 "dialogues": [
  ("Why did sales drop last week?", [
    ("The checkout page had errors on Tuesday. Most of the drop is from that day.", True, "Dữ liệu chỉ ra nguyên nhân."),
    ("People didn't want to buy.", False, "Đoán, không có dữ liệu."),
    ("Sales drop because drop.", False, "Vô nghĩa.")]),
  ("Can you make a chart for the meeting?", [
    ("Sure, a line chart of daily users for the last 30 days.", True, "Loại biểu đồ + dữ liệu cụ thể."),
    ("Charts are not useful.", False, "Từ chối không lý do."),
    ("I make chart many.", False, "Sai ngữ pháp.")]),
  ("Is this number correct?", [
    ("Let me double-check. The filter might exclude test users.", True, "Thận trọng + giả thuyết."),
    ("Of course, I never make mistakes.", False, "Thiếu kiểm tra."),
    ("Number is correct maybe.", False, "Mơ hồ.")]),
 ],
 "listen": [
  ("This report shows that mobile users grew by twenty percent, but they spend less time in the app.", ["report", "twenty", "less"], "đọc báo cáo"),
  ("Before we compare the two groups, let's remove test accounts. They make the average look higher.", ["compare", "remove", "average"], "làm sạch dữ liệu"),
 ]},
30: {  # Machine learning cơ bản
 "dialogues": [
  ("How accurate is the model?", [
    ("About 92% on the test set, but lower on new users.", True, "Số liệu + giới hạn."),
    ("It's always right.", False, "Không thực tế."),
    ("Accuracy is good very.", False, "Sai trật tự từ.")]),
  ("Why does the model do well in training but badly in production?", [
    ("It's probably overfitting. The training data is too small.", True, "Chẩn đoán đúng khái niệm."),
    ("Production users are wrong.", False, "Đổ lỗi."),
    ("Model tired.", False, "Vô nghĩa.")]),
  ("Can we use this data to train the model?", [
    ("We need to check privacy rules and remove personal data first.", True, "Chú ý quyền riêng tư."),
    ("Yes, use all data.", False, "Có thể vi phạm quyền riêng tư."),
    ("Data train ok.", False, "Không rõ.")]),
 ],
 "listen": [
  ("We trained the model on six months of data. It predicts which users will cancel with about ninety percent accuracy.", ["trained", "predicts", "accuracy"], "báo cáo mô hình"),
  ("The labels in this dataset are not consistent. We should fix them before we train again.", ["labels", "consistent", "train"], "chất lượng dữ liệu"),
 ]},
31: {  # Email công việc
 "dialogues": [
  ("How should I start an email to a new client?", [
    ("'Dear Ms. Tanaka, thank you for your time yesterday.'", True, "Mở đầu trang trọng, lịch sự."),
    ("'Hey, what's up?'", False, "Quá suồng sã với khách mới."),
    ("'To client, hello you.'", False, "Sai cách xưng hô.")]),
  ("Did you reply to the customer?", [
    ("Yes, I sent a reply and copied the team lead.", True, "Xác nhận + đã CC đúng người."),
    ("I will reply maybe next week.", False, "Quá chậm."),
    ("Yes I reply yesterday.", False, "Sai thì: I replied.")]),
  ("The attachment is missing.", [
    ("Sorry about that. I've resent the email with the file.", True, "Xin lỗi + đã khắc phục."),
    ("It's your email's problem.", False, "Đổ lỗi."),
    ("Attachment is inside maybe.", False, "Không giải quyết.")]),
 ],
 "listen": [
  ("Thank you for your email. I have attached the report, and I will send the final version by Friday.", ["attached", "final", "Friday"], "trả lời email"),
  ("Sorry for the late reply. I was out of the office yesterday, but I am back today and happy to help.", ["late", "office", "help"], "xin lỗi trả lời muộn"),
 ]},
32: {  # Chat & Slack công việc
 "dialogues": [
  ("Hey, do you have a minute?", [
    ("Sure, what's up?", True, "Tự nhiên, thân thiện."),
    ("No.", False, "Cộc lốc."),
    ("I have minute yes.", False, "Sai ngữ pháp.")]),
  ("Can you move this conversation to a thread?", [
    ("Good idea, I'll reply in the thread.", True, "Hợp tác, giữ kênh gọn."),
    ("Threads are annoying.", False, "Không hợp tác."),
    ("Thread is where?", False, "Câu hỏi lạc đề.")]),
  ("Are you online?", [
    ("I'm in a meeting now. I'll get back to you in 30 minutes.", True, "Trạng thái + khi nào phản hồi."),
    ("Yes but busy, no talk.", False, "Cộc, sai ngữ pháp."),
    ("Online maybe.", False, "Mơ hồ.")]),
 ],
 "listen": [
  ("Quick update: the fix is deployed. Please let me know in this thread if you still see the error.", ["fix", "deployed", "thread"], "tin nhắn cập nhật"),
  ("I will be offline this afternoon for a doctor's appointment. Please message Linh if anything is urgent.", ["offline", "appointment", "urgent"], "báo vắng mặt"),
 ]},
33: {  # Phỏng vấn & CV
 "dialogues": [
  ("Tell me about yourself.", [
    ("I'm a backend developer with four years of experience in Java and cloud services.", True, "Ngắn gọn: vai trò + kinh nghiệm + thế mạnh."),
    ("My name is Hung and I like football.", False, "Không liên quan công việc."),
    ("I am developer four year.", False, "Thiếu mạo từ và 's'.")]),
  ("Why do you want to join our company?", [
    ("I like your product, and I want to work on large-scale systems.", True, "Lý do cụ thể, tích cực."),
    ("Because the salary is high.", False, "Chỉ nói về lương — không ấn tượng."),
    ("Your company is good company.", False, "Chung chung.")]),
  ("Tell me about a difficult bug you fixed.", [
    ("We had random timeouts. I found a connection leak and fixed it, which cut errors by 90%.", True, "Tình huống + hành động + kết quả có số."),
    ("I never have difficult bugs.", False, "Không thuyết phục."),
    ("Bug was hard, I fix.", False, "Thiếu chi tiết, sai thì.")]),
 ],
 "listen": [
  ("In my last project, I led a team of three developers. We rebuilt the payment system and reduced errors by half.", ["led", "rebuilt", "half"], "kể kinh nghiệm"),
  ("My strength is solving problems step by step. My weakness is public speaking, but I am practicing every week.", ["strength", "weakness", "practicing"], "điểm mạnh yếu"),
 ]},
34: {  # Nghỉ phép & hành chính
 "dialogues": [
  ("Can I take next Friday off?", [
    ("Sure. Please add it to the team calendar and hand over your tasks.", True, "Đồng ý + hướng dẫn bàn giao."),
    ("No holidays allowed.", False, "Không hợp lý."),
    ("Friday off ok go.", False, "Lủng củng.")]),
  ("Who will cover your work while you're away?", [
    ("Minh will cover my tickets. I've shared my notes with him.", True, "Người thay + đã bàn giao."),
    ("Nobody, it can wait.", False, "Bỏ bê công việc."),
    ("Minh cover maybe.", False, "Mơ hồ.")]),
  ("Did you submit your timesheet?", [
    ("Not yet. I'll do it before 5 p.m.", True, "Trung thực + mốc thời gian."),
    ("Timesheets are useless.", False, "Thái độ tiêu cực."),
    ("I submit it yesterday.", False, "Sai thì: I submitted it.")]),
 ],
 "listen": [
  ("I will be on leave from Monday to Wednesday. Minh will cover my tasks, and I will check email once a day.", ["leave", "cover", "once"], "báo nghỉ phép"),
  ("I am not feeling well today, so I will take a sick day. I will update my tickets tomorrow morning.", ["well", "sick", "tomorrow"], "xin nghỉ ốm"),
 ]},
35: {  # Đánh giá & phản hồi
 "dialogues": [
  ("What would you like to improve next quarter?", [
    ("I want to get better at system design and lead one feature.", True, "Mục tiêu cụ thể, chủ động."),
    ("Nothing, I'm already good.", False, "Thiếu tinh thần phát triển."),
    ("Improve many thing.", False, "Chung chung, sai ngữ pháp.")]),
  ("How do you feel about the feedback?", [
    ("It's helpful. I'll work on writing clearer PR descriptions.", True, "Tiếp nhận tích cực + hành động."),
    ("I don't agree with anything.", False, "Phòng thủ."),
    ("Feedback make me sad.", False, "Không xây dựng, sai ngữ pháp.")]),
  ("What was your biggest achievement this year?", [
    ("I cut the build time from 20 minutes to 6.", True, "Thành tích có số đo."),
    ("I worked very hard.", False, "Không có kết quả cụ thể."),
    ("Achievement is many.", False, "Mơ hồ.")]),
 ],
 "listen": [
  ("You did a great job on the migration this year. Next year, I would like you to mentor one new developer.", ["migration", "mentor", "developer"], "nhận xét cuối năm"),
  ("One area to improve is communication. Please share updates earlier when a task is going to be late.", ["improve", "updates", "late"], "góp ý cải thiện"),
 ]},
36: {  # Khách hàng & hỗ trợ
 "dialogues": [
  ("The customer is very angry about the outage.", [
    ("Let's apologize, explain what happened, and offer a discount.", True, "Xin lỗi + minh bạch + bù đắp."),
    ("It's not our fault.", False, "Làm khách giận thêm."),
    ("Angry customer ignore.", False, "Bỏ mặc khách hàng.")]),
  ("Can you help me reset my password?", [
    ("Of course. I've sent a reset link to your email.", True, "Lịch sự + đã xử lý."),
    ("Read the FAQ.", False, "Thiếu hỗ trợ."),
    ("Password reset you do.", False, "Sai trật tự từ.")]),
  ("When will the bug be fixed?", [
    ("Our team is working on it. We expect a fix by tomorrow and will update you.", True, "Minh bạch + mốc + cam kết cập nhật."),
    ("We don't know.", False, "Không trấn an khách."),
    ("Fix soon maybe.", False, "Mơ hồ.")]),
 ],
 "listen": [
  ("Thank you for your patience. We fixed the issue this morning, and we added a credit to your account.", ["patience", "issue", "credit"], "phản hồi khách"),
  ("I understand this is frustrating. Could you send me a screenshot so we can find the problem faster?", ["understand", "screenshot", "problem"], "hỗ trợ khách"),
 ]},
}
