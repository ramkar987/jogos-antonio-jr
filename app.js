const ZONES = [
  {id:'aventura', icon:'🏎️', name:'Pista de Aventura', desc:'Ação, coordenação e exploração.', cats:['Ação','Coordenação','Aventura']},
  {id:'desafios', icon:'🏰', name:'Castelo dos Desafios', desc:'Lógica, estratégia e quebra-cabeças.', cats:['Raciocínio','Estratégia','Quebra-cabeça']},
  {id:'memoria', icon:'🌳', name:'Floresta da Memória', desc:'Memória, atenção e percepção.', cats:['Memória','Atenção','Percepção','Audição','Cores']},
  {id:'laboratorio', icon:'🔬', name:'Laboratório de Ideias', desc:'Programação, construção e criatividade.', cats:['Programação','Construção','Criatividade']},
  {id:'escola', icon:'📚', name:'Escola Mágica', desc:'Palavras, números, música e sequências.', cats:['Palavras','Números','Educação','Sequência','Música']},
  {id:'parque', icon:'🎡', name:'Parque de Diversões', desc:'Simulações e brincadeiras diferentes.', cats:['Simulação','Experimento']}
];

let games = [];
let category = 'Todos';
let zone = 'Todos';
const grid = document.getElementById('grid');
const search = document.getElementById('search');
const resultCount = document.getElementById('resultCount');
const empty = document.getElementById('empty');
const chips = document.getElementById('chips');
const world = document.getElementById('world');
const missionEl = document.getElementById('mission');
const gameCount = document.getElementById('gameCount');
const starCount = document.getElementById('starCount');
const favoriteCount = document.getElementById('favoriteCount');
const now=new Date(); const today=`${now.getFullYear()}-${String(now.getMonth()+1).padStart(2,'0')}-${String(now.getDate()).padStart(2,'0')}`;
const PROGRESS_KEY = 'antonio-jr-progress-v2';

