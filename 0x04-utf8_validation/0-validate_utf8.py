#!/usr/bin/python3
""" a modlue housing the log parsing function """


def validUTF8(data) -> bool:
    """ a function to validate utf-8 """

    if data is None:
        return False

    if None in data:
        return False

    for i in data:
        if i >= 256:
            return False

    return True