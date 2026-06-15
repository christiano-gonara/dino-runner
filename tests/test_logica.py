from src.funcoes import (
    calcular_pontos,
    jogador_perdeu,
    limitar_valor,
    verificar_tentativa,
    jogador_venceu,
    tentativas_esgotadas,
    sortear_palavra,
)


def test_calcular_pontos():
    """Deve somar corretamente os pontos atuais com os pontos ganhos."""
    assert calcular_pontos(10, 5) == 15


def test_jogador_perdeu_com_zero_vidas():
    """Deve indicar derrota quando o total de vidas chega a zero."""
    assert jogador_perdeu(0) is True


def test_jogador_nao_perdeu_com_vidas():
    """Nao deve indicar derrota quando o jogador ainda tem vidas."""
    assert jogador_perdeu(3) is False


def test_limitar_valor_abaixo_do_minimo():
    """Deve retornar o limite minimo quando o valor informado for menor."""
    assert limitar_valor(-5, 0, 100) == 0


def test_limitar_valor_acima_do_maximo():
    """Deve retornar o limite maximo quando o valor informado for maior."""
    assert limitar_valor(150, 0, 100) == 100


def test_limitar_valor_dentro_do_intervalo():
    """Deve manter o valor original quando ele ja estiver no intervalo."""
    assert limitar_valor(50, 0, 100) == 50


def test_verificar_tentativa_acertou_tudo():
    resultado = verificar_tentativa("casa", "casa")
    assert resultado == ["verde", "verde", "verde", "verde"]


def test_verificar_tentativa_letras_trocadas():
    resultado = verificar_tentativa("saca", "casa")
    assert resultado == ["amarelo", "verde", "amarelo", "verde"]


def test_verificar_tentativa_nada_acertou():
    resultado = verificar_tentativa("xxxx", "casa")
    assert resultado == ["cinza", "cinza", "cinza", "cinza"]


def test_verificar_tentativa_letra_repetida_uma_so():
    resultado = verificar_tentativa("ccxz", "casa")
    assert resultado == ["verde", "cinza", "cinza", "cinza"]


def test_verificar_tentativa_letra_repetida_demais():
    resultado = verificar_tentativa("cccc", "casa")
    assert resultado == ["verde", "cinza", "cinza", "cinza"]


def test_jogador_venceu_tudo_verde():
    assert jogador_venceu(["verde", "verde", "verde", "verde"]) is True


def test_jogador_venceu_com_amarelo():
    assert jogador_venceu(["verde", "amarelo", "verde", "verde"]) is False


def test_jogador_venceu_tudo_cinza():
    assert jogador_venceu(["cinza", "cinza", "cinza", "cinza"]) is False


def test_tentativas_esgotadas_atingiu_maximo():
    assert tentativas_esgotadas(6, 6) is True


def test_tentativas_esgotadas_abaixo():
    assert tentativas_esgotadas(3, 6) is False


def test_tentativas_esgotadas_zero():
    assert tentativas_esgotadas(0, 6) is False


def test_sortear_palavra_retorna_da_lista():
    palavras = ["casa", "bola", "dado"]
    sorteada = sortear_palavra(palavras)
    assert sorteada in palavras