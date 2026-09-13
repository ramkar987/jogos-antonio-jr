#!/usr/bin/env python3
import json, re, shutil, sys, zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
IMPORTS = ROOT / 'imports'
GAMES_DIR = ROOT / 'jogos'
META = ROOT / 'games-imported.json'

GAMES_DIR.mkdir(exist_ok=True)
records = []

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

# Reimporta todos os ZIPs para que o resultado seja determinístico.
for zpath in sorted(IMPORTS.glob('*.zip')):
    work = ROOT / '.import-tmp' / zpath.stem
    if work.exists():
        shutil.rmtree(work)
    work.mkdir(parents=True)
    with zipfile.ZipFile(zpath) as z:
        z.extractall(work)
    for src in sorted(work.rglob('*.html')):
        name = re.sub(r'[^a-zA-Z0-9._-]+', '-', src.name).lower()
        dst = GAMES_DIR / name
        shutil.copy2(src, dst)
        title, desc = extract_meta(dst)
        records.append({
            'title': title,
            'file': f'jogos/{name}',
            'icon': '🎮',
            'categories': ['Importado'],
            'description': desc,
            'source': zpath.name,
        })

# remove duplicatas por arquivo mantendo a última ocorrência
by_file = {r['file']: r for r in records}
records = sorted(by_file.values(), key=lambda r: r['title'].casefold())
META.write_text(json.dumps(records, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(f'{len(records)} jogos importados.')
