#!/usr/local/bin/python3
def fibonacci(sequencia=[0, 1]):
    # Uso de mutáveis como valor default (armadilha)
    # A lista usada como valor default é gerada uma
    # única vez e toda chamada da função a referência
    # é sempre a mesma, ou seja, alterar o conteúdo
    # da lista faz com que as próximas chamadas o valor
    # desta lista seja o alterado na chamada anterior
    sequencia.append(sequencia[-1] + sequencia[-2])
    return sequencia


if __name__ == '__main__':
    inicio = fibonacci()
    print(inicio, id(inicio))
    print(fibonacci(inicio))
    restart = fibonacci()
    print(restart, id(restart))
    assert restart == [0, 1, 1]
