#! /usr/local/bin/python3
from functools import reduce


def mdc(numbers):
    denominator = reduce(lambda pv, cv: min(pv, cv), numbers, numbers[0])
    while reduce(lambda pv, cv: pv + (cv % denominator), numbers, 0) != 0:
        denominator -= 1

    return denominator


if __name__ == '__main__':
    print(mdc([21, 7]))  # 7
    print(mdc([125, 40]))  # 5
    print(mdc([9, 564, 66, 3]))  # 3
    print(mdc([55, 22]))  # 11
    print(mdc([15, 150]))  # 15
    print(mdc([7, 9]))  # 1
