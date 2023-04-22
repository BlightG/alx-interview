#!/usr/bin/python3
"""This module implements Pascal's triangle.

Pascal's triangle is a triangular array of numbers that follows a simple rule:
each number is the sum of the two numbers directly above it. The module
contains a function that generates Pascal's triangle up to a given number of
rows.

Example:
    >>> pascal_triangle(5)
    [[], [1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
"""


def pascal_triangle(n):
    """Generate Pascal's triangle up to n rows.

    Args:
        n (int): The number of rows to generate.

    Returns:
        list: A list of lists representing Pascal's triangle.

    Raises:
        ValueError: If n is negative.
    """
    if n <= 0:
        return [[]]

    triangle = [[]]

    for i in range(n):
        triangle.append(triangle_row(i, triangle))

    return triangle


def triangle_row(i, triangle):
    """ create an array for the trianlge """
    # print(f'in triangle row returning for i = {i}')#, end="")
    if i == 0:
        # print(f" {[1]}")
        return [1]
    elif i == 1:
        print(f" {[1, 1]}")
        return [1, 1]
    elif i == 2:
        print(f" {[1, 2, 1]}")
        return [1, 2, 1]
    elif i == 3:
        print(f' {[1, 3, 3, 1]}')
        return [1, 3, 3, 1]

    row = []
    range_ = int((i) / 2)
    # print(f' and with range {range_}', end="")

    for j in range(range_ + 1):
        # print(f'foward j = {j}')
        if j == 0:
            row.append(1)
        elif j == 1:
            row.append(i)
        else:
            if i % 2 != 0 and j == range_ + 1:
                continue
            row.append(triangle[i][j - 1] + triangle[i][j])

    if i % 2 != 0:
        for j in range(range_, -1, -1):
            # print(f'reverse j = {j}')
            row.append(row[j])
            # if j - i == 1:
            # 	row.append(1)
            # elif j - 1 == 2:
            # 	row.append(i)
            # else:
            # 	row.append(triangle[i - 1][j - 1] - triangle[i - 1][j])
    else:
        for j in range(range_ - 1, -1, -1):
            # print(f'reverse j = {j}')
            row.append(row[j])
    # print(f' {row}')
    return row
