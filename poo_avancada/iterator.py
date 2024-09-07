#!/usr/local/bin/python3

# duck type - se voa como pato, faz quá como pato,
# nada como pato e anda como pato, então é um pato
class RGB:
    # para ser iterável precisa ser tanto iterável quanto iterator
    def __init__(self):
        self.cores = ['red', 'green', 'blue'][::-1]

    # iterável
    def __iter__(self):
        return self

    # iterator
    def __next__(self):
        try:
            return self.cores.pop()
        except IndexError:
            raise StopIteration()


if __name__ == '__main__':
    cores = RGB()
    print(next(cores))
    print(next(cores))
    print(next(cores))

    try:
        print(next(cores))
    except StopIteration:
        print('Acabou!')

    for cor in RGB():
        print(cor)
