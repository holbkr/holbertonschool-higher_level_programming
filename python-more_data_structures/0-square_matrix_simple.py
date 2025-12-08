#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    matrix2 = matrix[:]
    for i in matrix2:
        for j in i:
            j=j**2
    return matrix2
