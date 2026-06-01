# Proposta Inicial do Jogo

## 1. Nome provisório do jogo

> morcegoide

## 2. Integrantes do grupo

- Christiano Gonçalves Araujo

## 3. Tipo de jogo

> Jogo de coleta de itens com inimigos em visão top-down.

## 4. Descrição geral do jogo

> O jogador controla um cavaleiro visto de cima que se move por uma dungeon. Gemas aparecem espalhadas pelo mapa e devem ser coletadas para aumentar a pontuação. Morcegos se movem pelo cenário e, ao tocarem o jogador, reduzem suas vidas. A partida termina quando o jogador perde todas as vidas ou quando atinge a pontuação alvo.

## 5. Objetivo do jogador

> Coletar o maior número possível de gemas antes de perder todas as vidas, sobrevivendo aos morcegos que percorrem o mapa.

## 6. Regras principais

- O jogador começa com 3 vidas.
- Cada gema coletada vale 10 pontos.
- Ao colidir com um morcego, o jogador perde 1 vida.
- Após perder uma vida, o jogador fica temporariamente invulnerável por 2 segundos.
- Novas gemas reaparecem no mapa após todas serem coletadas.
- A cada rodada concluída, a velocidade dos morcegos aumenta.
- A partida termina quando o jogador perde todas as vidas.

## 7. Condição de vitória

> O jogador vence ao atingir 100 pontos (10 gemas coletadas) antes de perder todas as vidas.

## 8. Condição de derrota ou encerramento

> O jogador perde quando suas vidas chegam a zero. Ao final é exibida a pontuação obtida e o recorde salvo.

## 9. Elementos previstos no jogo

### Jogador ou elemento principal

> Cavaleiro controlado pelas setas do teclado ou pelas teclas WASD, com animação de movimento nos quatro sentidos, representado por spritesheet.

### Obstáculos, inimigos ou desafios

> Morcegos que se movem pelo mapa. Inicialmente com movimentação aleatória; se houver tempo, com perseguição simples ao jogador.

### Itens, alvos ou objetos de interação

> Gemas espalhadas em posições aleatórias do mapa. Cada gema coletada aumenta a pontuação em 10 pontos.

### Pontuação, vidas, tempo ou progresso

> O jogador começa com 3 vidas. A pontuação é exibida na tela. O recorde é salvo em arquivo para comparação entre partidas.

## 10. Controles previstos

- Seta para cima / W: mover para cima
- Seta para baixo / S: mover para baixo
- Seta para esquerda / A: mover para esquerda
- Seta para direita / D: mover para direita
- ESC: sair do jogo

## 11. Organização inicial do código

- `main.py`: inicializa o Pygame e inicia o loop principal;
- `src/jogo.py`: contém o loop principal do jogo e controle de estados;
- `src/config.py`: constantes de configuração (tamanho da tela, cores, velocidades, FPS);
- `src/funcoes.py`: funções puras de lógica (calcular pontos, verificar derrota, limitar posição, verificar colisão);
- `src/dados.py`: funções de leitura e escrita do recorde em arquivo;
- `assets/`: sprites do jogador, gemas e morcegos;
- `data/`: arquivo de recorde (`recorde.txt`);
- `tests/test_logica.py`: testes das funções de lógica com pytest.

## 12. Estruturas de dados que poderão ser utilizadas

- **Listas**: armazenar as gemas e os morcegos ativos no mapa.
- **Dicionários**: representar cada entidade (jogador, gema, morcego) com suas propriedades (posição, velocidade, estado).
- **Tuplas**: representar posições fixas e configurações de cor (RGB).
- **Matrizes (listas de listas)**: representar o mapa da dungeon com células transitáveis e bloqueadas.

## 13. Uso previsto de arquivos

> O recorde do jogador será salvo no arquivo `data/recorde.txt`. A cada fim de partida, o jogo compara a pontuação atual com o recorde salvo e atualiza o arquivo se necessário.

## 14. Testes planejados

- `test_calcular_pontos`: verifica se a soma de pontos está correta.
- `test_jogador_perdeu_com_zero_vidas`: verifica a condição de derrota.
- `test_jogador_nao_perdeu_com_vidas`: verifica que o jogo continua com vidas restantes.
- `test_limitar_valor`: verifica que o jogador não sai dos limites da tela.
- `test_colisao`: verifica detecção de colisão entre jogador e inimigo/item.
- `test_atualizar_recorde`: verifica se o recorde é atualizado corretamente quando superado.

## 15. Principais dificuldades esperadas

- Recortar e animar corretamente os sprites do spritesheet.
- Implementar a movimentação dos morcegos de forma fluida.
- Detectar colisões de forma precisa sem falsos positivos.
- Organizar o código em módulos mantendo a clareza e a testabilidade.

## 16. Escopo mínimo para a entrega final

> A versão mínima terá: jogador controlável pelo teclado, gemas espalhadas no mapa para coleta, morcegos com movimentação simples, sistema de pontuação e vidas exibidos na tela, condição de derrota ao perder todas as vidas, tela de fim de jogo com pontuação e recorde salvo em arquivo.

## 17. Possíveis melhorias, caso haja tempo

- Tela inicial com título e instrução para começar.
- Morcegos com perseguição ao jogador.
- Aumento progressivo da dificuldade a cada rodada.
- Sons de coleta e de dano.
- Ranking com os 5 melhores resultados salvos em arquivo.
- Mapa com paredes e obstáculos usando matriz.