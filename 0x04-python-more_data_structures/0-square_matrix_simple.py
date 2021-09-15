#!/usr/bin/python3


# square_matrix_simple - computes the square value of all ints if a matrix.
def square_matrix_simple(matrix=[]):
    lenM = len(matrix)
    new_matrix = [[0 for _ in range(len(matrix[0]))] for _ in range(lenM)]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            new_matrix[i][j] = matrix[i][j]*matrix[i][j]
    return new_matrix
