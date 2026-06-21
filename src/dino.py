import pygame
from src.config import DINO_RUN, DINO_JUMP, DINO_DUCK, TELA, VEL_PULO, CHAO_Y, CHAO_Y_AGACHADO, TECLA_PULAR, TECLA_ABAIXAR, TEMPO_INVULNERAVEL

X_POS = 80


class Dino:

    def __init__(self):
        self.agachando = False
        self.correndo = True
        self.pulando = False

        self.step_index = 0
        self.vel_pulo = VEL_PULO
        self.invulneravel = False
        self.tempo_invulneravel = 0
        self.image = DINO_RUN[0]
        self.rect = self.image.get_rect()
        self.rect.x = X_POS
        self.rect.y = CHAO_Y

    def ativar_invulnerabilidade(self):
        self.invulneravel = True
        self.tempo_invulneravel = pygame.time.get_ticks()

    def atualizar(self, teclas):
        # verifica se o tempo de invulnerabilidade expirou
        if self.invulneravel:
            if pygame.time.get_ticks() - self.tempo_invulneravel >= TEMPO_INVULNERAVEL:
                self.invulneravel = False

        # Executa o estado atual ANTES de ler novo input (igual ao original)
        if self.agachando:
            self._agachar()
        if self.correndo:
            self._correr()
        if self.pulando:
            self._pular()

        if self.step_index >= 10:
            self.step_index = 0

        if any(teclas[k] for k in TECLA_PULAR) and not self.pulando:
            self.agachando = False
            self.correndo = False
            self.pulando = True
        elif any(teclas[k] for k in TECLA_ABAIXAR) and not self.pulando:
            self.agachando = True
            self.correndo = False
            self.pulando = False
        elif not (self.pulando or any(teclas[k] for k in TECLA_ABAIXAR)):
            self.agachando = False
            self.correndo = True
            self.pulando = False

    def _agachar(self):
        self.image = DINO_DUCK[self.step_index // 5]
        self.rect = self.image.get_rect()
        self.rect.x = X_POS
        self.rect.y = CHAO_Y_AGACHADO
        self.step_index += 1

    def _correr(self):
        self.image = DINO_RUN[self.step_index // 5]
        self.rect = self.image.get_rect()
        self.rect.x = X_POS
        self.rect.y = CHAO_Y
        self.step_index += 1

    def _pular(self):
        self.image = DINO_JUMP
        if self.pulando:
            self.rect.y -= self.vel_pulo * 4
            self.vel_pulo -= 0.8
        if self.vel_pulo < -VEL_PULO:
            self.pulando = False
            self.vel_pulo = VEL_PULO

    def desenhar(self):
        # quando invulnerável, pisca alternando visibilidade a cada 5 frames
        if self.invulneravel and (self.step_index // 5) % 2 == 1:
            return
        TELA.blit(self.image, (self.rect.x, self.rect.y))
