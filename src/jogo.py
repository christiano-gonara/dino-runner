import pygame

from src.config import (
    LARGURA_TELA,
    ALTURA_TELA,
    FPS,
    TITULO_JOGO,
    MAX_TENTATIVAS,
    FUNDO,
    TEXTO,
    TECLA_PADRAO,
    TAMANHO_CELULA,
    ESPACAMENTO_CELULA,
    CINZA_CELULA,
    BORDA_ATIVA,
    VERDE,
    AMARELO,
    PRETO,
    CAMINHO_FONTE,
    CAMINHO_RECORDE,
    CAMINHO_PALAVRAS_4,
    CAMINHO_PALAVRAS_5,
    CAMINHO_PALAVRAS_6,
)
from src.funcoes import sortear_palavra, verificar_tentativa, jogador_venceu
from src.dados import carregar_palavras, carregar_recorde, salvar_recorde

TECLADO_LAYOUT = [
    "qwertyuiop",
    "asdfghjkl",
    "zxcvbnm",
]
TECLA_LARGURA = 40
TECLA_ALTURA = 40
TECLA_ESPACO = 4

COR_POR_NOME = {"verde": VERDE, "amarelo": AMARELO, "cinza": CINZA_CELULA}
PRIORIDADE_COR = {"cinza": 0, "amarelo": 1, "verde": 2}


def desenhar_texto(tela, texto, tamanho, cor, x, y):
    fonte = pygame.font.Font(CAMINHO_FONTE, tamanho)
    superficie = fonte.render(texto, True, cor)
    rect = superficie.get_rect(center=(x, y))
    tela.blit(superficie, rect)
    return rect


