import {launch,page,BASE,baseStore,shot,report} from './lib.mjs';
const d=new Date(),dow=(d.getDay()+6)%7,mon=new Date(d);mon.setDate(d.getDate()-dow);const wk=mon.toISOString().slice(0,10);
const b=await launch();
// 1. T1 chat XSS + myVocab migration
const evil='<img src=x onerror="window.__pwn=1">';
let p=await page(b,{store:baseStore({stats:{placed:true,sundayShown:wk},myVocab:[{t:'<script>x</script>deploy',ipa:'',pos:'n',vi:'triển khai<img src=x onerror="window.__pwn=2">',ex:'We <b>deploy</b> <i>now</i><img src=x onerror="window.__pwn=3">',exVi:'',custom:true}]}),
  ai:`return 'Hi '+${JSON.stringify(evil)}+' how are you?\\nFIX: OK';`,
  aiJson:`return [{en:'Try ${evil.replace(/"/g,'\\"')}',vi:'x'}];`});
await p.goto(BASE+'index.html');await p.waitForTimeout(800);
const mv=await p.evaluate(()=>JSON.parse(localStorage.getItem('it-english-v1')).myVocab[0]);
console.log('myVocab cleaned:',JSON.stringify(mv));
await p.evaluate(()=>{vMode='list';vTopic='mine';go('vocab');});await p.waitForTimeout(400);
await p.evaluate(()=>{go('talk');aiUseCustom('Test','A colleague asks about deploy.');});await p.waitForTimeout(900);
const talkState=await p.evaluate(()=>({hasInput:!!document.querySelector('#aiInput'),txt:document.querySelector('#main').innerText.slice(0,200)}));
console.log('talk',JSON.stringify(talkState));
await shot(p,'a_talk');
if(talkState.hasInput){
  await p.evaluate(async()=>{await aiStart?.();});await p.waitForTimeout(600);
  await p.fill('#aiInput','I deploy yesterday');await p.evaluate(()=>aiSend());await p.waitForTimeout(800);
}
const pwn=await p.evaluate(()=>({pwn:window.__pwn||0,bubbles:[...document.querySelectorAll('.bubble')].map(x=>x.textContent).slice(-3)}));
console.log('XSS check',JSON.stringify(pwn));
await shot(p,'a_chat');
report(p,'T1');
// 2. K1 backup roundtrip
const bk=await p.evaluate(()=>JSON.stringify(backupData()));
await p.evaluate(()=>{localStorage.setItem('it-english-v1',JSON.stringify({days:{cur:1,done:{}},stats:{placed:true}}));});
await p.evaluate((t)=>applyBackup(t),bk);await p.waitForTimeout(1500);
const after=await p.evaluate(()=>JSON.parse(localStorage.getItem('it-english-v1')).days);
console.log('restored days',JSON.stringify(after));
const bad=await p.evaluate(()=>applyBackup('{"foo":1}'));console.log('bad backup rejected',bad===false);
await p.evaluate(()=>go('me'));await p.waitForTimeout(300);await shot(p,'a_me');
await p.evaluate(()=>importBackup());await p.waitForTimeout(300);await shot(p,'a_import');
report(p,'K1');
await b.close();
