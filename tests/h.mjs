// v3.1: báo lỗi nội dung, luyện nói rảnh tay (giả SpeechRecognition), gói "Nghề của tôi" do AI tạo, ảnh → bài học, 4 gói ngành mới, game đổi ngành
import {launch,page,BASE,baseStore,shot,report} from './lib.mjs';
const d=new Date(),dow=(d.getDay()+6)%7,mon=new Date(d);mon.setDate(d.getDate()-dow);const wk=mon.toISOString().slice(0,10);
const V=(t,vi)=>({t,ipa:'/x/',pos:'n',vi,ex:'The <b>'+t+'</b> is here.',exVi:'Ví dụ.'});
const aiJson=`
if(/Design a short workplace-English course/.test(prompt))return {label:'Dược sĩ bệnh viện',short:'Dược sĩ',persona:'a Vietnamese hospital pharmacist',context:'hospital pharmacy',phases:['Tư vấn thuốc','Kiểm kho thuốc','Gọi điện cho bác sĩ'],ai:[{k:'patient',l:'Bệnh nhân hỏi thuốc',s:'You are a foreign patient asking about your medicine.'}],rev:[['Thuốc này uống sau ăn.','Take this after meals.']]};
if(/Topic of this lesson/.test(prompt)){var v=[];for(var i=0;i<10;i++)v.push({t:'term'+i+'x',ipa:'/t/',pos:'n',vi:'từ '+i,ex:'This is term'+i+'x today.',exVi:'Đây.'});
  var dl=[];for(var k=0;k<5;k++)dl.push({them:'Question '+k+'?',opts:[{t:'Good answer '+k+'.',good:true,fb:'Tốt'},{t:'Bad '+k,good:false,fb:'Sai'},{t:'Worse '+k,good:false,fb:'Sai'}]});
  return {vocab:v,phrases:[{en:'Please take one tablet.',vi:'Uống một viên.'},{en:'Any allergies?',vi:'Có dị ứng không?'},{en:'I will check.',vi:'Tôi kiểm tra.'}],dialogues:dl,
   listen:[{s:'Please take the tablet after lunch',blanks:['tablet'],hint:'uống thuốc'},{s:'The pharmacy opens at eight',blanks:['pharmacy','eight'],hint:'giờ mở'},{s:'Good morning. Your medicine is ready. Please sign here.',blanks:['medicine','ready','sign'],hint:'đoạn'}]};}
if(/This photo shows/.test(prompt))return {kind:'Email đặt phòng',summary:'Khách đặt 2 phòng đôi từ 12/10.',vocab:[{t:'double room',ipa:'/ˌdʌbl ˈruːm/',pos:'n',vi:'phòng đôi',ex:'Two <b>double rooms</b>, please.',exVi:'Hai phòng đôi.'}],replies:[{en:'Thank you for your booking.',vi:'Cảm ơn anh đã đặt phòng.'}],questions:[{q:'How many rooms?',o:['One','Two','Three'],a:1}],scenario:{label:'Gọi xác nhận đặt phòng',prompt:'You are the guest who sent the email.'}};
return [];`;
const b=await launch();
// 1) 4 gói mới nạp được
for(const t of ['logistics','finance','marketing','health']){
  const q=await page(b,{store:baseStore({stats:{placed:true,sundayShown:wk},cfg:{level:'A2',autoSpeak:false,track:t,trackChosen:true}})});
  await q.goto(BASE+'index.html');await q.waitForTimeout(600);
  const info=await q.evaluate(()=>({track:TRACK,pack:PACK&&PACK.id,days:DAYS.length,rep:REPORT.title,them:themVi(),roles:Object.keys(ROLE_PACKS).length}));
  for(const fn of [()=>go('practice'),()=>standupStart(),()=>roleQuizStart(),()=>readingStart(),()=>revStart(),()=>go('talk')])await q.evaluate(fn);
  console.log('pack',JSON.stringify(info));report(q,'H '+t);await q.close();
}
// 2) báo lỗi nội dung
let p=await page(b,{aiJson,store:baseStore({stats:{placed:true,sundayShown:wk},cfg:{level:'A2',autoSpeak:false,track:'hotel',trackChosen:true}})});
await p.goto(BASE+'index.html');await p.waitForTimeout(600);
await p.evaluate(()=>openDay(3));await p.waitForTimeout(200);
console.log('flag buttons on day',await p.evaluate(()=>document.querySelectorAll('#main .flagbtn').length));
await p.evaluate(()=>document.querySelector('#main .flagbtn').click());await p.waitForTimeout(200);await shot(p,'h_report1');
await p.evaluate(()=>{[...document.querySelectorAll('.modal .chip')].find(x=>/IPA/.test(x.textContent)).click();document.querySelector('.modal textarea').value='IPA nên là /rɪˈzɜːv/';[...document.querySelectorAll('.modal .btn')].find(x=>/Lưu báo lỗi/.test(x.textContent)).click();});
await p.waitForTimeout(200);await shot(p,'h_report2');
console.log('report saved',await p.evaluate(()=>({n:store.reports.length,gh:/github\.com\/hunglv201\/it-english-app\/issues\/new\?/.test(document.querySelector('.modal a.btn').href)})));
await p.evaluate(()=>{closeModal();go('reports');});await p.waitForTimeout(200);await shot(p,'h_reports');report(p,'H report');
// 3) rảnh tay với SpeechRecognition giả
const q=await page(b,{store:baseStore({stats:{placed:true,sundayShown:wk},cfg:{level:'A2',autoSpeak:false,track:'office',trackChosen:true}})});
await q.addInitScript(()=>{window.__srSay=null;window.SpeechRecognition=function(){var self=this;this.start=function(){setTimeout(function(){var t=window.__srSay?window.__srSay():'';if(t&&self.onresult)self.onresult({resultIndex:0,results:[Object.assign([{transcript:t}],{isFinal:true})]});setTimeout(function(){self.onend&&self.onend();},20);},60);};this.stop=function(){};this.abort=function(){};};});
await q.goto(BASE+'index.html');await q.waitForTimeout(600);
await q.evaluate(()=>{window.__srSay=function(){var it=hf.list[hf.i];return it?it.a:'';};hfStart();hf.n=5;});await q.waitForTimeout(200);await shot(q,'h_hf0');
await q.evaluate(()=>hfGo());await q.waitForTimeout(400);await shot(q,'h_hf1');
for(let i=0;i<40;i++){await q.waitForTimeout(250);if(await q.evaluate(()=>hf.st==='done'))break;}
console.log('handsfree',JSON.stringify(await q.evaluate(()=>({st:hf.st,res:hf.res,i:hf.i}))));await shot(q,'h_hf2');
await q.evaluate(()=>{hf.list=[];hf.st='';hf.mode='reply';window.__srSay=function(){return 'um no';};vHandsfree();hfGo();});
for(let i=0;i<60;i++){await q.waitForTimeout(250);if(await q.evaluate(()=>hf.i>=1))break;}
console.log('reply wrong→ psrs',await q.evaluate(()=>({i:hf.i,res:hf.res[0],due:Object.keys(store.psrs||{}).length})));
await q.evaluate(()=>hfStop(true));report(q,'H handsfree');
// 4) Nghề của tôi (AI tạo gói)
const r=await page(b,{aiJson,store:baseStore({stats:{placed:true,sundayShown:wk},cfg:{level:'A2',autoSpeak:false,track:'office',trackChosen:true,jd:'Mình là dược sĩ ở bệnh viện quốc tế, tư vấn thuốc cho bệnh nhân nước ngoài.'}})});
await r.goto(BASE+'index.html');await r.waitForTimeout(600);await r.evaluate(()=>go('jd'));await r.waitForTimeout(200);await shot(r,'h_cp0');
await Promise.all([r.waitForNavigation({timeout:15000}),r.evaluate(()=>cpGenerate())]);await r.waitForTimeout(800);
console.log('custom',JSON.stringify(await r.evaluate(()=>({track:TRACK,label:TRK.label,days:DAYS.length,ph0:D.phaseTitles[0],ph3:D.phaseTitles[3],who:who(),v0:VOCAB[DAYS[0].v[0]].t,li:DICTATION[DAYS[0].li].blank.length,ai:AI_SCENARIOS[0].l,chip:document.querySelector('#trackChip').textContent}))));
await r.evaluate(()=>openDay(1));await r.waitForTimeout(200);await shot(r,'h_cp_day');
await r.evaluate(()=>go('jd'));await r.waitForTimeout(200);await shot(r,'h_cp_card');report(r,'H custom');
const rg=await r.context().newPage();rg.errs=[];rg.on('pageerror',e=>rg.errs.push(e.message));await rg.goto(BASE+'game/index.html');await rg.waitForTimeout(700);
console.log('game custom',await rg.evaluate(()=>({pack:(window.PACK||{}).id,days:window.DATA.days.length})),rg.errs.length?rg.errs:'ok');
// 5) Ảnh → bài học
const s=await page(b,{aiJson,store:baseStore({stats:{placed:true,sundayShown:wk},cfg:{level:'A2',autoSpeak:false,track:'hotel',trackChosen:true}})});
await s.addInitScript(()=>{const o=window.claude&&window.claude.use;if(o)window.claude={use:async n=>{const sp=await o(n);if(sp&&!sp.limits)sp.limits=async()=>({maxPromptBytes:1e6,images:{maxCount:5,maxInputBytes:5e6,mediaTypes:['image/jpeg']}});return sp;}};});
await s.goto(BASE+'index.html');await s.waitForTimeout(600);await s.evaluate(()=>go('photo'));await s.waitForTimeout(200);await shot(s,'h_ph0');
const png=Buffer.from('iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg==','base64');
await s.setInputFiles('#phFile',{name:'doc.png',mimeType:'image/png',buffer:png});await s.waitForTimeout(500);
await s.evaluate(()=>phGo());await s.waitForTimeout(500);await shot(s,'h_ph1');
console.log('photo',JSON.stringify(await s.evaluate(()=>({kind:ph1.res&&ph1.res.kind,cards:document.querySelectorAll('#main .card').length,calls:window.__calls.filter(c=>c.opts&&c.opts.images).length}))));
report(s,'H photo');
// 6) game: đổi ngành trong Hồ sơ
const g=await page(b,{store:baseStore({cfg:{track:'office'}})});await g.goto(BASE+'game/index.html');await g.waitForTimeout(800);
console.log('game pack',await g.evaluate(()=>(window.PACK||{}).id));report(g,'H game');
await b.close();
