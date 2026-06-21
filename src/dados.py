import os
from src.config import DADOS_DIR, RANKING_FILE


def salvar_ranking(pontos):
    #Salva os 5 maiores pontos.
    os.makedirs(DADOS_DIR, exist_ok=True)

    ranking = ler_ranking()
    ranking.append(int(pontos))
    ranking.sort(reverse=True)
    ranking = ranking[:5]

    with open(RANKING_FILE, 'w') as arquivo:
        for p in ranking:
            arquivo.write(f"{p}\n")


def ler_ranking():
    #Lê o ranking do arquivo
    if not os.path.exists(RANKING_FILE):
        return []

    with open(RANKING_FILE, 'r') as arquivo:
        return [int(float(linha.strip())) for linha in arquivo if linha.strip()]
