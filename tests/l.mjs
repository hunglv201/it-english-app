// G3: game — boss cuối chặng theo ngành (3 pha), thắng/thua ghi nhận, màn kết cục + chế độ vô tận, dữ liệu game cũ
import {launch,page,BASE,baseStore,shot,report} from './lib.mjs';
const b=await launch();let fail=0;
const ok=(c,msg)=>{console.log((c?'  ok  ':'  FAIL ')+msg);if(!c)fail++;};
const gstore=(extra={})=>Object.assign({seenTut:true,cur:11,ch:0,hp:100,maxHp:100,coins:0,idle:{last:Date.now(),bugs:0}},extra);
// đánh tới khi hết trận: mode 'win' chọn đúng, 'lose' chọn sai
async function fight(p,mode,max=60){const kinds=new Set();
  for(let i=0;i<max;i++){
    const st=await p.evaluate(()=>{const s=NNGame.state();return s.B?{locked:s.B.locked,has:!!s.B.cur,kind:s.B.cur&&s.B.cur.kind,stage:s.B.stage}:null;});
    if(!st)break;
    if(st.locked||!st.has||!(await p.$('.opt:not([disabled])'))){await p.waitForTimeout(150);i--;continue;}
    kinds.add(st.stage+':'+st.kind);
    await p.evaluate(m=>{const B=NNGame.state().B;const os=[...document.querySelectorAll('.opt:not([disabled])')];const o=m==='win'?os.find(x=>x.textContent===B.cur.ans):os.find(x=>x.textContent!==B.cur.ans);(o||os[0]).click();},mode);
    await p.waitForTimeout(80);
  }
  await p.waitForTimeout(1200);return [...kinds];}
