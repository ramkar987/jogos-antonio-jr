# ⌨️ Controles que merecem validação no celular

Trechos gerados automaticamente para ajudar a revisão dos jogos que usam teclado.

## Apaga-Incêndio

`data/apaga_incendio.gz.b64`

```html
.card{width:min(100%,450px);background:var(--card);border-radius:24px;box-shadow:var(--shadow);padding:18px;position:relative;overflow:hidden}.theme-btn{position:absolute;right:14px;top:14px;width:42px;height:42px;border-radius:50%;border:1px solid var(--line);background:var(--card);color:var(--text);font-size:20px;cursor:pointer}
h1{margin:2px 52px 2px 0;color:var(--purple);font-size:28px;line-height:1.05}.subtitle{margin:8px 48px 14px 0;color:var(--muted);font-size:14px;line-height:1.35}.stats{display:grid;grid-template-columns:repeat(3,1fr);gap:8px;margin-bottom:10px}.stat{border:1px solid var(--line);border-radius:14px;padding:8px;text-align:center;background:color-mix(in srgb,var(--card) 92%,var(--blue) 8%)}.stat small{display:block;color:var(--muted);font-size:11px}.stat strong{display:block;font-size:18px;margin-top:1px}
.status{min-height:42px;display:flex;align-items:center;justify-content:center;text-align:center;border-radius:13px;padding:8px 10px;margin-bottom:10px;background:color-mix(in srgb,var(--card) 88%,var(--orange) 12%);font-weight:800;font-size:14px}.meters{display:grid;grid-template-columns:1fr 1fr;gap:8px;margin-bottom:10px}.meter{border:1px solid var(--line);border-radius:12px;padding:7px 9px;background:var(--card)}.meter-label{display:flex;justify-content:space-between;font-size:11px;color:var(--muted);font-weight:800;margin-bottom:5px}.bar{height:9px;border-radius:999px;background:color-mix(in srgb,var(--line) 75%,transparent);overflow:hidden}.fill{height:100%;width:100%;border-radius:inherit;transition:width .12s linear}#waterFill{background:var(--blue)}#pressureFill{background:var(--orange)}
.board-wrap{border-radius:20px;overflow:hidden;border:1px solid var(--line);background:#CBE8F7}svg{display:block;width:100%;height:auto;touch-action:none;user-select:none}.controls{display:grid;grid-template-columns:1fr .88fr 1fr;gap:9px;margin-top:12px}.ctrl{min-height:60px;border:0;border-radius:17px;color:#fff;font-size:15px;font-weight:900;cursor:pointer;touch-action:none;box-shadow:0 4px 0 rgba(0,0,0,.14)}.ctrl:active,.ctrl.active{transform:translateY(2px);box-shadow:0 2px 0 rgba(0,0,0,.14)}.left{background:var(--blue)}.spray{background:var(--orange)}.right{background:var(--red)}.start{width:100%;margin-top:11px;min-height:52px;border:0;border-radius:16px;background:var(--green);color:#fff;font-weight:900;font-size:17px;cursor:pointer}.help,.best{text-align:center;color:var(--muted);font-size:12px;line-height:1.4}.help{margin-top:9px}.best{margin-top:6px}kbd{font:inherit;font-size:11px;border:1px solid var(--line);border-bottom-width:2px;border-radius:6px;padding:1px 5px;background:var(--card)}@media(max-width:390px){.card{padding:14px;border-radius:20px}h1{font-size:25px}.ctrl{min-height:56px;font-size:14px}}
</style>
</head>
<body>
<div class="card">
<button class="theme-btn" id="themeBtn" aria-label="Alternar tema">🌙</button>
<h1>Apaga-Incêndio</h1><div class="subtitle">Mova o bombeiro, mire a mangueira e apague o fogo antes que ele cresça!</div>
<div class="stats"><div class="stat"><small>PONTOS</small><strong id="score">0</strong></div><div class="stat"><small>VIDAS</small><strong id="lives">3</strong></div><div class="stat"><small>FASE</small><strong id="phase">1</strong></div></div>
<div class="status" id="status">Aperte “Iniciar jogo” para começar.</div>
```

```html
<g id="firefighter" filter="url(#shadow)"><circle cx="0" cy="-26" r="13" fill="#F0B989" stroke="#fff" stroke-width="2"/><path d="M-16 -30 Q0 -48 16 -30 L13 -22 L-13 -22 Z" fill="#E24B4A" stroke="#fff" stroke-width="2"/><rect x="-18" y="-14" width="36" height="38" rx="10" fill="#E24B4A" stroke="#fff" stroke-width="3"/><rect x="-20" y="-4" width="8" height="33" rx="4" fill="#F0B989"/><rect x="12" y="-4" width="8" height="33" rx="4" fill="#F0B989"/><rect x="-14" y="22" width="11" height="26" rx="5" fill="#35485B"/><rect x="3" y="22" width="11" height="26" rx="5" fill="#35485B"/><rect x="-21" y="3" width="42" height="6" rx="3" fill="#EF9F27"/></g>
<g id="startMessage"><rect x="76" y="216" width="208" height="72" rx="18" fill="#fff" opacity=".94"/><text x="180" y="246" text-anchor="middle" fill="#3C3489" font-size="18" font-weight="900">PRONTO?</text><text x="180" y="268" text-anchor="middle" fill="#555" font-size="11" font-weight="700">Mire no fogo e jogue água!</text></g>
</svg></div>
<div class="controls"><button class="ctrl left" id="leftBtn">⬅ MOVER</button><button class="ctrl spray" id="sprayBtn">💦 ÁGUA</button><button class="ctrl right" id="rightBtn">MOVER ➡</button></div>
<button class="start" id="startBtn">Iniciar jogo</button><div class="help">Mouse/touch: aponte ou arraste no prédio para mirar e jogar água.<br>Teclado: <kbd>←</kbd>/<kbd>→</kbd> move, <kbd>Q</kbd>/<kbd>E</kbd> mira e <kbd>Espaço</kbd> joga água.</div><div class="best">Melhor pontuação: <strong id="best">0</strong></div>
</div>
<script>
"use strict";
const NS="http://www.w3.org/2000/svg",svg=document.getElementById("game"),windowsEl=document.getElementById("windows"),firesEl=document.getElementById("fires"),smokeEl=document.getElementById("smoke"),bonusesEl=document.getElementById("bonuses"),dropletsEl=document.getElementById("droplets"),firefighterEl=document.getElementById("firefighter"),aimGuide=document.getElementById("aimGuide"),waterJet=document.getElementById("waterJet"),scoreEl=document.getElementById("score"),livesEl=document.getElementById("lives"),phaseEl=document.getElementById("phase"),statusEl=document.getElementById("status"),waterFill=document.getElementById("waterFill"),waterText=document.getElementById("waterText"),pressureFill=document.getElementById("pressureFill"),pressureText=document.getElementById("pressureText"),leftBtn=document.getElementById("leftBtn"),rightBtn=document.getElementById("rightBtn"),sprayBtn=document.getElementById("sprayBtn"),startBtn=document.getElementById("startBtn"),themeBtn=document.getElementById("themeBtn"),bestEl=document.getElementById("best"),startMessage=document.getElementById("startMessage");
const BEST_KEY="apagaIncendioBest",THEME_KEY="kidsGamesTheme";let best=Number(localStorage.getItem(BEST_KEY)||0);bestEl.textContent=best;let audioCtx=null;
function beep(freq=440,duration=.07,type="sine",volume=.04){try{audioCtx||=new(window.AudioContext||window.webkitAudioContext)();if(audioCtx.state==="suspended")audioCtx.resume();const o=audioCtx.createOscillator(),g=audioCtx.createGain();o.type=type;o.frequency.value=freq;g.gain.setValueAtTime(volume,audioCtx.currentTime);g.gain.exponentialRampToValueAtTime(.001,audioCtx.currentTime+duration);o.connect(g).connect(audioCtx.destination);o.start();o.stop(audioCtx.currentTime+duration)}catch(_){}}
function extinguishSound(){beep(620,.06,"triangle");setTimeout(()=>beep(820,.08,"triangle"),55)}function dangerSound(){beep(155,.16,"sawtooth",.035)}function bonusSound(){[520,700
```

