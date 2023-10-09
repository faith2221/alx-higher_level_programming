#!/usr/bin/python3
"""Defines a Rectangle child class of BaseGeometry."""
BaseGeometry = __import__('7-rectangle.py').BaseGeometry


class Rectangle(BaseGeometry):
    """Inherits methods and properties from BaseGeometry."""
    def __init__(self, width, height):
        """

        Validates width and height using integer_validator from
        the parent class.

        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.height = height

    def area(self):
        """Calculates and returns the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Returns a string representation of the Rectangle."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
