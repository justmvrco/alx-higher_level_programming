#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    if matrix:
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[i])):
                if j != len(matrix[i]) - 1:
                    print("{:d}".format(matrix[i][j]), end=" ")
                else:
                    print("{:d}".format(matrix[i][j]))
    else:
        print()

