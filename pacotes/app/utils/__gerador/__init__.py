from random import randint


def novo_nome():
    nomes = ['pedro', 'carla', 'ana', 'joão', 'rebeca']
    escolhido = randint(0, len(nomes) - 1)
    return nomes[escolhido]
