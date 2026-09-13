# ⌨️ Controles que merecem validação no celular

Trechos gerados automaticamente para ajudar a revisão dos jogos que usam teclado.

## Apaga-Incêndio

`data/apaga_incendio.gz.b64`

```html
function gameOver(){state.running=false;setSpray(false);setMove("left",false);setMove("right",false);startMessage.style.display="block";startMessage.querySelector("text").textContent="MISSÃO ENCERRADA!";setStatus(`Você fez ${Math.floor(state.score)} pontos e chegou à fase ${state.phase}!`);startBtn.textContent="Jogar novamente"}
function loop(now){if(!state.running)return;const dt=Math.min(2,(now-state.lastTime)/16.6667||1);state.lastTime=now;updateGame(now,dt);drawPlayer(now);updateStats(now);requestAnimationFrame(loop)}
function bindHold(btn,onStart,onStop){const start=e=>{e.preventDefault();onStart()},stop=e=>{if(e)e.preventDefault();onStop()};btn.addEventListener("mousedown",start);btn.addEventListener("mouseup",stop);btn.addEventListener("mouseleave",stop);btn.addEventListener("touchstart",start,{passive:false});btn.addEventListener("touchend",stop,{passive:false});btn.addEventListener("touchcancel",stop,{passive:false})}
bindHold(leftBtn,()=>setMove("left",true),()=>setMove("left",false));bindHold(rightBtn,()=>setMove("right",true),()=>setMove("right",false));bindHold(sprayBtn,()=>setSpray(true),()=>setSpray(false));
const downKeys=new Set();window.addEventListener("keydown",e=>{if(["ArrowLeft","ArrowRight","KeyA","KeyD","KeyQ","KeyE","Space"].includes(e.code))e.preventDefault();if(e.code==="Space"){setSpray(true);return}if(downKeys.has(e.code))return;downKeys.add(e.code);if(e.code==="ArrowLeft"||e.code==="KeyA")setMove("left",true);if(e.code==="ArrowRight"||e.code==="KeyD")setMove("right",true);if(e.code==="KeyQ")rotateAim(-.10);if(e.code==="KeyE")rotateAim(.10)},{passive:false});window.addEventListener("keyup",e=>{downKeys.delete(e.code);if(e.code==="ArrowLeft"||e.code==="KeyA")setMove("left",false);if(e.code==="ArrowRight"||e.code==="KeyD")setMove("right",false);if(e.code==="Space")setSpray(false)});window.addEventListener("blur",()=>{downKeys.clear();setMove("left",false);setMove("right",false);setSpray(false)});
svg.addEventListener("mousemove",e=>{if(!state.running)return;setAimFromClient(e.clientX,e.clientY);if(mouseDown)setSpray(true)});svg.addEventListener("mousedown",e=>{if(!state.running)return;e.preventDefault();mouseDown=true;setAimFromClient(e.clientX,e.clientY);setSpray(true)});window.addEventListener("mouseup",()=>{mouseDown=false;setSpray(false)});
svg.addEventListener("touchstart",e=>{if(!state.running||e.changedTouches.length===0)return;e.preventDefault();const t=e.changedTouches[0];touchId=t.identifier;setAimFromClient(t.clientX,t.clientY);setSpray(true)},{passive:false});svg.addEventListener("touchmove",e=>{if(touchId===null)return;e.preventDefault();const t=[...e.touches].find(v=>v.identifier===touchId);if(!t)return;setAimFromClient(t.clientX,t.clientY);setSpray(true)},{passive:false});svg.addEventListener("touchend",e=>{if(touchId===null)return;e.preventDefault();const ended=[...e.changedTouches].some(v=>v.identifier===touchId);if(ended){touchId=null;setSpray(false)}},{passive:false});svg.addEventListener("touchcancel",e=>{e.preventDefault();touchId=null;setSpray(false)},{passive:false});startBtn.addEventListener("click",startGame);buildWindows();clampAim();drawPlayer(performance.now());updateStats();
</script>
</body></html>
```

```html
*{box-sizing:border-box}html,body{margin:0;min-height:100%;font-family:system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;background:var(--bg);color:var(--text)}body{padding:18px 12px;display:flex;justify-content:center;align-items:flex-start}
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
<div class="meters"><div class="meter"><div class="meter-label"><span>ÁGUA</span><span id="waterText">100%</span></div><div class="bar"><div class="fill" id="waterFill"></div></div></div><div class="meter"><div class="meter-label"><span>PRESSÃO EXTRA</span><span id="pressureText">—</span></div><div class="bar"><div class="fill" id="pressureFill" style="width:0%"></div></div></div></div>
<div class="board-wrap"><svg id="game" viewBox="0 0 360 520" aria-label="Prédio com focos de incêndio e bombeiro"><defs><linearGradient id="sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#B9E2F6
```

```html
<line id="aimGuide" x1="180" y1="458" x2="180" y2="120" stroke="#378ADD" stroke-width="2" stroke-dasharray="5 6" opacity=".32"/><line id="waterJet" x1="180" y1="458" x2="180" y2="120" stroke="#BCEBFF" stroke-width="7" stroke-linecap="round" opacity="0" filter="url(#glow)"/><g id="droplets"></g>
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
function extinguishSound(){beep(620,.06,"triangle");setTimeout(()=>beep(820,.08,"triangle"),55)}function dangerSound(){beep(155,.16,"sawtooth",.035)}function bonusSound(){[520,700,940].forEach((f,i)=>setTimeout(()=>beep(f,.08,"sine"),i*55))}function phaseSound(){[523,659,784].forEach((f,i)=>setTimeout(()=>beep(f,.09,"triangle"),i*70))}
function applyTheme(theme){document.documentElement.dataset.theme=theme;themeBtn.textContent=theme==="dark"?"☀️":"🌙"}applyTheme(localStorage.getItem(THEME_KEY)||"light");themeBtn.addEventListener("click",()=>{const next=document.documentElement.
```

## Atravessa a Rua

`jogos/atravessa-a-rua.html`

```html
      rafId = requestAnimationFrame(physicsLoop);
    }
  }

  document.addEventListener('keydown', (e) => {
    if (!gameActive) return;
    switch(e.key){
      case 'ArrowUp': case 'w': case 'W':
        movePlayer(-1, 0); e.preventDefault(); break;
      case 'ArrowDown': case 's': case 'S':
        movePlayer(1, 0); e.preventDefault(); break;
      case 'ArrowLeft': case 'a': case 'A':
        movePlayer(0, -1); e.preventDefault(); break;
      case 'ArrowRight': case 'd': case 'D':
        movePlayer(0, 1); e.preventDefault(); break;
    }
```