```html
function loop(now){if(!state.running)return;const dt=Math.min(2,(now-state.lastTime)/16.6667||1);state.lastTime=now;updateGame(now,dt);drawPlayer(now);updateStats(now);requestAnimationFrame(loop)}
function bindHold(btn,onStart,onStop){const start=e=>{e.preventDefault();onStart()},stop=e=>{if(e)e.preventDefault();onStop()};btn.addEventListener("mousedown",start);btn.addEventListener("mouseup",stop);btn.addEventListener("mouseleave",stop);btn.addEventListener("touchstart",start,{passive:false});btn.addEventListener("touchend",stop,{passive:false});btn.addEventListener("touchcancel",stop,{passive:false})}
bindHold(leftBtn,()=>setMove("left",true),()=>setMove("left",false));bindHold(rightBtn,()=>setMove("right",true),()=>setMove("right",false));bindHold(sprayBtn,()=>setSpray(true),()=>setSpray(false));
const downKeys=new Set();window.addEventListener("keydown",e=>{if(["ArrowLeft","ArrowRight","KeyA","KeyD","KeyQ","KeyE","Space"].includes(e.code))e.preventDefault();if(e.code==="Space"){setSpray(true);return}if(downKeys.has(e.code))return;downKeys.add(e.code);if(e.code==="ArrowLeft"||e.code==="KeyA")setMove("left",true);if(e.code==="ArrowRight"||e.code==="KeyD")setMove("right",true);if(e.code==="KeyQ")rotateAim(-.10);if(e.code==="KeyE")rotateAim(.10)},{passive:false});window.addEventListener("keyup",e=>{downKeys.delete(e.code);if(e.code==="ArrowLeft"||e.code==="KeyA")setMove("left",false);if(e.code==="ArrowRight"||e.code==="KeyD")setMove("right",false);if(e.code==="Space")setSpray(false)});window.addEventListener("blur",()=>{downKeys.clear();setMove("left",false);setMove("right",false);setSpray(false)});
svg.addEventListener("mousemove",e=>{if(!state.running)return;setAimFromClient(e.clientX,e.clientY);if(mouseDown)setSpray(true)});svg.addEventListener("mousedown",e=>{if(!state.running)return;e.preventDefault();mouseDown=true;setAimFromClient(e.clientX,e.clientY);setSpray(true)});window.addEventListener("mouseup",()=>{mouseDown=false;setSpray(false)});
svg.addEventListener("touchstart",e=>{if(!state.running||e.changedTouches.length===0)return;e.preventDefault();const t=e.changedTouches[0];touchId=t.identifier;setAimFromClient(t.clientX,t.clientY);setSpray(true)},{passive:false});svg.addEventListener("touchmove",e=>{if(touchId===null)return;e.preventDefault();const t=[...e.touches].find(v=>v.identifier===touchId);if(!t)return;setAimFromClient(t.clientX,t.clientY);setSpray(true)},{passive:false});svg.addEventListener("touchend",e=>{if(touchId===null)return;e.preventDefault();const ended=[...e.changedTouches].some(v=>v.identifier===touchId);if(ended){touchId=null;setSpray(false)}},{passive:false});svg.addEventListener("touchcancel",e=>{e.preventDefault();touchId=null;setSpray(false)},{passive:false});startBtn.addEventListener("click",startGame);buildWindows();clampAim();drawPlayer(performance.now());updateStats();
</script>
</body></html>
```

## Atravessa a Rua

`jogos/atravessa-a-rua.html`

```html
    display: block;
  }

  .controls {
    display: grid;
    grid-template-columns: repeat(3, 56px);
    grid-template-rows: repeat(2, 56px);
    gap: 6px;
    justify-content: center;
    margin: 0 auto 16px;
  }
  .ctrl-btn {
```

```html
    justify-content: center;
    margin: 0 auto 16px;
  }
  .ctrl-btn {
    border-radius: 12px;
    border: 2px solid var(--key-border);
    background: var(--key-bg);
    color: var(--key-text);
    font-size: 22px;
    cursor: pointer;
    touch-action: manipulation;
    display: flex;
```

```html
    align-items: center;
    justify-content: center;
  }
  .ctrl-btn:active { transform: scale(0.94); background: var(--btn-bg-active); color: #fff; }
  .ctrl-up { grid-column: 2; grid-row: 1; }
  .ctrl-left { grid-column: 1; grid-row: 2; }
  .ctrl-down { grid-column: 2; grid-row: 2; }
  .ctrl-right { grid-column: 3; grid-row: 2; }

  .start-btn {
    width: 100%;
    padding: 15px;
```

## A Aventura de Blinky

`jogos/aventura-do-blinky.html`

```html
    <div class="board" id="board"></div>
  </div>

  <div id="game-controls" class="hidden">
    <div class="program-label">Seu programa (nessa ordem):</div>
    <div class="program-list" id="program-list"></div>

    <div class="block-picker" id="block-picker"></div>

    <div class="action-row">
      <button class="action-btn clear" id="clear-btn">Limpar</button>
      <button class="action-btn play" id="play-btn">▶ Executar</button>
```

```html
  const startBtn = document.getElementById('start');
  const coinsEl = document.getElementById('coins');
  const levelEl = document.getElementById('level');
  const gameControls = document.getElementById('game-controls');
  const programListEl = document.getElementById('program-list');
  const blockPickerEl = document.getElementById('block-picker');
  const clearBtn = document.getElementById('clear-btn');
  const playBtn = document.getElementById('play-btn');

  const GRID = 6;
  const DIRECTIONS = [
    { id: 'up',    symbol: '↑', dr: -1, dc: 0 },
```

```html
        const collected = coins.filter(c => c.collected).length;
        statusEl.textContent = 'Chegou na meta! Moedas: ' + collected + ' de ' + coins.length + ' 🎉';
        gameActive = false;
        gameControls.classList.add('hidden');
        startBtn.classList.remove('hidden');
        startBtn.textContent = 'Próxima fase';
        level++;
        levelEl.textContent = level;
      } else if (!hitWall){
        statusEl.textContent = 'O programa terminou mas não chegou na meta. Ajuste os comandos!';
      }
      renderBoard();
```

## Bichinhos Camuflados — O Mistério das Cores

`data/bichinhos_camuflados_misterio_das_cores.gz.b64`

```html
  const NONE = {id:"none", emoji:"🌿", label:"nenhum"};

  const PALETTES = {
    control: {
      name:"Controle visual",
      bg:["#6e9972","#86ad86","#5f8c67","#96b692"],
      fg:["#294c32","#365c3d","#214329","#426a47"],
      neutral:["#7ca17e","#6f936f"]
    },
    rgA: {
      name:"Vermelho–verde A",
      bg:["#a59a62","#978f59","#afa46b","#8f8959","#b4a76f"],
```

```html

  const PALETTES = {
    control: {
      name:"Controle visual",
      bg:["#6e9972","#86ad86","#5f8c67","#96b692"],
      fg:["#294c32","#365c3d","#214329","#426a47"],
      neutral:["#7ca17e","#6f936f"]
    },
    rgA: {
      name:"Vermelho–verde A",
      bg:["#a59a62","#978f59","#afa46b","#8f8959","#b4a76f"],
      fg:["#ba765f","#b66f59","#c47f69","#ad6854","#bd735e"],
```

```html
  function renderPlate(canvas, trial, easy=false){
    const ctx=canvas.getContext("2d");
    const w=canvas.width,h=canvas.height;
    const pal = easy ? PALETTES.control : PALETTES[trial.group];
    ctx.clearRect(0,0,w,h);
    ctx.fillStyle="#d9ddd3"; ctx.fillRect(0,0,w,h);

    const mask = trial.shape==="none" ? null : buildMask(trial.shape,w,h);
    const dots=[];
    const minR=8,maxR=18;
    let tries=0;

```

## Canhão de Bolinhas

`data/canhao_de_bolinhas.gz.b64`

```html

  startBtn.addEventListener('click', startGame);

  window.addEventListener('keydown', e => {
    if (!running || shot || resolving) return;
    if (e.key === 'ArrowLeft' || e.key.toLowerCase() === 'a') {
      e.preventDefault();
      aimTheta = Math.max(-1.28, aimTheta - .07);
      updateAimVisual();
    } else if (e.key === 'ArrowRight' || e.key.toLowerCase() === 'd') {
      e.preventDefault();
      aimTheta = Math.min(1.28, aimTheta + .07);
```

```html

  window.addEventListener('keydown', e => {
    if (!running || shot || resolving) return;
    if (e.key === 'ArrowLeft' || e.key.toLowerCase() === 'a') {
      e.preventDefault();
      aimTheta = Math.max(-1.28, aimTheta - .07);
      updateAimVisual();
    } else if (e.key === 'ArrowRight' || e.key.toLowerCase() === 'd') {
      e.preventDefault();
      aimTheta = Math.min(1.28, aimTheta + .07);
      updateAimVisual();
    } else if (e.key === ' ' || e.key === 'Enter') {
```

```html
      e.preventDefault();
      aimTheta = Math.max(-1.28, aimTheta - .07);
      updateAimVisual();
    } else if (e.key === 'ArrowRight' || e.key.toLowerCase() === 'd') {
      e.preventDefault();
      aimTheta = Math.min(1.28, aimTheta + .07);
      updateAimVisual();
    } else if (e.key === ' ' || e.key === 'Enter') {
      e.preventDefault();
      startShot();
    }
  });
```

## Cara a Cara

`jogos/cara-a-cara.html`

```html

  <div class="faces-grid" id="faces-grid"></div>

  <div id="game-controls">
    <div class="questions" id="questions"></div>

    <div class="answer-row" id="answer-row">
      <button class="answer-btn yes" id="answer-yes">Sim ✔️</button>
      <button class="answer-btn no" id="answer-no">Não ✖️</button>
    </div>

    <div class="guess-row hidden" id="guess-row">
```

## Código Secreto de Setas

`data/codigo_secreto_de_setas.gz.b64`

