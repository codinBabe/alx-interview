#!/usr/bin/python3
"""A prime game module."""


def rem_multiples(a, b):
    """remove multiples of prime number."""
    for i in range(2, len(a)):
        try:
            a[i * b] = 0
        except (ValueError, IndexError):
            break


def isWinner(x, nums):
    if x <= 0 or nums is None:
        return None
    if x != len(nums):
        return None
    
    ben = 0
    maria = 0

    a = [1 for x in range(sorted(nums)[-1] + 1)]
    a[0], a[1] = 0, 0
    for i in range(2, len(a)):
        rem_multiples(a, i)

    for i in nums:
        if sum(a[0:i + 1]) % 2 == 0:
            ben += 1
        else:
            maria += 1
    if ben > maria:
        return "Ben"
    elif ben < maria:
        return "Maria"
    else:
        return None