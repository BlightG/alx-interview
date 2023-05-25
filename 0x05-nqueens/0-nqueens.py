#!/usr/bin/python3
""" a solution to the nqueens problem """
import sys


def solveNqueen(n):
    """ setsup enviroment for backtrack """
    col = set()  # col value to check if col has queen
    posdiag = set()  # row + col to check if + diagonal has queen
    negdiag = set()  # row - col to check if - diagonal has queen

    result = []
    board = [[i] for i in range(n)]

    def backtrack(r):
        if r == n:
            copy = board.copy()
            result.append(copy)
            print(board)
            return

        for c in range(n):
            if c in col or (r + c) in posdiag or (r - c) in negdiag:
                continue

            col.add(c)
            posdiag.add(r + c)
            negdiag.add(r - c)
            board[r].append(c)

            backtrack(r + 1)

            col.remove(c)
            posdiag.remove(r + c)
            negdiag.remove(r - c)
            board[r].pop()

    backtrack(0)
    return result


if __name__ == "__main__":

    if len(sys.argv) != 2:
        print('Usage: nqueens N')
        exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print('N must be a number')
        exit(1)

    if N < 4:
        print("N must be at least 4")
        exit(1)

    solveNqueen(N)
