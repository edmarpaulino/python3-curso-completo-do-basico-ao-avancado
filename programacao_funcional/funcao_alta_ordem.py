#! /usr/local/bin/python3

from funcao_primeira_classe import dobro, quadrado


# High Order Function
# é quando uma função pode receber outras funções como parâmetro
# e retornar funções
def processar(titulo, lista, funcao):
    print(f'Processando: {titulo}')
    for i in lista:
        print(i, '=>', funcao(i))


if __name__ == '__main__':
    processar('Dobros de 1 a 10', range(1, 11), dobro)
    processar('Quadrados de 1 a 10', range(1, 11), quadrado)