```html
.dot{width:14px;height:14px;border-radius:50%;border:2px solid var(--muted);background:transparent;transition:.15s}
.dot.done{background:var(--green);border-color:var(--green);transform:scale(1.06)}
.dot.current{border-color:var(--orange);box-shadow:0 0 0 3px rgba(239,159,39,.16)}
.controls{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;margin-top:14px;align-items:center}
.ctrl{height:62px;border:0;border-radius:17px;background:var(--blue);color:#fff;cursor:pointer;box-shadow:0 5px 0 rgba(0,0,0,.15);display:grid;place-items:center;user-select:none;-webkit-user-select:none;touch-action:manipulation}
.ctrl:active,.ctrl.pressed{transform:translateY(3px);box-shadow:0 2px 0 rgba(0,0,0,.15)}
.ctrl svg{width:34px;height:34px;fill:currentColor}
.ctrl.up{grid-column:2;background:var(--orange)}
.ctrl.left{grid-column:1;grid-row:2;background:var(--blue)}
.ctrl.down{grid-column:2;grid-row:2;background:var(--red)}
.ctrl.right{grid-column:3;grid-row:2;background:var(--green)}
.start{width:100%;margin-top:14px;border:0;border-radius:16px;padding:14px 16px;background:var(--purple);color:white;font-size:17px;font-weight:800;cursor:pointer}
```

```html
.dot.done{background:var(--green);border-color:var(--green);transform:scale(1.06)}
.dot.current{border-color:var(--orange);box-shadow:0 0 0 3px rgba(239,159,39,.16)}
.controls{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;margin-top:14px;align-items:center}
.ctrl{height:62px;border:0;border-radius:17px;background:var(--blue);color:#fff;cursor:pointer;box-shadow:0 5px 0 rgba(0,0,0,.15);display:grid;place-items:center;user-select:none;-webkit-user-select:none;touch-action:manipulation}
.ctrl:active,.ctrl.pressed{transform:translateY(3px);box-shadow:0 2px 0 rgba(0,0,0,.15)}
.ctrl svg{width:34px;height:34px;fill:currentColor}
.ctrl.up{grid-column:2;background:var(--orange)}
.ctrl.left{grid-column:1;grid-row:2;background:var(--blue)}
.ctrl.down{grid-column:2;grid-row:2;background:var(--red)}
.ctrl.right{grid-column:3;grid-row:2;background:var(--green)}
.start{width:100%;margin-top:14px;border:0;border-radius:16px;padding:14px 16px;background:var(--purple);color:white;font-size:17px;font-weight:800;cursor:pointer}
.start:disabled,.ctrl:disabled{opacity:.45;cursor:not-allowed}
```

```html
.dot.current{border-color:var(--orange);box-shadow:0 0 0 3px rgba(239,159,39,.16)}
.controls{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;margin-top:14px;align-items:center}
.ctrl{height:62px;border:0;border-radius:17px;background:var(--blue);color:#fff;cursor:pointer;box-shadow:0 5px 0 rgba(0,0,0,.15);display:grid;place-items:center;user-select:none;-webkit-user-select:none;touch-action:manipulation}
.ctrl:active,.ctrl.pressed{transform:translateY(3px);box-shadow:0 2px 0 rgba(0,0,0,.15)}
.ctrl svg{width:34px;height:34px;fill:currentColor}
.ctrl.up{grid-column:2;background:var(--orange)}
.ctrl.left{grid-column:1;grid-row:2;background:var(--blue)}
.ctrl.down{grid-column:2;grid-row:2;background:var(--red)}
.ctrl.right{grid-column:3;grid-row:2;background:var(--green)}
.start{width:100%;margin-top:14px;border:0;border-radius:16px;padding:14px 16px;background:var(--purple);color:white;font-size:17px;font-weight:800;cursor:pointer}
.start:disabled,.ctrl:disabled{opacity:.45;cursor:not-allowed}
.best{margin-top:10px;text-align:center;color:var(--muted);font-size:12px}
```

## Corrida de Carrinhos

`data/corrida_de_carrinhos.gz.b64`

```html
}
.board-wrap{border-radius:20px;overflow:hidden;border:1px solid var(--line);background:var(--grass)}
svg{display:block;width:100%;height:auto;touch-action:none;user-select:none}
.controls{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-top:12px}
.ctrl{
  min-height:62px;border:0;border-radius:17px;color:#fff;font-size:18px;font-weight:900;
  cursor:pointer;touch-action:none;box-shadow:0 4px 0 rgba(0,0,0,.14)
}
.ctrl:active,.ctrl.active{transform:translateY(2px);box-shadow:0 2px 0 rgba(0,0,0,.14)}
.left{background:var(--blue)} .right{background:var(--red)}
.start{
  width:100%;margin-top:11px;min-height:52px;border:0;border-radius:16px;background:var(--green);
```

```html
.board-wrap{border-radius:20px;overflow:hidden;border:1px solid var(--line);background:var(--grass)}
svg{display:block;width:100%;height:auto;touch-action:none;user-select:none}
.controls{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-top:12px}
.ctrl{
  min-height:62px;border:0;border-radius:17px;color:#fff;font-size:18px;font-weight:900;
  cursor:pointer;touch-action:none;box-shadow:0 4px 0 rgba(0,0,0,.14)
}
.ctrl:active,.ctrl.active{transform:translateY(2px);box-shadow:0 2px 0 rgba(0,0,0,.14)}
.left{background:var(--blue)} .right{background:var(--red)}
.start{
  width:100%;margin-top:11px;min-height:52px;border:0;border-radius:16px;background:var(--green);
  color:#fff;font-weight:900;font-size:17px;cursor:pointer
```

```html
  min-height:62px;border:0;border-radius:17px;color:#fff;font-size:18px;font-weight:900;
  cursor:pointer;touch-action:none;box-shadow:0 4px 0 rgba(0,0,0,.14)
}
.ctrl:active,.ctrl.active{transform:translateY(2px);box-shadow:0 2px 0 rgba(0,0,0,.14)}
.left{background:var(--blue)} .right{background:var(--red)}
.start{
  width:100%;margin-top:11px;min-height:52px;border:0;border-radius:16px;background:var(--green);
  color:#fff;font-weight:900;font-size:17px;cursor:pointer
}
.help,.best{text-align:center;color:var(--muted);font-size:12px;line-height:1.35}
.help{margin-top:9px}.best{margin-top:6px}
kbd{font:inherit;font-size:11px;border:1px solid var(--line);border-bottom-width:2px;border-radius:6px;padding:1px 5px;background:var(--card)}
```

## Duelo de Bananas

`jogos/duelo-de-bananas.html`

```html
    touch-action: none;
  }

  .controls {
    display: grid;
    grid-template-columns: 1fr;
    gap: 10px;
    margin-bottom: 14px;
  }
  .control-row {
    display: flex;
    align-items: center;
```

```html
    gap: 10px;
    margin-bottom: 14px;
  }
  .control-row {
    display: flex;
    align-items: center;
    gap: 10px;
  }
  .control-row label {
    font-size: 13px;
    color: var(--text-secondary);
    width: 66px;
```

```html
    align-items: center;
    gap: 10px;
  }
  .control-row label {
    font-size: 13px;
    color: var(--text-secondary);
    width: 66px;
    text-align: left;
    flex-shrink: 0;
  }
  .control-row input[type="range"] {
    flex: 1;
```

## Encaixa Cano

`jogos/encaixa-cano.html`

