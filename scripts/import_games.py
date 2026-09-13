#!/usr/bin/env python3
import json, re, shutil, zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
IMPORTS = ROOT / 'imports'
GAMES_DIR = ROOT / 'jogos'
CATALOG = ROOT / 'games.json'

GAMES_DIR.mkdir(exist_ok=True)

KNOWN = {
    'torre-de-formas.html': ('🔺', ['Raciocínio', 'Percepção']),
    'toupeira-maluca.html': ('🔨', ['Ação', 'Coordenação']),
    'caca-palavras.html': ('🔤', ['Palavras', 'Atenção']),
    'jogo-da-velha.html': ('⭕', ['Estratégia', 'Raciocínio']),
    'trilha-moinho.html': ('⚫', ['Estratégia', 'Raciocínio']),
    'batalha-naval.html': ('🚢', ['Estratégia', 'Raciocínio']),
    'labirinto-eletrico.html': ('⚡', ['Coordenação', 'Atenção']),
    'cara-a-cara.html': ('🙂', ['Raciocínio', 'Percepção']),
    'corta-frutas.html': ('🍉', ['Ação', 'Coordenação']),
    'ligue-4.html': ('🔴', ['Estratégia', 'Raciocínio']),
    'jogo-da-memoria.html': ('🧠', ['Memória', 'Atenção']),
    'cara-maluca.html': ('🤪', ['Percepção', 'Atenção']),
    'robo-programacao-reversa.html': ('🤖', ['Programação', 'Raciocínio']),
    'mastermind.html': ('🧩', ['Raciocínio', 'Estratégia']),
    'jogo-dos-quadradinhos.html': ('🟦', ['Estratégia', 'Raciocínio']),
    'siga-os-numeros.html': ('🔢', ['Memória', 'Números']),
    'jogo-de-damas.html': ('🔴', ['Estratégia', 'Raciocínio']),
    'jogo-da-forca.html': ('🔤', ['Palavras', 'Raciocínio']),
    'duelo-de-bananas.html': ('🍌', ['Coordenação', 'Estratégia']),
    'resta-um.html': ('🟢', ['Raciocínio', 'Quebra-cabeça']),
    'atravessa-a-rua.html': ('🚦', ['Ação', 'Coordenação']),
    'aventura-do-blinky.html': ('👾', ['Programação', 'Raciocínio']),
    'passarinho-faminto.html': ('🐦', ['Ação', 'Coordenação']),
    'fabrica-de-pintinhos.html': ('🐥', ['Estratégia', 'Raciocínio']),
    'sequencia-da-memoria.html': ('🔢', ['Memória', 'Números']),
    'mesa-de-ar.html': ('🏒', ['Ação', 'Coordenação']),
}

def clean_text(html):
    text = re.sub(r'<[^>]+>', ' ', html)
    return re.sub(r'\s+', ' ', text).strip()

def extract_meta(path: Path):
    text = path.read_text(encoding='utf-8', errors='replace')
    title_m = re.search(r'<title[^>]*>(.*?)</title>', text, re.I | re.S)
    h1_m = re.search(r'<h1[^>]*>(.*?)</h1>', text, re.I | re.S)
    p_m = re.search(r'<p[^>]*>(.*?)</p>', text, re.I | re.S)
    title = clean_text((title_m or h1_m).group(1)) if (title_m or h1_m) else path.stem.replace('-', ' ').title()
    desc = clean_text(p_m.group(1)) if p_m else 'Jogo importado para a coleção do Antônio Jr.'
    return title[:100], desc[:180]

