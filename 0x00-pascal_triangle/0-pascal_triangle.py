#!/usr/bin/python3
""" Pascal Triangle Interview Challenge """


def pascal_triangle(n):
    """ Generate Pascal's triangle up to n rows.

    Args:
        n (int): The number of rows to generate.

    Returns:
        list: A list of lists representing Pascal's triangle.

    Raises:
        ValueError: If n is negative
    """

   if n <= 0:
        return []
    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)
        triangle.append(row)
    return triangle