#!/usr/bin/python3
"""
This module provides a function that divides all elements of a matrix.
It handles various edge cases like zero division and type checking.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a divisor (div).

    Args:
        matrix: A list of lists containing integers or floats.
        div: A number (integer or float) to divide the matrix elements by.

    Returns:
        A new matrix with the results rounded to 2 decimal places.
    """
    msg = "matrix must be a matrix (list of lists) of integers/floats"

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(msg)

    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError(msg)

    row_size = len(matrix[0])

    new_matrix = []
    for row in matrix:
        if len(row) != row_size:
            raise TypeError("Each row of the matrix must have the same size")

        new_row = []
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(msg)
            new_row.append(round((element / div), 2))
        new_matrix.append(new_row)

    return new_matrix