```html
<style>
:root{--bg:#f5fbff;--card:#fff;--text:#25323b;--muted:#71808b;--accent:#378ADD;--accent2:#639922;--tile:#eef5f8;--border:#cbd8df;--pipe:#697982;--water:#41a7e8;--soil:#d9b77d;--shadow:rgba(0,0,0,.09)}
[data-theme="dark"]{--bg:#162028;--card:#202b33;--text:#eef6fb;--muted:#a7b5bf;--accent:#67b7ee;--accent2:#8fbd55;--tile:#2a3740;--border:#43525c;--pipe:#b5c1c8;--soil:#70563b;--shadow:rgba(0,0,0,.35)}
*{box-sizing:border-box;-webkit-tap-highlight-color:transparent}body{margin:0;min-height:100vh;background:var(--bg);color:var(--text);font-family:system-ui,-apple-system,Segoe UI,sans-serif;display:grid;place-items:center;padding:18px}.card{width:min(96vw,620px);background:var(--card);border-radius:24px;padding:20px;box-shadow:0 10px 35px var(--shadow);text-align:center;position:relative}.theme{position:absolute;right:16px;top:16px;border:1px solid var(--border);background:var(--tile);color:var(--text);border-radius:50%;width:40px;height:40px;font-size:18px;cursor:pointer}h1{margin:0 48px 4px;font-size:24px}.sub{margin:0 0 14px;color:var(--muted);font-size:14px}.stats{display:flex;justify-content:center;gap:26px;flex-wrap:wrap;margin:10px 0}.stat small{display:block;color:var(--muted);font-size:11px}.stat b{font-size:19px}.status{min-height:24px;font-weight:700;margin:8px 0 12px}.board-wrap{display:grid;grid-template-columns:42px 1fr 42px;align-items:center;gap:8px}.source,.goal{font-size:30px;display:flex;align-items:center;justify-content:center}.board{display:grid;gap:5px;background:var(--soil);padding:8px;border-radius:18px;touch-action:manipulation}.tile{aspect-ratio:1;border:1px solid var(--border);border-radius:12px;background:var(--tile);position:relative;cursor:pointer;padding:0;overflow:hidden}.tile:active{transform:scale(.96)}.tile.fixed{cursor:default}.tile.wet{box-shadow:inset 0 0 0 3px rgba(65,167,232,.35)}.tile.hint{animation:hint .65s ease 2}@keyframes hint{50%{transform:scale(1.08);box-shadow:0 0 0 4px rgba(239,159,39,.35)}}.pipe{position:absolute;inset:0}.seg{position:absolute;background:var(--pipe);border-radius:8px}.seg.wet{background:var(--water)}.seg.u,.seg.d{width:22%;height:52%;left:39%}.seg.u{top:0}.seg.d{bottom:0}.seg.l,.seg.r{height:22%;width:52%;top:39%}.seg.l{left:0}.seg.r{right:0}.hub{position:absolute;width:30%;height:30%;left:35%;top:35%;border-radius:50%;background:var(--pipe)}.wet .hub{background:var(--water)}.controls{display:flex;gap:8px;justify-content:center;margin-top:14px;flex-wrap:wrap}.btn{border:0;border-radius:14px;padding:11px 14px;background:var(--accent);color:white;font-weight:800;cursor:pointer}.btn.secondary{background:var(--tile);color:var(--text);border:1px solid var(--border)}.legend{margin-top:12px;color:var(--muted);font-size:12px}.overlay{position:absolute;inset:0;background:rgba(0,0,0,.62);display:none;align-items:center;justify-content:center;border-radius:24px;padding:20px;z-index:5}.overlay.show{display:flex}.modal{background:var(--card);color:var(--text);border-radius:20px;padding:24px;width:min(90%,380px)}.modal .big{font-size:50px}.modal h2{margin:6px 0}.stars{font-size:30px;letter-spacing:4px}.next{width:100%;margin-top:14px}@media(max-width:460px){.card{padding:16px 12px}.board-wrap{grid-template-columns:34px 1fr 34px;gap:4px}.board{gap:3px;padding:5px}.tile{border-radius:8px}.source,.goal{font-size:24px}}
</style>
</head>
<body><main class="card">
<button class="theme" id="theme">🌙</button>
<h1>🔧 Encaixa Cano</h1><p class="sub">Gire os canos e leve a água da torneira a
```

```html
<div class="stats"><div class="stat"><small>FASE</small><b id="level">1 / 5</b></div><div class="stat"><small>GIROS</small><b id="moves">0</b></div><div class="stat"><small>PONTOS</small><b id="score">0</b></div><div class="stat"><small>RECORDE</small><b id="record">0</b></div></div>
<div class="status" id="status">Clique nos canos para girar ↻</div>
<div class="board-wrap"><div class="source" id="source">🚰</div><div class="board" id="board"></div><div class="goal" id="goal">🌱</div></div>
<div class="controls"><button class="btn secondary" id="reset">↺ Reiniciar fase</button><button class="btn secondary" id="hint">💡 Dica</button></div>
<div class="legend">Conecte as pontas dos canos. Quando a água chegar à 🌱, a fase termina.</div>
<div class="overlay" id="overlay"><div class="modal"><div class="big">💦🌿</div><h2 id="winTitle">Água chegou!</h2><div class="stars" id="stars">⭐⭐⭐</div><p id="winText"></p><button class="btn next" id="next">Próxima fase ▶</button></div></div>
</main>
<script>
(()=>{
const DIRS=['u','r','d','l'], DELTA={u:[0,-1],r:[1,0],d:[0,1],l:[-1,0]}, OPP={u:'d',d:'u',l:'r',r:'l'};
const levels=[
 {n:4,path:[[0,1],[1,1],[2,1],[2,2],[3,2]]},
```

## Entrega do Carteiro

`data/entrega_do_carteiro.gz.b64`

```html
  .tools{display:grid;grid-template-columns:1fr 1fr;gap:8px;margin:8px 0}
  button{font:inherit}
  .smallBtn{border:1px solid var(--line);background:var(--btn);color:var(--btnText);padding:10px 8px;border-radius:13px;font-weight:700;cursor:pointer}
  .controls{display:grid;grid-template-columns:repeat(3,64px);grid-template-rows:repeat(2,54px);justify-content:center;gap:7px;margin:10px 0 12px}
  .ctrl{border:0;border-radius:15px;background:var(--blue);color:white;font-size:24px;font-weight:900;box-shadow:0 3px 0 color-mix(in srgb,var(--blue) 65%,black);touch-action:none;cursor:pointer}
  .ctrl:active{transform:translateY(2px);box-shadow:0 1px 0 color-mix(in srgb,var(--blue) 65%,black)}
  .up{grid-column:2;grid-row:1}.left{grid-column:1;grid-row:2}.down{grid-column:2;grid-row:2}.right{grid-column:3;grid-row:2}
  .main{width:100%;border:0;border-radius:16px;background:var(--orange);color:#251d10;font-weight:900;font-size:17px;padding:14px 12px;cursor:pointer;box-shadow:0 3px 0 #b97817}
  .main:active{transform:translateY(2px);box-shadow:0 1px 0 #b97817}
  .foot{margin-top:8px;font-size:11px;text-align:center;color:var(--muted)}
  .pulse{animation:pulse .7s ease-in-out 2}
  @keyframes pulse{0%,100%{opacity:1}50%{opacity:.25}}
```

```html
  button{font:inherit}
  .smallBtn{border:1px solid var(--line);background:var(--btn);color:var(--btnText);padding:10px 8px;border-radius:13px;font-weight:700;cursor:pointer}
  .controls{display:grid;grid-template-columns:repeat(3,64px);grid-template-rows:repeat(2,54px);justify-content:center;gap:7px;margin:10px 0 12px}
  .ctrl{border:0;border-radius:15px;background:var(--blue);color:white;font-size:24px;font-weight:900;box-shadow:0 3px 0 color-mix(in srgb,var(--blue) 65%,black);touch-action:none;cursor:pointer}
  .ctrl:active{transform:translateY(2px);box-shadow:0 1px 0 color-mix(in srgb,var(--blue) 65%,black)}
  .up{grid-column:2;grid-row:1}.left{grid-column:1;grid-row:2}.down{grid-column:2;grid-row:2}.right{grid-column:3;grid-row:2}
  .main{width:100%;border:0;border-radius:16px;background:var(--orange);color:#251d10;font-weight:900;font-size:17px;padding:14px 12px;cursor:pointer;box-shadow:0 3px 0 #b97817}
  .main:active{transform:translateY(2px);box-shadow:0 1px 0 #b97817}
  .foot{margin-top:8px;font-size:11px;text-align:center;color:var(--muted)}
  .pulse{animation:pulse .7s ease-in-out 2}
  @keyframes pulse{0%,100%{opacity:1}50%{opacity:.25}}
</style>
```

```html
  .smallBtn{border:1px solid var(--line);background:var(--btn);color:var(--btnText);padding:10px 8px;border-radius:13px;font-weight:700;cursor:pointer}
  .controls{display:grid;grid-template-columns:repeat(3,64px);grid-template-rows:repeat(2,54px);justify-content:center;gap:7px;margin:10px 0 12px}
  .ctrl{border:0;border-radius:15px;background:var(--blue);color:white;font-size:24px;font-weight:900;box-shadow:0 3px 0 color-mix(in srgb,var(--blue) 65%,black);touch-action:none;cursor:pointer}
  .ctrl:active{transform:translateY(2px);box-shadow:0 1px 0 color-mix(in srgb,var(--blue) 65%,black)}
  .up{grid-column:2;grid-row:1}.left{grid-column:1;grid-row:2}.down{grid-column:2;grid-row:2}.right{grid-column:3;grid-row:2}
  .main{width:100%;border:0;border-radius:16px;background:var(--orange);color:#251d10;font-weight:900;font-size:17px;padding:14px 12px;cursor:pointer;box-shadow:0 3px 0 #b97817}
  .main:active{transform:translateY(2px);box-shadow:0 1px 0 #b97817}
  .foot{margin-top:8px;font-size:11px;text-align:center;color:var(--muted)}
  .pulse{animation:pulse .7s ease-in-out 2}
  @keyframes pulse{0%,100%{opacity:1}50%{opacity:.25}}
</style>
</head>
```

## Equilibra a Torre

`data/equilibra_a_torre.gz.b64`

```html
.game-wrap{border:1px solid var(--line);border-radius:18px;overflow:hidden;background:linear-gradient(var(--sky1),var(--sky2));position:relative;user-select:none;-webkit-user-select:none;touch-action:none}
svg{display:block;width:100%;height:auto;touch-action:none}
#dropHint{position:absolute;left:50%;bottom:9px;transform:translateX(-50%);background:color-mix(in srgb,var(--card) 88%,transparent);border:1px solid var(--line);border-radius:999px;padding:6px 10px;font-size:12px;font-weight:700;pointer-events:none;white-space:nowrap}
.controls-note{text-align:center;color:var(--muted);font-size:12px;margin:9px 0 0}
.primary{width:100%;border:0;border-radius:16px;background:var(--orange);color:#2A1A00;font-weight:900;font-size:18px;padding:14px 16px;margin-top:14px;cursor:pointer;box-shadow:0 5px 0 rgba(0,0,0,.12)}
.primary:active{transform:translateY(2px);box-shadow:0 3px 0 rgba(0,0,0,.12)}
.legend{display:flex;gap:8px;justify-content:center;flex-wrap:wrap;margin-top:10px;font-size:12px;color:var(--muted)}
.pill{background:var(--panel);border:1px solid var(--line);border-radius:999px;padding:5px 9px}
@media(max-width:380px){.card{padding:14px;border-radius:20px}h1{font-size:24px}.sub{font-size:13px}.status{font-size:14px}}
</style>
</head>
<body>
```

