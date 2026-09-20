import {launch,page,BASE,baseStore,shot,report} from './lib.mjs';
const d=new Date(),dow=(d.getDay()+6)%7,mon=new Date(d);mon.setDate(d.getDate()-dow);const wk=mon.toISOString().slice(0,10);
const tomorrow=new Date(Date.now()+864e5).toISOString().slice(0,10);
const b=await launch();
const aiJson=`
if(/described their job/.test(prompt))return {role:'qa',domain:'ticketing platform QA',phases:[3,7,1,20,30,12],why:'Bạn làm QA nên ưu tiên chặng bug & test.',scenarios:[{label:'Báo bug cho dev Nhật',prompt:'You are a Japanese developer; I report a bug.'},{label:'Họp test plan',prompt:'You are QA lead.'}]};
if(/Create practice/.test(prompt))return {sentences:[{en:'Thanks, I will check it today.',vi:'Cảm ơn, hôm nay mình sẽ kiểm tra.'},{en:'Could you share the logs?',vi:'Bạn gửi log được không?'}],scenario:{label:'Trả lời PR',prompt:'You are the PR author.'}};
if(/mispronounced/.test(prompt))return {words:[{w:'deploy',ipa:'/dɪˈplɔɪ/',tip:'Nhấn âm tiết 2'}],summary:'Tốt lắm!'};
if(/asks:/.test(prompt))return {answer:'Blocker là việc chặn tiến độ.',example:'This bug is a blocker for the release.',term:'blocker',term_vi:'việc chặn tiến độ'};
return [];`;
let p=await page(b,{store:baseStore({stats:{placed:true,sundayShown:wk},cfg:{level:'A2',autoSpeak:false,showJa:true},events:[{id:1,date:tomorrow,type:'client',note:'demo thanh toán'}],
  psrs:{'Could you review my PR?':{ease:1.9,int:0,reps:0,due:0,vi:'Bạn review PR giúp mình?',src:'fix',n:2}}}),aiJson,ai:`return 'OK!\\nFIX: OK';`});
