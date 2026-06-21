import pygame
import os

# Controles
TECLA_PULAR = [pygame.K_UP, pygame.K_w]
TECLA_ABAIXAR = [pygame.K_DOWN, pygame.K_s]
TECLA_INICIAR = [pygame.K_SPACE, pygame.K_RETURN]

# Jogo
VIDAS_MAX = 3
TEMPO_LIMITE = 30

VEL_PULO = 8.5    # velocidade inicial do pulo (maior = mais alto)
GRAVIDADE = 0.8     # desaceleração do pulo (maior = cai mais rápido)
VEL_JOGO = 25     #velocidade inicial dos obstáculos
PONTOS_POR_FRAME = 5      # conta 1 ponto a cada X frames
AUMENTO_VEL = 10         # aumenta velocidade a cada X pontos
INCREMENTO_VEL = 3       # quanto a velocidade aumenta por vez
TEMPO_INVULNERAVEL = 2000 # duração da invulnerabilidade após dano (ms)

# Tela
LARGURA = 1100
ALTURA = 600
FPS = 30

TRILHA_Y = 380      # posição Y da trilha na tela
CHAO_Y = TRILHA_Y - 70      # posição Y do dino (altura da imagem = 70)
CHAO_Y_AGACHADO = TRILHA_Y -    45 # posição Y do dino agachado (altura = 45)
DINO_X = 80        # posição horizontal fixa do dinossauro
PASSARO_Y = 250    # altura que o pássaro voa





# Cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERMELHO = (255, 0, 0)
VERDE = (0, 255, 0)


# Caminhos
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSETS_DIR = os.path.join(BASE_DIR, "assets")
DADOS_DIR = os.path.join(BASE_DIR, "data")
RANKING_FILE = os.path.join(DADOS_DIR, "ranking.txt")


# Inicializar pygame
pygame.init()
TELA = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Dino Runner - Sobreviva 30s!")



# Carregar imagens
DINO_RUN = [
    pygame.image.load(os.path.join(ASSETS_DIR, "Dino", "DinoRun1.png")),
    pygame.image.load(os.path.join(ASSETS_DIR, "Dino", "DinoRun2.png"))
]
DINO_JUMP = pygame.image.load(os.path.join(ASSETS_DIR, "Dino", "DinoJump.png"))
DINO_DUCK = [
    pygame.image.load(os.path.join(ASSETS_DIR, "Dino", "DinoDuck1.png")),
    pygame.image.load(os.path.join(ASSETS_DIR, "Dino", "DinoDuck2.png"))
]
DINO_DEAD = pygame.image.load(os.path.join(ASSETS_DIR, "Dino", "DinoDead.png"))
CACTO_PEQUENO = [
    pygame.image.load(os.path.join(ASSETS_DIR, "Cactus", "SmallCactus1.png")),
    pygame.image.load(os.path.join(ASSETS_DIR, "Cactus", "SmallCactus2.png")),
    pygame.image.load(os.path.join(ASSETS_DIR, "Cactus", "SmallCactus3.png"))
]
CACTO_GRANDE = [
    pygame.image.load(os.path.join(ASSETS_DIR, "Cactus", "LargeCactus1.png")),
    pygame.image.load(os.path.join(ASSETS_DIR, "Cactus", "LargeCactus2.png")),
    pygame.image.load(os.path.join(ASSETS_DIR, "Cactus", "LargeCactus3.png"))
]


# Y calculado do tamanho real da imagem para alinhar a base com TRILHA_Y
CACTO_PEQUENO_Y = TRILHA_Y - CACTO_PEQUENO[0].get_height()
CACTO_GRANDE_Y = TRILHA_Y - CACTO_GRANDE[0].get_height()

PASSARO_IMG = [
    pygame.image.load(os.path.join(ASSETS_DIR, "Bird", "Bird1.png")),
    pygame.image.load(os.path.join(ASSETS_DIR, "Bird", "Bird2.png"))
]
NUVEM = pygame.image.load(os.path.join(ASSETS_DIR, "Other", "Cloud.png"))
TRILHA = pygame.image.load(os.path.join(ASSETS_DIR, "Other", "Track.png"))



# Redimensionar
DINO_RUN = [pygame.transform.scale(img, (60, 70)) for img in DINO_RUN]
DINO_JUMP = pygame.transform.scale(DINO_JUMP, (60, 70))
DINO_DUCK = [pygame.transform.scale(img, (80, 45)) for img in DINO_DUCK]
DINO_DEAD = pygame.transform.scale(DINO_DEAD, (60, 70))