#!/usr/bin/python3
"""Defines a child class called Square."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Initializes a square."""
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Constructor for the square class.

        Args:
            width (int) : The width of the square.
            height (int): The height of the square.
            x (int): The x-coordinate of the square's position.
            y (int): The y-coordinate of the square's position.
            id (int): The unique identifier of the square.

        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter for the size attribute."""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for the size attribute."""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Assign arguments to attribute in a specific order."""
        if args and len(args) != 0:
            m = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif m == 1:
                    self.width = arg
                elif m == 2:
                    self.height = arg
                elif m == 3:
                    self.x = arg
                elif m == 4:
                    self.y = arg

            elif kwargs and len(kwargs) != 0:
                for n, b in kwargs.items():
                    if n == "id":
                        if b is None:
                            self.__init__(self.width, self.height,
                                          self.x, self.y)
                        else:
                            self.id = b
                    elif n == "width":
                        self.width = b
                    elif n == "height":
                        self.height = b
                    elif n == "x":
                        self.x = b
                    elif n == "y":
                        self.y = b

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle."""
        return {
            "id": self.id
            "width": self.width
            "height": self.height
            "x": self.x
            "y": self.y
        }

    def __str__(self):
        """Override the string representation of Rectangle."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y,
                                                       self.width, self.height)
