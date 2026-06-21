from src.funcoes import formatar_tempo


def test_formatar_tempo_com_minuto_e_segundos():
    # 65 segundos = 1 minuto e 5 segundos
    assert formatar_tempo(65) == "01:05"


def test_formatar_tempo_trinta_segundos():
    # 30 segundos sem minutos completos
    assert formatar_tempo(30) == "00:30"


def test_formatar_tempo_zero():
    # zero segundos deve retornar string zerada
    assert formatar_tempo(0) == "00:00"


def test_formatar_tempo_dois_minutos_e_cinco_segundos():
    # 125 segundos = 2 minutos e 5 segundos
    assert formatar_tempo(125) == "02:05"
