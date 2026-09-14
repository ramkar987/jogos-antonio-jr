#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
path = ROOT / 'scripts' / 'import_games.py'
text = path.read_text(encoding='utf-8')

imp = "from mobile_drag_upgrade import patch_file as apply_drag_upgrade\n"
if imp not in text:
    marker = "from pathlib import Path\n"
    text = text.replace(marker, marker + imp, 1)

old = "        shutil.copy2(src, dst)\n        apply_mobile_fixes(dst)\n        title, desc = extract_meta(dst)"
new = "        shutil.copy2(src, dst)\n        apply_mobile_fixes(dst)\n        apply_drag_upgrade(dst)\n        title, desc = extract_meta(dst)"
if old in text and 'apply_drag_upgrade(dst)' not in text:
    text = text.replace(old, new, 1)

path.write_text(text, encoding='utf-8')
print('Hook de melhorias mobile instalado no importador.')
