#! /opt/homebrew/bin/python

from math import pi
import sys
import errno


class TerminalColor:
    ERRO = '\033[91m'
    NORMAL = '\033[0m'


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
        sys.exit(errno.EPERM)

    raio = sys.argv[1]
    if not raio.isnumeric():
        help()
        erro = 'O raio deve ser um valor numérico'
        print(TerminalColor.ERRO + erro + TerminalColor.NORMAL)
        sys.exit(errno.EINVAL)

    area = circulo(raio)
    print('Área do círculo', area)
