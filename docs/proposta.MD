# Proposta do Jogo — TERMO

## 1. Nome do jogo

> TERMO

## 2. Integrantes do grupo

- Christiano Gonçalves Araujo

## 3. Tipo de jogo

> Jogo de adivinhação de palavras inspirado no Wordle/Termo.

## 4. Descrição geral do jogo

> O jogador tem 6 tentativas para adivinhar uma palavra secreta. A cada tentativa, letras corretas na posição certa ficam verdes, letras corretas em posição errada ficam amarelas, e letras ausentes ficam cinza. O jogo possui 3 dificuldades: Fácil (4 letras), Médio (5 letras) e Difícil (6 letras). As palavras são sorteadas de arquivos texto. O teclado virtual mostra o estado de cada letra ao longo da partida.

## 5. Objetivo do jogador

> Adivinhar a palavra secreta no menor número de tentativas possível.

## 6. Regras principais

- Escolha uma dificuldade na tela inicial (Fácil 4, Médio 5, Difícil 6 letras).
- Digite letras e pressione ENTER para enviar a tentativa.
- Feedback visual com cores: verde (certa posição certa), amarelo (certa posição errada), cinza (ausente).
- O teclado virtual é colorido conforme o estado de cada letra.
- São 6 tentativas por partida.
- Ao vencer, o recorde de partidas vencidas é incrementado e salvo.
- Tela de fim com opção de jogar novamente (R) ou sair (ESC).

## 7. Condição de vitória

> O jogador vence ao acertar todas as letras na posição correta dentro das 6 tentativas.

## 8. Condição de derrota ou encerramento

> O jogador perde quando as 6 tentativas se esgotam sem acertar a palavra. A palavra secreta é revelada na tela de fim.

## 9. Elementos do jogo

### Tela de dificuldade

> Três botões para selecionar Fácil (4 letras), Médio (5 letras) ou Difícil (6 letras). Título "TERMO" em amarelo.

### Grade de células

> Grade 6xN desenhada com `pygame.draw.rect`, onde N varia conforme a dificuldade. Letras digitadas aparecem centralizadas nas células.

### Teclado virtual

> Layout QWERTY com 3 linhas desenhado na parte inferior da tela. Cada tecla recebe a cor correspondente ao melhor estado obtido para aquela letra (verde > amarelo > cinza).

### Recorde

> Número de partidas vencidas salvo em `data/recorde.txt`, carregado e atualizado a cada vitória.

## 10. Controles

- Teclas A-Z: digitar letras
- BACKSPACE: apagar última letra
- ENTER: confirmar tentativa
- R (tela de fim): jogar novamente
- ESC: sair

## 11. Organização do código

- `main.py`: inicializa o Pygame e chama `executar_jogo()`.
- `src/jogo.py`: loop principal, desenho da grade, teclado virtual, telas de dificuldade e fim.
- `src/config.py`: constantes de configuração (cores, tamanhos, caminhos).
- `src/funcoes.py`: funções puras de lógica (`verificar_tentativa`, `jogador_venceu`, `tentativas_esgotadas`, `sortear_palavra`).
- `src/dados.py`: funções de leitura e escrita (`carregar_recorde`, `salvar_recorde`, `carregar_palavras`).
- `data/palavras_4.txt`, `data/palavras_5.txt`, `data/palavras_6.txt`: palavras para cada dificuldade.
- `assets/fontes/Outfit-Bold.ttf`: fonte utilizada no jogo.
- `tests/test_logica.py`: testes das funções de lógica com pytest.

## 12. Estruturas de dados utilizadas

- **Listas**: armazenar linhas da grade, resultados, layouts do teclado.
- **Dicionários**: mapear estado de cada letra no teclado virtual, mapear nome da cor para RGB.
- **Tuplas**: cores RGB.
- **Arquivos texto**: palavras por dificuldade e recorde de partidas vencidas.

## 13. Uso de arquivos

> `data/palavras_N.txt` contém uma palavra por linha para cada dificuldade. `data/recorde.txt` armazena o número de partidas vencidas, atualizado a cada vitória.

## 14. Testes planejados / implementados

- `test_verificar_tentativa_acertou_tudo`: todas verdes.
- `test_verificar_tentativa_letras_trocadas`: amarelo nas posições trocadas.
- `test_verificar_tentativa_nada_acertou`: tudo cinza.
- `test_verificar_tentativa_letra_repetida`: letras repetidas contadas corretamente.
- `test_jogador_venceu`: True quando tudo verde, False caso contrário.
- `test_tentativas_esgotadas`: True quando atinge o limite.
- `test_sortear_palavra`: retorna uma palavra válida da lista.

## 15. Principais dificuldades encontradas

- Implementar a lógica de letras repetidas no `verificar_tentativa`.
- Posicionar corretamente a grade e o teclado dentro da tela de 800x600.
- Gerenciar o estado do teclado virtual com prioridade de cores.

## 16. Escopo entregue

> Versão completa com: tela de seleção de dificuldade, grade de células, entrada de teclado, feedback visual (verde/amarelo/cinza), teclado virtual colorido, tela de fim com vitória/derrota, recorde salvo em arquivo, e opção de jogar novamente.

## 17. Possíveis melhorias futuras

- Animações nas células ao revelar as cores.
- Efeitos sonoros.
- Estatísticas por dificuldade.
- Dicionário para validar se a palavra digitada existe.
- Tema claro/escuro.