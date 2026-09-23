// v4.0: tài khoản khách tự động + Google, đồng bộ offline-first giữa 2 máy, gộp tiến độ, AI qua máy chủ, báo lỗi, xoá tài khoản.
// Dùng máy chủ giả (tests/cloud-fake.mjs) thay Supabase — cloud.js nhận adapter qua window.NN_CLOUD_ADAPTER.
import {launch,page,BASE,baseStore,shot,report} from './lib.mjs';
import {fakeServer,adapterInit} from './cloud-fake.mjs';
import assert from 'assert/strict';
const d=new Date(),dow=(d.getDay()+6)%7,mon=new Date(d);mon.setDate(d.getDate()-dow);const wk=mon.toISOString().slice(0,10);
const srv=fakeServer();
const b=await launch();
async function device(store,email){
  const p=await page(b,{claude:false,store});
  await p.exposeFunction('nnFake',(m,a)=>{try{return srv.handle(m,a);}catch(e){return {__err:e.message};}});
  await p.route(/cloud-config\.js$/,r=>r.fulfill({contentType:'text/javascript',body:"window.NN_CLOUD_CONFIG={url:'https://test.supabase.co',anonKey:'anon-test'};"}));
  await p.addInitScript(adapterInit);
  await p.addInitScript(e=>{window.__googleEmail=e;},email||'an@example.com');
  return p;
}
const st=()=>baseStore({stats:{placed:true,sundayShown:wk},cfg:{level:'A2',autoSpeak:false,track:'office',trackChosen:true}});
const until=async(p,fn,ms=6000)=>{for(let i=0;i<ms/100;i++){try{if(await p.evaluate(fn))return true;}catch(e){}await p.waitForTimeout(100);}return false;};
const sync=p=>p.evaluate(()=>NNCloud.syncNow({pull:true}));
const cs=p=>p.evaluate(()=>NNCloud.state());
const userOf=async p=>srv.users.get(await p.evaluate(()=>localStorage.getItem('fake-auth')));

// 1) Máy 1 mở app → tự tạo khách, đẩy tiến độ sẵn có lên server, hiện thông báo lần đầu
const p1=await device(st(),'an@example.com');
await p1.goto(BASE+'index.html');
assert.ok(await until(p1,()=>NNCloud.state().status==='ok'),'guest synced');
let s1=await cs(p1);console.log('guest',JSON.stringify({anon:s1.anon,status:s1.status,pending:s1.pending}));
assert.ok(s1.anon && s1.pending===0);
let u1=await userOf(p1);assert.equal(u1.state['tdays|office|done|4'],true);assert.equal(u1.state['tdays|office|cur'],5);
await p1.evaluate(()=>go('home'));await p1.waitForTimeout(900);
assert.ok(await p1.evaluate(()=>/lưu tự động trên máy chủ/.test(document.getElementById('main').textContent)),'notice card');
assert.equal(await p1.evaluate(()=>document.getElementById('tabDot').dataset.st),''); // đã đồng bộ → không chấm
await shot(p1,'i_home_notice');

// 2) Học → tự đồng bộ (debounce) → server có thẻ ôn
await p1.evaluate(()=>{grade('deploy',2);grade('meeting',3);toggleSaved('Could you send me the agenda?','office');});
assert.ok(await until(p1,()=>NNCloud.state().pending===0&&NNCloud.state().status==='ok',8000),'auto sync');
u1=await userOf(p1);assert.equal(u1.state['srs|deploy'].reps,1);assert.ok(u1.state['saved|Could you send me the agenda?']);
const revA=u1.rev;

// 3) Offline: học tiếp → chờ gửi → có mạng lại → gửi đủ, không trùng
await p1.context().setOffline(true);await p1.evaluate(()=>window.dispatchEvent(new Event('offline')));
await p1.evaluate(()=>{grade('deploy',2);grade('budget',2);});await p1.waitForTimeout(300);
s1=await cs(p1);console.log('offline',JSON.stringify({status:s1.status,pending:s1.pending}));
assert.equal(s1.status,'offline');assert.ok(s1.pending>=2);
await p1.evaluate(()=>renderTabs());assert.equal(await p1.evaluate(()=>document.getElementById('tabDot').dataset.st),'off');
await p1.evaluate(()=>go('account'));await p1.waitForTimeout(150);await shot(p1,'i_account_offline');
await p1.context().setOffline(false);await p1.evaluate(()=>window.dispatchEvent(new Event('online')));
assert.ok(await until(p1,()=>NNCloud.state().pending===0&&NNCloud.state().status==='ok'),'online resync');
u1=await userOf(p1);assert.equal(u1.state['srs|deploy'].reps,2);assert.ok(u1.state['srs|budget']);
console.log('after online rev',revA,'→',u1.rev);

