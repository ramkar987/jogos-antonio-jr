const ALBUM_KEY = 'antonio-jr-progress-v2';
const ALBUM_ZONES = [
  {id:'aventura', cats:['Ação','Coordenação','Aventura']},
  {id:'desafios', cats:['Raciocínio','Estratégia','Quebra-cabeça']},
  {id:'memoria', cats:['Memória','Atenção','Percepção','Audição','Cores']},
  {id:'laboratorio', cats:['Programação','Construção','Criatividade']},
  {id:'escola', cats:['Palavras','Números','Educação','Sequência','Música']},
  {id:'parque', cats:['Simulação','Experimento']}
];

let albumGames = [];

function albumProgress(){
  try {
    const p = JSON.parse(localStorage.getItem(ALBUM_KEY) || '{}');
    return {
      played: Array.isArray(p.played) ? p.played : [],
      days: p.days && typeof p.days === 'object' ? p.days : {}
    };
  } catch {
    return {played:[], days:{}};
  }
}

function albumZone(g){
  for(const z of ALBUM_ZONES){
    if((g.categories || []).some(c => z.cats.includes(c))) return z.id;
  }
  return 'parque';
}

function albumHashDay(s){
  let h = 2166136261;
  for(const ch of s){ h ^= ch.charCodeAt(0); h = Math.imul(h, 16777619); }
  return h >>> 0;
}

function albumMissionForDate(dateStr){
  if(!albumGames.length) return [];
  let seed = albumHashDay(dateStr), pool = [...albumGames], out = [], usedZones = new Set();
  while(out.length < 3 && pool.length){
    seed = (Math.imul(seed, 1664525) + 1013904223) >>> 0;
    const idx = seed % pool.length;
    const g = pool.splice(idx, 1)[0];
    const z = albumZone(g);
    if(!usedZones.has(z) || pool.length < 3 - out.length){ out.push(g); usedZones.add(z); }
  }
  return out;
}

function completedMissions(progress){
  let total = 0;
  for(const [date, ids] of Object.entries(progress.days)){
    if(!Array.isArray(ids)) continue;
    const mission = albumMissionForDate(date);
    if(mission.length === 3 && mission.every(g => ids.includes(g.id))) total++;
  }
  return total;
}

function countPlayedBy(progress, predicate){
  const played = new Set(progress.played);
  return albumGames.filter(g => played.has(g.id) && predicate(g)).length;
}

function zoneCoverage(progress){
  const played = new Set(progress.played);
  const visited = new Set(albumGames.filter(g => played.has(g.id)).map(albumZone));
  return visited.size;
}

function achievementDefs(progress){
  const explored = progress.played.length;
  const missions = completedMissions(progress);
  const action = countPlayedBy(progress, g => (g.categories||[]).some(c => ['Ação','Coordenação'].includes(c)));
  const mind = countPlayedBy(progress, g => (g.categories||[]).some(c => ['Memória','Atenção','Percepção'].includes(c)));
  const code = countPlayedBy(progress, g => (g.categories||[]).includes('Programação'));
  const numbers = countPlayedBy(progress, g => (g.categories||[]).includes('Números'));
  const challenges = countPlayedBy(progress, g => albumZone(g) === 'desafios');
  const zones = zoneCoverage(progress);
  const total = albumGames.length;
  return [
    {icon:'⭐', name:'Primeira Estrela', desc:'Explore seu primeiro jogo.', value:explored, goal:1},
    {icon:'🧭', name:'Pequeno Explorador', desc:'Explore 5 jogos diferentes.', value:explored, goal:5},
    {icon:'🎒', name:'Aventureiro', desc:'Explore 15 jogos diferentes.', value:explored, goal:15},
    {icon:'🏆', name:'Colecionador', desc:'Explore 30 jogos diferentes.', value:explored, goal:30},
    {icon:'👑', name:'Lenda do Mundo', desc:'Explore todos os jogos da coleção.', value:explored, goal:Math.max(1,total)},
    {icon:'🌎', name:'Volta ao Mundo', desc:'Visite todas as 6 regiões.', value:zones, goal:6},
    {icon:'🏰', name:'Mestre dos Desafios', desc:'Explore 8 jogos do Castelo dos Desafios.', value:challenges, goal:8},
    {icon:'⚡', name:'Mãos Rápidas', desc:'Explore 8 jogos de ação ou coordenação.', value:action, goal:8},
    {icon:'🧠', name:'Memória de Elefante', desc:'Explore 6 jogos de memória, atenção ou percepção.', value:mind, goal:6},
    {icon:'🤖', name:'Pequeno Programador', desc:'Explore 2 jogos de programação.', value:code, goal:2},
    {icon:'🔢', name:'Amigo dos Números', desc:'Explore 3 jogos com números.', value:numbers, goal:3},
    {icon:'📅', name:'Missão Cumprida', desc:'Complete uma Missão do Dia inteira.', value:missions, goal:1},
    {icon:'🔥', name:'Trinca de Missões', desc:'Complete Missões do Dia em 3 datas diferentes.', value:missions, goal:3}
  ].map(a => ({...a, unlocked:a.value >= a.goal}));
}

function renderAlbum(){
  const grid = document.getElementById('albumGrid');
  const countEl = document.getElementById('achievementCount');
  const textEl = document.getElementById('achievementText');
  if(!grid || !countEl || !textEl || !albumGames.length) return;
  const progress = albumProgress();
  const defs = achievementDefs(progress);
  const unlocked = defs.filter(a => a.unlocked).length;
  countEl.textContent = unlocked;
  textEl.textContent = `${unlocked} de ${defs.length} conquistas desbloqueadas`;
  grid.innerHTML = defs.map(a => {
    const pct = Math.min(100, Math.round((a.value / a.goal) * 100));
    return `<article class="achievement ${a.unlocked?'unlocked':'locked'}">
      <div class="achievement-icon">${a.unlocked?a.icon:'🔒'}</div>
      <div class="achievement-body"><strong>${a.name}</strong><p>${a.desc}</p><div class="achievement-bar"><span style="width:${pct}%"></span></div><small>${Math.min(a.value,a.goal)}/${a.goal}${a.unlocked?' · desbloqueada':''}</small></div>
    </article>`;
  }).join('');
}

(async()=>{
  try{
    const r = await fetch(`games.json?v=${Date.now()}`, {cache:'no-store'});
    if(!r.ok) return;
    const list = await r.json();
    albumGames = Array.isArray(list) ? list : [];
    renderAlbum();
  } catch {}
})();

document.addEventListener('click', () => setTimeout(renderAlbum, 40));
window.addEventListener('focus', renderAlbum);
