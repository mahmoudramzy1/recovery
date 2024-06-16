#!/usr/bin/python3
"""Square module"""


class Square:
    """Defines a square"""

    def __init__(self, size=0):
        """Constractor

        Args:
            size: length of the side of the square
        """
        self.__size = size

    @property
    def size(self):
        """Returns the size
        """
        return self.__size

    @size.setter
    def size(self, new_size):
        """Property setter for size

        Args:
            new_size: the size to set

        Raise:
            TypeError: if size not integer
            ValueError: if size less than 0

        """
        if not isinstance(new_size, int):
            raise TypeError('size must be an integer')
        if new_size < 0:
            raise ValueError('size must be >= 0')
        self.__size = new_size

    def area(self):
        """Calculate the area of the square

        Return: area of the square
        """
        return self.__size**2
