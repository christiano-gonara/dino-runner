import random


def calcular_pontos(pontos_atual, pontos_ganhos):
    """Soma os pontos ganhos à pontuação atual."""
    return pontos_atual + pontos_ganhos


def tomar_dano(vida_atual, dano):
    """Reduz a vida atual com base no dano recebido."""
    return vida_atual - dano


def jogador_perdeu(vidas):
    """Indica se o jogador ficou sem vidas."""
    return vidas <= 0


def limitar_valor(valor, minimo, maximo):
    """Mantém um valor dentro do intervalo [minimo, maximo]."""
    if valor < minimo:
        return minimo
    if valor > maximo:
        return maximo
    return valor


def verificar_colisao(retangulo_1, retangulo_2):
    """Verifica sobreposição entre dois retângulos do Pygame."""
    return retangulo_1.colliderect(retangulo_2)


def verificar_tentativa(tentativa, palavra_secreta):
    """Retorna lista com 'verde', 'amarelo' ou 'cinza' para cada letra."""

    resultado = ["cinza"] * len(tentativa)
    contagem = {}

    for letra in palavra_secreta:
        contagem[letra] = contagem.get(letra, 0) + 1

    for i in range(len(tentativa)):
        if tentativa[i] == palavra_secreta[i]:
            resultado[i] = "verde"
            contagem[tentativa[i]] -= 1

    for i in range(len(tentativa)):
        if resultado[i] == "cinza" and tentativa[i] in contagem and contagem[tentativa[i]] > 0:
            resultado[i] = "amarelo"
            contagem[tentativa[i]] -= 1

    return resultado


def jogador_venceu(resultado):
    """Retorna True se todas as letras estão em posição correta."""
    return all(cor == "verde" for cor in resultado)


def tentativas_esgotadas(tentativas_usadas, max_tentativas):
    """Retorna True se o jogador usou todas as tentativas."""
    return tentativas_usadas >= max_tentativas


def sortear_palavra(palavras):
    """Retorna uma palavra aleatória da lista fornecida."""
    return random.choice(palavras)