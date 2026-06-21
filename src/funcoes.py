import pygame
from src.config import TELA


def desenhar_texto(texto, tamanho, cor, x, y):
    """Desenha texto centralizado na tela."""
    fonte = pygame.font.Font(None, tamanho)
    imagem = fonte.render(texto, True, cor)
    retangulo = imagem.get_rect(center=(x, y))
    TELA.blit(imagem, retangulo)


def formatar_tempo(segundos):
    """Formata segundos para MM:SS."""
    minutos = int(segundos // 60)
    segs = int(segundos % 60)
    return f"{minutos:02d}:{segs:02d}"