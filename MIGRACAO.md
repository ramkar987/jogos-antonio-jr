# Migração em lote

O projeto aceita ZIPs de jogos HTML pela pasta `imports/`.

Ao enviar um ZIP, o workflow `Importar jogos`:

1. extrai todos os `.html`;
2. copia para `jogos/`;
3. gera `games-imported.json`;
4. publica tudo automaticamente.

A central carrega o catálogo original e o catálogo importado.
