#!/usr/bin/python3
"""Square module."""


class Square:
    """Define a square"""

    def __init__(self, size=0):
        """Constractor.

        Args:
            size: length of the side of the square

        Raise:
            TypeError: if size is not an integer
            ValueError: if size is less than zero
            """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        """Area of the square

        Return: area of the square
        """
        return self.__size**2
