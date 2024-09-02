#! /opt/homebrew/bin/python
import csv

with open('desafio-ibge.csv', encoding='ISO-8859-1') as entrada:
    with open('desafio-ibge.txt', 'w') as saida:
        primeira_linha = True
        for pessoa in csv.reader(entrada):
            if primeira_linha:
                primeira_linha = False
                continue
            print(f'{pessoa[8]}, {pessoa[3]}', file=saida)
