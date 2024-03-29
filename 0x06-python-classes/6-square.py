#!/usr/bin/python3
"""6-square.py"""


class Square:
    """The class Square defines a square"""
    def __init__(self, size=0, position=(0,0)):
        """The __init__ is a special method.

        Args:
            size (int): It's a private instance attribute.
            position (tuple): it's a private instance attribute.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """This is the setter property used to retrieve size.

        Args:
        value (int): variable in the setter property that holds
        the new size value.
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """The getter property retrieves the position.

        Args:
            value (int): it is the new position to be set using setter.
        """
        return self.__position

    @position.setter
    def position(self, value):
        if (
                (type(value) is not tuple) or (len(value) != 2) or
                (type(value[0]) is not int) or (type(value[1]) is not int) or
                (value[0] < 0) or (value[1] < 0)
                ):
            raise TypeError("The position must be a tuple of two positive integers")
        self.__position = value

    def area(self):
        """It calculates the area of the square.

        Args:
            cal int: It calculates the area of a square.
        """
        cal = self.__size * self.__size
        return cal

    def my_print(self):
        """It prints to the stdout the square with #.
        if size is 0, it prints an empty line.
        """
        if self.__size == 0:
            print()
        else:
            for m in range(self.__position[1]):
                print()
            for m in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
