#! /opt/homebrew/bin/python

from math import pi

if __name__ == '__main__':
    raio = input('Informe o raio: ')
    area_circulo = pi * float(raio) ** 2
    print('Área do círculo', area_circulo)