```html
    </svg>
    <div id="dropHint">Toque • Clique • Espaço</div>
  </div>
  <p class="controls-note">No computador, use Espaço ou Enter. No celular, toque na área do jogo.</p>
  <div class="legend">
    <span class="pill">✨ Centro perfeito = bônus</span>
    <span class="pill">⚠️ Pouco apoio = cai</span>
  </div>
  <button class="primary" id="startBtn">Iniciar jogo</button>
</div>

<script>
```

```html
startBtn.addEventListener('click',startGame);

gameWrap.addEventListener('click',e=>{if(e.target===startBtn)return;drop();});
window.addEventListener('keydown',e=>{
  if(e.code==='Space'||e.code==='Enter'){e.preventDefault();drop();}
});

gameWrap.addEventListener('touchstart',e=>{
  e.preventDefault();
  if(touchIdentifier!==null)return;
  const t=e.changedTouches[0];if(!t)return;touchIdentifier=t.identifier;drop();
},{passive:false});
```

## Floresta dos Bichinhos Escondidos

`data/floresta_bichinhos_escondidos.gz.b64`

```html
    <div class="card">
      <div style="font-size:74px">🐰🌳</div>
      <h1>Floresta dos Bichinhos Escondidos</h1>
      <p>Os bichinhos se esconderam atrás dos arbustos. Quando você <strong>escutar um bichinho</strong>, aperte o Ctrl do mesmo lado do som!</p>
      <div class="keys">
        <div class="key"><span class="ear">👂</span>Ctrl esquerdo</div>
        <div class="key"><span class="ear">👂</span>Ctrl direito</div>
      </div>
      <div class="safety">
        <strong>Para o adulto:</strong> use fone estéreo em ambiente silencioso. Ajuste o volume do computador para um nível confortável <strong>antes</strong> do jogo e não aumente durante as rodadas. Este jogo é uma triagem lúdica e não mede dB HL nem substitui avaliação audiológica.
      </div>
      <button class="btn" id="prepareBtn">Preparar a floresta</button>
```

```html
      <h1>Floresta dos Bichinhos Escondidos</h1>
      <p>Os bichinhos se esconderam atrás dos arbustos. Quando você <strong>escutar um bichinho</strong>, aperte o Ctrl do mesmo lado do som!</p>
      <div class="keys">
        <div class="key"><span class="ear">👂</span>Ctrl esquerdo</div>
        <div class="key"><span class="ear">👂</span>Ctrl direito</div>
      </div>
      <div class="safety">
        <strong>Para o adulto:</strong> use fone estéreo em ambiente silencioso. Ajuste o volume do computador para um nível confortável <strong>antes</strong> do jogo e não aumente durante as rodadas. Este jogo é uma triagem lúdica e não mede dB HL nem substitui avaliação audiológica.
      </div>
      <button class="btn" id="prepareBtn">Preparar a floresta</button>
    </div>
  </section>
```

```html
      <p>Os bichinhos se esconderam atrás dos arbustos. Quando você <strong>escutar um bichinho</strong>, aperte o Ctrl do mesmo lado do som!</p>
      <div class="keys">
        <div class="key"><span class="ear">👂</span>Ctrl esquerdo</div>
        <div class="key"><span class="ear">👂</span>Ctrl direito</div>
      </div>
      <div class="safety">
        <strong>Para o adulto:</strong> use fone estéreo em ambiente silencioso. Ajuste o volume do computador para um nível confortável <strong>antes</strong> do jogo e não aumente durante as rodadas. Este jogo é uma triagem lúdica e não mede dB HL nem substitui avaliação audiológica.
      </div>
      <button class="btn" id="prepareBtn">Preparar a floresta</button>
    </div>
  </section>

```

## Jogo da Forca

`jogos/jogo-da-forca.html`

```html
  });

  // Suporte a teclado físico durante o jogo
  document.addEventListener('keydown', (e) => {
    if (!gameActive) return;
    if (gameEl.classList.contains('hidden')) return;
    const letter = normalizeLetter(e.key || '');
    if (letter.length !== 1 || letter < 'A' || letter > 'Z') return;
    const key = keyboardEl.querySelector('[data-letter="' + letter + '"]');
    if (!key || key.disabled) return;
    key.classList.add('key-pressed');
    setTimeout(() => key.classList.remove('key-pressed'), 120);
```

## Limpa o Oceano

`jogos/limpa-o-oceano.html`

```html
@keyframes rise{to{transform:translateY(-45px);opacity:0}}
.legend{display:flex;flex-wrap:wrap;gap:7px;justify-content:center;margin:11px 0}
.pill{font-size:12px;border:2px solid var(--border);border-radius:999px;padding:5px 9px;background:var(--card)}
.controls{display:flex;gap:9px;margin-top:12px}.btn{flex:1;border:0;border-radius:14px;padding:13px;font-size:16px;font-weight:800;cursor:pointer;background:var(--blue);color:#fff}.btn.secondary{background:var(--green)}
.help{text-align:center;color:var(--muted);font-size:12px;margin:10px 0 0;line-height:1.4}
.overlay{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;background:rgba(9,45,67,.54);z-index:30;padding:18px}
.overlay.hidden{display:none}.panel{max-width:380px;background:var(--card);color:var(--text);border-radius:22px;padding:22px;text-align:center;box-shadow:0 12px 34px rgba(0,0,0,.2)}.panel h2{margin:0 0 8px;font-size:27px}.panel p{margin:7px 0;color:var(--muted);line-height:1.45}.stars{font-size:30px;margin:9px 0}
@media(max-width:560px){body{padding:8px}.game{padding:13px;border-radius:18px}.stats{grid-template-columns:repeat(2,1fr)}.ocean{min-height:390px}.controls{flex-direction:column}.legend{justify-content:flex-start}}
</style>
</head>
<body>
<div class="game">
```

```html
.help{text-align:center;color:var(--muted);font-size:12px;margin:10px 0 0;line-height:1.4}
.overlay{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;background:rgba(9,45,67,.54);z-index:30;padding:18px}
.overlay.hidden{display:none}.panel{max-width:380px;background:var(--card);color:var(--text);border-radius:22px;padding:22px;text-align:center;box-shadow:0 12px 34px rgba(0,0,0,.2)}.panel h2{margin:0 0 8px;font-size:27px}.panel p{margin:7px 0;color:var(--muted);line-height:1.45}.stars{font-size:30px;margin:9px 0}
@media(max-width:560px){body{padding:8px}.game{padding:13px;border-radius:18px}.stats{grid-template-columns:repeat(2,1fr)}.ocean{min-height:390px}.controls{flex-direction:column}.legend{justify-content:flex-start}}
</style>
</head>
<body>
<div class="game">
  <div class="top">
    <div><h1>🌊 Limpa o Oceano</h1><p class="sub">Recolha o lixo, proteja os peixes e deixe o mar limpinho!</p></div>
    <button class="theme" id="theme" aria-label="Alternar tema">🌙</button>
  </div>
```

```html
  <div class="legend">
    <span class="pill">🧴 Garrafa +10</span><span class="pill">🥫 Lata +15</span><span class="pill">🛍️ Sacola +20</span><span class="pill">🛞 Pneu +30</span><span class="pill">♻️ Bônus +40</span><span class="pill">🐟 Peixe: perde vida</span>
  </div>
  <div class="controls"><button class="btn" id="start">▶ Iniciar / Reiniciar</button><button class="btn secondary" id="pause">⏸️ Pausar</button></div>
  <p class="help">Dica: pegue vários resíduos seguidos sem acertar peixe para ganhar bônus de sequência.</p>
</div>
<script>
(()=>{
const ocean=document.getElementById('ocean'),net=document.getElementById('net'),scoreEl=document.getElementById('score'),phaseEl=document.getElementById('phase'),livesEl=document.getElementById('lives'),recordEl=document.getElementById('record'),statusEl=document.getElementById('status'),overlay=document.getElementById('overlay'),startBtn=document.getElementById('start'),pauseBtn=document.getElementById('pause'),overlayStart=document.getElementById('overlayStart'),themeBtn=document.getElementById('theme');
const TRASH=[
 {emoji:'🧴',name:'garrafa',points:10,size:34},
 {emoji:'🥫',name:'lata',points:15,size:32},
```

## Mastermind

`jogos/mastermind.html`

