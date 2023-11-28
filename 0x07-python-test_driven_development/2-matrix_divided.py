#!/usr/bin/python3
"""

Matrix Divide Module

"""


def matrix_divided(matrix, div):
    string = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list) or not isinstance(matrix[0], list):
        raise TypeError(string)
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    lenchk = len(matrix[0])
    for i in range(len(matrix)):
        if len(matrix[i]) != lenchk:
            raise TypeError("Each row of the matrix must have the same size")
    ret = []
    for i in range(len(matrix)):
        app = []
        for j in range(len(matrix[i])):
            if type(matrix[i][j]) not in [int, float]:
                raise TypeError(string)
            app.append(round(matrix[i][j] / div, 2))
        ret.append(app)
    return ret
