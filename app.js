const BUILTIN_GAMES = [
  ['Pega-Gotas','pega_gotas','💧',['Ação','Coordenação'],'Mova o cesto e pegue as gotas antes que elas caiam no chão!'],
  ['Quebra-Blocos','quebra_blocos','🧱',['Ação','Coordenação'],'Rebata a bolinha e quebre todos os blocos.'],
  ['Caminho das Cores','caminho_das_cores','🌈',['Memória','Atenção'],'Observe as casas que brilham e repita a sequência.'],
  ['Estacionamento Maluco','estacionamento_maluco','🚗',['Raciocínio','Quebra-cabeça'],'Arraste os carros e abra caminho para o carro vermelho sair.'],
  ['Tangram Infantil','tangram_infantil','🔺',['Raciocínio','Quebra-cabeça'],'Use as sete peças para completar as figuras.'],
  ['Equilibra a Torre','equilibra_a_torre','🏗️',['Coordenação','Ação'],'Solte os blocos no lugar certo e construa a torre mais alta.'],
  ['Canhão de Bolinhas','canhao_de_bolinhas','🔵',['Ação','Estratégia'],'Mire, rebata nas paredes e junte bolinhas da mesma cor.'],
  ['Pescaria','pescaria','🎣',['Coordenação','Ação'],'Mova o anzol, pesque e recolha sem perder a captura.'],
  ['Entrega do Carteiro','entrega_do_carteiro','📮',['Raciocínio','Aventura'],'Encontre os melhores caminhos para fazer todas as entregas.'],
  ['Código Secreto de Setas','codigo_secreto_de_setas','⬆️',['Memória','Atenção'],'Veja o código e repita as setas na mesma ordem.'],
  ['Mini Pinball','mini_pinball','🟣',['Ação','Coordenação'],'Use os flippers, acerte os alvos e não deixe a bolinha cair.'],
  ['Corrida de Carrinhos','corrida_de_carrinhos','🏎️',['Ação','Coordenação'],'Desvie dos obstáculos, pegue moedas e vá mais longe.'],
  ['Submarino Aventureiro','submarino_aventureiro','🚤',['Aventura','Coordenação'],'Pegue tesouros e escape dos perigos do fundo do mar.'],
  ['Floresta dos Bichinhos Escondidos','floresta_bichinhos_escondidos','🐰',['Experimento','Audição'],'Escute de que lado o bichinho apareceu e responda usando os controles.',1],
  ['Bichinhos Camuflados','bichinhos_camuflados_misterio_das_cores','🦎',['Experimento','Cores'],'Encontre os bichinhos camuflados em um jogo de percepção de cores.',1],
  ['Snake Infantil','snake_infantil','🐍',['Ação','Coordenação'],'Ajude a cobrinha a comer frutas sem bater.'],
  ['Apaga-Incêndio','apaga_incendio','🚒',['Ação','Coordenação'],'Mova o bombeiro e apague o fogo antes que ele cresça.'],
  ['Trenzinho dos Vagões','trenzinho_dos_vagoes','🚂',['Memória','Raciocínio'],'Monte o trem na mesma ordem mostrada pela estação.'],
  ['Cofre dos Números','cofre_dos_numeros','🔐',['Raciocínio','Números'],'Descubra o número secreto usando as pistas de maior e menor.'],
  ['Robô Programável','robo_programavel','🤖',['Raciocínio','Programação'],'Monte os comandos e faça o robô chegar até a estrela.'],
  ['Salva-Bichinhos','salva_bichinhos','🐶',['Ação','Coordenação'],'Mova a cestinha e salve os bichinhos antes que caiam.'],
  ['Sapo Saltador','sapo_saltador','🐸',['Estratégia','Coordenação'],'Escolha a força e pule de folha em folha até a margem.'],
  ['Constrói a Ponte','constroi_a_ponte','🌉',['Raciocínio','Construção'],'Escolha as peças certas e faça a ponte aguentar a travessia.'],
  ['Espelho Mágico','espelho_magico','🪞',['Raciocínio','Percepção'],'Complete o outro lado exatamente como no espelho.'],
  ['Sombras Misteriosas','sombras_misteriosas','👤',['Percepção','Raciocínio'],'Leve cada figura até a sombra com o mesmo formato.'],
  ['Qual é o Intruso?','qual_e_o_intruso','🕵️',['Atenção','Raciocínio'],'Descubra qual figura não combina com as outras.']
].map(([title,key,icon,categories,description,special]) => ({
  title, icon, categories, description, special,
  file: `jogar.html?j=${encodeURIComponent(key)}`,
  source: 'Coleção original'
}));