```html
    height: 100%;
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
    border-radius: 12px;
    border: 2px solid var(--key-border);
    background: var(--key-bg);
```

```html
    gap: 6px;
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
    align-items: center;
    justify-content: center;
  }
```

```html
    display: flex;
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
    font-size: 17px;
    font-weight: 700;
    border-radius: 16px;
```

## A Aventura de Blinky

`jogos/aventura-do-blinky.html`

```html
    if (c.state === 'suspended') c.resume();
    runProgram();
  });

  document.addEventListener('keydown', (e) => {
    if (!gameActive || running) return;
    switch(e.key){
      case 'ArrowUp': addBlock('up'); e.preventDefault(); break;
      case 'ArrowDown': addBlock('down'); e.preventDefault(); break;
      case 'ArrowLeft': addBlock('left'); e.preventDefault(); break;
      case 'ArrowRight': addBlock('right'); e.preventDefault(); break;
      case 'Enter': if (program.length > 0) playBtn.click(); break;
      case 'Backspace': if (program.length > 0) removeBlock(program.length - 1); break;
    }
  });

```

```html
  <div class="board-wrap">
    <div class="board" id="board"></div>
  </div>

  <div id="game-controls" class="hidden">
    <div class="program-label">Seu programa (nessa ordem):</div>
    <div class="program-list" id="program-list"></div>

    <div class="block-picker" id="block-picker"></div>

    <div class="action-row">
      <button class="action-btn clear" id="clear-btn">Limpar</button>
      <button class="action-btn play" id="play-btn">▶ Executar</button>
    </div>
  </div>

```

```html
  const statusEl = document.getElementById('status');
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
    { id: 'down',  symbol: '↓', dr: 1, dc: 0 },
    { id: 'left',  symbol: '←', dr: 0, dc: -1 },
    { id: 'right', symbol: '→', dr: 0, dc: 1 }
```

```html
        playWin();
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
    }, 500);
  }

```

## Bichinhos Camuflados — O Mistério das Cores

`data/bichinhos_camuflados_misterio_das_cores.gz.b64`

```html
  ];
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
      fg:["#ba765f","#b66f59","#c47f69","#ad6854","#bd735e"],
      neutral:["#a18e68","#aa9b70"]
    },
```

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
      fg:["#ba765f","#b66f59","#c47f69","#ad6854","#bd735e"],
      neutral:["#a18e68","#aa9b70"]
    },
    rgB: {
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

    while(dots.length<520 && tries<6000){
      tries++;
      const r=minR+Math.random()*(maxR-minR);
```

```html
  }

  function buildRounds(){
    const arr=[];
    // 4 controles visuais
    for(let i=0;i<4;i++) arr.push({group:"control",shape:pick(SHAPES).id,kind:"control"});
    // 8 vermelho-verde A
    for(let i=0;i<8;i++) arr.push({group:"rgA",shape:pick(SHAPES).id,kind:"test"});
    // 8 vermelho-verde B
    for(let i=0;i<8;i++) arr.push({group:"rgB",shape:pick(SHAPES).id,kind:"test"});
    // 4 azul-amarelo
    for(let i=0;i<4;i++) arr.push({group:"by",shape:pick(SHAPES).id,kind:"test"});
    // 4 placas sem figura (duas RG, uma BY, uma controle)
    arr.push({group:"rgA",shape:"none",kind:"catch"});
    arr.push({group:"rgB",shape:"none",kind:"catch"});
    arr.push({group:"by",shape:"none",kind:"catch"});
```

## Canhão de Bolinhas

`data/canhao_de_bolinhas.gz.b64`

```html
  }, { passive: false });

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
      updateAimVisual();
    } else if (e.key === ' ' || e.key === 'Enter') {
      e.preventDefault();
```

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
      updateAimVisual();
    } else if (e.key === ' ' || e.key === 'Enter') {
      e.preventDefault();
      startShot();
    }
```

```html
    if (e.key === 'ArrowLeft' || e.key.toLowerCase() === 'a') {
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

  renderShooter();
  updateStats();
```

## Cara a Cara

`jogos/cara-a-cara.html`

```html
  <div class="status" id="status">Toque em iniciar</div>

  <div class="faces-grid" id="faces-grid"></div>

  <div id="game-controls">
    <div class="questions" id="questions"></div>

    <div class="answer-row" id="answer-row">
      <button class="answer-btn yes" id="answer-yes">Sim ✔️</button>
      <button class="answer-btn no" id="answer-no">Não ✖️</button>
    </div>

    <div class="guess-row hidden" id="guess-row">
      <select class="guess-select" id="guess-select">
        <option value="">Escolha quem você acha que é...</option>
      </select>
```

## Código Secreto de Setas

`data/codigo_secreto_de_setas.gz.b64`

```html
    ArrowLeft:'left', a:'left', A:'left',
    ArrowRight:'right', d:'right', D:'right'
  };

  window.addEventListener('keydown', e => {
    const dir = keyMap[e.key];
    if (!dir) return;
    e.preventDefault();
    handleDirection(dir);
  }, {passive:false});

  els.controls.forEach(btn => {
    btn.addEventListener('click', () => handleDirection(btn.dataset.dir));
    btn.addEventListener('touchstart', e => {
      e.preventDefault();
      handleDirection(btn.dataset.dir);
```

```html
.progress{display:flex;flex-wrap:wrap;justify-content:center;gap:7px;margin-top:18px;max-width:320px}
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
.start:disabled,.ctrl:disabled{opacity:.45;cursor:not-allowed}
.best{margin-top:10px;text-align:center;color:var(--muted);font-size:12px}
.legend{text-align:center;margin-top:8px;color:var(--muted);font-size:11px}
```

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
.start:disabled,.ctrl:disabled{opacity:.45;cursor:not-allowed}
.best{margin-top:10px;text-align:center;color:var(--muted);font-size:12px}
.legend{text-align:center;margin-top:8px;color:var(--muted);font-size:11px}
@media(max-width:380px){.card{padding:16px}.flash{width:104px;height:104px}.ctrl{height:58px}h1{font-size:25px}}
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
.best{margin-top:10px;text-align:center;color:var(--muted);font-size:12px}
.legend{text-align:center;margin-top:8px;color:var(--muted);font-size:11px}
@media(max-width:380px){.card{padding:16px}.flash{width:104px;height:104px}.ctrl{height:58px}h1{font-size:25px}}
@media(prefers-reduced-motion:reduce){*{transition:none!important;animation:none!important}}
```

## Corrida de Carrinhos

`data/corrida_de_carrinhos.gz.b64`

```html
}
bindHold(leftBtn,moveLeft);
bindHold(rightBtn,moveRight);

