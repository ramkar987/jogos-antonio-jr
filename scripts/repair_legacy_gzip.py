#!/usr/bin/env python3
import base64, gzip, zlib
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
TARGETS=['cofre_dos_numeros.gz.b64','estacionamento_maluco.gz.b64']

def raw_payload(data: bytes):
    if len(data)<18 or data[:2]!=b'\x1f\x8b' or data[2]!=8:
        raise ValueError('gzip inválido')
    flags=data[3]
    pos=10
    if flags & 0x04:
        xlen=int.from_bytes(data[pos:pos+2],'little'); pos+=2+xlen
    if flags & 0x08:
        pos=data.index(b'\x00',pos)+1
    if flags & 0x10:
        pos=data.index(b'\x00',pos)+1
    if flags & 0x02:
        pos+=2
    return data[pos:-8]

for name in TARGETS:
    path=ROOT/'data'/name
    if not path.exists():
        print(name, 'não encontrado')
        continue
    data=base64.b64decode(path.read_text(encoding='utf-8').strip())
    try:
        gzip.decompress(data)
        print(name, 'já está íntegro')
        continue
    except Exception as exc:
        print(name, 'falhou validação:', exc)
    try:
        html=zlib.decompress(raw_payload(data),-15)
    except Exception as exc:
        print(name, 'não reparado; stream DEFLATE também está danificado:', exc)
        continue
    repaired=gzip.compress(html,compresslevel=9,mtime=0)
    # validação antes de gravar
    gzip.decompress(repaired)
    path.write_text(base64.b64encode(repaired).decode('ascii')+'\n',encoding='utf-8')
    print(name, 'CRC/trailer reconstruído com sucesso')
