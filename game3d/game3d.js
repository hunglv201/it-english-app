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
function sprite(txt,fs,bg){var c=document.createElement('canvas');c.width=256;c.height=96;var x=c.getContext('2d');x.font='700 '+fs+'px sans-serif';x.textAlign='center';x.textBaseline='middle';
  if(bg){x.fillStyle=bg;var w=Math.min(250,x.measureText(txt).width+34);x.beginPath();x.roundRect?x.roundRect(128-w/2,16,w,64,30):x.rect(128-w/2,16,w,64);x.fill();}
  x.fillStyle='#fff';x.fillText(txt,128,49);var t=new THREE.CanvasTexture(c);var sp=new THREE.Sprite(new THREE.SpriteMaterial({map:t,transparent:true,depthTest:false}));sp.scale.set(.85,.32,1);sp.renderOrder=9;return sp;}
function person(o){
  var g=new THREE.Group(),skin=mat(o.skin),cloth=mat(o.cloth),pm=mat(o.pants);
  var l1=box(.19,.5,.21,o.pants,-.13,.27,0,g),l2=box(.19,.5,.21,o.pants,.13,.27,0,g);
  box(.22,.09,.32,0x1b1b22,-.13,.05,.04,g);box(.22,.09,.32,0x1b1b22,.13,.05,.04,g);
  var body=new THREE.Mesh(new THREE.CylinderGeometry(.27,.31,.78,14),cloth);body.position.y=.9;g.add(body);
  box(.5,.07,.3,o.pants,0,.55,0,g);
  var a1=new THREE.Group(),a2=new THREE.Group();a1.position.set(-.36,1.22,0);a2.position.set(.36,1.22,0);g.add(a1,a2);
  [a1,a2].forEach(function(a,ix){var arm=box(.12,.58,.14,o.cloth,0,-.29,0,a);var hand=new THREE.Mesh(new THREE.SphereGeometry(.075,10,8),skin);hand.position.set(0,-.62,0);a.add(hand);});
  var neck=new THREE.Mesh(new THREE.CylinderGeometry(.09,.1,.14,10),skin);neck.position.y=1.33;g.add(neck);
  var head=new THREE.Group();head.position.y=1.55;g.add(head);
  head.add(new THREE.Mesh(new THREE.SphereGeometry(.26,20,16),skin));
  var hair=new THREE.Mesh(new THREE.SphereGeometry(.28,20,12,0,Math.PI*2,0,Math.PI*.55),mat(o.hair));hair.position.set(0,.03,-.02);head.add(hair);
  if(o.long){box(.5,.5,.14,o.hair,0,-.12,-.17,head);}
  var eyes=[];[-.095,.095].forEach(function(x){var w=new THREE.Mesh(new THREE.SphereGeometry(.05,10,8),mat(0xffffff));w.position.set(x,.03,.21);w.scale.z=.5;head.add(w);
    var e=new THREE.Mesh(new THREE.SphereGeometry(.03,10,8),mat(0x1a1a1a));e.position.set(x,.03,.238);head.add(e);eyes.push(w,e);
    box(.1,.018,.02,o.hair,x,.12,.235,head);});
  var nose=new THREE.Mesh(new THREE.SphereGeometry(.03,8,6),skin);nose.position.set(0,-.03,.26);head.add(nose);
  [-.15,.15].forEach(function(x){var ch=new THREE.Mesh(new THREE.SphereGeometry(.04,8,6),mat(0xf08a8a));ch.position.set(x,-.05,.2);ch.scale.z=.3;head.add(ch);});
  var mouth=box(.11,.026,.02,0x8a3030,0,-.11,.245,head);
  if(o.glasses){[-.095,.095].forEach(function(x){var r=new THREE.Mesh(new THREE.TorusGeometry(.06,.01,6,14),mat(0x222222));r.position.set(x,.03,.245);head.add(r);});}
  if(o.tie){box(.07,.34,.03,o.tie,0,.98,.29,g);}
  var tag=sprite(o.name,40,'rgba(20,24,44,.82)');tag.position.set(0,2.05,0);g.add(tag);
  g.userData={head:head,mouth:mouth,a1:a1,a2:a2,eyes:eyes,react:null,reactAt:0,base:0,bub:null,bubAt:0};
  return g;
}
var SLOTS=[
  {k:'reception',time:'08:30',where:'Quầy lễ tân',x:-6,z:-3,name:'Lan',role:'Lễ tân · HR',goal:'You are Lan, the front-desk/HR person. Greet the new employee, ask their name, tell them about the badge, wifi password and where to sit. Be warm.',cast:{name:'Lan',long:1,skin:0xf2c9a0,cloth:0xe86a92,pants:0x33344d,hair:0x2a1c14}},
  {k:'desk',time:'10:00',where:'Bàn làm việc',x:-1,z:-3,name:'David',role:'Đồng nghiệp bàn cạnh',goal:'You are David, the colleague at the next desk. Introduce yourself, ask what the new person will work on, offer help, and talk about the team.',cast:{name:'David',skin:0xe8b48c,cloth:0x4a90d9,pants:0x2b2f3f,hair:0x4b2e1a,glasses:1}},
  {k:'kitchen',time:'12:15',where:'Bếp văn phòng',x:-6,z:2.5,name:'Emma',role:'Đồng nghiệp phòng khác',goal:'You are Emma from another department, meeting the new person in the kitchen at lunch. Make small talk: coffee, lunch, hobbies, weekend, where they live.',cast:{name:'Emma',long:1,skin:0xf5d5b5,cloth:0x59b36b,pants:0x3a3a3a,hair:0xc0842c}},
  {k:'meeting',time:'14:00',where:'Phòng họp',x:5,z:-3,name:'Kenji',role:'Trưởng nhóm',goal:'You are Kenji, the team lead, in a short team meeting. Ask the new person for a quick self-introduction, then ask a work question they must answer or clarify (deadline, task, problem). Sometimes speak fast so they must ask you to repeat.',cast:{name:'Kenji',skin:0xe3b58f,cloth:0x6b6bd6,pants:0x22263a,hair:0x151515}},
  {k:'boss',time:'16:30',where:'Phòng sếp',x:5,z:2.5,name:'Ms. Park',role:'Quản lý — nói chuyện tự do',goal:'You are Ms. Park, the manager. It is the END of their first day. Ask how the day went, what they learned, what was difficult, and about tomorrow.',cast:{name:'Ms. Park',long:1,skin:0xeac09a,cloth:0x30364f,pants:0x1c1f2e,hair:0x201510,tie:0xd9534f}}
];
function build(){
  scene=new THREE.Scene();scene.background=new THREE.Color(0x9ec9ff);scene.fog=new THREE.Fog(0x9ec9ff,14,34);
  camera=new THREE.PerspectiveCamera(58,1,.1,60);
  amb=new THREE.HemisphereLight(0xffffff,0x8a8f9e,.85);scene.add(amb);
  sun=new THREE.DirectionalLight(0xffffff,.8);sun.position.set(-4,9,6);sun.castShadow=true;sun.shadow.mapSize.set(1024,1024);var sc=sun.shadow.camera;sc.left=-13;sc.right=13;sc.top=10;sc.bottom=-10;sc.near=1;sc.far=30;sun.shadow.bias=-.0008;scene.add(sun);
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
  // sàn caro + trang trí
  for(var gx=-9;gx<=9;gx+=2)box(.03,.01,15,0xbcc4d8,gx,.005,.5);for(var gz=-5;gz<=7;gz+=2)box(20,.01,.03,0xbcc4d8,0,.006,gz);
  box(1.6,.5,.7,0x5b6fd6,-8.4,.25,-4.8);box(1.6,.5,.15,0x4a5cbb,-8.4,.7,-5.1); // sofa
  box(.9,.6,.08,0xffffff,-3.4,2.4,-5.85);box(.85,.55,.02,0xf59e0b,-3.4,2.4,-5.8);box(.9,.6,.08,0xffffff,3.2,2.4,-5.85);box(.85,.55,.02,0x60a5fa,3.2,2.4,-5.8); // tranh
  var ck=new THREE.Mesh(new THREE.CylinderGeometry(.3,.3,.06,20),mat(0xffffff));ck.rotation.x=Math.PI/2;ck.position.set(2.6,3.3,-5.8);scene.add(ck);box(.03,.22,.02,0x222222,2.6,3.36,-5.76);box(.16,.03,.02,0x222222,2.65,3.3,-5.76);
  box(2.2,1.6,.3,0x6b4a2e,8.6,.8,-5.5);[.4,.9,1.4].forEach(function(y){box(2,.05,.34,0x8a6a44,8.6,y,-5.5);[0,1,2,3,4].forEach(function(n){box(.25,.3,.2,[0xd9534f,0x4a90d9,0x59b36b,0xf59e0b,0x9b6bd6][n],7.9+n*.35,y+.18,-5.5);});}); // giá sách
  box(.6,.9,.6,0x30364f,-9,.45,1);box(.4,.3,.4,0xd9534f,-9,1.1,1); // máy pha cà phê
  [-4,-2].forEach(function(x){box(.9,.05,.9,0xc9a875,x,.75,-3.4);box(.06,.75,.06,0x555b70,x-.4,.37,-3.0);box(.06,.75,.06,0x555b70,x+.4,.37,-3.8);box(.5,.35,.04,0x161b2b,x,1.05,-3.7);});
  // người
  SLOTS.forEach(function(s){var p=person(s.cast);p.position.set(s.x,0,s.z);p.userData.base=s.z;
    p.rotation.y=(s.x<0?.18:-.18);scene.add(p);people[s.k]=p;});
  scene.traverse(function(o){if(o.isMesh&&o.material!==skyMat){o.castShadow=true;o.receiveShadow=true;}});
}
var camTarget={p:new THREE.Vector3(0,7,10),l:new THREE.Vector3(0,0,-1)},camPos=new THREE.Vector3(0,7,10),camLook=new THREE.Vector3(0,0,-1);
function focusSlot(i){var s=SLOTS[i];camTarget.p.set(s.x+(s.x<0?.9:-.9),1.9,s.z+4.2);camTarget.l.set(s.x,-.05,s.z);}
function emote(k,e){var p=people[k],u=p.userData;if(u.bub)p.remove(u.bub);var sp=sprite(e,60);sp.scale.set(.9,.34,1);sp.position.set(0,2.55,0);p.add(sp);u.bub=sp;u.bubAt=performance.now();}
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
    var bl=(Math.floor(now/1000+ix*.7)%4===0&&(now%1000)<130)?.1:1;u.eyes.forEach(function(e){e.scale.y=bl;});
    if(talking&&!reduce){u.a1.rotation.z=Math.sin(now/220)*.35;u.a2.rotation.z=-Math.sin(now/260)*.35;u.a1.rotation.x=Math.sin(now/300)*.25;}else{u.a1.rotation.z=.05;u.a2.rotation.z=-.05;u.a1.rotation.x=0;if(!reduce)u.a1.rotation.x=Math.sin(now/900+ix)*.03;}
    if(u.bub){var e2=(now-u.bubAt)/1600;if(e2>1){p.remove(u.bub);u.bub=null;}else{u.bub.position.y=2.55+e2*.35;u.bub.material.opacity=1-Math.max(0,e2-.7)/.3;}}
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
  panel('<div class="box"><h2>Ngày đầu đi làm</h2><div class="muted">Bạn là nhân viên mới ('+esc(trackLabel())+'). Đi qua 5 điểm trong văn phòng: nói đúng, đồng nghiệp sẽ nể bạn. Mỗi điểm: chọn câu đáp, rồi (nếu có AI) nói chuyện tự do với nhân vật đó.</div>'+
    '<div class="muted">'+(aiConfigured()?'✅ AI sẵn sàng: mỗi nhân vật sẽ trò chuyện tự do với bạn.':'ℹ️ Chưa có AI — chỉ có câu chọn. Nhập key trong Hồ sơ game chính để nói chuyện tự do ở mỗi điểm.')+'</div>'+
    '<div class="muted">Điểm cao nhất: <b>'+S.best+'</b> · Số lần chơi: <b>'+S.plays+'</b></div>'+
    '<button class="btn" id="go">Bắt đầu 08:30</button></div>');
  $('#go').onclick=function(){start();};
}
function start(){
  st.on=true;st.i=0;st.list=[];st.miss=[];st.good=0;st.total=0;st.done=false;setImp(50);
  var need=5;st.dlg=pickDialogs(need);
  if(st.dlg.length<need){toast('Gói này chưa đủ hội thoại');}
  scene0();
}
function scene0(){
  var s=SLOTS[st.i];focusSlot(st.i);clockEl.textContent=s.time;setDayTime(st.i/(SLOTS.length-1));
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
  if(o.good){st.good++;btn.classList.add('ok');setImp(st.imp+16);p.react='nod';emote(s.k,'👍');}
  else{btn.classList.add('no');setImp(st.imp-9);p.react='shake';emote(s.k,'🤔');
    all.forEach(function(b,ix){if(opts[ix]===good)b.classList.add('ok');});
    st.miss.push({wrong:o.t,right:good?good.t:'',note:o.fb||''});}
  var fb=$('#fbx');fb.innerHTML='<div class="fb '+(o.good?'ok':'no')+'">'+(o.good?'✅ ':'❌ ')+esc(o.fb||'')+'</div><button class="btn" id="nx" style="margin-top:8px;width:100%">'+(aiConfigured()?'💬 Nói chuyện tiếp với '+s.name:(st.i>=SLOTS.length-1?'Kết thúc ngày':'Tiếp — '+SLOTS[st.i+1].time))+'</button>';
  if(good)speak(good.t);
  $('#nx').onclick=function(){if(aiConfigured())chatScene(s);else next();};
}
function next(){st.i++;if(st.i>=SLOTS.length)return finish();scene0();}

