#!/usr/bin/python3
""" a module for the minOperations function """


def minOperations(n: int) -> int:
    """ returns the minimum number of addition and
        multiplication required to make n  starting from 1
    """

    if n <= 0:
        return 0

    # 1 => ca => p => (1 + 1) 2 => ca => p => (2 + 2) 4
    # 1 => ca => p => (1 + 1) 2 => p => (1 + 2) 3 => ca =>
    # p => (3 + 3) 6 => ca => p => (6 + 6) 12
    factor_list = [i for i in range(1, n + 1) if n % i == 0]
    return len(factor_list) + 1
