import pygame
import sys
import random
from src.config import (
    LARGURA, ALTURA, FPS, TELA,
    BRANCO, PRETO, VERMELHO, VERDE,
    VIDAS_MAX, TEMPO_LIMITE,
    TECLA_INICIAR,
    VEL_JOGO, TRILHA_Y, TRILHA, NUVEM,
    PONTOS_POR_FRAME, AUMENTO_VEL, INCREMENTO_VEL
)
from src.dados import salvar_ranking, ler_ranking
from src.funcoes import desenhar_texto, formatar_tempo
from src.dino import Dino
from src.obstaculo import CactoPequeno, CactoGrande, Passaro


class Nuvem:
    def __init__(self):
        """Inicializa fora da tela à direita."""
        self.x = LARGURA + random.randint(800, 1000)
        self.y = random.randint(50, 100)
        self.largura = NUVEM.get_width()

    def atualizar(self, vel):
        """Move e recicla ao sair pela esquerda."""
        self.x -= vel
        if self.x < -self.largura:
            self.x = LARGURA + random.randint(2500, 3000)
            self.y = random.randint(50, 100)

    def desenhar(self):
        TELA.blit(NUVEM, (self.x, self.y))


class Jogo:
    """Controla o loop principal do jogo"""

    def __init__(self):
        self.clock = pygame.time.Clock()
        self.ranking = ler_ranking()
        self.estado = "menu"
        self._inicializar_partida()

    def _inicializar_partida(self):
        """Zera contadores e recria os objetos da partida."""
        self.dino = Dino()
        self.obstaculos = []
        self.nuvem = Nuvem()
        self.pontos = 0
        self.frame = 0
        self.vidas = VIDAS_MAX
        self.tempo = TEMPO_LIMITE
        self.vel_jogo = VEL_JOGO
        self.x_bg = 0
        self.ultimo_tempo = pygame.time.get_ticks()

    def reiniciar(self):
        self._inicializar_partida()

    def gerar_obstaculo(self):
        """Gera um obstáculo quando a lista está vazia."""
        if len(self.obstaculos) == 0:
            if random.randint(0, 2) == 0:
                self.obstaculos.append(CactoPequeno())
            elif random.randint(0, 2) == 1:
                self.obstaculos.append(CactoGrande())
            elif random.randint(0, 2) == 2:
                self.obstaculos.append(Passaro())


    def atualizar(self):
        """Atualiza toda a lógica do jogo"""
        if self.estado != "jogando":
            return

        # timer
        agora = pygame.time.get_ticks()
        self.tempo -= (agora - self.ultimo_tempo) / 1000
        self.ultimo_tempo = agora

        if self.tempo <= 0:
            self.tempo = 0
            self.estado = "vitoria"
            salvar_ranking(self.pontos)
            self.ranking = ler_ranking()
            return

        # pontos e velocidade
        self.frame += 1
        if self.frame % PONTOS_POR_FRAME == 0:
            self.pontos += 1
            if self.pontos % AUMENTO_VEL == 0:
                self.vel_jogo += INCREMENTO_VEL

        # input
        teclas = pygame.key.get_pressed()
        self.dino.atualizar(teclas)

        # obstáculos
        self.gerar_obstaculo()
        for obs in self.obstaculos[:]:
            obs.atualizar(self.vel_jogo)
            if obs.saiu():
                self.obstaculos.remove(obs)

        # colisões
        for obs in self.obstaculos[:]:
            if self.dino.rect.colliderect(obs.rect) and not self.dino.invulneravel:
                self.vidas -= 1
                self.dino.ativar_invulnerabilidade()
                self.obstaculos.remove(obs)
                if self.vidas <= 0:
                    self.estado = "gameover"
                    salvar_ranking(self.pontos)
                    self.ranking = ler_ranking()
                break

        # nuvem
        self.nuvem.atualizar(self.vel_jogo)

        # fundo rolante
        self.x_bg -= self.vel_jogo
        if self.x_bg <= -TRILHA.get_width():
            self.x_bg = 0


    def desenhar(self):
        """Desenha tudo na tela."""
        TELA.fill(BRANCO)

        if self.estado == "menu":
            self._desenhar_menu()
        elif self.estado == "jogando":
            self._desenhar_jogo()
        elif self.estado == "gameover":
            self._desenhar_gameover()
        elif self.estado == "vitoria":
            self._desenhar_vitoria()


    def _desenhar_jogo(self):
        """Desenha fundo, nuvem, dino, obstáculos e HUD"""
        largura_trilha = TRILHA.get_width()
        TELA.blit(TRILHA, (self.x_bg, TRILHA_Y))
        TELA.blit(TRILHA, (self.x_bg + largura_trilha, TRILHA_Y))

        self.nuvem.desenhar()
        self.dino.desenhar()
        for obs in self.obstaculos:
            obs.desenhar()

        desenhar_texto(f"Pontos: {self.pontos}", 20, PRETO, 900, 30)
        desenhar_texto(f"Tempo: {formatar_tempo(max(0, self.tempo))}", 20, VERMELHO, 100, 30)
        desenhar_texto(f"Vidas: {self.vidas}", 20, VERMELHO, 500, 30)


    def _desenhar_menu(self):
        """Desenha a tela de menu com ranking"""
        desenhar_texto("DINO RUNNER", 50, PRETO, LARGURA // 2, 120)
        desenhar_texto("Sobreviva 30 segundos!", 20, PRETO, LARGURA // 2, 170)
        desenhar_texto("Pressione ESPACO para comecar", 20, PRETO, LARGURA // 2, 200)
        desenhar_texto("Seta para cima para pular | Seta para baixo para agachar", 16, PRETO, LARGURA // 2, 230)

        if self.ranking:
            desenhar_texto("MELHORES PONTOS:", 18, PRETO, LARGURA // 2, 280)
            for i, pontos in enumerate(self.ranking[:5]):
                desenhar_texto(f"{i+1}. {pontos}", 16, PRETO, LARGURA // 2, 305 + i * 22)


    def _desenhar_gameover(self):
        """Desenha a tela de game over"""
        desenhar_texto("GAME OVER", 50, VERMELHO, LARGURA // 2, ALTURA // 2 - 40)
        desenhar_texto(f"Pontos: {self.pontos}", 25, PRETO, LARGURA // 2, ALTURA // 2 + 20)
        desenhar_texto("Pressione ESPACO para recomecar", 20, PRETO, LARGURA // 2, ALTURA // 2 + 60)


    def _desenhar_vitoria(self):
        """Desenha a tela de vitória com ranking"""
        desenhar_texto("VOCE VENCEU!", 50, VERDE, LARGURA // 2, ALTURA // 2 - 60)
        desenhar_texto(f"Pontos: {self.pontos}", 25, PRETO, LARGURA // 2, ALTURA // 2)

        if self.ranking:
            desenhar_texto("MELHORES PONTOS:", 18, PRETO, LARGURA // 2, ALTURA // 2 + 50)
            for i, pontos in enumerate(self.ranking[:5]):
                desenhar_texto(f"{i+1}. {pontos}", 16, PRETO, LARGURA // 2, ALTURA // 2 + 75 + i * 22)

        desenhar_texto("Pressione ESPACO para recomecar", 20, PRETO, LARGURA // 2, ALTURA // 2 + 190)


    def eventos(self):
        """Processa eventos do pygame"""
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return False

            if evento.type == pygame.KEYDOWN:
                if evento.key in TECLA_INICIAR:
                    if self.estado in ["menu", "gameover", "vitoria"]:
                        self.estado = "jogando"
                        self.reiniciar()

        return True


    def rodar(self):
        """Loop principal do jogo"""
        rodando = True

        while rodando:
            rodando = self.eventos()
            self.atualizar()
            self.desenhar()
            pygame.display.flip()
            self.clock.tick(FPS)

        pygame.quit()
        sys.exit()


def main():
    """Inicia o jogo"""
    jogo = Jogo()
    jogo.rodar()