function safeParse(v, fallback) { try { return JSON.parse(v) ?? fallback; } catch { return fallback; } }
let progress = safeParse(localStorage.getItem(PROGRESS_KEY), {played:[], favorites:[], days:{}});
progress.played = Array.isArray(progress.played) ? progress.played : [];
progress.favorites = Array.isArray(progress.favorites) ? progress.favorites : [];
progress.days = progress.days && typeof progress.days === 'object' ? progress.days : {};
function saveProgress(){ localStorage.setItem(PROGRESS_KEY, JSON.stringify(progress)); updateProgress(); }
function escapeHtml(value=''){return String(value).replace(/[&<>"']/g,ch=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[ch]));}
function inferZone(g){
  for(const z of ZONES){ if((g.categories||[]).some(c=>z.cats.includes(c))) return z.id; }
  return 'parque';
}
function zoneInfo(id){return ZONES.find(z=>z.id===id)||ZONES[5];}
function updateProgress(){
  starCount.textContent = progress.played.length;
  favoriteCount.textContent = progress.favorites.length;
  document.getElementById('progressText').textContent = games.length ? `${progress.played.length} de ${games.length} jogos explorados` : 'Carregando…';
}
function markPlayed(id){
  if(!progress.played.includes(id)) progress.played.push(id);
  progress.days[today] ||= [];
  if(!progress.days[today].includes(id)) progress.days[today].push(id);
  saveProgress();
}
function toggleFavorite(id){
  const i=progress.favorites.indexOf(id);
  if(i>=0) progress.favorites.splice(i,1); else progress.favorites.push(id);
  saveProgress(); render(); renderMission();
}
function openGame(id){
  const g=games.find(x=>x.id===id); if(!g) return;
  markPlayed(id); render(); renderMission();
  const touchDevice = (navigator.maxTouchPoints || 0) > 0 || (window.matchMedia && window.matchMedia('(pointer: coarse)').matches);
  if(touchDevice) location.assign(g.file);
  else window.open(g.file,'_blank','noopener');
}

function updateWorld(){
  world.innerHTML = ZONES.map(z=>{
    const arr=games.filter(g=>inferZone(g)===z.id);
    const explored=arr.filter(g=>progress.played.includes(g.id)).length;
    return `<button class="zone-card ${zone===z.id?'active':''}" data-zone="${z.id}"><span class="zone-icon">${z.icon}</span><strong>${escapeHtml(z.name)}</strong><small>${escapeHtml(z.desc)}</small><span class="zone-progress">${explored}/${arr.length} explorados</span></button>`;
  }).join('');
}
function updateCategories(){
  const cats=['Todos','Favoritos',...new Set(games.flatMap(g=>g.categories||[]))];
  chips.innerHTML=cats.map(c=>`<button class="chip ${c===category?'active':''}" data-cat="${escapeHtml(c)}">${escapeHtml(c)}</button>`).join('');
}
function render(){
  const q=search.value.trim().toLowerCase();
  const arr=games.filter(g=>{
    const catOk=category==='Todos'||(category==='Favoritos'?progress.favorites.includes(g.id):(g.categories||[]).includes(category));
    const zoneOk=zone==='Todos'||inferZone(g)===zone;
    const qOk=!q||`${g.title} ${g.description} ${(g.categories||[]).join(' ')}`.toLowerCase().includes(q);
    return catOk&&zoneOk&&qOk;
  });
  grid.innerHTML=arr.map(g=>{
    const played=progress.played.includes(g.id), fav=progress.favorites.includes(g.id), zi=zoneInfo(inferZone(g));
    return `<article class="card ${played?'played':''}">
      <button class="fav ${fav?'on':''}" data-fav="${escapeHtml(g.id)}" aria-label="Favoritar">${fav?'♥':'♡'}</button>
      <div class="game-icon">${escapeHtml(g.icon||'🎮')}</div>
      <div class="card-zone">${zi.icon} ${escapeHtml(zi.name)}</div>
      <h3>${escapeHtml(g.title)}</h3>
      <p>${escapeHtml(g.description||'Jogo da coleção do Antônio Jr.')}</p>
      <div class="tags">${(g.categories||[]).map(c=>`<span class="tag">${escapeHtml(c)}</span>`).join('')}</div>
      <div class="card-foot"><span>${played?'⭐ Explorado':'☆ Novo para você'}</span><button class="play" data-play="${escapeHtml(g.id)}">JOGAR ▶</button></div>
    </article>`;
  }).join('');
  resultCount.textContent=`${arr.length} jogo${arr.length===1?'':'s'}`;
  empty.style.display=arr.length?'none':'block';
  gameCount.textContent=games.length;
  updateProgress(); updateWorld();
}

function hashDay(s){let h=2166136261;for(const ch of s){h^=ch.charCodeAt(0);h=Math.imul(h,16777619)}return h>>>0;}
function dailyMission(){
  if(!games.length) return [];
  let seed=hashDay(today), pool=[...games], out=[], usedZones=new Set();
  while(out.length<3&&pool.length){
    seed=(Math.imul(seed,1664525)+1013904223)>>>0;
    let idx=seed%pool.length, g=pool.splice(idx,1)[0], z=inferZone(g);
    if(!usedZones.has(z)||pool.length<3-out.length){out.push(g);usedZones.add(z)}
  }
  return out;
}
function renderMission(){
  const mission=dailyMission(), doneToday=progress.days[today]||[], done=mission.filter(g=>doneToday.includes(g.id)).length;
  missionEl.innerHTML=`<div class="mission-head"><div><p class="eyebrow">MISSÃO DO DIA</p><h2>${done===3?'🏆 Missão completa!':'Ganhe 3 estrelas explorando jogos'}</h2></div><strong>${done}/3</strong></div><div class="mission-games">${mission.map(g=>`<button class="mission-game ${doneToday.includes(g.id)?'done':''}" data-play="${escapeHtml(g.id)}"><span>${g.icon}</span><b>${escapeHtml(g.title)}</b><small>${doneToday.includes(g.id)?'✓ feito':'jogar'}</small></button>`).join('')}</div>`;
}

document.addEventListener('click',e=>{
  const p=e.target.closest('[data-play]'); if(p){openGame(p.dataset.play);return;}
  const f=e.target.closest('[data-fav]'); if(f){toggleFavorite(f.dataset.fav);return;}
  const c=e.target.closest('[data-cat]'); if(c){category=c.dataset.cat;updateCategories();render();return;}
  const z=e.target.closest('[data-zone]'); if(z){zone=zone===z.dataset.zone?'Todos':z.dataset.zone;render();document.getElementById('jogos').scrollIntoView({behavior:'smooth'});return;}
});
search.addEventListener('input',render);
document.getElementById('clear').onclick=()=>{search.value='';category='Todos';zone='Todos';updateCategories();render();};
document.getElementById('allZones').onclick=()=>{zone='Todos';render();};
document.getElementById('random').onclick=()=>{if(games.length)openGame(games[Math.floor(Math.random()*games.length)].id);};

const themeBtn=document.getElementById('theme');
function setTheme(t){document.documentElement.dataset.theme=t;themeBtn.textContent=t==='dark'?'☀️':'🌙';localStorage.setItem('antonio-jr-theme',t)}
setTheme(localStorage.getItem('antonio-jr-theme')||(matchMedia('(prefers-color-scheme:dark)').matches?'dark':'light'));
themeBtn.onclick=()=>setTheme(document.documentElement.dataset.theme==='dark'?'light':'dark');

(async()=>{
  try{
    const r=await fetch(`games.json?v=${Date.now()}`,{cache:'no-store'});
    if(!r.ok) throw new Error('Catálogo indisponível');
    const list=await r.json();
    games=Array.isArray(list)?list.map((g,i)=>({...g,id:g.id||`jogo-${i}`,categories:Array.isArray(g.categories)?g.categories:[]})):[];
  }catch(err){console.error(err);document.getElementById('loadError').style.display='block';}
  updateCategories();render();renderMission();
})();

if('serviceWorker' in navigator){window.addEventListener('load',()=>navigator.serviceWorker.register('sw.js').catch(()=>{}));}
