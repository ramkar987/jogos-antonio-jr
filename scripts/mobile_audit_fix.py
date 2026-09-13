#!/usr/bin/env python3
import base64
import gzip
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read_text(path: Path) -> str:
    return path.read_text(encoding='utf-8', errors='replace')


def write_if_changed(path: Path, text: str) -> bool:
    old = read_text(path) if path.exists() else None
    if old == text:
        return False
    path.write_text(text, encoding='utf-8')
    return True


def patch_app():
    path = ROOT / 'app.js'
    text = read_text(path)
    old = "  window.open(g.file,'_blank','noopener');"
    new = "  const touchDevice = (navigator.maxTouchPoints || 0) > 0 || (window.matchMedia && window.matchMedia('(pointer: coarse)').matches);\n  if(touchDevice) location.assign(g.file);\n  else window.open(g.file,'_blank','noopener');"
    if old in text:
        text = text.replace(old, new, 1)
    return write_if_changed(path, text)


def patch_atravessa_text(text: str) -> str:
    text = text.replace(
        'Use as setas do teclado para atravessar sem ser atropelado nem cair na água!',
        'Use as setas do teclado ou os botões abaixo para atravessar sem ser atropelado nem cair na água!'
    )

    controls = '''\n  <div class="controls" aria-label="Controles de movimento">\n    <button class="ctrl-btn ctrl-up" data-move="up" aria-label="Mover para cima">▲</button>\n    <button class="ctrl-btn ctrl-left" data-move="left" aria-label="Mover para esquerda">◀</button>\n    <button class="ctrl-btn ctrl-down" data-move="down" aria-label="Mover para baixo">▼</button>\n    <button class="ctrl-btn ctrl-right" data-move="right" aria-label="Mover para direita">▶</button>\n  </div>\n'''
    marker = '  <button class="start-btn" id="start">Iniciar jogo</button>'
    if 'data-move="up"' not in text and marker in text:
        text = text.replace(marker, controls + '\n' + marker, 1)

    keyboard_block = """  document.addEventListener('keydown', (e) => {\n    if (!gameActive) return;\n    switch(e.key){\n      case 'ArrowUp': case 'w': case 'W':\n        movePlayer(-1, 0); e.preventDefault(); break;\n      case 'ArrowDown': case 's': case 'S':\n        movePlayer(1, 0); e.preventDefault(); break;\n      case 'ArrowLeft': case 'a': case 'A':\n        movePlayer(0, -1); e.preventDefault(); break;\n      case 'ArrowRight': case 'd': case 'D':\n        movePlayer(0, 1); e.preventDefault(); break;\n    }\n  });\n"""
    touch_block = keyboard_block + """\n  const MOVE_DIRS = {up:[-1,0], down:[1,0], left:[0,-1], right:[0,1]};\n  document.querySelectorAll('[data-move]').forEach(btn => {\n    btn.addEventListener('pointerdown', (e) => {\n      e.preventDefault();\n      const dir = MOVE_DIRS[btn.dataset.move];\n      if (dir) movePlayer(dir[0], dir[1]);\n    });\n  });\n"""
    if 'const MOVE_DIRS' not in text and keyboard_block in text:
        text = text.replace(keyboard_block, touch_block, 1)

    text = text.replace(
        "statusEl.textContent = 'Vai! Use as setas do teclado pra atravessar';",
        "statusEl.textContent = 'Vai! Use as setas ou os botões para atravessar';"
    )
    return text


def patch_atravessa():
    path = ROOT / 'jogos' / 'atravessa-a-rua.html'
    if not path.exists():
        return False
    return write_if_changed(path, patch_atravessa_text(read_text(path)))


