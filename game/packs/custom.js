/* v3.1 — gói "Nghề của tôi": nạp SAU packs/office.gen.js khi store.cfg.track==='custom'.
   Đọc store.customPack (AI tạo 3 chặng theo mô tả công việc, lưu trên máy) rồi ghép vào ĐẦU lộ trình Công sở chung.
   File viết tay (không sinh), build.py tự copy sang game/packs/. */
(function(){
  var s=null;try{s=JSON.parse(localStorage.getItem('it-english-v1')||'null');}catch(e){}
  var cp=s&&s.customPack;var D=window.DATA,P=window.PACK;
  if(!cp||!cp.phases||!cp.phases.length||!D||!P)return;
  var days=[],titles=[];
  cp.phases.forEach(function(ph,pi){
    var vi=[],di=[],li=[],phi=[];
    (ph.vocab||[]).forEach(function(w){vi.push(D.vocab.length);D.vocab.push(w);});
    (ph.phrases||[]).forEach(function(x){phi.push(D.phrases.length);D.phrases.push({en:x.en,vi:x.vi,note:''});});
    (ph.dialogues||[]).forEach(function(x){di.push(D.dialogues.length);D.dialogues.push(x);});
    (ph.listen||[]).forEach(function(x){li.push(D.listen.length);D.listen.push(x);});
    if(!vi.length||!phi.length||!di.length||!li.length)return;
    titles.push(ph.title);var k=titles.length-1;
    for(var dp=0;dp<10;dp++)days.push({phase:k,title:ph.title,v:[vi[(dp*3)%vi.length],vi[(dp*3+1)%vi.length],vi[(dp*3+2)%vi.length]],ph:phi[dp%phi.length],di:di[dp%di.length],li:li[dp%li.length]});
  });
  if(!titles.length)return;
  var n=titles.length;D.days.forEach(function(d){d.phase+=n;});
  D.days=days.concat(D.days);D.days.forEach(function(d,i){d.n=i+1;});
  D.phaseTitles=titles.concat(D.phaseTitles);
  window.PHRASES=cp.phases.map(function(ph){return {name:ph.title,items:(ph.phrases||[]).map(function(x){return {en:x.en,vi:x.vi};})};}).concat(window.PHRASES||[]);
  P.id='custom';P.emoji='✏️';P.label=cp.label||'Nghề của tôi';P.short=cp.short||'Nghề tôi';
  if(cp.persona)P.persona=cp.persona;if(cp.context)P.context=cp.context;
  if(cp.ai&&cp.ai.length)P.ai=cp.ai.concat(P.ai||[]);
  if(cp.rev&&cp.rev.length)P.rev=cp.rev.concat(P.rev||[]);
  P.podcast='Podcast nghề của tôi';P.reverse_tag='kiểu nghề bạn';
  window.CUSTOM_PACK=cp;
})();
