/* Nói Nghề 3D — "Ngày đầu đi làm": văn phòng low-poly (three.js), 4 hội thoại chọn đáp + 1 buổi nói chuyện AI với sếp.
   Dùng chung dữ liệu gói ngành (window.DATA.dialogues, window.PACK) và AI key của app (localStorage it-english-v1). Không build. */
(function(){
'use strict';
var $=function(s){return document.querySelector(s);};
var D=window.DATA||{dialogues:[]},PACK=window.PACK||null,TRACK=window.TRACK||'office';
var APPKEY='it-english-v1',KEY='it-english-game3d-v1';
function esc(s){return String(s==null?'':s).replace(/[&<>"]/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c];});}
function loadApp(){try{return JSON.parse(localStorage.getItem(APPKEY))||{};}catch(e){return {};}}
function loadS(){try{return Object.assign({best:0,plays:0},JSON.parse(localStorage.getItem(KEY))||{});}catch(e){return {best:0,plays:0};}}
function saveS(){try{localStorage.setItem(KEY,JSON.stringify(S));}catch(e){}}
var S=loadS();
function shuffle(a){a=a.slice();for(var i=a.length-1;i>0;i--){var j=Math.floor(Math.random()*(i+1)),t=a[i];a[i]=a[j];a[j]=t;}return a;}
var reduce=window.matchMedia&&matchMedia('(prefers-reduced-motion:reduce)').matches;

/* ---------- toast + TTS ---------- */
var tt;function toast(m){var t=$('#toast');t.textContent=m;t.classList.add('on');clearTimeout(tt);tt=setTimeout(function(){t.classList.remove('on');},2200);}
var talkUntil=0;
function speak(text){text=String(text||'').replace(/<[^>]+>/g,'');talkUntil=performance.now()+Math.min(5500,500+text.length*58);
  try{if(!('speechSynthesis'in window))return;speechSynthesis.cancel();var u=new SpeechSynthesisUtterance(text);u.lang='en-US';u.rate=.95;speechSynthesis.speak(u);}catch(e){}}

/* ---------- AI (giống game 2D: claude.ai sample → key trong app) ---------- */
function aiCfg(){var a=loadApp();return (a.ai&&a.ai.key&&a.ai.provider)?a.ai:null;}
function inClaude(){return !!(window.claude&&window.claude.use);}
function aiConfigured(){return inClaude()||!!aiCfg();}
var SAMPLE;function claudeSp(){if(SAMPLE!==undefined)return Promise.resolve(SAMPLE);SAMPLE=null;if(inClaude()){return window.claude.use('sample').then(function(s){SAMPLE=s;return s;},function(){return null;});}return Promise.resolve(null);}
async function aiCall(system,msgs){
  if(inClaude()){var sp=await claudeSp();if(sp){var r=await sp([{role:'user',content:system}].concat(msgs),{modelTier:'quick'});return (r&&r.text)||'';}}
  var c=aiCfg();if(!c)throw new Error('no-ai');
  if(c.provider==='gemini'){var model=c.model||'gemini-flash-lite-latest';
    var contents=[{role:'user',parts:[{text:system}]},{role:'model',parts:[{text:'OK.'}]}].concat(msgs.map(function(m){return {role:m.role==='assistant'?'model':'user',parts:[{text:m.content}]};}));
    var r1=await fetch('https://generativelanguage.googleapis.com/v1beta/models/'+encodeURIComponent(model)+':generateContent',{method:'POST',headers:{'Content-Type':'application/json','x-goog-api-key':c.key},body:JSON.stringify({contents:contents,generationConfig:{maxOutputTokens:400,temperature:.8}})});
    if(!r1.ok)throw new Error('Gemini '+r1.status);var j1=await r1.json();return (((j1.candidates||[])[0]||{}).content||{parts:[]}).parts.map(function(p){return p.text||'';}).join('');}
  if(c.provider==='claude'){var r2=await fetch('https://api.anthropic.com/v1/messages',{method:'POST',headers:{'Content-Type':'application/json','x-api-key':c.key,'anthropic-version':'2023-06-01','anthropic-dangerous-direct-browser-access':'true'},body:JSON.stringify({model:c.model||'claude-3-5-haiku-latest',max_tokens:400,system:system,messages:msgs})});
    if(!r2.ok)throw new Error('Claude '+r2.status);var j2=await r2.json();return (j2.content||[]).map(function(x){return x.text||'';}).join('');}
  var r3=await fetch('https://api.groq.com/openai/v1/chat/completions',{method:'POST',headers:{'Content-Type':'application/json','Authorization':'Bearer '+c.key},body:JSON.stringify({model:c.model||'llama-3.1-8b-instant',messages:[{role:'system',content:system}].concat(msgs),temperature:.8,max_tokens:400})});
  if(!r3.ok)throw new Error('Groq '+r3.status);var j3=await r3.json();return (((j3.choices||[])[0]||{}).message||{}).content||'';
}
function parseReply(t){var i=t.indexOf('FIX:');return i<0?{reply:t.trim(),fix:''}:{reply:t.slice(0,i).trim(),fix:t.slice(i+4).trim()};}

/* ---------- 3D ---------- */
var canvas=$('#c'),renderer,scene,camera,sun,amb,skyMat,people={},clockEl=$('#clock');
function mat(c){return new THREE.MeshLambertMaterial({color:c});}
function box(w,h,d,c,x,y,z,parent){var m=new THREE.Mesh(new THREE.BoxGeometry(w,h,d),mat(c));m.position.set(x,y,z);(parent||scene).add(m);return m;}
function person(o){
  var g=new THREE.Group(),skin=mat(o.skin),cloth=mat(o.cloth);
  var l1=box(.2,.5,.22,o.pants,-.13,.25,0,g),l2=box(.2,.5,.22,o.pants,.13,.25,0,g);
  var body=new THREE.Mesh(new THREE.CylinderGeometry(.26,.3,.75,12),cloth);body.position.y=.88;g.add(body);
  var a1=box(.12,.62,.14,o.cloth,-.37,.9,0,g),a2=box(.12,.62,.14,o.cloth,.37,.9,0,g);
  var head=new THREE.Group();head.position.y=1.5;g.add(head);
  var hm=new THREE.Mesh(new THREE.SphereGeometry(.25,16,12),skin);head.add(hm);
  var hair=new THREE.Mesh(new THREE.SphereGeometry(.27,16,10,0,Math.PI*2,0,Math.PI*.55),mat(o.hair));hair.position.set(0,.03,-.02);head.add(hair);
  [-.09,.09].forEach(function(x){var e=new THREE.Mesh(new THREE.SphereGeometry(.035,8,6),mat(0x1a1a1a));e.position.set(x,.03,.225);head.add(e);});
  var mouth=box(.1,.028,.02,0x7a2b2b,0,-.09,.235,head);
  if(o.tie){box(.07,.3,.03,o.tie,0,.95,.27,g);}
  g.userData={head:head,mouth:mouth,a1:a1,a2:a2,react:null,reactAt:0,base:0};
  return g;
}
var SLOTS=[
  {k:'reception',time:'08:30',where:'Quầy lễ tân',x:-6,z:-3,name:'Lan',role:'Lễ tân · HR',cast:{skin:0xf2c9a0,cloth:0xe86a92,pants:0x33344d,hair:0x2a1c14}},
  {k:'desk',time:'10:00',where:'Bàn làm việc',x:-1,z:-3,name:'David',role:'Đồng nghiệp bàn cạnh',cast:{skin:0xe8b48c,cloth:0x4a90d9,pants:0x2b2f3f,hair:0x4b2e1a}},
  {k:'kitchen',time:'12:15',where:'Bếp văn phòng',x:-6,z:2.5,name:'Emma',role:'Đồng nghiệp phòng khác',cast:{skin:0xf5d5b5,cloth:0x59b36b,pants:0x3a3a3a,hair:0xc0842c}},
  {k:'meeting',time:'14:00',where:'Phòng họp',x:5,z:-3,name:'Kenji',role:'Trưởng nhóm',cast:{skin:0xe3b58f,cloth:0x6b6bd6,pants:0x22263a,hair:0x151515}},
  {k:'boss',time:'16:30',where:'Phòng sếp',x:5,z:2.5,name:'Ms. Park',role:'Quản lý — nói chuyện tự do',cast:{skin:0xeac09a,cloth:0x30364f,pants:0x1c1f2e,hair:0x201510,tie:0xd9534f}}
];
function build(){
  scene=new THREE.Scene();scene.background=new THREE.Color(0x9ec9ff);scene.fog=new THREE.Fog(0x9ec9ff,14,34);
  camera=new THREE.PerspectiveCamera(58,1,.1,60);
  amb=new THREE.HemisphereLight(0xffffff,0x8a8f9e,.85);scene.add(amb);
  sun=new THREE.DirectionalLight(0xffffff,.8);sun.position.set(-4,9,6);scene.add(sun);
  // sàn + tường
  box(20,.2,15,0xcfd6e6,0,-.1,.5);
  box(20,4,.3,0xf1efe9,0,2,-6);box(.3,4,15,0xece9e2,-10,2,.5);box(.3,4,15,0xece9e2,10,2,.5);
  box(20,.12,.34,0x5a6688,0,.06,-6);
  // cửa sổ (nền trời đổi màu theo giờ)
  skyMat=new THREE.MeshBasicMaterial({color:0x9ec9ff});
  [-6,0,6].forEach(function(x){var w=new THREE.Mesh(new THREE.PlaneGeometry(3.2,1.9),skyMat);w.position.set(x,2.3,-5.83);scene.add(w);
    box(3.4,.1,.12,0x8a7a66,x,3.28,-5.85);box(3.4,.1,.12,0x8a7a66,x,1.32,-5.85);box(.1,2.0,.12,0x8a7a66,x-1.65,2.3,-5.85);box(.1,2.0,.12,0x8a7a66,x+1.65,2.3,-5.85);box(.06,1.9,.1,0x8a7a66,x,2.3,-5.85);});
  // thảm khu vực
  box(3.6,.02,3,0x8aa4d6,-6,.01,-3);box(3.6,.02,3,0xa4c6a0,-6,.01,2.5);box(4.6,.02,3.4,0xc6a4a4,5,.01,-3);box(4.6,.02,3.4,0xb8a4d6,5,.01,2.5);
  // lễ tân
  box(2.4,.95,.6,0x7a5c3e,-6,.48,-2.1);box(2.5,.06,.7,0xd9c29a,-6,.98,-2.1);box(.5,.32,.04,0x222a3d,-5.6,1.16,-2.15);box(.5,.16,.04,0x60a5fa,-6.6,1.2,-2.1);
  // bàn làm việc
  box(2.2,.06,1,0xc9a875,.9,.75,-3.4);box(.08,.75,.8,0x555b70,-.1,.37,-3.4);box(.08,.75,.8,0x555b70,1.9,.37,-3.4);
  box(.7,.45,.04,0x161b2b,.9,1.1,-3.7);box(.1,.3,.06,0x555b70,.9,.9,-3.7);box(.5,.02,.18,0x333a4d,.9,.79,-3.2);box(.3,.05,.3,0xffffff,1.6,.8,-3.4);
  box(.5,.06,.5,0x3c4460,-1.9,.5,-3.3);box(.06,.5,.5,0x3c4460,-1.9,.8,-3.55);
  // bếp
  box(3,.9,.7,0xe9e6df,-6,.45,4.6);box(3.1,.06,.8,0x8a8f9e,-6,.92,4.6);box(.3,.35,.3,0xb8bdd0,-5.3,1.13,4.6);box(.5,1.6,.6,0xd6dbe8,-8.2,.8,4.4);box(.25,.25,.25,0xd9534f,-6.9,1.05,4.6);
  // phòng họp
  box(3,.08,1.4,0xb98a5a,5,.78,-4.4);box(.1,.78,.1,0x555b70,3.7,.39,-4.4);box(.1,.78,.1,0x555b70,6.3,.39,-4.4);box(.8,.5,.04,0x1c2233,5,1.35,-5.8);box(.9,.55,.03,0xffffff,5,2.05,-5.82);
  [-1,0,1].forEach(function(i){box(.45,.06,.45,0x3c4460,4+i*1.0,.5,-3.5);box(.45,.5,.06,0x3c4460,4+i*1.0,.8,-3.28);});
  // phòng sếp
  box(2,.06,.9,0x6b4a2e,5,.78,1.3);box(.08,.78,.8,0x4a3320,4.05,.39,1.3);box(.08,.78,.8,0x4a3320,5.95,.39,1.3);box(.55,.4,.04,0x161b2b,5.3,1.1,1.1);
  box(.7,.1,.7,0x30364f,5,.55,.4);box(.7,.7,.1,0x30364f,5,.95,.05);
  // cây cảnh
  [[-9,-5],[9,-5],[9,5],[-9,5],[1,1]].forEach(function(p){box(.5,.4,.5,0xa86b3c,p[0],.2,p[1]);var l=new THREE.Mesh(new THREE.SphereGeometry(.45,10,8),mat(0x3f9d54));l.position.set(p[0],.85,p[1]);scene.add(l);});
  // người
  SLOTS.forEach(function(s){var p=person(s.cast);p.position.set(s.x,0,s.z);p.userData.base=s.z;
    p.rotation.y=(s.x<0?.18:-.18);scene.add(p);people[s.k]=p;});
}
var camTarget={p:new THREE.Vector3(0,7,10),l:new THREE.Vector3(0,0,-1)},camPos=new THREE.Vector3(0,7,10),camLook=new THREE.Vector3(0,0,-1);
function focusSlot(i){var s=SLOTS[i];camTarget.p.set(s.x+(s.x<0?.9:-.9),1.9,s.z+4.2);camTarget.l.set(s.x,-.05,s.z);}
function overview(){camTarget.p.set(0,6.5,11);camTarget.l.set(0,0,-1);}
function setDayTime(f){ // f 0..1 (08:30 → 17:30)
  var c1=new THREE.Color(0xffd9a8),c2=new THREE.Color(0x9ec9ff),c3=new THREE.Color(0xff9e6b),c;
  if(f<.35)c=c1.clone().lerp(c2,f/.35);else if(f<.7)c=c2.clone();else c=c2.clone().lerp(c3,(f-.7)/.3);
  scene.background.copy(c);scene.fog.color.copy(c);skyMat.color.copy(c);
  sun.color.copy(new THREE.Color(0xffffff).lerp(new THREE.Color(0xffb27a),Math.max(0,(f-.6)/.4)));sun.intensity=.85-.25*Math.max(0,f-.6);
}
function resize(){var w=innerWidth,h=innerHeight;renderer.setPixelRatio(Math.min(devicePixelRatio||1,1.5));renderer.setSize(w,h,false);camera.aspect=w/h;camera.fov=w/h<.75?66:52;camera.updateProjectionMatrix();}
var t0=performance.now();
function frame(now){
  requestAnimationFrame(frame);
  var dt=Math.min(.05,(now-t0)/1000);t0=now;
  camPos.lerp(camTarget.p,1-Math.pow(.02,dt));camLook.lerp(camTarget.l,1-Math.pow(.02,dt));
  camera.position.copy(camPos);camera.lookAt(camLook);
  if(!reduce&&!st.on){var a=now/9000;camTarget.p.set(Math.sin(a)*3,6.3,11);}
  Object.keys(people).forEach(function(k,ix){var p=people[k],u=p.userData,talking=(now<talkUntil)&&SLOTS[st.i]&&SLOTS[st.i].k===k&&st.on;
    if(!reduce)p.position.y=Math.sin(now/700+ix)*.012;
    u.mouth.scale.y=talking?(1+(Math.sin(now/70)>0?3:0)):1;
    var rx=0,ry=0;if(u.react){var e=(now-u.reactAt)/700;if(e>1)u.react=null;else{if(u.react==='nod')rx=Math.sin(e*Math.PI*3)*.28*(1-e);else ry=Math.sin(e*Math.PI*4)*.4*(1-e);}}
    u.head.rotation.x=rx;u.head.rotation.y=ry;
    if(talking&&!reduce){u.a1.rotation.z=Math.sin(now/220)*.12;u.a2.rotation.z=-Math.sin(now/260)*.12;}else{u.a1.rotation.z=u.a2.rotation.z=0;}
  });
  renderer.render(scene,camera);
}

/* ---------- Game flow ---------- */
var st={on:false,i:0,imp:50,list:[],miss:[],good:0,total:0,chat:null,done:false};
window.__g3d={st:st,S:function(){return S;},slots:SLOTS};
function setImp(v){st.imp=Math.max(0,Math.min(100,v));$('#impbar').style.width=st.imp+'%';}
function panel(html){var p=$('#panel');p.innerHTML=html;p.scrollTop=0;return p;}
function pickDialogs(n){var all=(D.dialogues||[]).filter(function(d){return d&&d.them&&d.opts&&d.opts.some(function(o){return o.good;})&&d.opts.length>=2;});return shuffle(all).slice(0,n);}
function trackLabel(){return PACK?(PACK.emoji||'')+' '+PACK.label:'💻 IT · Phần mềm';}

function intro(){
  overview();st.on=false;setImp(50);
  panel('<div class="box"><h2>Ngày đầu đi làm</h2><div class="muted">Bạn là nhân viên mới ('+esc(trackLabel())+'). Đi qua 5 điểm trong văn phòng: nói đúng, đồng nghiệp sẽ nể bạn. Chọn câu đáp phù hợp ở 4 điểm đầu, rồi nói chuyện tự do với quản lý ở cuối ngày.</div>'+
    '<div class="muted">'+(aiConfigured()?'✅ AI sẵn sàng cho cuộc nói chuyện cuối ngày.':'ℹ️ Chưa có AI — cuối ngày dùng câu chọn. Nhập key trong Hồ sơ của game chính để nói tự do.')+'</div>'+
    '<div class="muted">Điểm cao nhất: <b>'+S.best+'</b> · Số lần chơi: <b>'+S.plays+'</b></div>'+
    '<button class="btn" id="go">Bắt đầu 08:30</button></div>');
  $('#go').onclick=function(){start();};
}
function start(){
  st.on=true;st.i=0;st.list=[];st.miss=[];st.good=0;st.total=0;st.done=false;setImp(50);
  var need=aiConfigured()?4:5;st.dlg=pickDialogs(need);
  if(st.dlg.length<need){toast('Gói này chưa đủ hội thoại');}
  scene0();
}
function scene0(){
  var s=SLOTS[st.i];focusSlot(st.i);clockEl.textContent=s.time;setDayTime(st.i/(SLOTS.length-1));
  if(st.i===SLOTS.length-1&&aiConfigured())return chatScene();
  var d=st.dlg[Math.min(st.i,st.dlg.length-1)];
  if(!d){return finish();}
  choiceScene(s,d);
}
function choiceScene(s,d){
  var opts=shuffle(d.opts);
  panel('<div class="box"><div class="who">'+esc(s.where)+' · '+esc(s.name)+' <span class="muted" style="text-transform:none">'+esc(s.role)+'</span></div>'+
    '<div class="line" id="line">“'+esc(d.them)+'”</div><button class="btn ghost" id="rep" style="align-self:flex-start;min-height:36px;padding:6px 10px">🔊 Nghe lại</button>'+
    '<div class="muted">Bạn sẽ đáp thế nào?</div><div id="opts" style="display:flex;flex-direction:column;gap:8px"></div><div id="fbx"></div></div>');
  $('#rep').onclick=function(){speak(d.them);};
  var wrap=$('#opts');
  opts.forEach(function(o){var b=document.createElement('button');b.className='opt';b.textContent=o.t;b.onclick=function(){answer(b,o,d,s,opts);};wrap.appendChild(b);});
  setTimeout(function(){speak(d.them);},600);
}
function answer(btn,o,d,s,opts){
  var all=document.querySelectorAll('#opts .opt');all.forEach(function(b){b.disabled=true;});
  st.total++;var p=people[s.k].userData;p.reactAt=performance.now();
  var good=opts.filter(function(x){return x.good;})[0];
  if(o.good){st.good++;btn.classList.add('ok');setImp(st.imp+16);p.react='nod';}
  else{btn.classList.add('no');setImp(st.imp-9);p.react='shake';
    all.forEach(function(b,ix){if(opts[ix]===good)b.classList.add('ok');});
    st.miss.push({wrong:o.t,right:good?good.t:'',note:o.fb||''});}
  var fb=$('#fbx');fb.innerHTML='<div class="fb '+(o.good?'ok':'no')+'">'+(o.good?'✅ ':'❌ ')+esc(o.fb||'')+'</div><button class="btn" id="nx" style="margin-top:8px;width:100%">'+(st.i>=SLOTS.length-1?'Kết thúc ngày':'Tiếp — '+SLOTS[st.i+1].time)+'</button>';
  if(good)speak(good.t);
  $('#nx').onclick=next;
}
function next(){st.i++;if(st.i>=SLOTS.length)return finish();scene0();}

/* --- Cuộc nói chuyện AI với quản lý --- */
function bossSystem(){
  var lvl=(loadApp().cfg||{}).level||'A2',who=PACK?PACK.persona:'a Vietnamese software developer',ctx=PACK?PACK.context:'a software company';
  return 'You are Ms. Park, a friendly but busy manager at '+ctx+'. The person talking to you is '+who+' (CEFR '+lvl+') at the END of their first day at work. Chat about how the first day went, what they learned, and tomorrow. Use very simple English, max 2 short sentences, and ask ONE question at a time. After your reply, on a NEW line write "FIX:" followed by either OK (if their last message was fine) or "wrong => right ~ short Vietnamese note" for the most important mistake. Never skip the FIX line.';
}
function chatScene(){
  var s=SLOTS[st.i];st.chat={turns:[],user:0,busy:false};
  panel('<div class="box"><div class="who">'+esc(s.where)+' · '+esc(s.name)+' <span class="muted" style="text-transform:none">'+esc(s.role)+'</span></div>'+
    '<div class="chat" id="chat"></div><div class="row"><input class="tx" id="inp" placeholder="Trả lời bằng tiếng Anh…" autocomplete="off"><button class="btn ghost" id="mic" aria-label="Nói">🎤</button><button class="btn" id="snd">Gửi</button></div>'+
    '<div class="muted" id="cnt">Lượt 0/3 — nói đủ 3 lượt để kết thúc ngày</div></div>');
  $('#snd').onclick=function(){send();};
  $('#inp').onkeydown=function(e){if(e.key==='Enter')send();};
  $('#mic').onclick=mic;
  bossTurn([{role:'user',content:'(I walk into your office at the end of my first day.)'}],true);
}
function bubble(cls,txt){var c=$('#chat');if(!c)return;var b=document.createElement('div');b.className='b '+cls;b.innerHTML=txt;c.appendChild(b);c.scrollTop=c.scrollHeight;return b;}
async function bossTurn(msgs,first){
  var ch=st.chat;ch.busy=true;var wait=bubble('ai','…');
  try{var raw=await aiCall(bossSystem(),msgs);var r=parseReply(raw);wait.textContent=r.reply;ch.turns.push({role:'assistant',content:raw});speak(r.reply);
    if(!first&&r.fix===''){}
    ch.lastFix=r.fix;
  }catch(e){wait.textContent='(AI đang bận, thử gửi lại)';ch.turns.pop&&0;}
  ch.busy=false;
}
async function send(){
  var ch=st.chat,inp=$('#inp');if(!ch||ch.busy)return;var t=inp.value.trim();if(!t)return;inp.value='';
  var ub=bubble('me',esc(t));ch.user++;$('#cnt').textContent='Lượt '+Math.min(ch.user,3)+'/3';
  var msgs=(ch.turns.length?[{role:'user',content:'(I walk into your office at the end of my first day.)'}]:[]).concat(ch.turns.map(function(m){return {role:m.role,content:m.content};})).concat([{role:'user',content:t}]);
  ch.turns.push({role:'user',content:t});ch.busy=true;var wait=bubble('ai','…');
  try{var raw=await aiCall(bossSystem(),msgs);var r=parseReply(raw);wait.textContent=r.reply;ch.turns.push({role:'assistant',content:raw});speak(r.reply);
    var ok=/^\s*ok\b/i.test(r.fix)||!r.fix;
    if(ok){setImp(st.imp+8);st.good++;}else{setImp(st.imp+2);var m=r.fix.match(/^(.*?)\s*=>\s*(.*?)(?:\s*~\s*(.*))?$/);
      if(m){st.miss.push({wrong:m[1].trim(),right:m[2].trim(),note:(m[3]||'').trim()});ub.innerHTML+='<div class="vi">💡 '+esc(m[2].trim())+(m[3]?' — '+esc(m[3].trim()):'')+'</div>';}}
    st.total++;
    var pu=people.boss.userData;pu.react=ok?'nod':'shake';pu.reactAt=performance.now();
  }catch(e){wait.textContent='(AI đang bận — thử gửi lại câu đó)';ch.user--;$('#cnt').textContent='Lượt '+ch.user+'/3';ch.turns.pop();}
  ch.busy=false;
  if(ch.user>=3&&!$('#endd')){var b=document.createElement('button');b.className='btn';b.id='endd';b.style.width='100%';b.textContent='Kết thúc ngày đi làm';b.onclick=finish;$('#cnt').after(b);}
}
function mic(){var SR=window.SpeechRecognition||window.webkitSpeechRecognition;if(!SR){toast('Trình duyệt không hỗ trợ mic');return;}
  var r=new SR();r.lang='en-US';r.onresult=function(e){$('#inp').value=e.results[0][0].transcript;};r.onerror=function(){toast('Không nghe được, thử lại');};try{r.start();toast('Đang nghe…');}catch(e){}}

/* --- Kết thúc --- */
function rankOf(v){return v<35?['Chưa qua thử việc','😅','Ôn lại các câu đáp rồi thử ngày mới nhé.']:v<60?['Qua thử việc','🙂','Đồng nghiệp thấy bạn ổn. Cố thêm chút nữa để được nể.']:v<85?['Được đồng nghiệp mến','😄','Giao tiếp tự nhiên, ngày đầu rất ổn!']:['Ngôi sao ngày đầu','🌟','Sếp đã nhớ tên bạn. Xuất sắc!'];}
function finish(){
  if(st.done)return;st.done=true;st.on=false;overview();speak('');clockEl.textContent='17:30';setDayTime(1);
  var r=rankOf(st.imp);S.plays++;var nb=st.imp>S.best;if(nb)S.best=st.imp;saveS();
  panel('<div class="box"><h2>'+r[1]+' '+esc(r[0])+'</h2><div class="muted">Ấn tượng: <b>'+st.imp+'/100</b>'+(nb?' · 🏆 Kỷ lục mới':'')+' · Đáp tốt '+st.good+'/'+st.total+'. '+esc(r[2])+'</div>'+
    (st.miss.length?'<div class="who">Nên nói thế này</div><div style="display:flex;flex-direction:column;gap:6px">'+st.miss.slice(0,5).map(function(m){return '<div class="fb no"><s>'+esc(m.wrong)+'</s><br>→ <b>'+esc(m.right)+'</b>'+(m.note?'<br><span class="vi">'+esc(m.note)+'</span>':'')+'</div>';}).join('')+'</div>':'<div class="muted">Không sai câu nào 👏</div>')+
    '<div class="row"><button class="btn grow" id="again">Chơi lại</button><a class="btn ghost grow" href="../game/" style="text-decoration:none;text-align:center;display:flex;align-items:center;justify-content:center">Game chính</a></div></div>');
  $('#again').onclick=start;
}

/* ---------- Khởi động ---------- */
function boot(){
  try{renderer=new THREE.WebGLRenderer({canvas:canvas,antialias:true});}catch(e){$('#nogl').style.display='flex';return;}
  if(!renderer.getContext()){$('#nogl').style.display='flex';return;}
  build();resize();addEventListener('resize',resize);setDayTime(0);
  camPos.copy(camTarget.p);camLook.copy(camTarget.l);
  requestAnimationFrame(frame);intro();
}
boot();
})();
