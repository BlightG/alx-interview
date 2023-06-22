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

    r, c = 0, 0
    perimeter = 0

    while r < len(grid):
        if 1 not in grid[r]:
            r += 1
            continue
        c = 0
        while c < len(grid[r]):
            if grid[r][c] == 1:
                if check_left(grid[r], c):
                    perimeter += 1
                if check_right(grid[r], c):
                    perimeter += 1
                if check_down(grid, r, c):
                    perimeter += 1
                if check_up(grid, r, c):
                    perimeter += 1
            c += 1
        r += 1
    return perimeter


def check_left(row, c):
    """ Args:
            row: current row
            c: currnet column
        Returns:
         False: if there is a one to the left
         True: if there is a one or c is the first element
    """

    if c not in range(len(row)):
        raise (f'index {c} is out of range {len(row)}')

    if not isinstance(row, list):
        raise (f'row must be type list but found {type(row)}')

    if len(row) == 1:
        return True

    if c == 0:
        return True

    if c in range(1, len(row)):
        if row[c - 1] == 1:
            return False
        else:
            return True


def check_right(row, c):
    """ Args:
            row: current row
            c: currnet column
        Returns:
         False: if there is a one to the right
         True: if there is a one to the right or c is the last element
    """

    if c not in range(len(row)):
        raise (f'index {c} is out of range {len(row)}')

    if not isinstance(row, list):
        raise (f'row must be type list but found {type(row)}')

    if len(row) == 1:
        return True

    if c == len(row):
        return True

    if c in range(len(row) - 1):
        if row[c + 1] == 1:
            return False
        else:
            return True


def check_up(grid, r, c):
    """
        Args:
            grid: a List[List] object described in island_perimater doc
            r: row index for grid
            c: column index of grid
        Returns:
            True: if it is on first row or has no 1 above
            Fasle: if has 1 above
    """
    if r not in range(len(grid)):
        raise (f'row index {r} is out of range {len(grid)}')

    if c not in range(len(grid[r])):
        raise (f'index {c} is out of range {len(grid[r])}')

    if not isinstance(grid, list):
        raise (f'row must be type list but found {type(grid)}')

    if not isinstance(grid[r], list):
        raise (f'row must be type list but found {type(grid[r])}')

    if len(grid) == 1:
        return True

    if r == 0:
        return True

    if r in range(1, len(grid)):
        if grid[r - 1][c] == 1:
            return False
        else:
            return True


def check_down(grid, r, c):
    """
        Args:
            grid: a List[List] object described in island_perimater doc
            r: row index for grid
            c: column index of grid
        Returns:
            True: if it is on last row or has no 1 below
            Fasle: if has 1 below
    """
    if r not in range(len(grid)):
        raise (f'row index {r} is out of range {len(grid)}')

    if c not in range(len(grid[r])):
        raise (f'index {c} is out of range {len(grid[r])}')

    if not isinstance(grid, list):
        raise (f'row must be type list but found {type(grid)}')

    if not isinstance(grid[r], list):
        raise (f'row must be type list but found {type(grid[r])}')

    # check grid has only one row
    if len(grid) == 1:
        return True

    if r == len(grid) - 1:
        return True

    if r in range(len(grid) - 1):
        if grid[r + 1][c] == 1:
            return False
        else:
            return True
