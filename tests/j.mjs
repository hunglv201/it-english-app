// v4.0 đợt B: từ mục tiêu trong chat, chạm từ tra nghĩa, gõ tiếng Việt khi bí, phỏng vấn/họp/thuyết trình + tiêu chí chấm,
// phát âm 3 mức (gần đúng), phân tích bài nói, lá chắn cuối tuần, sửa chuỗi, chúc mừng nối chuỗi, ngày hoàn hảo
import {launch,page,BASE,baseStore,shot,report} from './lib.mjs';
import assert from 'assert/strict';
const d=new Date(),dow=(d.getDay()+6)%7,mon=new Date(d);mon.setDate(d.getDate()-dow);const wk=mon.toISOString().slice(0,10);
const today=new Date().toISOString().slice(0,10),yest=new Date(Date.now()-864e5).toISOString().slice(0,10);
const ai=`var s=typeof input==='string'?input:JSON.stringify(input);
if(/want to say \\(in Vietnamese\\)/.test(s))return 'Could you give me one more day, please?';
if(/Translate this workplace English sentence/.test(s))return 'Chúng ta cùng xem lại hạn chót nhé.';
return "Let's check the deadline and the blorptastic report together. What do you think?\\nFIX: OK";`;
const aiJson=`
if(/explain the English word "blorptastic"/.test(prompt))return {t:'blorptastic',ipa:'/blɔːp/',pos:'adj',vi:'tuyệt vời (từ thử)',ex:'It is blorptastic.',exVi:'Nó tuyệt.'};
if(/This is a transcript/.test(prompt))return {score:6,summary:'Nói rõ ý nhưng nhiều từ đệm.',fixes:[{wrong:'I very like',right:'I really like',note:'đặt really trước động từ'}],better:'I really like my job. I help customers every day.',tips:['Dừng ngắn thay vì nói um.']};
if(/Evaluate ONLY Me/.test(prompt))return {score:7,tips:['Nêu kết quả cụ thể hơn.'],phrases:['As a result, we saved two days.'],criteria:[{name:'Trả lời đúng câu hỏi',score:4,note:'Ổn'},{name:'Có ví dụ cụ thể',score:2,note:'Thiếu kết quả'}]};
return [];`;
const due=Date.now()-1000;
const b=await launch();
const st=(extra={})=>baseStore(Object.assign({stats:{placed:true,sundayShown:wk},cfg:{level:'A2',autoSpeak:false,track:'office',trackChosen:true},
  srs:{deadline:{ease:2.3,int:1,reps:1,due},agenda:{ease:1.9,int:3,reps:2,due:Date.now()+9e8}},
  myVocab:[{t:'deadline',ipa:'/ˈdedlaɪn/',pos:'n',vi:'hạn chót',ex:'The <b>deadline</b> is Friday.',exVi:'Hạn là thứ Sáu.',custom:true},{t:'agenda',ipa:'/əˈdʒendə/',pos:'n',vi:'chương trình họp',ex:'<b>agenda</b>',exVi:'',custom:true}]},extra));

// 1) Chat: từ mục tiêu vào prompt + thanh 🎯; dùng đúng → ✓ + tính 1 lần ôn
let p=await page(b,{ai,aiJson,store:st()});
await p.goto(BASE+'index.html');await p.waitForTimeout(600);
await p.evaluate(()=>{go('talk');});await p.waitForTimeout(150);
await p.evaluate(()=>{aiScenario=scenarioList()[0].k;aiTurns=[];aiStart();});await p.waitForTimeout(500);
const t1=await p.evaluate(()=>({targets:aiTargets.map(x=>x.t),bar:!!document.querySelector('#main .card .chip')&&/Thử dùng/.test(document.getElementById('main').textContent),prompt:JSON.stringify(window.__calls[0].input)}));
console.log('targets',JSON.stringify(t1.targets));
assert.ok(t1.targets.includes('deadline')&&t1.targets.includes('agenda'),'targets due + weak');
assert.ok(t1.bar,'targets bar');assert.ok(/deadline/.test(t1.prompt)&&/never quiz/.test(t1.prompt),'targets in prompt');
await shot(p,'j_targets');
const reps0=await p.evaluate(()=>store.srs.deadline.reps);
await p.evaluate(()=>{document.getElementById('aiInput').value='We can move the deadlines to Monday.';aiSend();});await p.waitForTimeout(500);
const t2=await p.evaluate(()=>({used:aiTargets.filter(x=>x.used).map(x=>x.t),reps:store.srs.deadline.reps,chip:[...document.querySelectorAll('#main .chip.on')].map(c=>c.textContent)}));
console.log('used',JSON.stringify(t2));assert.deepEqual(t2.used,['deadline']);assert.equal(t2.reps,reps0+1);assert.ok(t2.chip.some(c=>/✓ deadline/.test(c)));
// agenda chưa tới hạn → dùng được nhưng không tính ôn thêm
await p.evaluate(()=>{document.getElementById('aiInput').value='Let me share the agenda.';aiSend();});await p.waitForTimeout(500);
assert.equal(await p.evaluate(()=>store.srs.agenda.reps),2);

