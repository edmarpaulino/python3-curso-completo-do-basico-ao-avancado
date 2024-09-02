#! /opt/homebrew/bin/python

from math import pi
import sys


def circulo(raio):
    area = pi * float(raio) ** 2
    return area


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('É necessário informar o raio do círculo.')
        nome_script = sys.argv[0][2:]
        print(f'Sintaxe: {nome_script} <raio>')
    else:
        raio = sys.argv[1]
        area = circulo(raio)
        print('Área do círculo', area)
