# 🌎 Mundo Antônio Jr.

Coleção de jogos infantis em HTML, CSS e JavaScript para brincar, pensar, criar e aprender direto no navegador.

## 🌐 Jogar

https://ramkar987.github.io/jogos-antonio-jr/

## ✨ O que virou o projeto

A antiga grade de jogos evoluiu para o **Mundo Antônio Jr.**. A página inicial organiza os jogos por regiões, mantém busca e filtros e salva localmente no navegador:

- jogos explorados e estrelas;
- favoritos;
- missão do dia;
- progresso por região;
- álbum de conquistas;
- tema claro/escuro.

O projeto também possui um manifesto PWA e cache básico para melhorar o uso offline depois que os arquivos já foram visitados.

## 🏅 Álbum de conquistas

O álbum usa somente o progresso já salvo no navegador e não precisa de conta ou servidor. As conquistas são calculadas a partir de atividades como:

- explorar diferentes quantidades de jogos;
- visitar todas as regiões do Mundo;
- jogar desafios de ação, memória, programação e números;
- completar Missões do Dia em datas diferentes.

As conquistas são progressivas e aparecem bloqueadas até que o objetivo seja atingido.

## 🗺️ Regiões

- 🏎️ Pista de Aventura — ação, coordenação e aventura;
- 🏰 Castelo dos Desafios — lógica, estratégia e quebra-cabeças;
- 🌳 Floresta da Memória — memória, atenção e percepção;
- 🔬 Laboratório de Ideias — programação, construção e criatividade;
- 📚 Escola Mágica — palavras, números, música e sequências;
- 🎡 Parque de Diversões — simulações e experiências diferentes.

## 📚 Catálogo

`games.json` é a fonte única usada pela página inicial. Cada jogo possui, no mínimo:

```json
{
  "id": "meu-jogo",
  "title": "Meu Jogo",
  "file": "jogos/meu-jogo.html",
  "icon": "🎮",
  "categories": ["Raciocínio"],
  "description": "Descrição curta.",
  "origin": "custom",
  "source": "Coleção original"
}
```

Os jogos mais antigos ainda são abertos pelo `jogar.html`, que funciona como camada de compatibilidade para os arquivos compactados em `data/`. Jogos novos e importados ficam normalmente em `jogos/`.

## ➕ Adicionar novos jogos por ZIP

1. Abra a pasta `imports/` no GitHub.
2. Use **Add file → Upload files**.
3. Envie um `.zip` contendo jogos `.html` standalone.
4. Faça o commit.
5. O workflow **Importar jogos** extrai os HTMLs para `jogos/` e atualiza diretamente o `games.json`.

O importador preserva os jogos manuais e substitui somente entradas com `origin: "import"`. Se um ZIP tentar usar o mesmo arquivo de um jogo manual, ele é ignorado para não sobrescrever a coleção criada no repositório.

## 🧪 Jogos experimentais

Os jogos de audição e percepção de cores são experimentos lúdicos e não substituem avaliação profissional.
