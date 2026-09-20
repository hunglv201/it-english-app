# -*- coding: utf-8 -*-
# Sinh curriculum 100 ngày cho app IT English.
# Nội dung soạn tay theo 10 chặng, phân bổ đều ra 100 ngày (có lặp lại để nhớ).
import json

# Mỗi phase: title, vocab[10] (t,ipa,pos,vi,ex,exVi), phrases[5] (en,vi,note),
# dialogues[2] (them,[(t,good,fb)x3]), listen[4] (sentence, [blank_words], hint)
PHASES = [
{
 "title":"Công việc hằng ngày",
 "vocab":[
  ("task","/tɑːsk/","n","công việc cần làm","I have three <b>tasks</b> today.","Hôm nay mình có ba task."),
  ("standup","/ˈstændʌp/","n","họp nhanh đầu ngày","The <b>standup</b> is at 9 a.m.","Standup lúc 9 giờ sáng."),
  ("blocker","/ˈblɒkər/","n","thứ chặn không cho làm tiếp","I have a <b>blocker</b> on this task.","Task này mình đang bị chặn."),
  ("in progress","/ɪn ˈprɒɡres/","phr","đang làm","This task is still <b>in progress</b>.","Task này vẫn đang làm."),
  ("backlog","/ˈbæklɒɡ/","n","danh sách việc còn tồn","It's still in the <b>backlog</b>.","Nó vẫn còn trong backlog."),
  ("priority","/praɪˈɒrəti/","n","mức ưu tiên","This bug is high <b>priority</b>.","Lỗi này ưu tiên cao."),
  ("deadline","/ˈdedlaɪn/","n","hạn chót","The <b>deadline</b> is Friday.","Hạn chót là thứ Sáu."),
  ("update","/ˈʌpdeɪt/","n/v","cập nhật (tình hình)","Here's a quick <b>update</b>.","Đây là cập nhật nhanh."),
  ("assign","/əˈsaɪn/","v","giao (việc) cho ai","This task is <b>assigned</b> to me.","Task này giao cho mình."),
  ("estimate","/ˈestɪmət/","n/v","ước lượng thời gian","My <b>estimate</b> is two days.","Mình ước lượng hai ngày."),
 ],
 "phrases":[
  ("Yesterday I finished the login API.","Hôm qua mình xong API login.",""),
  ("Today I'll work on the payment module.","Hôm nay mình làm module thanh toán.",""),
  ("I'm blocked because staging is down.","Mình đang bị chặn vì staging sập.","blocked = bị chặn"),
  ("No blockers from my side.","Phía mình không có gì vướng.",""),
  ("I'll need one more day for this.","Mình cần thêm một ngày cho cái này.",""),
 ],
 "dialogues":[
  ("How's the login feature going?",[
    ("It's almost done. I'll finish it today.",True,"Rõ, đúng thì hiện tại."),
    ("It is almost done, I finish today.",False,"Thiếu 'will': I'll finish it today."),
    ("Almost, today finish.",False,"Thiếu chủ ngữ và động từ, khó hiểu."),
  ]),
  ("Any blockers today?",[
    ("No blockers from my side.",True,"Cách trả lời gọn, tự nhiên."),
    ("No, I no have block.",False,"Nên là: No, I don't have any blockers."),
    ("Block no today me.",False,"Sai trật tự từ hoàn toàn."),
  ]),
 ],
 "listen":[
  ("Today I will work on the payment module",["work","payment"],"việc hôm nay làm"),
  ("The deadline for this task is Friday",["deadline","Friday"],"hạn chót"),
  ("This bug is high priority",["priority"],"mức ưu tiên"),
  ("I need one more day to finish",["finish"],"hoàn thành"),
 ],
},
{
 "title":"Git & quản lý mã",
 "vocab":[
  ("commit","/kəˈmɪt/","n/v","lưu một thay đổi vào git","I'll <b>commit</b> this change now.","Mình commit thay đổi này luôn."),
  ("branch","/brɑːntʃ/","n","nhánh code","Create a new <b>branch</b> for this.","Tạo một branch mới cho cái này."),
  ("merge","/mɜːrdʒ/","v","gộp code từ nhánh này vào nhánh khác","Can I <b>merge</b> this now?","Mình merge được chưa?"),
  ("pull request","/pʊl rɪˈkwest/","n","yêu cầu merge code (PR)","Please review my <b>pull request</b>.","Review PR của mình nhé."),
  ("clone","/kloʊn/","v","sao repo về máy","<b>Clone</b> the repo first.","Clone repo về trước đã."),
  ("push","/pʊʃ/","v","đẩy code lên server","I'll <b>push</b> my changes.","Mình push code lên đây."),
  ("pull","/pʊl/","v","kéo code mới nhất về","Did you <b>pull</b> the latest code?","Bạn pull code mới nhất chưa?"),
  ("merge conflict","/mɜːrdʒ ˈkɒnflɪkt/","n","xung đột khi gộp code","I got a <b>merge conflict</b>.","Mình bị merge conflict."),
  ("repository","/rɪˈpɒzɪtri/","n","kho code (repo)","The code is in this <b>repository</b>.","Code nằm trong repo này."),
  ("revert","/rɪˈvɜːrt/","v","hoàn tác một commit","Let's <b>revert</b> that commit.","Mình revert commit đó đi."),
 ],
 "phrases":[
  ("Did you pull the latest code?","Bạn pull code mới nhất chưa?",""),
  ("I'll push my changes now.","Mình push code lên đây.",""),
  ("Can you review my pull request?","Bạn review PR của mình được không?",""),
  ("I got a merge conflict in this file.","Mình bị merge conflict ở file này.",""),
  ("Let's create a new branch for this.","Tạo một branch mới cho cái này đi.",""),
 ],
 "dialogues":[
  ("Can you review my pull request?",[
    ("Sure, I'll take a look this afternoon.",True,"Tự nhiên, hẹn rõ thời gian."),
    ("Yes I see it now later.",False,"'now later' mâu thuẫn, khó hiểu."),
    ("OK, I review after.",False,"Nên là: I'll review it later."),
  ]),
  ("Why is the build broken?",[
    ("I think someone pushed without pulling first.",True,"Đưa ra phỏng đoán rõ ràng."),
    ("Build broken because push.",False,"Thiếu chủ ngữ và mạo từ."),
    ("I don't know, maybe git.",False,"Không giúp được gì cho người hỏi."),
  ]),
 ],
 "listen":[
  ("Please review my pull request today",["review","request"],"nhờ review PR"),
  ("I got a merge conflict in this file",["merge","conflict"],"xung đột code"),
  ("Did you pull the latest code",["pull","latest"],"kéo code mới"),
  ("Let me revert that commit",["revert","commit"],"hoàn tác"),
 ],
},
{
 "title":"Code review",
 "vocab":[
  ("code review","/koʊd rɪˈvjuː/","n","rà soát code trước khi merge","The <b>code review</b> found two bugs.","Buổi review tìm ra hai lỗi."),
  ("approve","/əˈpruːv/","v","duyệt (PR)","I'll <b>approve</b> it after one change.","Sửa một chỗ nữa là mình duyệt."),
  ("comment","/ˈkɒment/","n/v","góp ý trong review","I left a few <b>comments</b>.","Mình để lại vài góp ý."),
  ("feedback","/ˈfiːdbæk/","n","phản hồi","Thanks for the <b>feedback</b>.","Cảm ơn phản hồi nhé."),
  ("refactor","/ˌriːˈfæktər/","v","sửa code cho gọn, không đổi chức năng","We should <b>refactor</b> this later.","Nên refactor chỗ này sau."),
  ("readable","/ˈriːdəbl/","adj","dễ đọc","This code is more <b>readable</b> now.","Code này giờ dễ đọc hơn."),
  ("naming","/ˈneɪmɪŋ/","n","cách đặt tên","The <b>naming</b> here is confusing.","Cách đặt tên ở đây khó hiểu."),
  ("duplicate","/ˈdjuːplɪkət/","adj/n","trùng lặp","This code is <b>duplicate</b>.","Đoạn code này bị trùng."),
  ("suggestion","/səˈdʒestʃən/","n","đề xuất","Just a small <b>suggestion</b>.","Chỉ là một đề xuất nhỏ thôi."),
  ("minor","/ˈmaɪnər/","adj","nhỏ, không quan trọng lắm","This is a <b>minor</b> issue.","Đây là vấn đề nhỏ."),
 ],
 "phrases":[
  ("This looks good to me.","Cái này mình thấy ổn.","viết tắt LGTM"),
  ("Could you add a test for this case?","Bạn thêm test cho trường hợp này nhé?",""),
  ("I think this might break when the list is empty.","Mình nghĩ cái này có thể lỗi khi list rỗng.","'might' làm câu nhẹ đi"),
  ("Small thing: can we rename this variable?","Chuyện nhỏ: đổi tên biến này được không?",""),
  ("Thanks for the feedback, I'll fix it.","Cảm ơn góp ý, mình sẽ sửa.",""),
 ],
 "dialogues":[
  ("Can you take a look at my code?",[
    ("Sure, it looks good. Just one small suggestion.",True,"Khen trước, góp ý nhẹ sau."),
    ("Your code have many problem.",False,"'have' sai và nghe nặng nề."),
    ("Code bad, change all.",False,"Cộc lốc, không rõ sửa gì."),
  ]),
  ("Do you have any comments on the PR?",[
    ("Just a minor one: could you rename this variable?",True,"Góp ý cụ thể, lịch sự."),
    ("Yes, all is wrong.",False,"Chung chung, không giúp được."),
    ("Comment no, is fine maybe.",False,"Lộn xộn, khó hiểu."),
  ]),
 ],
 "listen":[
  ("This looks good to me",["looks","good"],"khen code ổn"),
  ("Could you add a test for this case",["add","test"],"nhờ thêm test"),
  ("The naming here is a bit confusing",["naming","confusing"],"cách đặt tên"),
  ("Thanks for the feedback I will fix it",["feedback","fix"],"nhận góp ý"),
 ],
},
{
 "title":"Test & lỗi",
 "vocab":[
  ("unit test","/ˈjuːnɪt test/","n","kiểm thử từng đơn vị code","Please add a <b>unit test</b>.","Thêm unit test nhé."),
  ("bug","/bʌɡ/","n","lỗi","I found a <b>bug</b> in the report.","Mình tìm thấy một bug ở phần báo cáo."),
  ("reproduce","/ˌriːprəˈdjuːs/","v","tái hiện lại lỗi","I can't <b>reproduce</b> the bug.","Mình không tái hiện được lỗi."),
  ("edge case","/edʒ keɪs/","n","trường hợp hiếm, dễ bị bỏ sót","This fails on an <b>edge case</b>.","Cái này lỗi ở một edge case."),
  ("coverage","/ˈkʌvərɪdʒ/","n","độ phủ của test","Test <b>coverage</b> is low here.","Độ phủ test ở đây thấp."),
  ("fail","/feɪl/","v","thất bại (test không đạt)","Two tests <b>failed</b>.","Hai test bị fail."),
  ("pass","/pɑːs/","v","đạt (test qua)","All tests <b>pass</b> now.","Giờ tất cả test đều pass."),
  ("regression","/rɪˈɡreʃn/","n","lỗi cũ tái phát","This is a <b>regression</b> bug.","Đây là lỗi tái phát."),
  ("stack trace","/stæk treɪs/","n","log chi tiết chỗ lỗi","Send me the <b>stack trace</b>.","Gửi mình stack trace nhé."),
  ("root cause","/ruːt kɔːz/","n","nguyên nhân gốc","We found the <b>root cause</b>.","Bọn mình tìm ra nguyên nhân gốc."),
 ],
 "phrases":[
  ("I found a bug in the login page.","Mình tìm thấy lỗi ở trang login.",""),
  ("Can you reproduce it on your machine?","Bạn tái hiện được trên máy bạn không?",""),
  ("Two tests are failing after my change.","Hai test bị fail sau khi mình sửa.",""),
  ("Let me check the logs and get back to you.","Để mình xem log rồi báo lại.",""),
  ("It only happens on an edge case.","Nó chỉ xảy ra ở một edge case.",""),
 ],
 "dialogues":[
  ("The build is failing. Any idea why?",[
    ("Let me check the logs and get back to you.",True,"Chuẩn — cách nói khi chưa biết ngay."),
    ("I don't know, maybe error.",False,"Không giúp được người hỏi."),
    ("Because build is fail.",False,"Lặp câu hỏi và 'is fail' sai."),
  ]),
  ("Can you reproduce the bug?",[
    ("Not yet. Could you tell me the exact steps?",True,"Hỏi thêm thông tin đúng cách."),
    ("No, bug no come to me.",False,"Nên là: I can't reproduce it."),
    ("Reproduce what, I no see.",False,"Cộc lốc, khó hiểu."),
  ]),
 ],
 "listen":[
  ("Two tests failed after my change",["tests","failed"],"test không đạt"),
  ("Can you reproduce it on your machine",["reproduce","machine"],"tái hiện lỗi"),
  ("We finally found the root cause",["root","cause"],"nguyên nhân gốc"),
  ("Please send me the stack trace",["send","trace"],"gửi log lỗi"),
 ],
},
{
 "title":"Deploy & môi trường",
 "vocab":[
  ("deploy","/dɪˈplɔɪ/","v","triển khai (đưa code lên chạy)","We <b>deploy</b> every Friday.","Bọn mình deploy mỗi thứ Sáu."),
  ("rollback","/ˈroʊlbæk/","n/v","quay lại bản trước khi lỗi","If it breaks, we <b>roll back</b>.","Nếu hỏng thì mình rollback."),
  ("staging","/ˈsteɪdʒɪŋ/","n","môi trường thử trước production","Test it on <b>staging</b> first.","Thử trên staging trước."),
  ("production","/prəˈdʌkʃn/","n","môi trường thật, người dùng đang chạy","Don't test on <b>production</b>.","Đừng test trên production."),
  ("environment","/ɪnˈvaɪrənmənt/","n","môi trường","Which <b>environment</b> is this on?","Cái này ở môi trường nào?"),
  ("downtime","/ˈdaʊntaɪm/","n","thời gian hệ thống ngừng","There will be a short <b>downtime</b>.","Sẽ có downtime ngắn."),
  ("hotfix","/ˈhɒtfɪks/","n","bản sửa gấp trên production","We pushed a <b>hotfix</b>.","Bọn mình đẩy một hotfix."),
  ("release","/rɪˈliːs/","n/v","phát hành bản mới","The next <b>release</b> is Monday.","Bản release tiếp theo là thứ Hai."),
  ("build","/bɪld/","n/v","bản dựng của code","The <b>build</b> is broken.","Bản build bị hỏng."),
  ("config","/kənˈfɪɡ/","n","cấu hình","Check the <b>config</b> file.","Kiểm tra file config."),
 ],
 "phrases":[
  ("We're deploying to production now.","Bọn mình đang deploy lên production.",""),
  ("Please expect a short downtime.","Mọi người lưu ý sẽ có downtime ngắn.",""),
  ("If anything breaks, we'll roll back.","Nếu có gì hỏng, bọn mình sẽ rollback.",""),
  ("The deploy is done, please test again.","Deploy xong rồi, mọi người test lại nhé.",""),
  ("Let's test it on staging first.","Thử trên staging trước đã.",""),
 ],
 "dialogues":[
  ("Did you finish the deployment?",[
    ("Not yet. I ran into a session conflict.",True,"'ran into' = gặp phải, rất tự nhiên."),
    ("No, session conflict is coming.",False,"'is coming' dịch thẳng từ tiếng Việt."),
    ("Not finish, have problem.",False,"Nên là: Not yet, I hit a problem."),
  ]),
  ("Can we deploy this now?",[
    ("Let's test it on staging first, then deploy.",True,"Đề xuất bước hợp lý."),
    ("Yes deploy now production fast.",False,"Cộc lốc, thiếu mạo từ."),
    ("Deploy maybe, I not sure so.",False,"Do dự, khó hiểu."),
  ]),
 ],
 "listen":[
  ("We are deploying to production now",["deploying","production"],"đang triển khai"),
  ("Please expect a short downtime",["expect","downtime"],"báo ngừng dịch vụ"),
  ("If anything breaks we will roll back",["breaks","roll"],"quay lại bản cũ"),
  ("Let us test it on staging first",["test","staging"],"môi trường thử"),
 ],
},
{
 "title":"Cơ sở dữ liệu",
 "vocab":[
  ("schema","/ˈskiːmə/","n","cấu trúc dữ liệu / bảng","We changed the database <b>schema</b>.","Bọn mình đổi schema database."),
  ("migration","/maɪˈɡreɪʃn/","n","thay đổi cấu trúc database","Run the <b>migration</b> before deploy.","Chạy migration trước khi deploy."),
  ("query","/ˈkwɪəri/","n/v","truy vấn dữ liệu","This <b>query</b> is slow.","Câu query này chậm."),
  ("table","/ˈteɪbl/","n","bảng dữ liệu","Add a column to this <b>table</b>.","Thêm một cột vào bảng này."),
  ("record","/ˈrekɔːrd/","n","bản ghi (một dòng)","There are 500 <b>records</b>.","Có 500 bản ghi."),
  ("backup","/ˈbækʌp/","n/v","sao lưu","Do we have a <b>backup</b>?","Mình có backup không?"),
  ("index","/ˈɪndeks/","n","chỉ mục (giúp query nhanh)","Add an <b>index</b> on this column.","Thêm index cho cột này."),
  ("constraint","/kənˈstreɪnt/","n","ràng buộc dữ liệu","There's a unique <b>constraint</b> here.","Ở đây có ràng buộc unique."),
  ("dataset","/ˈdeɪtəset/","n","tập dữ liệu","The <b>dataset</b> is too big.","Tập dữ liệu quá lớn."),
  ("duplicate","/ˈdjuːplɪkət/","n","dữ liệu trùng","We have some <b>duplicates</b>.","Có một số dữ liệu trùng."),
 ],
 "phrases":[
  ("We changed the database schema.","Bọn mình đổi schema database.",""),
  ("Please run the migration first.","Chạy migration trước nhé.",""),
  ("This query is a bit slow.","Câu query này hơi chậm.",""),
  ("Do we have a backup of this table?","Mình có backup bảng này không?",""),
  ("There are some duplicate records.","Có một số bản ghi bị trùng.",""),
 ],
 "dialogues":[
  ("Why is the page so slow?",[
    ("I think this query needs an index.",True,"Chẩn đoán rõ, đúng chuyên môn."),
    ("Page slow because data many.",False,"Thiếu mạo từ và động từ."),
    ("I don't know, database maybe.",False,"Mơ hồ, không hữu ích."),
  ]),
  ("Did you run the migration?",[
    ("Not yet, I'll run it before the deploy.",True,"Rõ ràng, có kế hoạch."),
    ("Migration I run no yet.",False,"Sai trật tự từ."),
    ("Yes maybe, I not sure.",False,"Không chắc chắn, khó tin."),
  ]),
 ],
 "listen":[
  ("We changed the database schema today",["changed","schema"],"đổi cấu trúc"),
  ("Please run the migration before deploy",["run","migration"],"chạy migration"),
  ("This query needs an index",["query","index"],"tối ưu truy vấn"),
  ("We have some duplicate records",["duplicate","records"],"dữ liệu trùng"),
 ],
},
{
 "title":"API & tích hợp",
 "vocab":[
  ("endpoint","/ˈendpɔɪnt/","n","địa chỉ API để gọi","The login <b>endpoint</b> returns a token.","Endpoint login trả về token."),
  ("request","/rɪˈkwest/","n/v","yêu cầu gửi lên server","The <b>request</b> failed.","Request bị lỗi."),
  ("response","/rɪˈspɒns/","n","phản hồi từ server","Check the <b>response</b> body.","Kiểm tra nội dung response."),
  ("payload","/ˈpeɪloʊd/","n","dữ liệu gửi trong request","The <b>payload</b> is missing a field.","Payload thiếu một trường."),
  ("timeout","/ˈtaɪmaʊt/","n","quá thời gian chờ, bị ngắt","It failed with a <b>timeout</b>.","Nó lỗi do timeout."),
  ("latency","/ˈleɪtənsi/","n","độ trễ","The API has high <b>latency</b>.","API bị trễ cao."),
  ("token","/ˈtoʊkən/","n","mã xác thực","The <b>token</b> is expired.","Token đã hết hạn."),
  ("status code","/ˈsteɪtəs koʊd/","n","mã trạng thái (200, 404...)","It returns a 500 <b>status code</b>.","Nó trả về mã 500."),
  ("rate limit","/reɪt ˈlɪmɪt/","n","giới hạn số lần gọi","We hit the <b>rate limit</b>.","Bọn mình chạm rate limit."),
  ("integration","/ˌɪntɪˈɡreɪʃn/","n","tích hợp giữa các hệ thống","The <b>integration</b> is not working.","Phần tích hợp chưa chạy."),
 ],
 "phrases":[
  ("The request failed with a timeout.","Request lỗi do timeout.",""),
  ("Check the response body for the error.","Xem nội dung response để tìm lỗi.",""),
  ("The token is expired, please log in again.","Token hết hạn, đăng nhập lại nhé.",""),
  ("The payload is missing one field.","Payload thiếu một trường.",""),
  ("The API is slow today, high latency.","Hôm nay API chậm, độ trễ cao.",""),
 ],
 "dialogues":[
  ("The API call is not working. Why?",[
    ("It returns a 500. Let me check the logs.",True,"Cụ thể và có bước tiếp theo."),
    ("API no work, I don't know why.",False,"Không giúp gì."),
    ("Because API is bad today.",False,"Mơ hồ, không chuyên nghiệp."),
  ]),
  ("Why did the request fail?",[
    ("It failed with a timeout. The server was slow.",True,"Nêu nguyên nhân rõ ràng."),
    ("Request fail because internet.",False,"Thiếu mạo từ, đoán mò."),
    ("Fail, maybe token or something.",False,"Không chắc chắn."),
  ]),
 ],
 "listen":[
  ("The request failed with a timeout",["request","timeout"],"lỗi quá giờ chờ"),
  ("The token is expired please log in again",["token","expired"],"mã hết hạn"),
  ("The payload is missing one field",["payload","missing"],"thiếu dữ liệu"),
  ("It returns a 500 status code",["status","code"],"mã trạng thái"),
 ],
},
{
 "title":"Họp & trao đổi",
 "vocab":[
  ("agenda","/əˈdʒendə/","n","nội dung cuộc họp","What's on the <b>agenda</b> today?","Hôm nay họp về gì?"),
  ("action item","/ˈækʃn ˈaɪtəm/","n","việc cần làm sau họp","Let's note the <b>action items</b>.","Ghi lại các việc cần làm nhé."),
  ("follow up","/ˈfɒloʊ ʌp/","v/n","theo dõi tiếp sau đó","I'll <b>follow up</b> with the team.","Mình sẽ theo dõi tiếp với team."),
  ("clarify","/ˈklærɪfaɪ/","v","làm rõ","Could you <b>clarify</b> that point?","Bạn làm rõ chỗ đó được không?"),
  ("align","/əˈlaɪn/","v","thống nhất quan điểm","Let's <b>align</b> on the plan.","Mình thống nhất kế hoạch nhé."),
  ("recap","/ˈriːkæp/","n/v","tóm tắt lại","Quick <b>recap</b> of the meeting.","Tóm tắt nhanh cuộc họp."),
  ("sync","/sɪŋk/","n/v","họp ngắn để đồng bộ","Let's have a quick <b>sync</b>.","Mình sync nhanh một chút nhé."),
  ("stakeholder","/ˈsteɪkhoʊldər/","n","bên liên quan","We need the <b>stakeholders</b> to agree.","Cần các bên liên quan đồng ý."),
  ("minutes","/ˈmɪnɪts/","n","biên bản họp","I'll send the <b>minutes</b> later.","Mình sẽ gửi biên bản sau."),
  ("wrap up","/ræp ʌp/","v","kết thúc","Let's <b>wrap up</b> here.","Mình kết thúc ở đây nhé."),
 ],
 "phrases":[
  ("Sorry, could you clarify what you mean?","Xin lỗi, bạn nói rõ hơn được không?",""),
  ("Just to confirm, do you want A or B?","Xác nhận lại, bạn muốn A hay B?","rất hay dùng"),
  ("Let's align on the plan before we start.","Thống nhất kế hoạch trước khi bắt đầu nhé.",""),
  ("I'll follow up with you by email.","Mình sẽ theo dõi tiếp qua email.",""),
  ("Quick recap: we agreed on three things.","Tóm tắt nhanh: mình đã thống nhất ba điểm.",""),
 ],
 "dialogues":[
  ("Do you understand the requirement?",[
    ("Not fully. Could you clarify the second part?",True,"Hỏi lại đúng chỗ, tự tin."),
    ("Yes yes ok ok.",False,"Gật đại dù chưa hiểu — sẽ làm sai."),
    ("Requirement I no understand all.",False,"Sai cấu trúc, khó hiểu."),
  ]),
  ("Can you summarize the meeting?",[
    ("Sure. Quick recap: we agreed on the deadline and the scope.",True,"Tóm tắt rõ ràng."),
    ("Meeting is about many thing.",False,"Chung chung, không có nội dung."),
    ("Summarize what, I forget.",False,"Không chuẩn bị, khó tin."),
  ]),
 ],
 "listen":[
  ("Could you clarify the second part",["clarify","second"],"hỏi lại cho rõ"),
  ("Let us align on the plan first",["align","plan"],"thống nhất"),
  ("I will follow up with you by email",["follow","email"],"theo dõi tiếp"),
  ("Quick recap of the meeting",["recap","meeting"],"tóm tắt họp"),
 ],
},
{
 "title":"Sự cố & vướng mắc",
 "vocab":[
  ("issue","/ˈɪʃuː/","n","vấn đề","We have an <b>issue</b> on production.","Có vấn đề trên production."),
  ("workaround","/ˈwɜːrkəraʊnd/","n","cách khắc phục tạm","For now, use this <b>workaround</b>.","Tạm thời dùng cách này."),
  ("escalate","/ˈeskəleɪt/","v","báo lên cấp trên","We should <b>escalate</b> this.","Mình nên báo lên cấp trên."),
  ("investigate","/ɪnˈvestɪɡeɪt/","v","điều tra nguyên nhân","I'll <b>investigate</b> the issue.","Mình sẽ điều tra vấn đề này."),
  ("impact","/ˈɪmpækt/","n","mức ảnh hưởng","What's the <b>impact</b> on users?","Ảnh hưởng đến người dùng thế nào?"),
  ("urgent","/ˈɜːrdʒənt/","adj","gấp","This is <b>urgent</b>.","Cái này gấp."),
  ("outage","/ˈaʊtɪdʒ/","n","sự cố ngừng dịch vụ","There was a short <b>outage</b>.","Có một sự cố ngừng ngắn."),
  ("severity","/sɪˈverəti/","n","mức nghiêm trọng","What's the <b>severity</b> of this bug?","Lỗi này nghiêm trọng cỡ nào?"),
  ("mitigate","/ˈmɪtɪɡeɪt/","v","giảm nhẹ ảnh hưởng","We need to <b>mitigate</b> it fast.","Cần giảm nhẹ nhanh."),
  ("resolve","/rɪˈzɒlv/","v","giải quyết xong","The issue is <b>resolved</b> now.","Vấn đề đã được giải quyết."),
 ],
 "phrases":[
  ("We have an issue on production.","Có vấn đề trên production.",""),
  ("I'll investigate and update you soon.","Mình sẽ điều tra và cập nhật sớm.",""),
  ("For now, there's a workaround.","Trước mắt có một cách khắc phục tạm.",""),
  ("This is urgent, it affects all users.","Cái này gấp, ảnh hưởng tất cả người dùng.",""),
  ("The issue is resolved now.","Vấn đề đã được giải quyết.",""),
 ],
 "dialogues":[
  ("Production is down! What do we do?",[
    ("Let's roll back first, then investigate.",True,"Bình tĩnh, ưu tiên đúng."),
    ("I don't know, very panic now.",False,"Không đưa ra hành động."),
    ("Down? Maybe wait and see.",False,"Chờ đợi khi đang sự cố là sai."),
  ]),
  ("How bad is this bug?",[
    ("It's high severity, it affects all users.",True,"Đánh giá rõ mức độ."),
    ("Bug is very very bad much.",False,"Lặp từ, không cụ thể."),
    ("Not sure, maybe small maybe big.",False,"Không đánh giá được."),
  ]),
 ],
 "listen":[
  ("We have an issue on production",["issue","production"],"sự cố"),
  ("I will investigate and update you soon",["investigate","update"],"điều tra"),
  ("This is urgent it affects all users",["urgent","affects"],"mức độ gấp"),
  ("The issue is resolved now",["resolved"],"đã xử lý xong"),
 ],
},
{
 "title":"Kế hoạch & ước lượng",
 "vocab":[
  ("scope","/skoʊp/","n","phạm vi công việc","Let's define the <b>scope</b> first.","Xác định phạm vi trước đã."),
  ("milestone","/ˈmaɪlstoʊn/","n","cột mốc quan trọng","The next <b>milestone</b> is next week.","Cột mốc tiếp theo là tuần sau."),
  ("sprint","/sprɪnt/","n","chu kỳ làm việc (1-2 tuần)","This is in the next <b>sprint</b>.","Cái này để sprint sau."),
  ("requirement","/rɪˈkwaɪərmənt/","n","yêu cầu của tính năng","The <b>requirement</b> is not clear.","Yêu cầu chưa rõ."),
  ("dependency","/dɪˈpendənsi/","n","thứ mà việc này phụ thuộc","This task has a <b>dependency</b>.","Task này có một dependency."),
  ("deliverable","/dɪˈlɪvərəbl/","n","sản phẩm bàn giao","What's the final <b>deliverable</b>?","Sản phẩm bàn giao cuối là gì?"),
  ("timeline","/ˈtaɪmlaɪn/","n","mốc thời gian","Let's agree on a <b>timeline</b>.","Thống nhất mốc thời gian nhé."),
  ("trade-off","/ˈtreɪdɒf/","n","sự đánh đổi","There's a <b>trade-off</b> here.","Ở đây có sự đánh đổi."),
  ("feasible","/ˈfiːzəbl/","adj","khả thi","Is this <b>feasible</b> by Friday?","Cái này xong trước thứ Sáu có khả thi không?"),
  ("estimate","/ˈestɪmət/","n/v","ước lượng thời gian","My <b>estimate</b> is three days.","Mình ước lượng ba ngày."),
 ],
 "phrases":[
  ("Let's define the scope first.","Xác định phạm vi trước đã.",""),
  ("My estimate for this is three days.","Mình ước lượng cái này ba ngày.",""),
  ("This task depends on the API being ready.","Task này phụ thuộc vào API đã sẵn sàng.",""),
  ("Is this feasible by Friday?","Cái này xong trước thứ Sáu có khả thi không?",""),
  ("Let's agree on a timeline.","Thống nhất mốc thời gian nhé.",""),
 ],
 "dialogues":[
  ("How long will this take?",[
    ("My estimate is about three days.",True,"Ước lượng rõ ràng."),
    ("Maybe fast, maybe slow, not sure.",False,"Không đưa ra con số."),
    ("Take long time I think so.",False,"Mơ hồ, thiếu chủ ngữ."),
  ]),
  ("Can we finish this by Friday?",[
    ("It's tight, but feasible if there are no blockers.",True,"Trung thực, có điều kiện."),
    ("Yes yes no problem sure.",False,"Hứa đại dễ vỡ kế hoạch."),
    ("Friday? I don't think about it.",False,"Né tránh câu hỏi."),
  ]),
 ],
 "listen":[
  ("My estimate for this is three days",["estimate","days"],"ước lượng thời gian"),
  ("Let us define the scope first",["define","scope"],"phạm vi"),
  ("This task depends on the API",["depends","API"],"phụ thuộc"),
  ("Is this feasible by Friday",["feasible","Friday"],"khả thi"),
 ],
},
]

