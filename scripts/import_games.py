#!/usr/bin/env python3
import json, re, shutil, zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
IMPORTS = ROOT / 'imports'
GAMES_DIR = ROOT / 'jogos'
META = ROOT / 'games-imported.json'

GAMES_DIR.mkdir(exist_ok=True)
records = []

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

def safe_extract(z: zipfile.ZipFile, dest: Path):
    base = dest.resolve()
    for member in z.infolist():
        target = (dest / member.filename).resolve()
        if target != base and base not in target.parents:
            raise ValueError(f'Caminho inseguro no ZIP: {member.filename}')
    z.extractall(dest)

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
        dst = GAMES_DIR / name
        shutil.copy2(src, dst)
        title, desc = extract_meta(dst)
        icon, categories = KNOWN.get(name, ('🎮', ['Importado']))
        records.append({
            'title': title,
            'file': f'jogos/{name}',
            'icon': icon,
            'categories': categories,
            'description': desc,
            'source': zpath.name,
        })

by_file = {r['file']: r for r in records}
records = sorted(by_file.values(), key=lambda r: r['title'].casefold())
META.write_text(json.dumps(records, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(f'{len(records)} jogos importados.')
