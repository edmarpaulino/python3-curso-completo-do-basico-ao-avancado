#!/usr/loca/bin/python3
class ClasseSimples:
    contador = 0

    def __init__(self):
        ClasseSimples.contador += 1


if __name__ == '__main__':
    lista = [ClasseSimples(), ClasseSimples()]
    print(ClasseSimples.contador)  # Esperado 2