window.addEventListener("keydown",e=>{
  if(["ArrowLeft","ArrowRight","KeyA","KeyD"].includes(e.code))e.preventDefault();
  if(e.repeat)return;
  if(e.code==="ArrowLeft"||e.code==="KeyA")moveLeft();
  if(e.code==="ArrowRight"||e.code==="KeyD")moveRight();
},{passive:false});

svg.addEventListener("touchstart",e=>{
  if(!state.running||e.changedTouches.length===0)return;
  e.preventDefault();
  const t=e.changedTouches[0];
  touchId=t.identifier;touchStartX=t.clientX;touchStartY=t.clientY;
```

```html
  font-weight:800;font-size:14px
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
  color:#fff;font-weight:900;font-size:17px;cursor:pointer
}
.help,.best{text-align:center;color:var(--muted);font-size:12px;line-height:1.35}
```

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
  color:#fff;font-weight:900;font-size:17px;cursor:pointer
}
.help,.best{text-align:center;color:var(--muted);font-size:12px;line-height:1.35}
.help{margin-top:9px}.best{margin-top:6px}
```

```html
.ctrl{
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
@media(max-width:390px){
  .card{padding:14px;border-radius:20px}
  h1{font-size:25px}
```

## Duelo de Bananas

`jogos/duelo-de-bananas.html`

```html
    margin-bottom: 16px;
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
    gap: 10px;
  }
  .control-row label {
```

```html
    grid-template-columns: 1fr;
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
    text-align: left;
    flex-shrink: 0;
  }
```

```html
    display: flex;
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
  }
  .control-row .value {
    font-size: 14px;
```

```html
    width: 66px;
    text-align: left;
    flex-shrink: 0;
  }
  .control-row input[type="range"] {
    flex: 1;
  }
  .control-row .value {
    font-size: 14px;
    font-weight: 700;
    color: var(--text-primary);
    width: 46px;
    text-align: right;
    flex-shrink: 0;
  }

```

## Encaixa Cano

`jogos/encaixa-cano.html`

```html
<title>Encaixa Cano</title>
<style>
:root{--bg:#f5fbff;--card:#fff;--text:#25323b;--muted:#71808b;--accent:#378ADD;--accent2:#639922;--tile:#eef5f8;--border:#cbd8df;--pipe:#697982;--water:#41a7e8;--soil:#d9b77d;--shadow:rgba(0,0,0,.09)}
[data-theme="dark"]{--bg:#162028;--card:#202b33;--text:#eef6fb;--muted:#a7b5bf;--accent:#67b7ee;--accent2:#8fbd55;--tile:#2a3740;--border:#43525c;--pipe:#b5c1c8;--soil:#70563b;--shadow:rgba(0,0,0,.35)}
*{box-sizing:border-box;-webkit-tap-highlight-color:transparent}body{margin:0;min-height:100vh;background:var(--bg);color:var(--text);font-family:system-ui,-apple-system,Segoe UI,sans-serif;display:grid;place-items:center;padding:18px}.card{width:min(96vw,620px);background:var(--card);border-radius:24px;padding:20px;box-shadow:0 10px 35px var(--shadow);text-align:center;position:relative}.theme{position:absolute;right:16px;top:16px;border:1px solid var(--border);background:var(--tile);color:var(--text);border-radius:50%;width:40px;height:40px;font-size:18px;cursor:pointer}h1{margin:0 48px 4px;font-size:24px}.sub{margin:0 0 14px;color:var(--muted);font-size:14px}.stats{display:flex;justify-content:center;gap:26px;flex-wrap:wrap;margin:10px 0}.stat small{display:block;color:var(--muted);font-size:11px}.stat b{font-size:19px}.status{min-height:24px;font-weight:700;margin:8px 0 12px}.board-wrap{display:grid;grid-template-columns:42px 1fr 42px;align-items:center;gap:8px}.source,.goal{font-size:30px;display:flex;align-items:center;justify-content:center}.board{display:grid;gap:5px;background:var(--soil);padding:8px;border-radius:18px;touch-action:manipulation}.tile{aspect-ratio:1;border:1px solid var(--border);border-radius:12px;background:var(--tile);position:relative;cursor:pointer;padding:0;overflow:hidden}.tile:active{transform:scale(.96)}.tile.fixed{cursor:default}.tile.wet{box-shadow:inset 0 0 0 3px rgba(65,167,232,.35)}.tile.hint{animation:hint .65s ease 2}@keyframes hint{50%{transform:scale(1.08);box-shadow:0 0 0 4px rgba(239,159,39,.35)}}.pipe{position:absolute;inset:0}.seg{position:absolute;background:var(--pipe);border-radius:8px}.seg.wet{background:var(--water)}.seg.u,.seg.d{width:22%;height:52%;left:39%}.seg.u{top:0}.seg.d{bottom:0}.seg.l,.seg.r{height:22%;width:52%;top:39%}.seg.l{left:0}.seg.r{right:0}.hub{position:absolute;width:30%;height:30%;left:35%;top:35%;border-radius:50%;background:var(--pipe)}.wet .hub{background:var(--water)}.controls{display:flex;gap:8px;justify-content:center;margin-top:14px;flex-wrap:wrap}.btn{border:0;border-radius:14px;padding:11px 14px;background:var(--accent);color:white;font-weight:800;cursor:pointer}.btn.secondary{background:var(--tile);color:var(--text);border:1px solid var(--border)}.legend{margin-top:12px;color:var(--muted);font-size:12px}.overlay{position:absolute;inset:0;background:rgba(0,0,0,.62);display:none;align-items:center;justify-content:center;border-radius:24px;padding:20px;z-index:5}.overlay.show{display:flex}.modal{background:var(--card);color:var(--text);border-radius:20px;padding:24px;width:min(90%,380px)}.modal .big{font-size:50px}.modal h2{margin:6px 0}.stars{font-size:30px;letter-spacing:4px}.next{width:100%;margin-top:14px}@media(max-width:460px){.card{padding:16px 12px}.board-wrap{grid-template-columns:34px 1fr 34px;gap:4px}.board{gap:3px;padding:5px}.tile{border-radius:8px}.source,.goal{font-size:24px}}
</style>
</head>
<body><main class="card">
<button class="theme" id="theme">🌙</button>
<h1>🔧 Encaixa Cano</h1><p class="sub">Gire os canos e leve a água da torneira até a plantinha.</p>
<div class="stats"><div class="stat"><small>FASE</small><b id="level">1 / 5</b></div><div class="stat"><small>GIROS</small><b id="moves">0</b></div><div class="stat"><small>PONTOS</small><b id="score">0</b></div><div class="stat"><small>RECORDE</small><b id="record">0</b></div></div>
<div class="status" id="status">Clique nos canos para girar ↻</div>
<div class="board-wrap"><div class="source" id="source">🚰</div><div class="board" id="board"></div><div class="goal" id="goal">🌱</div></div>
<div class="controls"><button class="btn secondary" id="reset">↺ Reiniciar fase</button><button class="btn secondary" id="hint">💡 Dica</button></div>
<div cla
```

```html
<h1>🔧 Encaixa Cano</h1><p class="sub">Gire os canos e leve a água da torneira até a plantinha.</p>
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
 {n:5,path:[[0,2],[1,2],[1,1],[2,1],[3,1],[3,2],[3,3],[4,3]]},
 {n:5,path:[[0,3],[1,3],[1,2],[2,2],[2,1],[3,1],[3,2],[4,2]]},
 {n:6,path:[[0,1],[1,1],[1,2],[2,2],[3,2],[3,1],[4,1],[4,2],[4,3],[5,3]]},
```

## Entrega do Carteiro

`data/entrega_do_carteiro.gz.b64`

```html
    const dir=b.dataset.dir;
    b.addEventListener('pointerdown',e=>{ e.preventDefault(); move(dir); });
    b.addEventListener('touchstart',e=>{ e.preventDefault(); },{passive:false});
  });
  window.addEventListener('keydown',e=>{
    const map={ArrowUp:'up',w:'up',W:'up',ArrowDown:'down',s:'down',S:'down',ArrowLeft:'left',a:'left',A:'left',ArrowRight:'right',d:'right',D:'right'};
    if(map[e.key]){ e.preventDefault(); move(map[e.key]); }
  },{passive:false});

  // Swipe opcional no tabuleiro: um gesto curto move uma casa.
  let touchId=null, sx=0, sy=0;
  svg.addEventListener('touchstart',e=>{
    if(touchId!==null) return; const t=e.changedTouches[0]; touchId=t.identifier; sx=t.clientX; sy=t.clientY; e.preventDefault();
  },{passive:false});
  svg.addEventListener('touchend',e=>{
    let t=null; for(const x of e.changedTouches) if(x.identifier===touchId){t=x;break;} if(!t) return;
```

```html
  .legend span{background:var(--tile);border:1px solid var(--line);padding:4px 7px;border-radius:999px}
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
</style>
</head>
<body>
```

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
</style>
</head>
<body>
<div class="card">
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
</head>
<body>
<div class="card">
  <button class="theme" id="themeBtn" aria-label="Alternar tema">🌙</button>
```

## Equilibra a Torre

`data/equilibra_a_torre.gz.b64`

```html
}
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
gameWrap.addEventListener('touchmove',e=>{
  e.preventDefault();
  if(touchIdentifier===null)return;
```

```html
.status{min-height:50px;border:1px solid var(--line);background:var(--panel);border-radius:14px;padding:12px;text-align:center;font-weight:700;margin-bottom:10px;display:flex;align-items:center;justify-content:center}
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
<div class="card">
  <button class="theme-btn" id="themeBtn" aria-label="Alternar tema">🌙</button>
  <h1>Equilibra a Torre</h1>
```

```html
      <g id="fallingLayer"></g>
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
(() => {
'use strict';

```

## Floresta dos Bichinhos Escondidos

`data/floresta_bichinhos_escondidos.gz.b64`

```html
    $("finishModal").classList.remove("open");
    $("reportModal").classList.remove("open");
    show("setup");
  };
  document.addEventListener("keydown",keyHandler,{passive:false});
})();
</script>

<div id="mobileEarControls" aria-label="Controles de resposta por ouvido">
  <button id="mobileEarLeft" type="button">👂 ESQUERDA</button>
  <button id="mobileEarRight" type="button">DIREITA 👂</button>
</div>
<script id="mobileEarScript">
(()=>{
  function emitControl(side){
    const right=side==='right', init={key:'Control',code:right?'ControlRight':'ControlLeft',location:right?2:1,ctrlKey:true,bubbles:true,cancelable:true};
```

```html
<script id="mobileEarScript">
(()=>{
  function emitControl(side){
    const right=side==='right', init={key:'Control',code:right?'ControlRight':'ControlLeft',location:right?2:1,ctrlKey:true,bubbles:true,cancelable:true};
    try{document.dispatchEvent(new KeyboardEvent('keydown',init));}catch(_){return}
    setTimeout(()=>{try{document.dispatchEvent(new KeyboardEvent('keyup',init));}catch(_){}},70);
  }
  document.getElementById('mobileEarLeft')?.addEventListener('pointerdown',e=>{e.preventDefault();emitControl('left')});
  document.getElementById('mobileEarRight')?.addEventListener('pointerdown',e=>{e.preventDefault();emitControl('right')});
})();
</script>
</body>
</html>
```

```html
(()=>{
  function emitControl(side){
    const right=side==='right', init={key:'Control',code:right?'ControlRight':'ControlLeft',location:right?2:1,ctrlKey:true,bubbles:true,cancelable:true};
    try{document.dispatchEvent(new KeyboardEvent('keydown',init));}catch(_){return}
    setTimeout(()=>{try{document.dispatchEvent(new KeyboardEvent('keyup',init));}catch(_){}},70);
  }
  document.getElementById('mobileEarLeft')?.addEventListener('pointerdown',e=>{e.preventDefault();emitControl('left')});
  document.getElementById('mobileEarRight')?.addEventListener('pointerdown',e=>{e.preventDefault();emitControl('right')});
})();
</script>
</body>
</html>
```

```html
  }
</style>

<style id="mobileEarStyle">
#mobileEarControls{display:none;position:fixed;left:10px;right:10px;bottom:max(10px,env(safe-area-inset-bottom));z-index:9999;grid-template-columns:1fr 1fr;gap:10px;pointer-events:none}
#mobileEarControls button{pointer-events:auto;min-height:64px;border:0;border-radius:18px;font:800 15px system-ui,-apple-system,sans-serif;color:#fff;box-shadow:0 7px 24px rgba(0,0,0,.22);touch-action:manipulation}
#mobileEarLeft{background:#378ADD}#mobileEarRight{background:#E24B4A}
#mobileEarControls button:active{transform:scale(.97)}
@media (pointer:coarse),(max-width:820px){#mobileEarControls{display:grid}body{padding-bottom:92px!important}}
</style>
</head>
<body>
<div class="app">
  <div class="sun"></div>
  <div class="hill"></div><div class="ground"></div>
  <div class="tree t1"></div><div class="tree t2"></div><div class="tree t3"></div><div class="tree t4"></div>
```

## Jogo da Forca

`jogos/jogo-da-forca.html`

```html
    setupEl.classList.remove('hidden');
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
    handleGuess(letter);
  });
})();
```

## Limpa o Oceano

`jogos/limpa-o-oceano.html`

```html
function startGame(){cancelAnimationFrame(raf);clearObjects();score=0;lives=3;phase=1;collected=0;streak=0;spawnTimer=.2;running=true;paused=false;last=performance.now();netPos={x:.5,y:.72};setNet();overlay.classList.add('hidden');pauseBtn.textContent='⏸️ Pausar';statusEl.textContent='Recolha o lixo e deixe os peixes passarem!';updateHud();beep(520,.12,'triangle',.06);raf=requestAnimationFrame(step)}
function endGame(win){running=false;cancelAnimationFrame(raf);clearObjects();overlay.classList.remove('hidden');overlay.querySelector('.panel').innerHTML=`<h2>${win?'🏆 Oceano limpo!':'🌊 Fim da rodada'}</h2><p>Você fez <b>${score} pontos</b> e recolheu <b>${collected} resíduos</b>.</p><div class="stars">${win?'🌟🌟🌟':'🐠 ♻️ 🐟'}</div><button class="btn" id="again">Jogar novamente</button>`;document.getElementById('again').onclick=startGame;statusEl.textContent=win?'Parabéns! Você completou a missão.':'Tente novamente e proteja os animais.'}
function moveFromPointer(e){if(!running||paused)return;const r=rect();netPos.x=clamp((e.clientX-r.left)/r.width,.06,.94);netPos.y=clamp((e.clientY-r.top)/r.height,.18,.90);setNet()}
ocean.addEventListener('pointerdown',e=>{if(!running||paused)return;e.preventDefault();ocean.setPointerCapture?.(e.pointerId);moveFromPointer(e)});ocean.addEventListener('pointermove',e=>{if(e.buttons||e.pointerType==='touch')moveFromPointer(e)});
window.addEventListener('keydown',e=>{if(!running||paused)return;const step=.045;if(['ArrowLeft','ArrowRight','ArrowUp','ArrowDown'].includes(e.key))e.preventDefault();if(e.key==='ArrowLeft')netPos.x-=step;if(e.key==='ArrowRight')netPos.x+=step;if(e.key==='ArrowUp')netPos.y-=step;if(e.key==='ArrowDown')netPos.y+=step;netPos.x=clamp(netPos.x,.06,.94);netPos.y=clamp(netPos.y,.18,.90);setNet()});
startBtn.onclick=startGame;overlayStart.onclick=startGame;pauseBtn.onclick=()=>{if(!running)return;paused=!paused;pauseBtn.textContent=paused?'▶ Continuar':'⏸️ Pausar';statusEl.textContent=paused?'Jogo pausado.':'De volta à limpeza!';last=performance.now()};
function applyTheme(t){document.documentElement.dataset.theme=t;themeBtn.textContent=t==='dark'?'☀️':'🌙';localStorage.setItem('limpa-oceano-theme',t)}applyTheme(localStorage.getItem('limpa-oceano-theme')||'light');themeBtn.onclick=()=>applyTheme(document.documentElement.dataset.theme==='dark'?'light':'dark');
window.addEventListener('resize',setNet);setNet();updateHud();
})();
</script>
</body>
</html>
```

```html
.float{position:absolute;font-weight:900;font-size:20px;pointer-events:none;z-index:20;animation:rise .7s ease-out forwards;text-shadow:0 2px 2px rgba(0,0,0,.18)}
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
  <div class="top">
    <div><h1>🌊 Limpa o Oceano</h1><p class="sub">Recolha o lixo, proteja os peixes e deixe o mar limpinho!</p></div>
    <button class="theme" id="theme" aria-label="Alternar tema">🌙</button>
