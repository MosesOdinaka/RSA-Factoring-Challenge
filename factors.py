#!/usr/bin/python3
import sys


def factorize(n):
    for i in range(2, n):
        if n % i == 0:
            return (i, n // i)
    return None


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: factors <file>')
        sys.exit(1)

    with open(sys.argv[1], 'r') as f:
        for line in f:
            n = int(line.strip())
            factors = factorize(n)
            if factors is not None:
                print(f'{n}={factors[0]}*{factors[1]}')
