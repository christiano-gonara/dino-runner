import pytest
from src.dados import salvar_ranking, ler_ranking


def test_salvar_e_carregar_ranking(tmp_path, monkeypatch):
    # salva pontos e verifica que são lidos corretamente
    arquivo = tmp_path / "ranking.txt"
    monkeypatch.setattr("src.dados.RANKING_FILE", str(arquivo))
    monkeypatch.setattr("src.dados.DADOS_DIR", str(tmp_path))

    salvar_ranking(500)
    resultado = ler_ranking()

    assert resultado == [500]


def test_ranking_mantem_cinco_maiores(tmp_path, monkeypatch):
    # com 6 pontuações salvas, apenas as 5 maiores devem ser mantidas
    arquivo = tmp_path / "ranking.txt"
    monkeypatch.setattr("src.dados.RANKING_FILE", str(arquivo))
    monkeypatch.setattr("src.dados.DADOS_DIR", str(tmp_path))

    for pontos in [100, 200, 300, 400, 500, 600]:
        salvar_ranking(pontos)

    resultado = ler_ranking()

    assert len(resultado) == 5
    assert resultado == [600, 500, 400, 300, 200]  # ordenado decrescente, menor excluído


def test_ler_ranking_retorna_vazio_se_arquivo_nao_existe(tmp_path, monkeypatch):
    # arquivo inexistente deve retornar lista vazia, sem erro
    monkeypatch.setattr("src.dados.RANKING_FILE", str(tmp_path / "nao_existe.txt"))

    resultado = ler_ranking()

    assert resultado == []
