# Tarefas - Termo

## Tarefa 1 — Lógica pura
- [x] Implementar `verificar_tentativa(tentativa, palavra_secreta)` → lista com "verde", "amarelo" ou "cinza" pra cada letra
- [x] Implementar `jogador_venceu(resultado)` → bool
- [x] Implementar `tentativas_esgotadas(tentativas_usadas, max_tentativas)` → bool
- [x] Testes em `tests/test_logica.py` cobrindo as funções acima

## Tarefa 2 — Palavras e dificuldade
- [x] Criar `data/palavras_4.txt`, `data/palavras_5.txt`, `data/palavras_6.txt`
- [x] Implementar função pra sortear palavra aleatória do arquivo conforme dificuldade
- [x] Tela de seleção de dificuldade (Fácil 4 letras / Médio 5 letras / Difícil 6 letras)

## Tarefa 3 — Grade e entrada do jogador
- [x] Capturar entrada do teclado letra por letra
- [x] Desenhar grade de células (6 linhas x N colunas) com `pygame.draw.rect`
- [x] Exibir letras digitadas nas células

## Tarefa 4 — Cores e feedback visual
- [x] Aplicar cores nas células conforme resultado (verde/amarelo/cinza)
- [x] Desenhar teclado virtual na tela com estado de cada letra colorida

## Tarefa 5 — Fim de jogo e recorde
- [x] Condição de vitória com tela de fim de jogo
- [x] Condição de derrota com tela de fim de jogo e revelação da palavra
- [x] Recorde salvo em `data/recorde.txt` (partidas vencidas)

## Tarefa 6 — Finalização
- [x] README atualizado com regras e controles
- [x] Atualizar `docs/proposta.MD` com nova proposta
- [x] Todos os testes passando com `pytest`