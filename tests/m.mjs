// v4.2: lệnh giọng nói khi rảnh tay · Ảnh → bài học lưu thành bộ (mở lại / xoá) · đọc chữ TRÊN MÁY (Tesseract thật, không AI)
import assert from 'assert';
import {launch,page,BASE,baseStore,shot,report} from './lib.mjs';
const d=new Date(),dow=(d.getDay()+6)%7,mon=new Date(d);mon.setDate(d.getDate()-dow);const wk=mon.toISOString().slice(0,10);
const b=await launch();
const SR=()=>{window.__srSay=null;window.__srN=0;window.SpeechRecognition=function(){var self=this;this.start=function(){setTimeout(function(){window.__srN++;var t=window.__srSay?window.__srSay():'';if(t&&self.onresult)self.onresult({resultIndex:0,results:[Object.assign([{transcript:t}],{isFinal:true})]});setTimeout(function(){self.onend&&self.onend();},20);},40);};this.stop=function(){};this.abort=function(){};};};
// 1) lệnh giọng nói
{const q=await page(b,{store:baseStore({stats:{placed:true,sundayShown:wk},cfg:{level:'A2',autoSpeak:false,track:'office',trackChosen:true,rate:0.95}})});
await q.addInitScript(SR);
await q.goto(BASE+'index.html');await q.waitForTimeout(600);
assert.equal(await q.evaluate(()=>hfCmd('Next','Please send the report.')),'next');
assert.equal(await q.evaluate(()=>hfCmd('again please','Thanks.')),'again');
assert.equal(await q.evaluate(()=>hfCmd('stop','Stop.')),'','câu mẫu chính là lệnh → không coi là lệnh');
assert.equal(await q.evaluate(()=>hfCmd('I will send it next week','x')),'','câu dài không phải lệnh');
// câu 1: nói "slower" → chậm lại + nghe lại; rồi "next" → bỏ qua; câu 2: nói đúng; câu 3: "stop"
await q.evaluate(()=>{window.__seq=['slower','next'];window.__srSay=function(){if(window.__seq.length)return window.__seq.shift();var it=hf.list[hf.i];if(hf.i===2)return 'stop';return it?it.a:'';};hfStart();hf.n=5;});
await q.evaluate(()=>hfGo());
for(let i=0;i<60;i++){await q.waitForTimeout(150);if(await q.evaluate(()=>!hf.run&&hf.i>=2))break;}
const hs=await q.evaluate(()=>({i:hf.i,run:hf.run,res:hf.res.slice(),rate:store.cfg.rate,cmd:hf.cmd,hint:/next/.test(document.getElementById('main').textContent)}));
console.log('hf',JSON.stringify(hs));
assert.equal(hs.i,2);assert.equal(hs.run,false);assert.equal(hs.res[0],0);assert.ok(hs.res[1]>=70);assert.equal(hs.rate,0.85);assert.equal(hs.cmd,'stop');
await shot(q,'m_hf');report(q,'M handsfree');await q.close();}
// 2) Ảnh → bài học: lưu bộ, mở lại, xoá
const aiJson=`if(/This photo shows/.test(prompt))return {kind:'Email đặt phòng',summary:'Khách đặt 2 phòng đôi từ 12/10.',vocab:[{t:'double room',ipa:'/ˌdʌbl ˈruːm/',pos:'n',vi:'phòng đôi',ex:'Two <b>double rooms</b>, please.',exVi:'Hai phòng đôi.'}],replies:[{en:'Thank you for your booking.',vi:'Cảm ơn anh đã đặt phòng.'}],questions:[{q:'How many rooms?',o:['One','Two','Three'],a:1}],scenario:{label:'Gọi xác nhận',prompt:'You are the guest.'}};
if(/This text was read by OCR/.test(prompt))return {kind:'Thông báo',summary:'Đọc từ chữ',vocab:[{t:'notice',ipa:'',pos:'n',vi:'thông báo',ex:'<b>notice</b>',exVi:''}],replies:[],questions:[]};return [];`;
const png=Buffer.from('iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg==','base64');
{const s=await page(b,{aiJson,store:baseStore({stats:{placed:true,sundayShown:wk},cfg:{level:'A2',autoSpeak:false,track:'hotel',trackChosen:true}})});
await s.addInitScript(()=>{const o=window.claude&&window.claude.use;if(o)window.claude={use:async n=>{const sp=await o(n);if(sp&&!sp.limits)sp.limits=async()=>({images:{maxCount:5}});return sp;}};});
await s.goto(BASE+'index.html');await s.waitForTimeout(600);await s.evaluate(()=>go('photo'));
await s.setInputFiles('#phFile',{name:'doc.png',mimeType:'image/png',buffer:png});await s.waitForTimeout(400);
await s.evaluate(()=>phGo());await s.waitForTimeout(500);
let st=await s.evaluate(()=>({n:store.photoLessons.length,id:store.photoLessons[0].id,v:store.photoLessons[0].vocab.length,q:store.photoLessons[0].questions.length,sc:!!store.photoLessons[0].scenario,saved:/Bộ đã lưu · 1/.test(document.getElementById('main').textContent)}));
console.log('saved',JSON.stringify(st));assert.equal(st.n,1);assert.equal(st.v,1);assert.equal(st.q,1);assert.ok(st.sc&&st.saved);
await s.evaluate(()=>{ph1.res=null;vPhoto();});await s.evaluate(id=>phOpen(id),st.id);await s.waitForTimeout(150);
assert.ok(await s.evaluate(()=>/double room/.test(document.getElementById('main').textContent)&&/đã lưu bộ/.test(document.getElementById('main').textContent)),'mở lại bộ');
await s.reload();await s.waitForTimeout(600);await s.evaluate(()=>go('photo'));await s.waitForTimeout(150);
assert.ok(await s.evaluate(()=>/Bộ đã lưu · 1/.test(document.getElementById('main').textContent)),'còn sau khi tải lại');
await shot(s,'m_ph_sets');
await s.evaluate(id=>phDel(id),st.id);assert.equal(await s.evaluate(()=>store.photoLessons.length),0);
report(s,'M photo sets');await s.close();}
// 3) Đọc chữ trên máy (không AI): ảnh chữ thật vẽ bằng canvas → Tesseract → tra từ trong gói
{const s=await page(b,{claude:false,store:baseStore({stats:{placed:true,sundayShown:wk},cfg:{level:'A2',autoSpeak:false,track:'hotel',trackChosen:true}})});
await s.goto(BASE+'index.html');await s.waitForTimeout(600);await s.evaluate(()=>go('photo'));
const img=await s.evaluate(async()=>{const c=document.createElement('canvas');c.width=900;c.height=260;const x=c.getContext('2d');x.fillStyle='#fff';x.fillRect(0,0,900,260);x.fillStyle='#000';x.font='bold 44px Arial';
  x.fillText('Your reservation is confirmed.',30,90);x.fillText('Breakfast is served until ten.',30,170);return c.toDataURL('image/png').split(',')[1];});
await s.setInputFiles('#phFile',{name:'sign.png',mimeType:'image/png',buffer:Buffer.from(img,'base64')});await s.waitForTimeout(400);
await s.evaluate(()=>phGo());await s.waitForTimeout(200);
assert.ok(await s.evaluate(()=>ph1.need==='noai'&&/Đọc chữ trên máy/.test(document.getElementById('main').textContent)),'gợi ý đọc trên máy khi không có AI');
await s.evaluate(()=>phOcr());
for(let i=0;i<120;i++){await s.waitForTimeout(500);if(await s.evaluate(()=>ph1.ocr&&!ph1.ocr.busy))break;}
const text=await s.evaluate(()=>ph1.ocr&&ph1.ocr.text);console.log('ocr',JSON.stringify(text));await shot(s,'m_ocr');
assert.ok(/reservation/i.test(text)&&/breakfast/i.test(text),'OCR đọc được chữ');
await s.evaluate(()=>phFromText());await s.waitForTimeout(200);
const o=await s.evaluate(()=>({src:ph1.res.src,v:ph1.res.vocab.map(x=>x.t),text:!!ph1.res.text,n:store.photoLessons.length}));console.log('offline',JSON.stringify(o));
assert.equal(o.src,'ocr');assert.ok(o.v.includes('reservation'),'tra được từ trong gói');assert.ok(o.text);assert.equal(o.n,1);
await shot(s,'m_ocr_lesson');report(s,'M ocr');await s.close();}
await b.close();console.log('M ALL OK');
