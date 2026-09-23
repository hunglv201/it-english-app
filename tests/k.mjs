// v4.0 đợt A/C/D: nhắc học (push giả), cam kết 7 ngày, lớp học + bảng tuần + bạn học (server giả), kiểm tra trình độ 3 phút,
// tiếng Nhật công sở (furigana từ romaji, kính ngữ, đố nhanh), 2 ngành mới
import {launch,page,BASE,baseStore,shot,report} from './lib.mjs';
import {fakeServer,adapterInit} from './cloud-fake.mjs';
import assert from 'assert/strict';
const d=new Date(),dow=(d.getDay()+6)%7,mon=new Date(d);mon.setDate(d.getDate()-dow);const wk=mon.toISOString().slice(0,10);
const today=new Date().toISOString().slice(0,10),yest=new Date(Date.now()-864e5).toISOString().slice(0,10);
const b=await launch();
const until=async(p,fn,ms=6000)=>{for(let i=0;i<ms/100;i++){try{if(await p.evaluate(fn))return true;}catch(e){}await p.waitForTimeout(100);}return false;};
const st=(extra={})=>baseStore(Object.assign({stats:{placed:true,sundayShown:wk},cfg:{level:'A2',autoSpeak:false,track:'office',trackChosen:true}},extra));

// 1) Tiếng Nhật: romaji → hiragana, furigana chỉ trên Kanji
let p=await page(b,{store:st({cfg:{level:'A2',autoSpeak:false,track:'office',trackChosen:true,showJa:true}})});
await p.goto(BASE+'index.html');await p.waitForTimeout(500);
const j1=await p.evaluate(()=>({a:romajiToHira('kakunin'),b:romajiToHira('shōnin'),c:romajiToHira('kitte'),d:romajiToHira('konban'),e:jaRuby('確認する','kakunin suru'),f:jaRuby('デプロイ','depuroi'),g:romajiToHira('xyz'),h:jaRuby('会議室','kaigishitsu')}));
console.log('ja',JSON.stringify(j1));
assert.equal(j1.a,'かくにん');assert.equal(j1.b,'しょうにん');assert.equal(j1.c,'きって');assert.equal(j1.d,'こんばん');
assert.equal(j1.e,'<ruby>確認<rt>かくにん</rt></ruby>する');assert.equal(j1.f,'デプロイ');assert.equal(j1.g,null);assert.equal(j1.h,'<ruby>会議室<rt>かいぎしつ</rt></ruby>');
// kính ngữ
await p.evaluate(()=>keigoStart());await until(p,()=>!!window.JA_KEIGO&&/Kính ngữ/.test(document.getElementById('main').textContent));
const j2=await p.evaluate(()=>({groups:JA_KEIGO.length,cards:document.querySelectorAll('#main ruby').length,btn:document.querySelectorAll('#main [data-jasay]').length}));
console.log('keigo',JSON.stringify(j2));assert.equal(j2.groups,7);assert.ok(j2.cards>=6&&j2.btn>=6);await shot(p,'k_keigo');
await p.evaluate(()=>{[...document.querySelectorAll('#main .chip')].find(c=>/Romaji/.test(c.textContent)).click();});
assert.equal(await p.evaluate(()=>store.cfg.jaRomaji),false);
await p.evaluate(()=>kgQuizStart());
for(let i=0;i<8;i++){await p.evaluate(()=>{var q=kg.quiz,it=q.items[q.i];var bs=[...document.querySelectorAll('#main .opt')];var k=q.opts.indexOf(it);bs[k].click();});
  await p.evaluate(()=>{[...document.querySelectorAll('#main .btn')].find(x=>/Tiếp/.test(x.textContent)).click();});}
assert.ok(await p.evaluate(()=>/8\/8 câu đúng/.test(document.getElementById('main').textContent)),'quiz 8/8');
assert.equal(await p.evaluate(()=>jaMatch({ja:'お疲れ様です。',kana:'おつかれさまです。'},'お疲れ様です')),100);
assert.ok(await p.evaluate(()=>jaMatch({ja:'お疲れ様です。',kana:'おつかれさまです。'},'おつかれ'))<60);
report(p,'K ja');await p.close();

