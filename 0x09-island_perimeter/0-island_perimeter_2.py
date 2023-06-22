#!/usr/bin/python3
""" a function to callculate the permater of an island """


def island_perimeter(grid):
    """ Arg:
            grid: list[list] object
                - 0 represents water
                - 1 represents land
                - Each cell is square, with a side length of 1
                - Cells are connected horizontally/vertically (not diagonally).
                - grid is rectangular, with its width and height not exceeding 100
                - The grid is completely surrounded by water
                - There is only one island (or nothing).
                - The island doesnt have “lakes”
        Returns:
            an int object of the total perimater
    """

    r, c = 0, 0
    perimeter = 0

    while r < len(grid):
        if 1 not in grid[r]:
            r += 1
            continue
        c = 0
        while c < len(grid[r]):
            if grid[r][c] == 0:
                c += 1
                continue
            elif grid[r][c] == 1:
                # on the first row
                if r == 0:
                    # on the first column
                    # add 1 to perimeter for top of row 0
                    perimeter += 1
                    if c == 0:
                        # check if it has only one column
                        if len(grid[c]) < 1:
                            perimeter += 2
                            continue
                        else:
                            # check if the next index is 1
                            if grid[r][c + 1] == 1:
                                perimeter += 1
                                c += 1
                                continue
                            else:
                                perimeter += 2
                                c += 1
                                continue
                    # on the first row last column for line with more than one column
                    elif c == len(grid[r]) - 1 and len(grid[r]) > 1:
                        # add 1 if has a neighbour
                        if grid[r][c - 1] == 1:
                            perimeter += 1
                            continue
                        # or 2 if it doesnt have a neighbour
                        else:
                            perimeter += 2
                            continue
                    # on the first row middle lines
                    else:
                        # check left and right
                        if grid[r][c - 1] != 1:
                            perimeter += 1
                        if grid[r][c + 1] != 1:
                            perimeter += 1
                        c += 1
                        continue
                if r >= 1 and r < len(grid) - 1:
                    if c == 0:
                        # check if it has only one column
                        if len(grid[c]) < 1:
                            perimeter += 2
                            continue
                        else:
                            # check if the next index is 1
                            if grid[r][c + 1] == 1:
                                perimeter += 1
                                c += 1
                                continue
                            else:
                                perimeter += 2
                                c += 1
                                continue
                    # on the last column for line with more than one column
                    elif c == len(grid[r]) - 1 and len(grid[r]) > 1:
                        # add 1 if has a neighbour
                        if grid[r][c - 1] == 1:
                            perimeter += 1
                            continue
                        # or 2 if it doesnt have a neighbour
                        else:
                            perimeter += 2
                            continue
                    # on the first row middle lines
                    else:
                        # check left and right
                        if grid[r][c - 1] != 1:
                            perimeter += 1
                        if grid[r][c + 1] != 1:
                            perimeter += 1
                        c += 1
                        continue
                if r == len(grid) - 1:
                    perimeter += 1
