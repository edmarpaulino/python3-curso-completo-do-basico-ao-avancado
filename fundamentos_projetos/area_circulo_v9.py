#! /opt/homebrew/bin/python

from math import pi


def circulo(raio):
    area = pi * float(raio) ** 2
    return area


if __name__ == '__main__':
    raio = input('Informe o raio: ')
    area = circulo(raio)
    print('Área do círculo', area)
