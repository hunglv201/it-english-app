/* IT English Quest — game logic (anime RPG × quiz battle × visual novel) */
(function(){
'use strict';
const D=window.DATA, VOCAB=D.vocab, DAYS=D.days, PHASES=D.phaseTitles, LISTEN=D.listen, DIALOGS=D.dialogues, PHR=D.phrases;
const GKEY='it-english-game-v1', APPKEY='it-english-v1';
const $=s=>document.querySelector(s);
const main=$('#main');
function el(tag,cls,html){const e=document.createElement(tag);if(cls)e.className=cls;if(html!=null)e.innerHTML=html;return e;}
function esc(s){return String(s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));}
function rnd(a){return a[Math.floor(Math.random()*a.length)];}
function shuffle(a){a=a.slice();for(let i=a.length-1;i>0;i--){const j=Math.floor(Math.random()*(i+1));[a[i],a[j]]=[a[j],a[i]];}return a;}
function todayStr(){return new Date().toISOString().slice(0,10);}

/* ---------- state ---------- */
function loadG(){try{return JSON.parse(localStorage.getItem(GKEY))||{};}catch(e){return {};}}
function saveG(){try{localStorage.setItem(GKEY,JSON.stringify(G));}catch(e){}}
function loadApp(){try{return JSON.parse(localStorage.getItem(APPKEY))||{};}catch(e){return {};}}
function saveApp(a){try{localStorage.setItem(APPKEY,JSON.stringify(a));}catch(e){}}
let G=Object.assign({name:'Dev',lv:1,xp:0,hp:100,maxHp:100,coins:0,combo:0,bestCombo:0,cleared:{},badges:{},cur:1,ch:null,wins:0,correct:0,total:0,bossWins:0,streak:0,lastDay:null,
  items:{hint:2,potion:1},up:{hp:0,timer:0,combo:0,rate:0,cap:0},idle:{last:Date.now(),bugs:0},daily:{},seenTut:false,sound:true},loadG());
G.items=Object.assign({hint:0,potion:0},G.items||{});G.up=Object.assign({hp:0,timer:0,combo:0,rate:0,cap:0},G.up||{});G.idle=Object.assign({last:Date.now(),bugs:0},G.idle||{});G.daily=G.daily||{};G.talk=Object.assign({equipped:[],shadowBest:0,reflexBest:0,battleWins:0,endings:{}},G.talk||{});
/* ---------- AFK / idle economy ---------- */
function clearedDays(){return Object.keys(G.cleared).filter(n=>dayCleared(+n)).length;}
function equipBonus(){return Math.min(40,(G.talk.equipped||[]).length);}
function idleRate(){return 20+clearedDays()*4+(G.up.rate||0)*12+equipBonus();} // xu mỗi giờ
function idleCapMs(){return (8+(G.up.cap||0)*4)*3600e3;}
function idlePending(){const e=Math.max(0,Math.min(Date.now()-(G.idle.last||Date.now()),idleCapMs()));const coins=Math.floor(e/3600e3*idleRate());return {coins,xp:Math.floor(coins/4),bugs:Math.floor(e/90e3),ms:e,capped:e>=idleCapMs()};}
function fmtDur(ms){const h=Math.floor(ms/3600e3),m=Math.floor(ms%3600e3/60e3);return h?h+' giờ '+m+' phút':m+' phút';}
function collectIdle(){const p=idlePending();G.idle.last=Date.now();G.idle.bugs=(G.idle.bugs||0)+p.bugs;if(p.coins>0){gainXp(p.xp,p.coins);toast('🪙 +'+p.coins+' xu · ✨ +'+p.xp+' XP');}saveG();}
function daily(){const t=todayStr();if(G.daily.date!==t){G.daily={date:t,wins:0,combo:0,boss:0,claimed:{},chest:false};saveG();}return G.daily;}
const DQ=[['wins','Thắng 3 trận Bug',3,60,'⚔️'],['combo','Đạt combo x5 trong trận',5,40,'🔥'],['boss','Hạ 1 Boss',1,100,'👑']];
const SHOP=[
 ['hp','❤️','Máu tối đa +10','Chịu đòn tốt hơn',k=>100+k*80,99,()=>{G.maxHp+=10;G.hp=Math.min(G.maxHp,G.hp+10);}],
 ['timer','⏱️','Thêm 2 giây trả lời','Mỗi câu có thêm thời gian',k=>150+k*120,5,null],
 ['combo','🔥','Combo +10% XP','XP mỗi câu đúng tăng theo combo',k=>200+k*150,5,null],
 ['rate','🌙','Mochi cày nhanh hơn','+12 xu/giờ khi AFK',k=>120+k*100,99,null],
 ['cap','⏰','Giới hạn offline +4 giờ','Tích xu lâu hơn khi vắng',k=>300+k*250,4,null],
 ['hint','💡','Gợi ý ×1','Loại 1 đáp án sai trong trận',k=>40,999,()=>{G.items.hint++;}],
 ['potion','🧪','Bình máu ×1','Hồi 50 HP giữa trận',k=>80,999,()=>{G.items.potion++;}]
];
// bootstrap từ tiến trình app cũ (ngày đang học)
(function(){const a=loadApp();if(a.days&&a.days.cur&&a.days.cur>G.cur&&!Object.keys(G.cleared).length){G.cur=a.days.cur;}})();
if(G.ch==null)G.ch=DAYS[G.cur-1]?DAYS[G.cur-1].phase:0;
function xpNeed(lv){return 100+(lv-1)*60;}
function dayInfo(n){return DAYS[n-1];}
function dayCleared(n){const c=G.cleared[n];return !!(c&&c.v&&c.p&&c.l);}
function touchStreak(){const t=todayStr();if(G.lastDay===t)return;const y=new Date(Date.now()-864e5).toISOString().slice(0,10);G.streak=(G.lastDay===y)?(G.streak||0)+1:1;G.lastDay=t;}
function syncApp(n){ // đồng bộ "xong ngày" sang app cũ
  try{const a=loadApp();a.days=a.days||{done:{},cur:1};a.days.done=a.days.done||{};a.days.done[n]=1;if((a.days.cur||1)<=n)a.days.cur=n+1;saveApp(a);}catch(e){}
}

/* ---------- art (original chibi characters, SVG) ---------- */
function mascot(expr){ // Mochi — bạn đồng hành
  expr=expr||'happy';
  const eyes={
    happy:'<ellipse cx="38" cy="52" rx="7" ry="9" fill="#fff"/><ellipse cx="62" cy="52" rx="7" ry="9" fill="#fff"/><circle cx="39" cy="54" r="4.5" fill="#5b3fd6"/><circle cx="63" cy="54" r="4.5" fill="#5b3fd6"/><circle cx="41" cy="51" r="1.8" fill="#fff"/><circle cx="65" cy="51" r="1.8" fill="#fff"/>',
    cheer:'<path d="M31 53q7-8 14 0" stroke="#3b2a8f" stroke-width="3.5" fill="none" stroke-linecap="round"/><path d="M55 53q7-8 14 0" stroke="#3b2a8f" stroke-width="3.5" fill="none" stroke-linecap="round"/>',
    sad:'<ellipse cx="38" cy="53" rx="7" ry="8" fill="#fff"/><ellipse cx="62" cy="53" rx="7" ry="8" fill="#fff"/><circle cx="38" cy="56" r="4.2" fill="#5b3fd6"/><circle cx="62" cy="56" r="4.2" fill="#5b3fd6"/><path d="M30 44l12 4M70 44l-12 4" stroke="#3b2a8f" stroke-width="3" stroke-linecap="round"/><ellipse cx="68" cy="62" rx="2.2" ry="4" fill="#8ad9ff"/>',
    think:'<ellipse cx="38" cy="52" rx="7" ry="9" fill="#fff"/><ellipse cx="62" cy="52" rx="7" ry="9" fill="#fff"/><circle cx="41" cy="50" r="4.5" fill="#5b3fd6"/><circle cx="65" cy="50" r="4.5" fill="#5b3fd6"/><path d="M30 42q8-4 14 0" stroke="#3b2a8f" stroke-width="3" fill="none" stroke-linecap="round"/>',
    wink:'<ellipse cx="38" cy="52" rx="7" ry="9" fill="#fff"/><circle cx="39" cy="54" r="4.5" fill="#5b3fd6"/><circle cx="41" cy="51" r="1.8" fill="#fff"/><path d="M55 53q7-7 14 0" stroke="#3b2a8f" stroke-width="3.5" fill="none" stroke-linecap="round"/>'
  }[expr]||'';
  const mouth={happy:'<path d="M42 66q8 7 16 0" stroke="#c2405f" stroke-width="3" fill="none" stroke-linecap="round"/>',
    cheer:'<path d="M40 64q10 12 20 0z" fill="#c2405f"/><path d="M44 66q6 4 12 0" fill="#ff9bb8"/>',
    sad:'<path d="M42 70q8-6 16 0" stroke="#c2405f" stroke-width="3" fill="none" stroke-linecap="round"/>',
    think:'<path d="M44 68h12" stroke="#c2405f" stroke-width="3" stroke-linecap="round"/>',
    wink:'<path d="M42 66q8 8 16 0" stroke="#c2405f" stroke-width="3" fill="none" stroke-linecap="round"/>'}[expr]||'';
  return '<svg viewBox="0 0 100 110" xmlns="http://www.w3.org/2000/svg">'+
    '<path d="M22 96q28-16 56 0v12H22z" fill="#7c5cff" stroke="#0d0826" stroke-width="3"/>'+ // hoodie
    '<path d="M18 52q0-30 32-30t32 30q0 8-4 12H22q-4-4-4-12z" fill="#5ee0d8" stroke="#0d0826" stroke-width="3"/>'+ // hair back
    '<circle cx="50" cy="56" r="27" fill="#ffe3cf" stroke="#0d0826" stroke-width="3"/>'+ // face
    '<path d="M24 50q6-22 26-22t26 22q-6-8-14-9-6 6-12 0-6 9-14 9-6-2-12 0z" fill="#5ee0d8" stroke="#0d0826" stroke-width="3" stroke-linejoin="round"/>'+ // bangs
    '<path d="M18 52q-6 22 6 34l6-8q-6-10-4-24z M82 52q6 22-6 34l-6-8q6-10 4-24z" fill="#ff7eb6" stroke="#0d0826" stroke-width="3"/>'+ // side hair pink
    '<path d="M22 44q28-14 56 0" stroke="#0d0826" stroke-width="4" fill="none"/><rect x="14" y="44" width="10" height="16" rx="4" fill="#ff7eb6" stroke="#0d0826" stroke-width="3"/><rect x="76" y="44" width="10" height="16" rx="4" fill="#ff7eb6" stroke="#0d0826" stroke-width="3"/>'+ // headset
    eyes+'<circle cx="30" cy="63" r="4" fill="#ffb1c8" opacity=".8"/><circle cx="70" cy="63" r="4" fill="#ffb1c8" opacity=".8"/>'+mouth+'</svg>';
}
function bug(state){ // quái Bug
  const eyes=state==='dead'?'<path d="M40 44l8 8M48 44l-8 8M62 44l8 8M70 44l-8 8" stroke="#0d0826" stroke-width="4" stroke-linecap="round"/>':
    '<ellipse cx="44" cy="48" rx="8" ry="9" fill="#fff"/><ellipse cx="66" cy="48" rx="8" ry="9" fill="#fff"/><circle cx="46" cy="50" r="4.5" fill="#0d0826"/><circle cx="68" cy="50" r="4.5" fill="#0d0826"/><path d="M34 38l14 6M76 38l-14 6" stroke="#0d0826" stroke-width="4" stroke-linecap="round"/>';
  const mouth=state==='dead'?'<path d="M46 68q9-6 18 0" stroke="#0d0826" stroke-width="3.5" fill="none" stroke-linecap="round"/>':'<path d="M44 66q11 10 22 0z" fill="#3a0f2a"/><path d="M48 66l4 5 4-5 4 5 4-5" fill="#fff"/>';
  return '<svg viewBox="0 0 110 100" xmlns="http://www.w3.org/2000/svg">'+
    '<path d="M30 18q-8-14-2-16 6 0 10 12M80 18q8-14 2-16-6 0-10 12" stroke="#0d0826" stroke-width="4" fill="none" stroke-linecap="round"/>'+
    '<path d="M12 70q-12 4-8 14M98 70q12 4 8 14M18 84q-10 6-4 14M92 84q10 6 4 14" stroke="#0d0826" stroke-width="4" fill="none" stroke-linecap="round"/>'+
    '<ellipse cx="55" cy="58" rx="42" ry="38" fill="#8be36b" stroke="#0d0826" stroke-width="3.5"/>'+
    '<circle cx="30" cy="70" r="6" fill="#4caf50"/><circle cx="82" cy="72" r="7" fill="#4caf50"/><circle cx="55" cy="86" r="5" fill="#4caf50"/><circle cx="28" cy="50" r="4" fill="#4caf50"/>'+
    eyes+mouth+'</svg>';
}
function senpai(mood){ // Minh-senpai — đồng nghiệp/boss
  const mouth=mood==='angry'?'<path d="M42 70q8-5 16 0" stroke="#7a2e2e" stroke-width="3" fill="none" stroke-linecap="round"/>':mood==='glad'?'<path d="M40 66q10 10 20 0z" fill="#7a2e2e"/>':'<path d="M42 68q8 5 16 0" stroke="#7a2e2e" stroke-width="3" fill="none" stroke-linecap="round"/>';
  const brow=mood==='angry'?'<path d="M28 42l14 4M72 42l-14 4" stroke="#0d0826" stroke-width="3.5" stroke-linecap="round"/>':'<path d="M28 44q7-4 14-1M72 44q-7-4-14-1" stroke="#0d0826" stroke-width="3.5" fill="none" stroke-linecap="round"/>';
  return '<svg viewBox="0 0 100 110" xmlns="http://www.w3.org/2000/svg">'+
    '<path d="M18 110V96q32-18 64 0v14z" fill="#f4f6ff" stroke="#0d0826" stroke-width="3"/><path d="M44 96l6 14 6-14" fill="#2f9cff" stroke="#0d0826" stroke-width="2.5"/><path d="M50 96v14" stroke="#ffd166" stroke-width="3"/>'+ // shirt + lanyard
    '<circle cx="50" cy="56" r="27" fill="#ffe3cf" stroke="#0d0826" stroke-width="3"/>'+
    '<path d="M22 50q2-26 28-26t28 26q-4-10-12-12-4 5-9 1-5 7-13 6-6-2-12 0-6 2-10 5z" fill="#2b2a55" stroke="#0d0826" stroke-width="3" stroke-linejoin="round"/>'+
    '<rect x="27" y="47" width="18" height="13" rx="6" fill="#dff3ff88" stroke="#0d0826" stroke-width="3"/><rect x="55" y="47" width="18" height="13" rx="6" fill="#dff3ff88" stroke="#0d0826" stroke-width="3"/><path d="M45 53h10M22 52l5 0M73 52l5 0" stroke="#0d0826" stroke-width="3"/>'+ // glasses
    '<circle cx="36" cy="54" r="3.5" fill="#0d0826"/><circle cx="64" cy="54" r="3.5" fill="#0d0826"/>'+brow+mouth+'</svg>';
}

/* ---------- ui helpers ---------- */
let toastT;function toast(m){const t=$('#toast');t.textContent=m;t.classList.add('show');clearTimeout(toastT);toastT=setTimeout(()=>t.classList.remove('show'),1700);}
function openModal(build){closeModal();const b=el('div','mback');b.id='mback';const m=el('div','card modal pop');b.appendChild(m);document.body.appendChild(b);build(m,closeModal);}
function closeModal(){const b=$('#mback');if(b)b.remove();}
function fxText(x,y,txt,cls){const f=el('div','dmg'+(cls?' '+cls:''),txt);f.style.left=x+'px';f.style.top=y+'px';f.style.transform='translateX(-50%)';$('#fx').appendChild(f);setTimeout(()=>f.remove(),950);}
function flashRed(){const f=$('#flash');f.classList.remove('on');void f.offsetWidth;f.classList.add('on');}
function confetti(){const w=el('div','confetti');w.style.cssText='position:fixed;inset:0;pointer-events:none;z-index:55';const cols=['#ff7eb6','#5ec8ff','#ffd166','#5eead4','#a78bfa','#7cf29a'];for(let i=0;i<60;i++){const p=el('i');p.style.left=Math.random()*100+'vw';p.style.background=rnd(cols);p.style.animationDuration=(1.6+Math.random()*1.4)+'s';p.style.animationDelay=(Math.random()*.4)+'s';w.appendChild(p);}document.body.appendChild(w);setTimeout(()=>w.remove(),3400);}
function petals(){const w=$('#petals');for(let i=0;i<12;i++){const p=el('i','petal');p.style.left=Math.random()*100+'vw';p.style.animationDuration=(9+Math.random()*9)+'s';p.style.animationDelay=(-Math.random()*14)+'s';p.style.transform='scale('+(.6+Math.random())+')';w.appendChild(p);}}
petals();
/* sfx */
let AC=null;function beep(f,d,type,v){if(G.sound===false)return;try{AC=AC||new (window.AudioContext||window.webkitAudioContext)();const o=AC.createOscillator(),g=AC.createGain();o.type=type||'sine';o.frequency.value=f;g.gain.value=v||.05;o.connect(g);g.connect(AC.destination);const t=AC.currentTime;g.gain.setValueAtTime(g.gain.value,t);g.gain.exponentialRampToValueAtTime(.0001,t+d);o.start(t);o.stop(t+d);}catch(e){}}
const sfx={ok(){beep(660,.12,'triangle');setTimeout(()=>beep(880,.16,'triangle'),90);},bad(){beep(160,.28,'sawtooth',.04);},win(){[523,659,784,1046].forEach((f,i)=>setTimeout(()=>beep(f,.22,'triangle',.06),i*110));},hit(){beep(240,.1,'square',.03);},lv(){[784,988,1175,1568].forEach((f,i)=>setTimeout(()=>beep(f,.26,'sine',.06),i*120));}};
/* tts */
let VOICE=null;function pickVoice(){try{const vs=speechSynthesis.getVoices();VOICE=vs.find(v=>/^en/i.test(v.lang)&&/google|natural|samantha|daniel|libby|sonia/i.test(v.name))||vs.find(v=>/^en/i.test(v.lang))||null;}catch(e){}}
if('speechSynthesis'in window){pickVoice();speechSynthesis.onvoiceschanged=pickVoice;}
function speak(t){if(!('speechSynthesis'in window))return;try{speechSynthesis.cancel();const u=new SpeechSynthesisUtterance(String(t).replace(/<[^>]+>/g,''));u.lang='en-US';u.rate=.95;if(VOICE)u.voice=VOICE;speechSynthesis.speak(u);}catch(e){}}

/* ---------- progression ---------- */
function gainXp(n,coins){G.xp+=n;G.coins+=(coins||0);let ups=0;while(G.xp>=xpNeed(G.lv)){G.xp-=xpNeed(G.lv);G.lv++;G.maxHp+=10;G.hp=G.maxHp;ups++;}saveG();paintCoins();if(ups)levelUp();}
function levelUp(){sfx.lv();confetti();openModal((m,close)=>{m.innerHTML='<div class="lvup">LEVEL UP!</div><div class="big" style="margin-top:6px">Lv '+G.lv+'</div><div class="mascot-row" style="margin-top:14px"><div class="mascot">'+mascot('cheer')+'</div><div class="bubble grow"><span class="who">Mochi</span>Tuyệt vời! HP tối đa +10 và hồi đầy máu. Tiến lên nào!</div></div>';const b=el('button','btn yellow block','Tiếp tục');b.style.marginTop='14px';b.onclick=close;m.appendChild(b);});}
const BADGES=[
 ['first','🐛','Bug đầu tiên',g=>g.wins>=1],['ten','⚔️','10 trận thắng',g=>g.wins>=10],['combo5','🔥','Combo x5',g=>g.bestCombo>=5],['combo10','💥','Combo x10',g=>g.bestCombo>=10],
 ['day1','🗓️','Xong 1 ngày',g=>Object.keys(g.cleared).some(n=>dayCleared(+n))],['day7','📅','Xong 7 ngày',g=>Object.keys(g.cleared).filter(n=>dayCleared(+n)).length>=7],
 ['boss','👑','Hạ boss',g=>g.bossWins>=1],['boss5','🏆','Hạ 5 boss',g=>g.bossWins>=5],['lv5','⭐','Đạt Lv 5',g=>g.lv>=5],['lv10','🌟','Đạt Lv 10',g=>g.lv>=10],
 ['acc','🎯','200 câu đúng',g=>g.correct>=200],['streak3','🔥','Chuỗi 3 ngày',g=>g.streak>=3]
];
function checkBadges(){let n=[];BADGES.forEach(b=>{if(!G.badges[b[0]]&&b[3](G)){G.badges[b[0]]=todayStr();n.push(b);}});if(n.length){saveG();n.forEach((b,i)=>setTimeout(()=>toast(b[1]+' Huy hiệu mới: '+b[2]),i*900));}}
function paintCoins(){$('#coinN').textContent=G.coins;}

/* ---------- router ---------- */
let cur='map';
const TABS=[['map','🗺️','Bản đồ'],['talk','🎙️','Nói'],['shop','🛒','Shop'],['profile','👤','Hồ sơ']];
const APP_URL='https://hunglv201.github.io/it-english-app/';
function openApp(){if(/github\.io$/.test(location.hostname))location.href=APP_URL;else window.open(APP_URL,'_blank','noopener');}
function renderTabs(){const n=$('#tabs');n.innerHTML='';TABS.forEach(t=>{const b=el('button','tab'+(cur===t[0]?' on':''),'<span>'+t[1]+'</span>'+t[2]);b.onclick=()=>go(t[0]);n.appendChild(b);});}
let mapTimer=null;
function go(k){document.body.classList.remove('infight');cur=k;renderTabs();window.scrollTo(0,0);if(mapTimer){clearInterval(mapTimer);mapTimer=null;}stopSR();({map:vMap,talk:vTalk,shop:vShop,profile:vProfile})[k]();}
/* ---------- speech recognition + word matching ---------- */
let SRcur=null;
function stopSR(){try{if(SRcur){SRcur.onend=null;SRcur.stop();}}catch(e){}SRcur=null;}
function hasSR(){return !!(window.SpeechRecognition||window.webkitSpeechRecognition);}
function listenOnce(onResult,onEnd,ms){const SR=window.SpeechRecognition||window.webkitSpeechRecognition;if(!SR){onEnd&&onEnd('nosr');return null;}stopSR();const r=new SR();SRcur=r;r.lang='en-US';r.interimResults=false;r.maxAlternatives=1;let got=false;
  r.onresult=e=>{got=true;const t=e.results[0][0].transcript;onResult&&onResult(t);};r.onerror=()=>{};r.onend=()=>{SRcur=null;onEnd&&onEnd(got?'ok':'empty');};
  try{r.start();}catch(e){onEnd&&onEnd('err');return null;}
  if(ms)setTimeout(()=>{try{if(SRcur===r)r.stop();}catch(e){}},ms);return r;}
function normW(s){return String(s).toLowerCase().replace(/<[^>]+>/g,'').replace(/[^a-z0-9' ]+/g,' ').split(/\s+/).filter(Boolean);}
function matchWords(target,heard){const T=normW(target),H=normW(heard);let j=0;const res=T.map(w=>{const k=H.indexOf(w,j);if(k>=0){j=k+1;return true;}return false;});return {words:T,res,pct:T.length?Math.round(res.filter(Boolean).length/T.length*100):0};}
const STOP=new Set('i you he she it we they the a an to of in on at for and or but is are am was were be been do did does have has had will would can could should my your our this that yes no not'.split(' '));
function keywordScore(heard,sample){const H=new Set(normW(heard));const K=normW(sample).filter(w=>!STOP.has(w)&&w.length>2);const hit=K.filter(w=>H.has(w)).length;const n=normW(heard).length;let s=n>=4?4:n>=2?2:n?1:0;s+=Math.min(6,hit*2);return Math.min(10,s);}
/* ---------- NPC cast ---------- */
const CAST={minh:{name:'Minh-senpai',role:'Senior dev',hair:'#2b2a55',glasses:true,shirt:'#f4f6ff',acc:'lanyard'},linh:{name:'Linh',role:'PM',hair:'#c46b8a',glasses:false,shirt:'#ffd7e6',acc:'bun'},an:{name:'An',role:'QA',hair:'#3fbf8f',glasses:false,shirt:'#d9f6ff',acc:'band'}};
function npc(who,mood){const c=CAST[who]||CAST.minh;
  const mouth=mood==='angry'?'<path d="M42 70q8-5 16 0" stroke="#7a2e2e" stroke-width="3" fill="none" stroke-linecap="round"/>':mood==='glad'?'<path d="M40 66q10 10 20 0z" fill="#7a2e2e"/>':'<path d="M42 68q8 5 16 0" stroke="#7a2e2e" stroke-width="3" fill="none" stroke-linecap="round"/>';
  const brow=mood==='angry'?'<path d="M28 42l14 4M72 42l-14 4" stroke="#0d0826" stroke-width="3.5" stroke-linecap="round"/>':'<path d="M28 44q7-4 14-1M72 44q-7-4-14-1" stroke="#0d0826" stroke-width="3.5" fill="none" stroke-linecap="round"/>';
  const eyes=c.glasses?'<rect x="27" y="47" width="18" height="13" rx="6" fill="#dff3ff88" stroke="#0d0826" stroke-width="3"/><rect x="55" y="47" width="18" height="13" rx="6" fill="#dff3ff88" stroke="#0d0826" stroke-width="3"/><path d="M45 53h10M22 52l5 0M73 52l5 0" stroke="#0d0826" stroke-width="3"/><circle cx="36" cy="54" r="3.5" fill="#0d0826"/><circle cx="64" cy="54" r="3.5" fill="#0d0826"/>'
    :'<ellipse cx="37" cy="54" rx="6" ry="7.5" fill="#fff"/><ellipse cx="63" cy="54" rx="6" ry="7.5" fill="#fff"/><circle cx="38" cy="56" r="4" fill="#3b2a8f"/><circle cx="64" cy="56" r="4" fill="#3b2a8f"/><circle cx="40" cy="53" r="1.5" fill="#fff"/><circle cx="66" cy="53" r="1.5" fill="#fff"/>';
  const acc=c.acc==='bun'?'<circle cx="74" cy="30" r="9" fill="'+c.hair+'" stroke="#0d0826" stroke-width="3"/>':c.acc==='band'?'<path d="M24 46q26-12 52 0" stroke="#ff7eb6" stroke-width="5" fill="none" stroke-linecap="round"/>':'<path d="M44 96l6 14 6-14" fill="#2f9cff" stroke="#0d0826" stroke-width="2.5"/><path d="M50 96v14" stroke="#ffd166" stroke-width="3"/>';
  const hairBack=c.acc==='bun'?'<path d="M20 60q-4 26 10 40h40q14-14 10-40z" fill="'+c.hair+'" stroke="#0d0826" stroke-width="3"/>':'';
  return '<svg viewBox="0 0 100 110" xmlns="http://www.w3.org/2000/svg">'+hairBack+'<path d="M18 110V96q32-18 64 0v14z" fill="'+c.shirt+'" stroke="#0d0826" stroke-width="3"/>'+(c.acc==='lanyard'?acc:'')+
    '<circle cx="50" cy="56" r="27" fill="#ffe3cf" stroke="#0d0826" stroke-width="3"/>'+
    '<path d="M22 50q2-26 28-26t28 26q-4-10-12-12-4 5-9 1-5 7-13 6-6-2-12 0-6 2-10 5z" fill="'+c.hair+'" stroke="#0d0826" stroke-width="3" stroke-linejoin="round"/>'+(c.acc!=='lanyard'?acc:'')+eyes+brow+mouth+'</svg>';}
function playerCard(){
  const c=el('div','card player');
  c.innerHTML='<div class="avatar">'+mascot(G.hp<=30?'sad':'happy')+'</div><div class="grow stat"><div class="row between"><b class="h" style="font-size:17px">'+esc(G.name)+'</b><span class="lv">Lv '+G.lv+'</span></div>'+
    '<small>HP '+G.hp+'/'+G.maxHp+'</small><div class="bar hp'+(G.hp<=30?' low':'')+'"><i style="width:'+Math.round(G.hp/G.maxHp*100)+'%"></i></div>'+
    '<small>XP '+G.xp+'/'+xpNeed(G.lv)+' · 🔥 chuỗi '+(G.streak||0)+' ngày</small><div class="bar xp"><i style="width:'+Math.round(G.xp/xpNeed(G.lv)*100)+'%"></i></div></div>';
  return c;
}

/* ---------- MAP (mobile-first) ---------- */
const TIPS=['Đánh vài con Bug từ vựng lấy XP nhé!','Combo càng cao, XP và xu càng nhiều!','Hạ Boss bằng cách chọn đúng câu trả lời!','Sai câu nào mất HP đó — cẩn thận!','Hết HP thì nghỉ chút, HP hồi 50% khi chơi lại.','Xong đủ 3 quest là mở ngày tiếp theo!','Ghé tab Nói để luyện mic — nói thật mới lên trình!'];
function hud(){
  const h=el('div','hud');
  h.innerHTML='<div class="avatar sm">'+mascot(G.hp<=30?'sad':'happy')+'</div><div class="grow"><div class="row" style="gap:6px"><b class="h" style="font-size:15px">'+esc(G.name)+'</b><span class="lv">Lv '+G.lv+'</span><span class="kbd" style="margin-left:auto">🔥 '+(G.streak||0)+'</span></div>'+
    '<div class="row" style="gap:6px;margin-top:5px"><div class="bar hp mini grow'+(G.hp<=30?' low':'')+'"><i style="width:'+Math.round(G.hp/G.maxHp*100)+'%"></i></div><div class="bar xp mini grow"><i style="width:'+Math.round(G.xp/xpNeed(G.lv)*100)+'%"></i></div></div>'+
    '<div class="row between" style="margin-top:2px"><small class="mono">HP '+G.hp+'/'+G.maxHp+'</small><small class="mono">XP '+G.xp+'/'+xpNeed(G.lv)+'</small></div></div>';
  h.onclick=()=>go('profile');return h;
}
const QI={v:['📘','Từ vựng','#5ec8ff'],p:['💬','Ngữ pháp','#a78bfa'],l:['🎧','Nghe','#5eead4'],b:['👑','Boss','#ffd166']};
function vMap(){
  main.innerHTML='';touchStreak();saveG();
  main.appendChild(hud());
  // ---- Chơi tiếp ----
  const d=dayInfo(G.cur),st=G.cleared[G.cur]||{};
  const play=el('div','card play');
  play.innerHTML='<div class="row between"><div><div class="eyebrow">Chơi tiếp · ngày '+G.cur+'</div><b class="h" style="font-size:18px;line-height:1.15">'+esc(d.title)+'</b></div><div class="mascot xs">'+mascot('wink')+'</div></div>';
  const chips=el('div','qchips');
  ['v','p','l','b'].forEach(k=>{const c=el('button','qchip'+(st[k]?' done':''));c.style.setProperty('--c',QI[k][2]);c.innerHTML='<span class="ic">'+QI[k][0]+'</span><span>'+QI[k][1]+'</span><small>'+(st[k]?'★'.repeat(st[k]):'—')+'</small>';c.onclick=()=>{k==='b'?bossStart(G.cur):battleStart(G.cur,k);};chips.appendChild(c);});
  play.appendChild(chips);
  play.appendChild(el('div','tipline','💬 '+esc(rnd(TIPS))));
  main.appendChild(play);
  // ---- AFK strip ----
  const p0=idlePending();
  const afk=el('div','strip afk');
  afk.innerHTML='<div class="mini-farm">'+mascot('happy')+bug()+'</div><div class="grow"><b class="h" style="font-size:14px">AFK · +'+idleRate()+' xu/giờ</b><div class="mono" id="afkLine">🪙 <b id="afkCoins">'+p0.coins+'</b> · ✨ <span id="afkXp">'+p0.xp+'</span> XP · <span id="afkTime">'+fmtDur(p0.ms)+'</span></div></div>';
  const col=el('button','btn yellow sm','Thu');col.id='afkCollect';col.onclick=e=>{e.stopPropagation();const p=idlePending();if(p.coins<=0){toast('Chưa có gì để thu — chờ Mochi cày thêm nhé');return;}collectIdle();confetti();vMap();};
  afk.appendChild(col);afk.onclick=afkSheet;main.appendChild(afk);
  function paintAfk(){const p=idlePending();const a=$('#afkCoins'),x=$('#afkXp'),t=$('#afkTime');if(!a)return;a.textContent=p.coins;x.textContent=p.xp;t.textContent=p.capped?'⚠️ đầy túi':fmtDur(p.ms);}
  mapTimer=setInterval(paintAfk,1000);
  // ---- Daily strip ----
  const dl=daily();const qdone=DQ.filter(q=>(dl[q[0]]||0)>=q[2]).length,qclaim=DQ.filter(q=>dl.claimed[q[0]]).length;const hasNew=(!dl.chest)||(qdone>qclaim);
  const ds=el('button','strip daily'+(hasNew?' new':''));
  ds.innerHTML='<span class="qi">🎁</span><span class="grow"><b class="h" style="font-size:14px">Hằng ngày</b><div class="mono">'+(dl.chest?'rương đã mở':'<span style="color:var(--yellow)">rương chưa mở</span>')+' · nhiệm vụ '+qclaim+'/'+DQ.length+'</div></span><span class="sc">›</span>';
  ds.onclick=dailySheet;main.appendChild(ds);
  // ---- Bản đồ chặng ----
  const c=el('div','card map');
  const ch=G.ch;const days=DAYS.filter(x=>x.phase===ch);
  const head=el('div','chapter');
  const prev=el('button','nav','‹');prev.disabled=ch<=0;prev.onclick=()=>{G.ch=Math.max(0,ch-1);saveG();vMap();};
  const next=el('button','nav','›');next.disabled=ch>=PHASES.length-1;next.onclick=()=>{G.ch=Math.min(PHASES.length-1,ch+1);saveG();vMap();};
  const t=el('div','grow','<div class="eyebrow">Chặng '+(ch+1)+'/'+PHASES.length+'</div><div class="h" style="font-size:16px;line-height:1.15">'+esc(PHASES[ch])+'</div>');t.style.textAlign='center';
  head.appendChild(prev);head.appendChild(t);head.appendChild(next);c.appendChild(head);
  const path=el('div','path');
  days.forEach(x=>{const n=x.n;const s2=G.cleared[n]||{};const done=dayCleared(n);
    const b=el('button','node'+(done?' done':n===G.cur?' cur':n<G.cur?' open':' lock'),String(n));
    if(n>G.cur)b.innerHTML+='<span class="lk">🔒</span>';
    const stars=(s2.v||0)+(s2.p||0)+(s2.l||0)+(s2.b||0);if(stars)b.innerHTML+='<span class="st">'+'★'.repeat(Math.min(3,Math.ceil(stars/4)))+'</span>';
    b.onclick=()=>{if(n>G.cur){toast('🔒 Xong ngày '+G.cur+' để mở');return;}questSelect(n);};
    path.appendChild(b);
  });
  c.appendChild(path);
  if(dayInfo(G.cur).phase!==ch){const j=el('button','btn ghost sm block','🎯 Về chặng hiện tại');j.style.marginTop='8px';j.onclick=()=>{G.ch=dayInfo(G.cur).phase;saveG();vMap();};c.appendChild(j);}
  main.appendChild(c);
}
function afkSheet(){
  openModal((m,close)=>{const p=idlePending();
    m.innerHTML='<div class="eyebrow">AFK · Mochi tự cày</div><b class="h" style="font-size:18px">+'+idleRate()+' xu/giờ · tối đa '+Math.round(idleCapMs()/3600e3)+' giờ offline</b>'+
      '<div class="farm"><div class="fm">'+mascot('happy')+'</div><div class="fx-hit go" id="farmHit">⚔️</div><div class="fb">'+bug()+'</div>'+(G.talk.equipped.length?'<div class="fsay">“'+esc(rnd(G.talk.equipped))+'”</div>':'')+'</div>'+
      '<div class="row between" style="margin-top:10px"><div><div class="h" style="font-size:24px;color:var(--yellow)">🪙 '+p.coins+' <small style="font-size:12px;color:var(--muted)">· ✨ '+p.xp+' XP</small></div><small class="muted">'+(p.capped?'⚠️ đầy túi — thu hoạch đi!':'đã cày '+fmtDur(p.ms))+' · 🐛 '+(G.idle.bugs||0)+' bug tổng</small></div></div>'+
      '<p class="muted" style="font-size:13px;margin-top:10px">Cày nhanh hơn: xong thêm ngày (+4/giờ), nâng cấp ở Shop (+12/giờ), trang bị câu ở tab Nói (+1/giờ mỗi câu).</p>';
    const r=el('div','row');r.style.cssText='gap:10px;margin-top:12px';const k=el('button','btn ghost grow','Đóng');k.onclick=close;const c=el('button','btn yellow grow','Thu hoạch');c.disabled=p.coins<=0;c.onclick=()=>{close();collectIdle();confetti();vMap();};r.appendChild(k);r.appendChild(c);m.appendChild(r);});
}
function dailySheet(){
  openModal((m,close)=>{const dl=daily();
    m.innerHTML='<div class="eyebrow">Hằng ngày</div><b class="h" style="font-size:18px">Rương đăng nhập · chuỗi '+(G.streak||0)+' ngày</b>';
    const chest=el('button','btn '+(dl.chest?'ghost':'violet')+' block',dl.chest?'✅ Đã nhận hôm nay':'🎁 Mở rương ('+(50+(G.streak||0)*10)+' xu + 💡)');chest.style.marginTop='10px';chest.disabled=!!dl.chest;
    chest.onclick=()=>{const d=daily();if(d.chest)return;d.chest=true;const c=50+(G.streak||0)*10;G.items.hint++;let extra='';if((G.streak||0)%3===0){G.items.potion++;extra=' + 🧪';}gainXp(20,c);saveG();confetti();sfx.win();toast('🎁 +'+c+' xu + 💡'+extra);close();dailySheet();};
    m.appendChild(chest);
    const ql=el('div');ql.style.cssText='display:flex;flex-direction:column;gap:8px;margin-top:12px';
    DQ.forEach(q=>{const v=Math.min(dl[q[0]]||0,q[2]);const done=v>=q[2];const cl=dl.claimed[q[0]];const r=el('div','dq'+(done?' done':''));
      r.innerHTML='<span class="qi">'+q[4]+'</span><span class="grow"><b>'+q[1]+'</b><div class="bar mini"><i style="width:'+Math.round(v/q[2]*100)+'%"></i></div><small class="muted">'+v+'/'+q[2]+' · '+q[3]+' xu</small></span>';
      const b=el('button','btn sm '+(cl?'ghost':done?'yellow':'ghost'),cl?'✓':done?'Nhận':'…');b.disabled=!done||cl;b.onclick=()=>{const d=daily();if(d.claimed[q[0]])return;d.claimed[q[0]]=1;gainXp(30,q[3]);saveG();sfx.win();toast('+'+q[3]+' xu');close();dailySheet();};r.appendChild(b);ql.appendChild(r);});
    m.appendChild(ql);const k=el('button','btn ghost block sm','Đóng');k.style.marginTop='12px';k.onclick=()=>{close();vMap();};m.appendChild(k);});
}
/* ---------- QUEST SELECT ---------- */
function questSelect(n){
  const d=dayInfo(n),st=G.cleared[n]||{};
  openModal((m,close)=>{
    m.innerHTML='<div class="eyebrow">Ngày '+n+' · chặng '+(d.phase+1)+'</div><div class="h" style="font-size:22px;margin-top:4px">'+esc(d.title)+'</div>';
    const list=el('div');list.style.cssText='display:flex;flex-direction:column;gap:10px;margin-top:14px';
    const Q=[['v','📘','Bug từ vựng','Đánh bại bằng nghĩa từ','#5ec8ff'],['p','💬','Bug ngữ pháp','Chọn câu tiếng Anh đúng','#a78bfa'],['l','🎧','Bug tai nghe','Nghe rồi chọn đúng câu','#5eead4'],['b','👑','BOSS: Minh-senpai','Đối thoại công sở (visual novel)','#ffd166']];
    Q.forEach(q=>{const b=el('button','quest');b.innerHTML='<span class="qi" style="background:'+q[4]+'">'+q[1]+'</span><span><b>'+q[2]+'</b><small>'+q[3]+'</small></span><span class="ok">'+(st[q[0]]?'★'.repeat(st[q[0]]):'')+'</span>';
      b.onclick=()=>{close();if(q[0]==='b')bossStart(n);else battleStart(n,q[0]);};list.appendChild(b);});
    m.appendChild(list);
    const x=el('button','btn ghost block sm','Đóng');x.style.marginTop='12px';x.onclick=close;m.appendChild(x);
  });
}

/* ---------- question builders ---------- */
function pickOthers(pool,notIdx,k,keyFn){const out=[];const seen=new Set([keyFn(pool[notIdx])]);let guard=0;while(out.length<k&&guard++<400){const i=Math.floor(Math.random()*pool.length);const v=keyFn(pool[i]);if(i===notIdx||seen.has(v)||!v)continue;seen.add(v);out.push(pool[i]);}return out;}
function vocabQs(d){
  let idx=d.v.slice();const prevMax=Math.min(...d.v);if(prevMax>3){for(let k=0;k<2;k++)idx.push(Math.floor(Math.random()*prevMax));}
  const qs=[];
  idx.forEach(i=>{const w=VOCAB[i];if(!w)return;
    const o1=pickOthers(VOCAB,i,3,x=>x.vi).map(x=>x.vi);qs.push({kind:'Nghĩa của từ',q:w.t,ipa:w.ipa,sub:w.pos,ans:w.vi,opts:shuffle([w.vi].concat(o1)),say:w.t});
    const o2=pickOthers(VOCAB,i,3,x=>x.t).map(x=>x.t);qs.push({kind:'Từ tiếng Anh là gì?',q:w.vi,sub:w.ex?w.ex.replace(/<b>.*?<\/b>/,'____').replace(/<[^>]+>/g,''):'',ans:w.t,opts:shuffle([w.t].concat(o2))});
  });
  return shuffle(qs);
}
function phraseQs(d){
  const base=PHR.slice(d.phase*5,d.phase*5+5);const qs=[];
  base.forEach((p,k)=>{const gi=d.phase*5+k;
    const o1=pickOthers(PHR,gi,3,x=>x.en).map(x=>x.en);qs.push({kind:'Nói câu này bằng tiếng Anh',q:p.vi,ans:p.en,opts:shuffle([p.en].concat(o1)),say:p.en});
    const words=p.en.replace(/[.,!?]/g,'').split(' ').filter(w=>w.length>3);if(words.length){const w=rnd(words);const blank=p.en.replace(new RegExp('\\b'+w.replace(/[.*+?^${}()|[\]\\]/g,'\\$&')+'\\b'),'____');
      const pool=PHR.map(x=>x.en.replace(/[.,!?]/g,'').split(' ')).flat().filter(x=>x.length>3&&x.toLowerCase()!==w.toLowerCase());const o2=shuffle(Array.from(new Set(pool))).slice(0,3);
      qs.push({kind:'Điền từ còn thiếu',q:blank,sub:p.vi,ans:w,opts:shuffle([w].concat(o2)),say:p.en});}
  });
  return shuffle(qs);
}
function listenQs(d){
  const li=d.li;const items=[LISTEN[li]].concat(pickOthers(LISTEN,li,3,x=>x.s.join(' ')));const qs=[];
  items.forEach(it=>{const s=it.s.join(' ');const idx=LISTEN.indexOf(it);
    const o1=pickOthers(LISTEN,idx,3,x=>x.s.join(' ')).map(x=>x.s.join(' '));qs.push({kind:'Nghe rồi chọn đúng câu',q:'🔊',sub:it.hint?'gợi ý: '+it.hint:'',ans:s,opts:shuffle([s].concat(o1)),say:s,listen:true});
    if(it.blank&&it.blank.length){const bi=it.blank[0];const w=it.s[bi];const shown=it.s.map((x,i)=>it.blank.includes(i)?'____':x).join(' ');
      const pool=LISTEN.map(x=>x.s).flat().filter(x=>x.length>2&&x.toLowerCase()!==w.toLowerCase());const o2=shuffle(Array.from(new Set(pool))).slice(0,3);
      qs.push({kind:'Nghe và điền từ thiếu',q:shown,ans:w,opts:shuffle([w].concat(o2)),say:s,listen:true});}
  });
  return shuffle(qs);
}

/* ---------- BATTLE ---------- */
let B=null;
const MON={v:['Bug Từ Vựng','#5ec8ff'],p:['Bug Ngữ Pháp','#a78bfa'],l:['Bug Tai Nghe','#5eead4']};
function battleStart(n,type){
  const d=dayInfo(n);const qs=type==='v'?vocabQs(d):type==='p'?phraseQs(d):listenQs(d);
  if(!qs.length){toast('Chưa có dữ liệu cho quest này');return;}
  if(G.hp<=0){G.hp=Math.ceil(G.maxHp/2);}
  B={n,type,queue:qs.slice(),total:qs.length,monHp:qs.length*10,monMax:qs.length*10,right:0,wrong:0,combo:0,timer:null,t0:0,limit:(type==='l'?15:12)+(G.up.timer||0)*2,cur:null,locked:false,hinted:false};
  document.body.classList.add('infight');G.combo=0;cur='battle';renderTabs();window.scrollTo(0,0);vBattle();nextQ();
}
function vBattle(){
  main.innerHTML='';const a=el('div','arena');
  const top=el('div','card btop');
  top.innerHTML='<span class="avatar" style="width:38px;height:38px;border-radius:11px;flex:0 0 auto">'+mascot('happy')+'</span><div class="grow" style="min-width:80px"><small class="mono">HP <b id="php">'+G.hp+'</b>/'+G.maxHp+'</small><div class="bar hp mini" id="phpbar"><i style="width:'+Math.round(G.hp/G.maxHp*100)+'%"></i></div></div>';
  const hb=el('button','ibtn','💡<b>'+G.items.hint+'</b>');hb.id='itHint';hb.disabled=G.items.hint<=0;hb.title='Gợi ý: loại 1 đáp án sai';
  hb.onclick=()=>{if(!B||B.locked||B.hinted||G.items.hint<=0)return;const wrong=[...document.querySelectorAll('.opt:not([disabled])')].filter(o=>o.textContent!==B.cur.ans);if(!wrong.length)return;const w=rnd(wrong);w.disabled=true;w.style.opacity='.25';B.hinted=true;G.items.hint--;saveG();hb.innerHTML='💡<b>'+G.items.hint+'</b>';hb.disabled=true;sfx.hit();};
  const pb=el('button','ibtn','🧪<b>'+G.items.potion+'</b>');pb.id='itPotion';pb.disabled=G.items.potion<=0;pb.title='Bình máu +50';
  pb.onclick=()=>{if(!B||G.items.potion<=0||G.hp>=G.maxHp)return;G.items.potion--;G.hp=Math.min(G.maxHp,G.hp+50);saveG();pb.innerHTML='🧪<b>'+G.items.potion+'</b>';pb.disabled=G.items.potion<=0;const ph=$('#php'),bar=$('#phpbar');if(ph)ph.textContent=G.hp;if(bar){bar.querySelector('i').style.width=Math.round(G.hp/G.maxHp*100)+'%';bar.classList.toggle('low',G.hp<=30);}const r=bar.getBoundingClientRect();fxText(r.left+40,r.top-10,'+50 HP','heal');sfx.ok();};
  const q=el('button','ibtn','✕');q.id='quitB';q.title='Rút lui';
  top.appendChild(hb);top.appendChild(pb);top.appendChild(q);a.appendChild(top);
  const mon=el('div','card moncard');
  mon.innerHTML='<div class="monster" id="mon"><div class="art">'+bug()+'</div><div class="grow"><div class="row between"><div class="mname">'+MON[B.type][0]+' · Ngày '+B.n+'</div><span class="combo" id="combo">x0</span></div><div class="bar mon" id="monbar"><i style="width:100%"></i><span id="montxt">'+B.monHp+' / '+B.monMax+'</span></div></div></div>';
  a.appendChild(mon);
  a.appendChild(el('div','bar time','<i id="tbar" style="width:100%"></i>'));
  a.appendChild(el('div','',''));a.lastChild.id='qwrap';
  main.appendChild(a);
  $('#quitB').onclick=()=>{stopTimer();openModal((m,close)=>{m.innerHTML='<div class="h" style="font-size:20px">Rút lui?</div><p class="muted">Tiến độ trận này sẽ mất.</p>';const r=el('div','row');r.style.gap='10px';const y=el('button','btn ghost grow','Ở lại');y.onclick=()=>{close();startTimer();};const nno=el('button','btn grow','Rút lui');nno.onclick=()=>{close();B=null;go('map');};r.appendChild(y);r.appendChild(nno);m.appendChild(r);});};
}
function stopTimer(){if(B&&B.timer){cancelAnimationFrame(B.timer);B.timer=null;}}
function startTimer(){stopTimer();B.t0=performance.now();const tick=()=>{if(!B||B.locked)return;const p=1-(performance.now()-B.t0)/(B.limit*1000);const bar=$('#tbar');if(bar)bar.style.width=Math.max(0,p*100)+'%';if(p<=0){answer(null);return;}B.timer=requestAnimationFrame(tick);};B.timer=requestAnimationFrame(tick);}
function nextQ(){
  if(!B)return;
  if(B.monHp<=0){victory();return;}
  if(!B.queue.length){B.queue=shuffle(B.wrongList||[]);B.wrongList=[];if(!B.queue.length){victory();return;}}
  const q=B.cur=B.queue.shift();B.locked=false;B.hinted=false;const ih=$('#itHint');if(ih)ih.disabled=G.items.hint<=0;
  const w=$('#qwrap');w.innerHTML='';
  const card=el('div','qcard pop');card.innerHTML='<div class="kind">'+esc(q.kind)+'</div><div class="q">'+(q.listen&&q.q==='🔊'?'<button class="btn blue" id="replay" style="min-height:64px;width:64px;border-radius:50%;font-size:26px">🔊</button>':esc(q.q))+'</div>'+(q.ipa?'<div class="ipa">'+esc(q.ipa)+'</div>':'')+(q.sub?'<div class="sub">'+esc(q.sub)+'</div>':'')+(q.listen&&q.q!=='🔊'?'<div style="margin-top:8px"><button class="btn blue sm" id="replay">🔊 Nghe lại</button></div>':'');
  w.appendChild(card);
  const opts=el('div','opts');q.opts.forEach(o=>{const b=el('button','opt',esc(o));b.onclick=()=>answer(o,b);opts.appendChild(b);});w.appendChild(opts);
  const rp=$('#replay');if(rp)rp.onclick=()=>speak(q.say);
  if(q.listen)setTimeout(()=>speak(q.say),250);
  startTimer();
}
function answer(o,btn){
  if(!B||B.locked)return;B.locked=true;stopTimer();
  const q=B.cur;const ok=o===q.ans;G.total++;
  document.querySelectorAll('.opt').forEach(b=>{b.disabled=true;if(b.textContent===q.ans)b.classList.add('good');});
  const monEl=$('#mon');
  if(ok){
    B.right++;G.correct++;B.combo++;G.combo=B.combo;G.bestCombo=Math.max(G.bestCombo||0,B.combo);
    const dmg=10;B.monHp=Math.max(0,B.monHp-dmg);
    sfx.ok();monEl.classList.remove('hit');void monEl.offsetWidth;monEl.classList.add('hit');
    const r=monEl.getBoundingClientRect();fxText(r.left+r.width/2+(Math.random()*60-30),r.top+40,'-'+dmg+(B.combo>=3?' ✦':''));
    const cb=$('#combo');cb.textContent='x'+B.combo;cb.classList.remove('big');void cb.offsetWidth;cb.classList.add('big');
    const xp=Math.round((10+Math.min(B.combo,10)*2)*(1+(G.up.combo||0)*.1));gainXp(xp,5);
    const dq=daily();dq.combo=Math.max(dq.combo||0,B.combo);
    fxText(r.left+r.width/2+60,r.top+70,'+'+xp+' XP','heal');
  }else{
    if(btn)btn.classList.add('bad');B.wrong++;B.combo=0;G.combo=0;$('#combo').textContent='x0';
    (B.wrongList=B.wrongList||[]).push(q);
    G.hp=Math.max(0,G.hp-10);sfx.bad();flashRed();main.classList.add('shaking');setTimeout(()=>main.classList.remove('shaking'),400);
    const ph=$('#php'),pb=$('#phpbar');if(ph)ph.textContent=G.hp;if(pb){pb.querySelector('i').style.width=Math.round(G.hp/G.maxHp*100)+'%';pb.classList.toggle('low',G.hp<=30);}
    const r=$('#phpbar').getBoundingClientRect();fxText(r.left+40,r.top-10,'-10 HP');
    if(!q.listen&&q.say)speak(q.say);else if(q.listen)speak(q.say);
  }
  saveG();
  const mb=$('#monbar');if(mb){mb.querySelector('i').style.width=Math.round(B.monHp/B.monMax*100)+'%';$('#montxt').textContent=B.monHp+' / '+B.monMax;}
  if(G.hp<=0){setTimeout(defeat,700);return;}
  setTimeout(nextQ,ok?650:1300);
}
function victory(){
  stopTimer();const monEl=$('#mon');if(monEl)monEl.classList.add('dead');sfx.win();confetti();
  const acc=B.right/Math.max(1,B.right+B.wrong);const stars=acc>=.9?3:acc>=.7?2:1;
  const st=G.cleared[B.n]||(G.cleared[B.n]={});st[B.type]=Math.max(st[B.type]||0,stars);
  G.wins++;daily().wins++;const bonus=50+stars*20;gainXp(bonus,20+stars*10);
  let opened=false;if(dayCleared(B.n)&&G.cur<=B.n){G.cur=B.n+1;opened=true;syncApp(B.n);}
  saveG();checkBadges();
  const b=B;B=null;
  setTimeout(()=>openModal((m,close)=>{
    m.innerHTML='<div class="eyebrow" style="text-align:center">CHIẾN THẮNG</div><div class="stars3">'+'★'.repeat(stars)+'<span style="opacity:.25">'+'★'.repeat(3-stars)+'</span></div><div class="big" style="font-size:26px">'+MON[b.type][0]+' bị hạ!</div>'+
      '<div class="row" style="justify-content:center;gap:14px;margin-top:10px;font-family:var(--disp);font-weight:700"><span>✅ '+b.right+' đúng</span><span>❌ '+b.wrong+' sai</span><span>+'+bonus+' XP</span></div>'+
      '<div class="mascot-row" style="margin-top:14px"><div class="mascot">'+mascot('cheer')+'</div><div class="bubble grow"><span class="who">Mochi</span>'+(opened?'Xong đủ 3 quest — mở khoá ngày '+G.cur+' rồi!':stars===3?'Hoàn hảo! Combo đẹp quá!':'Làm tốt lắm! Ôn lại vài từ sai là 3 sao ngay.')+'</div></div>';
    const r=el('div','row');r.style.cssText='gap:10px;margin-top:14px';
    const again=el('button','btn ghost grow','Chơi lại');again.onclick=()=>{close();battleStart(b.n,b.type);};
    const back=el('button','btn yellow grow','Về ngày '+b.n);back.onclick=()=>{close();go('map');questSelect(b.n);};
    r.appendChild(again);r.appendChild(back);m.appendChild(r);
  }),700);
}
function defeat(){
  stopTimer();const b=B;B=null;
  openModal((m,close)=>{m.innerHTML='<div class="eyebrow" style="text-align:center;color:var(--red)">HẾT HP</div><div class="big" style="font-size:26px">Bạn gục rồi…</div><div class="mascot-row" style="margin-top:14px"><div class="mascot">'+mascot('sad')+'</div><div class="bubble grow"><span class="who">Mochi</span>Không sao! Nghỉ một chút, HP hồi 50% rồi quay lại nhé.</div></div>';
    G.hp=Math.ceil(G.maxHp/2);saveG();
    const r=el('div','row');r.style.cssText='gap:10px;margin-top:14px';const a=el('button','btn grow','Thử lại');a.onclick=()=>{close();battleStart(b.n,b.type);};const k=el('button','btn ghost grow','Về bản đồ');k.onclick=()=>{close();go('map');};r.appendChild(a);r.appendChild(k);m.appendChild(r);});
}

/* ---------- BOSS (visual novel) ---------- */
let V=null;
function typeText(elm,text,cb){let i=0;elm.innerHTML='';const c=el('span','cur');elm.appendChild(c);const step=()=>{if(!elm.isConnected)return;if(i<text.length){c.insertAdjacentText('beforebegin',text[i++]);setTimeout(step,18);}else{c.remove();cb&&cb();}};step();}
function bossStart(n){
  const d=dayInfo(n);const rounds=[DIALOGS[d.di]].concat(pickOthers(DIALOGS,d.di,2,x=>x.them));
  if(G.hp<=0)G.hp=Math.ceil(G.maxHp/2);
  document.body.classList.add('infight');V={n,rounds,i:0,bossHp:100,right:0};cur='boss';renderTabs();window.scrollTo(0,0);vBoss();bossRound();
}
function vBoss(){
  main.innerHTML='';
  const head=el('div','card');head.style.padding='12px 14px';
  head.innerHTML='<div class="row between"><div><div class="eyebrow">BOSS · ngày '+V.n+'</div><b class="h" style="font-size:17px">Minh-senpai</b></div><button class="btn ghost sm" id="quitV">✕ Rút lui</button></div><div class="row" style="gap:8px;margin-top:8px"><small style="font-family:var(--mono);font-size:10.5px;color:var(--faint)">HP bạn</small><div class="bar hp grow" id="vphp"><i style="width:'+Math.round(G.hp/G.maxHp*100)+'%"></i></div></div>';
  main.appendChild(head);
  const vn=el('div','vn');vn.innerHTML='<div class="scene"><div class="bosshp"><div class="bar mon" id="bosshp"><i style="width:100%"></i><span>BOSS 100</span></div></div><div class="npc" id="npc">'+senpai()+'</div></div><div class="box"><span class="name">Minh-senpai</span><div class="txt" id="vtxt"></div></div>';
  main.appendChild(vn);
  const ch=el('div','choices');ch.id='choices';main.appendChild(ch);
  $('#quitV').onclick=()=>{V=null;go('map');};
}
function bossRound(){
  if(!V)return;
  if(V.i>=V.rounds.length||V.bossHp<=0){bossEnd();return;}
  const r=V.rounds[V.i];const npc=$('#npc');npc.innerHTML=senpai();npc.classList.add('talk');
  const ch=$('#choices');ch.innerHTML='';
  typeText($('#vtxt'),r.them,()=>{npc.classList.remove('talk');
    shuffle(r.opts).forEach(o=>{const b=el('button','choice',esc(o.t));b.onclick=()=>bossPick(o,b);ch.appendChild(b);});
  });
  speak(r.them);
}
function bossPick(o,btn){
  document.querySelectorAll('.choice').forEach(b=>b.disabled=true);
  const npc=$('#npc');
  if(o.good){btn.classList.add('good');V.right++;V.bossHp=Math.max(0,V.bossHp-50);sfx.ok();npc.innerHTML=senpai('angry');npc.classList.add('shaking');setTimeout(()=>npc.classList.remove('shaking'),400);
    const r=npc.getBoundingClientRect();fxText(r.left+r.width/2,r.top+30,'-50');gainXp(30,10);}
  else{btn.classList.add('bad');document.querySelectorAll('.choice').forEach(b=>{const t=V.rounds[V.i].opts.find(x=>x.good);if(t&&b.textContent===t.t)b.classList.add('good');});
    G.hp=Math.max(0,G.hp-15);sfx.bad();flashRed();npc.innerHTML=senpai('glad');const pb=$('#vphp');if(pb)pb.querySelector('i').style.width=Math.round(G.hp/G.maxHp*100)+'%';}
  const hb=$('#bosshp');hb.querySelector('i').style.width=V.bossHp+'%';hb.querySelector('span').textContent='BOSS '+V.bossHp;
  speak(o.t);
  const tip=el('div','tip');tip.innerHTML='<b>'+(o.good?'✓ Chuẩn!':'✗ Chưa đúng')+'</b> '+esc(o.fb||'');$('#choices').appendChild(tip);
  saveG();
  if(G.hp<=0){setTimeout(()=>{V=null;defeatBoss();},800);return;}
  const nb=el('button','btn yellow block pin','Tiếp ›');nb.onclick=()=>{V.i++;bossRound();};$('#choices').appendChild(nb);
}
function defeatBoss(){openModal((m,close)=>{m.innerHTML='<div class="eyebrow" style="text-align:center;color:var(--red)">HẾT HP</div><div class="big" style="font-size:24px">Senpai thắng lần này…</div><div class="mascot-row" style="margin-top:14px"><div class="mascot">'+mascot('sad')+'</div><div class="bubble grow"><span class="who">Mochi</span>Đọc kỹ phản hồi rồi thử lại nhé. HP hồi 50%.</div></div>';G.hp=Math.ceil(G.maxHp/2);saveG();const b=el('button','btn block','Về bản đồ');b.style.marginTop='14px';b.onclick=()=>{close();go('map');};m.appendChild(b);});}
function bossEnd(){
  const win=V.bossHp<=0;const stars=V.right>=3?3:V.right>=2?2:1;const n=V.n;V=null;
  if(win){const st=G.cleared[n]||(G.cleared[n]={});st.b=Math.max(st.b||0,stars);G.bossWins++;daily().boss++;gainXp(120+stars*30,60);sfx.win();confetti();}else sfx.bad();
  saveG();checkBadges();
  const ai=aiConfigured();
  openModal((m,close)=>{
    m.innerHTML='<div class="eyebrow" style="text-align:center">'+(win?'BOSS BỊ HẠ':'BOSS THOÁT MẤT')+'</div>'+(win?'<div class="stars3">'+'★'.repeat(stars)+'<span style="opacity:.25">'+'★'.repeat(3-stars)+'</span></div>':'')+'<div class="big" style="font-size:24px">'+(win?'Minh-senpai gật gù!':'Cần ≥ 2/3 câu đúng')+'</div>'+
      '<div class="mascot-row" style="margin-top:14px"><div class="mascot">'+mascot(win?'cheer':'think')+'</div><div class="bubble grow"><span class="who">Mochi</span>'+(win?'Giao tiếp công sở chuẩn luôn! ':'Suýt nữa thôi! ')+(ai?'Muốn thử <b>Boss AI</b> nói chuyện tự do không?':'Cấu hình AI trong app để mở <b>Boss AI</b> nói chuyện tự do.')+'</div></div>';
    const r=el('div','row');r.style.cssText='gap:10px;margin-top:14px;flex-wrap:wrap';
    if(ai){const a=el('button','btn violet grow','🤖 Boss AI');a.onclick=()=>{close();aiBossStart(n);};r.appendChild(a);}
    const k=el('button','btn yellow grow','Về ngày '+n);k.onclick=()=>{close();go('map');questSelect(n);};r.appendChild(k);m.appendChild(r);
  });
}

/* ---------- AI BOSS (free talk, visual novel) ---------- */
function aiCfg(){const a=loadApp();return (a.ai&&a.ai.key&&a.ai.provider)?a.ai:null;}
let SAMPLE;async function claudeSp(){if(SAMPLE!==undefined)return SAMPLE;SAMPLE=null;if(window.claude&&window.claude.use){try{SAMPLE=await window.claude.use('sample');}catch(e){SAMPLE=null;}}return SAMPLE;}
function inClaude(){return !!(window.claude&&window.claude.use);}
function aiConfigured(){return inClaude()||!!aiCfg();}
async function aiCall(system,msgs){
  if(inClaude()){const sp=await claudeSp();if(sp){const r=await sp([{role:'user',content:system}].concat(msgs),{modelTier:'quick'});return (r&&r.text)||'';}}
  const c=aiCfg();if(!c)throw new Error('no-ai');
  if(c.provider==='gemini'){
    const model=c.model||'gemini-flash-lite-latest';
    const contents=[{role:'user',parts:[{text:system}]},{role:'model',parts:[{text:'OK.'}]}].concat(msgs.map(m=>({role:m.role==='assistant'?'model':'user',parts:[{text:m.content}]})));
    const r=await fetch('https://generativelanguage.googleapis.com/v1beta/models/'+encodeURIComponent(model)+':generateContent',{method:'POST',headers:{'Content-Type':'application/json','x-goog-api-key':c.key},body:JSON.stringify({contents,generationConfig:{maxOutputTokens:1024,temperature:.8}})});
    if(!r.ok)throw new Error('gemini '+r.status);const j=await r.json();return ((j.candidates||[])[0]||{}).content?.parts?.map(p=>p.text||'').join('')||'';
  }
  if(c.provider==='claude'){
    const r=await fetch('https://api.anthropic.com/v1/messages',{method:'POST',headers:{'Content-Type':'application/json','x-api-key':c.key,'anthropic-version':'2023-06-01','anthropic-dangerous-direct-browser-access':'true'},body:JSON.stringify({model:c.model||'claude-3-5-haiku-latest',max_tokens:1024,system,messages:msgs})});
    if(!r.ok)throw new Error('claude '+r.status);const j=await r.json();return (j.content||[]).map(x=>x.text||'').join('');
  }
  const r=await fetch('https://api.groq.com/openai/v1/chat/completions',{method:'POST',headers:{'Content-Type':'application/json','Authorization':'Bearer '+c.key},body:JSON.stringify({model:c.model||'llama-3.1-8b-instant',messages:[{role:'system',content:system}].concat(msgs),temperature:.8})});
  if(!r.ok)throw new Error('groq '+r.status);const j=await r.json();return ((j.choices||[])[0]||{}).message?.content||'';
}
function parseJSON(t){try{const m=String(t).match(/\{[\s\S]*\}|\[[\s\S]*\]/);return m?JSON.parse(m[0]):null;}catch(e){return null;}}
function aiRules(sc){const lvl=(loadApp().cfg||{}).level||'A2';return 'You are Minh, a friendly senior developer and English conversation partner for a Vietnamese junior developer (CEFR '+lvl+'). Roleplay this work scenario: '+sc+' Reply IN CHARACTER in 1-2 short simple sentences (about 20 words) ending with a question. Your English must be grammatically correct. Then, on a NEW line starting exactly with "FIX:", list up to 2 corrections of the user\'s last message as: wrong => right ~ short Vietnamese note (with full diacritics). If the user\'s English was fine, write exactly "FIX: OK".';}
const SCEN=['We are in a daily standup. Ask what I did yesterday, what I do today, and blockers.','I am reporting a blocker to you, my team lead. React and ask short follow-up questions.','You are reviewing my pull request. Give short feedback and ask why I made some choices.','We are about to deploy to production. Talk about the plan and the risks.'];
function parseReply(t){const i=t.indexOf('FIX:');return i<0?{reply:t.trim(),fix:''}:{reply:t.slice(0,i).trim(),fix:t.slice(i+4).trim()};}
function aiBossStart(n){
  document.body.classList.add('infight');const sc=rnd(SCEN);V={n,ai:true,sc,turns:[],user:0,bossHp:60};cur='boss';renderTabs();window.scrollTo(0,0);
  main.innerHTML='';
  const head=el('div','card');head.style.padding='12px 14px';
  head.innerHTML='<div class="row between"><div><div class="eyebrow">BOSS AI · nói tự do</div><b class="h" style="font-size:17px">Minh-senpai</b></div><button class="btn ghost sm" id="quitV">✕ Rút lui</button></div>';
  main.appendChild(head);
  const vn=el('div','vn');vn.innerHTML='<div class="scene"><div class="bosshp"><div class="bar mon" id="bosshp"><i style="width:100%"></i><span>BOSS 60 · chấm điểm sau 4 lượt</span></div></div><div class="npc" id="npc">'+senpai()+'</div></div><div class="box"><span class="name">Minh-senpai</span><div class="txt" id="vtxt"></div></div>';
  main.appendChild(vn);
  const tips=el('div');tips.id='tips';tips.style.cssText='display:flex;flex-direction:column;gap:8px';main.appendChild(tips);
  const inrow=el('div','row');inrow.style.gap='8px';
  const inp=el('input','input grow');inp.id='vin';inp.placeholder='Trả lời bằng tiếng Anh…';inp.autocomplete='off';
  const mic=el('button','btn blue sm','🎤');mic.style.minHeight='50px';mic.onclick=()=>micTo(inp);
  const send=el('button','btn sm','Gửi');send.style.minHeight='50px';send.onclick=()=>aiSend();
  inp.onkeydown=e=>{if(e.key==='Enter')aiSend();};
  inrow.appendChild(inp);inrow.appendChild(mic);inrow.appendChild(send);main.appendChild(inrow);
  const endb=el('button','btn yellow block','Kết thúc & chấm điểm');endb.id='endB';endb.disabled=true;endb.onclick=aiScore;main.appendChild(endb);
  $('#quitV').onclick=()=>{V=null;go('map');};
  (async()=>{try{const t=await aiCall(aiRules(sc),[{role:'user',content:'Start the conversation now with your first line.'}]);const p=parseReply(t);V.turns.push({role:'assistant',content:t});npcSay(p.reply);}catch(e){toast('AI lỗi: '+(e.message||''));}})();
}
function npcSay(txt){const npc=$('#npc');npc.classList.add('talk');typeText($('#vtxt'),txt,()=>npc.classList.remove('talk'));speak(txt);}
function micTo(inp){const SR=window.SpeechRecognition||window.webkitSpeechRecognition;if(!SR){toast('Trình duyệt không hỗ trợ mic');return;}const r=new SR();r.lang='en-US';r.onresult=e=>{inp.value=e.results[0][0].transcript;inp.focus();};r.onerror=()=>toast('Không nghe được');try{r.start();toast('Đang nghe… nói tiếng Anh');}catch(e){}}
async function aiSend(){
  if(!V||!V.ai)return;const inp=$('#vin');const t=(inp.value||'').trim();if(!t)return;inp.value='';V.user++;
  V.turns.push({role:'user',content:t});$('#vtxt').innerHTML='<span class="muted">…</span>';
  try{const out=await aiCall(aiRules(V.sc),V.turns);const p=parseReply(out);V.turns.push({role:'assistant',content:out});npcSay(p.reply);
    if(p.fix&&p.fix.replace(/[.\s]/g,'')!=='OK'){const tip=el('div','tip');tip.innerHTML='<b>✎ Mochi sửa:</b>'+p.fix.split('\n').filter(Boolean).map(l=>{const m=l.match(/^(.*?)=>(.*?)(?:~(.*))?$/);return m?'<span class="fixl"><s>'+esc(m[1].trim())+'</s> → <b class="r">'+esc(m[2].trim())+'</b>'+(m[3]?' <span class="muted">('+esc(m[3].trim())+')</span>':'')+'</span>':'<span class="fixl">'+esc(l)+'</span>';}).join('');$('#tips').prepend(tip);}
    else{const tip=el('div','tip');tip.innerHTML='<b>✓ Mochi:</b> câu này ổn!';$('#tips').prepend(tip);gainXp(10,3);}
    if(V.user>=4)$('#endB').disabled=false;
  }catch(e){toast('AI lỗi, thử lại');}
}
async function aiScore(){
  if(!V||!V.ai)return;$('#endB').disabled=true;toast('Senpai đang chấm…');
  const ctx=V.turns.map(m=>(m.role==='user'?'Me: ':'Colleague: ')+parseReply(m.content).reply).join('\n');
  try{const out=await aiCall('You grade English speaking practice. Reply ONLY JSON.',[{role:'user',content:'Evaluate ONLY the developer (Me). Reply ONLY JSON {"score": number 1-10, "tip": one short specific tip in Vietnamese}.\n\n'+ctx}]);
    const r=parseJSON(out)||{score:5,tip:''};const sc=Math.max(1,Math.min(10,+r.score||5));const n=V.n;const win=sc>=6;const stars=sc>=9?3:sc>=7?2:1;V=null;
    if(win){const st=G.cleared[n]||(G.cleared[n]={});st.b=Math.max(st.b||0,stars);G.bossWins++;daily().boss++;gainXp(150+stars*40,80);sfx.win();confetti();}else sfx.bad();
    saveG();checkBadges();
    openModal((m,close)=>{m.innerHTML='<div class="eyebrow" style="text-align:center">'+(win?'BOSS AI BỊ HẠ':'CHƯA HẠ ĐƯỢC')+'</div><div class="big">'+sc+'<span style="font-size:20px;color:var(--muted)">/10</span></div>'+(win?'<div class="stars3">'+'★'.repeat(stars)+'</div>':'')+'<div class="mascot-row" style="margin-top:12px"><div class="mascot">'+mascot(win?'cheer':'think')+'</div><div class="bubble grow"><span class="who">Mochi</span>'+esc(r.tip||(win?'Quá đỉnh!':'Cần ≥ 6 điểm. Thử lại nhé!'))+'</div></div>';const b=el('button','btn yellow block','Về ngày '+n);b.style.marginTop='14px';b.onclick=()=>{close();go('map');questSelect(n);};m.appendChild(b);});
  }catch(e){toast('AI lỗi khi chấm');$('#endB').disabled=false;}
}

/* ================= TALK HUB (5 chế độ luyện nói) ================= */
const TALK=[
 ['battle','⚔️','Đấu thoại','Nói từng câu, AI chấm thành sát thương',true,'#ff7eb6'],
 ['shadow','🎵','Đọc theo nhịp','Đọc theo câu mẫu, mic chấm từng từ',false,'#5ec8ff'],
 ['story','🏢','Chuyện văn phòng','Visual novel 5 cảnh · 3 nhân vật · 3 kết cục',false,'#a78bfa'],
 ['reflex','⚡','Phản xạ 5 giây','Nghe hỏi, 5 giây để trả lời bằng miệng',false,'#ffd166'],
 ['equip','🛡️','Trang bị cho Mochi','Câu đọc chuẩn = Mochi nói khi AFK, +xu/giờ',false,'#5eead4']
];
function vTalk(){
  main.innerHTML='';
  const h=el('div','card');h.innerHTML='<div class="mascot-row"><div class="mascot">'+mascot('cheer')+'</div><div class="bubble grow"><span class="who">Mochi</span>Đây là phòng tập <b>nói</b>. Bật mic lên, nói thật to — chọn đáp án không tính đâu nha!</div></div>'+(hasSR()?'':'<p class="tip" style="margin-top:10px">Trình duyệt này không có nhận diện giọng nói — các chế độ vẫn chơi được bằng cách gõ.</p>');
  main.appendChild(h);
  const list=el('div');list.style.cssText='display:flex;flex-direction:column;gap:10px';
  TALK.forEach(t=>{const b=el('button','quest');const rec=t[0]==='shadow'?(G.talk.shadowBest?'kỷ lục '+G.talk.shadowBest+'%':''):t[0]==='reflex'?(G.talk.reflexBest?'kỷ lục '+G.talk.reflexBest+' điểm':''):t[0]==='battle'?(G.talk.battleWins?G.talk.battleWins+' trận thắng':''):t[0]==='story'?(Object.keys(G.talk.endings).length+'/3 kết cục'):(G.talk.equipped.length+' câu · +'+equipBonus()+' xu/giờ');
    b.innerHTML='<span class="qi" style="background:'+t[5]+'">'+t[1]+'</span><span class="grow"><b>'+t[2]+(t[4]?' <span class="kbd">AI</span>':'')+'</b><small>'+t[3]+(rec?' · <span style="color:var(--yellow)">'+rec+'</span>':'')+'</small></span><span class="ok">›</span>';
    b.onclick=()=>({battle:talkBattleStart,shadow:shadowStart,story:storyStart,reflex:reflexStart,equip:vEquip})[t[0]]();list.appendChild(b);});
  main.appendChild(list);
}
function talkHeader(title,sub,extra){const h=el('div','card');h.style.padding='12px 14px';h.innerHTML='<div class="row between"><div><div class="eyebrow">'+title+'</div><b class="h" style="font-size:16px">'+sub+'</b></div><button class="btn ghost sm" id="quitT">✕ Thoát</button></div>'+(extra||'');main.appendChild(h);$('#quitT').onclick=()=>{stopSR();speechSynthesis&&speechSynthesis.cancel();go('talk');};}
function micButton(label,onStart){const b=el('button','btn blue block',label||'🎤 Bấm rồi nói');b.onclick=()=>onStart(b);return b;}
function typeFallback(placeholder,onSubmit){const r=el('div','row');r.style.gap='8px';const i=el('input','input grow');i.placeholder=placeholder||'…hoặc gõ câu tiếng Anh';i.autocomplete='off';const s=el('button','btn sm','Gửi');s.style.minHeight='50px';const go_=()=>{const t=i.value.trim();if(!t)return;i.value='';onSubmit(t);};s.onclick=go_;i.onkeydown=e=>{if(e.key==='Enter')go_();};r.appendChild(i);r.appendChild(s);return r;}
function wordsHtml(m){return m.words.map((w,i)=>'<span class="wd '+(m.res[i]?'hit':'miss')+'">'+esc(w)+'</span>').join(' ');}
function pickSentences(n){const ch=DAYS[G.cur-1]?DAYS[G.cur-1].phase:0;const base=PHR.slice(ch*5,ch*5+5).map(p=>({en:p.en,vi:p.vi}));const pool=shuffle(PHR.map(p=>({en:p.en,vi:p.vi})).concat(LISTEN.map(l=>({en:l.s.join(' '),vi:l.hint||''}))));const out=shuffle(base);for(const p of pool){if(out.length>=n)break;if(!out.some(x=>x.en===p.en))out.push(p);}return out.slice(0,n);}
function addEquip(en){if(!G.talk.equipped.includes(en)){G.talk.equipped.push(en);if(G.talk.equipped.length>60)G.talk.equipped.shift();saveG();return true;}return false;}

/* ---- 2) Đọc theo nhịp (shadowing) ---- */
let SH=null;
document.body.classList.add('infight');function shadowStart(){SH={qs:pickSentences(8),i:0,sum:0,equipped:0};cur='talk';main.innerHTML='';talkHeader('ĐỌC THEO NHỊP','Câu '+1+'/8');shadowRound();}
function shadowRound(){
  if(!SH)return;if(SH.i>=SH.qs.length){shadowEnd();return;}
  const q=SH.qs[SH.i];main.innerHTML='';talkHeader('ĐỌC THEO NHỊP','Câu '+(SH.i+1)+'/'+SH.qs.length,'<div class="bar time" style="margin-top:10px"><i id="shbar" style="width:0%"></i></div>');
  const c=el('div','qcard pop');c.innerHTML='<div class="kind">Nghe rồi đọc theo</div><div class="q" style="font-size:21px" id="shTxt">'+esc(q.en)+'</div>'+(q.vi?'<div class="sub">'+esc(q.vi)+'</div>':'')+'<div class="row" style="justify-content:center;gap:8px;margin-top:12px"><button class="btn blue sm" id="shPlay">🔊 Nghe</button></div>';
  main.appendChild(c);
  const res=el('div');res.id='shRes';main.appendChild(res);
  const mic=micButton('🎤 Bấm rồi đọc câu trên',b=>{b.textContent='● Đang nghe… đọc đi!';b.classList.add('rec');let t0=performance.now();const dur=6000;const tick=()=>{const bar=$('#shbar');if(!bar||!SRcur)return;bar.style.width=Math.min(100,(performance.now()-t0)/dur*100)+'%';requestAnimationFrame(tick);};
    listenOnce(t=>shadowGrade(q,t),st=>{b.textContent='🎤 Bấm rồi đọc câu trên';b.classList.remove('rec');if(st==='nosr')toast('Không có mic — hãy gõ bên dưới');else if(st==='empty'&&!$('#shRes').children.length)toast('Chưa nghe rõ, thử lại hoặc gõ');},dur);tick();});
  main.appendChild(mic);main.appendChild(typeFallback('…hoặc gõ lại câu',t=>shadowGrade(q,t)));
  $('#shPlay').onclick=()=>speak(q.en);setTimeout(()=>speak(q.en),300);
}
function shadowGrade(q,heard){
  stopSR();const m=matchWords(q.en,heard);SH.sum+=m.pct;const eq=m.pct>=80&&addEquip(q.en);if(eq)SH.equipped++;
  const xp=Math.round(m.pct/5);gainXp(xp,Math.round(m.pct/10));if(m.pct>=80)sfx.ok();else if(m.pct>=50)sfx.hit();else sfx.bad();
  const r=$('#shRes');r.innerHTML='<div class="card pop" style="margin-top:10px"><div class="row between"><b class="h" style="font-size:22px;color:'+(m.pct>=80?'var(--green)':m.pct>=50?'var(--yellow)':'var(--red)')+'">'+m.pct+'%</b><span class="kbd">+'+xp+' XP'+(eq?' · 🛡️ trang bị':'')+'</span></div><div class="wds">'+wordsHtml(m)+'</div><small class="muted">Bạn nói: “'+esc(heard)+'”</small></div>';
  const nb=el('button','btn yellow block pin','Câu tiếp ›');nb.onclick=()=>{SH.i++;shadowRound();};r.appendChild(nb);
  const dq=daily();dq.combo=Math.max(dq.combo||0,m.pct>=80?5:0);
}
function shadowEnd(){const avg=Math.round(SH.sum/SH.qs.length);const best=Math.max(G.talk.shadowBest||0,avg);const isBest=avg>(G.talk.shadowBest||0);G.talk.shadowBest=best;const stars=avg>=85?3:avg>=65?2:1;gainXp(60+stars*20,30+stars*10);G.wins++;daily().wins++;saveG();checkBadges();sfx.win();confetti();const eqn=SH.equipped;SH=null;
  openModal((m,close)=>{m.innerHTML='<div class="eyebrow" style="text-align:center">HOÀN THÀNH</div><div class="stars3">'+'★'.repeat(stars)+'<span style="opacity:.25">'+'★'.repeat(3-stars)+'</span></div><div class="big">'+avg+'%</div>'+(isBest?'<div style="text-align:center;color:var(--yellow);font-family:var(--disp);font-weight:700">🏆 Kỷ lục mới!</div>':'')+'<div class="mascot-row" style="margin-top:12px"><div class="mascot">'+mascot(stars===3?'cheer':'happy')+'</div><div class="bubble grow"><span class="who">Mochi</span>'+(eqn?'Mình học được <b>'+eqn+' câu mới</b> để nói khi AFK! ':'')+(stars===3?'Phát âm chuẩn quá!':'Đọc chậm, rõ từng từ là lên % ngay.')+'</div></div>';const r=el('div','row');r.style.cssText='gap:10px;margin-top:14px';const a=el('button','btn ghost grow','Chơi lại');a.onclick=()=>{close();shadowStart();};const k=el('button','btn yellow grow','Về Nói');k.onclick=()=>{close();go('talk');};r.appendChild(a);r.appendChild(k);m.appendChild(r);});}

/* ---- 4) Phản xạ 5 giây ---- */
let RF=null;
document.body.classList.add('infight');function reflexStart(){RF={qs:shuffle(DIALOGS).slice(0,8),i:0,score:0};cur='talk';reflexRound();}
function reflexRound(){
  if(!RF)return;if(RF.i>=RF.qs.length){reflexEnd();return;}
  const d=RF.qs[RF.i];main.innerHTML='';talkHeader('PHẢN XẠ 5 GIÂY','Câu '+(RF.i+1)+'/'+RF.qs.length+' · '+RF.score+' điểm','<div class="bar time" style="margin-top:10px"><i id="rfbar" style="width:100%"></i></div>');
  const vn=el('div','vn');vn.innerHTML='<div class="scene" style="min-height:150px"><div class="npc" style="width:150px;height:150px" id="npc">'+npc('minh')+'</div></div><div class="box"><span class="name">Minh-senpai</span><div class="txt" id="vtxt"></div></div>';main.appendChild(vn);
  const res=el('div');res.id='rfRes';main.appendChild(res);
  const status=el('div','tip');status.id='rfStat';status.textContent='🔊 Nghe câu hỏi…';main.appendChild(status);
  main.appendChild(typeFallback('…hoặc gõ câu trả lời',t=>reflexGrade(d,t)));
  typeText($('#vtxt'),d.them,()=>{
    $('#rfStat').textContent='🎤 Trả lời ngay! (5 giây)';$('#rfStat').classList.add('rec');
    const t0=performance.now();const tick=()=>{const bar=$('#rfbar');if(!bar||!RF||RF.graded)return;const p=1-(performance.now()-t0)/5000;bar.style.width=Math.max(0,p*100)+'%';if(p>0)requestAnimationFrame(tick);};tick();
    RF.tmr=setTimeout(()=>{if(RF&&!RF.graded)reflexGrade(d,'');},5200);
    listenOnce(t=>reflexGrade(d,t),st=>{if(RF&&!RF.graded&&st!=='ok'){const s=$('#rfStat');if(s)s.textContent=st==='nosr'?'Không có mic — gõ câu trả lời bên dưới':'Mic chưa nghe được — nói lại hoặc gõ bên dưới';}},5000);
  });speak(d.them);
}
function reflexGrade(d,heard){
  if(!RF||RF.graded)return;RF.graded=true;stopSR();clearTimeout(RF.tmr);const good=d.opts.find(o=>o.good);const sc=heard?keywordScore(heard,good.t):0;RF.score+=sc;
  if(sc>=7)sfx.ok();else if(sc>=4)sfx.hit();else sfx.bad();gainXp(sc*2,sc);
  const r=$('#rfRes');r.innerHTML='<div class="card pop"><div class="row between"><b class="h" style="font-size:22px;color:'+(sc>=7?'var(--green)':sc>=4?'var(--yellow)':'var(--red)')+'">+'+sc+' điểm</b><span class="kbd">'+(heard?'bạn nói':'im lặng')+'</span></div>'+(heard?'<small class="muted">“'+esc(heard)+'”</small>':'')+'<div class="tip" style="margin-top:8px"><b>Mẫu:</b> '+esc(good.t)+'<br><small>'+esc(good.fb||'')+'</small></div></div>';
  const st=$('#rfStat');if(st){st.classList.remove('rec');st.textContent=sc>=7?'Phản xạ tốt!':sc>=4?'Ổn, thêm từ khoá nữa nhé':'Nói gì đó cũng được — quan trọng là mở miệng!';}
  const nb=el('button','btn yellow block pin','Câu tiếp ›');nb.onclick=()=>{RF.i++;RF.graded=false;reflexRound();};r.appendChild(nb);
}
function reflexEnd(){const sc=RF.score,max=RF.qs.length*10;const isBest=sc>(G.talk.reflexBest||0);G.talk.reflexBest=Math.max(G.talk.reflexBest||0,sc);const stars=sc>=max*.8?3:sc>=max*.5?2:1;gainXp(50+stars*20,20+stars*10);G.wins++;daily().wins++;saveG();checkBadges();sfx.win();if(stars>1)confetti();RF=null;
  openModal((m,close)=>{m.innerHTML='<div class="eyebrow" style="text-align:center">KẾT QUẢ</div><div class="stars3">'+'★'.repeat(stars)+'<span style="opacity:.25">'+'★'.repeat(3-stars)+'</span></div><div class="big">'+sc+'<span style="font-size:18px;color:var(--muted)">/'+max+'</span></div>'+(isBest?'<div style="text-align:center;color:var(--yellow);font-family:var(--disp);font-weight:700">🏆 Kỷ lục mới!</div>':'')+'<div class="mascot-row" style="margin-top:12px"><div class="mascot">'+mascot(stars===3?'cheer':'think')+'</div><div class="bubble grow"><span class="who">Mochi</span>'+(stars===3?'Phản xạ như dev senior!':'Mẹo: trả lời ngắn nhưng có từ khoá của câu hỏi.')+'</div></div>';const r=el('div','row');r.style.cssText='gap:10px;margin-top:14px';const a=el('button','btn ghost grow','Chơi lại');a.onclick=()=>{close();reflexStart();};const k=el('button','btn yellow grow','Về Nói');k.onclick=()=>{close();go('talk');};r.appendChild(a);r.appendChild(k);m.appendChild(r);});}

/* ---- 3) Chuyện văn phòng (story mode) ---- */
let ST=null;
const ENDINGS=[[85,'🌟 Được khen trước cả team',3],[60,'☕ Một ngày làm việc ổn',2],[0,'📝 Bị PM nhắc nhở nhẹ',1]];
function storyStart(){const who=['minh','linh','an'];document.body.classList.add('infight');ST={scenes:shuffle(DIALOGS).slice(0,5).map((d,i)=>({d,who:who[i%3]})),i:0,rep:50};cur='talk';storyScene();}
function storyScene(){
  if(!ST)return;if(ST.i>=ST.scenes.length){storyEnd();return;}
  const s=ST.scenes[ST.i],c=CAST[s.who];main.innerHTML='';
  talkHeader('CHUYỆN VĂN PHÒNG','Cảnh '+(ST.i+1)+'/5','<div class="row" style="gap:8px;margin-top:8px"><small style="font-family:var(--mono);font-size:10.5px;color:var(--faint)">UY TÍN</small><div class="bar xp grow"><i id="repbar" style="width:'+ST.rep+'%"></i><span>'+ST.rep+'</span></div></div>');
  const vn=el('div','vn '+s.who);vn.innerHTML='<div class="scene"><div class="npc talk" id="npc">'+npc(s.who)+'</div></div><div class="box"><span class="name">'+c.name+' · '+c.role+'</span><div class="txt" id="vtxt"></div></div>';main.appendChild(vn);
  const ch=el('div','choices');ch.id='choices';main.appendChild(ch);
  typeText($('#vtxt'),s.d.them,()=>{$('#npc').classList.remove('talk');shuffle(s.d.opts).forEach(o=>{const b=el('button','choice',esc(o.t));b.onclick=()=>storyPick(s,o,b);ch.appendChild(b);});});speak(s.d.them);
}
function storyPick(s,o,btn){
  document.querySelectorAll('.choice').forEach(b=>b.disabled=true);const npcEl=$('#npc');
  if(o.good){btn.classList.add('good');ST.rep=Math.min(100,ST.rep+15);sfx.ok();npcEl.innerHTML=npc(s.who,'glad');gainXp(25,8);}
  else{btn.classList.add('bad');document.querySelectorAll('.choice').forEach(b=>{const g=s.d.opts.find(x=>x.good);if(g&&b.textContent===g.t)b.classList.add('good');});ST.rep=Math.max(0,ST.rep-12);sfx.bad();npcEl.innerHTML=npc(s.who,'angry');}
  const rb=$('#repbar');if(rb){rb.style.width=ST.rep+'%';rb.nextElementSibling.textContent=ST.rep;}
  speak(o.t);const tip=el('div','tip');tip.innerHTML='<b>'+(o.good?'✓':'✗')+'</b> '+esc(o.fb||'');$('#choices').appendChild(tip);
  const nb=el('button','btn yellow block pin','Cảnh tiếp ›');nb.onclick=()=>{ST.i++;storyScene();};$('#choices').appendChild(nb);
}
function storyEnd(){const e=ENDINGS.find(x=>ST.rep>=x[0]);const stars=e[2];G.talk.endings[stars]=1;const rep=ST.rep;ST=null;gainXp(80+stars*30,40+stars*10);G.wins++;daily().wins++;if(stars===3){G.bossWins++;daily().boss++;}saveG();checkBadges();sfx.win();if(stars>1)confetti();
  openModal((m,close)=>{m.innerHTML='<div class="eyebrow" style="text-align:center">KẾT CỤC</div><div class="stars3">'+'★'.repeat(stars)+'<span style="opacity:.25">'+'★'.repeat(3-stars)+'</span></div><div class="big" style="font-size:22px">'+e[1]+'</div><p class="muted" style="text-align:center;margin-top:6px">Uy tín cuối ngày: '+rep+'/100 · đã mở '+Object.keys(G.talk.endings).length+'/3 kết cục</p><div class="mascot-row" style="margin-top:12px"><div class="mascot">'+mascot(stars===3?'cheer':stars===2?'happy':'sad')+'</div><div class="bubble grow"><span class="who">Mochi</span>'+(stars===3?'Cả team quý bạn rồi!':stars===2?'Ổn! Thử lại để lấy kết cục 3 sao.':'Đọc kỹ phản hồi mỗi cảnh nha, mai làm lại.')+'</div></div>';const r=el('div','row');r.style.cssText='gap:10px;margin-top:14px';const a=el('button','btn ghost grow','Ngày mới');a.onclick=()=>{close();storyStart();};const k=el('button','btn yellow grow','Về Nói');k.onclick=()=>{close();go('talk');};r.appendChild(a);r.appendChild(k);m.appendChild(r);});}

/* ---- 1) Đấu thoại (AI turn-based) ---- */
let TB=null;
function battleRules(sc){const lvl=(loadApp().cfg||{}).level||'A2';return 'You are Minh, a friendly senior developer, doing an English speaking battle with a Vietnamese junior developer (CEFR '+lvl+'). Scenario: '+sc+' Each turn: (1) reply IN CHARACTER in 1-2 short simple sentences ending with a question; (2) on a new line write exactly "SCORE: n" where n is 0-10 rating the user\'s LAST message for clarity, grammar and relevance (be fair, 7+ means good); (3) on a new line starting with "FIX:", up to 2 corrections as: wrong => right ~ short Vietnamese note (full diacritics), or exactly "FIX: OK". For the very first turn (no user message yet) write SCORE: 0 and FIX: OK.';}
function parseBattle(t){const s=(t.match(/SCORE:\s*(\d+)/)||[])[1];const fi=t.indexOf('FIX:');const si=t.search(/SCORE:/);let reply=t;if(si>=0)reply=t.slice(0,si);else if(fi>=0)reply=t.slice(0,fi);return {reply:reply.trim(),score:s!=null?Math.max(0,Math.min(10,+s)):null,fix:fi>=0?t.slice(fi+4).trim():''};}
function talkBattleStart(){
  if(!aiConfigured()){openModal((m,close)=>{m.innerHTML='<div class="h" style="font-size:20px">Cần AI</div><div class="mascot-row" style="margin-top:12px"><div class="mascot">'+mascot('think')+'</div><div class="bubble grow"><span class="who">Mochi</span>Chế độ này cần AI chấm câu. Mở app › Giao tiếp AI › <b>Cài đặt AI</b> để nhập key (Gemini miễn phí), game sẽ dùng chung.</div></div>';const r=el('div','row');r.style.cssText='gap:10px;margin-top:14px';const a=el('button','btn ghost grow','Đóng');a.onclick=close;const k=el('button','btn grow','Mở app');k.onclick=openApp;r.appendChild(a);r.appendChild(k);m.appendChild(r);});return;}
  if(G.hp<=0)G.hp=Math.ceil(G.maxHp/2);
  document.body.classList.add('infight');TB={sc:rnd(SCEN),turns:[],user:0,bossHp:300,combo:0,busy:false};cur='talk';main.innerHTML='';
  talkHeader('ĐẤU THOẠI · AI','Minh-senpai · 6 lượt','<div class="row" style="gap:8px;margin-top:8px"><small style="font-family:var(--mono);font-size:10.5px;color:var(--faint)">HP</small><div class="bar hp grow" id="tbhp"><i style="width:'+Math.round(G.hp/G.maxHp*100)+'%"></i></div></div>');
  const vn=el('div','vn');vn.innerHTML='<div class="scene"><div class="bosshp"><div class="bar mon" id="tbboss"><i style="width:100%"></i><span>BOSS 300</span></div></div><div class="combo" style="top:36px" id="tbcombo">COMBO x0</div><div class="npc" id="npc">'+npc('minh')+'</div></div><div class="box"><span class="name">Minh-senpai</span><div class="txt" id="vtxt"><span class="muted">…</span></div></div>';main.appendChild(vn);
  const tips=el('div');tips.id='tips';tips.style.cssText='display:flex;flex-direction:column;gap:8px';main.appendChild(tips);
  const mic=micButton('🎤 Bấm rồi nói',b=>{if(TB.busy)return;b.textContent='● Đang nghe…';b.classList.add('rec');listenOnce(t=>{b.textContent='🎤 Bấm rồi nói';b.classList.remove('rec');tbSend(t);},st=>{b.textContent='🎤 Bấm rồi nói';b.classList.remove('rec');if(st==='nosr')toast('Không có mic — gõ bên dưới');},7000);});
  main.appendChild(mic);main.appendChild(typeFallback('…hoặc gõ câu trả lời',t=>tbSend(t)));
  (async()=>{try{const t=await aiCall(battleRules(TB.sc),[{role:'user',content:'Start the conversation now with your first line.'}]);const p=parseBattle(t);TB.turns.push({role:'assistant',content:t});npcSay(p.reply);}catch(e){toast('AI lỗi: '+(e.message||''));}})();
}
async function tbSend(t){
  if(!TB||TB.busy||!t)return;TB.busy=true;TB.user++;TB.turns.push({role:'user',content:t});$('#vtxt').innerHTML='<span class="muted">Senpai đang nghĩ…</span>';
  try{const out=await aiCall(battleRules(TB.sc),TB.turns);const p=parseBattle(out);TB.turns.push({role:'assistant',content:out});
    const sc=p.score==null?5:p.score;const npcEl=$('#npc');
    if(sc>=7){TB.combo++;}else TB.combo=0;
    const dmg=sc*10+Math.min(TB.combo,5)*5;TB.bossHp=Math.max(0,TB.bossHp-dmg);
    const bb=$('#tbboss');bb.querySelector('i').style.width=Math.round(TB.bossHp/300*100)+'%';bb.querySelector('span').textContent='BOSS '+TB.bossHp;
    const cb=$('#tbcombo');cb.textContent='COMBO x'+TB.combo;cb.classList.remove('big');void cb.offsetWidth;cb.classList.add('big');
    const r=npcEl.getBoundingClientRect();fxText(r.left+r.width/2,r.top+30,'-'+dmg);
    if(sc>=7){sfx.ok();npcEl.classList.add('shaking');setTimeout(()=>npcEl.classList.remove('shaking'),400);}
    if(sc<4){G.hp=Math.max(0,G.hp-15);sfx.bad();flashRed();const hb=$('#tbhp');if(hb)hb.querySelector('i').style.width=Math.round(G.hp/G.maxHp*100)+'%';}
    gainXp(sc*3,sc);
    const tip=el('div','tip');tip.innerHTML='<b>Điểm câu vừa rồi: '+sc+'/10</b>'+(p.fix&&p.fix.replace(/[.\s]/g,'')!=='OK'?p.fix.split('\n').filter(Boolean).map(l=>{const m=l.match(/^(.*?)=>(.*?)(?:~(.*))?$/);return m?'<span class="fixl"><s>'+esc(m[1].trim())+'</s> → <b class="r">'+esc(m[2].trim())+'</b>'+(m[3]?' <span class="muted">('+esc(m[3].trim())+')</span>':'')+'</span>':'<span class="fixl">'+esc(l)+'</span>';}).join(''):'<span class="fixl">✓ Câu ổn!</span>');$('#tips').prepend(tip);
    saveG();
    if(TB.bossHp<=0||G.hp<=0||TB.user>=6){tbEnd();return;}
    npcSay(p.reply);
  }catch(e){toast('AI lỗi, thử lại');TB.user--;TB.turns.pop();}
  TB.busy=false;
}
function tbEnd(){const win=TB.bossHp<=0;const dealt=300-TB.bossHp;const stars=win?(TB.user<=4?3:2):1;TB=null;if(win){G.talk.battleWins++;G.bossWins++;daily().boss++;gainXp(160+stars*40,80);sfx.win();confetti();}else{sfx.bad();if(G.hp<=0)G.hp=Math.ceil(G.maxHp/2);}saveG();checkBadges();
  openModal((m,close)=>{m.innerHTML='<div class="eyebrow" style="text-align:center">'+(win?'THẮNG ĐẤU THOẠI':'CHƯA THẮNG')+'</div>'+(win?'<div class="stars3">'+'★'.repeat(stars)+'<span style="opacity:.25">'+'★'.repeat(3-stars)+'</span></div>':'')+'<div class="big" style="font-size:24px">Gây '+dealt+'/300 sát thương</div><div class="mascot-row" style="margin-top:12px"><div class="mascot">'+mascot(win?'cheer':'think')+'</div><div class="bubble grow"><span class="who">Mochi</span>'+(win?'Nói chuẩn là boss ngã ngay!':'Câu ≥7 điểm mới đau. Nói câu đầy đủ, đúng thì, có từ khoá nhé.')+'</div></div>';const r=el('div','row');r.style.cssText='gap:10px;margin-top:14px';const a=el('button','btn ghost grow','Đấu lại');a.onclick=()=>{close();talkBattleStart();};const k=el('button','btn yellow grow','Về Nói');k.onclick=()=>{close();go('talk');};r.appendChild(a);r.appendChild(k);m.appendChild(r);});}

/* ---- 5) Trang bị cho Mochi ---- */
function vEquip(){
  main.innerHTML='';cur='talk';talkHeader('TRANG BỊ CHO MOCHI',G.talk.equipped.length+' câu · +'+equipBonus()+' xu/giờ khi AFK');
  const c=el('div','card');c.innerHTML='<div class="mascot-row"><div class="mascot">'+mascot('happy')+'</div><div class="bubble grow"><span class="who">Mochi</span>Mỗi câu bạn <b>đọc theo đạt ≥ 80%</b> mình sẽ học thuộc và nói khi đi cày. Mỗi câu +1 xu/giờ (tối đa 40).</div></div>';main.appendChild(c);
  const go_=el('button','btn blue block','🎵 Đi đọc theo nhịp để trang bị thêm');go_.onclick=shadowStart;main.appendChild(go_);
  if(G.talk.equipped.length){const l=el('div','card');l.innerHTML='<div class="eyebrow">Câu Mochi đã thuộc</div>';const ul=el('div');ul.style.cssText='display:flex;flex-direction:column;gap:8px;margin-top:10px';
    G.talk.equipped.slice().reverse().forEach(s=>{const r=el('div','eq');r.innerHTML='<span class="grow">'+esc(s)+'</span>';const pb=el('button','btn ghost sm','🔊');pb.onclick=()=>speak(s);r.appendChild(pb);ul.appendChild(r);});l.appendChild(ul);main.appendChild(l);}
  else main.appendChild(el('p','muted','Chưa có câu nào. Đọc theo nhịp đạt 80%+ là có ngay!'));
}

/* ---------- SHOP ---------- */
function vShop(){
  main.innerHTML='';
  const h=el('div','card');h.innerHTML='<div class="row between"><div><div class="eyebrow">Shop nâng cấp</div><b class="h" style="font-size:18px">Tiêu xu cho mạnh hơn</b></div><span class="coins"><i></i>'+G.coins+'</span></div><div class="mascot-row" style="margin-top:12px"><div class="mascot">'+mascot('think')+'</div><div class="bubble grow"><span class="who">Mochi</span>Xu kiếm được từ trận đánh và lúc AFK. Nâng "cày nhanh hơn" sớm là lời nhất đó!</div></div>';
  main.appendChild(h);
  const list=el('div');list.style.cssText='display:flex;flex-direction:column;gap:10px';
  SHOP.forEach(it=>{const key=it[0],isItem=key==='hint'||key==='potion';const k=isItem?0:(G.up[key]||0);const max=it[5];const cost=it[4](k);const maxed=!isItem&&k>=max;
    const r=el('div','shopi');
    r.innerHTML='<span class="qi">'+it[1]+'</span><span class="grow"><b>'+it[2]+(isItem?' <span class="kbd">có '+G.items[key]+'</span>':maxed?' <span class="kbd">MAX</span>':' <span class="kbd">Lv '+k+'/'+(max>=99?'∞':max)+'</span>')+'</b><small>'+it[3]+'</small></span>';
    const b=el('button','btn sm '+(maxed?'ghost':G.coins>=cost?'yellow':'ghost'),maxed?'—':'🪙 '+cost);b.disabled=maxed||G.coins<cost;
    b.onclick=()=>{if(G.coins<cost)return;G.coins-=cost;if(isItem){it[6]();}else{G.up[key]=k+1;if(it[6])it[6]();}saveG();paintCoins();sfx.ok();toast('Đã mua: '+it[2]);vShop();};
    r.appendChild(b);list.appendChild(r);});
  main.appendChild(list);
}
/* ---------- PROFILE (mobile-first) ---------- */
const RANKS=[[1,'Tập sự'],[3,'Junior Dev'],[6,'Mid Dev'],[10,'Senior Dev'],[15,'Tech Lead'],[20,'Kiến trúc sư']];
function rankName(){let r=RANKS[0][1];RANKS.forEach(x=>{if(G.lv>=x[0])r=x[1];});return r;}
function setRow(icon,label,value,onClick,cls){const r=el(onClick?'button':'div','srow'+(cls?' '+cls:''));r.innerHTML='<span class="si">'+icon+'</span><span class="sl">'+label+'</span><span class="sv">'+(value||'')+'</span>'+(onClick?'<span class="sc">›</span>':'');if(onClick)r.onclick=onClick;return r;}
function toggleRow(icon,label,on,onChange){const r=el('div','srow');r.innerHTML='<span class="si">'+icon+'</span><span class="sl">'+label+'</span>';const t=el('button','sw'+(on?' on':''));t.setAttribute('role','switch');t.setAttribute('aria-checked',on?'true':'false');t.innerHTML='<i></i>';t.onclick=()=>{onChange(!on);};r.appendChild(t);return r;}
function group(title,rows){const g=el('div','sgroup');if(title)g.appendChild(el('div','slab',title));const box=el('div','sbox');rows.forEach(r=>box.appendChild(r));g.appendChild(box);return g;}
function vProfile(){
  main.innerHTML='';
  const hero=el('div','card phero');
  hero.innerHTML='<div class="avatar big">'+mascot(G.hp<=30?'sad':'happy')+'</div><div class="pname h">'+esc(G.name)+'</div><div class="row" style="justify-content:center;gap:8px;margin-top:6px"><span class="lv">Lv '+G.lv+'</span><span class="kbd">'+rankName()+'</span></div>'+
    '<div class="pbars"><div><small>HP '+G.hp+'/'+G.maxHp+'</small><div class="bar hp'+(G.hp<=30?' low':'')+'"><i style="width:'+Math.round(G.hp/G.maxHp*100)+'%"></i></div></div><div><small>XP '+G.xp+'/'+xpNeed(G.lv)+'</small><div class="bar xp"><i style="width:'+Math.round(G.xp/xpNeed(G.lv)*100)+'%"></i></div></div></div>';
  main.appendChild(hero);
  const done=clearedDays();
  const stats=el('div','stats');
  [['⚔️',G.wins,'trận thắng'],['👑',G.bossWins,'boss'],['🗓️',done,'ngày xong'],['🔥',G.bestCombo||0,'combo max'],['🎯',G.total?Math.round(G.correct/G.total*100)+'%':'—','chính xác'],['🔥',(G.streak||0),'chuỗi ngày']].forEach(s=>{stats.appendChild(el('div','stile','<div class="ic">'+s[0]+'</div><div class="h n">'+s[1]+'</div><small>'+s[2]+'</small>'));});
  main.appendChild(group('Thống kê',[stats]));
  const g=el('div','badges');BADGES.forEach(x=>{g.appendChild(el('div','badge'+(G.badges[x[0]]?'':' lock'),x[1]+'<small>'+x[2]+'</small>'));});
  main.appendChild(group('Huy hiệu · '+Object.keys(G.badges).length+'/'+BADGES.length,[g]));
  const ai=aiConfigured();
  main.appendChild(group('Tài khoản',[
    setRow('✏️','Tên nhân vật',esc(G.name),()=>openModal((m,close)=>{m.innerHTML='<div class="h" style="font-size:20px">Đổi tên</div>';const i=el('input','input');i.value=G.name;i.maxLength=16;i.style.marginTop='12px';m.appendChild(i);const r=el('div','row');r.style.cssText='gap:10px;margin-top:12px';const c=el('button','btn ghost grow','Huỷ');c.onclick=close;const ok=el('button','btn grow','Lưu');ok.onclick=()=>{G.name=i.value.trim()||'Dev';saveG();close();toast('Đã đổi tên');vProfile();};r.appendChild(c);r.appendChild(ok);m.appendChild(r);setTimeout(()=>i.focus(),50);})),
    setRow('🤖','Boss AI',ai?'<b style="color:var(--green)">sẵn sàng</b>':'chưa có key',ai?null:openApp)
  ]));
  main.appendChild(group('Cài đặt',[
    toggleRow('🔊','Âm thanh',G.sound!==false,v=>{G.sound=v;saveG();vProfile();}),
    toggleRow('🌸','Hoa rơi & hiệu ứng nền',G.fx!==false,v=>{G.fx=v;saveG();document.body.classList.toggle('nofx',!v);vProfile();}),
    setRow('📖','Xem lại hướng dẫn','',tutorial),
    setRow('📱','Mở app học IT English','',openApp)
  ]));
  main.appendChild(group('Dữ liệu',[
    setRow('🗑️','Đặt lại tiến trình game','',()=>openModal((m,close)=>{m.innerHTML='<div class="h" style="font-size:20px">Đặt lại?</div><p class="muted">Xoá toàn bộ XP, xu, huy hiệu, sao. Không ảnh hưởng app học.</p>';const r=el('div','row');r.style.cssText='gap:10px;margin-top:12px';const a=el('button','btn ghost grow','Huỷ');a.onclick=close;const b2=el('button','btn grow','Đặt lại');b2.onclick=()=>{localStorage.removeItem(GKEY);location.reload();};r.appendChild(a);r.appendChild(b2);m.appendChild(r);}),'danger')
  ]));
  main.appendChild(el('p','muted','<small style="font-family:var(--mono);font-size:11px">IT English Quest · dữ liệu lưu trên máy này</small>')).style.textAlign='center';
}
/* ---------- tutorial + offline welcome ---------- */
function tutorial(){
  const steps=[['wink','Chào! Mình là <b>Mochi</b>, bạn đồng hành của bạn. Đây là <b>IT English Quest</b> — học tiếng Anh IT bằng cách… đánh quái!'],
   ['happy','Trên <b>bản đồ</b>, mỗi ngày trong lộ trình là một màn. Mỗi màn có 3 con <b>Bug</b> (từ vựng · ngữ pháp · nghe) và 1 <b>Boss</b>.'],
   ['cheer','Trả lời đúng = gây sát thương + <b>combo</b>. Sai = mất HP. Xong đủ 3 Bug là mở ngày tiếp theo!'],
   ['think','Khi bạn vắng, mình <b>tự cày</b> bug kiếm xu (AFK). Nhớ về <b>thu hoạch</b>, mở <b>rương ngày</b> và ghé <b>Shop</b> nâng cấp nhé!']];
  let i=0;
  openModal((m,close)=>{const draw=()=>{m.innerHTML='<div class="eyebrow">Hướng dẫn '+(i+1)+'/'+steps.length+'</div><div class="mascot-row" style="margin-top:12px"><div class="mascot" style="width:96px;height:96px">'+mascot(steps[i][0])+'</div><div class="bubble grow"><span class="who">Mochi</span>'+steps[i][1]+'</div></div>';
      const b=el('button','btn yellow block',i<steps.length-1?'Tiếp ›':'Bắt đầu chơi!');b.style.marginTop='14px';b.onclick=()=>{if(i<steps.length-1){i++;draw();}else{G.seenTut=true;saveG();close();}};m.appendChild(b);};draw();});
}
function offlineWelcome(){
  const p=idlePending();if(p.ms<15*60e3||p.coins<=0)return false;
  openModal((m,close)=>{m.innerHTML='<div class="eyebrow" style="text-align:center">CHÀO MỪNG TRỞ LẠI</div><div class="mascot-row" style="margin-top:12px"><div class="mascot" style="width:96px;height:96px">'+mascot('cheer')+'</div><div class="bubble grow"><span class="who">Mochi</span>Bạn vắng <b>'+fmtDur(p.ms)+'</b>. Mình đã hạ <b>'+p.bugs+' bug</b> và tích được:</div></div><div class="row" style="justify-content:center;gap:16px;margin-top:14px;font-family:var(--disp);font-weight:700;font-size:22px"><span>🪙 +'+p.coins+'</span><span>✨ +'+p.xp+' XP</span></div>'+(p.capped?'<p class="muted" style="text-align:center;margin-top:8px">Túi đã đầy — nâng "giới hạn offline" ở Shop để tích lâu hơn.</p>':'');
    const b=el('button','btn yellow block','Thu hoạch');b.style.marginTop='14px';b.onclick=()=>{close();collectIdle();confetti();vMap();};m.appendChild(b);});
  return true;
}
/* ---------- boot ---------- */
if(G.fx===false)document.body.classList.add('nofx');
paintCoins();renderTabs();vMap();checkBadges();
if(!G.seenTut){G.idle.last=Date.now();saveG();tutorial();}else offlineWelcome();
})();
