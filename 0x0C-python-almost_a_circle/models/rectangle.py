#!/usr/bin/python3
"""Defines a child class called Rectangle."""
from models.base import Base


class Rectangle(Base):
    """Rectangle class that inherits from base."""
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Constructor for the rectangle class.

        Args:
            width (int) : The width of the rectangle.
            height (int): The height of the rectangle.
            x (int): The x-coordinate of the rectangle's position.
            y (int): The y-coordinate of the rectangle's position.
            id (int): The unique identifier of the rectangle.

        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter for the width attribute."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for the width attribute."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter for the height attribute."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for the height attribute."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter for the x attribute."""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for the x attribute."""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value <= 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter for the y attribute."""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for the y attribute."""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value <= 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Calculates and returns area of a rectangle."""
        return self.__width * self.__height

    def display(self):
        """Print the rectangle using '#' characteers."""
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print("#" * self.__width)

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
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """Override the string representation of Rectangle."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y,
                                                       self.width, self.height)
