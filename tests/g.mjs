// v3.0: đa ngành — làm quen (bỏ qua → Công sở), chọn ngành, mọi màn chạy được với từng gói, tiến độ riêng từng gói, game theo gói
import {launch,page,BASE,baseStore,shot,report} from './lib.mjs';
const d=new Date(),dow=(d.getDay()+6)%7,mon=new Date(d);mon.setDate(d.getDate()-dow);const wk=mon.toISOString().slice(0,10);
const aiJson=`if(/Reply ONLY JSON \\{"track"/.test(prompt))return {track:'hotel',persona:'a Vietnamese hotel receptionist',role:'reception',domain:'4-star beach hotel',phases:[0,2],why:'Bạn làm lễ tân.',scenarios:[{label:'Khách đến sớm',prompt:'You are a guest arriving at 8 a.m.'}],words:[{t:'early check-in',ipa:'',vi:'nhận phòng sớm',ex:'Can I get an early check-in?'}]};
 if(/"score"/.test(prompt))return {score:7,polished:'In my shift ten guests checked in.',fixes:[],tip:'Tốt'};return [];`;
const b=await launch();
// 1) người mới: làm quen hiện, bỏ qua → Công sở chung
let p=await page(b,{aiJson});await p.goto(BASE+'index.html');await p.waitForTimeout(1200);
const onb=await p.evaluate(()=>({modal:!!document.querySelector('.modal.onb'),tiles:document.querySelectorAll('.trtile').length,track:TRACK}));
console.log('onboarding',JSON.stringify(onb));await shot(p,'g_onb1');
await p.evaluate(()=>[...document.querySelectorAll('.modal button')].find(x=>/Bỏ qua/.test(x.textContent)).click());await p.waitForTimeout(400);
console.log('after skip',JSON.stringify(await p.evaluate(()=>({track:TRACK,cfg:store.cfg.track,chosen:store.cfg.trackChosen,placed:store.stats.placed,modal:!!document.querySelector('.modal'),chip:document.querySelector('#trackChip').textContent,days:DAYS.length}))));
await shot(p,'g_home_office');report(p,'G skip');
// 2) người mới: chọn Khách sạn → vai → trình độ → tải lại gói hotel
p=await page(b,{aiJson});await p.goto(BASE+'index.html');await p.waitForTimeout(1200);
await p.evaluate(()=>[...document.querySelectorAll('.trtile')].find(x=>/Khách sạn/.test(x.textContent)).click());await p.waitForTimeout(300);await shot(p,'g_onb2');
await p.evaluate(()=>[...document.querySelectorAll('.modal .chip')].find(x=>/Lễ tân/.test(x.textContent)).click());await p.waitForTimeout(300);await shot(p,'g_onb3');
await Promise.all([p.waitForNavigation(),p.evaluate(()=>[...document.querySelectorAll('.modal button')].find(x=>/Biết cơ bản/.test(x.textContent)).click())]);await p.waitForTimeout(900);
console.log('after pick',JSON.stringify(await p.evaluate(()=>({track:TRACK,role:store.cfg.role,cur:store.days.cur,level:store.cfg.level,pack:PACK&&PACK.id,modal:!!document.querySelector('.modal')}))));
await shot(p,'g_home_hotel');report(p,'G pick');
// 3) mọi màn với từng gói
for(const t of ['office','hotel','sales','factory','it']){
  const q=await page(b,{aiJson,store:baseStore({stats:{placed:true,sundayShown:wk},cfg:{level:'A2',autoSpeak:false,track:t,trackChosen:true}})});
  await q.goto(BASE+'index.html');await q.waitForTimeout(700);
  const steps=[['home',()=>go('home')],['practice',()=>go('practice')],['vocab',()=>{vMode='card';vTopic='all';go('vocab');}],['phrase',()=>go('phrase')],
    ['rolequiz',()=>roleQuizStart()],['report',()=>standupStart()],['reverse',()=>revStart()],['reading',()=>readingStart()],['podcast',()=>podcastStart()],
    ['events',()=>go('events')],['listen',()=>go('listen')],['talk',()=>go('talk')],['roadmap',()=>go('roadmap')],['jd',()=>go('jd')],['me',()=>go('me')]];
  const bad=[];
  for(const [k,fn] of steps){await q.evaluate(fn);await q.waitForTimeout(150);const n=await q.evaluate(()=>document.querySelector('#main').textContent.length);if(n<30)bad.push(k);}
  await q.evaluate(()=>go('practice'));await q.waitForTimeout(150);await shot(q,'g_practice_'+t);
  await q.evaluate(()=>standupStart());await q.waitForTimeout(150);await shot(q,'g_report_'+t);
  const info=await q.evaluate(()=>({track:TRACK,days:DAYS.length,ph:D.phaseTitles.length,roles:Object.keys(ROLE_PACKS).length,ai:AI_SCENARIOS.length,who:who(),rep:REPORT.title,read:READING.length,ev:EVENT_TYPES.length,phr:PHRASES.length}));
  console.log(t,JSON.stringify(info),'empty:',bad.join(',')||'-');
  // game theo gói
  const g=await q.context().newPage();g.errs=[];g.on('pageerror',e=>g.errs.push(e.message));await g.goto(BASE+'game/index.html');await g.waitForTimeout(800);
  console.log('  game',t,await g.evaluate(()=>({pack:(window.PACK||{}).id||'it',days:window.DATA.days.length,title:document.title})),g.errs.length?g.errs:'ok');
  report(q,'G '+t);
}
// 4) JD gợi ý chuyển ngành + đổi ngành giữ tiến độ riêng
const r=await page(b,{aiJson,store:baseStore({stats:{placed:true,sundayShown:wk},cfg:{level:'A2',autoSpeak:false,track:'office',trackChosen:true}})});
await r.goto(BASE+'index.html');await r.waitForTimeout(600);
await r.evaluate(()=>{go('jd');document.querySelector('#jdIn').value='Mình làm lễ tân khách sạn 4 sao ở Đà Nẵng, check-in cho khách Úc, Hàn.';});await r.evaluate(()=>jdGo());await r.waitForTimeout(400);await shot(r,'g_jd');
console.log('jd',JSON.stringify(await r.evaluate(()=>({persona:store.cfg.persona,words:(store.cfg.jdWords||[]).length,sugBtn:!![...document.querySelectorAll('#main button')].find(x=>/Chuyển sang gói/.test(x.textContent))}))));
const office5=await r.evaluate(()=>store.days.cur);
await Promise.all([r.waitForNavigation(),r.evaluate(()=>[...document.querySelectorAll('#main button')].find(x=>/Chuyển sang gói/.test(x.textContent)).click())]);await r.waitForTimeout(600);
const h=await r.evaluate(()=>({track:TRACK,cur:store.days.cur,stash:Object.keys(store.trackDays||{})}));
await r.evaluate(()=>switchTrack('office'));await r.waitForTimeout(900);
console.log('switch',JSON.stringify(h),'back office cur',await r.evaluate(()=>store.days.cur),'was',office5);
report(r,'G jd');
await b.close();
