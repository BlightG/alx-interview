#!/usr/bin/python3
""" Lockboxes """


def canUnlockAll(boxes):
    """ can unlock boxes """
    # if len(boxes[0]) == 0:
    #     return False

    keyset = set()

    for i in boxes[0]:
        keyset.add(i)

    lenght = 0
    while lenght < len(keyset):
        lenght = len(keyset)
        for i in keyset.copy():
            for j in boxes[i]:
                keyset.add(j)

    keyset.remove(0)

    if len(keyset) == len(boxes):
        return True

    return False
