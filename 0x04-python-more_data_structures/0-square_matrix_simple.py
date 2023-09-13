#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    res = []
    for row in range(len(matrix)):
        row_squared = list(map(lambda x: x ** 2, matrix[row]))
        res.append(row_squared)
    return (res)
