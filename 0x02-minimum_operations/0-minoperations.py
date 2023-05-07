#!/usr/bin/python3
""" a module for the minOperations function """


def minOperations(n: int) -> int:
    """ returns the minimum number of addition and
        multiplication required to make n  starting from 1
    """

    if n <= 1:
        return 0
    

    factor_list = [i for i in range(1, n + 1) if n % i == 0]
    # print(factor_list)
    return factor_recursion(n)
    # return factor_list


def factor_recursion(n: int) -> int:
    """ a recusive function that creats a recursive function """

    # print(n, end="")

    if n == 1:
        return 1

    if n <= 0:
        return 0

    flag = 0
    for i in range(2, n + 1):
        if n % i == 0:
            if n != i:
                flag = i
            break

    # print(f'count = {count}')
    if flag == 0:
        return n
    else:
        return int(n / factor_recursion(int(n / flag))) + factor_recursion(int(n / flag))