```html

  <div class="history" id="history"></div>

  <div id="game-controls" class="hidden">
    <div class="current-row" id="current-row"></div>
    <div class="color-picker" id="color-picker"></div>
    <button class="submit-btn" id="submit-guess" disabled>Confirmar tentativa</button>
  </div>

  <button class="start-btn" id="start">Iniciar jogo</button>
</div>

```

```html
  const statusEl = document.getElementById('status');
  const startBtn = document.getElementById('start');
  const historyEl = document.getElementById('history');
  const gameControls = document.getElementById('game-controls');
  const currentRowEl = document.getElementById('current-row');
  const colorPickerEl = document.getElementById('color-picker');
  const submitBtn = document.getElementById('submit-guess');

  let secretCode = [];
  let currentGuess = [];
  let attempts = [];
  let gameActive = false;
```

```html

  function endGame(won){
    gameActive = false;
    gameControls.classList.add('hidden');
    if (won){
      statusEl.textContent = 'Parabéns! Você descobriu em ' + attempts.length + ' tentativa' + (attempts.length === 1 ? '' : 's') + '! 🎉';
    } else {
      const secretRow = document.createElement('div');
      secretRow.className = 'history-row';
      const slots = document.createElement('div');
      slots.className = 'row-slots';
      secretCode.forEach(colorId => {
```

## Mini Pinball

`data/mini_pinball.gz.b64`

```html
}
.board-wrap{position:relative;border-radius:20px;overflow:hidden;border:1px solid var(--line);background:var(--board)}
svg{display:block;width:100%;height:auto;touch-action:none;user-select:none}
.controls{display:grid;grid-template-columns:1fr .82fr 1fr;gap:9px;margin-top:12px}
.ctrl{
  min-height:58px;border:0;border-radius:16px;font-weight:800;font-size:15px;color:white;
  box-shadow:0 4px 0 rgba(0,0,0,.13);cursor:pointer;touch-action:none
}
.ctrl:active,.ctrl.active{transform:translateY(2px);box-shadow:0 2px 0 rgba(0,0,0,.13)}
.left{background:var(--blue)} .launch{background:var(--orange)} .right{background:var(--red)}
.start{
  width:100%;margin-top:11px;min-height:52px;border:0;border-radius:16px;background:var(--green);color:#fff;
```

```html
.board-wrap{position:relative;border-radius:20px;overflow:hidden;border:1px solid var(--line);background:var(--board)}
svg{display:block;width:100%;height:auto;touch-action:none;user-select:none}
.controls{display:grid;grid-template-columns:1fr .82fr 1fr;gap:9px;margin-top:12px}
.ctrl{
  min-height:58px;border:0;border-radius:16px;font-weight:800;font-size:15px;color:white;
  box-shadow:0 4px 0 rgba(0,0,0,.13);cursor:pointer;touch-action:none
}
.ctrl:active,.ctrl.active{transform:translateY(2px);box-shadow:0 2px 0 rgba(0,0,0,.13)}
.left{background:var(--blue)} .launch{background:var(--orange)} .right{background:var(--red)}
.start{
  width:100%;margin-top:11px;min-height:52px;border:0;border-radius:16px;background:var(--green);color:#fff;
  font-weight:900;font-size:17px;cursor:pointer
```

```html
  min-height:58px;border:0;border-radius:16px;font-weight:800;font-size:15px;color:white;
  box-shadow:0 4px 0 rgba(0,0,0,.13);cursor:pointer;touch-action:none
}
.ctrl:active,.ctrl.active{transform:translateY(2px);box-shadow:0 2px 0 rgba(0,0,0,.13)}
.left{background:var(--blue)} .launch{background:var(--orange)} .right{background:var(--red)}
.start{
  width:100%;margin-top:11px;min-height:52px;border:0;border-radius:16px;background:var(--green);color:#fff;
  font-weight:900;font-size:17px;cursor:pointer
}
.help{text-align:center;color:var(--muted);font-size:12px;margin:9px 2px 0;line-height:1.35}
.best{font-size:12px;color:var(--muted);text-align:center;margin-top:7px}
kbd{font:inherit;font-size:11px;border:1px solid var(--line);border-bottom-width:2px;border-radius:6px;padding:1px 5px;background:var(--card)}
```

## Pega-Gotas

`data/pega_gotas.gz.b64`

```html

  [data-theme="dark"] .settings summary { color: #B8B2FF; }

  .control-options {
    display: grid;
    grid-template-columns: 1fr;
    gap: 8px;
    margin-top: 10px;
  }

  .check-row {
    display: flex;
```

```html
  </div>

  <details class="settings">
    <summary>Controles</summary>
    <div class="control-options">
      <label class="check-row"><span>⌨️ Teclado (← → ou A/D)</span><input id="keyboardToggle" type="checkbox" checked /></label>
      <label class="check-row"><span>🔘 Botões na tela</span><input id="buttonsToggle" type="checkbox" checked /></label>
      <label class="check-row"><span>👆 Arrastar no jogo</span><input id="dragToggle" type="checkbox" checked /></label>
    </div>
  </details>

  <div class="pad" id="pad">
```

```html

  <details class="settings">
    <summary>Controles</summary>
    <div class="control-options">
      <label class="check-row"><span>⌨️ Teclado (← → ou A/D)</span><input id="keyboardToggle" type="checkbox" checked /></label>
      <label class="check-row"><span>🔘 Botões na tela</span><input id="buttonsToggle" type="checkbox" checked /></label>
      <label class="check-row"><span>👆 Arrastar no jogo</span><input id="dragToggle" type="checkbox" checked /></label>
    </div>
  </details>

  <div class="pad" id="pad">
    <button class="move-btn" id="leftBtn" type="button" aria-label="Mover para esquerda">←</button>
```

## Pescaria

`data/pescaria.gz.b64`

```html
}
.game-wrap{border:1px solid var(--border); border-radius:16px; overflow:hidden; background:var(--water); touch-action:none; user-select:none}
svg{display:block; width:100%; height:auto; aspect-ratio:4/5; background:linear-gradient(var(--water),var(--water2))}
.controls{display:grid; grid-template-columns:1fr 1fr 1fr 1fr; gap:8px; margin-top:10px}
.ctrl{
  min-height:52px; border:1px solid var(--border); border-radius:14px; background:var(--card);
  color:var(--text); font-size:21px; font-weight:800; cursor:pointer; touch-action:none;
  box-shadow:0 3px 0 rgba(0,0,0,.06);
}
.ctrl:active,.ctrl.active{transform:translateY(1px); box-shadow:none; background:color-mix(in srgb,var(--card) 80%,var(--blue) 20%)}
.legend{display:flex; flex-wrap:wrap; gap:8px; justify-content:center; font-size:12px; color:var(--muted); margin:10px 0 2px}
.pill{border:1px solid var(--border); border-radius:999px; padding:5px 8px}
```

```html
.game-wrap{border:1px solid var(--border); border-radius:16px; overflow:hidden; background:var(--water); touch-action:none; user-select:none}
svg{display:block; width:100%; height:auto; aspect-ratio:4/5; background:linear-gradient(var(--water),var(--water2))}
.controls{display:grid; grid-template-columns:1fr 1fr 1fr 1fr; gap:8px; margin-top:10px}
.ctrl{
  min-height:52px; border:1px solid var(--border); border-radius:14px; background:var(--card);
  color:var(--text); font-size:21px; font-weight:800; cursor:pointer; touch-action:none;
  box-shadow:0 3px 0 rgba(0,0,0,.06);
}
.ctrl:active,.ctrl.active{transform:translateY(1px); box-shadow:none; background:color-mix(in srgb,var(--card) 80%,var(--blue) 20%)}
.legend{display:flex; flex-wrap:wrap; gap:8px; justify-content:center; font-size:12px; color:var(--muted); margin:10px 0 2px}
.pill{border:1px solid var(--border); border-radius:999px; padding:5px 8px}
.start{
```

```html
  color:var(--text); font-size:21px; font-weight:800; cursor:pointer; touch-action:none;
  box-shadow:0 3px 0 rgba(0,0,0,.06);
}
.ctrl:active,.ctrl.active{transform:translateY(1px); box-shadow:none; background:color-mix(in srgb,var(--card) 80%,var(--blue) 20%)}
.legend{display:flex; flex-wrap:wrap; gap:8px; justify-content:center; font-size:12px; color:var(--muted); margin:10px 0 2px}
.pill{border:1px solid var(--border); border-radius:999px; padding:5px 8px}
.start{
  width:100%; margin-top:12px; border:0; border-radius:15px; padding:14px 16px;
  background:var(--orange); color:#2d2108; font-weight:900; font-size:17px; cursor:pointer;
}
.start:active{transform:translateY(1px)}
.small{margin-top:9px; color:var(--muted); font-size:12px; text-align:center; line-height:1.35}
```

## Quebra-Cabeça Deslizante

`jogos/quebra-cabeca-deslizante.html`

