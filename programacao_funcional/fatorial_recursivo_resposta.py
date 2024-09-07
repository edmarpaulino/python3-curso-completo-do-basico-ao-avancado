#! /usr/local/bin/python3

def fatorial(n):
    return (n * fatorial(n - 1)) if (n - 1) > 1 else 1


if __name__ == '__main__':
    print(f'10! = {fatorial(10)}')
    # curiosidade: a quantidade de segundos em 6 semanas é igual fatorial de 10
    print(6 * 7 * 24 * 60 * 60)  # semanas * dias * horas * minutos * segundos
