#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    a = 0
    while a < len(matrix):
        for b in matrix[a]:
            if b != matrix[a][len(matrix[a]) - 1]:
                print("{:d}".format(b), end=' ')
            else:
                print("{:d}".format(b), end='')
        print()
        a = a + 1
