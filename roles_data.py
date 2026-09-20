# -*- coding: utf-8 -*-
# C3: gói nội dung theo vai trò (QA, DevOps, BA, PM, Designer, Data) -> roles.gen.js (window.ROLES), copy sang game/
# Mỗi vai: 4 tình huống AI (k, nhãn VN, prompt EN) + 6 hội thoại chọn đáp (câu đồng nghiệp + 3 lựa chọn: câu, đúng?, phản hồi VN)
import json, os, shutil

ROLES = {
 "dev": {"label": "Developer", "emoji": "💻", "scenarios": [], "dialogues": []},
 "qa": {"label": "QA / Tester", "emoji": "🧪",
  "scenarios": [
   ("qa_bug", "Báo bug cho dev", "You are a developer. I am a QA tester reporting a bug I found in your feature. Ask me how to reproduce it, the environment and the expected result."),
   ("qa_plan", "Họp test plan", "You are the QA lead. We are planning the test scope for the next release. Ask what I will test, what is risky and what is out of scope."),
   ("qa_reject", "Trả ticket về dev", "You are a developer whose ticket I am reopening because the fix does not work. Push back a little and ask for evidence."),
   ("qa_signoff", "Xác nhận release", "You are the product manager. Ask me if the release is ready to ship and whether there are any known issues."),
  ],
  "dialogues": [
   ("Can you tell me how to reproduce the bug?", [
     ("Sure. Log in as admin, open Settings, and click Save twice. The page crashes.", True, "Đưa các bước rõ ràng, có thứ tự — đúng kiểu báo bug."),
     ("It's broken, just try it.", False, "Quá chung chung, dev không biết làm lại thế nào."),
     ("I reproduce yesterday many time.", False, "Sai thì và không có bước tái hiện.")]),
   ("Which environment did you test on?", [
     ("On staging, with Chrome 128 on Windows.", True, "Nêu môi trường + trình duyệt — thông tin dev cần."),
     ("On my computer.", False, "Thiếu thông tin môi trường."),
     ("Environment is test.", False, "Câu cụt, không rõ môi trường nào.")]),
   ("Is this a blocker for the release?", [
     ("Yes, it's a blocker. Users can't finish checkout.", True, "Trả lời có/không + lý do ảnh hưởng."),
     ("Maybe, I don't know.", False, "QA nên đánh giá mức độ nghiêm trọng."),
     ("It is block.", False, "Sai ngữ pháp: nên nói 'It's a blocker'.")]),
   ("I've fixed it. Can you retest?", [
     ("Sure, I'll retest it this afternoon and update the ticket.", True, "Xác nhận + mốc thời gian + cập nhật ticket."),
     ("OK retest.", False, "Quá cộc lốc."),
     ("Why you not test before?", False, "Thiếu lịch sự và sai ngữ pháp.")]),
   ("What's the test coverage for this feature?", [
     ("We have 12 test cases. The payment flow is fully covered, but refunds aren't yet.", True, "Nêu số liệu + phần còn thiếu."),
     ("Coverage is good.", False, "Không có số liệu cụ thể."),
     ("We test all.", False, "Mơ hồ và sai ngữ pháp.")]),
   ("Can we skip regression testing this time?", [
     ("I'd rather not. The change touches the login module, so the risk is high.", True, "Phản đối lịch sự + lý do rủi ro."),
     ("No.", False, "Cộc lốc, không giải thích."),
     ("Skip is dangerous very.", False, "Sai trật tự từ.")]),
  ]},
 "devops": {"label": "DevOps / SRE", "emoji": "🛠️",
  "scenarios": [
   ("do_incident", "Xử lý sự cố", "You are the on-call engineer's manager. Production is down. Ask me for status, impact and ETA in short questions."),
   ("do_postmortem", "Họp postmortem", "You are facilitating a blameless postmortem. Ask me about the timeline, root cause and action items."),
   ("do_pipeline", "CI/CD bị lỗi", "You are a developer whose pipeline is failing. Ask me for help and explain what you see."),
   ("do_cost", "Tối ưu chi phí cloud", "You are the engineering manager. Our cloud bill went up 30%. Ask me why and what we can do."),
  ],
  "dialogues": [
   ("What's the current status of the outage?", [
     ("The API is back up. We're still monitoring error rates for the next 30 minutes.", True, "Trạng thái + bước tiếp theo."),
     ("Fixing.", False, "Quá ngắn, không đủ thông tin."),
     ("Server is die.", False, "Sai ngữ pháp: 'The server is down'.")]),
   ("What was the root cause?", [
     ("A config change set the connection pool too low, so requests timed out.", True, "Nguyên nhân gốc rõ ràng, có chuỗi hệ quả."),
     ("Somebody made mistake.", False, "Đổ lỗi cá nhân — không đúng tinh thần blameless."),
     ("I don't know why it happen.", False, "Sai ngữ pháp và thiếu phân tích.")]),
   ("Can you roll back the deployment?", [
     ("Yes, rolling back to version 2.3 now. It'll take about five minutes.", True, "Hành động + phiên bản + thời gian."),
     ("OK.", False, "Thiếu thông tin."),
     ("Rollback is not possible never.", False, "Phủ định kép sai.")]),
   ("Why is the pipeline so slow?", [
     ("The test stage runs everything in sequence. We can run it in parallel.", True, "Nêu nguyên nhân + đề xuất."),
     ("Because slow.", False, "Không giải thích."),
     ("Pipeline have many step.", False, "Sai chia động từ.")]),
   ("Do we need more servers for the sale next week?", [
     ("I think so. Last year traffic tripled, so let's add auto-scaling.", True, "Dựa trên dữ liệu + giải pháp."),
     ("Yes more.", False, "Không có lý do."),
     ("Maybe need.", False, "Câu thiếu chủ ngữ.")]),
   ("Who is on call this weekend?", [
     ("I am. I'll keep my phone on and check alerts every few hours.", True, "Trả lời rõ + cam kết."),
     ("Not me.", False, "Không giúp gì."),
     ("Me on call.", False, "Thiếu động từ 'I'm on call'.")]),
  ]},
 "ba": {"label": "Business Analyst", "emoji": "📋",
  "scenarios": [
   ("ba_elicit", "Lấy yêu cầu từ khách", "You are a client describing a new feature you want. I am the BA asking clarifying questions. Be a little vague so I have to ask."),
   ("ba_story", "Viết user story với team", "You are a developer reviewing my user story. Ask about acceptance criteria and edge cases."),
   ("ba_change", "Khách đổi yêu cầu", "You are a client who wants to change the requirements in the middle of the sprint. I must handle it politely."),
   ("ba_demo", "Demo cho khách", "You are a client watching my demo. Ask simple questions and give some feedback."),
  ],
  "dialogues": [
   ("We want users to export reports.", [
     ("Got it. Which format do you need — PDF or Excel — and who will use them?", True, "Hỏi làm rõ định dạng + người dùng."),
     ("OK, we will do.", False, "Nhận việc mà không làm rõ yêu cầu."),
     ("Export what?", False, "Hơi cộc, thiếu lịch sự.")]),
   ("Can we add this to the current sprint?", [
     ("Let me check with the team. If we add it, something else may move to the next sprint.", True, "Nêu trade-off, không hứa bừa."),
     ("Yes, no problem.", False, "Hứa ngay có thể làm vỡ sprint."),
     ("Cannot.", False, "Cộc lốc.")]),
   ("What are the acceptance criteria?", [
     ("A user can filter by date, and the result loads in under two seconds.", True, "Tiêu chí đo được."),
     ("It should work good.", False, "Không đo được, sai 'well'."),
     ("Criteria is in the document.", False, "Né câu hỏi.")]),
   ("I'm not sure this is what we asked for.", [
     ("Thanks for the feedback. Could you show me which part is different from what you expected?", True, "Lắng nghe + hỏi cụ thể."),
     ("It is what you said.", False, "Phòng thủ, dễ gây căng thẳng."),
     ("You wrong.", False, "Thiếu lịch sự và sai ngữ pháp.")]),
   ("How long will this change take?", [
     ("I'll confirm with the developers and get back to you by tomorrow.", True, "Không đoán bừa, có mốc trả lời."),
     ("One day.", False, "Đoán khi chưa hỏi team."),
     ("Very long time maybe.", False, "Mơ hồ.")]),
   ("Can you summarize today's meeting?", [
     ("Sure. We agreed on the scope, and the next step is the design review on Friday.", True, "Tóm tắt thống nhất + bước tiếp."),
     ("Meeting is finished.", False, "Không tóm tắt gì."),
     ("We talk many things.", False, "Sai thì, mơ hồ.")]),
  ]},
 "pm": {"label": "PM / Scrum Master", "emoji": "🧭",
  "scenarios": [
   ("pm_planning", "Sprint planning", "You are a developer in sprint planning. I am the PM. Tell me some tasks are bigger than they look and ask me to prioritise."),
   ("pm_stakeholder", "Báo cáo tiến độ cho sếp", "You are a senior stakeholder. Ask me whether the project is on track, what the risks are and what I need."),
   ("pm_retro", "Điều phối retro", "You are a team member in a retrospective. Share one thing that went well and one problem; answer my questions."),
   ("pm_delay", "Báo trễ deadline", "You are the client. I have to tell you the release will be one week late. React with concern and ask why."),
  ],
  "dialogues": [
   ("Are we still on track for the release?", [
     ("Mostly. Two features are done, but the payment work is two days behind. I'll share a new plan today.", True, "Trạng thái trung thực + kế hoạch."),
     ("Yes, everything is perfect.", False, "Giấu rủi ro."),
     ("We are late maybe.", False, "Mơ hồ, không có số liệu.")]),
   ("Can the team take one more ticket this sprint?", [
     ("Our capacity is full. We can take it if we drop the export feature.", True, "Nói về capacity + đánh đổi."),
     ("Sure, they can work overtime.", False, "Không bền vững."),
     ("No capacity no.", False, "Cộc và lủng củng.")]),
   ("What went wrong last sprint?", [
     ("Requirements changed late, so we lost about three days. Let's freeze scope earlier.", True, "Nguyên nhân + đề xuất cải tiến."),
     ("The developers were slow.", False, "Đổ lỗi, không xây dựng."),
     ("Many thing wrong.", False, "Sai ngữ pháp, mơ hồ.")]),
   ("Why is the release delayed?", [
     ("We found a security issue in testing. Fixing it first protects your users.", True, "Lý do + lợi ích cho khách."),
     ("Because of the team.", False, "Không giải thích."),
     ("Delay is normal.", False, "Thiếu trách nhiệm.")]),
   ("Who owns this action item?", [
     ("Linh will own it, and she'll update us at Thursday's standup.", True, "Người phụ trách + thời hạn."),
     ("Somebody.", False, "Không ai chịu trách nhiệm."),
     ("Everybody own it.", False, "Sai chia động từ, không rõ người.")]),
   ("Can we cancel the daily standup?", [
     ("Let's keep it short instead — 10 minutes, blockers only.", True, "Đề xuất giải pháp thay vì huỷ."),
     ("OK cancel.", False, "Bỏ mất kênh đồng bộ."),
     ("Standup is not use.", False, "Sai ngữ pháp.")]),
  ]},
 "designer": {"label": "UI/UX Designer", "emoji": "🎨",
  "scenarios": [
   ("ds_handoff", "Bàn giao thiết kế cho dev", "You are a frontend developer receiving my design in Figma. Ask about spacing, states, and what happens on small screens."),
   ("ds_critique", "Góp ý thiết kế", "You are a product manager giving feedback on my new screen design. Ask why I made some choices and suggest one change."),
   ("ds_research", "Phỏng vấn người dùng", "You are a user of our app in a short interview. I am the designer asking about your experience. Answer honestly, sometimes vaguely."),
   ("ds_system", "Design system", "You are a developer. We are discussing whether to add a new button style to the design system. Push back a little."),
  ],
  "dialogues": [
   ("What happens when the list is empty?", [
     ("We show an empty state with a short message and a button to add the first item.", True, "Nghĩ tới trạng thái rỗng — dev rất cần."),
     ("It will never be empty.", False, "Bỏ sót trường hợp thực tế."),
     ("Empty is nothing show.", False, "Sai ngữ pháp, không rõ.")]),
   ("The design doesn't fit on small phones.", [
     ("Good catch. I'll add a layout for 360-pixel screens.", True, "Tiếp nhận + giải pháp cụ thể."),
     ("Users should buy bigger phones.", False, "Không đặt người dùng làm trung tâm."),
     ("Small phone not my problem.", False, "Thái độ không hợp tác.")]),
   ("Why did you choose this color?", [
     ("It has better contrast, so it's easier to read for everyone.", True, "Lý do dựa trên khả năng tiếp cận."),
     ("Because I like it.", False, "Lý do cảm tính."),
     ("Color is beautiful very.", False, "Sai trật tự từ.")]),
   ("Can you share the Figma link?", [
     ("Sure. I've shared it in the channel with edit access for the team.", True, "Chia sẻ + phân quyền rõ."),
     ("Figma is secret.", False, "Không hợp tác."),
     ("I share you link later maybe.", False, "Mơ hồ, sai ngữ pháp.")]),
   ("Users can't find the settings button.", [
     ("Let's move it to the top bar and test it with five users.", True, "Giải pháp + kiểm chứng."),
     ("They should look harder.", False, "Đổ lỗi cho người dùng."),
     ("Settings button is there, see.", False, "Phủ nhận vấn đề.")]),
   ("Is this component in the design system?", [
     ("Not yet. I'll add it after we test it on this page.", True, "Trả lời rõ + kế hoạch."),
     ("Every component is different.", False, "Làm hỏng tính nhất quán."),
     ("Component is design maybe.", False, "Khó hiểu.")]),
  ]},
 "data": {"label": "Data / Analyst", "emoji": "📊",
  "scenarios": [
   ("da_request", "Nhận yêu cầu báo cáo", "You are a marketing manager asking me for a new report. Be vague at first so I must ask clarifying questions about metrics and time range."),
   ("da_explain", "Giải thích số liệu", "You are a non-technical manager. Ask me to explain why a key number went down last month, in simple words."),
   ("da_quality", "Dữ liệu sai lệch", "You are a data engineer. I found wrong numbers in the dashboard. Discuss the possible causes with me."),
   ("da_model", "Trình bày mô hình", "You are a product owner. I am presenting a simple prediction model. Ask about accuracy, risks, and how we will use it."),
  ],
  "dialogues": [
   ("Can you pull the numbers for last month?", [
     ("Sure. Do you need daily numbers or just the monthly total?", True, "Hỏi làm rõ trước khi làm."),
     ("Numbers are in the database.", False, "Không giúp người hỏi."),
     ("I pull tomorrow maybe.", False, "Mơ hồ, sai thì.")]),
   ("Why is this number different from the finance report?", [
     ("Finance counts refunds, but our dashboard doesn't. I'll add a note.", True, "Giải thích nguyên nhân khác biệt."),
     ("Finance is wrong.", False, "Đổ lỗi khi chưa đối chiếu."),
     ("Different because different.", False, "Vô nghĩa.")]),
   ("Is this trend real or just noise?", [
     ("It lasted six weeks and the sample is large, so it's likely real.", True, "Lập luận dựa trên thời gian và cỡ mẫu."),
     ("Definitely real, trust me.", False, "Thiếu căn cứ."),
     ("Trend is maybe noise real.", False, "Khó hiểu.")]),
   ("Can you make this dashboard load faster?", [
     ("Yes, I'll pre-aggregate the data every night.", True, "Giải pháp kỹ thuật cụ thể."),
     ("Dashboards are always slow.", False, "Không cải thiện."),
     ("Faster make I try.", False, "Sai trật tự từ.")]),
   ("Can we trust this data?", [
     ("Mostly. About 3% of rows have missing dates, so I excluded them.", True, "Minh bạch về chất lượng dữ liệu."),
     ("Yes, data is always correct.", False, "Chủ quan."),
     ("Trust yes no.", False, "Không rõ ràng.")]),
   ("What should we do with this insight?", [
     ("I suggest we test a shorter sign-up form with 10% of users.", True, "Biến insight thành hành động có kiểm chứng."),
     ("Nothing, it's just a chart.", False, "Bỏ phí phân tích."),
     ("Insight is good, do.", False, "Không cụ thể.")]),
  ]},
}

def _shuffle(o, n):
    g = [x for x in o if x['good']][0]; rest = [x for x in o if not x['good']]
    rest.insert(n % 3, g); return rest

out = {}
for k, r in ROLES.items():
    out[k] = {"label": r["label"], "emoji": r["emoji"],
              "scenarios": [{"k": "r_" + a, "l": b, "s": c} for a, b, c in r["scenarios"]],
              "dialogues": [{"them": t, "opts": _shuffle([{"t": x, "good": g, "fb": f} for x, g, f in o], n)} for n, (t, o) in enumerate(r["dialogues"])]}
js = "window.ROLES=" + json.dumps(out, ensure_ascii=False, separators=(",", ":")) + ";\n"
here = os.path.dirname(os.path.abspath(__file__))
open(os.path.join(here, "roles.gen.js"), "w", encoding="utf-8").write(js)
if os.path.isdir(os.path.join(here, "game")):
    shutil.copyfile(os.path.join(here, "roles.gen.js"), os.path.join(here, "game", "roles.gen.js"))
print("roles", len(out), "scenarios", sum(len(r["scenarios"]) for r in out.values()), "dialogues", sum(len(r["dialogues"]) for r in out.values()))
