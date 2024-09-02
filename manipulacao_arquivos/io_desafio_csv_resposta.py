#! /opt/homebrew/bin/python
import csv
from urllib import request


def read(url):
    with request.urlopen(url) as entrada:
        print('Baixando o CSV...')
        dados = entrada.read().decode('latin1')
        print('Download completo!')
        for cidade in csv.reader(dados.splitlines()):
            print(f'{cidade[8]}: {cidade[3]}')


if __name__ == '__main__':
    # r string: não interpreta caracteres especiais (raw)
    read(r'http://files.cod3r.com.br/curso-python/desafio-ibge.csv')
