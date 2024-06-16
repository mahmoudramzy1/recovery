#!/usr/bin/python3
"""module for square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """A square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """the constructor"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """retruns string info about the square object"""
        return '[{}] ({}) {}/{} - {}'.\
            format(type(self).__name__, self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """get the size of the square"""
        return self.width

    @size.setter
    def size(self, value):
        """set the size of the square"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """method to update square atributes"""
        if args:
            self.id = args[0]
        if len(args) > 1 and args[1] is not None:
            self.width = args[1]
        if len(args) > 2 and args[2] is not None:
            self.x = args[2]
        if len(args) > 3 and args[3] is not None:
            self.y = args[3]

        elif kwargs:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.width = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        '''Returns dictionary representation of this class.'''
        return {"id": self.id, "size": self.width,
                "x": self.x, "y": self.y}
