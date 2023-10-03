#!/usr/bin/python3
"""Implements a function that divides all elements in a matrix."""


def matrix_divided(matrix, div):
    """Returns  a new matrix where each element has been divided by div."""
    matrix_type = 'matrix must be a matrix (list of lists) of integers/floats'
    matrix_len = 'Each row of the matrix must have the same size'
    div_type = 'div must be number'
    div_zero = 'division by zero'

    if not isinstance(div, (int, float)):
        raise TypeError(div_type)
    if div == 0:
        raise ZeroDivisionError(div_zero)

    row_len = None
    new_matrix = []

    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(matrix_type)

        for i in row:
            if not isinstance(i, (int, float)):
                raise TypeError(matrix_type)

        if row_len is None:
            row_len = len(row)
        elif len(row) != row_len:
            raise TypeError(matrix_len)

        new_row = [round(i / div, 2) for i in row]
        new_matrix.append(new_row)

    return new_matrix
