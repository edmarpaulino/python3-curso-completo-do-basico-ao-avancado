#! /usr/local/bin/python3

def fatorial(n):
    if (n < 2):
        return 1
    return n * fatorial(n - 1)


if __name__ == '__main__':
    print(f'10! = {fatorial(10)}')
