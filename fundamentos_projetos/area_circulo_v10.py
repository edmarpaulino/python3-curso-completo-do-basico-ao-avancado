#! /opt/homebrew/bin/python

from math import pi
import sys


def circulo(raio):
    area = pi * float(raio) ** 2
    return area


if __name__ == '__main__':
    raio = sys.argv[1]
    area = circulo(raio)
    print('Área do círculo', area)