```

```html
.controls{display:flex;gap:9px;margin-top:12px}.btn{flex:1;border:0;border-radius:14px;padding:13px;font-size:16px;font-weight:800;cursor:pointer;background:var(--blue);color:#fff}.btn.secondary{background:var(--green)}
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

  <div class="stats">
    <div class="stat"><b id="score">0</b><span>PONTOS</span></div>
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
 {emoji:'🛍️',name:'sacola',points:20,size:36},
 {emoji:'🛞',name:'pneu',points:30,size:39}
];
```

## Mastermind

`jogos/mastermind.html`

```html
  <div class="status" id="status">Toque em iniciar</div>

  <div class="history" id="history"></div>

  <div id="game-controls" class="hidden">
    <div class="current-row" id="current-row"></div>
    <div class="color-picker" id="color-picker"></div>
    <button class="submit-btn" id="submit-guess" disabled>Confirmar tentativa</button>
  </div>

  <button class="start-btn" id="start">Iniciar jogo</button>
</div>

<script>
(function(){
  // Modo escuro
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

  function randInt(min, max){ return Math.floor(Math.random() * (max - min + 1)) + min; }

```

```html
  });

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
        const s = document.createElement('div');
        s.className = 'row-slot';
        const colorDef = COLORS.find(c => c.id === colorId);
