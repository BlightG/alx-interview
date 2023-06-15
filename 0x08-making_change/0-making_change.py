#!/usr/bin/python3
""" an interview module housing the function makeChange """


def makeChange(coins, total):
    """ Args:
            coins: Lists a list of the values of the coins in your possession
            total: amount that you should try to make
        Return:
            if total is 0 or less, return 0
            If total cannot be met by any number of coins you have, return -1
    """

    if not isinstance(coins, list):
        return 0

    if total <= 0:
        return 0

    if total in coins:
        return 1

    new_total = total
    sum_list = []
    coins.sort(reverse=True)
    i = 0
    while i < len(coins):
        if coins[i] <= new_total:
            if (new_total - coins[i]) >= 0:
                new_total -= coins[i]
                sum_list.append(coins[i])
            if (new_total - coins[i]) < 0:
                i += 1
        else:
            i += 1
        if new_total == 0:
            break

    if sum(sum_list) == total:
        return len(sum_list)
    else:
        return -1