```html
.tile:active{transform:scale(.96)}
.tile .num{position:absolute;right:4px;bottom:4px;background:rgba(0,0,0,.48);color:#fff;border-radius:8px;padding:2px 6px;font-size:11px;font-weight:800}
.empty{background:transparent;box-shadow:none;cursor:default}
.controls{display:flex;gap:8px;justify-content:center;flex-wrap:wrap;margin-top:10px}
button.ctrl{border:0;border-radius:13px;padding:11px 15px;font-weight:800;cursor:pointer;background:var(--primary);color:white}
button.ctrl.secondary{background:var(--slot);color:var(--text);border:1px solid var(--border)}
.win{color:var(--good)}
.hint{font-size:12px;color:var(--muted);margin-top:10px;line-height:1.35}
@media(max-width:430px){.card{padding:16px}.stats{grid-template-columns:repeat(2,1fr)}h1{font-size:21px}.board{gap:4px;padding:4px}}
</style>
</head>
<body>
```

```html
.tile .num{position:absolute;right:4px;bottom:4px;background:rgba(0,0,0,.48);color:#fff;border-radius:8px;padding:2px 6px;font-size:11px;font-weight:800}
.empty{background:transparent;box-shadow:none;cursor:default}
.controls{display:flex;gap:8px;justify-content:center;flex-wrap:wrap;margin-top:10px}
button.ctrl{border:0;border-radius:13px;padding:11px 15px;font-weight:800;cursor:pointer;background:var(--primary);color:white}
button.ctrl.secondary{background:var(--slot);color:var(--text);border:1px solid var(--border)}
.win{color:var(--good)}
.hint{font-size:12px;color:var(--muted);margin-top:10px;line-height:1.35}
@media(max-width:430px){.card{padding:16px}.stats{grid-template-columns:repeat(2,1fr)}h1{font-size:21px}.board{gap:4px;padding:4px}}
</style>
</head>
<body>
<div class="card">
```

```html
.empty{background:transparent;box-shadow:none;cursor:default}
.controls{display:flex;gap:8px;justify-content:center;flex-wrap:wrap;margin-top:10px}
button.ctrl{border:0;border-radius:13px;padding:11px 15px;font-weight:800;cursor:pointer;background:var(--primary);color:white}
button.ctrl.secondary{background:var(--slot);color:var(--text);border:1px solid var(--border)}
.win{color:var(--good)}
.hint{font-size:12px;color:var(--muted);margin-top:10px;line-height:1.35}
@media(max-width:430px){.card{padding:16px}.stats{grid-template-columns:repeat(2,1fr)}h1{font-size:21px}.board{gap:4px;padding:4px}}
</style>
</head>
<body>
<div class="card">
<button class="theme" id="theme" aria-label="Alternar tema">🌙</button>
```

## Quebra-Blocos

`data/quebra_blocos.gz.b64`

```html
  gameWrap.addEventListener('touchend', finishTouch, { passive: false });
  gameWrap.addEventListener('touchcancel', finishTouch, { passive: false });

  window.addEventListener('keydown', (e) => {
    const key = e.key.toLowerCase();
    if (['arrowleft', 'arrowright', 'a', 'd'].includes(key)) e.preventDefault();
    if (key === 'arrowleft' || key === 'a') leftPressed = true;
    if (key === 'arrowright' || key === 'd') rightPressed = true;
  });

  window.addEventListener('keyup', (e) => {
    const key = e.key.toLowerCase();
```

```html

  window.addEventListener('keydown', (e) => {
    const key = e.key.toLowerCase();
    if (['arrowleft', 'arrowright', 'a', 'd'].includes(key)) e.preventDefault();
    if (key === 'arrowleft' || key === 'a') leftPressed = true;
    if (key === 'arrowright' || key === 'd') rightPressed = true;
  });

  window.addEventListener('keyup', (e) => {
    const key = e.key.toLowerCase();
    if (key === 'arrowleft' || key === 'a') leftPressed = false;
    if (key === 'arrowright' || key === 'd') rightPressed = false;
```

```html
  window.addEventListener('keydown', (e) => {
    const key = e.key.toLowerCase();
    if (['arrowleft', 'arrowright', 'a', 'd'].includes(key)) e.preventDefault();
    if (key === 'arrowleft' || key === 'a') leftPressed = true;
    if (key === 'arrowright' || key === 'd') rightPressed = true;
  });

  window.addEventListener('keyup', (e) => {
    const key = e.key.toLowerCase();
    if (key === 'arrowleft' || key === 'a') leftPressed = false;
    if (key === 'arrowright' || key === 'd') rightPressed = false;
  });
```

## Robô Programável

`data/robo_programavel.gz.b64`

```html
      expandedIndex++;
    }
  }
  updateControls();
}

function updateControls(){
  const level=state.level;
  const used=expandedSteps();
  stepsPill.textContent = level ? `Passos: ${used}/${level.maxSteps}` : "Passos: 0/0";
  repeatBtn.disabled = !level || !level.allowRepeat || state.executing || !state.queue.some(q=>q.type==="dir") || used>=level.maxSteps;
  repeatPill.textContent = level && level.allowRepeat ? "×2: liberado" : "×2: bloqueado";
```

```html
  updateControls();
}

function updateControls(){
  const level=state.level;
  const used=expandedSteps();
  stepsPill.textContent = level ? `Passos: ${used}/${level.maxSteps}` : "Passos: 0/0";
  repeatBtn.disabled = !level || !level.allowRepeat || state.executing || !state.queue.some(q=>q.type==="dir") || used>=level.maxSteps;
  repeatPill.textContent = level && level.allowRepeat ? "×2: liberado" : "×2: bloqueado";
  dirButtons.forEach(b=>b.disabled = !state.running || state.executing || !level || used>=level.maxSteps);
  undoBtn.disabled = !state.running || state.executing || !state.queue.length;
  clearBtn.disabled = !state.running || state.executing || !state.queue.length;
```

```html
function sleep(ms){return new Promise(r=>setTimeout(r,ms))}
async function executeProgram(){
  if(!state.running||state.executing||!state.queue.length)return;
  state.executing=true;updateControls();
  state.robot={...state.level.start};moveRobotVisual(state.robot);
  setStatus("🤖 Executando seu programa...");
  const moves=flattenQueue();
  const blocked=new Set(state.level.obstacles.map(o=>keyOf(o.r,o.c)));
  let failed=false;
  for(let i=0;i<moves.length;i++){
    const dir=moves[i],d=NS_DIRS[dir];
    renderQueue(Math.min(i,state.queue.length-1));
```

## Salva-Bichinhos

`data/salva_bichinhos.gz.b64`

```html
.status{min-height:42px;display:flex;align-items:center;justify-content:center;text-align:center;border-radius:13px;padding:8px 10px;margin-bottom:10px;background:color-mix(in srgb,var(--card) 88%,var(--orange) 12%);font-weight:800;font-size:14px}
.board-wrap{border-radius:20px;overflow:hidden;border:1px solid var(--line);background:var(--sky)}
svg{display:block;width:100%;height:auto;touch-action:none;user-select:none}
.controls{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-top:12px}
.ctrl{min-height:60px;border:0;border-radius:17px;color:#fff;font-size:17px;font-weight:900;cursor:pointer;touch-action:none;box-shadow:0 4px 0 rgba(0,0,0,.14)}
.ctrl:active,.ctrl.active{transform:translateY(2px);box-shadow:0 2px 0 rgba(0,0,0,.14)}
.left{background:var(--blue)} .right{background:var(--red)}
.start{width:100%;margin-top:11px;min-height:52px;border:0;border-radius:16px;background:var(--green);color:#fff;font-weight:900;font-size:17px;cursor:pointer}
.legend{display:flex;gap:8px;justify-content:center;flex-wrap:wrap;margin-top:10px}
.legend span{font-size:11px;font-weight:800;border:1px solid var(--line);border-radius:999px;padding:5px 9px;background:var(--card)}
.help,.best{text-align:center;color:var(--muted);font-size:12px;line-height:1.38}.help{margin-top:9px}.best{margin-top:6px}
kbd{font:inherit;font-size:11px;border:1px solid var(--line);border-bottom-width:2px;border-radius:6px;padding:1px 5px;background:var(--card)}
```

```html
.board-wrap{border-radius:20px;overflow:hidden;border:1px solid var(--line);background:var(--sky)}
svg{display:block;width:100%;height:auto;touch-action:none;user-select:none}
.controls{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-top:12px}
.ctrl{min-height:60px;border:0;border-radius:17px;color:#fff;font-size:17px;font-weight:900;cursor:pointer;touch-action:none;box-shadow:0 4px 0 rgba(0,0,0,.14)}
.ctrl:active,.ctrl.active{transform:translateY(2px);box-shadow:0 2px 0 rgba(0,0,0,.14)}
.left{background:var(--blue)} .right{background:var(--red)}
.start{width:100%;margin-top:11px;min-height:52px;border:0;border-radius:16px;background:var(--green);color:#fff;font-weight:900;font-size:17px;cursor:pointer}
.legend{display:flex;gap:8px;justify-content:center;flex-wrap:wrap;margin-top:10px}
.legend span{font-size:11px;font-weight:800;border:1px solid var(--line);border-radius:999px;padding:5px 9px;background:var(--card)}
.help,.best{text-align:center;color:var(--muted);font-size:12px;line-height:1.38}.help{margin-top:9px}.best{margin-top:6px}
kbd{font:inherit;font-size:11px;border:1px solid var(--line);border-bottom-width:2px;border-radius:6px;padding:1px 5px;background:var(--card)}
@media(max-width:390px){.card{padding:14px;border-radius:20px}h1{font-size:25px}.ctrl{min-height:56px;font-size:15px}}
```