// 2) Gõ tiếng Việt khi bí → gợi ý tiếng Anh, không thành lượt nói
const n0=await p.evaluate(()=>aiTurns.length);
await p.evaluate(()=>{document.getElementById('aiInput').value='cho tôi thêm một ngày được không';aiSend();});await p.waitForTimeout(500);
const t3=await p.evaluate(()=>({n:aiTurns.length,hint:aiHint,lab:document.getElementById('main').textContent.includes('Cách nói bằng tiếng Anh')}));
console.log('vi→en',JSON.stringify(t3));assert.equal(t3.n,n0);assert.ok(/one more day/.test(t3.hint)&&t3.lab);
await shot(p,'j_vi_hint');

// 3) Chạm từ: có trong gói → nghĩa ngay; không có → hỏi AI; dịch cả câu
await p.evaluate(()=>{var w=[...document.querySelectorAll('#main .bubble.them .tw')].find(x=>/deadline/.test(x.textContent));w.click();});await p.waitForTimeout(200);
let mt=await p.evaluate(()=>document.querySelector('.modal').textContent);
assert.ok(/hạn chót/.test(mt)&&/từ trong gói/.test(mt),'dict hit');await shot(p,'j_tap_dict');
await p.evaluate(()=>{[...document.querySelectorAll('.modal .btn')].find(x=>/Dịch cả câu/.test(x.textContent)).click();});await p.waitForTimeout(300);
assert.ok(/Chúng ta cùng xem lại/.test(await p.evaluate(()=>document.querySelector('.modal').textContent)),'translate sentence');
await p.evaluate(()=>closeModal());
await p.evaluate(()=>{var w=[...document.querySelectorAll('#main .bubble.them .tw')].find(x=>/blorptastic/.test(x.textContent));w.click();});await p.waitForTimeout(150);
await p.evaluate(()=>{[...document.querySelectorAll('.modal .btn')].find(x=>/Hỏi AI nghĩa/.test(x.textContent)).click();});await p.waitForTimeout(300);
mt=await p.evaluate(()=>document.querySelector('.modal').textContent);assert.ok(/tuyệt vời \(từ thử\)/.test(mt),'ai lookup');
await p.evaluate(()=>{[...document.querySelectorAll('.modal .btn')].find(x=>/Lưu vào/.test(x.textContent)).click();});
assert.ok(await p.evaluate(()=>store.myVocab.some(v=>v.t==='blorptastic'&&v.custom)),'saved to mine');
await shot(p,'j_tap_ai');await p.evaluate(()=>closeModal());
report(p,'J chat');

// 4) Phỏng vấn: có trong danh sách tình huống, chấm có tiêu chí + số từ mục tiêu
await p.evaluate(()=>{aiScenario='x_interview';aiTurns=[];aiStart();});await p.waitForTimeout(400);
const t4=await p.evaluate(()=>({inList:scenarioList().some(x=>x.k==='x_interview'&&/Phỏng vấn/.test(x.l)),prompt:JSON.stringify(window.__calls[window.__calls.length-1].input)}));
assert.ok(t4.inList&&/interviewer/.test(t4.prompt));
for(const m of ['I am a sales staff.','I solved a customer problem last year.','We saved two days.'])await p.evaluate(m=>{document.getElementById('aiInput').value=m;aiSend();},m),await p.waitForTimeout(350);
await p.evaluate(()=>aiReview());await p.waitForTimeout(400);
const rv=await p.evaluate(()=>({t:document.querySelector('.modal').textContent,prompt:window.__calls.filter(c=>c.json).pop().prompt}));
assert.ok(/Có ví dụ cụ thể/.test(rv.t)&&/từ mục tiêu/.test(rv.t)&&/criteria/.test(rv.prompt));await shot(p,'j_interview_review');
await p.evaluate(()=>closeModal());

// 5) Phát âm 3 mức
const t5=await p.evaluate(()=>{var toks=lTokens([{w:'We',hit:true},{w:'developed',hit:false},{w:'module',hit:false}],'we develop the');
  var m=wordMatch('We developed the module','we develop the');
  return {cls:[...toks.querySelectorAll('.tok')].map(x=>x.className),say:toks.querySelector('.tok.near').getAttribute('data-heard'),legend:/chạm từ/.test(toks.textContent),wm:m.words.map(w=>w.hit?'h':w.near?'n':'m').join('')};});
