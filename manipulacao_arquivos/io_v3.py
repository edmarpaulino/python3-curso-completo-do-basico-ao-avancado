#! /opt/homebrew/bin/python
arquivo = open('pessoas.csv')
for registro in arquivo:
    # strip remove caracteres das laterais da string
    # se não passar parâmetro o default é espaços em branco
    print('Nome: {}, Idade: {}'.format(*registro.strip().split(',')))
arquivo.close()
