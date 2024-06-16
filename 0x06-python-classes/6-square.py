#!/usr/bin/python3
"""Square module"""


class Square:
    """Defines a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Constractor

        Args:
            __size: length of the side of the square
            __position: position of printing square
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Returns the position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Property setter of position

        Args:
            value: the new position

        Raise:
            TypeError: if the value is not tuple of two integer positives
        """
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculate the area of the square

        Return: area of the square
        """
        return self.__size**2

    def my_print(self):
        """Prints the square
        """
        if self.__size == 0:
            print()
        else:
            for j in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for k in range(self.__position[0]):
                    print(" ", end="")
                print("#" * (self.__size))
