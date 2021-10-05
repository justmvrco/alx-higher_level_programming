#!/usr/bin/python3
"""
    4-print_square: print_square()
"""


def print_square(size):
    """
        print_square prints square of size provided.
        Args:
            size (int): size of square.
    """
    if isinstance(size, float) and size < 0.0:
        raise TypeError("size must be an integer")
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()

