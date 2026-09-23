/* Nói Nghề — Mẫu email & tin nhắn theo ngành (v4.3). File dữ liệu thuần. */
/* Quy ước: {me} = tên người dùng (luôn có sẵn). Mọi {k} khác phải khai báo trong fields.
   kind "email" có subject + tone.short (bản chat 1–2 câu); kind "chat" có subject = "". */
window.MAIL_TPL = [

  /* ============ CHUNG (track "*") — 16 mẫu ============ */

  { id: "leave", track: "*", kind: "email", title: "Xin nghỉ phép", vi: "Xin nghỉ 1–vài ngày, có người thay",
    fields: [
      { k: "boss", label: "Tên người nhận", ph: "Anna" },
      { k: "date", label: "Ngày nghỉ", ph: "Friday, May 10" },
      { k: "cover", label: "Người làm thay", ph: "Minh" }
    ],
    subject: "Leave request – {date}",
    body: "Hi {boss},\n\nI'd like to request a day off on {date} for personal reasons.\n\nMy tasks are on track. While I'm away, {cover} will cover for me, and I'll send a short handover note before I leave.\n\nPlease let me know if this is OK.\n\nBest regards,\n{me}",
    tone: {
      polite: "Dear {boss},\n\nI would like to kindly request a day off on {date} for personal reasons.\n\nI will make sure my work is up to date before I leave. {cover} has kindly agreed to cover for me, and I will prepare a handover note.\n\nPlease let me know if this would be possible.\n\nKind regards,\n{me}",
      short: "Hi {boss}, may I take a day off on {date}? {cover} will cover for me, and I'll send a handover note before I leave."
    } },

  { id: "sick", track: "*", kind: "email", title: "Báo ốm", vi: "Báo nghỉ ốm hôm nay, ai lo việc gấp",
    fields: [
      { k: "boss", label: "Tên người nhận", ph: "Anna" },
      { k: "date", label: "Ngày nghỉ", ph: "today (May 10)" },
      { k: "cover", label: "Người lo việc gấp", ph: "Minh" },
      { k: "back", label: "Dự kiến đi làm lại", ph: "tomorrow" }
    ],
    subject: "Sick leave – {date}",
    body: "Hi {boss},\n\nI'm not feeling well, so I won't be able to come to work {date}.\n\nI'll check my messages when I can. If anything is urgent, please contact {cover}.\n\nI hope to be back {back}.\n\nBest regards,\n{me}",
    tone: {
      short: "Hi {boss}, I'm sick and can't come to work {date}. {cover} can help with anything urgent. I hope to be back {back}."
    } },

  { id: "late", track: "*", kind: "chat", title: "Báo đến trễ", vi: "Nhắn nhanh: đến muộn, mấy giờ tới",
    fields: [
      { k: "boss", label: "Tên người nhận", ph: "Anna" },
      { k: "reason", label: "Lý do (ngắn)", ph: "heavy traffic" },
      { k: "time", label: "Giờ đến dự kiến", ph: "9:30" }
    ],
    subject: "",
    body: "Hi {boss}, sorry, I'm running late because of {reason}. I should be there by {time}. I'll catch up on anything I miss.",
    tone: {
      polite: "Good morning {boss}, I'm very sorry, but I'm running late because of {reason}. I expect to arrive by {time}. I apologize for the inconvenience."
    } },

  { id: "deadline_delay", track: "*", kind: "email", title: "Báo trễ hạn + ngày mới", vi: "Việc không kịp hạn, nêu lý do và ngày mới",
    fields: [
      { k: "boss", label: "Tên người nhận", ph: "Anna" },
      { k: "task", label: "Việc bị trễ", ph: "the sales report" },
      { k: "reason", label: "Lý do", ph: "we are still waiting for data from the client" },
      { k: "newdate", label: "Ngày hoàn thành mới", ph: "Wednesday, May 15" }
    ],
    subject: "Update: {task} – new date {newdate}",
    body: "Hi {boss},\n\nI'm writing to let you know that {task} will not be ready by the original deadline. This is because {reason}. I'm sorry for the delay.\n\nThe new completion date is {newdate}. I'll keep you updated and let you know right away if anything changes.\n\nBest regards,\n{me}",
    tone: {
      polite: "Dear {boss},\n\nI'm sorry to let you know that {task} will not be ready by the original deadline, as {reason}.\n\nI now expect to complete it by {newdate}. I apologize for any inconvenience, and I will keep you informed of my progress.\n\nKind regards,\n{me}",
      short: "Hi {boss}, sorry, {task} is delayed because {reason}. The new date is {newdate}. I'll keep you posted."
    } },

  { id: "extension", track: "*", kind: "email", title: "Xin gia hạn", vi: "Xin thêm thời gian trước khi đến hạn",
    fields: [
      { k: "boss", label: "Tên người nhận", ph: "Anna" },
      { k: "task", label: "Việc cần gia hạn", ph: "the training plan" },
      { k: "deadline", label: "Hạn hiện tại", ph: "this Friday" },
      { k: "reason", label: "Lý do", ph: "the client changed some requirements" },
      { k: "newdate", label: "Hạn mới đề xuất", ph: "next Tuesday" }
    ],
    subject: "Extension request – {task}",
    body: "Hi {boss},\n\nCould I have a little more time for {task}? The current deadline is {deadline}.\n\nI need extra time because {reason}. Would it be possible to move the deadline to {newdate}? This will help me deliver good quality work.\n\nPlease let me know what you think.\n\nThank you,\n{me}",
    tone: {
      short: "Hi {boss}, could I move the deadline for {task} from {deadline} to {newdate}? I need a bit more time because {reason}."
    } },

  { id: "followup", track: "*", kind: "email", title: "Nhắc hạn (follow-up)", vi: "Nhắc nhẹ khi chưa nhận được phản hồi",
    fields: [
      { k: "name", label: "Tên người nhận", ph: "David" },
      { k: "item", label: "Việc cần nhắc", ph: "the signed contract" },
      { k: "sent", label: "Đã gửi lúc", ph: "last Monday" },
      { k: "need", label: "Cần phản hồi trước", ph: "Thursday, May 16" }
    ],
    subject: "Follow-up: {item}",
    body: "Hi {name},\n\nI'm just following up on my email from {sent} about {item}.\n\nCould you please get back to me by {need}? We need your reply to move to the next step.\n\nPlease let me know if you need anything from me.\n\nThank you,\n{me}",
    tone: {
      polite: "Dear {name},\n\nI hope you are well. I'm writing to follow up on my email from {sent} regarding {item}.\n\nI understand you are busy, but I would be grateful if you could reply by {need}.\n\nThank you in advance,\n{me}",
      short: "Hi {name}, just a quick reminder about {item}. Could you get back to me by {need}? Thanks!"
    } },

  { id: "meeting_confirm", track: "*", kind: "email", title: "Xác nhận lịch họp", vi: "Chốt chủ đề, giờ, địa điểm họp",
    fields: [
      { k: "name", label: "Tên người nhận", ph: "David" },
      { k: "topic", label: "Chủ đề họp", ph: "the Q3 plan" },
      { k: "time", label: "Thời gian", ph: "Tuesday, May 14, 10:00 AM" },
      { k: "place", label: "Địa điểm / link", ph: "Meeting Room 2" }
    ],
    subject: "Meeting confirmed: {topic} – {time}",
    body: "Hi {name},\n\nI'm writing to confirm our meeting:\n\nTopic: {topic}\nTime: {time}\nPlace: {place}\n\nPlease let me know if anything changes. See you then.\n\nBest regards,\n{me}",
    tone: {
      short: "Hi {name}, confirming our meeting about {topic}: {time}, {place}. See you then!"
    } },

  { id: "meeting_move", track: "*", kind: "email", title: "Dời lịch họp", vi: "Xin đổi giờ họp, đề xuất giờ mới",
    fields: [
      { k: "name", label: "Tên người nhận", ph: "David" },
      { k: "topic", label: "Chủ đề họp", ph: "the Q3 plan" },
      { k: "old", label: "Giờ cũ", ph: "Tuesday at 10:00 AM" },
      { k: "newtime", label: "Giờ mới đề xuất", ph: "Wednesday at 2:00 PM" }
    ],
    subject: "Reschedule request: {topic}",
    body: "Hi {name},\n\nI'm sorry, but I can't make our meeting about {topic} on {old}.\n\nWould it be possible to move it to {newtime}? If that doesn't work for you, please suggest another time that suits you.\n\nSorry for any inconvenience.\n\nBest regards,\n{me}",
    tone: {
      polite: "Dear {name},\n\nI'm very sorry, but something urgent has come up, and I won't be able to attend our meeting about {topic} on {old}.\n\nWould {newtime} be convenient for you? I'm also happy to adjust to your schedule.\n\nI apologize for the short notice.\n\nKind regards,\n{me}",
      short: "Hi {name}, sorry, I can't make our meeting about {topic} on {old}. Could we move it to {newtime}?"
    } },

  { id: "attach", track: "*", kind: "email", title: "Gửi tài liệu kèm", vi: "Gửi file đính kèm, nhờ xem và góp ý",
    fields: [
      { k: "name", label: "Tên người nhận", ph: "David" },
      { k: "doc", label: "Tài liệu gửi kèm", ph: "the updated price list" },
      { k: "purpose", label: "Dùng cho việc gì", ph: "tomorrow's meeting" },
      { k: "date", label: "Góp ý trước ngày", ph: "Friday" }
    ],
    subject: "Attached: {doc}",
    body: "Hi {name},\n\nPlease find attached {doc} for {purpose}.\n\nCould you please review it and send me your feedback by {date}? If you have any questions or need any changes, just let me know.\n\nBest regards,\n{me}",
    tone: {
      short: "Hi {name}, I've sent you {doc} for {purpose}. Could you take a look and give me feedback by {date}? Thanks!"
    } },

  { id: "thanks_meeting", track: "*", kind: "email", title: "Cảm ơn sau họp", vi: "Cảm ơn, tóm tắt bước tiếp theo",
    fields: [
      { k: "name", label: "Tên người nhận", ph: "David" },
      { k: "topic", label: "Chủ đề họp", ph: "the new website" },
      { k: "next", label: "Bước tiếp theo", ph: "to finalize the budget" },
      { k: "date", label: "Cập nhật trước ngày", ph: "next Monday" }
    ],
    subject: "Thank you – {topic}",
    body: "Hi {name},\n\nThank you for your time today. Our meeting about {topic} was very helpful.\n\nAs we agreed, the next step is {next}. I'll send you an update by {date}.\n\nPlease let me know if I missed anything.\n\nBest regards,\n{me}",
    tone: {
      short: "Thanks for the meeting today, {name}! As agreed, the next step is {next}. I'll update you by {date}."
    } },

  { id: "apology", track: "*", kind: "email", title: "Xin lỗi vì sai sót", vi: "Nhận lỗi, nói đã sửa thế nào",
    fields: [
      { k: "name", label: "Tên người nhận", ph: "David" },
      { k: "mistake", label: "Sai sót gì", ph: "the wrong price in yesterday's quote" },
      { k: "fix", label: "Đã khắc phục thế nào (dạng đã làm: sent…, fixed…)", ph: "sent you the corrected quote" }
    ],
    subject: "Apology and correction",
    body: "Hi {name},\n\nI'm sorry for {mistake}. That was my mistake.\n\nI have already {fix}. I've also added an extra check to my process, so this won't happen again.\n\nThank you for your patience. Please let me know if you have any questions.\n\nBest regards,\n{me}",
    tone: {
      polite: "Dear {name},\n\nPlease accept my sincere apologies for {mistake}. I take full responsibility for this.\n\nI have already {fix}, and I have added an extra check to make sure it does not happen again.\n\nThank you for your understanding.\n\nKind regards,\n{me}",
      short: "Hi {name}, sorry for {mistake}. I have already {fix}. It won't happen again."
    } },

  { id: "clarify", track: "*", kind: "email", title: "Hỏi lại cho rõ", vi: "Hỏi lại điểm chưa rõ, nêu cách mình hiểu",
    fields: [
      { k: "name", label: "Tên người nhận", ph: "David" },
      { k: "topic", label: "Về việc gì", ph: "the new report format" },
      { k: "question", label: "Điểm chưa rõ", ph: "which template we should use" },
      { k: "guess", label: "Mình đang hiểu là", ph: "we should use the new template from May" }
    ],
    subject: "Quick question about {topic}",
    body: "Hi {name},\n\nThank you for your message about {topic}. I want to make sure I understand it correctly.\n\nCould you please clarify {question}? My understanding is that {guess}. Is that right?\n\nThank you,\n{me}",
    tone: {
      short: "Hi {name}, quick question about {topic}: could you clarify {question}? I think {guess}. Is that right?"
    } },

  { id: "progress", track: "*", kind: "email", title: "Báo cáo tiến độ ngắn", vi: "Đã xong gì, sắp làm gì, vướng gì",
    fields: [
      { k: "boss", label: "Tên người nhận", ph: "Anna" },
      { k: "project", label: "Dự án / việc", ph: "the new website" },
      { k: "done", label: "Đã xong", ph: "the home page and the contact form" },
      { k: "next", label: "Sắp làm", ph: "testing on mobile" },
      { k: "issue", label: "Vướng mắc", ph: "none at the moment", def: "none at the moment" }
    ],
    subject: "Progress update – {project}",
    body: "Hi {boss},\n\nHere is a quick update on {project}.\n\nDone: {done}\nNext: {next}\nIssues: {issue}\n\nPlease let me know if you have any questions.\n\nBest regards,\n{me}",
    tone: {
      short: "Update on {project}. Done: {done}. Next: {next}. Issues: {issue}."
    } },

  { id: "approval", track: "*", kind: "email", title: "Xin phê duyệt", vi: "Xin sếp duyệt việc gì, vì sao, trước ngày nào",
    fields: [
      { k: "boss", label: "Tên người duyệt", ph: "Anna" },
      { k: "item", label: "Cần duyệt gì", ph: "the purchase of two new monitors" },
      { k: "reason", label: "Lý do", ph: "our old monitors often break down" },
      { k: "date", label: "Cần duyệt trước", ph: "Wednesday" }
    ],
    subject: "Approval needed: {item}",
    body: "Hi {boss},\n\nCould you please approve {item}?\n\nWe need it because {reason}. I've attached the details for your review.\n\nIf possible, I'd like your approval by {date} so we can stay on schedule.\n\nThank you,\n{me}",
    tone: {
      short: "Hi {boss}, could you approve {item} by {date}? We need it because {reason}. Thanks!"
    } },

  { id: "intro_team", track: "*", kind: "email", title: "Giới thiệu bản thân với đội mới", vi: "Chào cả đội ngày đầu vào làm",
    fields: [
      { k: "role", label: "Vị trí của bạn", ph: "QA engineer" },
      { k: "before", label: "Trước đây làm gì (công việc, nơi làm)", ph: "a tester at a software company for two years" },
      { k: "hobby", label: "Sở thích", ph: "cooking and playing badminton" }
    ],
    subject: "Hello from {me}, new {role}",
    body: "Hi everyone,\n\nMy name is {me}, and I've just joined the team as the new {role}.\n\nBefore this, I worked as {before}. I'm looking forward to working with all of you and learning from you.\n\nOutside work, I enjoy {hobby}.\n\nPlease feel free to say hi or message me any time.\n\nBest regards,\n{me}",
    tone: {
      short: "Hi everyone! I'm {me}, the new {role}. I'm looking forward to working with you all!"
    } },

  { id: "ask_help", track: "*", kind: "email", title: "Nhờ giúp đỡ", vi: "Nhờ đồng nghiệp giúp một việc cụ thể",
    fields: [
      { k: "name", label: "Tên người nhận", ph: "Minh" },
      { k: "task", label: "Việc đang làm", ph: "the monthly report" },
      { k: "ask", label: "Nhờ làm gì", ph: "show me how to use the new report tool" },
      { k: "time", label: "Mất khoảng", ph: "15 minutes" }
    ],
    subject: "Could you help me with {task}?",
    body: "Hi {name},\n\nI hope you're doing well. I'm working on {task}, and I'd really appreciate your help.\n\nCould you {ask}? It should only take about {time}.\n\nIf you're busy now, no problem. Just let me know a better time.\n\nThank you so much,\n{me}",
    tone: {
      short: "Hi {name}, could you {ask}? It's for {task} and should only take about {time}. Thanks a lot!"
    } },

  /* ============ CÔNG SỞ (office) ============ */

  { id: "office_minutes", track: "office", kind: "email", title: "Gửi tóm tắt cuộc họp", vi: "Quyết định, việc cần làm, lịch họp sau",
    fields: [
      { k: "topic", label: "Chủ đề họp", ph: "the year-end party" },
      { k: "date", label: "Ngày họp", ph: "May 10" },
      { k: "decision", label: "Đã quyết định", ph: "the party will be on December 20" },
      { k: "actions", label: "Việc cần làm (ai – gì)", ph: "Lan books the venue, Nam prepares the budget" },
      { k: "next", label: "Họp lần sau", ph: "Friday, May 17 at 3:00 PM" }
    ],
    subject: "Meeting notes – {topic} ({date})",
    body: "Hi team,\n\nThank you for joining the meeting about {topic} on {date}. Here is a short summary.\n\nDecisions: {decision}\nAction items: {actions}\nNext meeting: {next}\n\nPlease let me know if I missed anything.\n\nBest regards,\n{me}",
    tone: {
      short: "Notes from our meeting about {topic} ({date}): {decision}. Action items: {actions}. Next meeting: {next}."
    } },

  { id: "office_interview_invite", track: "office", kind: "email", title: "Mời ứng viên phỏng vấn", vi: "HR mời phỏng vấn, xin xác nhận",
    fields: [
      { k: "name", label: "Tên ứng viên", ph: "Mr. Tuan" },
      { k: "role", label: "Vị trí", ph: "Sales Assistant" },
      { k: "time", label: "Thời gian", ph: "Thursday, May 16, 9:00 AM" },
      { k: "place", label: "Địa điểm / link", ph: "5th floor, 12 Le Loi Street" }
    ],
    subject: "Interview invitation – {role}",
    body: "Dear {name},\n\nThank you for applying for the {role} position. We would like to invite you to an interview.\n\nTime: {time}\nPlace: {place}\n\nPlease reply to confirm that this time works for you. If not, we are happy to find another time.\n\nWe look forward to meeting you.\n\nBest regards,\n{me}",
    tone: {
      short: "Hello {name}, we'd like to invite you to an interview for the {role} position. Time: {time}. Place: {place}. Could you please confirm?"
    } },

  { id: "office_apply", track: "office", kind: "email", title: "Gửi CV ứng tuyển", vi: "Ứng viên gửi email ứng tuyển kèm CV",
    fields: [
      { k: "name", label: "Tên người tuyển dụng", ph: "Ms. Linh" },
      { k: "role", label: "Vị trí ứng tuyển", ph: "Office Administrator" },
      { k: "source", label: "Thấy tin tuyển ở đâu", ph: "your company website" },
      { k: "strength", label: "Điểm mạnh / kinh nghiệm", ph: "two years of experience in office administration" }
    ],
    subject: "Application for {role} – {me}",
    body: "Dear {name},\n\nI'm writing to apply for the {role} position that I saw on {source}.\n\nI have {strength}, and I believe I can bring this experience to your team.\n\nPlease find my CV attached. I would be happy to talk more at a time that suits you.\n\nThank you for your time and consideration.\n\nBest regards,\n{me}",
    tone: {
      short: "Hello {name}, I'd like to apply for the {role} position. I have {strength}. May I send you my CV?"
    } },

  /* ============ IT ============ */

  { id: "it_bug_client", track: "it", kind: "email", title: "Báo lỗi (bug) cho khách", vi: "Báo khách lỗi, ảnh hưởng, cách tạm, ngày sửa",
    fields: [
      { k: "name", label: "Tên khách", ph: "Mr. Brown" },
      { k: "issue", label: "Lỗi gì", ph: "users cannot upload files larger than 5 MB" },
      { k: "impact", label: "Ảnh hưởng", ph: "some users cannot attach reports" },
      { k: "workaround", label: "Cách xử lý tạm", ph: "split large files into smaller parts" },
      { k: "eta", label: "Dự kiến sửa xong", ph: "Friday, May 10" }
    ],
    subject: "Issue report: {issue}",
    body: "Dear {name},\n\nWe have found an issue in the system and would like to let you know.\n\nIssue: {issue}\nImpact: {impact}\nWorkaround: {workaround}\n\nOur team is working on a fix, and we expect to release it by {eta}. We will update you as soon as it is fixed.\n\nWe're sorry for the inconvenience.\n\nBest regards,\n{me}",
    tone: {
      short: "Hi {name}, we found an issue: {issue}. For now, please {workaround}. We expect to fix it by {eta}."
    } },

  { id: "it_release_note", track: "it", kind: "email", title: "Release note ngắn", vi: "Thông báo phiên bản mới: có gì mới, sửa gì",
    fields: [
      { k: "version", label: "Phiên bản", ph: "2.4.0" },
      { k: "date", label: "Ngày phát hành", ph: "May 10" },
      { k: "new", label: "Tính năng mới", ph: "CSV export on the report page" },
      { k: "fixed", label: "Lỗi đã sửa", ph: "the login error on older phones" },
      { k: "note", label: "Lưu ý", ph: "please log out and log in again after the update" }
    ],
    subject: "Release notes – version {version}",
    body: "Hi all,\n\nVersion {version} was released on {date}. Here are the main changes.\n\nNew: {new}\nFixed: {fixed}\nNote: {note}\n\nIf you see any problems, please let us know.\n\nBest regards,\n{me}",
    tone: {
      short: "Version {version} is live! New: {new}. Fixed: {fixed}."
    } },

  { id: "it_spec_confirm_jp", track: "it", kind: "email", title: "Xin xác nhận spec với khách Nhật", vi: "Hỏi 2 điểm spec, lịch sự kiểu khách Nhật",
    fields: [
      { k: "name", label: "Họ người nhận (Nhật)", ph: "Tanaka" },
      { k: "feature", label: "Chức năng", ph: "the order history screen" },
      { k: "q1", label: "Câu hỏi 1", ph: "Should the date format be YYYY/MM/DD?" },
      { k: "q2", label: "Câu hỏi 2", ph: "How many orders should we show on one page?" },
      { k: "date", label: "Xin trả lời trước", ph: "Wednesday, May 15" }
    ],
    subject: "Specification check: {feature}",
    body: "Dear {name}-san,\n\nThank you for your continued support.\n\nWe are now working on {feature}. Before we continue, we would like to confirm the following points in the specification:\n\n1. {q1}\n2. {q2}\n\nCould you kindly reply by {date}? This will help us keep the schedule.\n\nIf it is easier, we are also happy to discuss this in a short online meeting.\n\nThank you for your time.\n\nBest regards,\n{me}",
    tone: {
      short: "Hello {name}-san, could you please confirm two points about {feature}? 1. {q1} 2. {q2} We would appreciate your reply by {date}."
    } },

  /* ============ KHÁCH SẠN · DU LỊCH (hotel) ============ */

  { id: "hotel_booking_confirm", track: "hotel", kind: "email", title: "Xác nhận đặt phòng", vi: "Gửi khách mã đặt phòng, loại phòng, ngày ở",
    fields: [
      { k: "guest", label: "Tên khách", ph: "Ms. Smith" },
      { k: "ref", label: "Mã đặt phòng", ph: "HB2051" },
      { k: "room", label: "Loại phòng", ph: "Deluxe Double Room, sea view" },
      { k: "checkin", label: "Ngày nhận phòng", ph: "May 20" },
      { k: "checkout", label: "Ngày trả phòng", ph: "May 23" }
    ],
    subject: "Booking confirmation – {ref}",
    body: "Dear {guest},\n\nThank you for choosing our hotel. We are pleased to confirm your booking.\n\nBooking number: {ref}\nRoom: {room}\nCheck-in: {checkin}\nCheck-out: {checkout}\n\nIf you need an airport transfer or have any special requests, please reply to this email.\n\nWe look forward to welcoming you.\n\nKind regards,\n{me}",
    tone: {
      short: "Hello {guest}, your booking {ref} is confirmed: {room}, {checkin} to {checkout}. We look forward to welcoming you!"
    } },

  { id: "hotel_complaint_reply", track: "hotel", kind: "email", title: "Trả lời phàn nàn của khách", vi: "Xin lỗi, nói đã xử lý gì, đề nghị bù đắp",
    fields: [
      { k: "guest", label: "Tên khách", ph: "Mr. Lee" },
      { k: "problem", label: "Khách phàn nàn gì", ph: "the noise from the street" },
      { k: "action", label: "Đã xử lý thế nào (dạng đã làm: shared…, fixed…)", ph: "shared your feedback with our maintenance team" },
      { k: "offer", label: "Bù đắp cho khách", ph: "10% off your next stay" }
    ],
    subject: "Our apologies – {problem}",
    body: "Dear {guest},\n\nThank you for your feedback, and we are very sorry about {problem}. This is not the experience we want for our guests.\n\nWe have {action}. As a small apology, we would like to offer you {offer}.\n\nWe hope to have the chance to welcome you again.\n\nKind regards,\n{me}",
    tone: {
      short: "Dear {guest}, we're very sorry about {problem}. We have {action}, and we'd like to offer you {offer}."
    } },

  { id: "hotel_airport_pickup", track: "hotel", kind: "email", title: "Thông tin đón sân bay", vi: "Ngày, chuyến bay, tài xế, số điện thoại",
    fields: [
      { k: "guest", label: "Tên khách", ph: "Ms. Smith" },
      { k: "date", label: "Ngày đón", ph: "May 20" },
      { k: "flight", label: "Chuyến bay", ph: "NN123, arriving at 3:15 PM" },
      { k: "driver", label: "Tên tài xế", ph: "Mr. Hai" },
      { k: "phone", label: "SĐT tài xế", ph: "+84 912 345 678" }
    ],
    subject: "Airport pickup details – {date}",
    body: "Dear {guest},\n\nHere are the details of your airport pickup.\n\nDate: {date}\nFlight: {flight}\nDriver: {driver}\nDriver's phone: {phone}\n\nThe driver will wait for you in the arrival hall with a sign showing your name. If your flight is delayed, don't worry. We will check your flight status and adjust the pickup time.\n\nHave a safe trip, and see you soon.\n\nKind regards,\n{me}",
    tone: {
      short: "Hello {guest}, your driver {driver} will meet you in the arrival hall on {date} (flight {flight}). Driver's phone: {phone}."
    } },

  /* ============ BÁN HÀNG · CSKH (sales) ============ */

  { id: "sales_quote", track: "sales", kind: "email", title: "Gửi báo giá", vi: "Gửi báo giá kèm file, giá và hạn hiệu lực",
    fields: [
      { k: "name", label: "Tên khách", ph: "Mr. Brown" },
      { k: "product", label: "Sản phẩm / dịch vụ", ph: "500 office chairs" },
      { k: "price", label: "Tổng giá", ph: "USD 24,500 (VAT included)" },
      { k: "valid", label: "Hiệu lực đến", ph: "May 31" }
    ],
    subject: "Quotation – {product}",
    body: "Dear {name},\n\nThank you for your request. Please find attached our quotation for {product}.\n\nTotal price: {price}\nValid until: {valid}\n\nIf you have any questions or would like to discuss the details, I'd be happy to arrange a call.\n\nBest regards,\n{me}",
    tone: {
      short: "Hi {name}, I've sent you our quotation for {product}: {price}, valid until {valid}. Happy to answer any questions!"
    } },

  { id: "sales_ticket_reply", track: "sales", kind: "email", title: "Trả lời khiếu nại (ticket)", vi: "CSKH xin lỗi, nêu cách giải quyết, thời gian",
    fields: [
      { k: "name", label: "Tên khách", ph: "Ms. Garcia" },
      { k: "ticket", label: "Mã yêu cầu", ph: "58213" },
      { k: "issue", label: "Vấn đề của khách", ph: "your damaged order" },
      { k: "solution", label: "Sẽ giải quyết thế nào", ph: "send you a replacement free of charge" },
      { k: "time", label: "Trong thời gian", ph: "3 working days" }
    ],
    subject: "Your request #{ticket} – update",
    body: "Dear {name},\n\nThank you for contacting us about request #{ticket}, and we're sorry for the trouble with {issue}.\n\nWe have checked your case and will {solution}. You should see the result within {time}.\n\nIf the problem continues, please reply to this email, and we will help you right away.\n\nThank you for your patience.\n\nBest regards,\n{me}\nCustomer Support",
    tone: {
      short: "Hi {name}, sorry for the trouble with {issue}. We will {solution} within {time}. Request number: #{ticket}."
    } },

  { id: "sales_lead_followup", track: "sales", kind: "email", title: "Follow-up khách sau cuộc gọi", vi: "Cảm ơn khách tiềm năng, hẹn bước tiếp theo",
    fields: [
      { k: "name", label: "Tên khách", ph: "Mr. Kim" },
      { k: "topic", label: "Đã bàn về", ph: "your delivery needs" },
      { k: "benefit", label: "Lợi ích cho khách", ph: "reduce delivery time by about 20%" },
      { k: "time", label: "Đề xuất lịch gọi", ph: "Thursday afternoon" }
    ],
    subject: "Following up on our call",
    body: "Hi {name},\n\nThank you for taking the time to speak with me about {topic}.\n\nAs we discussed, our solution can help you {benefit}. I've attached a short brochure with more details.\n\nWould you be free for a short call on {time} to discuss the next steps?\n\nBest regards,\n{me}",
    tone: {
      short: "Hi {name}, thanks for the call today! Would {time} work for a quick follow-up about {topic}?"
    } },

  /* ============ SẢN XUẤT · NHÀ MÁY (factory) ============ */

  { id: "factory_quality_supplier", track: "factory", kind: "email", title: "Báo lỗi chất lượng cho nhà cung cấp", vi: "Hàng nhập lỗi, giữ lô, xin phân tích nguyên nhân",
    fields: [
      { k: "name", label: "Tên người nhận", ph: "Mr. Chen" },
      { k: "part", label: "Tên linh kiện / hàng", ph: "plastic cover A-120" },
      { k: "lot", label: "Số lô", ph: "L2405-07" },
      { k: "defect", label: "Lỗi gì, bao nhiêu", ph: "scratches on the surface, 35 of 500 pieces" },
      { k: "date", label: "Xin trả lời trước", ph: "May 17" }
    ],
    subject: "Quality issue – {part}, lot {lot}",
    body: "Dear {name},\n\nDuring our incoming inspection, we found a quality problem with {part} (lot {lot}).\n\nDefect: {defect}\n\nWe have put this lot on hold. The photos and the inspection report are attached.\n\nCould you please send us your root cause analysis and corrective action plan by {date}? Please also let us know when you can send replacement parts.\n\nThank you for your quick support.\n\nBest regards,\n{me}",
    tone: {
      short: "Hi {name}, we found a defect in {part} (lot {lot}): {defect}. The lot is on hold. Please send your root cause and action plan by {date}."
    } },

  { id: "factory_machine_down", track: "factory", kind: "chat", title: "Báo dừng máy", vi: "Nhắn nhóm: máy dừng lúc nào, lỗi gì, khi nào chạy lại",
    fields: [
      { k: "line", label: "Chuyền số", ph: "3" },
      { k: "machine", label: "Máy nào", ph: "the packing machine" },
      { k: "time", label: "Dừng lúc", ph: "10:15 AM" },
      { k: "problem", label: "Lỗi (nếu biết)", ph: "motor error, cause not known yet" },
      { k: "eta", label: "Dự kiến chạy lại", ph: "around 11:30 AM" }
    ],
    subject: "",
    body: "Line {line} update: {machine} stopped at {time}. Problem: {problem}. Maintenance is checking it now. Expected restart: {eta}. I'll update you when it's running again.",
    tone: {
      polite: "Hi, I'd like to report that {machine} on Line {line} stopped at {time}. Problem: {problem}. The maintenance team is working on it, and we expect to restart {eta}. I'll send another update soon."
    } },

  { id: "factory_audit_confirm", track: "factory", kind: "email", title: "Xác nhận lịch audit", vi: "Chốt ngày audit, phạm vi, hỏi tài liệu cần chuẩn bị",
    fields: [
      { k: "name", label: "Tên người nhận", ph: "Ms. Tanaka" },
      { k: "audit", label: "Loại audit", ph: "customer quality audit" },
      { k: "date", label: "Ngày audit", ph: "Tuesday, June 4" },
      { k: "scope", label: "Phạm vi", ph: "production line 2 and the warehouse" }
    ],
    subject: "Audit confirmation – {date}",
    body: "Dear {name},\n\nThank you for your email. We are pleased to confirm the {audit} at our factory on {date}.\n\nScope: {scope}\n\nWe will share the agenda and the list of attendees before the audit. Please let us know if you need any documents in advance or have any special requests for the visit.\n\nWe look forward to welcoming you.\n\nBest regards,\n{me}",
    tone: {
      short: "Hi {name}, confirming the {audit} on {date}. Scope: {scope}. We'll send the agenda soon."
    } },

  /* ============ LOGISTICS · XNK (logistics) ============ */

  { id: "log_shipment_delay", track: "logistics", kind: "email", title: "Báo chậm lô hàng", vi: "Lô hàng trễ, lý do, ETA cũ và mới",
    fields: [
      { k: "name", label: "Tên người nhận", ph: "Mr. Park" },
      { k: "ref", label: "Số lô / booking", ph: "BK-240512" },
      { k: "reason", label: "Lý do", ph: "port congestion in Singapore" },
      { k: "oldeta", label: "ETA cũ", ph: "May 18" },
      { k: "neweta", label: "ETA mới", ph: "May 22" }
    ],
    subject: "Shipment delay – {ref}",
    body: "Dear {name},\n\nWe're sorry to inform you that shipment {ref} has been delayed.\n\nReason: {reason}\nOriginal ETA: {oldeta}\nNew ETA: {neweta}\n\nWe are following the shipment closely and will update you if anything changes. We apologize for the inconvenience.\n\nBest regards,\n{me}",
    tone: {
      short: "Hi {name}, shipment {ref} is delayed because of {reason}. New ETA: {neweta} (was {oldeta}). Sorry for the inconvenience."
    } },

  { id: "log_docs_request", track: "logistics", kind: "email", title: "Yêu cầu chứng từ", vi: "Xin chứng từ để làm thủ tục hải quan",
    fields: [
      { k: "name", label: "Tên người nhận", ph: "Ms. Wong" },
      { k: "ref", label: "Số lô / booking", ph: "BK-240512" },
      { k: "docs", label: "Chứng từ còn thiếu", ph: "commercial invoice, packing list and certificate of origin" },
      { k: "date", label: "Cần trước ngày", ph: "Wednesday, May 15" }
    ],
    subject: "Documents needed – {ref}",
    body: "Dear {name},\n\nTo prepare customs clearance for shipment {ref}, we need the following documents: {docs}.\n\nCould you please send them by {date}? Without them, the goods may stay at the port longer, and extra storage fees may apply.\n\nThank you for your support.\n\nBest regards,\n{me}",
    tone: {
      short: "Hi {name}, for shipment {ref} we still need: {docs}. Could you send them by {date}? Thanks!"
    } },

  { id: "log_freight_quote", track: "logistics", kind: "email", title: "Báo giá cước", vi: "Báo cước theo tuyến, hàng, giá, hiệu lực",
    fields: [
      { k: "name", label: "Tên khách", ph: "Mr. Park" },
      { k: "route", label: "Tuyến", ph: "Ho Chi Minh City to Busan" },
      { k: "cargo", label: "Hàng / container", ph: "one 40-foot container of furniture" },
      { k: "rate", label: "Giá cước", ph: "USD 1,250 per container" },
      { k: "valid", label: "Hiệu lực đến", ph: "May 31" }
    ],
    subject: "Freight quotation – {route}",
    body: "Dear {name},\n\nThank you for your inquiry. Please see our freight rate below.\n\nRoute: {route}\nCargo: {cargo}\nRate: {rate}\nValid until: {valid}\n\nThis rate does not include local charges, duties or taxes. Space is subject to availability at the time of booking.\n\nPlease let us know if you would like to go ahead with the booking.\n\nBest regards,\n{me}",
    tone: {
      short: "Hi {name}, our rate for {route} ({cargo}) is {rate}, valid until {valid}. Local charges not included. Shall we book?"
    } },

  /* ============ TÀI CHÍNH · KẾ TOÁN (finance) ============ */

  { id: "fin_payment_reminder", track: "finance", kind: "email", title: "Nhắc thanh toán hoá đơn", vi: "Nhắc nhẹ hoá đơn quá hạn",
    fields: [
      { k: "name", label: "Tên người nhận", ph: "Mr. Davis" },
      { k: "invoice", label: "Số hoá đơn", ph: "INV-0425" },
      { k: "amount", label: "Số tiền", ph: "USD 3,200" },
      { k: "due", label: "Hạn thanh toán", ph: "April 30" }
    ],
    subject: "Payment reminder – invoice {invoice}",
    body: "Dear {name},\n\nI hope you are well. This is a friendly reminder that invoice {invoice} for {amount} was due on {due}, and we have not received the payment yet.\n\nCould you please check and arrange the payment at your earliest convenience? If you have already paid, please ignore this reminder, or send us the payment details so we can check.\n\nThank you,\n{me}\nAccounts Department",
    tone: {
      polite: "Dear {name},\n\nWe hope this message finds you well. According to our records, invoice {invoice} for {amount}, due on {due}, is still outstanding.\n\nWe would be grateful if you could arrange the payment soon. If the payment has already been made, please accept our thanks and send us the details so we can update our records.\n\nKind regards,\n{me}\nAccounts Department",
      short: "Hi {name}, a friendly reminder that invoice {invoice} for {amount} was due on {due}. Could you please check? Thank you!"
    } },

  { id: "fin_monthly_report", track: "finance", kind: "email", title: "Gửi báo cáo tháng", vi: "Gửi sếp báo cáo tài chính tháng + 2 điểm chính",
    fields: [
      { k: "boss", label: "Tên người nhận", ph: "Ms. Nguyen" },
      { k: "month", label: "Tháng", ph: "April 2026" },
      { k: "highlight", label: "Điểm nổi bật", ph: "revenue was 8% higher than in March" },
      { k: "issue", label: "Điểm cần lưu ý", ph: "office costs were 5% over budget" }
    ],
    subject: "Monthly financial report – {month}",
    body: "Hi {boss},\n\nPlease find attached the financial report for {month}.\n\nKey points:\n- {highlight}\n- {issue}\n\nI'm happy to go through the numbers with you if you have any questions.\n\nBest regards,\n{me}",
    tone: {
      short: "Hi {boss}, the {month} report is ready. Key points: {highlight}; {issue}. I've emailed you the file."
    } },

  { id: "fin_discrepancy", track: "finance", kind: "email", title: "Hỏi khoản chênh lệch", vi: "Đối chiếu công nợ lệch, xin chứng từ",
    fields: [
      { k: "name", label: "Tên người nhận", ph: "Ms. Tran" },
      { k: "period", label: "Kỳ đối chiếu", ph: "April 2026" },
      { k: "amount", label: "Số tiền lệch", ph: "USD 320" },
      { k: "date", label: "Xin trả lời trước", ph: "May 15" }
    ],
    subject: "Reconciliation query – {period}",
    body: "Dear {name},\n\nWhile checking our account balance with you for {period}, we found a difference of {amount} between our records and yours.\n\nCould you please check this on your side and send us any supporting documents, such as invoices or payment records? Our reconciliation is attached for your reference.\n\nWe would appreciate your reply by {date}.\n\nThank you,\n{me}",
    tone: {
      short: "Hi {name}, we found a difference of {amount} in our {period} balance. Could you check on your side and reply by {date}?"
    } },

  /* ============ MARKETING · TMĐT (marketing) ============ */

  { id: "mkt_campaign_report", track: "marketing", kind: "email", title: "Báo cáo kết quả chiến dịch", vi: "Kết quả, điều hiệu quả, bước tiếp theo",
    fields: [
      { k: "boss", label: "Tên người nhận", ph: "Anna" },
      { k: "campaign", label: "Tên chiến dịch", ph: "the summer sale campaign" },
      { k: "result", label: "Kết quả chính", ph: "1,200 orders, 15% above target" },
      { k: "learn", label: "Điều hiệu quả", ph: "short videos brought the most clicks" },
      { k: "next", label: "Bước tiếp theo", ph: "use more short videos in June" }
    ],
    subject: "Campaign results – {campaign}",
    body: "Hi {boss},\n\nHere is a quick summary of {campaign}.\n\nResults: {result}\nWhat worked: {learn}\nNext step: {next}\n\nThe full report is attached. I'm happy to discuss it at our next meeting.\n\nBest regards,\n{me}",
    tone: {
      short: "Quick results for {campaign}: {result}. What worked: {learn}. Next: {next}."
    } },

  { id: "mkt_content_approval", track: "marketing", kind: "chat", title: "Xin duyệt nội dung", vi: "Nhắn sếp/khách duyệt bài trước khi đăng",
    fields: [
      { k: "name", label: "Tên người duyệt", ph: "Anna" },
      { k: "content", label: "Nội dung gì", ph: "the Mother's Day post" },
      { k: "channel", label: "Đăng ở đâu", ph: "our fan page" },
      { k: "date", label: "Ngày đăng", ph: "Friday at 8:00 PM" }
    ],
    subject: "",
    body: "Hi {name}, the draft of {content} is ready for your review. We plan to post it on {channel} on {date}. Could you take a look and let me know if you'd like any changes? Thanks!",
    tone: {
      polite: "Hi {name}, I've prepared the draft of {content} for {channel}. We would like to post it on {date}. When you have a moment, could you please review it and share any comments? Thank you!"
    } },

  { id: "mkt_collab_invite", track: "marketing", kind: "email", title: "Mời hợp tác (KOL/creator)", vi: "Mời người sáng tạo nội dung hợp tác",
    fields: [
      { k: "name", label: "Tên người nhận", ph: "Linh" },
      { k: "product", label: "Sản phẩm / thương hiệu", ph: "our new green tea drink" },
      { k: "idea", label: "Ý tưởng hợp tác", ph: "a short review video" },
      { k: "offer", label: "Quyền lợi", ph: "a fixed fee and free products" }
    ],
    subject: "Collaboration idea for your channel",
    body: "Hi {name},\n\nMy name is {me}, and I work on the marketing team for {product}. We really enjoy your content, and we think your audience would like our product.\n\nWe'd love to work with you on {idea}. In return, we can offer {offer}.\n\nIf you're interested, I'd be happy to send more details or set up a short call.\n\nLooking forward to hearing from you.\n\nBest regards,\n{me}",
    tone: {
      short: "Hi {name}, I'm {me} from the marketing team for {product}. Would you be interested in {idea}? We can offer {offer}."
    } },

  /* ============ Y TẾ · ĐIỀU DƯỠNG (health) — chỉ thông tin hành chính, không tư vấn y khoa ============ */

  { id: "health_previsit", track: "health", kind: "email", title: "Hướng dẫn trước khám", vi: "Gửi bệnh nhân lưu ý trước buổi khám (theo chỉ định bác sĩ)",
    fields: [
      { k: "name", label: "Tên bệnh nhân", ph: "Mr. Johnson" },
      { k: "date", label: "Ngày giờ khám", ph: "Monday, May 13 at 9:30 AM" },
      { k: "prep", label: "Chuẩn bị (đúng chỉ định bác sĩ)", ph: "Please do not eat for 8 hours before your blood test, as your doctor advised." },
      { k: "bring", label: "Cần mang theo", ph: "your ID, insurance card and a list of the medicines you take" }
    ],
    subject: "Your appointment on {date} – how to prepare",
    body: "Dear {name},\n\nThank you for booking your appointment with us on {date}.\n\nTo prepare for your visit:\n- Please arrive 15 minutes early to check in.\n- {prep}\n- Please bring {bring}.\n\nIf you have any questions about these instructions, please contact the clinic. If you feel much worse before your appointment, please seek medical care right away.\n\nKind regards,\n{me}\nClinic Reception",
    tone: {
      short: "Hello {name}, for your appointment on {date}, please arrive 15 minutes early and bring {bring}. {prep}"
    } },

  { id: "health_appt_reminder", track: "health", kind: "chat", title: "Nhắc lịch hẹn", vi: "Tin nhắn nhắc bệnh nhân lịch khám",
    fields: [
      { k: "name", label: "Tên bệnh nhân", ph: "Ms. Taylor" },
      { k: "date", label: "Ngày giờ hẹn", ph: "Monday, May 13 at 9:30 AM" },
      { k: "place", label: "Địa điểm", ph: "our clinic on 25 Tran Phu Street" },
      { k: "phone", label: "SĐT phòng khám", ph: "028 3812 3456" }
    ],
    subject: "",
    body: "Hello {name}, this is a reminder of your appointment on {date} at {place}. Please arrive 15 minutes early. If you need to change or cancel, please call us at {phone}. Thank you!",
    tone: {
      polite: "Dear {name}, we would like to remind you of your appointment on {date} at {place}. Kindly arrive 15 minutes early. If you need to reschedule, please call us at {phone}. We look forward to seeing you."
    } },

  { id: "health_shift_handover", track: "health", kind: "chat", title: "Bàn giao ca cho bác sĩ", vi: "Nhắn bác sĩ tình trạng, việc đã làm, điểm cần lưu ý",
    fields: [
      { k: "doctor", label: "Tên bác sĩ", ph: "Lee" },
      { k: "patient", label: "Bệnh nhân / phòng", ph: "Mr. Nam, Room 12, Bed 2" },
      { k: "status", label: "Tình trạng hiện tại", ph: "stable, vital signs normal" },
      { k: "done", label: "Đã làm trong ca", ph: "blood test taken, results pending" },
      { k: "note", label: "Cần bác sĩ lưu ý", ph: "he reported mild pain at 3 PM" }
    ],
    subject: "",
    body: "Hi Dr. {doctor}, handover for {patient}:\n- Current status: {status}\n- Done this shift: {done}\n- Please note: {note}\nPlease let me know if you need more information.",
    tone: {
      polite: "Good evening Dr. {doctor}, here is my handover for {patient}.\n- Current status: {status}\n- Done this shift: {done}\n- For your attention: {note}\nPlease let me know if you need anything else. Thank you."
    } },

  /* ============ XÂY DỰNG · KỸ THUẬT (construction) ============ */

  { id: "con_rfi", track: "construction", kind: "email", title: "Gửi RFI (xin làm rõ bản vẽ)", vi: "Hỏi tư vấn thiết kế trước khi thi công tiếp",
    fields: [
      { k: "name", label: "Tên người nhận", ph: "Mr. Wilson" },
      { k: "ref", label: "Số RFI", ph: "RFI-015" },
      { k: "drawing", label: "Số bản vẽ", ph: "S-203, Level 3 slab" },
      { k: "question", label: "Câu hỏi", ph: "The beam size is different on S-203 and A-105. Which one should we follow?" },
      { k: "date", label: "Xin trả lời trước", ph: "May 16" }
    ],
    subject: "{ref} – drawing {drawing}",
    body: "Dear {name},\n\nWe need your clarification on the item below before we can continue the work on site.\n\nRFI No.: {ref}\nDrawing: {drawing}\nQuestion: {question}\n\nCould you please reply by {date}? A late reply may affect the construction schedule.\n\nThank you for your support.\n\nBest regards,\n{me}",
    tone: {
      short: "Hi {name}, we've sent {ref} about drawing {drawing}. Could you reply by {date}? It may affect the schedule."
    } },

  { id: "con_inspection_request", track: "construction", kind: "email", title: "Mời nghiệm thu", vi: "Báo hạng mục đã xong, mời kiểm tra",
    fields: [
      { k: "name", label: "Tên người nhận", ph: "Mr. Wilson" },
      { k: "work", label: "Hạng mục", ph: "rebar for the Level 3 slab" },
      { k: "location", label: "Vị trí", ph: "Block B, grid lines 1–4" },
      { k: "time", label: "Giờ đề xuất", ph: "Thursday, May 16, 8:00 AM" }
    ],
    subject: "Inspection request – {work}",
    body: "Dear {name},\n\nThe following work is ready for inspection:\n\nWork: {work}\nLocation: {location}\nProposed time: {time}\n\nPlease confirm if this time works for you. The inspection checklist is attached.\n\nBest regards,\n{me}",
    tone: {
      short: "Hi {name}, {work} ({location}) is ready for inspection. Does {time} work for you?"
    } },

  { id: "con_incident_report", track: "construction", kind: "email", title: "Báo sự cố an toàn", vi: "Báo nhanh sự cố/suýt tai nạn và việc đã làm ngay",
    fields: [
      { k: "name", label: "Tên người nhận", ph: "Mr. Harris" },
      { k: "time", label: "Thời gian", ph: "May 14, 2:30 PM" },
      { k: "place", label: "Vị trí", ph: "Block B, Level 5" },
      { k: "what", label: "Chuyện gì xảy ra", ph: "a steel pipe fell from the scaffold (no one was hurt)" },
      { k: "action", label: "Đã xử lý ngay", ph: "closed the area and checked all scaffold ties" }
    ],
    subject: "Incident report – {place}, {time}",
    body: "Dear {name},\n\nI'd like to report a safety incident on site.\n\nTime: {time}\nLocation: {place}\nWhat happened: {what}.\nImmediate action: we {action}.\n\nA full report with photos will follow. Please let me know if you need any more information.\n\nBest regards,\n{me}",
    tone: {
      short: "Safety incident at {place} ({time}): {what}. We {action}. Full report to follow."
    } },

  /* ============ HÀNG KHÔNG · SÂN BAY (aviation) ============ */

  { id: "avi_baggage_update", track: "aviation", kind: "email", title: "Cập nhật hành lý thất lạc", vi: "Báo khách số hồ sơ và tình trạng tìm hành lý",
    fields: [
      { k: "name", label: "Tên hành khách", ph: "Ms. Martin" },
      { k: "ref", label: "Số hồ sơ", ph: "SGN12345" },
      { k: "bag", label: "Mô tả hành lý", ph: "a large blue suitcase" },
      { k: "status", label: "Tình trạng hiện tại", ph: "we are checking with the transfer airport" }
    ],
    subject: "Your baggage report – {ref}",
    body: "Dear {name},\n\nWe're sorry that your baggage did not arrive with you. We have registered your report, and our team is tracing your bag.\n\nReference number: {ref}\nBag: {bag}\nCurrent status: {status}\n\nWhen we find your bag, we will contact you and arrange delivery. Please use your reference number whenever you contact us.\n\nThank you for your patience.\n\nKind regards,\n{me}\nBaggage Services",
    tone: {
      short: "Dear {name}, update on your bag ({ref}): {status}. We will contact you as soon as we find it."
    } },

  { id: "avi_flight_delay", track: "aviation", kind: "chat", title: "Thông báo chậm chuyến", vi: "Tin nhắn báo hành khách giờ bay mới, cửa ra",
    fields: [
      { k: "flight", label: "Số hiệu chuyến", ph: "NN245" },
      { k: "reason", label: "Lý do", ph: "bad weather" },
      { k: "newtime", label: "Giờ bay mới", ph: "4:40 PM" },
      { k: "gate", label: "Cửa ra", ph: "12" }
    ],
    subject: "",
    body: "Dear passenger, we're sorry to inform you that flight {flight} is delayed because of {reason}. The new departure time is {newtime}, from Gate {gate}. Please check the airport screens for updates. Thank you for your patience.",
    tone: {
      polite: "Dear passenger, we sincerely apologize that flight {flight} has been delayed due to {reason}. The new departure time is {newtime}, and boarding will be at Gate {gate}. Thank you for your patience and understanding."
    } },

  { id: "avi_assist_confirm", track: "aviation", kind: "email", title: "Xác nhận hỗ trợ đặc biệt", vi: "Xác nhận xe lăn / hỗ trợ cho hành khách",
    fields: [
      { k: "name", label: "Tên hành khách", ph: "Mr. Evans" },
      { k: "service", label: "Dịch vụ hỗ trợ", ph: "wheelchair assistance" },
      { k: "flight", label: "Số hiệu chuyến", ph: "NN245" },
      { k: "date", label: "Ngày bay", ph: "May 20" }
    ],
    subject: "Special assistance confirmed – flight {flight}",
    body: "Dear {name},\n\nWe're pleased to confirm your request for {service} on flight {flight} on {date}.\n\nPlease arrive at the check-in counter early and let our staff know about your request. Our team will help you through the airport and onto the aircraft.\n\nIf your plans change, please contact us as soon as possible.\n\nKind regards,\n{me}",
    tone: {
      short: "Dear {name}, your {service} for flight {flight} on {date} is confirmed. Please tell our check-in staff when you arrive."
    } },

  /* ============ GIÁO DỤC · ĐÀO TẠO (education) ============ */

  { id: "edu_progress_parent", track: "education", kind: "email", title: "Báo tiến bộ học sinh cho phụ huynh", vi: "Điểm tốt, điểm cần cố gắng, hẹn trao đổi",
    fields: [
      { k: "parent", label: "Tên phụ huynh", ph: "Mrs. Hoa" },
      { k: "student", label: "Tên học sinh", ph: "Minh Anh" },
      { k: "good", label: "Điểm tốt", ph: "speaking and group work" },
      { k: "work", label: "Cần cố gắng", ph: "spelling" },
      { k: "meet", label: "Có thể gặp lúc", ph: "on Thursday after 4 PM" }
    ],
    subject: "{student}'s progress update",
    body: "Dear {parent},\n\nI'd like to share a short update on {student}'s progress in class.\n\n{student} is doing well in {good}. One area to work on is {work}. We will keep practicing this in class, and a little practice at home would also help.\n\nIf you'd like to talk more, I'm available {meet}.\n\nBest regards,\n{me}",
    tone: {
      short: "Dear {parent}, {student} is doing well in {good}. A little extra practice in {work} at home would help. I'm free to talk {meet}."
    } },

  { id: "edu_event_notice", track: "education", kind: "email", title: "Thông báo sự kiện cho phụ huynh", vi: "Ngày, nơi, cần mang gì, hạn xác nhận",
    fields: [
      { k: "event", label: "Sự kiện", ph: "our class trip to the science museum" },
      { k: "date", label: "Ngày", ph: "Friday, May 24" },
      { k: "place", label: "Tập trung ở đâu, mấy giờ", ph: "the school gate at 7:30 AM" },
      { k: "bring", label: "Cần mang", ph: "a water bottle, a hat and a light lunch" },
      { k: "reply", label: "Xác nhận trước", ph: "Monday, May 20" }
    ],
    subject: "Notice: {event} on {date}",
    body: "Dear parents,\n\nWe are happy to invite your child to {event} on {date}. We will meet at {place}.\n\nYour child should bring {bring}.\n\nPlease reply to this email by {reply} to let us know if your child will join.\n\nIf you have any questions, please feel free to contact me.\n\nBest regards,\n{me}",
    tone: {
      short: "Dear parents, {event} is on {date}, and we will meet at {place}. Please bring {bring}, and reply by {reply}."
    } },

  { id: "edu_admissions_followup", track: "education", kind: "email", title: "Follow-up tư vấn tuyển sinh", vi: "Cảm ơn, nhắc bước tiếp theo, hạn nộp",
    fields: [
      { k: "name", label: "Tên người nhận", ph: "Mr. Quang" },
      { k: "program", label: "Chương trình", ph: "our English exam preparation course" },
      { k: "step", label: "Bước tiếp theo", ph: "to send us your latest school report" },
      { k: "date", label: "Hạn", ph: "June 5" }
    ],
    subject: "Your inquiry about {program}",
    body: "Dear {name},\n\nThank you for your interest in {program}. It was a pleasure speaking with you.\n\nAs we discussed, the next step is {step}. Please complete it by {date} so we can process your application on time.\n\nI've attached the program brochure and fee information. If you have any questions, please reply to this email or give me a call.\n\nBest regards,\n{me}\nAdmissions Team",
    tone: {
      short: "Hi {name}, thanks for your interest in {program}! The next step is {step}. Please complete it by {date}, and let me know if you have any questions."
    } },

  /* ============ LUẬT · HÀNH CHÍNH CÔNG (legal) — chỉ thủ tục/hành chính, không tư vấn pháp lý ============ */

  { id: "legal_missing_docs", track: "legal", kind: "email", title: "Báo hồ sơ còn thiếu", vi: "Một cửa báo giấy tờ cần bổ sung, nơi nộp, hạn",
    fields: [
      { k: "name", label: "Tên người nộp hồ sơ", ph: "Mr. Schmidt" },
      { k: "ref", label: "Số hồ sơ", ph: "HS-2026-0815" },
      { k: "missing", label: "Giấy tờ còn thiếu", ph: "a certified copy of your passport and two 4x6 photos" },
      { k: "place", label: "Nơi nộp bổ sung", ph: "Counter 3, District 1 Service Center" },
      { k: "date", label: "Hạn bổ sung", ph: "May 30" }
    ],
    subject: "Application {ref} – documents needed",
    body: "Dear {name},\n\nThank you for submitting application {ref}. After checking it, we found that the following documents are still missing: {missing}.\n\nPlease submit them at {place} by {date}. We will continue processing your application once we receive all the documents.\n\nIf you have any questions, please contact us.\n\nKind regards,\n{me}",
    tone: {
      short: "Hello {name}, for application {ref} we still need {missing}. Please submit them at {place} by {date}."
    } },

  { id: "legal_contract_comments", track: "legal", kind: "email", title: "Gửi góp ý dự thảo hợp đồng", vi: "Pháp chế gửi bản có track changes, xin phản hồi",
    fields: [
      { k: "name", label: "Tên người nhận", ph: "Ms. Clark" },
      { k: "contract", label: "Loại hợp đồng", ph: "service agreement" },
      { k: "points", label: "Điểm góp ý chính", ph: "payment terms (Clause 5) and termination notice (Clause 12)" },
      { k: "date", label: "Xin phản hồi trước", ph: "May 20" }
    ],
    subject: "Draft {contract} – our comments",
    body: "Dear {name},\n\nPlease find attached the draft {contract} with our comments in tracked changes.\n\nOur main comments are about {points}.\n\nCould you please review them and send us your feedback by {date}? We are happy to set up a call to discuss any of the points.\n\nBest regards,\n{me}",
    tone: {
      short: "Hi {name}, I've sent our comments on the draft {contract}, mainly about {points}. Could you reply by {date}?"
    } },

  { id: "legal_translation_order", track: "legal", kind: "email", title: "Xác nhận đơn dịch công chứng", vi: "Tài liệu, ngôn ngữ, phí, ngày nhận",
    fields: [
      { k: "name", label: "Tên khách", ph: "Ms. Lopez" },
      { k: "doc", label: "Tài liệu", ph: "birth certificate (2 pages)" },
      { k: "lang", label: "Ngôn ngữ", ph: "Vietnamese to English" },
      { k: "fee", label: "Phí", ph: "VND 450,000, notarization included" },
      { k: "date", label: "Ngày nhận bản dịch", ph: "Thursday, May 16, after 2 PM" }
    ],
    subject: "Translation order confirmed – {doc}",
    body: "Dear {name},\n\nThank you for your order. We are pleased to confirm the details below.\n\nDocument: {doc}\nLanguage: {lang}\nFee: {fee}\nReady for pickup: {date}\n\nPlease bring the original document when you come to collect the notarized translation. If you have any questions, please feel free to contact us.\n\nKind regards,\n{me}",
    tone: {
      short: "Hello {name}, your translation order is confirmed. Document: {doc}, {lang}. Ready on {date}. Fee: {fee}. Please bring the original."
    } }
];
