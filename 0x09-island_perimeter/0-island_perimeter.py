#!/usr/bin/python3
""" a function to callculate the permater of an island """


def island_perimeter(grid):
    """ Arg:
            grid: list[list] object
                - 0 represents water
                - 1 represents land
                - Each cell is square, with a side length of 1
                - Cells are connected horizontally/vertically (not diagonally).
                - grid is rectangular, with its width and height < 100
                - The grid is completely surrounded by water
                - There is only one island (or nothing).
                - The island doesnt have “lakes”
        Returns:
            an int object of the total perimater
    """
    island = [[]]  # an gird to store a island only
    g_r, g_c = 0, 0  # row and column for grid
    i_r, i_c = 0, 0  # row and column for island

    if not isinstance(grid, list):
        return 0

    if len(grid) == 0:
        return 0

    while g_r < len(grid):
        if 1 not in grid[g_r]:
            g_r += 1
            continue
        g_c = 0

        while g_c < len(grid[g_r]):
            if grid[g_r][g_c] == 1:
                # append any land to the island
                island[i_r].append(1)
            g_c += 1

        # if the last row of the issland is non empty append empty row
        if len(island[i_r]) > 0:
            i_r += 1
            island.append([])
        g_r += 1

    if len(island) == 0:
        return 0

    # if length of last row is 0 pop it
    if len(island[len(island) - 1]) == 0:
        island.pop()

    # find the row with the biggest width
    max_i_r = 0
    for r in island:
        if max_i_r <= len(r):
            max_i_r = len(r)

    perimeter = len(island) * 2
    perimeter += max_i_r * 2
    return perimeter
