#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    res = matrix.copy()
    for row in range (len(matrix)):
        res[row] = list(map(lambda x: x ** 2, matrix[row]))
    return (res)
