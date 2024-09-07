#! /usr/local/bin/python3

compras = (
    {'quantidade': 2, 'preco': 10},
    {'quantidade': 3, 'preco': 20},
    {'quantidade': 5, 'preco': 14},
)

# funções lambdas tem o retorno implícito
totais = tuple(
    map(lambda compra: compra['quantidade'] * compra['preco'], compras))


print('Preços totais:', totais)
print('Total geral:', sum(totais))
