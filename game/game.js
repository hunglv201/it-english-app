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
let G=Object.assign({name:'Dev',lv:1,xp:0,hp:100,maxHp:100,coins:0,combo:0,bestCombo:0,cleared:{},badges:{},cur:1,ch:null,wins:0,correct:0,total:0,bossWins:0,streak:0,lastDay:null},loadG());
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
let AC=null;function beep(f,d,type,v){try{AC=AC||new (window.AudioContext||window.webkitAudioContext)();const o=AC.createOscillator(),g=AC.createGain();o.type=type||'sine';o.frequency.value=f;g.gain.value=v||.05;o.connect(g);g.connect(AC.destination);const t=AC.currentTime;g.gain.setValueAtTime(g.gain.value,t);g.gain.exponentialRampToValueAtTime(.0001,t+d);o.start(t);o.stop(t+d);}catch(e){}}
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
const TABS=[['map','🗺️','Bản đồ'],['profile','👤','Hồ sơ'],['app','📱','App']];
function renderTabs(){const n=$('#tabs');n.innerHTML='';TABS.forEach(t=>{const b=el('button','tab'+(cur===t[0]?' on':''),'<span>'+t[1]+'</span>'+t[2]);b.onclick=()=>{if(t[0]==='app'){location.href='../';return;}go(t[0]);};n.appendChild(b);});}
function go(k){cur=k;renderTabs();window.scrollTo(0,0);({map:vMap,profile:vProfile})[k]();}
function playerCard(){
  const c=el('div','card player');
  c.innerHTML='<div class="avatar">'+mascot(G.hp<=30?'sad':'happy')+'</div><div class="grow stat"><div class="row between"><b class="h" style="font-size:17px">'+esc(G.name)+'</b><span class="lv">Lv '+G.lv+'</span></div>'+
    '<small>HP '+G.hp+'/'+G.maxHp+'</small><div class="bar hp'+(G.hp<=30?' low':'')+'"><i style="width:'+Math.round(G.hp/G.maxHp*100)+'%"></i></div>'+
    '<small>XP '+G.xp+'/'+xpNeed(G.lv)+' · 🔥 chuỗi '+(G.streak||0)+' ngày</small><div class="bar xp"><i style="width:'+Math.round(G.xp/xpNeed(G.lv)*100)+'%"></i></div></div>';
  return c;
}

