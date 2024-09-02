#! /opt/homebrew/bin/python
arquivo = open('pessoas.csv')
dados = arquivo.read()
arquivo.close()
for registro in dados.splitlines():
    # o * desenpacota a lista (semelhante ao spread operator do js)
    print('Nome: {}, Idade: {}'.format(*registro.split(',')))

# arquivo = open('pessoas.csv')
# for registro in arquivo.readlines():
#     print('Nome: {}, Idade: {}'.format(*registro.split(',')), end='')
# arquivo.close()