def patch_importer():
    path = ROOT / 'scripts' / 'import_games.py'
    text = read_text(path)
    if 'def apply_mobile_fixes' not in text:
        anchor = "def safe_extract(z: zipfile.ZipFile, dest: Path):\n"
        helper = '''def apply_mobile_fixes(path: Path):\n    # Correções persistentes para jogos importados do ZIP original.\n    # Assim um novo processamento de imports/ não desfaz ajustes de celular.\n    if path.name == 'atravessa-a-rua.html':\n        text = path.read_text(encoding='utf-8', errors='replace')\n        text = text.replace(\n            'Use as setas do teclado para atravessar sem ser atropelado nem cair na água!',\n            'Use as setas do teclado ou os botões abaixo para atravessar sem ser atropelado nem cair na água!'\n        )\n        controls = """\\n  <div class=\\"controls\\" aria-label=\\"Controles de movimento\\">\\n    <button class=\\"ctrl-btn ctrl-up\\" data-move=\\"up\\" aria-label=\\"Mover para cima\\">▲</button>\\n    <button class=\\"ctrl-btn ctrl-left\\" data-move=\\"left\\" aria-label=\\"Mover para esquerda\\">◀</button>\\n    <button class=\\"ctrl-btn ctrl-down\\" data-move=\\"down\\" aria-label=\\"Mover para baixo\\">▼</button>\\n    <button class=\\"ctrl-btn ctrl-right\\" data-move=\\"right\\" aria-label=\\"Mover para direita\\">▶</button>\\n  </div>\\n"""\n        marker = '  <button class=\\"start-btn\\" id=\\"start\\">Iniciar jogo</button>'\n        if 'data-move=\\"up\\"' not in text and marker in text:\n            text = text.replace(marker, controls + '\\n' + marker, 1)\n        keyboard = """  document.addEventListener('keydown', (e) => {\\n    if (!gameActive) return;\\n    switch(e.key){\\n      case 'ArrowUp': case 'w': case 'W':\\n        movePlayer(-1, 0); e.preventDefault(); break;\\n      case 'ArrowDown': case 's': case 'S':\\n        movePlayer(1, 0); e.preventDefault(); break;\\n      case 'ArrowLeft': case 'a': case 'A':\\n        movePlayer(0, -1); e.preventDefault(); break;\\n      case 'ArrowRight': case 'd': case 'D':\\n        movePlayer(0, 1); e.preventDefault(); break;\\n    }\\n  });\\n"""\n        if 'const MOVE_DIRS' not in text and keyboard in text:\n            extra = keyboard + """\\n  const MOVE_DIRS = {up:[-1,0], down:[1,0], left:[0,-1], right:[0,1]};\\n  document.querySelectorAll('[data-move]').forEach(btn => {\\n    btn.addEventListener('pointerdown', (e) => {\\n      e.preventDefault();\\n      const dir = MOVE_DIRS[btn.dataset.move];\\n      if (dir) movePlayer(dir[0], dir[1]);\\n    });\\n  });\\n"""\n            text = text.replace(keyboard, extra, 1)\n        text = text.replace(\n            "statusEl.textContent = 'Vai! Use as setas do teclado pra atravessar';",\n            "statusEl.textContent = 'Vai! Use as setas ou os botões para atravessar';"\n        )\n        path.write_text(text, encoding='utf-8')\n\n'''
        if anchor in text:
            text = text.replace(anchor, helper + anchor, 1)

    copy_line = '        shutil.copy2(src, dst)\n        title, desc = extract_meta(dst)'
    if 'apply_mobile_fixes(dst)' not in text and copy_line in text:
        text = text.replace(copy_line, '        shutil.copy2(src, dst)\n        apply_mobile_fixes(dst)\n        title, desc = extract_meta(dst)', 1)
    return write_if_changed(path, text)


def extract_title(html: str, fallback: str) -> str:
    m = re.search(r'<title[^>]*>(.*?)</title>', html, re.I | re.S)
    if m:
        return re.sub(r'<[^>]+>', '', m.group(1)).strip()[:100]
    return fallback