```

```html

    historyEl.innerHTML = '';
    statusEl.textContent = 'Tentativa 1 de ' + MAX_ATTEMPTS;
    startBtn.classList.add('hidden');
    gameControls.classList.remove('hidden');

    renderColorPicker();
    renderCurrentRow();
  }

  startBtn.addEventListener('click', startGame);
})();
</script>

</body>
</html>
```

## Mini Pinball

`data/mini_pinball.gz.b64`

```html
pressBinding(rightBtn,()=>setFlipper("right",true),()=>setFlipper("right",false));
pressBinding(launchBtn,launch,()=>{});

const downKeys=new Set();
window.addEventListener("keydown",(e)=>{
  if(["ControlLeft","ControlRight","Space","ArrowDown"].includes(e.code)) e.preventDefault();
  if(downKeys.has(e.code)) return;
  downKeys.add(e.code);

  if(e.code==="ControlLeft") setFlipper("left",true);
  if(e.code==="ControlRight") setFlipper("right",true);
  if(e.code==="Space" || e.code==="ArrowDown") launch();
},{passive:false});

window.addEventListener("keyup",(e)=>{
  downKeys.delete(e.code);
```

```html
  if(e.code==="ControlRight") setFlipper("right",true);
  if(e.code==="Space" || e.code==="ArrowDown") launch();
},{passive:false});

