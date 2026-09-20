import {launch,page,BASE,baseStore,shot,report} from './lib.mjs';
const d=new Date(),dow=(d.getDay()+6)%7,mon=new Date(d);mon.setDate(d.getDate()-dow);const wk=mon.toISOString().slice(0,10);
const b=await launch();const p=await page(b,{store:baseStore({stats:{placed:true,sundayShown:wk},cfg:{level:'A2',autoSpeak:false,role:'designer'}})});
await p.goto(BASE+'index.html');await p.waitForTimeout(500);
const info=await p.evaluate(()=>({dl:DIALOGUES.length,ls:DICTATION.length,pi:DICTATION.findIndex(x=>x.p),roles:Object.keys(ROLE_PACKS)}));
console.log('data',JSON.stringify(info));
await p.evaluate(i=>{lMode='dictation';lIdx=i;lChecked=false;go('listen');},info.pi);await p.waitForTimeout(300);
console.log('blanks',await p.evaluate(()=>document.querySelectorAll('.blankin').length));await shot(p,'f_pass1');
await p.evaluate(()=>{const L=DICTATION[lIdx];const ins=[...document.querySelectorAll('.blankin')];ins.forEach((x,k)=>{x.value=k===0?L.s[L.blank[0]].replace(/[.,]+$/,''):'wrong';x.dispatchEvent(new Event('input'));});});
await p.evaluate(()=>lCheckPassage());await p.waitForTimeout(200);await shot(p,'f_pass2');
console.log('result',await p.evaluate(()=>document.querySelector('#main .card .row b')?.textContent));
await p.evaluate(()=>roleQuizStart());await p.waitForTimeout(300);await shot(p,'f_role');
console.log('role quiz first',await p.evaluate(()=>document.querySelector('.bubble.them')?.textContent));
// day view: good answer position varies
const pos=await p.evaluate(()=>{const r=[0,0,0];DIALOGUES.forEach(d=>r[d.opts.findIndex(o=>o.good)]++);return r;});console.log('good pos',pos);
report(p,'F');
const pg=await page(b,{store:baseStore({days:{cur:15,done:{}}})});await pg.goto(BASE+'game/index.html');await pg.waitForTimeout(600);
report(pg,'game F');await b.close();