// 3b) Server từ chối lô (lỗi / phản hồi lạ) → giữ nguyên dữ liệu máy + lô chờ, lần sau gửi được
for(const kind of ['state_too_large','bad']){
  srv.failNext=kind;await p1.evaluate(()=>{grade('lỗi-thử',2);});
  await p1.evaluate(()=>NNCloud.syncNow());
  const a=await p1.evaluate(()=>({st:NNCloud.state().status,has:!!store.srs['lỗi-thử'],deploy:store.srs.deploy.reps,pend:NNCloud.state().pending}));
  console.log('server reject',kind,JSON.stringify(a));assert.ok(a.st==='error'&&a.has&&a.deploy===2&&a.pend>0);
  await p1.evaluate(()=>NNCloud.syncNow());assert.equal((await cs(p1)).status,'ok');
  assert.ok((await userOf(p1)).state['srs|lỗi-thử']);
}

// 4) Gửi lại lô cũ (mất phản hồi) → server bỏ qua, không cộng đôi
const dup=srv.handle('rpc',{uid:[...srv.users.keys()][0],name:'apply_changes',args:{p_id:'x1',p_changes:[{p:'hist|2000-01-01',v:1}]}});
const dup2=srv.handle('rpc',{uid:[...srv.users.keys()][0],name:'apply_changes',args:{p_id:'x1',p_changes:[{p:'hist|2000-01-01',v:1}]}});
assert.ok(dup2.dup && dup2.rev===dup.rev);

// 5) AI miễn phí qua máy chủ (không có key riêng, không chạy trong claude.ai)
const ai=await p1.evaluate(async()=>{aiReset();const sp=await aiInit();const r=await sp([{role:'user',content:'sys'},{role:'user',content:'hello'}]);return {cloud:!!(sp&&sp.__cloud)||true,text:r.text,cfg:aiConfigured()};});
console.log('cloud ai',JSON.stringify(ai));assert.ok(/Cloud AI says hi/.test(ai.text)&&ai.cfg);

// 6) Báo lỗi nội dung → gửi thẳng lên server
await p1.evaluate(()=>{openDay(2);});await p1.waitForTimeout(150);
await p1.evaluate(()=>document.querySelector('#main .flagbtn').click());await p1.waitForTimeout(150);
await p1.evaluate(()=>{document.querySelector('.modal .chip').click();[...document.querySelectorAll('.modal .btn')].find(x=>/Lưu báo lỗi/.test(x.textContent)).click();});
await p1.waitForTimeout(150);const rtext=await p1.evaluate(()=>document.querySelector('.modal').textContent);
assert.ok(/gửi thẳng/.test(rtext));await p1.evaluate(()=>closeModal());
assert.ok(await until(p1,()=>(store.reports||[]).every(r=>r.cloud===1)),'report sent');
u1=await userOf(p1);assert.equal(u1.reports.length,1);

// 7) Lưu bằng Google (linkIdentity) → cùng tài khoản, không mất gì
await p1.evaluate(()=>go('account'));await p1.waitForTimeout(150);await shot(p1,'i_account_guest');
await p1.evaluate(()=>[...document.querySelectorAll('#main .btn')].find(x=>/Lưu tiến độ bằng Google/.test(x.textContent)).click());
await p1.waitForLoadState('load');await p1.waitForTimeout(300);
assert.ok(await until(p1,()=>NNCloud.state().google&&NNCloud.state().status==='ok'),'linked');
s1=await cs(p1);console.log('linked',JSON.stringify({google:s1.google,email:s1.user.email,pending:s1.pending}));
assert.equal(await p1.evaluate(()=>store.srs.deploy.reps),2);
await p1.evaluate(()=>go('account'));await p1.waitForTimeout(250);await shot(p1,'i_account_google');
assert.ok(await p1.evaluate(()=>/an@example\.com/.test(document.getElementById('main').textContent)));
assert.ok(await p1.evaluate(()=>/Còn\s*\d+\s*\/\s*20/.test(document.getElementById('main').textContent)),'quota 20');
// 7b) Mất phiên (đăng xuất nơi khác / token hết hạn) → KHÔNG tự tạo khách mới; đăng nhập lại → cùng tài khoản, không hỏi gộp
const nUsers=srv.users.size;
await p1.evaluate(()=>localStorage.removeItem('fake-auth'));await p1.reload();
assert.ok(await until(p1,()=>NNCloud.state().relogin),'relogin state');assert.equal(srv.users.size,nUsers);
await p1.evaluate(()=>go('account'));await p1.waitForTimeout(200);await shot(p1,'i_relogin');
assert.ok(await p1.evaluate(()=>/Phiên đăng nhập đã hết/.test(document.getElementById('main').textContent)));
await p1.evaluate(()=>[...document.querySelectorAll('#main .btn')].find(x=>/Đăng nhập lại bằng Google/.test(x.textContent)).click());
await p1.waitForLoadState('load');
assert.ok(await until(p1,()=>NNCloud.state().google&&NNCloud.state().status==='ok'&&!document.querySelector('.modal')),'relogged');
assert.equal(await p1.evaluate(()=>store.srs.deploy.reps),2);
report(p1,'I device1');

