#!/usr/bin/python3
""" Lockboxes """


def canUnlockAll(boxes):
    """ can unlock boxes """
    if len(boxes[0]) == 0:
        return False

    keyset = set()

    for i in boxes[0]:
        keyset.add(i)

    lenght = 0
    while lenght < len(keyset):
        lenght = len(keyset)
        for i in keyset.copy():
            for j in boxes[i]:
                keyset.add(j)

    if 0 in keyset:
        keyset.remove(0)

    # print(f'keyset > {len(keyset)} boxes > {len(boxes)}')
    if len(keyset) + 1 == len(boxes):
        return True

    return False
