#!/usr/bin/env python3
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
PATH=ROOT/'MOBILE_AUDIT.md'
text=PATH.read_text(encoding='utf-8')
lines=text.splitlines()

# Página auxiliar/legada de listagem, não é um dos jogos do games.json.
lines=[line for line in lines if '`jogos/novos-jogos.html`' not in line]

# Revisão manual do código: nesses três casos o teclado é apenas um atalho;
# a ação principal está disponível por botões/peças clicáveis, que funcionam por toque.
reviewed={
    'A Aventura de Blinky':'teclado é atalho; comandos principais são botões/blocos clicáveis',
    'Jogo da Forca':'teclado físico é atalho; há teclado virtual clicável na tela',
    'Quebra-Cabeça Deslizante':'setas são atalho; as peças podem ser movidas por toque/clique',
}
for i,line in enumerate(lines):
    for title,reason in reviewed.items():
        needle=f'| MÉDIO | {title} |'
        if line.startswith(needle):
            parts=line.split('|')
            # ['', ' MÉDIO ', ' title ', ' file ', ' modes ', ' reason ', '']
            parts[1]=' BAIXO '
            parts[5]=f' {reason} '
            lines[i]='|'.join(parts)

# Recalcula resumo a partir da tabela.
rows=[line for line in lines if line.startswith('| ALTO |') or line.startswith('| MÉDIO |') or line.startswith('| BAIXO |')]
counts={r:sum(1 for line in rows if line.startswith(f'| {r} |')) for r in ('ALTO','MÉDIO','BAIXO')}
for i,line in enumerate(lines):
    if line.startswith('**Total analisado:**'):
        lines[i]=f'**Total analisado:** {len(rows)} jogos do catálogo · **alto:** {counts["ALTO"]} · **médio:** {counts["MÉDIO"]} · **baixo:** {counts["BAIXO"]}'
        break

# Reordena apenas as linhas da tabela por risco e título.
header_idx=next(i for i,l in enumerate(lines) if l.startswith('| Risco |'))
sep_idx=header_idx+1
start=sep_idx+1
end=start
while end<len(lines) and lines[end].startswith('|'):
    end+=1
order={'ALTO':0,'MÉDIO':1,'BAIXO':2}
def key(line):
    p=[x.strip() for x in line.split('|')]
    return (order.get(p[1],9),p[2].casefold())
lines[start:end]=sorted(lines[start:end],key=key)

PATH.write_text('\n'.join(lines)+'\n',encoding='utf-8')
print(f'Auditoria refinada: {len(rows)} jogos; alto={counts["ALTO"]}, médio={counts["MÉDIO"]}, baixo={counts["BAIXO"]}')
