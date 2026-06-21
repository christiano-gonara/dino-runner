# Dino Runner

Projeto final da disciplina de Introdução a Algoritmos/Programação, desenvolvido com Python e Pygame.

## Integrantes do grupo

- Christiano Gonçalves Araujo

## Descrição do jogo

O jogador controla um dinossauro que corre automaticamente e deve sobreviver por 30 segundos desviando de obstáculos. O jogo conta com cactos de diferentes tamanhos e pássaros como obstáculos, sistema de 3 vidas, invulnerabilidade temporária após tomar dano e ranking dos 5 melhores pontuações.

## Objetivo do jogador

Sobreviver por 30 segundos desviando de todos os obstáculos. Quanto mais tempo sobreviver, mais pontos acumula e mais rápido o jogo fica.

## Regras do jogo

- O jogador começa com 3 vidas.
- Colidir com um obstáculo remove 1 vida e ativa invulnerabilidade por 2 segundos.
- A velocidade dos obstáculos aumenta progressivamente com a pontuação.
- A partida termina quando o jogador perde todas as vidas ou sobrevive 30 segundos.
- Vencer salva a pontuação no ranking dos 5 melhores.

## Controles

- Seta para cima / W: pular
- Seta para baixo / S: agachar
- Espaço / Enter: iniciar ou reiniciar

## Estrutura do projeto

- `main.py`: ponto de entrada da aplicação.
- `src/config.py`: constantes e configurações do jogo.
- `src/dino.py`: classe do dinossauro controlado pelo jogador.
- `src/obstaculo.py`: classes dos obstáculos (cactos e pássaro).
- `src/jogo.py`: loop principal e controle de estados.
- `src/dados.py`: leitura e escrita do ranking em arquivo.
- `src/funcoes.py`: funções utilitárias.
- `assets/`: imagens do jogo.
- `data/ranking.txt`: arquivo com o ranking salvo.
- `tests/`: testes unitários com pytest.
- `docs/proposta.md`: proposta inicial do jogo.

## Como executar

```bash
pip install pygame-ce pytest
python main.py
```

## Como executar os testes

```bash
python -m pytest
```

## Referências

- Assets gráficos baseados no Chrome Dino (google/dinosaur-game).