```html
svg{display:block;width:100%;height:auto;touch-action:none;user-select:none}
.controls{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-top:12px}
.ctrl{min-height:60px;border:0;border-radius:17px;color:#fff;font-size:17px;font-weight:900;cursor:pointer;touch-action:none;box-shadow:0 4px 0 rgba(0,0,0,.14)}
.ctrl:active,.ctrl.active{transform:translateY(2px);box-shadow:0 2px 0 rgba(0,0,0,.14)}
.left{background:var(--blue)} .right{background:var(--red)}
.start{width:100%;margin-top:11px;min-height:52px;border:0;border-radius:16px;background:var(--green);color:#fff;font-weight:900;font-size:17px;cursor:pointer}
.legend{display:flex;gap:8px;justify-content:center;flex-wrap:wrap;margin-top:10px}
.legend span{font-size:11px;font-weight:800;border:1px solid var(--line);border-radius:999px;padding:5px 9px;background:var(--card)}
.help,.best{text-align:center;color:var(--muted);font-size:12px;line-height:1.38}.help{margin-top:9px}.best{margin-top:6px}
kbd{font:inherit;font-size:11px;border:1px solid var(--line);border-bottom-width:2px;border-radius:6px;padding:1px 5px;background:var(--card)}
@media(max-width:390px){.card{padding:14px;border-radius:20px}h1{font-size:25px}.ctrl{min-height:56px;font-size:15px}}
</style>
```

## Sapo Saltador

`data/sapo_saltador.gz.b64`

```html
function restartPhase(){if(!state.running&&state.lives<=0){startGame();return}const score=state.score;startPhase(state.phase,true);state.score=score;updateStats();setStatus("Fase reiniciada! Vamos tentar outra vez.")}
function loop(now,token){if(!state.running||token!==state.runToken)return;const dt=Math.min(.05,(now-state.lastTime)/1000||.016);state.lastTime=now;jumpStep(dt,now);updateMovingPads(now);updateRipples(now);drawFrog();updateAim();requestAnimationFrame(next=>loop(next,token))}
svg.addEventListener("pointerdown",beginAim,{passive:false});svg.addEventListener("pointermove",moveAim,{passive:false});svg.addEventListener("pointerup",endAim,{passive:false});svg.addEventListener("pointercancel",e=>{if(e.pointerId===state.pointerId){state.aiming=false;state.pointerId=null}},{passive:false});
window.addEventListener("keydown",e=>{if(!state.running||state.jumping)return;if(["ArrowLeft","ArrowRight","ArrowUp","ArrowDown","Space"].includes(e.code))e.preventDefault();if(e.code==="ArrowLeft")state.aimAngle-=.09;if(e.code==="ArrowRight")state.aimAngle+=.09;if(e.code==="ArrowUp")state.power=Math.min(145,state.power+5);if(e.code==="ArrowDown")state.power=Math.max(35,state.power-5);if(e.code==="Space")launchJump();updateAim();updateStats()},{passive:false});
startBtn.addEventListener("click",startGame);resetBtn.addEventListener("click",restartPhase);updateStats();drawFrog();
</script>
</body>
</html>
```

## Snake Infantil

`data/snake_infantil.gz.b64`

```html

  [data-theme="dark"] .settings summary { color: #B8B2FF; }

  .control-options {
    display: grid;
    grid-template-columns: 1fr;
    gap: 8px;
    margin-top: 10px;
  }

  .check-row {
    display: flex;
```

```html
    </div>

    <details class="settings">
      <summary>Controles</summary>
      <div class="control-options">
        <label class="check-row"><span>⌨️ Teclado (setas/WASD)</span><input id="keyboardToggle" type="checkbox" checked></label>
        <label class="check-row"><span>👆 Deslizar no tabuleiro</span><input id="swipeToggle" type="checkbox" checked></label>
        <label class="check-row"><span>🎮 Botões na tela</span><input id="buttonsToggle" type="checkbox" checked></label>
      </div>
    </details>

    <div id="pad" class="pad" aria-label="Botões de direção">
```

```html

    <details class="settings">
      <summary>Controles</summary>
      <div class="control-options">
        <label class="check-row"><span>⌨️ Teclado (setas/WASD)</span><input id="keyboardToggle" type="checkbox" checked></label>
        <label class="check-row"><span>👆 Deslizar no tabuleiro</span><input id="swipeToggle" type="checkbox" checked></label>
        <label class="check-row"><span>🎮 Botões na tela</span><input id="buttonsToggle" type="checkbox" checked></label>
      </div>
    </details>

    <div id="pad" class="pad" aria-label="Botões de direção">
      <button class="dir-btn dir-up" data-dir="up" type="button" aria-label="Cima">↑</button>
```

## Submarino Aventureiro

`data/submarino_aventureiro.gz.b64`

```html
}
.board-wrap{border-radius:20px;overflow:hidden;border:1px solid var(--line);background:var(--sea2)}
svg{display:block;width:100%;height:auto;touch-action:none;user-select:none}
.controls{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-top:12px}
.ctrl{
  min-height:62px;border:0;border-radius:17px;color:#fff;font-size:18px;font-weight:900;
  cursor:pointer;touch-action:none;box-shadow:0 4px 0 rgba(0,0,0,.14)
}
.ctrl:active,.ctrl.active{transform:translateY(2px);box-shadow:0 2px 0 rgba(0,0,0,.14)}
.up{background:var(--blue)} .down{background:var(--red)}
.start{
  width:100%;margin-top:11px;min-height:52px;border:0;border-radius:16px;background:var(--green);
```

```html
.board-wrap{border-radius:20px;overflow:hidden;border:1px solid var(--line);background:var(--sea2)}
svg{display:block;width:100%;height:auto;touch-action:none;user-select:none}
.controls{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-top:12px}
.ctrl{
  min-height:62px;border:0;border-radius:17px;color:#fff;font-size:18px;font-weight:900;
  cursor:pointer;touch-action:none;box-shadow:0 4px 0 rgba(0,0,0,.14)
}
.ctrl:active,.ctrl.active{transform:translateY(2px);box-shadow:0 2px 0 rgba(0,0,0,.14)}
.up{background:var(--blue)} .down{background:var(--red)}
.start{
  width:100%;margin-top:11px;min-height:52px;border:0;border-radius:16px;background:var(--green);
  color:#fff;font-weight:900;font-size:17px;cursor:pointer
```

```html
  min-height:62px;border:0;border-radius:17px;color:#fff;font-size:18px;font-weight:900;
  cursor:pointer;touch-action:none;box-shadow:0 4px 0 rgba(0,0,0,.14)
}
.ctrl:active,.ctrl.active{transform:translateY(2px);box-shadow:0 2px 0 rgba(0,0,0,.14)}
.up{background:var(--blue)} .down{background:var(--red)}
.start{
  width:100%;margin-top:11px;min-height:52px;border:0;border-radius:16px;background:var(--green);
  color:#fff;font-weight:900;font-size:17px;cursor:pointer
}
.help,.best{text-align:center;color:var(--muted);font-size:12px;line-height:1.35}
.help{margin-top:9px}.best{margin-top:6px}
kbd{font:inherit;font-size:11px;border:1px solid var(--line);border-bottom-width:2px;border-radius:6px;padding:1px 5px;background:var(--card)}
```

## Tangram Infantil

`data/tangram_infantil.gz.b64`

```html
.exit-note{fill:var(--muted);font-size:11px;font-weight:700;text-anchor:middle}
.flash{animation:flash .8s ease-in-out 2}
@keyframes flash{50%{opacity:.2}}
.controls{display:grid;grid-template-columns:1fr 1fr;gap:9px;margin-top:11px}
button.action{border:0;border-radius:16px;padding:12px 9px;font-weight:850;font-size:14px;cursor:pointer;background:var(--soft);color:var(--text);border:1px solid var(--line)}
button.action.primary{background:var(--orange);border-color:transparent;color:#231A08}
.start{width:100%;border:0;border-radius:18px;background:var(--purple);color:white;font-size:17px;font-weight:900;padding:14px 16px;margin-top:10px;cursor:pointer}
.help{font-size:12px;color:var(--muted);line-height:1.4;margin:10px 2px 0;text-align:center}
.overlay{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;background:rgba(20,18,28,.60);backdrop-filter:blur(2px);z-index:8;padding:24px}
.overlay.hidden{display:none}
.overlay-box{width:min(100%,340px);background:var(--card);border-radius:22px;border:1px solid var(--line);padding:20px;text-align:center;box-shadow:var(--shadow)}
.overlay-box h2{margin:0 0 7px;color:var(--purple)}
```

```html
    </div>
  </div>

  <div class="controls">
    <button class="action" id="hintBtn">💡 Dica</button>
    <button class="action" id="resetBtn">↺ Recomeçar</button>
  </div>
  <button class="start" id="startBtn">Iniciar jogo</button>
  <p class="help">Mover: arraste a peça. Girar: selecione e arraste a bolinha roxa. No computador, a rodinha do mouse também gira a peça selecionada.</p>
</main>

<script>
```

