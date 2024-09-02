#! /opt/homebrew/bin/python

from math import pi

raio = input('Informe o raio: ')
area_circulo = pi * float(raio) ** 2
print('Área do círculo', area_circulo)

print('Nome do módulo', __name__)
print('Nome do pacote', __package__)
