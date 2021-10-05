#!/usr/bin/python3
"""
    2-matrix_divide: matrix_divide()
"""


def matrix_divided(matrix, div):
    """
        matrix_divide() divides all elements of a matrix.
        Args:
            matrix: list of lists of integers.
            div: number to be divided by.
        Returns:
            new matrix.
    """
    new_matrix = []
    temp = []
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div is 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a\
 matrix (list of lists) of integers/floats")
    if len(matrix) is 0:
        raise TypeError("matrix must be a\
 matrix (list of lists) of integers/floats")
    elif len(matrix) is 1:
        for item in matrix[0]:
            if type(item) not in [int, float]:
                raise TypeError("matrix must be a\
 matrix (list of lists) of integers/floats")
            temp.append(float("{:.2f}".format(item / div)))
        new_matrix.append(temp)
        return new_matrix
    else:
        length = len(matrix[0])
        for l_int in matrix:
            if not isinstance(l_int, list):
                raise TypeError("matrix must be a\
 matrix (list of lists) of integers/floats")
            if len(l_int) != length:
                raise TypeError("Each row of the matrix\
 must have the same size")
            for num in l_int:
                if type(num) not in [int, float]:
                    raise TypeError("matrix must be a\
 matrix (list of lists) of integers/floats")
                temp.append(float("{:.2f}".format(num / div)))
            new_matrix.append(temp)
            temp = []
        return new_matrix
