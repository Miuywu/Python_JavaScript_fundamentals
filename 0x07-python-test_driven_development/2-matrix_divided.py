#!/usr/bin/python3
"""
module contains matrix divide


"""


def matrix_divided(matrix, div):
    """
    divides each elem of matrix
    """
    line_len = 0
    prev_len = -1
    new_matrix = []
    pep8 = "matrix must be a matrix (list of lists) of integers/floats"
    if type(matrix) != list:
        raise TypeError("matrix must be a matrix (list of lists) of i\
ntegers/floats")
    for d in matrix:
        if type(d) != list:
            raise TypeError("matrix must be a matrix (list of lists) of i\
ntegers/floats")
    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for a in range(len(matrix)):
        new_list = []
        line_len = 0
        for b in range(len(matrix[a])):
            if type(matrix[a][b]) != int and type(matrix[a][b]) != float:
                raise TypeError(pep8)
            new_list.append(round(matrix[a][b] / div, 2))
            line_len += 1
        if prev_len == -1:
            prev_len = line_len
        if prev_len != line_len:
            raise TypeError("Each row of the matrix must have the same size")
        prev_len = line_len
        new_matrix.append(new_list)
    return new_matrix