window.addEventListener("keyup",(e)=>{
  downKeys.delete(e.code);
  if(e.code==="ControlLeft") setFlipper("left",false);
  if(e.code==="ControlRight") setFlipper("right",false);
});

window.addEventListener("blur",()=>{
  downKeys.clear();
  setFlipper("left",false);
  setFlipper("right",false);
});

```

```html
  color:var(--text);font-weight:700;font-size:14px
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
  font-weight:900;font-size:17px;cursor:pointer
}
.help{text-align:center;color:var(--muted);font-size:12px;margin:9px 2px 0;line-height:1.35}
```

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
  font-weight:900;font-size:17px;cursor:pointer
}
.help{text-align:center;color:var(--muted);font-size:12px;margin:9px 2px 0;line-height:1.35}
.best{font-size:12px;color:var(--muted);text-align:center;margin-top:7px}
```

## Pega-Gotas

`data/pega_gotas.gz.b64`

```html
  }

  startBtn.addEventListener('click', startGame);

  document.addEventListener('keydown', (e) => {
    if (!keyboardToggle.checked) return;
    const key = e.key.toLowerCase();
    if (key === 'arrowleft' || key === 'a') {
      e.preventDefault();
      moveLeft = true;
    }
    if (key === 'arrowright' || key === 'd') {
      e.preventDefault();
      moveRight = true;
    }
  });
```

```html
      moveRight = true;
    }
  });

  document.addEventListener('keyup', (e) => {
    const key = e.key.toLowerCase();
    if (key === 'arrowleft' || key === 'a') {
      e.preventDefault();
      moveLeft = false;
    }
    if (key === 'arrowright' || key === 'd') {
      e.preventDefault();
      moveRight = false;
    }
  });

```

```html
  }

  [data-theme="dark"] .settings summary { color: #B8B2FF; }

  .control-options {
    display: grid;
    grid-template-columns: 1fr;
    gap: 8px;
    margin-top: 10px;
  }

  .check-row {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 10px;
```

```html
    <span id="levelHint">Fase 1: só gotas azuis</span>
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
    <button class="move-btn" id="leftBtn" type="button" aria-label="Mover para esquerda">←</button>
    <button class="move-btn" id="rightBtn" type="button" aria-label="Mover para direita">→</button>
  </div>
```

## Pescaria

`data/pescaria.gz.b64`

```html
    buttons[name]?.classList.toggle('active',value);
  }

  const keyMap = {ArrowLeft:'left',a:'left',A:'left',ArrowRight:'right',d:'right',D:'right',ArrowDown:'down',s:'down',S:'down',ArrowUp:'up',w:'up',W:'up'};
  window.addEventListener('keydown',e=>{
    const k=keyMap[e.key];
    if(k){ e.preventDefault(); if(running) setHeld(k,true); }
  },{passive:false});
  window.addEventListener('keyup',e=>{
    const k=keyMap[e.key];
    if(k){ e.preventDefault(); setHeld(k,false); }
  },{passive:false});

  function bindHold(btn,name){
    let touchId=null;
    btn.addEventListener('mousedown',e=>{ e.preventDefault(); if(running) setHeld(name,true); });
```

```html
  window.addEventListener('keydown',e=>{
    const k=keyMap[e.key];
    if(k){ e.preventDefault(); if(running) setHeld(k,true); }
  },{passive:false});
  window.addEventListener('keyup',e=>{
    const k=keyMap[e.key];
    if(k){ e.preventDefault(); setHeld(k,false); }
  },{passive:false});

  function bindHold(btn,name){
    let touchId=null;
    btn.addEventListener('mousedown',e=>{ e.preventDefault(); if(running) setHeld(name,true); });
    window.addEventListener('mouseup',()=>setHeld(name,false));
    btn.addEventListener('mouseleave',e=>{ if(e.buttons===0) setHeld(name,false); });
    btn.addEventListener('touchstart',e=>{
      e.preventDefault(); if(!running || touchId!==null) return;
```