// 2) Kiểm tra trình độ 3 phút (không có nhận giọng nói → bỏ phần đọc)
p=await page(b,{store:{cfg:{level:'A2',autoSpeak:false}}});
await p.goto(BASE+'index.html');await p.waitForTimeout(900);
await p.evaluate(()=>{closeModal();onboardModal(3,{track:'office'});});await p.waitForTimeout(150);
await p.evaluate(()=>[...document.querySelectorAll('.modal .btn')].find(x=>/Kiểm tra nhanh/.test(x.textContent)).click());await p.waitForTimeout(150);
await p.evaluate(()=>[...document.querySelectorAll('.modal .btn')].find(x=>/Bắt đầu/.test(x.textContent)).click());
for(let i=0;i<3;i++){await p.waitForTimeout(120);await p.evaluate(i=>{var it=PT_LISTEN[i];[...document.querySelectorAll('.modal .btn')].find(x=>x.textContent===it.s).click();},i);}
for(let i=0;i<2;i++){await p.waitForTimeout(120);await p.evaluate(()=>{var b=[...document.querySelectorAll('.modal .btn')].find(x=>/Không nói được/.test(x.textContent));if(b)b.click();});}
await p.waitForTimeout(120);await shot(p,'k_pt_time');
await p.evaluate(()=>[...document.querySelectorAll('.modal .btn')].find(x=>/Tối/.test(x.textContent)).click());await p.waitForTimeout(120);
const pt=await p.evaluate(()=>document.querySelector('.modal').textContent);console.log('pt',pt.slice(0,90));assert.ok(/B2/.test(pt)&&/ngày 51/.test(pt));
await shot(p,'k_pt_result');
await p.evaluate(()=>[...document.querySelectorAll('.modal .btn')].find(x=>/Bắt đầu học/.test(x.textContent)).click());await p.waitForTimeout(200);
const pt2=await p.evaluate(()=>({cur:store.days.cur,level:store.cfg.level,time:store.cfg.studyTime,remind:store.cfg.remind,placed:store.stats.placed}));
console.log('placed',JSON.stringify(pt2));assert.deepEqual(pt2,{cur:51,level:'B2',time:'evening',remind:'20:30',placed:true});
report(p,'K placement');await p.close();

