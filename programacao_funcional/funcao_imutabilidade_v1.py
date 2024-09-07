#! /usr/local/bin/python3

from functools import reduce
from operator import add

valores = [30, 10, 25, 70, 100, 94]

# procedural - passa a lista para a função
print(sorted(valores))  # Não muda a lista - imutabilidade
print(valores)


# oop - chama o método do objeto
# valores.sort()  # Altera a lista - mutabilidade
# print(valores)

print(min(valores))
print(max(valores))
print(sum(valores))
print(reduce(add, valores))
print(reversed(valores))
print(list(reversed(valores)))
print(valores)
