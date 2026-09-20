// K3: bộ test Playwright mobile (375×667). Chạy: tests/run.sh  — xem tests/README.md
const pw=await import(process.env.PLAYWRIGHT_MODULE||'playwright');const chromium=pw.chromium||pw.default.chromium;
import path from 'path';import {fileURLToPath} from 'url';
export const BASE=process.env.BASE_URL||'http://localhost:8765/';
export const OUT=process.env.SHOTS_DIR||path.join(path.dirname(fileURLToPath(import.meta.url)),'shots');
import fs from 'fs'; fs.mkdirSync(OUT,{recursive:true});
export async function launch(){return chromium.launch(process.env.CHROMIUM_PATH?{executablePath:process.env.CHROMIUM_PATH}:{});}
// opts: {store, game, ai:(input,opts)=>text (serialized fn source), aiJson, w,h}
export async function page(b,o={}){
  const ctx=await b.newContext({viewport:{width:o.w||375,height:o.h||667},deviceScaleFactor:2,serviceWorkers:'block'});
  const p=await ctx.newPage();p.errs=[];
  p.on('pageerror',e=>p.errs.push('[err] '+e.message));
  p.on('console',m=>{if(m.type()==='error'&&!/ERR_|Failed to load resource|fonts\.g/.test(m.text()))p.errs.push('[con] '+m.text());});
  await p.route(/fonts\.(googleapis|gstatic)\.com/,r=>r.abort());
  await p.addInitScript(({store,game,ai,aiJson,claude})=>{
    const f={cancel(){},getVoices(){return[];},onvoiceschanged:null,addEventListener(){},speaking:false,pending:false,pause(){},resume(){},speak(u){setTimeout(()=>{u.onstart&&u.onstart();u.onend&&u.onend();},5);}};
    try{Object.defineProperty(window,'speechSynthesis',{configurable:true,get(){return f;}});}catch(e){}
    window.SpeechSynthesisUtterance=function(t){this.text=t;};
    if(!sessionStorage.getItem('__init')){sessionStorage.setItem('__init','1');
      localStorage.clear();
      if(store)localStorage.setItem('it-english-v1',JSON.stringify(store));
      if(game)localStorage.setItem('it-english-game-v1',JSON.stringify(game));}
    window.__calls=[];
    if(claude){
      const aiFn=ai?new Function('input','opts',ai):(()=>'OK');
      const jsonFn=aiJson?new Function('prompt',aiJson):(()=>[]);
      const sp=async(input,opts)=>{window.__calls.push({input,opts});const t=aiFn(input,opts);if(opts&&opts.onText)opts.onText({text:t,delta:t});return {text:t,truncated:false};};
      sp.json=async(prompt,opts)=>{window.__calls.push({prompt,opts,json:true});return jsonFn(prompt);};
      window.claude={use:async(n)=>n==='sample'?sp:null};
    }
  },{store:o.store||null,game:o.game||null,ai:o.ai||null,aiJson:o.aiJson||null,claude:o.claude!==false});
  return p;
}
export const baseStore=(extra={})=>Object.assign({days:{cur:5,done:{1:true,2:true,3:true,4:true}},cfg:{level:'A2',autoSpeak:false},stats:{placed:true,sundayShown:'x'},srs:{},hist:{},myVocab:[]},extra);
export async function shot(p,name){await p.screenshot({path:OUT+'/'+name+'.png'});}
export function report(p,label){console.log(label,'ERRORS:',p.errs.length?('\n  '+p.errs.join('\n  ')):'none');}
