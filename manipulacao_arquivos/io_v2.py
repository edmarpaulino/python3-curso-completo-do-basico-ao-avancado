#! /opt/homebrew/bin/python
arquivo = open('pessoas.csv')
for registro in arquivo:
    print('Nome: {}, Idade: {}'.format(*registro.split(',')), end='')
arquivo.close()