```html
  background:color-mix(in srgb,var(--card) 84%,var(--orange) 16%); font-weight:700; font-size:14px;
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
.start{
  width:100%; margin-top:12px; border:0; border-radius:15px; padding:14px 16px;
  background:var(--orange); color:#2d2108; font-weight:900; font-size:17px; cursor:pointer;
```

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
.start{
  width:100%; margin-top:12px; border:0; border-radius:15px; padding:14px 16px;
  background:var(--orange); color:#2d2108; font-weight:900; font-size:17px; cursor:pointer;
}
```

## Quebra-Cabeça Deslizante

`jogos/quebra-cabeca-deslizante.html`

```html
function win(){locked=true;clearInterval(timer);statusEl.className='status win';statusEl.textContent='🎉 Imagem completa! Muito bem!';beep(760,.09);setTimeout(()=>beep(990,.14),110);const old=Number(localStorage.getItem(recordKey())||0);if(!old||moves<old){localStorage.setItem(recordKey(),String(moves));loadRecord()}setTimeout(()=>{if(level<levels.length-1){level++;startLevel(true)}else{statusEl.textContent='🏆 Você completou todas as fases!';locked=true}},1300)}
function giveHint(){if(locked)return;const empty=tiles.indexOf(0),opts=neighbors(empty);let best=opts[0],bestScore=-999;for(const p of opts){const copy=[...tiles];[copy[empty],copy[p]]=[copy[p],copy[empty]];let score=0;copy.forEach((v,i)=>{if(v&&v===i+1)score++});if(score>bestScore){bestScore=score;best=p}}const val=tiles[best];statusEl.textContent=`💡 Tente mover a peça ${val}.`;beep(650,.05)}
function beep(freq,dur){try{const A=window.AudioContext||window.webkitAudioContext;if(!A)return;const c=beep.ctx||(beep.ctx=new A()),o=c.createOscillator(),g=c.createGain();o.frequency.value=freq;o.type='sine';g.gain.setValueAtTime(.08,c.currentTime);g.gain.exponentialRampToValueAtTime(.001,c.currentTime+dur);o.connect(g).connect(c.destination);o.start();o.stop(c.currentTime+dur)}catch(e){}}
document.getElementById('reshuffle').onclick=()=>startLevel(true);document.getElementById('restart').onclick=()=>startLevel(true);document.getElementById('hint').onclick=giveHint;
window.addEventListener('keydown',e=>{const empty=tiles.indexOf(0);let p=null;if(e.key==='ArrowUp'&&empty+n<tiles.length)p=empty+n;if(e.key==='ArrowDown'&&empty-n>=0)p=empty-n;if(e.key==='ArrowLeft'&&empty%n<n-1)p=empty+1;if(e.key==='ArrowRight'&&empty%n>0)p=empty-1;if(p!==null){e.preventDefault();moveTile(p)}});
const theme=document.getElementById('theme');function setTheme(t){document.documentElement.dataset.theme=t;theme.textContent=t==='dark'?'☀️':'🌙';localStorage.setItem('slide-theme',t)}setTheme(localStorage.getItem('slide-theme')||(matchMedia('(prefers-color-scheme:dark)').matches?'dark':'light'));theme.onclick=()=>setTheme(document.documentElement.dataset.theme==='dark'?'light':'dark');
startLevel(true);
})();
</script>
</body>
</html>
```

```html
.tile{border:0;border-radius:10px;cursor:pointer;background-repeat:no-repeat;box-shadow:0 2px 6px rgba(0,0,0,.18);position:relative;transition:transform .08s}
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
<div class="card">
<button class="theme" id="theme" aria-label="Alternar tema">🌙</button>
<h1>🧩 Quebra-Cabeça Deslizante</h1>
```

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
<div class="card">
<button class="theme" id="theme" aria-label="Alternar tema">🌙</button>
<h1>🧩 Quebra-Cabeça Deslizante</h1>
<p class="sub">Deslize as peças para reconstruir a imagem.</p>
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
<button class="theme" id="theme" aria-label="Alternar tema">🌙</button>
<h1>🧩 Quebra-Cabeça Deslizante</h1>
<p class="sub">Deslize as peças para reconstruir a imagem.</p>
<div class="stats">
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
    if (key === 'arrowleft' || key === 'a') leftPressed = false;
    if (key === 'arrowright' || key === 'd') rightPressed = false;
  });
```

```html
    if (key === 'arrowleft' || key === 'a') leftPressed = true;
    if (key === 'arrowright' || key === 'd') rightPressed = true;
  });

  window.addEventListener('keyup', (e) => {
    const key = e.key.toLowerCase();
    if (key === 'arrowleft' || key === 'a') leftPressed = false;
    if (key === 'arrowright' || key === 'd') rightPressed = false;
  });

  window.addEventListener('blur', () => {
    leftPressed = false;
    rightPressed = false;
    draggingMouse = false;
    activeTouchId = null;
  });
```

```html
  gameWrap.addEventListener('touchcancel', finishTouch, { passive: false });

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

  window.addEventListener('blur', () => {
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

  window.addEventListener('blur', () => {
    leftPressed = false;
```

## Robô Programável

`data/robo_programavel.gz.b64`

```html
repeatBtn.addEventListener("click",addRepeat);
undoBtn.addEventListener("click",undo);
clearBtn.addEventListener("click",clearQueue);
runBtn.addEventListener("click",()=>executeProgram());
window.addEventListener("keydown",e=>{
  if(["ArrowUp","ArrowDown","ArrowLeft","ArrowRight","Enter","Backspace","KeyR"].includes(e.code)) e.preventDefault();
  if(e.repeat)return;
  if(e.code==="ArrowUp")addDir("up");
  if(e.code==="ArrowDown")addDir("down");
  if(e.code==="ArrowLeft")addDir("left");
  if(e.code==="ArrowRight")addDir("right");
  if(e.code==="KeyR")addRepeat();
  if(e.code==="Backspace")undo();
  if(e.code==="Enter")executeProgram();
},{passive:false});

```

```html
      queueEl.appendChild(d);
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
  dirButtons.forEach(b=>b.disabled = !state.running || state.executing || !level || used>=level.maxSteps);
  undoBtn.disabled = !state.running || state.executing || !state.queue.length;
  clearBtn.disabled = !state.running || state.executing || !state.queue.length;
```

```html
  }
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
  runBtn.disabled = !state.running || state.executing || !state.queue.length;
}

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
    await sleep(350);
    const nr=state.robot.r+d.dr,nc=state.robot.c+d.dc;
    if(!inBounds(nr,nc)){
```

## Salva-Bichinhos

`data/salva_bichinhos.gz.b64`

```html
function loop(now){if(!state.running)return;const dt=Math.min(.034,(now-state.lastTime)/1000||.016);state.lastTime=now;updateGame(now,dt);requestAnimationFrame(loop);}

function bindHold(btn,dir){const start=e=>{e.preventDefault();setMove(dir,true)};const stop=e=>{if(e)e.preventDefault();setMove(dir,false)};btn.addEventListener("mousedown",start);btn.addEventListener("mouseup",stop);btn.addEventListener("mouseleave",stop);btn.addEventListener("touchstart",start,{passive:false});btn.addEventListener("touchend",stop,{passive:false});btn.addEventListener("touchcancel",stop,{passive:false});}
bindHold(leftBtn,"left");bindHold(rightBtn,"right");
const keys=new Set();window.addEventListener("keydown",e=>{if(["ArrowLeft","ArrowRight","KeyA","KeyD"].includes(e.code))e.preventDefault();if(keys.has(e.code))return;keys.add(e.code);if(e.code==="ArrowLeft"||e.code==="KeyA")setMove("left",true);if(e.code==="ArrowRight"||e.code==="KeyD")setMove("right",true);},{passive:false});window.addEventListener("keyup",e=>{keys.delete(e.code);if(e.code==="ArrowLeft"||e.code==="KeyA")setMove("left",false);if(e.code==="ArrowRight"||e.code==="KeyD")setMove("right",false);});window.addEventListener("blur",()=>{keys.clear();setMove("left",false);setMove("right",false);});

function pointerX(e){const r=svg.getBoundingClientRect();return(e.clientX-r.left)/r.width*380;}
svg.addEventListener("pointerdown",e=>{if(!state.running)return;e.preventDefault();dragPointer=e.pointerId;state.basketX=Math.max(52,Math.min(328,pointerX(e)));drawBasket();try{svg.setPointerCapture(e.pointerId)}catch(_){}});
svg.addEventListener("pointermove",e=>{if(!state.running||dragPointer!==e.pointerId)return;e.preventDefault();state.basketX=Math.max(52,Math.min(328,pointerX(e)));drawBasket();},{passive:false});
svg.addEventListener("pointerup",e=>{if(dragPointer!==e.pointerId)return;e.preventDefault();dragPointer=null;try{svg.releasePointerCapture(e.pointerId)}catch(_){}});
svg.addEventListener("pointercancel",e=>{if(dragPointer===e.pointerId)dragPointer=null;});

startBtn.addEventListener("click",startGame);drawBasket();updateStats();
</script>
</body>
</html>
```

