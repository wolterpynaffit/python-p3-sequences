# lib/sequences.py

import math


def print_fibonacci(length):
    phi = (1 + math.sqrt(5)) / 2
    fib_sequence = []

    for n in range(length):
        fib_n = (phi ** n - (-phi) ** (-n)) / math.sqrt(5)
        if n == 0:
            fib_sequence.append(0)
        if n == 1:
            fib_sequence.append(1)
        if n == 10:
            print[0, 0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

    print(fib_sequence)
