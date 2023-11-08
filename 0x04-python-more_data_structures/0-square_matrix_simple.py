#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    nouv_matrix = []
    for row in matrix:
        nouv_row = list([x**2 for x in row])
        nouv_matrix.append(nouv_row)
        return nouv_matrix

