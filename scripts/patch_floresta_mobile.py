#!/usr/bin/env python3
import base64, gzip
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
PATH=ROOT/'data'/'floresta_bichinhos_escondidos.gz.b64'
raw=base64.b64decode(PATH.read_text(encoding='utf-8').strip())
html=gzip.decompress(raw).decode('utf-8','replace')

html=html.replace(
    'Quando você <strong>escutar um bichinho</strong>, aperte o Ctrl do mesmo lado do som!',
    'Quando você <strong>escutar um bichinho</strong>, responda pelo lado do som: use Ctrl no computador ou os botões 👂 no celular!'
)

if 'id="mobileEarControls"' not in html:
    css='''\n<style id="mobileEarStyle">\n#mobileEarControls{display:none;position:fixed;left:10px;right:10px;bottom:max(10px,env(safe-area-inset-bottom));z-index:9999;grid-template-columns:1fr 1fr;gap:10px;pointer-events:none}\n#mobileEarControls button{pointer-events:auto;min-height:64px;border:0;border-radius:18px;font:800 15px system-ui,-apple-system,sans-serif;color:#fff;box-shadow:0 7px 24px rgba(0,0,0,.22);touch-action:manipulation}\n#mobileEarLeft{background:#378ADD}#mobileEarRight{background:#E24B4A}\n#mobileEarControls button:active{transform:scale(.97)}\n@media (pointer:coarse),(max-width:820px){#mobileEarControls{display:grid}body{padding-bottom:92px!important}}\n</style>\n'''
    controls='''\n<div id="mobileEarControls" aria-label="Controles de resposta por ouvido">\n  <button id="mobileEarLeft" type="button">👂 ESQUERDA</button>\n  <button id="mobileEarRight" type="button">DIREITA 👂</button>\n</div>\n<script id="mobileEarScript">\n(()=>{\n  function emitControl(side){\n    const right=side==='right', init={key:'Control',code:right?'ControlRight':'ControlLeft',location:right?2:1,ctrlKey:true,bubbles:true,cancelable:true};\n    try{document.dispatchEvent(new KeyboardEvent('keydown',init));}catch(_){return}\n    setTimeout(()=>{try{document.dispatchEvent(new KeyboardEvent('keyup',init));}catch(_){}},70);\n  }\n  document.getElementById('mobileEarLeft')?.addEventListener('pointerdown',e=>{e.preventDefault();emitControl('left')});\n  document.getElementById('mobileEarRight')?.addEventListener('pointerdown',e=>{e.preventDefault();emitControl('right')});\n})();\n</script>\n'''
    html=html.replace('</head>',css+'</head>',1)
    html=html.replace('</body>',controls+'</body>',1)

encoded=base64.b64encode(gzip.compress(html.encode('utf-8'),compresslevel=9,mtime=0)).decode('ascii')+'\n'
PATH.write_text(encoded,encoding='utf-8')
print('Floresta: controles mobile aplicados.')
