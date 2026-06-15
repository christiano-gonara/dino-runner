# TERMO

Jogo de adivinhação de palavras inspirado no Wordle/Termo, desenvolvido com Python e pygame-ce.

## Integrantes do grupo

- Christiano Gonçalves Araujo

## Estrutura do projeto

- `main.py`: ponto de entrada da aplicação.
- `src/`: código-fonte principal do jogo (configurações, funções lógicas, dados e loop principal).
- `assets/`: imagens e fontes.
- `data/`: arquivos de palavras e recorde.
- `tests/`: testes unitários com `pytest`.
- `docs/`: documentação do projeto, incluindo proposta inicial.

## Descrição do jogo

> O jogador tem 6 tentativas para adivinhar uma palavra secreta. A cada tentativa, as letras recebem cores que indicam se estão corretas e na posição certa (verde), se estão na palavra mas em posição errada (amarelo), ou se não fazem parte da palavra (cinza). O jogo possui 3 níveis de dificuldade: Fácil (4 letras), Médio (5 letras) e Difícil (6 letras).

## Objetivo do jogador

> Adivinhar a palavra secreta no menor número de tentativas possível, acumulando vitórias ao longo das partidas.

## Regras do jogo

- Escolha uma dificuldade na tela inicial (Fácil = 4 letras, Médio = 5 letras, Difícil = 6 letras).
- Digite letras no teclado para formar sua tentativa.
- Pressione ENTER para confirmar a tentativa.
- Letras verdes = letra correta na posição correta.
- Letras amarelas = letra correta em posição errada.
- Letras cinza = letra não está na palavra secreta.
- Você tem 6 tentativas para acertar a palavra.
- Após o fim da partida, pressione R para jogar novamente ou ESC para sair.

## Controles

- Teclas A-Z: digitar letras
- BACKSPACE: apagar a última letra
- ENTER: confirmar tentativa
- R (na tela de fim): jogar novamente
- ESC: sair do jogo

## Como executar o projeto

```bash
git clone LINK_DO_REPOSITORIO
cd NOME_DA_PASTA
pip install -r requirements.txt
python main.py
```

## Como executar os testes

```bash
python -m pytest
```

## Checklist para entrega

- README atualizado com descrição, regras e controles.
- `docs/proposta.MD` atualizado com a nova proposta.
- Jogo executa com `python main.py`.
- Testes passam com `pytest`.
