#! /opt/homebrew/bin/python

from math import floor
from sys import argv


def nota_para_conceito_melhorada(nota):
    nota = float(nota)
    if nota < 0 or nota > 10:
        return 'Nota inválida'
    conceitos = ['E-', 'E', 'D-', 'D', 'C-', 'C', 'B-', 'B', 'A-', 'A']
    normalizador_conceito = 0.1
    nota_normalizada = nota - normalizador_conceito if nota >= 0.1 else nota
    index = len(conceitos) - 1 if nota >= 9.1 else floor(nota_normalizada)
    return conceitos[index]


def nota_para_conceito(nota):
    nota = float(nota)
    if nota > 10:
        return 'Nota inválida'
    elif nota >= 9.1:
        return 'A'
    elif nota >= 8.1:
        return 'A-'
    elif nota >= 7.1:
        return 'B'
    elif nota >= 6.1:
        return 'B-'
    elif nota >= 5.1:
        return 'C'
    elif nota >= 4.1:
        return 'C-'
    elif nota >= 3.1:
        return 'D'
    elif nota >= 2.1:
        return 'D-'
    elif nota >= 1.1:
        return 'E'
    elif nota >= 0:
        return 'E-'
    else:
        return 'Nota inválida'


def __teste__():
    notas = [10, 9.5, 9, 8.3, 8, 7.1, 7, 6.9, 6, 5.2,
             5, 4.8, 4, 3.7, 3, 2.4, 2, 1.6, 1, 0.9, 0]
    tem_erro = False
    for nota in notas:
        if nota_para_conceito(nota) != nota_para_conceito_melhorada(nota):
            tem_erro = True
            print(f'normal: {nota} = {nota_para_conceito(nota)}')
            print(f'melhorada: {nota} = {nota_para_conceito_melhorada(nota)}')
            print()
    if tem_erro:
        print('FAIL')
    else:
        print('SUCCESS')


if __name__ == '__main__':
    if len(argv) > 1 and argv[1].lower() == 'teste':
        __teste__()
    elif len(argv) > 1 and argv[1].lower() == 'melhorada':
        valor_informado = input('Nota do aluno: ')
        conceito = nota_para_conceito_melhorada(valor_informado)
        print(conceito)
    else:
        valor_informado = input('Nota do aluno: ')
        conceito = nota_para_conceito(valor_informado)
        print(conceito)
