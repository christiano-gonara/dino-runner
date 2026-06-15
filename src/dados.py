def salvar_recorde(caminho_arquivo, sequencia_atual, recorde_sequencia):
    """Salva a sequência atual e o recorde de sequência em arquivo texto."""
    with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
        arquivo.write(f"{sequencia_atual}\n{recorde_sequencia}")


def carregar_recorde(caminho_arquivo):
    """Carrega (sequencia_atual, recorde_sequencia); retorna (0, 0) se não existir."""
    try:
        with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
            linhas = arquivo.read().strip().splitlines()
            sequencia = int(linhas[0]) if len(linhas) > 0 else 0
            recorde = int(linhas[1]) if len(linhas) > 1 else 0
            return sequencia, recorde
    except (FileNotFoundError, ValueError):
        return 0, 0


def carregar_palavras(caminho_arquivo):
    """Carrega lista de palavras de um arquivo (uma por linha)."""
    with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
        return [linha.strip().lower() for linha in arquivo if linha.strip()]