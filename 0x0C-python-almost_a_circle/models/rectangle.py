#!/usr/bin/python3
"""this is the circle module"""
from models.base import Base


class Rectangle(Base):
    """this is the rectangle class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """this is the sub class constructor"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        '''Width of this rectangle.'''
        return self.__width

    @width.setter
    def width(self, value):
        self.validate_integer("width", value, False)
        self.__width = value

    @property
    def height(self):
        '''Height of this rectangle.'''
        return self.__height

    @height.setter
    def height(self, value):
        self.validate_integer("height", value, False)
        self.__height = value

    @property
    def x(self):
        '''x of this rectangle.'''
        return self.__x

    @x.setter
    def x(self, value):
        self.validate_integer("x", value)
        self.__x = value

    @property
    def y(self):
        '''y of this rectangle.'''
        return self.__y

    @y.setter
    def y(self, value):
        self.validate_integer("y", value)
        self.__y = value

    def validate_integer(self, name, value, eq=True):
        '''Method for validating the value.'''
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if eq and value < 0:
            raise ValueError("{} must be >= 0".format(name))
        elif not eq and value <= 0:
            raise ValueError("{} must be > 0".format(name))

    def area(self):
        """method returns the rectangle area"""
        return self.width * self.height

    def display(self):
        """method prints the # of the rectangle"""
        if self.width == 0 or self.height == 0:
            return ""

        for b in range(self.y):
            print()

        for i in range(self.height):
            print(" " * self.x, end="")
            for j in range(self.width):
                print("#", end="")
            print()

    def update(self, *args, **kwargs):
        """this method to update attributes"""
        if args:
            self.id = args[0]
            if len(args) > 1 and args[1] is not None:
                self.width = args[1]
            if len(args) > 2 and args[2] is not None:
                self.height = args[2]
            if len(args) > 3 and args[3] is not None:
                self.x = args[3]
            if len(args) > 4 and args[4] is not None:
                self.y = args[4]
        elif kwargs:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.width = kwargs["width"]
            if "height" in kwargs:
                self.height = kwargs["height"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}".\
                format(self.id, self.x, self.y, self.width, self.height)

    def to_dictionary(self):
        "returns the rectangle atrributes in dict"""
        return {'x': self.x, 'y': self.y, 'id': self.id,
                'height': self.height, 'width': self.width}