// 8) Máy 2: mở → khách mới → "Lưu bằng Google" cùng email → báo đã có tài khoản → đăng nhập → máy gần trống nên tự lấy tiến độ tài khoản
const p2=await device(baseStore({stats:{placed:true,sundayShown:wk},days:{cur:1,done:{}},cfg:{level:'A2',autoSpeak:false,track:'office',trackChosen:true}}),'an@example.com');
await p2.goto(BASE+'index.html');
assert.ok(await until(p2,()=>NNCloud.state().anon&&NNCloud.state().status==='ok'),'device2 guest');
await p2.evaluate(()=>NNCloud.linkGoogle());await p2.waitForLoadState('load');await p2.waitForTimeout(400);
assert.ok(await until(p2,()=>!!document.querySelector('.modal')&&/đã có tài khoản/.test(document.querySelector('.modal').textContent)),'identity conflict modal');
await shot(p2,'i_conflict');
await p2.evaluate(()=>[...document.querySelectorAll('.modal .btn')].find(x=>/Đăng nhập tài khoản đó/.test(x.textContent)).click());
await p2.waitForLoadState('load');await p2.waitForTimeout(400);
assert.ok(await until(p2,()=>NNCloud.state().google&&NNCloud.state().status==='ok'),'device2 signed in');
const d2=await p2.evaluate(()=>({deploy:store.srs.deploy&&store.srs.deploy.reps,cur:store.days.cur,saved:store.saved.length}));
console.log('device2 adopted',JSON.stringify(d2));assert.equal(d2.deploy,2);assert.equal(d2.cur,5);assert.equal(d2.saved,1);

// 9) Cả hai máy offline cùng sửa một từ → online → gộp: giữ bản ôn nhiều hơn; ngày học hợp lại
for(const p of [p1,p2]){await p.context().setOffline(true);await p.evaluate(()=>window.dispatchEvent(new Event('offline')));}
await p1.evaluate(()=>{grade('deploy',0);store.days.done[5]=true;save(store);});                // máy 1: quên (reps 0), xong ngày 5
await p2.evaluate(()=>{grade('deploy',2);grade('deploy',2);store.days.done[6]=true;save(store);}); // máy 2: ôn thêm 2 lần (reps 4), xong ngày 6
for(const p of [p1,p2]){await p.context().setOffline(false);await p.evaluate(()=>window.dispatchEvent(new Event('online')));await until(p,()=>NNCloud.state().status==='ok'&&NNCloud.state().pending===0);}
await sync(p1);await sync(p2);await sync(p1);
const m1=await p1.evaluate(()=>({r:store.srs.deploy.reps,d5:!!store.days.done[5],d6:!!store.days.done[6]}));
const m2=await p2.evaluate(()=>({r:store.srs.deploy.reps,d5:!!store.days.done[5],d6:!!store.days.done[6]}));
console.log('merged',JSON.stringify({m1,m2}));assert.deepEqual(m1,{r:4,d5:true,d6:true});assert.deepEqual(m2,m1);
report(p2,'I device2');

