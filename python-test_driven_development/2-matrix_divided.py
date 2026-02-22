#!/usr/bin/python3
def matrix_divided(matrix, div):
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    msg = "matrix must be a matrix (list of lists) of integers/floats"

    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(msg)

    if not isinstance(matrix[0], list) or len(matrix[0]) == 0:
        raise TypeError(msg)

    row_size = len(matrix[0])
    new_matrix = []

    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(msg)

        if len(row) != row_size:
            raise TypeError("Each row of the matrix must have the same size")

        new_row = []
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(msg)
            new_row.append(round(element / div, 2))
        new_matrix.append(new_row)

    return new_matrix
