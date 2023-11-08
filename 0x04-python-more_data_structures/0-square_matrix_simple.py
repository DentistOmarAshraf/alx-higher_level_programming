#!/usr/bin/python3
def square_matrix_simple(matrix=[[]]):
    new = []
    x = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            x.append(matrix[i][j] ** 2)
        new.append(x)
        x = []
    return new
