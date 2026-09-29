/* Nói Nghề 3D — "Ngày đầu đi làm": văn phòng 2D hoạt hình (canvas), 4 hội thoại chọn đáp + 1 buổi nói chuyện AI với sếp.
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

/* ---------- Đồ hoạ 2D+ (canvas): mặt cắt văn phòng, nhân vật chibi hoạt hình, camera lướt giữa các phòng ---------- */
var canvas=$('#c'),cx=canvas.getContext('2d'),people={},clockEl=$('#clock'),DPR=1,CW=360,CH=640;
var W=380,WALL=270,DAYF=0;
function col(n){return typeof n==='string'?n:'#'+('000000'+n.toString(16)).slice(-6);}
function lerpHex(a,b,t){a=parseInt(a.slice(1),16);b=parseInt(b.slice(1),16);var r=[16,8,0].map(function(s){var x=(a>>s)&255,y=(b>>s)&255;return Math.round(x+(y-x)*t);});return 'rgb('+r.join(',')+')';}
function rr(x,y,w,h,r,f,stroke){cx.beginPath();r=Math.min(r,w/2,h/2);cx.moveTo(x+r,y);cx.arcTo(x+w,y,x+w,y+h,r);cx.arcTo(x+w,y+h,x,y+h,r);cx.arcTo(x,y+h,x,y,r);cx.arcTo(x,y,x+w,y,r);cx.closePath();if(f){cx.fillStyle=f;cx.fill();}if(stroke){cx.strokeStyle=stroke;cx.stroke();}}
function el(x,y,rx,ry,f,rot){cx.beginPath();cx.ellipse(x,y,Math.max(.01,rx),Math.max(.01,ry),rot||0,0,7);cx.fillStyle=f;cx.fill();}
function ln(x1,y1,x2,y2,w,c){cx.beginPath();cx.moveTo(x1,y1);cx.lineTo(x2,y2);cx.lineWidth=w;cx.lineCap='round';cx.strokeStyle=c;cx.stroke();}
function txt(t,x,y,size,c,al,w){cx.font=(w||'800')+' '+size+'px system-ui,-apple-system,sans-serif';cx.textAlign=al||'center';cx.textBaseline='middle';cx.fillStyle=c;cx.fillText(t,x,y);}

var SLOTS=[
  {k:'reception',time:'08:30',where:'Quầy lễ tân',name:'Lan',role:'Lễ tân · HR',goal:'You are Lan, the front-desk/HR person. Greet the new employee, ask their name, tell them about the badge, wifi password and where to sit. Be warm.',front:1,cast:{name:'Lan',long:1,skin:0xf2c9a0,cloth:0xe86a92,pants:0x33344d,hair:0x2a1c14}},
  {k:'desk',time:'10:00',where:'Bàn làm việc',name:'David',role:'Đồng nghiệp bàn cạnh',goal:'You are David, the colleague at the next desk. Introduce yourself, ask what the new person will work on, offer help, and talk about the team.',cast:{name:'David',skin:0xe8b48c,cloth:0x4a90d9,pants:0x2b2f3f,hair:0x4b2e1a,glasses:1}},
  {k:'kitchen',time:'12:15',where:'Bếp văn phòng',name:'Emma',role:'Đồng nghiệp phòng khác',goal:'You are Emma from another department, meeting the new person in the kitchen at lunch. Make small talk: coffee, lunch, hobbies, weekend, where they live.',cast:{name:'Emma',long:1,skin:0xf5d5b5,cloth:0x59b36b,pants:0x3a3a3a,hair:0xc0842c}},
  {k:'meeting',time:'14:00',where:'Phòng họp',name:'Kenji',role:'Trưởng nhóm',goal:'You are Kenji, the team lead, in a short team meeting. Ask the new person for a quick self-introduction, then ask a work question they must answer or clarify (deadline, task, problem). Sometimes speak fast so they must ask you to repeat.',cast:{name:'Kenji',skin:0xe3b58f,cloth:0x6b6bd6,pants:0x22263a,hair:0x151515}},
  {k:'boss',time:'16:30',where:'Phòng sếp',name:'Ms. Park',role:'Quản lý — nói chuyện tự do',goal:'You are Ms. Park, the manager. It is the END of their first day. Ask how the day went, what they learned, what was difficult, and about tomorrow.',front:1,cast:{name:'Ms. Park',long:1,skin:0xeac09a,cloth:0x30364f,pants:0x1c1f2e,hair:0x201510,tie:0xd9534f}}
];
var HERO={name:'Bạn',skin:0xf0c8a0,cloth:0xff8a3d,pants:0x2b3a67,hair:0x1c1c24,bag:1};
SLOTS.forEach(function(s,i){s.cx=(i+.5)*W;people[s.k]={userData:{react:null,reactAt:0,bub:null,bubAt:0,fx:[]}};});
var pl={x:0,walk:false,ud:{react:null,reactAt:0,bub:null,bubAt:0,fx:[]}};
var view={over:true,room:0,camX:2.5*W,sc:.5,fy:400};

