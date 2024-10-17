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
    """Determine who the winner of the game is."""
    if x < 1 or not nums:
        return None

    n = max(nums)
    primes = [0, 0] + [1] * (n - 1)
    for i in range(2, n + 1):
        if primes[i]:
            rem_multiples(primes, i)

    primes = [i for i, n in enumerate(primes) if n]

    m = 0
    for n in nums:
        m += sum(1 for p in primes if p <= n)

    return "Maria" if m % 2 else "Ben"
