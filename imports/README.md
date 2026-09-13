# Importação de jogos

Para adicionar novos jogos à central, envie um arquivo `.zip` para esta pasta.

O GitHub Actions executará automaticamente o workflow **Importar jogos**, extrairá todos os arquivos `.html` encontrados, copiará os jogos para `jogos/` e atualizará `games-imported.json`.

Cada jogo deve ser preferencialmente um HTML standalone (HTML + CSS + JavaScript no mesmo arquivo).
