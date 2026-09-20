import {launch,page,BASE,baseStore,shot,report} from './lib.mjs';
const d=new Date(),dow=(d.getDay()+6)%7,mon=new Date(d);mon.setDate(d.getDate()-dow);const wk=mon.toISOString().slice(0,10);
const b=await launch();
const convos=[];for(let i=0;i<6;i++){const dt=new Date(Date.now()-(10-i)*864e5).toISOString().slice(0,10);convos.push({id:1e12+i,name:'c'+i,scKey:'x',scLabel:'x',score:40+i*9,fixCount:6-i,userTurns:4,turns:[],date:dt});}
const game={name:'Dev',lv:3,xp:0,hp:100,maxHp:100,coins:10,cleared:{},badges:{},cur:5,ch:0,items:{},up:{},idle:{last:Date.now(),bugs:0},daily:{},seenTut:true,talk:{equipped:[],endings:{},log:[{id:2e12,date:new Date().toISOString().slice(0,10),sc:'x',score:75,fixCount:2,userTurns:5,turns:[{role:'assistant',content:'Hi!\nFIX: OK'},{role:'user',content:'hello'}]}]}};
let p=await page(b,{store:baseStore({stats:{placed:true,sundayShown:wk},convos,srs:{deploy:{ease:1.8,reps:2,due:0}}}),game,
  aiJson:`if(/standup/.test(prompt))return {score:7,polished:"Yesterday I fixed the login bug. Today I will write tests. No blockers.",fixes:[{wrong:"I fix",right:"I fixed",note:"quá khứ dùng V-ed"}],tip:"Nói chậm, rõ 3 ý."};
          if(/SAY this Vietnamese/.test(prompt))return {score:8,note:"Tự nhiên, chỉ thiếu 'please'.",natural:["Could you take a look at my PR, please?","Can you review my PR?"]};return [];`});
await p.goto(BASE+'index.html');await p.waitForTimeout(700);
await shot(p,'b_home');
// N1
await p.evaluate(()=>standupStart());await p.waitForTimeout(300);await shot(p,'b_su1');
await p.fill('#suText','yesterday I fix the login bug today I write test no blocker');
await p.evaluate(()=>suGrade());await p.waitForTimeout(500);await shot(p,'b_su2');
const su=await p.evaluate(()=>({saved:(store.standups||[]).length,score:store.standups[0].score,txt:document.querySelector('#main').innerText.slice(0,400),sh:document.documentElement.scrollHeight}));
console.log('N1',JSON.stringify(su).slice(0,300));
await p.evaluate(()=>go('home'));await p.waitForTimeout(300);
console.log('home standup card:',await p.evaluate(()=>[...document.querySelectorAll('#main .card')].map(c=>c.innerText).find(t=>/Standup/.test(t))));
// N3
await p.evaluate(()=>revStart());await p.waitForTimeout(300);await shot(p,'b_rv1');
await p.evaluate(()=>{rv.typing=true;vReverse();});await p.waitForTimeout(200);
await p.fill('#rvIn','please check my PR');await p.keyboard.press('Enter');await p.waitForTimeout(500);await shot(p,'b_rv2');
console.log('N3',await p.evaluate(()=>JSON.stringify({i:rv.i,res:rv.res})));
for(let k=0;k<9;k++){await p.evaluate(()=>{rv.i++;rv.res=null;});}
await p.evaluate(()=>{rv.i=rv.q.length;vReverse();});await p.waitForTimeout(200);await shot(p,'b_rv3');
// L3 + G2
await p.evaluate(()=>go('progress'));await p.waitForTimeout(400);await shot(p,'b_prog');
console.log('L3/G2',await p.evaluate(()=>JSON.stringify({convos:store.convos.length,game:store.convos.filter(c=>c.scKey==='game').length,svg:!!document.querySelector('#main svg polyline')})));
await p.evaluate(()=>go('practice'));await p.waitForTimeout(300);await shot(p,'b_practice');
report(p,'app B');
// G1 game weak words
const pg=await page(b,{store:baseStore({srs:{'deploy':{ease:1.8,reps:2,due:0},'bug':{ease:2.5,reps:0,due:0}}}),game});
await pg.goto(BASE+'game/index.html');await pg.waitForTimeout(700);
console.log('weak',await pg.evaluate(()=>{const r=[];for(const s of document.scripts){}return 'ok'}));
await pg.evaluate(()=>{document.querySelector('.mback')?.remove();const q=[...document.querySelectorAll('.qchip')][0];q&&q.click();});await pg.waitForTimeout(600);
await pg.evaluate(()=>{const b=[...document.querySelectorAll('.mback .quest,.mback .btn')].find(x=>/Từ vựng|Bug/.test(x.textContent));b&&b.click();});await pg.waitForTimeout(600);
console.log('G1 first q kind:',await pg.evaluate(()=>document.querySelector('.qcard .kind')?.textContent+' | '+document.querySelector('.qcard .q')?.textContent));
await shot(pg,'b_game_weak');
report(pg,'game B');
// T3 showcase
const ps=await page(b,{w:390,h:844});await ps.goto(BASE+'gioi-thieu.html');await ps.waitForTimeout(1200);
console.log('T3 imgs loaded',await ps.evaluate(()=>{const im=[...document.images];return im.filter(i=>i.complete&&i.naturalWidth>0).length+'/'+im.length}));
await ps.evaluate(()=>window.scrollTo(0,3000));await ps.waitForTimeout(1200);
console.log('T3 after scroll',await ps.evaluate(()=>{const im=[...document.images];return im.filter(i=>i.complete&&i.naturalWidth>0).length+'/'+im.length}));
report(ps,'showcase');
await b.close();