/* ---------- MAP ---------- */
const TIPS=['Đánh vài con Bug từ vựng lấy XP nhé!','Combo càng cao, XP và xu càng nhiều!','Hạ Boss bằng cách chọn đúng câu trả lời tiếng Anh!','Sai câu nào mất HP đó — cẩn thận nhé!','Hết HP thì nghỉ chút, HP hồi 50% khi chơi lại.','Xong đủ 3 quest là mở ngày tiếp theo!'];
function vMap(){
  main.innerHTML='';touchStreak();saveG();
  main.appendChild(playerCard());
  const mr=el('div','mascot-row');mr.innerHTML='<div class="mascot">'+mascot('wink')+'</div><div class="bubble grow"><span class="who">Mochi</span>'+esc(rnd(TIPS))+'</div>';main.appendChild(mr);
  const c=el('div','card');
  const ch=G.ch;const days=DAYS.filter(d=>d.phase===ch);
  const head=el('div','chapter');
  const prev=el('button','nav','‹');prev.disabled=ch<=0;prev.onclick=()=>{G.ch=Math.max(0,ch-1);saveG();vMap();};
  const next=el('button','nav','›');next.disabled=ch>=PHASES.length-1;next.onclick=()=>{G.ch=Math.min(PHASES.length-1,ch+1);saveG();vMap();};
  const t=el('div','grow','<div class="eyebrow">Chặng '+(ch+1)+' / '+PHASES.length+'</div><div class="h" style="font-size:19px;line-height:1.15">'+esc(PHASES[ch])+'</div>');t.style.textAlign='center';
  head.appendChild(prev);head.appendChild(t);head.appendChild(next);c.appendChild(head);
  const path=el('div','path');
  days.forEach(d=>{
    const n=d.n;const st=G.cleared[n]||{};const done=dayCleared(n);
    const b=el('button','node'+(done?' done':n===G.cur?' cur':n<G.cur?' open':' lock'),String(n));
    if(n>G.cur)b.innerHTML+='<span class="lk">🔒</span>';
    const stars=(st.v||0)+(st.p||0)+(st.l||0)+(st.b||0);if(stars)b.innerHTML+='<span class="st">'+'★'.repeat(Math.min(3,Math.ceil(stars/4)))+'</span>';
    b.onclick=()=>{if(n>G.cur){toast('🔒 Xong ngày '+G.cur+' để mở');return;}questSelect(n);};
    path.appendChild(b);
  });
  c.appendChild(path);main.appendChild(c);
  const jump=el('button','btn blue block','🎯 Tới ngày hiện tại · '+G.cur);jump.onclick=()=>{G.ch=dayInfo(G.cur).phase;saveG();vMap();setTimeout(()=>questSelect(G.cur),50);};main.appendChild(jump);
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
  B={n,type,queue:qs.slice(),total:qs.length,monHp:qs.length*10,monMax:qs.length*10,right:0,wrong:0,combo:0,timer:null,t0:0,limit:type==='l'?15:12,cur:null,locked:false};
  G.combo=0;cur='battle';renderTabs();window.scrollTo(0,0);vBattle();nextQ();
}
function vBattle(){
  main.innerHTML='';const a=el('div','arena');
  const top=el('div','card');top.style.padding='12px 14px';
  top.innerHTML='<div class="row between"><div class="row" style="gap:8px"><span class="avatar" style="width:40px;height:40px;border-radius:12px">'+mascot('happy')+'</span><div class="grow" style="min-width:120px"><small style="font-family:var(--mono);font-size:10.5px;color:var(--faint)">HP <b id="php">'+G.hp+'</b>/'+G.maxHp+'</small><div class="bar hp" id="phpbar"><i style="width:'+Math.round(G.hp/G.maxHp*100)+'%"></i></div></div></div><button class="btn ghost sm" id="quitB">✕ Rút lui</button></div>';
  a.appendChild(top);
  const mon=el('div','card');mon.style.background='linear-gradient(180deg,#2a2160,#1b1147)';
  mon.innerHTML='<div class="combo" id="combo">COMBO x0</div><div class="monster" id="mon"><div class="mname">'+MON[B.type][0]+' · Ngày '+B.n+'</div><div class="art">'+bug()+'</div><div style="width:100%;padding:0 6px"><div class="bar mon" id="monbar"><i style="width:100%"></i><span id="montxt">'+B.monHp+' / '+B.monMax+'</span></div></div></div>';
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
  const q=B.cur=B.queue.shift();B.locked=false;
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
  const q=B.cur;const ok=o===q.ans;B.total;G.total++;
  document.querySelectorAll('.opt').forEach(b=>{b.disabled=true;if(b.textContent===q.ans)b.classList.add('good');});
  const monEl=$('#mon');
  if(ok){
    B.right++;G.correct++;B.combo++;G.combo=B.combo;G.bestCombo=Math.max(G.bestCombo||0,B.combo);
    const dmg=10;B.monHp=Math.max(0,B.monHp-dmg);
    sfx.ok();monEl.classList.remove('hit');void monEl.offsetWidth;monEl.classList.add('hit');
    const r=monEl.getBoundingClientRect();fxText(r.left+r.width/2+(Math.random()*60-30),r.top+40,'-'+dmg+(B.combo>=3?' ✦':''));
    const cb=$('#combo');cb.textContent='COMBO x'+B.combo;cb.classList.remove('big');void cb.offsetWidth;cb.classList.add('big');
    const xp=10+Math.min(B.combo,10)*2;gainXp(xp,5);
  }else{
    if(btn)btn.classList.add('bad');B.wrong++;B.combo=0;G.combo=0;$('#combo').textContent='COMBO x0';
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
  G.wins++;const bonus=50+stars*20;gainXp(bonus,20+stars*10);
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
  V={n,rounds,i:0,bossHp:100,right:0};cur='boss';renderTabs();window.scrollTo(0,0);vBoss();bossRound();
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
  const nb=el('button','btn yellow block','Tiếp ›');nb.style.marginTop='4px';nb.onclick=()=>{V.i++;bossRound();};$('#choices').appendChild(nb);
}
function defeatBoss(){openModal((m,close)=>{m.innerHTML='<div class="eyebrow" style="text-align:center;color:var(--red)">HẾT HP</div><div class="big" style="font-size:24px">Senpai thắng lần này…</div><div class="mascot-row" style="margin-top:14px"><div class="mascot">'+mascot('sad')+'</div><div class="bubble grow"><span class="who">Mochi</span>Đọc kỹ phản hồi rồi thử lại nhé. HP hồi 50%.</div></div>';G.hp=Math.ceil(G.maxHp/2);saveG();const b=el('button','btn block','Về bản đồ');b.style.marginTop='14px';b.onclick=()=>{close();go('map');};m.appendChild(b);});}
function bossEnd(){
  const win=V.bossHp<=0;const stars=V.right>=3?3:V.right>=2?2:1;const n=V.n;V=null;
  if(win){const st=G.cleared[n]||(G.cleared[n]={});st.b=Math.max(st.b||0,stars);G.bossWins++;gainXp(120+stars*30,60);sfx.win();confetti();}else sfx.bad();
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
function aiConfigured(){return !!aiCfg();}
async function aiCall(system,msgs){
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
  const sc=rnd(SCEN);V={n,ai:true,sc,turns:[],user:0,bossHp:60};cur='boss';renderTabs();window.scrollTo(0,0);
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
    if(win){const st=G.cleared[n]||(G.cleared[n]={});st.b=Math.max(st.b||0,stars);G.bossWins++;gainXp(150+stars*40,80);sfx.win();confetti();}else sfx.bad();
    saveG();checkBadges();
    openModal((m,close)=>{m.innerHTML='<div class="eyebrow" style="text-align:center">'+(win?'BOSS AI BỊ HẠ':'CHƯA HẠ ĐƯỢC')+'</div><div class="big">'+sc+'<span style="font-size:20px;color:var(--muted)">/10</span></div>'+(win?'<div class="stars3">'+'★'.repeat(stars)+'</div>':'')+'<div class="mascot-row" style="margin-top:12px"><div class="mascot">'+mascot(win?'cheer':'think')+'</div><div class="bubble grow"><span class="who">Mochi</span>'+esc(r.tip||(win?'Quá đỉnh!':'Cần ≥ 6 điểm. Thử lại nhé!'))+'</div></div>';const b=el('button','btn yellow block','Về ngày '+n);b.style.marginTop='14px';b.onclick=()=>{close();go('map');questSelect(n);};m.appendChild(b);});
  }catch(e){toast('AI lỗi khi chấm');$('#endB').disabled=false;}
}

/* ---------- PROFILE ---------- */
function vProfile(){
  main.innerHTML='';main.appendChild(playerCard());
  const c=el('div','card');
  const done=Object.keys(G.cleared).filter(n=>dayCleared(+n)).length;
  c.innerHTML='<div class="eyebrow">Thống kê</div><div class="row" style="flex-wrap:wrap;gap:8px;margin-top:10px">'+[['⚔️',G.wins,'trận thắng'],['👑',G.bossWins,'boss'],['🗓️',done,'ngày xong'],['🔥',G.bestCombo||0,'combo max'],['🎯',G.total?Math.round(G.correct/G.total*100)+'%':'—','chính xác'],['🪙',G.coins,'xu']].map(s=>'<div style="flex:1 1 30%;background:var(--panel2);border:3px solid var(--stroke);border-radius:14px;padding:10px;text-align:center;box-shadow:0 4px 0 var(--stroke)"><div style="font-size:20px">'+s[0]+'</div><div class="h" style="font-size:20px">'+s[1]+'</div><small class="muted">'+s[2]+'</small></div>').join('')+'</div>';
  main.appendChild(c);
  const b=el('div','card');b.innerHTML='<div class="eyebrow">Huy hiệu · '+Object.keys(G.badges).length+'/'+BADGES.length+'</div>';const g=el('div','badges');g.style.marginTop='10px';
  BADGES.forEach(x=>{const d=el('div','badge'+(G.badges[x[0]]?'':' lock'),x[1]+'<small>'+x[2]+'</small>');g.appendChild(d);});b.appendChild(g);main.appendChild(b);
  const s=el('div','card');s.innerHTML='<div class="eyebrow">Cài đặt</div>';
  const nm=el('input','input');nm.value=G.name;nm.placeholder='Tên nhân vật';nm.style.marginTop='10px';nm.onchange=()=>{G.name=nm.value.trim()||'Dev';saveG();toast('Đã đổi tên');};s.appendChild(nm);
  const ai=aiConfigured();s.appendChild(el('p','muted','🤖 Boss AI: '+(ai?'<b style="color:var(--green)">sẵn sàng</b> (dùng key từ app)':'chưa cấu hình — mở app › Giao tiếp AI › Cài đặt AI')));
  const rs=el('button','btn ghost block sm','Đặt lại tiến trình game');rs.onclick=()=>openModal((m,close)=>{m.innerHTML='<div class="h" style="font-size:20px">Đặt lại?</div><p class="muted">Xoá toàn bộ XP, huy hiệu, sao. Không ảnh hưởng app học.</p>';const r=el('div','row');r.style.gap='10px';const a=el('button','btn ghost grow','Huỷ');a.onclick=close;const b2=el('button','btn grow','Đặt lại');b2.onclick=()=>{localStorage.removeItem(GKEY);location.reload();};r.appendChild(a);r.appendChild(b2);m.appendChild(r);});
  s.appendChild(rs);main.appendChild(s);
}

/* ---------- boot ---------- */
paintCoins();renderTabs();vMap();checkBadges();
})();
