// game3d: "Ngày đầu đi làm" — WebGL dựng được, hội thoại chọn đáp, chấm ấn tượng, AI nói chuyện cuối ngày, link từ game 2D
import {launch,page,BASE,baseStore,shot,report} from './lib.mjs';
import assert from 'assert/strict';
const ai=`return "Nice to meet you! How was your first day?\\nFIX: I very tired => I am very tired ~ thiếu động từ be";`;
const b=await launch();
// 1) không AI → 5 điểm chọn đáp
let p=await page(b,{store:baseStore({cfg:{level:'A2',autoSpeak:false,track:'office',trackChosen:true}}),claude:false});
await p.goto(BASE+'game3d/index.html');await p.waitForTimeout(900);
assert.ok(await p.evaluate(()=>/Ngày đầu đi làm/.test(document.getElementById('panel').textContent)),'intro');
assert.ok(await p.evaluate(()=>/Chưa có AI/.test(document.getElementById('panel').textContent)),'báo chưa có AI');
await shot(p,'o_intro');
await p.click('#go');await p.waitForTimeout(500);
for(let i=0;i<5;i++){
  assert.equal(await p.evaluate(()=>window.__g3d.st.i),i,'điểm '+i);
  assert.ok(await p.evaluate(()=>document.querySelectorAll('#opts .opt').length>=2),'có lựa chọn');
  if(i===0)await shot(p,'o_scene0');
  await p.evaluate(()=>document.querySelector('#opts .opt').click());await p.waitForTimeout(150);
  assert.ok(await p.evaluate(()=>!!document.querySelector('.fb')),'có phản hồi');
  await p.click('#nx');await p.waitForTimeout(350);
}
const r=await p.evaluate(()=>({t:document.getElementById('panel').textContent,imp:window.__g3d.st.imp,total:window.__g3d.st.total,best:window.__g3d.S().best}));
console.log('result',JSON.stringify({imp:r.imp,total:r.total,best:r.best}));
assert.equal(r.total,5);assert.ok(/Ấn tượng/.test(r.t)&&/Chơi lại/.test(r.t));await shot(p,'o_end');
assert.ok(await p.evaluate(()=>{const c=document.getElementById('c'),g=c.getContext('webgl2')||c.getContext('webgl');return !!g;}),'WebGL');
report(p,'O no-ai');await p.close();
// 2) có AI → điểm cuối là nói chuyện tự do 3 lượt, lỗi vào tổng kết
p=await page(b,{ai,store:baseStore({cfg:{level:'A2',autoSpeak:false,track:'it',trackChosen:true}})});
await p.goto(BASE+'game3d/index.html');await p.waitForTimeout(900);
await p.click('#go');await p.waitForTimeout(400);
for(let i=0;i<5;i++){
  await p.evaluate(()=>document.querySelector('#opts .opt').click());await p.waitForTimeout(120);
  await p.click('#nx');await p.waitForTimeout(500);
  assert.ok(await p.evaluate(()=>!!document.getElementById('inp')),'chat điểm '+i);
  const n=i===4?3:2;
  for(let k=0;k<n;k++){const m=i===4&&k===0?'I very tired today.':'I like it.';await p.evaluate(m=>{document.getElementById('inp').value=m;document.getElementById('snd').click();},m);await p.waitForTimeout(450);}
  if(i<4){await p.click('#endd');await p.waitForTimeout(350);}
}
assert.ok(await p.evaluate(()=>!!document.getElementById('endd')),'nút kết thúc sau 3 lượt');
await shot(p,'o_chat');
await p.click('#endd');await p.waitForTimeout(300);
const r2=await p.evaluate(()=>({t:document.getElementById('panel').textContent,miss:window.__g3d.st.miss.length}));
assert.ok(/I am very tired/.test(r2.t)&&r2.miss>=1,'lỗi AI hiện ở tổng kết');
report(p,'O ai');await p.close();
// 3) link từ game 2D
p=await page(b,{store:baseStore({cfg:{level:'A2',autoSpeak:false,track:'hotel',trackChosen:true}})});
await p.goto(BASE+'game/index.html');await p.waitForTimeout(800);
const lk=await p.evaluate(()=>{const t=[...document.querySelectorAll('.tab')].find(x=>/Hồ sơ/.test(x.textContent));t.click();return true;});await p.waitForTimeout(400);
assert.ok(await p.evaluate(()=>/Ngày đầu đi làm/.test(document.getElementById('main').textContent)),'link ở Hồ sơ');
report(p,'O link');await p.close();await b.close();console.log('O ALL OK');
