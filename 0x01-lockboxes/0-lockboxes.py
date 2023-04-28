#!/usr/bin/python3
""" Lockboxes """


def canUnlockAll(boxes):
    """ can unlock boxes """
    # return true if the box has only one portion at index 0
    if len(boxes) == 1:
        return True

    # initialize an empty set to store the keys
    keyset = set()

    # add keys found in the index 0 the unlocked box to keyset
    for i in boxes[0]:
        if i < len(boxes):
            keyset.add(i)

    lenght = 0
    # checks if the amount of k in the boxes is less than the amount of boxes
    while lenght < len(keyset):
        # set length as lenght of keyset
        lenght = len(keyset)
        # loop over the copy of the set
        for i in keyset.copy():
            # add keys to keyset that have mathicing boxes
            if i < len(boxes):
                for j in boxes[i]:
                    if j < len(boxes):
                        keyset.add(j)

    # remove 0 if in the set since index 0 is always unlocked
    if 0 in keyset:
        keyset.remove(0)

    if len(keyset) + 1 == len(boxes):
        return True

    return False