// 10) Máy 3 có nhiều tiến độ riêng → đăng nhập Google → hỏi cách gộp → Gộp cả hai
const big=st();big.srs={};for(let i=0;i<12;i++)big.srs['word'+i]={ease:2.3,int:1,reps:1,due:1};
const p3=await device(big,'an@example.com');
await p3.goto(BASE+'index.html');
assert.ok(await until(p3,()=>NNCloud.state().anon&&NNCloud.state().status==='ok'),'device3 guest');
await p3.evaluate(()=>NNCloud.signInGoogle());await p3.waitForLoadState('load');
assert.ok(await until(p3,()=>!!document.querySelector('.modal')&&/đã có tiến độ/.test(document.querySelector('.modal').textContent)),'choice modal');
console.log('choice status',(await cs(p3)).status);await shot(p3,'i_choice');
await p3.evaluate(()=>[...document.querySelectorAll('.modal .btn')].find(x=>/Gộp cả hai/.test(x.textContent)).click());
assert.ok(await until(p3,()=>!document.querySelector('.modal')&&NNCloud.state().status==='ok'&&NNCloud.state().pending===0),'merged choice');
const d3=await p3.evaluate(()=>({w:Object.keys(store.srs).filter(k=>/^word/.test(k)).length,deploy:store.srs.deploy&&store.srs.deploy.reps}));
console.log('device3 merged',JSON.stringify(d3));assert.deepEqual(d3,{w:12,deploy:4});
u1=await userOf(p3);assert.ok(u1.state['srs|word11']);
report(p3,'I device3');

// 11) Xoá tài khoản → server hết dữ liệu, máy chuyển về "chỉ lưu trên máy"
await p3.evaluate(()=>go('account'));await p3.waitForTimeout(150);
await p3.evaluate(()=>[...document.querySelectorAll('#main .iosr')].find(x=>/Xoá tài khoản/.test(x.textContent)).click());await p3.waitForTimeout(100);
await p3.evaluate(()=>{document.querySelector('.modal input.input').value='XOA';[...document.querySelectorAll('.modal .btn')].find(x=>/Xoá tài khoản/.test(x.textContent)).click();});
assert.ok(await until(p3,()=>NNCloud.state().status==='local'),'deleted');
assert.equal(srv.users.size,2); // còn 2 tài khoản khách của máy 2, máy 3 (Google đã xoá)
assert.equal(await p3.evaluate(()=>Object.keys(store.srs).length>10),true);
console.log('after delete',JSON.stringify(await p3.evaluate(()=>({st:NNCloud.state().status,dot:document.getElementById('tabDot').dataset.st}))));
await shot(p3,'i_account_local');
// khởi động lại ở chế độ máy: không tự tạo khách
await p3.reload();await p3.waitForTimeout(700);
assert.equal((await cs(p3)).status,'local');
report(p3,'I delete');
// 12) supabase-js thật (không adapter giả) + máy chủ không tới được → app vẫn chạy, báo lỗi nhẹ, CSP có URL máy chủ
{const p=await page(b,{claude:false,store:st()});
  await p.route(/cloud-config\.js$/,r=>r.fulfill({contentType:'text/javascript',body:"window.NN_CLOUD_CONFIG={url:'http://127.0.0.1:9',anonKey:'anon-test'};"}));
  await p.goto(BASE+'index.html');
  assert.ok(await until(p,()=>['error','offline'].includes(NNCloud.state().status),15000),'real sdk error state');
  const r=await p.evaluate(()=>({sdk:typeof window.supabase,csp:document.querySelector('meta[http-equiv="Content-Security-Policy"]').content.includes('http://127.0.0.1:9 ws://127.0.0.1:9'),st:NNCloud.state().status,title:document.querySelector('#main .eyebrow')&&document.querySelector('#main .eyebrow').textContent}));
  console.log('real sdk',JSON.stringify(r));assert.ok(r.sdk==='object'&&r.csp);
  const n0=await p.evaluate(()=>performance.getEntriesByType('resource').filter(e=>/127\.0\.0\.1:9/.test(e.name)).length);
  await p.waitForTimeout(6500);
  const n1=await p.evaluate(()=>performance.getEntriesByType('resource').filter(e=>/127\.0\.0\.1:9/.test(e.name)).length);
  console.log('guest retry requests',n0,'→',n1);assert.ok(n1>n0&&n1<n0+4,'backoff retry');
  p.errs=p.errs.filter(e=>!/127\.0\.0\.1:9|Failed to fetch|ERR_CONNECTION/.test(e));report(p,'I real-sdk');}
console.log('rpc calls',srv.calls.length,'report_content',srv.calls.filter(c=>/report_content/.test(c)).length);
await b.close();