for(const t of ['hotel','it','factory','aviation']){
  console.log('== '+t);
  const p=await page(b,{store:baseStore({cfg:{level:'A2',autoSpeak:false,track:t,trackChosen:true}}),game:gstore()});
  await p.goto(BASE+'game/index.html');await p.waitForTimeout(700);
  // 1) boss node cuối dải chặng 1 (đã mở vì cur=11)
  const node=await p.evaluate(()=>{const n=document.querySelector('#pbNode');return n&&{cls:n.className,last:n===n.parentNode.lastElementChild};});
  ok(node&&node.last&&!/lock/.test(node.cls),'boss node ở cuối chặng 1, đã mở ('+(node&&node.cls)+')');
  if(t==='hotel')await shot(p,'l_map_'+t);
  await p.click('#pbNode');await p.waitForTimeout(250);
  const intro=await p.evaluate(()=>({txt:document.querySelector('.modal').textContent,def:NNGame.pbDef(0).n}));
  ok(intro.txt.includes(intro.def),'intro boss: '+intro.def);
  await p.click('#pbGo');await p.waitForTimeout(500);
  const f0=await p.evaluate(()=>({pb:!!document.querySelector('.moncard.pb'),name:document.querySelector('.moncard .mname').textContent,say:document.querySelector('#pbsay').textContent,kind:document.querySelector('.qcard .kind').textContent,hp:NNGame.state().B.monMax}));
  ok(f0.pb&&/Boss nói/i.test(f0.kind)&&f0.hp>=120,'trận boss: '+f0.name+' · '+f0.say+' · '+f0.kind);
  if(t==='hotel')await shot(p,'l_boss_'+t);
  const kinds=await fight(p,'win');
  ok(new Set(kinds.map(k=>k[0])).size===3,'đủ 3 pha: '+[...new Set(kinds.map(k=>k.split(':')[0]))].join(','));
  const w=await p.evaluate(()=>({won:NNGame.pbT().won[0],saved:!!(JSON.parse(localStorage.getItem('it-english-game-v1')).pboss[NNGame.trk]||{won:{}}).won[0],modal:document.querySelector('.modal')&&document.querySelector('.modal').textContent,coins:NNGame.state().G.coins,bossWins:NNGame.state().G.bossWins}));
  ok(w.won&&w.won.n===1&&w.saved&&/BỊ HẠ/.test(w.modal||''),'thắng boss ghi nhận: '+JSON.stringify(w.won)+' · xu '+w.coins+' · bossWins '+w.bossWins);
  if(t==='hotel')await shot(p,'l_win_'+t);
  // 2) thua boss
  await p.evaluate(()=>{document.querySelector('#mback').remove();NNGame.state().G.hp=20;NNGame.pbStart(0);});await p.waitForTimeout(400);
  await fight(p,'lose');
  const l=await p.evaluate(()=>({modal:document.querySelector('.modal')&&document.querySelector('.modal').textContent,retry:!!document.querySelector('#pbRetry'),hp:NNGame.state().G.hp,n:NNGame.pbT().won[0].n}));
  ok(/HẾT HP/.test(l.modal||'')&&l.retry&&l.hp>0&&l.n===1,'thua boss: modal HẾT HP, HP hồi '+l.hp);
  // 3) boss chặng cuối → kết cục
  await p.evaluate(()=>{document.querySelector('#mback').remove();const G=NNGame.state().G;G.cur=window.DATA.days.length+1;G.hp=G.maxHp;NNGame.pbStart(window.DATA.phaseTitles.length-1);});await p.waitForTimeout(400);
  const c0=await p.evaluate(()=>NNGame.state().G.coins);
  await fight(p,'win');await p.waitForTimeout(300);
  const e=await p.evaluate(()=>({txt:document.querySelector('.modal')&&document.querySelector('.modal').textContent,end:NNGame.pbT().end,coins:NNGame.state().G.coins,inf:!!document.querySelector('#pbInf')}));
  ok(/KẾT CỤC/.test(e.txt||'')&&/Bạn đã trở thành/.test(e.txt)&&e.end&&e.inf&&e.coins-c0>=1000,'màn kết cục: '+((e.txt||'').match(/Bạn đã trở thành[^.]*?(?=Mochi)/)||[''])[0]+' · +'+(e.coins-c0)+' xu');
  await shot(p,'l_end_'+t);
  // 3b) thắng lại boss chặng cuối → KHÔNG nhận lại thưởng kết cục (chống cày xu)
  if(t==='hotel'){
    const snap=await p.evaluate(()=>({coins:NNGame.state().G.coins,n:NNGame.pbT().end.n}));
    await p.evaluate(()=>{document.querySelectorAll('.modal,#mback').forEach(x=>x.remove());NNGame.pbStart(window.DATA.phaseTitles.length-1);});await p.waitForTimeout(400);
    await fight(p,'win');await p.waitForTimeout(900);
    const r=await p.evaluate(()=>({coins:NNGame.state().G.coins,n:NNGame.pbT().end.n,txt:document.querySelector('.modal')&&document.querySelector('.modal').textContent}));
    ok(r.n===snap.n&&r.coins-snap.coins<200&&/BỊ HẠ/.test(r.txt||''),'thắng lại boss cuối không cộng thưởng kết cục: +'+(r.coins-snap.coins)+' xu, end.n '+r.n);
    await p.evaluate(()=>{document.querySelectorAll('.modal,#mback').forEach(x=>x.remove());NNGame.pbEnding();});await p.waitForTimeout(300);}
  // 4) vô tận
  await p.click('#pbInf');await p.waitForTimeout(400);
  const inf=await p.evaluate(()=>{const B=NNGame.state().B;return B&&{endless:B.boss.endless,lvl:B.boss.lvl,hp:B.monMax,lbl:document.querySelector('#pbstage').textContent};});
  ok(inf&&inf.endless&&inf.lvl===1&&inf.hp>120,'vô tận: '+JSON.stringify(inf));
  await fight(p,'win');
  const inf2=await p.evaluate(()=>({best:NNGame.pbT().infBest,next:!!document.querySelector('#pbNext')}));
  ok(inf2.best===1&&inf2.next,'vô tận thắng cấp 1 → kỷ lục '+inf2.best);
  // 5) hồ sơ + danh sách boss
  await p.evaluate(()=>[...document.querySelectorAll('.modal .btn')].find(x=>x.textContent==='Dừng').click());await p.waitForTimeout(300);await p.click('.tab:nth-child(4)');await p.waitForTimeout(300);
  const row=await p.evaluate(()=>{const r=[...document.querySelectorAll('.srow')].find(x=>/Boss chặng/.test(x.textContent));if(r)r.click();return r&&r.textContent;});
  await p.waitForTimeout(250);const rows=await p.evaluate(()=>document.querySelectorAll('.pbrow').length);
  ok(!!row&&rows>0,'hồ sơ › '+(row||'').trim()+' · '+rows+' boss');
  if(t==='hotel')await shot(p,'l_sheet_'+t);
  report(p,'L '+t);if(p.errs.length)fail++;await p.close();
}
// 6) dữ liệu game cũ (không có pboss / pboss sai kiểu) + ngành lạ → fallback
for(const [label,g,track] of [['cũ không pboss',{seenTut:true,cur:3,lv:4,xp:10,coins:50,cleared:{1:{v:3,p:2,l:1}},idle:{last:Date.now()}},'office'],['pboss sai kiểu',{seenTut:true,cur:11,pboss:[1,2],idle:{last:Date.now()}},'sales'],['track lạ (loader → it)',{seenTut:true,cur:11,idle:{last:Date.now()}},'zzz']]){
  const p=await page(b,{store:baseStore({cfg:{level:'A2',autoSpeak:false,track,trackChosen:true}}),game:g});
  await p.goto(BASE+'game/index.html');await p.waitForTimeout(700);
  const s=await p.evaluate(()=>({trk:NNGame.trk,node:document.querySelector('#pbNode')&&document.querySelector('#pbNode').className,pb:JSON.stringify(NNGame.pbT()),def:NNGame.pbDef(3).n,qs:[0,1,2].map(i=>NNGame.pbQs(0,i).length)}));
  ok(s.node&&s.qs.every(n=>n>0),label+': '+JSON.stringify(s));
  report(p,'L '+label);if(p.errs.length)fail++;await p.close();
}
// 7) bảng boss đủ 14 id + fallback cho ngành lạ
{const p=await page(b,{store:baseStore({cfg:{level:'A2',autoSpeak:false,track:'office',trackChosen:true}}),game:gstore()});
  await p.goto(BASE+'game/index.html');await p.waitForTimeout(600);
  const r=await p.evaluate(()=>{const ids=['office','it','hotel','sales','factory','logistics','finance','marketing','health','construction','aviation','education','legal','custom'];
    return {miss:ids.filter(i=>!(NNGame.PBOSS[i]&&NNGame.PBOSS[i].length>=3&&NNGame.PBOSS[i].every(x=>x.n&&x.e&&x.hi&&x.ko))),endMiss:ids.filter(i=>!/./.test(NNGame.pbEndText(i)[0])),lax:NNGame.pbDefs('zzz')[0].n,laxEnd:NNGame.pbEndText('zzz')[0]};});
  ok(!r.miss.length&&!r.endMiss.length&&r.lax,'14 id đủ boss + kết cục; ngành lạ → '+r.lax+' / '+r.laxEnd);
  report(p,'L tables');if(p.errs.length)fail++;await p.close();}
await b.close();
console.log(fail?'L FAILED '+fail:'L ALL OK');process.exit(fail?1:0);