def apply_mobile_fixes(path: Path):
    # Correções persistentes para jogos importados do ZIP original.
    # Assim um novo processamento de imports/ não desfaz ajustes de celular.
    if path.name == 'atravessa-a-rua.html':
        text = path.read_text(encoding='utf-8', errors='replace')
        text = text.replace(
            'Use as setas do teclado para atravessar sem ser atropelado nem cair na água!',
            'Use as setas do teclado ou os botões abaixo para atravessar sem ser atropelado nem cair na água!'
        )
        controls = """\n  <div class=\"controls\" aria-label=\"Controles de movimento\">\n    <button class=\"ctrl-btn ctrl-up\" data-move=\"up\" aria-label=\"Mover para cima\">▲</button>\n    <button class=\"ctrl-btn ctrl-left\" data-move=\"left\" aria-label=\"Mover para esquerda\">◀</button>\n    <button class=\"ctrl-btn ctrl-down\" data-move=\"down\" aria-label=\"Mover para baixo\">▼</button>\n    <button class=\"ctrl-btn ctrl-right\" data-move=\"right\" aria-label=\"Mover para direita\">▶</button>\n  </div>\n"""
        marker = '  <button class=\"start-btn\" id=\"start\">Iniciar jogo</button>'
        if 'data-move=\"up\"' not in text and marker in text:
            text = text.replace(marker, controls + '\n' + marker, 1)
        keyboard = """  document.addEventListener('keydown', (e) => {\n    if (!gameActive) return;\n    switch(e.key){\n      case 'ArrowUp': case 'w': case 'W':\n        movePlayer(-1, 0); e.preventDefault(); break;\n      case 'ArrowDown': case 's': case 'S':\n        movePlayer(1, 0); e.preventDefault(); break;\n      case 'ArrowLeft': case 'a': case 'A':\n        movePlayer(0, -1); e.preventDefault(); break;\n      case 'ArrowRight': case 'd': case 'D':\n        movePlayer(0, 1); e.preventDefault(); break;\n    }\n  });\n"""
        if 'const MOVE_DIRS' not in text and keyboard in text:
            extra = keyboard + """\n  const MOVE_DIRS = {up:[-1,0], down:[1,0], left:[0,-1], right:[0,1]};\n  document.querySelectorAll('[data-move]').forEach(btn => {\n    btn.addEventListener('pointerdown', (e) => {\n      e.preventDefault();\n      const dir = MOVE_DIRS[btn.dataset.move];\n      if (dir) movePlayer(dir[0], dir[1]);\n    });\n  });\n"""
            text = text.replace(keyboard, extra, 1)
        text = text.replace(
            "statusEl.textContent = 'Vai! Use as setas do teclado pra atravessar';",
            "statusEl.textContent = 'Vai! Use as setas ou os botões para atravessar';"
        )
        path.write_text(text, encoding='utf-8')

def safe_extract(z: zipfile.ZipFile, dest: Path):
    base = dest.resolve()
    for member in z.infolist():
        target = (dest / member.filename).resolve()
        if target != base and base not in target.parents:
            raise ValueError(f'Caminho inseguro no ZIP: {member.filename}')
    z.extractall(dest)

def load_catalog():
    if not CATALOG.exists():
        return []
    try:
        data = json.loads(CATALOG.read_text(encoding='utf-8'))
        return data if isinstance(data, list) else []
    except Exception:
        return []

catalog = load_catalog()
manual = [r for r in catalog if r.get('origin') != 'import']
old_imports = {r.get('file'): r for r in catalog if r.get('origin') == 'import'}
manual_files = {r.get('file') for r in manual}
records = []

for zpath in sorted(IMPORTS.glob('*.zip')):
    work = ROOT / '.import-tmp' / zpath.stem
    if work.exists():
        shutil.rmtree(work)
    work.mkdir(parents=True)
    try:
        with zipfile.ZipFile(zpath) as z:
            safe_extract(z, work)
    except zipfile.BadZipFile:
        print(f'Ignorando ZIP inválido: {zpath.name}')
        continue

    for src in sorted(work.rglob('*.html')):
        name = re.sub(r'[^a-zA-Z0-9._-]+', '-', src.name).lower()
        rel = f'jogos/{name}'
        if rel in manual_files:
            print(f'Ignorando {name}: já existe como jogo manual.')
            continue
        dst = GAMES_DIR / name
        shutil.copy2(src, dst)
        apply_mobile_fixes(dst)
        title, desc = extract_meta(dst)
        old = old_imports.get(rel, {})
        icon, categories = KNOWN.get(name, (old.get('icon', '🎮'), old.get('categories', ['Importado'])))
        records.append({
            'id': old.get('id') or Path(name).stem,
            'title': old.get('title') or title,
            'file': rel,
            'icon': icon,
            'categories': categories,
            'description': old.get('description') or desc,
            'origin': 'import',
            'source': zpath.name,
        })

by_file = {r['file']: r for r in records}
imports = sorted(by_file.values(), key=lambda r: r['title'].casefold())
final = manual + imports
CATALOG.write_text(json.dumps(final, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(f'{len(imports)} jogos importados; {len(final)} jogos no catálogo total.')