```html
.stat small{display:block;color:var(--muted);font-size:11px}.stat strong{display:block;font-size:18px;margin-top:1px}
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
@media(max-width:390px){.card{padding:14px;border-radius:20px}h1{font-size:25px}.ctrl{min-height:56px;font-size:15px}}
</style>
</head>
```

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
@media(max-width:390px){.card{padding:14px;border-radius:20px}h1{font-size:25px}.ctrl{min-height:56px;font-size:15px}}
</style>
</head>
<body>
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
</style>
</head>
<body>
<div class="card">
```

## Sapo Saltador

`data/sapo_saltador.gz.b64`

```html
function startGame(){state.lives=3;state.phase=1;startBtn.textContent="Reiniciar jogo";startPhase(1,false)}
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
    if (k === 'arrowright' || k === 'd') return 'right';
    return null;
  }

  function handleKeydown(e) {
    if (!keyboardToggle.checked) return;
    const dir = keyToDirection(e.key);
    if (!dir) return;
    e.preventDefault();
    setDirection(dir);
  }

  function handleTouchStart(e) {
    if (!swipeToggle.checked || touchIdentifier !== null) return;
    e.preventDefault();
    const t = e.changedTouches[0];
```

```html
      board.appendChild(svgEl('circle', { cx: eye.x, cy: eye.y, r: 0.9, fill: '#1F1F1F' }));
    });
  }

  document.addEventListener('keydown', handleKeydown, { passive: false });
  themeToggle.addEventListener('click', toggleTheme);
  startBtn.addEventListener('click', startGame);

  keyboardToggle.addEventListener('change', saveControlSettings);
  swipeToggle.addEventListener('change', saveControlSettings);
  buttonsToggle.addEventListener('change', saveControlSettings);

  document.querySelectorAll('.dir-btn').forEach(btn => {
    const go = (e) => {
      if (!buttonsToggle.checked) return;
      e.preventDefault();
```

```html
  }

  [data-theme="dark"] .settings summary { color: #B8B2FF; }

  .control-options {
    display: grid;
    grid-template-columns: 1fr;
    gap: 8px;
    margin-top: 10px;
  }

  .check-row {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 10px;
```

```html
      <span class="best">Recorde: <span id="bestScore">0</span></span>
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
      <button class="dir-btn dir-up" data-dir="up" type="button" aria-label="Cima">↑</button>
      <button class="dir-btn dir-left" data-dir="left" type="button" aria-label="Esquerda">←</button>
      <button class="dir-btn dir-down" data-dir="down" type="button" aria-label="Baixo">↓</button>
```

## Submarino Aventureiro

`data/submarino_aventureiro.gz.b64`

```html
bindHold(upBtn,"up");
bindHold(downBtn,"down");

const downKeys=new Set();
window.addEventListener("keydown",e=>{
  if(["ArrowUp","ArrowDown","KeyW","KeyS"].includes(e.code))e.preventDefault();
  if(downKeys.has(e.code))return;
  downKeys.add(e.code);
  if(e.code==="ArrowUp"||e.code==="KeyW")setMove("up",true);
  if(e.code==="ArrowDown"||e.code==="KeyS")setMove("down",true);
},{passive:false});
window.addEventListener("keyup",e=>{
  downKeys.delete(e.code);
  if(e.code==="ArrowUp"||e.code==="KeyW")setMove("up",false);
  if(e.code==="ArrowDown"||e.code==="KeyS")setMove("down",false);
});
```

```html
  downKeys.add(e.code);
  if(e.code==="ArrowUp"||e.code==="KeyW")setMove("up",true);
  if(e.code==="ArrowDown"||e.code==="KeyS")setMove("down",true);
},{passive:false});
window.addEventListener("keyup",e=>{
  downKeys.delete(e.code);
  if(e.code==="ArrowUp"||e.code==="KeyW")setMove("up",false);
  if(e.code==="ArrowDown"||e.code==="KeyS")setMove("down",false);
});
window.addEventListener("blur",()=>{
  downKeys.clear();setMove("up",false);setMove("down",false);
});

svg.addEventListener("touchstart",e=>{
  if(!state.running||e.changedTouches.length===0)return;
  e.preventDefault();
```

```html
  font-weight:800;font-size:14px
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
  color:#fff;font-weight:900;font-size:17px;cursor:pointer
}
.help,.best{text-align:center;color:var(--muted);font-size:12px;line-height:1.35}
```

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
  color:#fff;font-weight:900;font-size:17px;cursor:pointer
}
.help,.best{text-align:center;color:var(--muted);font-size:12px;line-height:1.35}
.help{margin-top:9px}.best{margin-top:6px}
```

## Tangram Infantil

`data/tangram_infantil.gz.b64`

```html
.tray-label{fill:var(--muted);font-size:12px;font-weight:700;text-anchor:middle}
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
.overlay-box p{margin:0 0 14px;color:var(--muted);line-height:1.4}
.overlay-box button{border:0;border-radius:15px;background:var(--orange);padding:12px 18px;font-weight:900;font-size:15px;cursor:pointer}
@media (max-width:390px){.card{padding:14px}.subtitle{margin-right:42px}.stats{gap:6px}.stat b{font-size:18px}}
```

```html
      </div>
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
(() => {
'use strict';

```

