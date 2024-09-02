produto = {'nome': 'Caneta Chic', 'preco': 14.99,
           'importada': True, 'estoque': 793}

for chave in produto:  # ou produto.keys() - redundante
    print(chave)

for valor in produto.values():
    print(valor)

for chave, valor in produto.items():
    print(chave, '=', valor)

# continua disponível mesmo fora do laço for (último valor atribuido)
# disponível dentro do escopo onde foi o laço for foi definido
print(chave, valor)


# for chave, valor in produto: # erro
#     print(chave, valor)