try:
    from phases_extra import EXTRA
    PHASES = PHASES + EXTRA
except Exception as e:
    print("EXTRA load failed:", e)

# Build flat pools + DAYS (index references)
V=[]; PH=[]; DI=[]; LI=[]
phaseVocab=[]; phasePhrase=[]; phaseDia=[]; phaseListen=[]
for p in PHASES:
    vi=[]
    for t,ipa,pos,vn,ex,exvi in p["vocab"]:
        vi.append(len(V)); V.append({"t":t,"ipa":ipa,"pos":pos,"vi":vn,"ex":ex,"exVi":exvi})
    phaseVocab.append(vi)
    pi=[]
    for en,vn,note in p["phrases"]:
        pi.append(len(PH)); PH.append({"en":en,"vi":vn,"note":note})
    phasePhrase.append(pi)
    di=[]
    for them,opts in p["dialogues"]:
        di.append(len(DI)); DI.append({"them":them,"opts":[{"t":t,"good":g,"fb":f} for t,g,f in opts]})
    phaseDia.append(di)
    li=[]
    for sent,blanks,hint in p["listen"]:
        words=sent.split()
        bidx=[]
        used=set()
        for bw in blanks:
            for i,w in enumerate(words):
                if i in used: continue
                if w.lower().strip(".,").replace("'","")==bw.lower():
                    bidx.append(i); used.add(i); break
        li.append(len(LI)); LI.append({"s":words,"blank":bidx,"hint":hint})
    phaseListen.append(li)

