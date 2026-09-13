#!/usr/bin/env python3
import base64, gzip, re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]

def read_html(path):
    if path.suffix=='.b64':
        raw=base64.b64decode(path.read_text(encoding='utf-8').strip())
        return gzip.decompress(raw).decode('utf-8','replace')
    return path.read_text(encoding='utf-8',errors='replace')

def title(html,name):
    m=re.search(r'<title[^>]*>(.*?)</title>',html,re.I|re.S)
    return re.sub(r'<[^>]+>','',m.group(1)).strip() if m else name

paths=list((ROOT/'jogos').glob('*.html'))+list((ROOT/'data').glob('*.gz.b64'))
out=['# ⌨️ Controles que merecem validação no celular','',
     'Trechos gerados automaticamente para ajudar a revisão dos jogos que usam teclado.','']
for path in sorted(paths,key=lambda p:p.name):
    try: html=read_html(path)
    except Exception: continue
    if not re.search(r'keydown|keyup|Arrow(?:Up|Down|Left|Right)|Ctrl|Control',html,re.I): continue
    lines=html.splitlines()
    hits=[]
    for i,line in enumerate(lines):
        if re.search(r'keydown|keyup|Arrow(?:Up|Down|Left|Right)|Ctrl|Control',line,re.I):
            a=max(0,i-3); b=min(len(lines),i+9)
            snippet='\n'.join(lines[a:b])
            if snippet not in hits: hits.append(snippet)
        if len(hits)>=3: break
    out += [f'## {title(html,path.stem)}', '', f'`{path.relative_to(ROOT)}`', '']
    for s in hits:
        out += ['```html', s[:3500], '```', '']
(ROOT/'MOBILE_KEYBOARD_SNIPPETS.md').write_text('\n'.join(out)+'\n',encoding='utf-8')
print('Relatório de trechos criado.')
