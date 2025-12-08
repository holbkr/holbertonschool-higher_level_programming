#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    matrix2 = [row[:] for row in matrix]
    for i in range(len(matrix2)):
        for j in range(len(matrix2[i])):
            matrix2[i][j] = matrix2[i][j] ** 2
    return matrix2