function skyCols(f){var st=[[0,'#ffcf99','#ffe9c8'],[.35,'#79b8ff','#cfe8ff'],[.65,'#79b8ff','#cfe8ff'],[1,'#ff8f5e','#ffd0a0']],i=0;while(i<st.length-2&&f>st[i+1][0])i++;var a=st[i],b=st[i+1],t=Math.max(0,Math.min(1,(f-a[0])/(b[0]-a[0])));return [lerpHex(a[1],b[1],t),lerpHex(a[2],b[2],t)];}
function skyWin(x,y,w,h,now){
  var sk=skyCols(DAYF);cx.save();cx.beginPath();cx.rect(x,y,w,h);cx.clip();
  var g=cx.createLinearGradient(0,y,0,y+h);g.addColorStop(0,sk[0]);g.addColorStop(1,sk[1]);cx.fillStyle=g;cx.fillRect(x,y,w,h);
  var dim=DAYF>.85?'#7a6a8f':'#9db4cf';
  for(var b=0;b<6;b++){var bw=w/6+6,bh=h*(.25+((b*37)%5)/12);cx.fillStyle=dim;cx.globalAlpha=.75;cx.fillRect(x+b*(w/6)-3,y+h-bh,bw,bh);}
  cx.globalAlpha=.9;var cxp=x+((now/90+x*3)%(w+120))-60;el(cxp,y+h*.28,26,9,'rgba(255,255,255,.85)');el(cxp+16,y+h*.24,18,8,'rgba(255,255,255,.85)');cx.globalAlpha=1;
  cx.restore();
  cx.lineWidth=5;cx.strokeStyle='#7b6a58';cx.strokeRect(x,y,w,h);ln(x+w/2,y,x+w/2,y+h,4,'#7b6a58');ln(x,y+h/2,x+w,y+h/2,3,'#7b6a58');
  rr(x-6,y+h,w+12,7,3,'#a48c72');
  cx.save();cx.globalAlpha=.09;cx.fillStyle=DAYF>.8?'#ffb27a':'#ffffff';cx.beginPath();cx.moveTo(x+6,y+h);cx.lineTo(x+w-6,y+h);cx.lineTo(x+w+70,0);cx.lineTo(x+70,0);cx.closePath();cx.fill();cx.restore();
}
function plant(x,s){s=s||1;cx.save();cx.translate(x,0);rr(-16*s,-30*s,32*s,30*s,6,'#b0703f');for(var i=0;i<6;i++){var a=-1.2+i*.48;cx.save();cx.translate(0,-30*s);cx.rotate(a);el(0,-26*s,8*s,26*s,i%2?'#3f9d54':'#52b566');cx.restore();}cx.restore();}
function frameArt(x,y,w,h,c1,c2){rr(x,y,w,h,4,'#fff','#c9c2b4');rr(x+6,y+6,w-12,h-12,3,c1);el(x+w*.65,y+h*.4,w*.16,w*.16,c2);cx.beginPath();cx.moveTo(x+6,y+h-6);cx.lineTo(x+w*.35,y+h*.5);cx.lineTo(x+w*.55,y+h*.75);cx.lineTo(x+w*.75,y+h*.55);cx.lineTo(x+w-6,y+h-6);cx.closePath();cx.fillStyle='rgba(0,0,0,.18)';cx.fill();}
var WALLS=['#f6e8d6','#e0eaf7','#e6f2e2','#e8e4f5','#f3e4e4'],WAIN=['#d9b98f','#b9c9e0','#b8d4b0','#c6bfe6','#d9b0b0'];
function room(i,layer,now){
  var s=SLOTS[i],x0=i*W;cx.save();cx.translate((i+.5)*W,0);
  if(layer===0){
    rr(-W/2,-WALL,W,WALL,0,WALLS[i]);rr(-W/2,-72,W,72,0,WAIN[i]);ln(-W/2,-72,W/2,-72,4,'rgba(0,0,0,.12)');rr(-W/2,-8,W,8,0,'rgba(0,0,0,.14)');
    if(i>0){rr(-W/2,-WALL,8,WALL,0,'rgba(0,0,0,.10)');}
    if(i===0){
      skyWin(-150,-215,110,110,now);skyWin(60,-215,110,110,now);
      el(0,-170,30,30,'#fff');el(0,-170,25,25,'#4a6bff');txt('NN',0,-169,22,'#fff');txt('NÓI NGHỀ',0,-126,13,'#7a5c3e');
      plant(-165);rr(-120,-84,50,16,4,'#8a6a44');
    }else if(i===1){
      skyWin(-160,-215,120,110,now);frameArt(-20,-215,50,60,'#a8c6ff','#ffd166');frameArt(40,-215,50,60,'#c6f0c6','#ff9e6b');
      rr(70,-120,100,10,3,'#8a6a44');rr(90,-150,18,30,3,'#d9534f');rr(112,-145,16,25,3,'#4a90d9');rr(132,-150,18,30,3,'#59b36b');
      rr(30,-88,130,14,4,'#c9a875');rr(38,-74,10,74,2,'#555b70');rr(142,-74,10,74,2,'#555b70');
      rr(78,-152,64,46,6,'#161b2b');rr(84,-146,52,34,3,'#1f2a44');for(var k=0;k<5;k++)ln(90,-140+k*6,90+16+(k*13)%28,-140+k*6,2.5,['#7ee787','#79c0ff','#ffa657','#d2a8ff','#7ee787'][k]);rr(104,-106,6,18,2,'#555b70');rr(90,-92,34,5,2,'#333a4d');
      rr(-130,-60,50,10,4,'#3c4460');rr(-118,-50,26,50,6,'#3c4460');rr(-124,-110,62,50,10,'#4a5478');
    }else if(i===2){
      skyWin(-40,-215,110,110,now);
      rr(-180,-235,120,70,6,'#f2f2ee','#c9c9c4');rr(-176,-231,56,62,4,'#e4e4df');rr(-116,-231,52,62,4,'#e4e4df');
      rr(-180,-88,175,88,4,'#e7e2d8');rr(-184,-96,183,12,4,'#8a8f9e');rr(-160,-86,60,84,2,'rgba(0,0,0,.05)');
      rr(-70,-132,42,44,6,'#30364f');rr(-64,-124,30,14,3,'#60a5fa');el(-49,-100,4,4,'#ff6b6b');rr(-54,-88,12,4,2,'#fff');
      rr(-150,-102,22,14,3,'#d9534f');rr(115,-200,80,200,8,'#dfe3ee','#b8bdd0');ln(115,-110,195,-110,3,'#b8bdd0');rr(122,-160,5,26,2,'#8a8f9e');rr(122,-96,5,26,2,'#8a8f9e');
    }else if(i===3){
      rr(-90,-225,180,110,8,'#1c2233');rr(-82,-217,164,94,4,'#eaf0ff');
      for(var b=0;b<5;b++){var bh=20+((b*29)%50);rr(-64+b*28,-133-bh,18,bh,3,['#4a90d9','#59b36b','#f59e0b','#d9534f','#9b6bd6'][b]);}
      ln(-70,-135,70,-135,3,'#9aa3c2');
      rr(-160,-80,320,14,6,'#b98a5a');rr(-140,-66,10,66,2,'#7a5c3e');rr(130,-66,10,66,2,'#7a5c3e');
      [-100,-30,40].forEach(function(x){rr(x-22,-56,44,10,4,'#3c4460');rr(x-18,-46,36,46,4,'#4a5478');});
      skyWin(-175,-215,70,90,now);skyWin(105,-215,70,90,now);
    }else{
      skyWin(-80,-235,160,130,now);
      rr(-185,-250,70,250,4,'#6b4a2e');for(var r=0;r<5;r++){ln(-181,-235+r*46,-119,-235+r*46,4,'#8a6a44');for(var b=0;b<4;b++)rr(-176+b*15,-233+r*46-24,11,24,2,['#d9534f','#4a90d9','#59b36b','#f59e0b','#9b6bd6'][(b+r)%5]);}
      frameArt(100,-215,44,58,'#c6d4f0','#f59e0b');frameArt(150,-215,36,50,'#f0d4c6','#9b6bd6');
      plant(165);
    }
  }else{
    if(i===0){rr(10,-78,190,78,8,'#8a6a44');rr(4,-86,202,14,6,'#e0c79a');rr(70,-128,52,42,5,'#222a3d');rr(76,-122,40,30,3,'#60a5fa');el(160,-96,12,6,'#ffd166');rr(20,-70,170,6,3,'rgba(0,0,0,.15)');}
    if(i===4){rr(0,-84,210,84,8,'#5a3d25');rr(-6,-92,222,14,6,'#7a5636');rr(60,-136,60,44,5,'#161b2b');rr(66,-130,48,32,3,'#2a3a66');rr(140,-104,40,12,4,'#fff');rr(150,-96,20,5,2,'#d9534f');}
  }
  cx.restore();
}
function hairBack(o,c){if(o.long){rr(-42,-34,84,96,32,c);}}
function drawChar(o,x,face,now,talk,walk,ud){
  var reduce_=reduce,bob=reduce_?0:(walk?Math.abs(Math.sin(now/110))*5:Math.sin(now/520+x)*1.6);
  var skin=col(o.skin),cloth=col(o.cloth),pants=col(o.pants),hair=col(o.hair);
  cx.save();cx.translate(x,0);
  el(0,2,44,9,'rgba(0,0,0,.22)');
  var sw=walk?Math.sin(now/110)*13:0;
  rr(-26+sw*.5,-64,22,64,9,pants);rr(4-sw*.5,-64,22,64,9,pants);
  rr(-32+sw*.5,-9,30,12,6,'#1b1b22');rr(2-sw*.5,-9,30,12,6,'#1b1b22');
  cx.translate(0,-bob);
  if(o.bag){rr(-32*face-16,-124,32,58,10,'#3b4a7a');}
  rr(-33,-132,66,76,24,cloth);rr(-31,-72,62,18,8,pants);
  if(o.tie){cx.beginPath();cx.moveTo(-9,-130);cx.lineTo(9,-130);cx.lineTo(6,-90);cx.lineTo(0,-82);cx.lineTo(-6,-90);cx.closePath();cx.fillStyle=col(o.tie);cx.fill();}
  else{cx.beginPath();cx.moveTo(-12,-132);cx.lineTo(0,-116);cx.lineTo(12,-132);cx.closePath();cx.fillStyle='rgba(255,255,255,.85)';cx.fill();}
  if(o.bag)ln(-24,-128,18,-66,5,'#2c3760');
  // tay
  var wave=talk&&!reduce_?Math.sin(now/240):0,nod=ud.react==='nod';
  var la=[-36,-118],ra=[36,-118];
  var lh=[-44+wave*6,-64-wave*10],rh=[44,-64];
  if(nod||ud.react==='cheer'){rh=[50,-110-Math.abs(Math.sin(now/120))*14];}
  if(walk){lh=[-40,-64+sw*.7];rh=[40,-64-sw*.7];}
  ln(la[0],la[1],lh[0],lh[1],17,cloth);ln(ra[0],ra[1],rh[0],rh[1],17,cloth);el(lh[0],lh[1]+6,9,9,skin);el(rh[0],rh[1]+6,9,9,skin);
  // đầu
  cx.save();cx.translate(0,-162);
  var rot=0;if(ud.react){var e=(now-ud.reactAt)/800;if(e>1)ud.react=null;else{if(ud.react==='nod')cx.translate(0,Math.sin(e*Math.PI*3)*4*(1-e));else rot=Math.sin(e*Math.PI*4)*.16*(1-e);}}
  rot+=talk&&!reduce_?Math.sin(now/330)*.04:0;cx.rotate(rot);
  hairBack(o,hair);
  el(-36,6,7,8,skin);el(36,6,7,8,skin);
  el(0,0,37,38,skin);
  // tóc
  cx.beginPath();cx.arc(0,-2,40,Math.PI,0);cx.bezierCurveTo(34,-4,16,-20,-4,-14);cx.bezierCurveTo(-18,-10,-32,-6,-40,-2);cx.closePath();cx.fillStyle=hair;cx.fill();
  if(o.long){rr(-42,-8,10,58,5,hair);rr(32,-8,10,58,5,hair);}
  var look=face*2.5,blink=(!reduce_&&(Math.floor(now/1000+x*.01)%4===0)&&(now%1000)<130)?.12:1;
  [-14,14].forEach(function(ex){el(ex,7,9,10*blink,'#fff');if(blink>.5){el(ex+look,8,5.4,6.2,'#1a1a24');el(ex+look-1.8,5.6,1.9,1.9,'#fff');}else ln(ex-7,7,ex+7,7,2,'#222');});
  var hp=ud.react==='shake'?3:(ud.react==='nod'?-2:0);
  ln(-21,-6+hp,-8,-8-hp,3,hair);ln(8,-8-hp,21,-6+hp,3,hair);
  if(o.glasses){cx.lineWidth=2.5;cx.strokeStyle='#2a2a2a';[-14,14].forEach(function(ex){cx.beginPath();cx.arc(ex,7,12.5,0,7);cx.stroke();});ln(-2,6,2,6,2.5,'#2a2a2a');}
  el(-24,19,7.5,4.5,'rgba(255,110,120,.42)');el(24,19,7.5,4.5,'rgba(255,110,120,.42)');
  cx.beginPath();cx.arc(0,15,2.6,0,Math.PI);cx.strokeStyle='rgba(0,0,0,.25)';cx.lineWidth=2;cx.stroke();
  if(talk){var mo=3+5*Math.abs(Math.sin(now/95));el(0,25,7,mo,'#7a2b2b');el(0,25+mo*.45,4.5,mo*.4,'#e0707a');}
  else{cx.beginPath();cx.arc(0,21,8,.15*Math.PI,.85*Math.PI);cx.strokeStyle='#7a2b2b';cx.lineWidth=2.6;cx.lineCap='round';cx.stroke();}
  cx.restore();
  cx.restore();
  // bảng tên + cảm xúc + điểm nổi
  cx.save();cx.translate(x,0);
  cx.font='800 13px system-ui,sans-serif';var tw=cx.measureText(o.name).width+22;rr(-tw/2,-236,tw,22,11,'rgba(20,26,50,.82)');txt(o.name,0,-225,13,'#fff');
  if(ud.bub){var e3=(now-ud.bubAt)/1700;if(e3>1)ud.bub=null;else{cx.globalAlpha=1-Math.max(0,e3-.7)/.3;var by=-262-e3*34;el(28,by,20,20,'#fff');txt(ud.bub,28,by+1,26,'#000','center','400');cx.globalAlpha=1;}}
  ud.fx=(ud.fx||[]).filter(function(f){return now-f.at<1500;});
  ud.fx.forEach(function(f){var e4=(now-f.at)/1500;cx.globalAlpha=1-e4*e4;cx.lineWidth=4;cx.strokeStyle='rgba(0,0,0,.45)';cx.font='900 22px system-ui,sans-serif';cx.textAlign='center';cx.strokeText(f.t,-30,-190-e4*50);txt(f.t,-30,-190-e4*50,22,f.c,'center','900');cx.globalAlpha=1;});
  cx.restore();
}
function emote(k,e){var u=(k==='__me'?pl.ud:people[k].userData);u.bub=e;u.bubAt=performance.now();}
function pop(k,t,c){var u=people[k].userData;u.fx=(u.fx||[]);u.fx.push({t:t,c:c,at:performance.now()});}
function slotX(i){return (i+.5)*W;}
function focusSlot(i){view.over=false;view.room=i;}
function overview(){view.over=true;}
function resetPlayer(){pl.x=slotX(0)-W*.95;}
function setDayTime(f){DAYF=f;}
function resize(){DPR=Math.min(devicePixelRatio||1,2);CW=innerWidth;CH=innerHeight;canvas.width=Math.round(CW*DPR);canvas.height=Math.round(CH*DPR);}
var t0=performance.now(),motes=[];for(var mi=0;mi<16;mi++)motes.push({x:Math.random(),y:Math.random(),s:.5+Math.random()*1.5,p:Math.random()*6});
function frame(now){
  requestAnimationFrame(frame);
  var dt=Math.min(.05,(now-t0)/1000);t0=now;
  var pt=$('#panel'),top=CH-(pt?pt.offsetHeight:200);
  var avail=Math.max(160,top-70),fyT,scT,camT;
  if(view.over||!st.on){scT=Math.min(CW/(W*1.15),avail/290);fyT=70+(avail+WALL*scT)/2;camT=reduce?2.5*W:(2.5*W+Math.sin(now/7000)*1.9*W);}
  else{scT=Math.min(CW/290,avail/290);fyT=70+(avail+WALL*scT)/2+6;camT=slotX(view.room)+20;}
  var k1=1-Math.pow(.004,dt);
  view.fy+=(fyT-view.fy)*k1;view.sc+=(scT-view.sc)*k1;view.camX+=(camT-view.camX)*k1;
  // người chơi đi bộ
  var tx=slotX(view.room)-82;pl.walk=false;
  if(st.on&&!view.over){var d=tx-pl.x;if(Math.abs(d)>3){pl.x+=Math.sign(d)*Math.min(Math.abs(d),(Math.abs(d)>W?520:300)*dt);pl.walk=true;}}
  var sc=view.sc,fy=view.fy;
  cx.setTransform(DPR,0,0,DPR,0,0);
  var g0=cx.createLinearGradient(0,0,0,CH);g0.addColorStop(0,'#232a4a');g0.addColorStop(1,'#141a33');cx.fillStyle=g0;cx.fillRect(0,0,CW,CH);
  cx.save();cx.translate(CW/2-view.camX*sc,fy);cx.scale(sc,sc);
  var vl=view.camX-CW/2/sc,vr=view.camX+CW/2/sc;
  // trần + đèn
  var cg=cx.createLinearGradient(0,-WALL-900,0,-WALL);cg.addColorStop(0,'#1a2040');cg.addColorStop(1,'#3b4272');cx.fillStyle=cg;cx.fillRect(vl-20,-WALL-900,vr-vl+40,900);ln(vl-20,-WALL,vr+20,-WALL,5,'#20264a');
  // sàn
  var fl=cx.createLinearGradient(0,0,0,(CH-fy)/sc);fl.addColorStop(0,'#c9a06a');fl.addColorStop(1,'#a37c4c');cx.fillStyle=fl;cx.fillRect(vl-20,0,vr-vl+40,(CH-fy)/sc+20);
  for(var y=26;y<(CH-fy)/sc;y+=34)ln(vl-20,y,vr+20,y,1.5,'rgba(0,0,0,.10)');
  for(var x=Math.floor(vl/90)*90;x<vr;x+=90){ln(x,0,x+((x-view.camX)*.15),(CH-fy)/sc,1.2,'rgba(0,0,0,.07)');}
  for(var i=0;i<SLOTS.length;i++){if((i+1)*W<vl-20||i*W>vr+20)continue;room(i,0,now);
    cx.save();cx.translate((i+.5)*W,-WALL-2);[-110,110].forEach(function(lx){rr(lx-26,0,52,8,3,'#fff6d6');cx.globalAlpha=.10;cx.fillStyle='#fff6d6';cx.beginPath();cx.moveTo(lx-24,8);cx.lineTo(lx+24,8);cx.lineTo(lx+70,WALL);cx.lineTo(lx-70,WALL);cx.closePath();cx.fill();cx.globalAlpha=1;});cx.restore();}
  var cur=SLOTS[view.room];
  for(var j=0;j<SLOTS.length;j++){var s=SLOTS[j];if((j+1)*W<vl-60||j*W>vr+60)continue;
    var talking=st.on&&now<talkUntil&&SLOTS[st.i]&&SLOTS[st.i].k===s.k;
    drawChar(s.cast,slotX(j)+(s.front?75:72),-1,now,talking,false,people[s.k].userData);
    if(s.front)room(j,1,now);}
  if(st.on&&pl.x)drawChar(HERO,pl.x,1,now,false,pl.walk,pl.ud);
  cx.restore();
  // ánh sáng theo giờ + vignette + bụi sáng
  var tint=DAYF<.25?'rgba(255,190,120,'+(.14*(1-DAYF/.25)).toFixed(3)+')':(DAYF>.6?'rgba(255,110,60,'+(.20*(DAYF-.6)/.4).toFixed(3)+')':'rgba(0,0,0,0)');
  cx.fillStyle=tint;cx.fillRect(0,0,CW,CH);
  var vg=cx.createRadialGradient(CW/2,CH*.4,Math.min(CW,CH)*.35,CW/2,CH*.4,Math.max(CW,CH)*.8);vg.addColorStop(0,'rgba(0,0,0,0)');vg.addColorStop(1,'rgba(8,10,25,.45)');cx.fillStyle=vg;cx.fillRect(0,0,CW,CH);
  if(!reduce){cx.fillStyle='rgba(255,255,255,.35)';motes.forEach(function(m){var mx=((m.x+now/60000*m.s+Math.sin(now/2000+m.p)*.01)%1)*CW,my=(m.y*.6*fy+Math.sin(now/1500+m.p)*8);cx.beginPath();cx.arc(mx,my,m.s,0,7);cx.fill();});}
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
  resetPlayer();st.on=true;st.i=0;st.list=[];st.miss=[];st.good=0;st.total=0;st.done=false;setImp(50);
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
  st.total++;var p=people[s.k].userData;if(o.good)pop(s.k,'+16','#4ade80');else pop(s.k,'-9','#fb7185');p.reactAt=performance.now();
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
function boot(){resize();addEventListener('resize',resize);setDayTime(0);requestAnimationFrame(frame);intro();}
boot();
})();
