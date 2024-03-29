#!/usr/bin/python3
"""Square class"""
from models.rectangle import Rectangle
"""Rectangle class module importation"""


class Square(Rectangle):
    """The class Square that inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """The constructor for the Square class
        Args:
            size(int): the height or width of the square
            x(int): the x coordinate
            y(int): y coordinates
            id(int): the id of the square
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """This is the public getter and setter for size"""
        return self.width

    @size.setter
    def size(self, value):
        """The size setter.
        Args:
            value: the value to be set for width
        Raises:
            TypeError: width must be an integer
            ValueError: width must be > 0
        """
        if type(value) is not int or value is None:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Public method that assigns an argument to each attribute
        Args:
            attribute_order[list]: holds the order of the updated attributes
            args: arbituary positional arguments
            kwargs: arbituary kwyworded arguments
        Raises:
            AttributeErrors: if an invalid attribute name is passed
        """
        attribute_order = ['id', 'size', 'x', 'y']

        if args:
            for m, arg in enumerate(args):
                if m < len(attribute_order):
                    setattr(self, attribute_order[m], arg)

        elif kwargs:
            for key, value in kwargs.items():
                if key not in attribute_order:
                    raise AttributeError(
                            "The key '{}' is not an attribute".format(key)
                            )
                    if key == 'size':
                        if value <= 0:
                            raise ValueError("width must be > 0")
                        self.width = value
                        self.height = value
                    elif key == 'x':
                        if value < 0:
                            raise ValueError("x must be >= 0")
                        self.x = value
                    elif key == 'y':
                        if value < 0:
                            raise ValueError("y must be >= 0")
                        self.y = value
                    else:
                        setattr(self, key, value)

    def to_dictionary(self):
        """it returns the dictionary representation of a Square"""
        return {
                'id': self.id,
                'size': self.size,
                'x': self.x,
                'y': self.y
                }

    def __str__(self):
        """The string representation of the Square class"""
        return ("[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
            self.width))
