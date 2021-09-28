#!/usr/bin/python3
""" Module 4-square: class Square """


class Square():
    """
        Square: defines a square.
        Attributes:
            size (int): size of square.
        Method:
                __init__ : init of size attribute for each instance.
    """

    def __init__(self, size=0):

        """ Initialization of attributes for instances
            Args:
                size (int): size of the square.
        """
        if not (isinstance(size, int)):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """ getter function for private attribute size.
            Returns:
                size.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ setter function for private attribute size.
            Args:
                value: value to be set.
            Returns:
                nothing
        """
        if not (isinstance(value, int)):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
             area of the square.
        """
        return self.__size * self.__size
