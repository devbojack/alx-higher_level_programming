#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    my_len = len(matrix)

    for x in range(my_len):
        for y in range(len(matrix[x])):
            if y < 2:
                skip = " "
            else:
                skip = ""
            print("{:d}".format(matrix[x][y]), end=skip)
        print("")
