#!/usr/bin/python3
"""Defines a class Rectangle"""


class Rectangle:
    """
    Class that defines properties of rectangle.

    Atrributes:
        width (int):weidth of the regtangle
        height (int):height of the regtangle
    """
    def __init__(self, width=0, height=0):
        """Creates new instances of Rectangle.

        Args:
            width (int, optional): width of rectangle. Defaults to 0.
            height (int, optional): height of rectangle. Defaults to 0.
        """

        self.height = height
        self.width = width

    @property
    def width(self):
        """Width retriver.

        Returns:
            int: the width of the rectangle.
        """

        return self.__width

    @property
    def height(self):
        """Height retriver.

        Returns:
            int: the height of the regtengle.
        """
        return self.__height

    @width.setter
    def width(self, value):
        """Property setter for width of rectangle.

        Args:
            value (int):the new width of the regtangle

        Raises:
            TypeError: if width is not integer
            ValueError: if width is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        """Property setter for height of rectangle.

        Args:
            value (int):the new height

        Raises:
            TypeError: if height is not integer
            ValueError: if height is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