def tela_dificuldade(tela):
    opcoes = [
        ("Fácil (4 letras)", 4, CAMINHO_PALAVRAS_4),
        ("Médio (5 letras)", 5, CAMINHO_PALAVRAS_5),
        ("Difícil (6 letras)", 6, CAMINHO_PALAVRAS_6),
    ]
    botoes = []
    espaco = 80
    inicio_y = ALTURA_TELA // 2 - (len(opcoes) * espaco) // 2

    for i, (texto, _, _) in enumerate(opcoes):
        rect = pygame.Rect(0, 0, 300, 60)
        rect.center = (LARGURA_TELA // 2, inicio_y + i * espaco)
        botoes.append(rect)

    while True:
        tela.fill(FUNDO)
        desenhar_texto(tela, "TERMO", 64, AMARELO, LARGURA_TELA // 2, 100)
        desenhar_texto(tela, "Escolha a dificuldade:", 28, TEXTO, LARGURA_TELA // 2, 170)

        mouse_pos = pygame.mouse.get_pos()

        for i, (texto, _, _) in enumerate(opcoes):
            cor = TECLA_PADRAO if not botoes[i].collidepoint(mouse_pos) else AMARELO
            pygame.draw.rect(tela, cor, botoes[i], border_radius=8)
            desenhar_texto(tela, texto, 24, TEXTO, botoes[i].centerx, botoes[i].centery)

        pygame.display.flip()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return None, None
            if evento.type == pygame.MOUSEBUTTONDOWN:
                for i, (_, qtd, caminho) in enumerate(opcoes):
                    if botoes[i].collidepoint(evento.pos):
                        return qtd, caminho


def desenhar_grade(tela, linhas, resultados, qtd_letras, linha_atual):
    largura_total = qtd_letras * TAMANHO_CELULA + (qtd_letras - 1) * ESPACAMENTO_CELULA
    inicio_x = (LARGURA_TELA - largura_total) // 2
    inicio_y = 50

    for linha in range(MAX_TENTATIVAS):
        for coluna in range(qtd_letras):
            x = inicio_x + coluna * (TAMANHO_CELULA + ESPACAMENTO_CELULA)
            y = inicio_y + linha * (TAMANHO_CELULA + ESPACAMENTO_CELULA)
            rect = pygame.Rect(x, y, TAMANHO_CELULA, TAMANHO_CELULA)
            letra = linhas[linha][coluna] if coluna < len(linhas[linha]) else ""

            if resultados[linha] is not None:
                cor = COR_POR_NOME[resultados[linha][coluna]]
                pygame.draw.rect(tela, cor, rect, border_radius=4)
            elif letra:
                pygame.draw.rect(tela, CINZA_CELULA, rect, border_radius=4)
                pygame.draw.rect(tela, BORDA_ATIVA, rect, width=2, border_radius=4)
            else:
                cor_borda = BORDA_ATIVA if linha == linha_atual else CINZA_CELULA
                pygame.draw.rect(tela, CINZA_CELULA, rect, border_radius=4)
                pygame.draw.rect(tela, cor_borda, rect, width=2, border_radius=4)

            if letra:
                desenhar_texto(tela, letra.upper(), 32, TEXTO, rect.centerx, rect.centery)


def desenhar_teclado(tela, estado_letras):
    for i_linha, linha in enumerate(TECLADO_LAYOUT):
        largura_linha = len(linha) * TECLA_LARGURA + (len(linha) - 1) * TECLA_ESPACO
        inicio_x = (LARGURA_TELA - largura_linha) // 2
        inicio_y = 460 + i_linha * (TECLA_ALTURA + TECLA_ESPACO)

        for i_coluna, letra in enumerate(linha):
            x = inicio_x + i_coluna * (TECLA_LARGURA + TECLA_ESPACO)
            rect = pygame.Rect(x, inicio_y, TECLA_LARGURA, TECLA_ALTURA)
            cor = COR_POR_NOME.get(estado_letras.get(letra), TECLA_PADRAO)
            pygame.draw.rect(tela, cor, rect, border_radius=6)
            desenhar_texto(tela, letra.upper(), 18, TEXTO, rect.centerx, rect.centery)


def atualizar_estado_letras(estado_letras, tentativa, resultado):
    for letra, cor in zip(tentativa, resultado):
        if letra not in estado_letras or PRIORIDADE_COR[cor] > PRIORIDADE_COR[estado_letras[letra]]:
            estado_letras[letra] = cor


def tela_fim(tela, venceu, palavra_secreta, tentativas_usadas, sequencia_atual, recorde_sequencia):
    tela.fill(FUNDO)

    if venceu:
        desenhar_texto(tela, "Parabéns!", 52, TEXTO, LARGURA_TELA // 2, ALTURA_TELA // 2 - 80)
        desenhar_texto(tela, f"Você acertou em {tentativas_usadas} tentativa(s)!", 24, TEXTO, LARGURA_TELA // 2, ALTURA_TELA // 2 - 30)
    else:
        desenhar_texto(tela, "Fim de jogo!", 52, TEXTO, LARGURA_TELA // 2, ALTURA_TELA // 2 - 80)
        desenhar_texto(tela, f"A palavra era:", 24, TEXTO, LARGURA_TELA // 2, ALTURA_TELA // 2 - 30)

    desenhar_texto(tela, palavra_secreta.upper(), 44, VERDE, LARGURA_TELA // 2, ALTURA_TELA // 2 + 30)
    desenhar_texto(tela, f"Sequência: {sequencia_atual}   |   Recorde: {recorde_sequencia}", 20, TEXTO, LARGURA_TELA // 2, ALTURA_TELA // 2 + 90)
    desenhar_texto(tela, "Pressione R para jogar novamente ou ESC para sair", 18, TEXTO, LARGURA_TELA // 2, ALTURA_TELA // 2 + 140)

    pygame.display.flip()

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return False
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_r:
                    return True
                if evento.key == pygame.K_ESCAPE:
                    return False


def executar_jogo():
    pygame.init()
    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption(TITULO_JOGO)
    relogio = pygame.time.Clock()

    sequencia_atual, recorde_sequencia = carregar_recorde(CAMINHO_RECORDE)
    jogando = True

    while jogando:
        qtd_letras, caminho_palavras = tela_dificuldade(tela)
        if qtd_letras is None:
            break

        palavras = carregar_palavras(caminho_palavras)
        palavra_secreta = sortear_palavra(palavras)

        linhas = ["" for _ in range(MAX_TENTATIVAS)]
        resultados = [None for _ in range(MAX_TENTATIVAS)]
        estado_letras = {}
        linha_atual = 0
        venceu = False
        rodando = True

        while rodando:
            relogio.tick(FPS)

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    rodando = False
                    jogando = False
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_RETURN:
                        if len(linhas[linha_atual]) == qtd_letras:
                            resultado = verificar_tentativa(linhas[linha_atual], palavra_secreta)
                            resultados[linha_atual] = resultado
                            atualizar_estado_letras(estado_letras, linhas[linha_atual], resultado)
                            linha_atual += 1
                            if jogador_venceu(resultado):
                                venceu = True
                                rodando = False
                            elif linha_atual >= MAX_TENTATIVAS:
                                rodando = False
                        continue
                    if evento.key == pygame.K_BACKSPACE:
                        if len(linhas[linha_atual]) > 0:
                            linhas[linha_atual] = linhas[linha_atual][:-1]
                        continue
                    if evento.unicode and evento.unicode.isalpha():
                        if len(linhas[linha_atual]) < qtd_letras:
                            linhas[linha_atual] += evento.unicode.lower()

            tela.fill(FUNDO)
            desenhar_grade(tela, linhas, resultados, qtd_letras, linha_atual)
            desenhar_teclado(tela, estado_letras)
            pygame.display.flip()

        if venceu:
            sequencia_atual += 1
            if sequencia_atual > recorde_sequencia:
                recorde_sequencia = sequencia_atual
        else:
            sequencia_atual = 0

        salvar_recorde(CAMINHO_RECORDE, sequencia_atual, recorde_sequencia)

        restart = tela_fim(tela, venceu, palavra_secreta, linha_atual, sequencia_atual, recorde_sequencia)
        if not restart:
            jogando = False

    pygame.quit()