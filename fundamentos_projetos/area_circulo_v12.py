#! /opt/homebrew/bin/python

from math import pi
import sys


def circulo(raio):
    area = pi * float(raio) ** 2
    return area


def help():
    nome_script = sys.argv[0][2:]
    print('É necessário informar o raio do círculo.')
    print(f'Sintaxe: {nome_script} <raio>')


if __name__ == '__main__':
    if len(sys.argv) < 2:
        help()
    else:
        raio = sys.argv[1]
        area = circulo(raio)
        print('Área do círculo', area)
