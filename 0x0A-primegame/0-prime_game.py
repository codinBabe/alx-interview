#!/usr/bin/python3
"""A prime game module."""


def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def isWinner(x, nums):
    """Determine the winner of the game."""
    if x < 1:
        return None
    if not nums:
        return None
    n = max(nums)
    primes = [0] * (n + 1)
    for i in range(1, n + 1):
        primes[i] = primes[i - 1]
        if is_prime(i):
            primes[i] += 1
    wins = [0, 0]
    for i in range(x):
        score = primes[nums[i]] - (i - wins[0])
        if score % 2 == 0:
            wins[1] += 1
        else:
            wins[0] += 1
    if wins[0] == wins[1]:
        return None
    return "Maria" if wins[0] > wins[1] else "Ben"