def signals(html: str):
    low = html.lower()
    keyboard = bool(re.search(r'keydown|keyup|keycode|arrowup|arrowdown|arrowleft|arrowright|ctrlleft|ctrlright|controlleft|controlright|e\.key|event\.key', low))
    pointer = bool(re.search(r'pointerdown|pointermove|pointerup|pointercancel', low))
    touch = bool(re.search(r'touchstart|touchmove|touchend|touchcancel', low))
    mouse = bool(re.search(r'mousedown|mousemove|mouseup|mouseenter|mouseleave', low))
    click = bool(re.search(r"addEventListener\s*\(\s*['\"]click|onclick\s*=", html, re.I))
    virtual = bool(re.search(r'data-move|ctrl-btn|d-?pad|joystick|touch-controls|mobile-controls|virtual-key|control-btn', low))
    viewport = 'name="viewport"' in low or "name='viewport'" in low
    coarse_safe = pointer or touch or virtual
    if keyboard and not coarse_safe and not click:
        risk = 'ALTO'
        reason = 'depende de teclado e não há controle touch evidente'
    elif mouse and not (pointer or touch):
        risk = 'MÉDIO'
        reason = 'usa eventos de mouse sem Pointer/Touch evidente'
    elif keyboard and not virtual and not (pointer or touch):
        risk = 'MÉDIO'
        reason = 'usa teclado; há clique, mas o controle mobile precisa ser validado'
    elif not viewport:
        risk = 'MÉDIO'
        reason = 'sem meta viewport'
    else:
        risk = 'BAIXO'
        reason = 'há interação compatível com toque ou não há dependência móvel óbvia'
    modes=[]
    if keyboard: modes.append('teclado')
    if pointer: modes.append('pointer')
    if touch: modes.append('touch')
    if mouse: modes.append('mouse')
    if click: modes.append('clique')
    if virtual: modes.append('controle-na-tela')
    return risk, reason, ', '.join(modes) or 'não identificado'


def build_audit():
    entries=[]
    for path in sorted((ROOT/'jogos').glob('*.html')):
        html=read_text(path)
        risk,reason,modes=signals(html)
        entries.append((risk, extract_title(html,path.stem), f'jogos/{path.name}', modes, reason, 'HTML'))
    for path in sorted((ROOT/'data').glob('*.gz.b64')):
        try:
            raw=base64.b64decode(read_text(path).strip())
            html=gzip.decompress(raw).decode('utf-8','replace')
        except Exception as exc:
            entries.append(('ALTO',path.stem,f'data/{path.name}','erro',f'não foi possível analisar: {exc}','compactado'))
            continue
        risk,reason,modes=signals(html)
        entries.append((risk, extract_title(html,path.stem), f'data/{path.name}', modes, reason, 'compactado'))

    order={'ALTO':0,'MÉDIO':1,'BAIXO':2}
    entries.sort(key=lambda x:(order.get(x[0],9),x[1].casefold()))
    counts={k:sum(1 for e in entries if e[0]==k) for k in order}
    lines=[
        '# 📱 Auditoria de compatibilidade mobile', '',
        'Relatório estático gerado automaticamente. Ele aponta riscos prováveis no código; não substitui teste real em iPhone/Android.', '',
        f'**Total analisado:** {len(entries)} arquivos de jogos · **alto:** {counts["ALTO"]} · **médio:** {counts["MÉDIO"]} · **baixo:** {counts["BAIXO"]}', '',
        '## Prioridade', '',
        '| Risco | Jogo | Arquivo | Entradas detectadas | Motivo |',
        '|---|---|---|---|---|'
    ]
    for risk,title,file,modes,reason,kind in entries:
        safe=lambda s:str(s).replace('|','\\|').replace('\n',' ')
        lines.append(f'| {risk} | {safe(title)} | `{file}` | {safe(modes)} | {safe(reason)} |')
    lines += ['', '## Critérios', '',
              '- **ALTO:** dependência de teclado sem alternativa touch clara.',
              '- **MÉDIO:** eventos de mouse sem Pointer/Touch, controle móvel ambíguo ou ausência de viewport.',
              '- **BAIXO:** há Pointer/Touch/controle na tela ou nenhuma dependência móvel óbvia.', '',
              '> Os 26 jogos antigos em `data/*.gz.b64` também são descompactados e analisados pelo script.']
    write_if_changed(ROOT/'MOBILE_AUDIT.md','\n'.join(lines)+'\n')
    return counts, len(entries)


if __name__ == '__main__':
    changed=[]
    if patch_app(): changed.append('app.js')
    if patch_atravessa(): changed.append('jogos/atravessa-a-rua.html')
    if patch_importer(): changed.append('scripts/import_games.py')
    counts,total=build_audit()
    print('Arquivos ajustados:', ', '.join(changed) or 'nenhum')
    print(f'Auditoria: {total} jogos; alto={counts["ALTO"]}, médio={counts["MÉDIO"]}, baixo={counts["BAIXO"]}')
