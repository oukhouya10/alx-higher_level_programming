#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in matrix:
        n1_row = list([x**2 for x in row])
        new_matrix.append(n1_row)
    return new_matrix
