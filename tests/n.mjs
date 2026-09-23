// v4.3: Anh ⇄ Nhật (BrSE) · Sổ lỗi · Chuẩn bị nhanh cho sự kiện · Mẫu email & tin nhắn
import assert from 'assert';
import {launch,page,BASE,baseStore,shot,report} from './lib.mjs';
const d=new Date(),dow=(d.getDay()+6)%7,mon=new Date(d);mon.setDate(d.getDate()-dow);const wk=mon.toISOString().slice(0,10);
const today=new Date().toISOString().slice(0,10),yest=new Date(Date.now()-864e5).toISOString().slice(0,10),tmr=new Date(Date.now()+864e5).toISOString().slice(0,10);
const b=await launch();
const SR=()=>{window.__srSay=null;window.__srLang=[];window.SpeechRecognition=function(){var self=this;this.start=function(){window.__srLang.push(self.lang);setTimeout(function(){var t=window.__srSay?window.__srSay(self.lang):'';if(t&&self.onresult)self.onresult({resultIndex:0,results:[Object.assign([{transcript:t}],{isFinal:true})]});setTimeout(function(){self.onend&&self.onend();},20);},40);};this.stop=function(){};this.abort=function(){};};};
const until=async(p,fn,ms=5000)=>{for(let i=0;i<ms/100;i++){try{if(await p.evaluate(fn))return true;}catch(e){}await p.waitForTimeout(100);}return false;};
const txt=p=>p.evaluate(()=>document.getElementById('main').textContent);
// 1) Anh ⇄ Nhật
{const p=await page(b,{claude:false,store:baseStore({stats:{placed:true,sundayShown:wk},cfg:{level:'A2',autoSpeak:false,track:'it',trackChosen:true}})});
await p.addInitScript(SR);await p.goto(BASE+'index.html');await p.waitForTimeout(500);
await p.evaluate(()=>go('practice'));assert.ok(/Anh ⇄ Nhật \(BrSE\)/.test(await txt(p)),'tile');
await p.evaluate(()=>brseStart());assert.ok(await until(p,()=>window.JA_BRSE&&/Làm việc với khách Nhật/.test(document.getElementById('main').textContent)));
const n=await p.evaluate(()=>({g:JA_BRSE.length,cards:document.querySelectorAll('#main .card').length,ruby:document.querySelectorAll('#main ruby').length>5}));
console.log('brse list',JSON.stringify(n));assert.equal(n.g,10);assert.ok(n.cards>=8&&n.ruby);await shot(p,'n_brse_list');
// Anh → nói Nhật: nói đúng câu tiếng Nhật
await p.evaluate(()=>{window.__srSay=function(l){var it=bs.q.items[bs.q.i];return l==='ja-JP'?it.kana:'';};brseQuiz('en2ja');});await p.waitForTimeout(300);
await p.evaluate(()=>brseMic());assert.ok(await until(p,()=>bs.q.res&&bs.q.res.pct!=null));
let r=await p.evaluate(()=>({pct:bs.q.res.pct,lang:window.__srLang.slice(-1)[0]}));console.log('en2ja',JSON.stringify(r));assert.ok(r.pct>=90&&r.lang==='ja-JP');await shot(p,'n_brse_en2ja');
// Nhật → nói Anh: nói sai → vào sổ lỗi
await p.evaluate(()=>{window.__srSay=function(l){return l==='en-US'?'um no':'';};brseQuiz('ja2en');});await p.waitForTimeout(300);
await p.evaluate(()=>brseMic());assert.ok(await until(p,()=>bs.q.res&&bs.q.res.pct!=null));
r=await p.evaluate(()=>({pct:bs.q.res.pct,mk:(store.mistakes||[]).filter(m=>m.src==='ja').length}));console.log('ja2en',JSON.stringify(r));assert.ok(r.pct<60&&r.mk===1);
report(p,'N brse');await p.close();}
// 2) Sổ lỗi: gom từ chọn cách đáp + AI sửa + dịch ngược, phân nhóm, ôn và "đã nắm"
{const p=await page(b,{claude:false,store:baseStore({stats:{placed:true,sundayShown:wk},cfg:{level:'A2',autoSpeak:false,track:'office',trackChosen:true}})});
await p.addInitScript(SR);await p.goto(BASE+'index.html');await p.waitForTimeout(500);
const cats=await p.evaluate(()=>[mkCat('I send it yesterday','I sent it yesterday'),mkCat('I have meeting at 3','I have a meeting at 3'),mkCat('Almost done, finish today','It is almost done. I will finish it today.'),mkCat('I work in Monday','I work on Monday'),mkCat('two report','two reports'),mkCat('He need help','He needs help'),mkCat('Send me the file','Send me the files'),mkCat('I fix it yesterday','I fixed it yesterday'),mkCat('Sorry busy','Sure, I can send it by Friday.','dialogue')]);
console.log('cats',JSON.stringify(cats));assert.deepEqual(cats,['Thì của động từ','Mạo từ a/an/the','Câu cộc / thiếu ý','Giới từ','Số nhiều / -s','Số nhiều / -s','Số nhiều / -s','Thì của động từ','Cách đáp / tình huống']);
// kết quả mic về muộn sau khi rời màn → không vẽ đè; "Xem đáp án" bị khoá khi đang nghe
await p.evaluate(()=>{mkAdd({src:'fix',wrong:'I go yesterday',right:'I went yesterday'});window.__srSay=null;mkQuizStart();});await p.waitForTimeout(100);
await p.evaluate(()=>{mkMic();});await p.waitForTimeout(20);
assert.ok(await p.evaluate(()=>{const b=[...document.querySelectorAll('#main .btn')].find(x=>/Xem đáp án/.test(x.textContent));return b&&b.disabled;}),'peek disabled while listening');
await p.evaluate(()=>go('home'));await p.waitForTimeout(400);
assert.ok(!/Lỗi 1\//.test(await txt(p))&&await p.evaluate(()=>window.__view==='home'),'không vẽ đè');
await p.evaluate(()=>{store.mistakes=[];mkq=null;save(store);});
await p.evaluate(()=>{openDay(1);});await p.waitForTimeout(200);
await p.evaluate(()=>{const d=DIALOGUES[DAYS[0].di];const bad=d.opts.find(o=>!o.good);[...document.querySelectorAll('#main .opt')].find(x=>x.textContent.startsWith(bad.t)).click();});
await p.evaluate(()=>psrsFromFix('"I send it yesterday" => "I sent it yesterday" ~ quá khứ\n"I have meeting" => "I have a meeting" ~ thiếu mạo từ'));
await p.evaluate(()=>{mkAdd({src:'pron',right:'schedule',wrong:'sedule'});mkAdd({src:'pron',right:'schedule',wrong:'sedule'});});
let st=await p.evaluate(()=>({n:store.mistakes.length,src:store.mistakes.map(m=>m.src).sort(),dupN:store.mistakes.find(m=>m.src==='pron').n}));
console.log('mistakes',JSON.stringify(st));assert.equal(st.n,4);assert.deepEqual(st.src,['dialogue','fix','fix','pron']);assert.equal(st.dupN,1,'cùng ngày không cộng dồn');
await p.evaluate(()=>{mkq=null;go('mistakes');});await p.waitForTimeout(150);
assert.ok(/Thì của động từ/.test(await txt(p))&&/Ôn lỗi 5 phút/.test(await txt(p)),'list');await shot(p,'n_mk_list');
// ôn: nói đúng mọi câu → ok, 2 lượt → đã nắm
for(let round=0;round<2;round++){
  await p.evaluate(()=>{window.__srSay=function(){return mkq.items[mkq.i].right;};mkQuizStart();});
  for(let i=0;i<8;i++){const more=await p.evaluate(()=>mkq&&mkq.i<mkq.items.length);if(!more)break;await p.evaluate(()=>mkMic());await until(p,()=>mkq.res&&mkq.res.pass!=null);await p.evaluate(()=>{mkq.i++;mkq.res=null;vMistakes();});}
}
st=await p.evaluate(()=>({active:mkActive().length,mast:store.mistakes.filter(m=>m.m).length,last:store.stats.mkLast}));console.log('after review',JSON.stringify(st));
assert.equal(st.active,0);assert.equal(st.mast,4);assert.equal(st.last,new Date().toISOString().slice(0,10));
// thẻ Hôm nay khi ≥5 lỗi và chưa ôn tuần này
await p.evaluate(()=>{store.stats.mkLast=null;for(let i=0;i<5;i++)mkAdd({src:'fix',wrong:'I go there '+i,right:'I went there '+i});save(store);go('home');});await p.waitForTimeout(200);
assert.ok(/Ôn 5 phút đúng lỗi của bạn/.test(await txt(p)),'home card');await shot(p,'n_mk_home');
report(p,'N mistakes');await p.close();}
// 3) Chuẩn bị nhanh (không AI → câu từ gói) + hỏi lại sau sự kiện
{const p=await page(b,{claude:false,store:baseStore({stats:{placed:true,sundayShown:wk},cfg:{level:'A2',autoSpeak:false,track:'office',trackChosen:true},events:[{id:1,date:tmr,type:'other',note:'meeting with the client about the report deadline',time:'09:00'},{id:2,date:yest,type:'other',note:'demo'}]})});
await p.goto(BASE+'index.html');await p.waitForTimeout(500);
let t=await txt(p);assert.ok(/vừa rồi thế nào/.test(t)&&/Chuẩn bị/.test(t),'home: hỏi lại + chuẩn bị');await shot(p,'n_ev_home');
await p.evaluate(()=>prepModal(store.events.find(e=>e.id===1)));assert.ok(await until(p,()=>{const e=store.events.find(e=>e.id===1);return e.prep&&document.querySelector('.modal')&&/5 câu bạn sẽ cần nói/.test(document.querySelector('.modal').textContent);}));
const pr=await p.evaluate(()=>{const e=store.events.find(e=>e.id===1);return {n:e.prep.phrases.length,src:e.prep.src};});console.log('prep',JSON.stringify(pr));assert.equal(pr.n,5);assert.equal(pr.src,'offline');
await p.evaluate(()=>[...document.querySelectorAll('.modal .btn')].find(x=>/Thêm 5 câu/.test(x.textContent)).click());
assert.ok(await p.evaluate(()=>store.events.find(e=>e.id===1).prepSaved&&Object.keys(store.psrs||{}).length>=5));await shot(p,'n_ev_prep');
await p.evaluate(()=>closeModal());
await p.evaluate(()=>[...document.querySelectorAll('#main .chip')].find(x=>/Ổn/.test(x.textContent)).click());await p.waitForTimeout(200);
assert.equal(await p.evaluate(()=>store.events.find(e=>e.id===2).after),'good');assert.ok(!/vừa rồi thế nào/.test(await txt(p)));
report(p,'N prep');await p.close();}
// 4) Mẫu email: chọn mẫu, điền ô, sao chép; AI chỉnh (AI giả)
{const aiJson=`if(/workplace email|chat message/.test(prompt))return {subject:'Leave request – Friday',body:'Hi Anna,\\n\\nPolished body.\\n\\nBest,\\nLan',note:'Sửa ngữ pháp'};return [];`;
const p=await page(b,{aiJson,store:baseStore({stats:{placed:true,sundayShown:wk},cfg:{level:'A2',autoSpeak:false,track:'hotel',trackChosen:true}})});
await p.addInitScript(()=>{window.__clip='';Object.defineProperty(navigator,'clipboard',{configurable:true,get(){return {writeText:async t=>{window.__clip=t;}};}});});
await p.goto(BASE+'index.html');await p.waitForTimeout(500);
await p.evaluate(()=>mailStart());assert.ok(await until(p,()=>window.MAIL_TPL&&/Của ngành Khách sạn/.test(document.getElementById('main').textContent)));
const cnt=await p.evaluate(()=>({all:MAIL_TPL.length,mine:mailList().length}));console.log('mail',JSON.stringify(cnt));assert.equal(cnt.mine,19);await shot(p,'n_mail_list');
await p.evaluate(()=>{ml.tpl=MAIL_TPL.find(t=>t.id==='leave');ml.vals=null;vMail();});await p.waitForTimeout(150);
await p.evaluate(()=>{const ins=[...document.querySelectorAll('#main input.input')];const set=(i,v)=>{ins[i].value=v;ins[i].dispatchEvent(new Event('input'));};set(0,'Anna');set(1,'Friday, May 10');set(2,'Minh');set(ins.length-1,'Lan');});
let o=await p.evaluate(()=>{const pre=[...document.querySelectorAll('#main .card div')].find(x=>x.style.whiteSpace==='pre-wrap');return pre.textContent;});
console.log('mail out',JSON.stringify(o.slice(0,120)));assert.ok(/Hi Anna/.test(o)&&/Friday, May 10/.test(o)&&/Minh/.test(o)&&/Lan/.test(o)&&!/\[/.test(o));
await p.evaluate(()=>[...document.querySelectorAll('#main .btn')].find(x=>/Sao chép/.test(x.textContent)).click());await p.waitForTimeout(100);
assert.ok(await p.evaluate(()=>/^Subject: Leave request/.test(window.__clip)),'copy');
assert.equal(await p.evaluate(()=>store.cfg.myName),'Lan');
await p.evaluate(()=>{const ins=[...document.querySelectorAll('#main input.input')];ins[1].value='thứ Sáu tuần sau';ins[1].dispatchEvent(new Event('input'));});
assert.ok(/gõ tiếng Việt/.test(await txt(p)),'cảnh báo ô tiếng Việt');
await p.evaluate(()=>mailAi(ml.tpl));await p.waitForTimeout(600);assert.ok(await until(p,()=>ml.out&&/Polished body/.test(document.getElementById('main').textContent)));await shot(p,'n_mail_ai');
await p.evaluate(()=>{ml.tone='short';ml.out=null;vMail();});o=await p.evaluate(()=>[...document.querySelectorAll('#main .card div')].find(x=>x.style.whiteSpace==='pre-wrap').textContent);assert.ok(o.length<300,'bản ngắn');
report(p,'N mail');await p.close();}
await b.close();console.log('N ALL OK');
