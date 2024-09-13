#!/usr/bin/python3
"""N queens problem"""
import sys


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

if not sys.argv[1].isdigit():
    print("N must be a number")
    sys.exit(1)

n = int(sys.argv[1])
if n < 4:
    print("N must be at least 4")
    sys.exit(1)


def queens(n, i=0, a=[], b=[], c=[]):
    """N queens problem"""
    if i < n:
        for j in range(n):
            if j not in a and i+j not in b and i-j not in c:
                for solution in queens(n, i+1, a+[j], b+[i+j], c+[i-j]):
                    yield solution
    else:
        yield a


def solve(n):
    """Solve N queens problem"""
    k = []
    i = 0
    for solution in queens(n, 0):
        for j in solution:
            k.append([i, j])
            i += 1
        print(k)
        k = []
        i = 0


solve(n)
