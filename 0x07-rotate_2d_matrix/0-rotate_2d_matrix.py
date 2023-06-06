#!/usr/bin/python3
""" a module for the rotate_2d_matrix function """


def rotate_2d_matrix(matrix):
    """ rotates a 2d list in place """
    n = len(matrix)
    c_m = [[i for i in matrix[j]] for j in range(len(matrix))]

    for i in range(n):
        for j in range(n):
            matrix[i][j] = c_m[n - 1 - j][i]
