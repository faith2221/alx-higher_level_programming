#!/usr/bin/python3
"""Define Rectangle class that inherits from BaseGeometry class."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Implements a rectangle from BaseGeometry."""
    def __init__(self, width, height):
        """

        Validates width and height using integer_validator
        from the parent class.

        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height
