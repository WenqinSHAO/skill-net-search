// Desktop/mobile rendering and interaction checks using installed Chrome + native CDP.
import {spawn} from 'node:child_process';
import {mkdtemp, readFile, writeFile, mkdir} from 'node:fs/promises';
import {tmpdir} from 'node:os';
import {dirname, resolve, join} from 'node:path';
import {fileURLToPath, pathToFileURL} from 'node:url';
import {createHash} from 'node:crypto';

const root=resolve(dirname(fileURLToPath(import.meta.url)),'..');
const output=join(root,'output');
const chinese=process.argv.includes('--zh');
const suffix=chinese?'_zh':'';
const reportFile=`tencent_networking_report${suffix}.html`;
const profile=await mkdtemp(join(tmpdir(),'tencent-report-chrome-'));
const chrome=spawn('/opt/google/chrome/chrome',['--headless','--no-sandbox','--disable-gpu','--disable-dev-shm-usage','--no-first-run','--no-default-browser-check','--disable-background-networking','--remote-debugging-port=0',`--user-data-dir=${profile}`,'about:blank'],{stdio:['ignore','ignore','pipe']});
const errors=[];
let socket;
try{
  const endpoint=await new Promise((resolve,reject)=>{
    let log='';
    const timer=setTimeout(()=>reject(new Error('Chrome startup timed out')),20000);
    chrome.stderr.on('data',data=>{log+=data;const m=log.match(/DevTools listening on (ws:\/\/[^\s]+)/);if(m){clearTimeout(timer);resolve(m[1]);}});
    chrome.once('exit',code=>{clearTimeout(timer);reject(new Error(`Chrome exited ${code}: ${log.slice(-1000)}`));});
  });
  socket=new WebSocket(endpoint);
  await new Promise((resolve,reject)=>{socket.onopen=resolve;socket.onerror=reject;});
  let seq=0;const pending=new Map();
  socket.addEventListener('message',event=>{
    const msg=JSON.parse(event.data);
    if(msg.id&&pending.has(msg.id)){const {resolve,reject}=pending.get(msg.id);pending.delete(msg.id);msg.error?reject(new Error(JSON.stringify(msg.error))):resolve(msg.result);}
    if(msg.method==='Runtime.exceptionThrown')errors.push(msg.params.exceptionDetails.text);
    if(msg.method==='Log.entryAdded'&&msg.params.entry.level==='error')errors.push(msg.params.entry.text);
  });
  const send=(method,params={},sessionId)=>new Promise((resolve,reject)=>{const id=++seq;pending.set(id,{resolve,reject});socket.send(JSON.stringify({id,method,params,...(sessionId?{sessionId}:{} )}));});
  const {targetId}=await send('Target.createTarget',{url:'about:blank'});
  const {sessionId}=await send('Target.attachToTarget',{targetId,flatten:true});
  const call=(method,params={})=>send(method,params,sessionId);
  await call('Page.enable');await call('Runtime.enable');await call('Log.enable');
  const evaluate=async expression=>{const result=await call('Runtime.evaluate',{expression,returnByValue:true,awaitPromise:true});if(result.exceptionDetails)throw new Error(JSON.stringify(result.exceptionDetails));return result.result.value;};
  const checks=[];
  const reviewDir=join(output,`report_review${suffix}`);await mkdir(reviewDir,{recursive:true});
  for(const [label,width,height] of [['desktop',1440,1000],['mobile',390,844]]){
    await call('Emulation.setDeviceMetricsOverride',{width,height,deviceScaleFactor:1,mobile:label==='mobile'});
    await call('Page.navigate',{url:pathToFileURL(join(output,reportFile)).href});
    for(let i=0;i<60;i++){
      const ready=await evaluate('document.readyState');
      if(ready==='complete')break;
      await new Promise(resolve=>setTimeout(resolve,100));
    }
    await evaluate('document.fonts.ready');
    const initial=await evaluate(`({viewport:innerWidth,body:document.body.scrollWidth,document:document.documentElement.scrollWidth,cards:document.querySelectorAll('.paper-card').length,figures:document.querySelectorAll('figure svg').length,brokenAnchors:[...document.querySelectorAll('a[href^="#"]')].map(a=>a.getAttribute('href').slice(1)).filter(id=>!document.getElementById(id)),externalAssets:[...document.querySelectorAll('script[src],link[rel="stylesheet"],img[src]')].map(e=>e.src||e.href),documentHeight:document.documentElement.scrollHeight})`);
    if(initial.body>width+1||initial.document>width+1)throw new Error(`${label}: horizontal page overflow ${JSON.stringify(initial)}`);
    if(initial.cards!==32||initial.figures!==7||initial.brokenAnchors.length||initial.externalAssets.length)throw new Error(`${label}: report structure failed ${JSON.stringify(initial)}`);
    const search=await evaluate(`(()=>{const s=document.querySelector('#paper-search');s.value='SwiftEP';s.dispatchEvent(new Event('input'));return {visible:[...document.querySelectorAll('.paper-card')].filter(c=>!c.hidden).length,label:document.querySelector('#search-count').textContent};})()`);
    if(search.visible!==1)throw new Error('Search filter failed');
    let chineseSearch;
    if(chinese){
      chineseSearch=await evaluate(`(()=>{const s=document.querySelector('#paper-search');s.value='孟子立';s.dispatchEvent(new Event('input'));return {visible:[...document.querySelectorAll('.paper-card')].filter(c=>!c.hidden).length,label:document.querySelector('#search-count').textContent};})()`);
      if(chineseSearch.visible<1||chineseSearch.visible===32||!chineseSearch.label.includes('篇论文'))throw new Error('Chinese author search failed');
    }
    await evaluate(`document.querySelector('a[href="#paper-tn-4ab76b7bd3b61a53"]').click()`);
    const reset=await evaluate(`[...document.querySelectorAll('.paper-card')].filter(c=>!c.hidden).length`);
    if(reset!==32)throw new Error('Citation link did not reset search');
    const captures=[];
    for(const [name,selector] of [['overview','.hero'],['topics','#fig-topic_partition'],['geography','#fig-partner_geography'],['deepdive','#topic-dcn_ai']]){
      const scroll=await evaluate(`(()=>{document.documentElement.style.scrollBehavior='auto';const e=document.querySelector(${JSON.stringify(selector)});window.scrollTo(0,e.getBoundingClientRect().top+scrollY-16);return scrollY;})()`);
      const {data}=await call('Page.captureScreenshot',{format:'png',captureBeyondViewport:false});
      const file=`${label}_${name}.png`;await writeFile(join(reviewDir,file),Buffer.from(data,'base64'));captures.push({file,scroll});
    }
    checks.push({viewport:label,width,height,...initial,search,chineseSearch,searchReset:reset,captures});
  }
  const report={status:'passed',language:chinese?'zh-CN':'en',checked_at:new Date().toISOString(),report_sha256:createHash('sha256').update(await readFile(join(output,reportFile))).digest('hex'),browser:'Installed Chrome headless via CDP',checks,console_errors:errors,temporary_browser_profile:profile};
  if(errors.length)throw new Error(`Browser errors: ${JSON.stringify(errors)}`);
  await writeFile(join(output,`report_browser_review${suffix}.json`),JSON.stringify(report,null,2)+'\n');
  console.log(JSON.stringify(report,null,2));
}finally{
  socket?.close();chrome.kill('SIGTERM');
}
