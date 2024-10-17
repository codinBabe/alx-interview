#!/usr/bin/python3
"""A prime game module."""


def isPrime(n):
        """
        Check if a number is prime.
        """
        if n <= 1:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True


def getPrimes(n):
    """Get all prime numbers up to n."""
    primes = []
    for i in range(2, n + 1):
        if isPrime(i):
            primes.append(i)
    return primes


def getWinner(n):
    """Determine the winner of the game."""
    primes = getPrimes(n)
    if len(primes) % 2 == 0:
        return "Ben"
    return "Maria"


def isWinner(x, nums):
    """Determine who the winner of each game is."""
    maria = 0
    ben = 0
    for n in nums:
        winner = getWinner(n)
        if winner == "Maria":
            maria += 1
        else:
            ben += 1
    if maria > ben:
        return "Maria"
    if ben > maria:
        return "Ben"
    return None