DAYS=[]
for d in range(len(PHASES)*10):
    p=d//10; dp=d%10
    vpool=phaseVocab[p]
    vsel=[vpool[(dp*3)%10], vpool[(dp*3+1)%10], vpool[(dp*3+2)%10]]
    DAYS.append({
        "n":d+1,
        "phase":p,
        "title":PHASES[p]["title"],
        "v":vsel,
        "ph":phasePhrase[p][dp%len(phasePhrase[p])],
        "di":phaseDia[p][dp%len(phaseDia[p])],
        "li":phaseListen[p][dp%len(phaseListen[p])],
    })

PHASE_TITLES=[p["title"] for p in PHASES]
out="window.DATA="+json.dumps({
    "vocab":V,"phrases":PH,"dialogues":DI,"listen":LI,"days":DAYS,
    "phaseTitles":PHASE_TITLES
},ensure_ascii=False,separators=(",",":"))+";\n"
open("data.gen.js","w",encoding="utf-8").write(out)
print("vocab",len(V),"phrases",len(PH),"dialogues",len(DI),"listen",len(LI),"days",len(DAYS))
print("bytes",len(out))
# T2: game dùng bản sao cùng dữ liệu — luôn đồng bộ khi sinh lại
import os, shutil
_here=os.path.dirname(os.path.abspath(__file__))
if os.path.isdir(os.path.join(_here,"game")):
    shutil.copyfile(os.path.join(_here,"data.gen.js"),os.path.join(_here,"game","data.gen.js"))
    print("copied -> game/data.gen.js")
