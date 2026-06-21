import pytest
from src.dino import Dino
from src.config import CHAO_Y, VEL_PULO, TECLA_PULAR, TECLA_ABAIXAR


class TeclasMock:
    """Simula o objeto retornado por pygame.key.get_pressed()."""

    def __init__(self, pressionadas=None):
        # pressionadas: lista de constantes pygame.K_* consideradas ativas
        self._pressionadas = pressionadas or []

    def __getitem__(self, key):
        return key in self._pressionadas


teclas_neutras = TeclasMock()  # nenhuma tecla pressionada


def test_dino_inicializa_sem_pular():
    # dino deve começar parado, não pulando
    dino = Dino()
    assert dino.pulando is False


def test_dino_inicializa_sem_invulnerabilidade():
    # dino deve começar vulnerável
    dino = Dino()
    assert dino.invulneravel is False


def test_dino_inicializa_em_chao_y():
    # posição vertical inicial deve ser CHAO_Y
    dino = Dino()
    assert dino.rect.y == CHAO_Y


def test_pulo_nao_funciona_quando_ja_pulando():
    # pressionar pular enquanto já está pulando não deve reiniciar o pulo
    dino = Dino()
    dino.pulando = True
    dino.correndo = False
    dino.vel_pulo = 3.0  # simula meio do pulo (já abaixo de VEL_PULO)

    teclas = TeclasMock(TECLA_PULAR)
    dino.atualizar(teclas)

    # vel_pulo deve ter diminuído pela física, não resetado para VEL_PULO (8.5)
    assert dino.vel_pulo != VEL_PULO
    assert dino.vel_pulo == pytest.approx(3.0 - 0.8)


def test_invulnerabilidade_ativa_ao_chamar_metodo():
    # após ativar_invulnerabilidade(), dino deve estar invulnerável
    dino = Dino()
    assert dino.invulneravel is False

    dino.ativar_invulnerabilidade()

    assert dino.invulneravel is True
