#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = []

    for x in range(len(matrix)):
        a = []
        for y in range(len(matrix[x])):
            total = matrix[x][y]**2
            a.append(total)
        new_matrix.append(a)

    return (new_matrix)
