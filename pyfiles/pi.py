#!/usr/bin/env python3


import math


# or, we can use math.factorial(n)
def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)


def srinivasa(k):
    total = 0
    for i in range(k):
        num = factorial(4 * i) * (1103 + 26390 * i)
        # num = math.factorial(4 * i) * (1103 + 26390 * i)
        den = factorial(i)**4 * 396**(4 * i)
        # den = math.factorial(i)**4 * 396**(4 * i)
        total += num / den
    total *= 2 * math.sqrt(2) / 9801
    return 1 / total


if __name__ == '__main__':
    import sys
    iterations = int(sys.argv[1])
    print(srinivasa(iterations))