let games = [...BUILTIN_GAMES];
let category = 'Todos';
const grid = document.getElementById('grid');
const search = document.getElementById('search');
const count = document.getElementById('resultCount');
const empty = document.getElementById('empty');
const chips = document.getElementById('chips');

function escapeHtml(value='') {
  return String(value).replace(/[&<>"']/g, ch => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[ch]));
}

function updateCategories() {
  const cats = ['Todos', ...new Set(games.flatMap(g => g.categories || []))];
  if (!cats.includes(category)) category = 'Todos';
  chips.innerHTML = cats.map(c => `<button class="chip ${c===category?'active':''}" data-cat="${escapeHtml(c)}">${escapeHtml(c)}</button>`).join('');
}

function render() {
  const q = search.value.trim().toLowerCase();
  const arr = games.filter(g =>
    (category === 'Todos' || (g.categories || []).includes(category)) &&
    (!q || `${g.title} ${g.description} ${(g.categories||[]).join(' ')}`.toLowerCase().includes(q))
  );
  grid.innerHTML = arr.map(g => `<article class="card ${g.special?'special':''}">
    <div class="game-icon">${escapeHtml(g.icon || '🎮')}</div>
    <h3>${escapeHtml(g.title)}</h3>
    <p>${escapeHtml(g.description || 'Jogo da coleção do Antônio Jr.')}</p>
    <div class="tags">${(g.categories||[]).map(c => `<span class="tag">${escapeHtml(c)}</span>`).join('')}</div>
    <a class="play" href="${escapeHtml(g.file)}" target="_blank" rel="noopener">JOGAR ▶</a>
  </article>`).join('');
  count.textContent = `${arr.length} jogo${arr.length===1?'':'s'}`;
  document.getElementById('gameCount').textContent = games.length;
  empty.style.display = arr.length ? 'none' : 'block';
}

chips.addEventListener('click', e => {
  const b = e.target.closest('[data-cat]');
  if (!b) return;
  category = b.dataset.cat;
  updateCategories();
  render();
});
search.addEventListener('input', render);
document.getElementById('clear').onclick = () => { search.value=''; category='Todos'; updateCategories(); render(); };
document.getElementById('random').onclick = () => {
  if (!games.length) return;
  const g = games[Math.floor(Math.random()*games.length)];
  window.open(g.file, '_blank', 'noopener');
};

const themeBtn = document.getElementById('theme');
function setTheme(t) {
  document.documentElement.dataset.theme = t;
  themeBtn.textContent = t === 'dark' ? '☀️' : '🌙';
  localStorage.setItem('antonio-jr-theme', t);
}
setTheme(localStorage.getItem('antonio-jr-theme') || (matchMedia('(prefers-color-scheme:dark)').matches ? 'dark' : 'light'));
themeBtn.onclick = () => setTheme(document.documentElement.dataset.theme === 'dark' ? 'light' : 'dark');

function normalizeGame(g, fallbackSource) {
  return {
    title: g.title || 'Jogo',
    file: g.file,
    icon: g.icon || '🎮',
    categories: Array.isArray(g.categories) ? g.categories : ['Outros'],
    description: g.description || 'Jogo da coleção do Antônio Jr.',
    source: g.source || fallbackSource
  };
}

(async () => {
  const catalogs = [
    ['games-imported.json', 'Importado'],
    ['games-custom.json', 'Coleção original']
  ];
  for (const [url, source] of catalogs) {
    try {
      const r = await fetch(`${url}?v=${Date.now()}`, {cache:'no-store'});
      if (!r.ok) continue;
      const list = await r.json();
      if (Array.isArray(list)) games.push(...list.map(g => normalizeGame(g, source)));
    } catch (err) {
      console.warn(`Não foi possível carregar ${url}:`, err);
    }
  }
  updateCategories();
  render();
})();
