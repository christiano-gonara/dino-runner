# Proposta Inicial do Jogo

## 1. Nome provisório do jogo

> Dino Runner

## 2. Integrantes do grupo

- Christiano Gonçalves Araujo

## 3. Tipo de jogo

> Jogo de desviar de obstáculos com corrida infinita.

## 4. Descrição geral do jogo

> O jogador controla um dinossauro visto de lado que corre automaticamente. Obstáculos surgem da direita (cactos e pássaros) e o jogador deve pular ou agachar para desviá-los. O objetivo é sobreviver por 30 segundos. A velocidade aumenta com o tempo, tornando o jogo progressivamente mais difícil.

## 5. Objetivo do jogador

> Sobreviver por 30 segundos desviando de todos os obstáculos sem perder as 3 vidas.

## 6. Regras principais

- O jogador começa com 3 vidas.
- Colidir com obstáculo remove 1 vida.
- Após tomar dano, o dino fica invulnerável por 2 segundos.
- A velocidade aumenta a cada 10 pontos.
- Sobreviver 30 segundos = vitória.
- Perder todas as vidas = derrota.

## 7. Condição de vitória

> Sobreviver por 30 segundos sem perder todas as vidas.

## 8. Condição de derrota ou encerramento

> Perder todas as 3 vidas antes de completar os 30 segundos.

## 9. Elementos previstos no jogo

### Jogador ou elemento principal

> Dinossauro controlado pelas setas do teclado ou WASD, com animações de corrida, pulo e agachamento.

### Obstáculos, inimigos ou desafios

> Cactos pequenos, cactos grandes e pássaros surgindo aleatoriamente da direita.

### Itens, alvos ou objetos de interação

> Não há itens coletáveis — a pontuação aumenta automaticamente com o tempo.

### Pontuação, vidas, tempo ou progresso

> 3 vidas, pontuação por tempo sobrevivido, timer de 30 segundos exibido na tela.

## 10. Controles previstos

- Seta para cima / W: pular
- Seta para baixo / S: agachar
- Espaço / Enter: iniciar ou reiniciar

## 11. Organização inicial do código

- `main.py`: ponto de entrada
- `src/config.py`: constantes configuráveis
- `src/dino.py`: classe Dino
- `src/obstaculo.py`: classes Obstaculo, CactoPequeno, CactoGrande, Passaro
- `src/jogo.py`: classe Jogo com loop principal
- `src/dados.py`: funções de ranking em arquivo
- `src/funcoes.py`: funções utilitárias

## 12. Estruturas de dados que poderão ser utilizadas

- Listas para armazenar obstáculos ativos e imagens dos sprites.
- Dicionário implícito no estado do jogo (strings de estado).

## 13. Uso previsto de arquivos

> Ranking salvo em `data/ranking.txt` com os 5 melhores pontos.

## 14. Testes planejados

- Testes de salvar e carregar ranking.
- Testes de formatação de tempo.
- Testes de inicialização e comportamento do Dino.
- Testes de movimento e saída dos obstáculos.

## 15. Principais dificuldades esperadas

- Alinhamento dos sprites com o chão.
- Física do pulo.
- Detecção de colisão precisa.

## 16. Escopo mínimo para a entrega final

> Dinossauro controlável, cactos como obstáculos, sistema de 3 vidas, timer de 30 segundos, tela de vitória e derrota, ranking salvo em arquivo, testes com pytest.


## 17. Possíveis melhorias, caso haja tempo

- Sons de pulo e colisão.
- Animação de morte do dinossauro ao perder vida.
- Tela inicial com dinossauro decorativo.
- Dificuldades selecionáveis (fácil, médio, difícil).