#!/usr/bin/python3
""" a modlue housing the log parsing function """


def validUTF8(data) -> bool:
    """ a function to validate utf-8 """

    if data is None:
        return False

    if None in data:
        return False

    for i in data:
        if i < 128:
            continue
        else if i >= 128 and i <= 256:
            return False

        # bin_list = bin(i)[2:].zfill()
        # print(f'bin_list = {bin_list} type = {type(bin_list)} for i = {i} ')

    return True

# def bin_list(integer: int) -> list:
#     """ converts an int to a binary """

    