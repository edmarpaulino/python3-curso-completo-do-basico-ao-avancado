#! /usr/local/bin/python3

# closure:  A função tem consciência do escopo em que foi definida
# neste caso conseguimos utilizar o valor de x a qualquer momento
# mesmo a função multiplicar já tendo sido chamada e retornado
def multiplicar(x):
    def calcular(y):
        return x * y  # lazy evaluation -> só é evaluado quando necessário

    return calcular


if __name__ == '__main__':
    dobro = multiplicar(2)
    triplo = multiplicar(3)
    print(dobro)
    print(triplo)
    print(f'O triplo de 3 é {triplo(3)}')
    print(f'O dobro de 7 é {dobro(7)}')
