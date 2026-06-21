import pygame
import random
from src.config import LARGURA, TELA, CACTO_PEQUENO, CACTO_GRANDE, PASSARO_IMG, CACTO_PEQUENO_Y, CACTO_GRANDE_Y, PASSARO_Y


class Obstaculo:
    """Base para todos os obstáculos."""

    def __init__(self, imagem, y):
        """Posiciona o obstáculo fora da tela à direita para entrar rolando.
        O rect é criado com as dimensões reais da imagem para colisão precisa.
        """
        self.imagem = imagem
        self.x = LARGURA
        self.y = y
        self.rect = pygame.Rect(self.x, self.y, self.imagem.get_width(), self.imagem.get_height())

    def atualizar(self, vel):
        """Move o obstáculo para a esquerda."""
        self.x -= vel
        self.rect.x = self.x

    def saiu(self):
        """Verifica se o obstáculo saiu da tela."""
        return self.x < -self.imagem.get_width()

    def desenhar(self):
        """Desenha o obstáculo na tela."""
        TELA.blit(self.imagem, (self.x, self.y))


class CactoPequeno(Obstaculo):
    """Cacto pequeno."""
    def __init__(self):
        imagem = random.choice(CACTO_PEQUENO)
        super().__init__(imagem, CACTO_PEQUENO_Y)


class CactoGrande(Obstaculo):
    """Cacto grande."""
    def __init__(self):
        imagem = random.choice(CACTO_GRANDE)
        super().__init__(imagem, CACTO_GRANDE_Y)


class Passaro(Obstaculo):
    """Pássaro que voa na altura média."""
    def __init__(self):
        self.index = 0
        super().__init__(PASSARO_IMG[0], PASSARO_Y)

    def desenhar(self):
        """Anima o pássaro alternando entre 2 frames."""
        self.index = (self.index + 1) % 10
        TELA.blit(PASSARO_IMG[self.index // 5], (self.x, self.y))