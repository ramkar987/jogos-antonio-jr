# Migração em lote

O projeto aceita ZIPs de jogos HTML pela pasta `imports/`.

Ao enviar um ZIP, o workflow `Importar jogos`:

1. extrai todos os `.html` com validação contra caminhos inseguros;
2. copia os jogos para `jogos/`;
3. atualiza diretamente o catálogo único `games.json`;
4. preserva entradas manuais (`origin` diferente de `import`);
5. publica as alterações automaticamente.

A página inicial lê somente `games.json`. Os antigos arquivos `games-imported.json` e `games-custom.json` não fazem mais parte da arquitetura.
