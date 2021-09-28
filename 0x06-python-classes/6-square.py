
#!/usr/bin/python3
""" Module 6-square: class Square """


class Square():
    """
        Square: defines a square.
        Attributes:
            size (int): size of square.
        Method:
                __init__ : init of size attribute for each instance.
    """

    def __init__(self, size=0, position=(0, 0)):

        """ Initialization of attributes for instances
            Args:
                size (int): size of the square.
                position (int tuple): position of the square
        """
        if not (isinstance(size, int)):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
        self.__position = position

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
                value: size value to set to
        """
        if not (isinstance(value, int)):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """ getter function for private attribuet position
            Returns:
                position.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
            setter function for private attribute position.
            Args:
                value: position value to set to.
        """
        if isinstance(value, tuple) and len(value) == 2:
            if isinstance(value[0], int) and isinstance(value[1], int):
                if value[0] >= 0 and value[1] >= 0:
                    self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """
             area of the square.
        """
        return self.__size * self.__size

    def my_print(self):
        """
            prints the square with character #
        """
        if self.__size == 0:
            print()
        else:
            i, j = 0, 0
            temp = self.__position[0]
            for i in range(self.__position[1]):
                print()
            for j in range(self.__size):
                print("{}{}".format(" " * temp, "#" * self.__size))
