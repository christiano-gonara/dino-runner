from src.obstaculo import CactoPequeno
from src.config import LARGURA


def test_cacto_pequeno_comeca_em_largura():
    # obstáculo deve surgir na borda direita da tela
    cacto = CactoPequeno()
    assert cacto.x == LARGURA


def test_saiu_retorna_false_quando_visivel():
    # cacto ainda visível na tela não deve ser marcado como saído
    cacto = CactoPequeno()
    cacto.x = 100
    cacto.rect.x = 100
    assert cacto.saiu() is False


def test_saiu_retorna_true_quando_fora():
    # cacto que passou da borda esquerda deve ser marcado como saído
    cacto = CactoPequeno()
    cacto.x = -100
    cacto.rect.x = -100
    assert cacto.saiu() is True


def test_atualizar_move_obstaculo_para_esquerda():
    # após atualizar, a posição x deve ter diminuído pela velocidade passada
    cacto = CactoPequeno()
    x_antes = cacto.x
    velocidade = 10

    cacto.atualizar(velocidade)

    assert cacto.x == x_antes - velocidade
    assert cacto.rect.x == cacto.x
