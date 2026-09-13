#!/usr/bin/env python3
import base64, gzip
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'data'/'cofre_dos_numeros.gz.b64'

HTML=r'''<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,maximum-scale=1,user-scalable=no,viewport-fit=cover">
<title>Cofre dos Números</title>
<style>
:root{--bg:#f6f4ee;--card:#fff;--panel:#fbfaf6;--text:#292622;--muted:#77736b;--line:#ded9ce;--purple:#3c3489;--blue:#378add;--orange:#ef9f27;--green:#639922;--red:#e24b4a;--shadow:0 14px 38px rgba(41,36,22,.12)}
[data-theme=dark]{--bg:#181817;--card:#262522;--panel:#211f1d;--text:#f5f2ea;--muted:#aaa69c;--line:#45423b;--purple:#9b94f2;--blue:#5ca7e6;--orange:#f3b350;--green:#85b451;--red:#e96b6a;--shadow:0 14px 38px rgba(0,0,0,.32)}
*{box-sizing:border-box;-webkit-tap-highlight-color:transparent}html,body{margin:0;min-height:100%;background:var(--bg);color:var(--text);font-family:system-ui,-apple-system,"Segoe UI",sans-serif}body{min-height:100vh;min-height:100dvh;display:grid;place-items:center;padding:max(14px,env(safe-area-inset-top)) max(12px,env(safe-area-inset-right)) max(14px,env(safe-area-inset-bottom)) max(12px,env(safe-area-inset-left))}.card{width:min(96vw,560px);background:var(--card);border:1px solid var(--line);border-radius:25px;padding:20px;box-shadow:var(--shadow);position:relative}.theme{position:absolute;right:15px;top:15px;width:42px;height:42px;border-radius:50%;border:1px solid var(--line);background:var(--panel);color:var(--text);font-size:20px;cursor:pointer;touch-action:manipulation}h1{font-size:27px;margin:2px 48px 4px 0;color:var(--purple)}.sub{margin:0 48px 16px 0;color:var(--muted);font-size:14px;line-height:1.4}.stats{display:grid;grid-template-columns:repeat(4,1fr);gap:7px;margin-bottom:12px}.stat{background:var(--panel);border:1px solid var(--line);border-radius:14px;padding:8px 4px;text-align:center}.stat small{display:block;color:var(--muted);font-size:10px;font-weight:800}.stat strong{display:block;font-size:18px;margin-top:2px}.vault{border:2px solid var(--line);background:linear-gradient(145deg,var(--panel),var(--card));border-radius:22px;padding:16px;margin-bottom:12px;text-align:center}.dial{width:86px;height:86px;border-radius:50%;margin:0 auto 10px;display:grid;place-items:center;font-size:40px;background:var(--purple);color:#fff;border:8px double rgba(255,255,255,.55);box-shadow:inset 0 0 0 3px rgba(0,0,0,.14)}.range{font-weight:900;color:var(--purple);font-size:14px}.hint{min-height:48px;display:flex;align-items:center;justify-content:center;font-weight:850;font-size:16px;line-height:1.3;margin:8px auto 0;padding:8px 10px;border-radius:14px;background:color-mix(in srgb,var(--blue) 9%,var(--panel));border:1px solid color-mix(in srgb,var(--blue) 25%,var(--line))}.display{display:flex;align-items:center;justify-content:center;gap:8px;margin:12px 0}.screen{min-width:155px;min-height:60px;border:2px solid var(--line);border-radius:16px;background:#19231b;color:#b9f79e;display:grid;place-items:center;padding:7px 12px;font:900 30px/1 ui-monospace,SFMono-Regular,Menlo,monospace;letter-spacing:.05em;box-shadow:inset 0 3px 12px rgba(0,0,0,.35)}.screen.empty{color:#78906e}.adjust{display:grid;gap:5px}.mini{width:44px;height:28px;border:1px solid var(--line);border-radius:9px;background:var(--panel);color:var(--text);font-weight:900;cursor:pointer;touch-action:manipulation}.keypad{display:grid;grid-template-columns:repeat(3,1fr);gap:8px}.virtual-key{min-height:58px;border:1px solid var(--line);border-radius:15px;background:var(--panel);color:var(--text);font-size:22px;font-weight:900;cursor:pointer;touch-action:manipulation;user-select:none}.virtual-key:active,.mini:active,.action:active{transform:scale(.96)}.virtual-key.utility{font-size:16px;color:var(--purple)}.actions{display:grid;grid-template-columns:1fr 1.4fr;gap:8px;margin-top:9px}.action{min-height:52px;border:0;border-radius:15px;font-size:16px;font-weight:900;cursor:pointer;touch-action:manipulation}.clear{background:var(--panel);border:1px solid var(--line);color:var(--text)}.try{background:var(--green);color:#fff}.try:disabled{opacity:.45}.start{width:100%;margin-top:10px;min-height:52px;border:0;border-radius:15px;background:var(--purple);color:#fff;font-weight:900;font-size:16px;cursor:pointer;touch-action:manipulation}.help{text-align:center;color:var(--muted);font-size:11px;line-height:1.4;margin-top:10px}.flash{animation:flash .35s ease}@keyframes flash{50%{transform:scale(1.04)}}@media(max-width:430px){body{padding:8px}.card{padding:15px;border-radius:20px}h1{font-size:24px}.stats{grid-template-columns:repeat(2,1fr)}.virtual-key{min-height:54px}.vault{padding:13px}.dial{width:72px;height:72px;font-size:34px}.screen{min-width:135px;font-size:27px}}
</style>
</head>
<body>
<main class="card">
<button class="theme" id="theme" aria-label="Alternar tema">🌙</button>
<h1>🔐 Cofre dos Números</h1>
<p class="sub">Descubra o número secreto usando as pistas de <strong>maior</strong> e <strong>menor</strong>.</p>
<div class="stats">
 <div class="stat"><small>FASE</small><strong id="phase">1</strong></div>
 <div class="stat"><small>TENTATIVAS</small><strong id="tries">0</strong></div>
 <div class="stat"><small>PONTOS</small><strong id="score">0</strong></div>
 <div class="stat"><small>RECORDE</small><strong id="record">0</strong></div>
</div>
<section class="vault">
 <div class="dial" id="dial">🔒</div>
 <div class="range" id="range">O segredo está entre 1 e 20</div>
 <div class="hint" id="hint">Toque em “Começar” para criar o segredo.</div>
</section>
<div class="display"><div class="screen empty" id="screen">---</div><div class="adjust"><button class="mini" id="plus" aria-label="Somar um">+1</button><button class="mini" id="minus" aria-label="Subtrair um">−1</button></div></div>
<div class="keypad" id="keypad" aria-label="Teclado numérico">
 <button class="virtual-key" data-digit="1">1</button><button class="virtual-key" data-digit="2">2</button><button class="virtual-key" data-digit="3">3</button>
 <button class="virtual-key" data-digit="4">4</button><button class="virtual-key" data-digit="5">5</button><button class="virtual-key" data-digit="6">6</button>
 <button class="virtual-key" data-digit="7">7</button><button class="virtual-key" data-digit="8">8</button><button class="virtual-key" data-digit="9">9</button>
 <button class="virtual-key utility" id="back">⌫</button><button class="virtual-key" data-digit="0">0</button><button class="virtual-key utility" id="random">🎲</button>
</div>
<div class="actions"><button class="action clear" id="clear">Limpar</button><button class="action try" id="test" disabled>🔓 Testar número</button></div>
<button class="start" id="start">▶ Começar</button>
<div class="help">No celular, use os botões. No computador, o teclado numérico, Backspace, Enter e as setas também funcionam.</div>
</main>
<script>
(()=>{
'use strict';
const LEVELS=[20,50,99,250,500,999];
const phaseEl=document.getElementById('phase'),triesEl=document.getElementById('tries'),scoreEl=document.getElementById('score'),recordEl=document.getElementById('record'),rangeEl=document.getElementById('range'),hintEl=document.getElementById('hint'),screen=document.getElementById('screen'),dial=document.getElementById('dial'),keypad=document.getElementById('keypad'),testBtn=document.getElementById('test'),startBtn=document.getElementById('start'),themeBtn=document.getElementById('theme');
let phase=1,secret=0,input='',tries=0,score=0,running=false,audio=null;
let record=Number(localStorage.getItem('cofre-numeros-record')||0);recordEl.textContent=record;
function beep(freq=440,d=.07,type='sine',vol=.035){try{audio||=new(window.AudioContext||window.webkitAudioContext)();if(audio.state==='suspended')audio.resume();const o=audio.createOscillator(),g=audio.createGain();o.type=type;o.frequency.value=freq;g.gain.setValueAtTime(vol,audio.currentTime);g.gain.exponentialRampToValueAtTime(.001,audio.currentTime+d);o.connect(g).connect(audio.destination);o.start();o.stop(audio.currentTime+d)}catch(_){}}
function maxForPhase(){return LEVELS[Math.min(phase-1,LEVELS.length-1)]}
function update(){phaseEl.textContent=phase;triesEl.textContent=tries;scoreEl.textContent=score;recordEl.textContent=record;const max=maxForPhase();rangeEl.textContent=`O segredo está entre 1 e ${max}`;screen.textContent=input||'---';screen.classList.toggle('empty',!input);testBtn.disabled=!running||!input}
function setInput(v){const max=maxForPhase();let n=Math.max(0,Math.min(max,Number(v)||0));input=n?String(n):'';update()}
function appendDigit(d){if(!running)return;const candidate=(input+d).replace(/^0+/,'');if(!candidate){input='';update();return}const n=Number(candidate);if(n<=maxForPhase()){input=candidate;beep(360,.035);update()}else{beep(150,.07,'square');screen.classList.add('flash');setTimeout(()=>screen.classList.remove('flash'),350)}}
function startRound(){const max=maxForPhase();secret=1+Math.floor(Math.random()*max);input='';tries=0;running=true;dial.textContent='🔒';hintEl.textContent='Qual será o número? Faça sua primeira tentativa!';startBtn.textContent='↻ Novo segredo';update();beep(520,.08,'triangle')}
function win(){running=false;const max=maxForPhase();const bonus=Math.max(20,Math.round(max*1.2)-tries*6);score+=bonus;if(score>record){record=score;localStorage.setItem('cofre-numeros-record',String(record))}dial.textContent='🔓';hintEl.textContent=`🎉 Abriu! Era ${secret}. +${bonus} pontos!`;beep(620,.08,'triangle');setTimeout(()=>beep(820,.12,'triangle'),80);phase++;input='';startBtn.textContent='▶ Próxima fase';update()}
function test(){if(!running||!input)return;const n=Number(input);tries++;if(n===secret){win();return}const diff=Math.abs(secret-n);const max=maxForPhase();const warm=diff<=Math.max(2,Math.floor(max*.08));hintEl.textContent=n<secret?`${warm?'🔥 Quase! ':''}O segredo é MAIOR que ${n} ⬆️`:`${warm?'🔥 Quase! ':''}O segredo é MENOR que ${n} ⬇️`;beep(n<secret?470:250,.08,'triangle');input='';update()}
keypad.addEventListener('click',e=>{const b=e.target.closest('[data-digit]');if(b)appendDigit(b.dataset.digit)});
document.getElementById('back').onclick=()=>{if(!running)return;input=input.slice(0,-1);update()};
document.getElementById('clear').onclick=()=>{input='';update()};
document.getElementById('random').onclick=()=>{if(!running)return;setInput(1+Math.floor(Math.random()*maxForPhase()))};
document.getElementById('plus').onclick=()=>{if(running)setInput((Number(input)||0)+1)};
document.getElementById('minus').onclick=()=>{if(running)setInput(Math.max(1,(Number(input)||1)-1))};
testBtn.onclick=test;startBtn.onclick=startRound;
window.addEventListener('keydown',e=>{if(!running&&e.key!=='Enter')return;if(/^\d$/.test(e.key)){appendDigit(e.key);return}if(e.key==='Backspace'){e.preventDefault();input=input.slice(0,-1);update()}else if(e.key==='Delete'||e.key==='Escape'){input='';update()}else if(e.key==='Enter'){e.preventDefault();running?test():startRound()}else if(e.key==='ArrowUp'||e.key==='ArrowRight'){e.preventDefault();setInput((Number(input)||0)+1)}else if(e.key==='ArrowDown'||e.key==='ArrowLeft'){e.preventDefault();setInput(Math.max(1,(Number(input)||1)-1))}});
function setTheme(t){document.documentElement.dataset.theme=t;themeBtn.textContent=t==='dark'?'☀️':'🌙';localStorage.setItem('cofre-theme',t)}
setTheme(localStorage.getItem('cofre-theme')||(matchMedia('(prefers-color-scheme:dark)').matches?'dark':'light'));themeBtn.onclick=()=>setTheme(document.documentElement.dataset.theme==='dark'?'light':'dark');
update();
})();
</script>
</body>
</html>'''

compressed=gzip.compress(HTML.encode('utf-8'),compresslevel=9,mtime=0)
OUT.write_text(base64.b64encode(compressed).decode('ascii')+'\n',encoding='utf-8')
# sanity check
assert gzip.decompress(base64.b64decode(OUT.read_text().strip())).decode('utf-8').startswith('<!doctype html>')
print('Cofre dos Números reconstruído:',len(HTML),'bytes HTML ->',len(compressed),'bytes gzip')
