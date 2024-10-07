#!/usr/bin/python3
"""Making change alogrithim"""


def makeChange(coins, total):
    """Making change alogrithim"""
    if not coins or coins is None:
        return -1
    if total <= 0:
        return 0
    coins_needed = 0
    coins = sorted(coins)[::-1]
    for coin in coins:
        while coins <= total:
            total -= coin
            coins_needed += 1
        if total == 0:
            return coins_needed
    return -1