// 3) Cam kết 7 ngày
p=await page(b,{store:st({stats:{placed:true,sundayShown:wk,streak:3,lastActive:yest}}),game:{coins:60,lv:1,xp:0}});
await p.goto(BASE+'index.html');await p.waitForTimeout(500);
await p.evaluate(()=>{go('me');wagerModal();});await p.waitForTimeout(150);
await p.evaluate(()=>[...document.querySelectorAll('.modal .btn')].find(x=>/Cam kết \(đặt/.test(x.textContent)).click());
const w1=await p.evaluate(()=>({w:store.stats.wager,coins:gameSave().coins}));console.log('wager',JSON.stringify(w1));
assert.equal(w1.coins,10);assert.equal(w1.w.target,10);
await p.evaluate(()=>{store.stats.streak=9;save(store);markToday('vocab');});await p.waitForTimeout(2600);
const w2=await p.evaluate(()=>({w:store.stats.wager,coins:gameSave().coins,c:document.querySelector('.celebr')&&document.querySelector('.celebr').textContent}));
console.log('wager done',JSON.stringify(w2));assert.equal(w2.w,undefined);assert.equal(w2.coins,110);
report(p,'K wager');await p.close();

// 4) Máy chủ giả: nhắc học (push giả), bạn học, bảng tuần, lớp học
const srv=fakeServer();
async function device(store,email){
  const q=await page(b,{claude:false,store});
  await q.exposeFunction('nnFake',(m,a)=>{try{return srv.handle(m,a);}catch(e){return {__err:e.message};}});
  await q.route(/cloud-config\.js$/,r=>r.fulfill({contentType:'text/javascript',body:"window.NN_CLOUD_CONFIG={url:'https://test.supabase.co',anonKey:'anon-test',vapidPublicKey:'BEl62iUYgUivxIkv69yViEuiBIa-Ib9-SkvMeAtA3LFgDzkrxZJjSgSnfckjBJuBkr3qBUYIHBQFLXYp5Nksh8U'};"}));
  await q.addInitScript(adapterInit);
  await q.addInitScript(e=>{window.__googleEmail=e;
    window.__subs=0;const sub={endpoint:'https://push.example/'+Math.random().toString(36).slice(2),toJSON(){return {endpoint:this.endpoint,keys:{p256dh:'k',auth:'a'}};},unsubscribe:async()=>true};
    const pm={getSubscription:async()=>window.__subs?sub:null,subscribe:async()=>{window.__subs++;return sub;}};
    Object.defineProperty(navigator,'serviceWorker',{configurable:true,get(){return {ready:Promise.resolve({pushManager:pm}),register:async()=>({}),addEventListener(){},controller:null};}});
    window.PushManager=function(){};window.Notification=function(){};Notification.permission='default';Notification.requestPermission=async()=>{Notification.permission='granted';return 'granted';};},email||'an@example.com');
  return q;
}
const p1=await device(st({hist:{[yest]:2},days:{cur:3,done:{1:true,2:true}}}),'an@example.com');
await p1.goto(BASE+'index.html');
assert.ok(await until(p1,()=>NNCloud.state().status==='ok'),'p1 ok');
await p1.evaluate(()=>{NNCloud.markNotice();go('home');});await p1.waitForTimeout(300);
assert.ok(await p1.evaluate(()=>/Bật nhắc học\?/.test(document.getElementById('main').textContent)),'push card');await shot(p1,'k_push_card');
await p1.evaluate(()=>[...document.querySelectorAll('#main .btn')].find(x=>/^Bật nhắc học$/.test(x.textContent)).click());
assert.ok(await until(p1,()=>NNCloud.pushInfo().on),'push on');
let uid1=await p1.evaluate(()=>localStorage.getItem('fake-auth'));
console.log('push saved',JSON.stringify(srv.push[uid1]));assert.ok(srv.push[uid1].sub&&srv.push[uid1].mode==='auto'&&typeof srv.push[uid1].tz==='number');
await p1.evaluate(()=>{markToday('vocab');});await p1.evaluate(()=>NNCloud.syncNow());await p1.waitForTimeout(200);
assert.equal(typeof srv.push[uid1].first,'number','touch_reminder');
await p1.evaluate(()=>go('account'));await p1.waitForTimeout(200);await shot(p1,'k_account_remind');
await p1.evaluate(()=>[...document.querySelectorAll('#main .chip')].find(x=>/Giờ cố định/.test(x.textContent)).click());await p1.waitForTimeout(200);
assert.equal(srv.push[uid1].mode,'fixed');
// bạn học: máy 1 tạo lời mời
await p1.evaluate(()=>socialStart());await until(p1,()=>/Tạo link mời/.test(document.getElementById('main').textContent));
await p1.evaluate(()=>{var i=[...document.querySelectorAll('#main input.input')][0];i.value='An';[...document.querySelectorAll('#main .btn')].find(x=>/Tạo link mời/.test(x.textContent)).click();});
assert.ok(await until(p1,()=>/\?buddy=/.test(document.getElementById('main').textContent)),'invite link');
const link=await p1.evaluate(()=>[...document.querySelectorAll('#main div')].map(x=>x.textContent).find(t=>/\?buddy=/.test(t)&&t.length<200));
const code=link.match(/buddy=([A-Z0-9]+)/)[1];console.log('buddy code',code);
// bảng tuần + lớp: máy 1 là khách → chưa tạo được lớp
await p1.evaluate(()=>{var ins=[...document.querySelectorAll('#main input.input')];ins[0].value='An';[...document.querySelectorAll('#main .btn')].find(x=>/Tham gia bảng tuần/.test(x.textContent)).click();});
assert.ok(await until(p1,()=>/Rời bảng xếp hạng/.test(document.getElementById('main').textContent)),'league on');
assert.ok(await p1.evaluate(()=>/Lưu tài khoản bằng Google trước/.test(document.getElementById('main').textContent)),'guest cannot create class');
await shot(p1,'k_social_guest');
report(p1,'K device1');
// máy 2: mở bằng link mời → nhận lời
const p2=await device(st({hist:{[today]:1}}),'binh@example.com');
await p2.goto(BASE+'index.html?buddy='+code);
assert.ok(await until(p2,()=>!!document.querySelector('.modal')&&/Lời mời học cặp/.test(document.querySelector('.modal').textContent),8000),'buddy modal');
assert.ok(await p2.evaluate(()=>!/buddy=/.test(location.search)),'url cleaned');
await p2.evaluate(()=>{document.querySelector('.modal input.input').value='Bình';[...document.querySelectorAll('.modal .btn')].find(x=>/Nhận lời/.test(x.textContent)).click();});
assert.ok(await until(p2,()=>!document.querySelector('.modal')),'accepted');
assert.equal(srv.buddies.length,1);
// máy 2 lưu bằng Google → tạo lớp
await p2.evaluate(()=>NNCloud.linkGoogle());await p2.waitForLoadState('load');
assert.ok(await until(p2,()=>NNCloud.state().google&&NNCloud.state().status==='ok'),'p2 google');
await p2.evaluate(()=>socialStart());await until(p2,()=>/Tạo lớp/.test(document.getElementById('main').textContent));
assert.ok(await p2.evaluate(()=>/An/.test(document.getElementById('main').textContent)&&/Nhắc An/.test(document.getElementById('main').textContent)),'buddy paired view');
await p2.evaluate(()=>[...document.querySelectorAll('#main .btn')].find(x=>/Nhắc An/.test(x.textContent)).click());await p2.waitForTimeout(300);
assert.equal(srv.nudges.length,1);
await p2.evaluate(()=>[...document.querySelectorAll('#main .btn')].find(x=>/Tạo lớp/.test(x.textContent)).click());await p2.waitForTimeout(100);
await p2.evaluate(()=>{document.querySelector('.modal input.input').value='Phòng Kinh doanh';[...document.querySelectorAll('.modal .btn')].find(x=>/^Tạo lớp$/.test(x.textContent)).click();});
assert.ok(await until(p2,()=>/Phòng Kinh doanh/.test(document.getElementById('main').textContent)),'class created');
const ccode=srv.classes[0].code;await shot(p2,'k_social_owner');
// máy 1 vào lớp: phải tick đồng ý
await p1.evaluate(c=>{joinClassModal(c);},ccode);await p1.waitForTimeout(100);
await p1.evaluate(()=>{[...document.querySelectorAll('.modal .btn')].find(x=>/^Vào lớp$/.test(x.textContent)).click();});await p1.waitForTimeout(150);
assert.equal(srv.classes[0].members.length,0,'no consent → not joined');
await p1.evaluate(()=>{document.querySelector('.modal input.input').value='An';document.querySelector('.modal input[type=checkbox]').checked=true;[...document.querySelectorAll('.modal .btn')].find(x=>/^Vào lớp$/.test(x.textContent)).click();});
assert.ok(await until(p1,()=>!document.querySelector('.modal')),'joined');assert.equal(srv.classes[0].members.length,1);
// chủ lớp xem bảng + báo cáo
await p2.evaluate(()=>socialLoad());await p2.waitForTimeout(300);
await p2.evaluate(()=>{[...document.querySelectorAll('#main .si')].find(x=>/Phòng Kinh doanh/.test(x.textContent)).click();});
assert.ok(await until(p2,()=>/Báo cáo cho chủ lớp/.test(document.getElementById('main').textContent)&&document.querySelectorAll('#main table tr').length===2),'owner report');
assert.ok(await p2.evaluate(()=>/Xuất CSV/.test(document.getElementById('main').textContent)&&/An/.test(document.getElementById('main').textContent)));
await shot(p2,'k_class_owner');
report(p2,'K device2');
// 5) Ngành mới nạp được
for(const t of ['construction','aviation']){const q=await page(b,{store:st({cfg:{level:'A2',autoSpeak:false,track:t,trackChosen:true}})});
  await q.goto(BASE+'index.html');await q.waitForTimeout(500);
  const info=await q.evaluate(()=>({track:TRACK,days:DAYS.length,label:TRK.label,rep:REPORT.title,hint:REPORT.hint}));console.log('pack',JSON.stringify(info));
  assert.equal(info.track,t);assert.equal(info.days,120);report(q,'K '+t);await q.close();}
await b.close();
