import pygame


def pegar_sprite(local_arquivo, x, y, width, height, scale=1, tolerancia=15):
    """Corta um sprite da spritesheet e remove o fundo com tolerância de cor."""

    sheet = pygame.image.load(local_arquivo).convert()

    image = pygame.Surface((width, height), pygame.SRCALPHA)
    image.blit(sheet, (0, 0), (x, y, width, height))

    cor_fundo = image.get_at((0, 0))

    for py in range(height):
        for px in range(width):
            cor = image.get_at((px, py))
            if (abs(cor[0] - cor_fundo[0]) <= tolerancia and
                abs(cor[1] - cor_fundo[1]) <= tolerancia and
                abs(cor[2] - cor_fundo[2]) <= tolerancia):
                image.set_at((px, py), (0, 0, 0, 0))

    if scale != 1:
        novo_largura = int(width * scale)
        novo_altura = int(height * scale)
        image = pygame.transform.scale(image, (novo_largura, novo_altura))

    return image