/* --- Cuộc nói chuyện AI với quản lý --- */
function bossSystem(){
  var s=SLOTS[st.i],lvl=(loadApp().cfg||{}).level||'A2',who=PACK?PACK.persona:'a Vietnamese software developer',ctx=PACK?PACK.context:'a software company';
  return s.goal+' The setting is '+ctx+', time '+s.time+' on the new person\'s FIRST DAY. The person talking to you is '+who+' (CEFR '+lvl+'). Stay in character, use very simple English, max 2 short sentences, ask ONE question at a time, and react naturally to what they say. After your reply, on a NEW line write "FIX:" followed by either OK (if their last message was fine) or "wrong => right ~ short Vietnamese note" for the most important mistake. Never skip the FIX line.';
}
function chatScene(s){
  focusSlot(st.i);st.chat={turns:[],user:0,busy:false,need:(st.i===SLOTS.length-1?3:2)};
  panel('<div class="box"><div class="who">'+esc(s.where)+' · '+esc(s.name)+' <span class="muted" style="text-transform:none">'+esc(s.role)+'</span></div>'+
    '<div class="chat" id="chat"></div><div class="row"><input class="tx" id="inp" placeholder="Trả lời bằng tiếng Anh…" autocomplete="off"><button class="btn ghost" id="mic" aria-label="Nói">🎤</button><button class="btn" id="snd">Gửi</button></div>'+
    '<div class="muted" id="cnt">Lượt 0/'+st.chat.need+' — nói đủ để đi tiếp</div></div>');
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
  var ub=bubble('me',esc(t));ch.user++;$('#cnt').textContent='Lượt '+Math.min(ch.user,ch.need)+'/'+ch.need;
  var msgs=(ch.turns.length?[{role:'user',content:'(I walk into your office at the end of my first day.)'}]:[]).concat(ch.turns.map(function(m){return {role:m.role,content:m.content};})).concat([{role:'user',content:t}]);
  ch.turns.push({role:'user',content:t});ch.busy=true;var wait=bubble('ai','…');
  try{var raw=await aiCall(bossSystem(),msgs);var r=parseReply(raw);wait.textContent=r.reply;ch.turns.push({role:'assistant',content:raw});speak(r.reply);
    var ok=/^\s*ok\b/i.test(r.fix)||!r.fix;
    if(ok){setImp(st.imp+8);st.good++;}else{setImp(st.imp+2);var m=r.fix.match(/^(.*?)\s*=>\s*(.*?)(?:\s*~\s*(.*))?$/);
      if(m){st.miss.push({wrong:m[1].trim(),right:m[2].trim(),note:(m[3]||'').trim()});ub.innerHTML+='<div class="vi">💡 '+esc(m[2].trim())+(m[3]?' — '+esc(m[3].trim()):'')+'</div>';}}
    st.total++;
    var pu=people[SLOTS[st.i].k].userData;pu.react=ok?'nod':'shake';pu.reactAt=performance.now();emote(SLOTS[st.i].k,ok?'😊':'🤔');
  }catch(e){wait.textContent='(AI đang bận — thử gửi lại câu đó)';ch.user--;$('#cnt').textContent='Lượt '+ch.user+'/'+ch.need;ch.turns.pop();}
  ch.busy=false;
  if(ch.user>=ch.need&&!$('#endd')){var last=st.i>=SLOTS.length-1,b=document.createElement('button');b.className='btn';b.id='endd';b.style.width='100%';b.textContent=last?'Kết thúc ngày đi làm':'Tiếp — '+SLOTS[st.i+1].time;b.onclick=last?finish:next;$('#cnt').after(b);}
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
  try{renderer=new THREE.WebGLRenderer({canvas:canvas,antialias:true});renderer.shadowMap.enabled=true;renderer.shadowMap.type=THREE.PCFSoftShadowMap;}catch(e){$('#nogl').style.display='flex';return;}
  if(!renderer.getContext()){$('#nogl').style.display='flex';return;}
  build();resize();addEventListener('resize',resize);setDayTime(0);
  camPos.copy(camTarget.p);camLook.copy(camTarget.l);
  requestAnimationFrame(frame);intro();
}
boot();
})();