await p.goto(BASE+'index.html');await p.waitForTimeout(700);await shot(p,'c_home');
console.log('home event card:',await p.evaluate(()=>!!document.querySelector('#askBtn')+' | '+([...document.querySelectorAll('#main .card')].map(c=>c.innerText).find(t=>/Ngày mai/.test(t))||'none').replace(/\n/g,' ')));
// N4 ja
await p.evaluate(()=>{vMode='list';vTopic='all';go('vocab');});await p.waitForTimeout(400);
console.log('N4 ja rows',await p.evaluate(()=>document.querySelectorAll('#main .ja').length));await shot(p,'c_ja');
// practice hub
await p.evaluate(()=>go('practice'));await p.waitForTimeout(300);await shot(p,'c_practice');
// L1 sreview
await p.evaluate(()=>sreviewStart());await p.waitForTimeout(300);await shot(p,'c_sr1');
await p.evaluate(()=>{sr.show=true;vSReview();});await p.waitForTimeout(200);await shot(p,'c_sr2');
await p.evaluate(()=>{psrsGrade(sr.q[0].en,2);sr.i++;vSReview();});
console.log('L1 due after',await p.evaluate(()=>psrsDue().length));
// C3 role quiz: set role qa
await p.evaluate(()=>{store.cfg.role='qa';save(store);roleQuizStart();});await p.waitForTimeout(300);await shot(p,'c_role');
await p.evaluate(()=>{const o=[...document.querySelectorAll('.opt')];o[0].click();});await p.waitForTimeout(200);await shot(p,'c_role2');
// C1 JD
await p.evaluate(()=>go('jd'));await p.waitForTimeout(200);await p.fill('#jdIn','I am a QA tester for a Japanese ticketing system, I report bugs and join test planning.');
await p.evaluate(()=>jdGo());await p.waitForTimeout(500);await shot(p,'c_jd');
console.log('C1',await p.evaluate(()=>JSON.stringify({role:store.cfg.role,focus:store.cfg.focus,sc:(store.cfg.jdScenarios||[]).length})));
await p.evaluate(()=>go('roadmap'));await p.waitForTimeout(300);await shot(p,'c_road');
await p.evaluate(()=>go('talk'));await p.waitForTimeout(300);
console.log('chips',await p.evaluate(()=>[...document.querySelectorAll('.chip')].slice(0,6).map(c=>c.textContent).join(' | ')));await shot(p,'c_talk');
// N5 events
await p.evaluate(()=>go('events'));await p.waitForTimeout(200);await shot(p,'c_events');
// N2 podcast
await p.evaluate(()=>podcastStart());await p.waitForTimeout(300);await shot(p,'c_pod1');
await p.evaluate(()=>{pc.i=pc.items.length;pcPlay();});await p.waitForTimeout(300);await shot(p,'c_pod2');
// N6 quick ask
await p.evaluate(()=>quickAsk());await p.waitForTimeout(200);await p.fill('.modal textarea','blocker vs impediment?');await p.evaluate(()=>[...document.querySelectorAll('.modal .btn')].find(x=>x.textContent==='Hỏi').click());await p.waitForTimeout(500);await shot(p,'c_ask');
await p.evaluate(()=>[...document.querySelectorAll('.modal .btn')].find(x=>/Lưu/.test(x.textContent)).click());
console.log('N6 saved',await p.evaluate(()=>store.myVocab.map(w=>w.t+':'+w.ex).join(',')));
await p.evaluate(()=>closeModal());
// N7 share
await p.evaluate(()=>shareCard());await p.waitForTimeout(800);await shot(p,'c_share');await p.evaluate(()=>closeModal());
// N8 cache + rules
console.log('N8 rules:',await p.evaluate(()=>ruleCheck('yesterday I fix the bug and he have informations, i am agree')));
const n1=await p.evaluate(async()=>{const sp=await aiInit();window.__calls=[];await sp.json('same prompt X');await sp.json('same prompt X');return window.__calls.filter(c=>c.json).length;});
console.log('N8 cache: calls for 2 identical json =',n1);
// C2
await p.evaluate(()=>{exSrc='Please review the PR before Friday, and check the logs for the timeout issue.';exResult=[{t:'timeout',ipa:'',pos:'n',vi:'hết thời gian',ex:'<b>timeout</b>',exVi:''}];vExtract();});await p.waitForTimeout(200);
await p.evaluate(()=>[...document.querySelectorAll('.btn')].find(x=>/Tạo 2 câu/.test(x.textContent)).click());await p.waitForTimeout(400);await shot(p,'c_extract');
console.log('C2',await p.evaluate(()=>[...document.querySelectorAll('.phrase .en')].map(e=>e.textContent).join(' / ')));
// L2 in phrase practice
await p.evaluate(()=>{startRandom(3);rnShow=true;rnApply('could you');});await p.waitForTimeout(300);
await p.evaluate(()=>{const b=[...document.querySelectorAll('.btn')].find(x=>/AI phân tích/.test(x.textContent));b&&b.click();});await p.waitForTimeout(400);await shot(p,'c_l2');
console.log('L2 psrs size',await p.evaluate(()=>Object.keys(store.psrs).length));
report(p,'app C');
// game role + ja
const pg=await page(b,{store:baseStore({cfg:{role:'devops',showJa:true}})});
await pg.goto(BASE+'game/index.html');await pg.waitForTimeout(600);
console.log('game talkPool role',await pg.evaluate(()=>{return 'n/a'}));
await pg.evaluate(()=>{document.querySelector('.mback')?.remove();[...document.querySelectorAll('.tab')].find(x=>/Nói/.test(x.textContent)).click();});await pg.waitForTimeout(300);
await pg.evaluate(()=>[...document.querySelectorAll('.tmode')].find(x=>/Chuyện văn phòng/.test(x.textContent)).click());await pg.waitForTimeout(2500);
console.log('story first line:',await pg.evaluate(()=>document.querySelector('#vtxt')?.textContent));
await shot(pg,'c_game_story');
report(pg,'game C');
await b.close();