console.log('pron',JSON.stringify(t5));assert.deepEqual(t5.cls,['tok hit','tok near','tok miss']);assert.equal(t5.say,'develop');assert.ok(t5.legend);assert.equal(t5.wm,'hnhm');
await p.evaluate(()=>{go('listen');});await p.waitForTimeout(150);
await p.evaluate(()=>{lMode='shadow';lHeard=lSentence().split(' ').map((w,i)=>i===1?w.slice(0,-1)+'x':w).join(' ');lChecked=true;vListen();});await p.waitForTimeout(150);
console.log('shadow toks',await p.evaluate(()=>[...document.querySelectorAll('#main .tok')].map(x=>x.className.split(' ')[1]).join(',')));
await shot(p,'j_shadow_colors');

// 6) Phân tích bài nói (dán chữ)
await p.evaluate(()=>auditStart());await p.waitForTimeout(150);
await p.evaluate(()=>{document.getElementById('auIn').value='um so I very like my job and like I help customers um every day you know';[...document.querySelectorAll('#main .btn')].find(x=>/Phân tích bản chữ/.test(x.textContent)).click();});
await p.waitForTimeout(500);
const t6=await p.evaluate(()=>({t:document.getElementById('main').textContent,a:store.audits[0]}));
console.log('audit',JSON.stringify(t6.a));assert.ok(/really like/.test(t6.t)&&/Nói lại tự nhiên hơn/.test(t6.t)&&/“um” ×2/.test(t6.t));assert.equal(t6.a.fillerN,6);assert.equal(t6.a.score,6);
await shot(p,'j_audit');
await p.evaluate(()=>{[...document.querySelectorAll('#main .btn')].find(x=>/Lưu các câu sửa/.test(x.textContent)).click();});
assert.ok(await p.evaluate(()=>!!psrs()['I really like']));
report(p,'J practice');await p.close();

// 7) Lá chắn cuối tuần (hàm thuần)
p=await page(b,{store:st({hist:{'2026-09-14':1,'2026-09-15':2,'2026-09-16':1,'2026-09-17':1,'2026-09-18':3}})});
await p.goto(BASE+'index.html');await p.waitForTimeout(500);
const t7=await p.evaluate(()=>({fri_mon:weekendShield('2026-09-18','2026-09-21'),fri_tue:weekendShield('2026-09-18','2026-09-22'),thu_mon:weekendShield('2026-09-17','2026-09-21')}));
console.log('shield',JSON.stringify(t7));assert.deepEqual(t7,{fri_mon:true,fri_tue:false,thu_mon:false});
await p.close();

// 8) Chúc mừng nối chuỗi + ngày hoàn hảo
p=await page(b,{store:st({stats:{placed:true,sundayShown:wk,streak:6,lastActive:yest}})});
await p.goto(BASE+'index.html');await p.waitForTimeout(500);
await p.evaluate(()=>markToday('vocab'));await p.waitForTimeout(500);
const t8=await p.evaluate(()=>({c:document.querySelector('.celebr')&&document.querySelector('.celebr').textContent,streak:store.stats.streak}));
console.log('celebrate',JSON.stringify(t8));assert.ok(/Chuỗi 7 ngày/.test(t8.c)&&/1 tuần/.test(t8.c));await shot(p,'j_celebrate');
await p.waitForTimeout(2300);
await p.evaluate(()=>{['listen','talk','phrases'].forEach(k=>markToday(k));});
assert.equal(await p.evaluate(()=>store.stats.perfect),1);
report(p,'J streak');await p.close();

// 9) Sửa chuỗi: bằng xu game, và tự nối khi làm đủ 4 việc
const brokeSt=()=>st({stats:{placed:true,sundayShown:wk,streak:1,lastActive:today,broke:{streak:12,at:today}}});
p=await page(b,{store:brokeSt(),game:{coins:200,lv:1,xp:0}});
await p.goto(BASE+'index.html');await p.waitForTimeout(600);
assert.ok(await p.evaluate(()=>/Chuỗi 12 ngày vừa đứt/.test(document.getElementById('main').textContent)),'repair card');await shot(p,'j_repair');
await p.evaluate(()=>[...document.querySelectorAll('#main .btn')].find(x=>/xu để nối lại/.test(x.textContent)).click());await p.waitForTimeout(300);
const t9=await p.evaluate(()=>({s:store.stats.streak,coins:JSON.parse(localStorage.getItem('it-english-game-v1')).coins,broke:!!store.stats.broke,again:!!repairInfo()}));
console.log('repair coins',JSON.stringify(t9));assert.deepEqual(t9,{s:13,coins:50,broke:false,again:false});
report(p,'J repair coins');await p.close();
p=await page(b,{store:brokeSt()});
await p.goto(BASE+'index.html');await p.waitForTimeout(500);
await p.evaluate(()=>{['vocab','listen','talk','phrases'].forEach(k=>markToday(k));});await p.waitForTimeout(300);
assert.equal(await p.evaluate(()=>store.stats.streak),13);
report(p,'J repair tasks');
await b.close();
