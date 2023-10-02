#!/usr/bin/python3
"""Defines a class called Rectangle."""


class Rectangle:
    """The defined rectangle class."""
    def __init__(self, width=0, height=0):
        """Initializes private instance attributes __width and __height."""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """The getter method for retrieving the width attribute."""
        return self.__width

    @width.setter
    def width(self, value):
        """Check if the provided value is an integer and raises errors."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter method for retrieving the height attribute."""
        return self.__height

    @height.setter
    def height(self, value):
        """Checks if the provided value is an integer and raises errors."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

    def area(self):
        """It returns the rectangle perimeter."""
        return self.__width * self.__height

    def perimeter(self):
        """It returns the rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Returns a string representation of a rectangle."""
        if self.__width == 0 or self.__height == 0:
            return ""
        rectangle_str = ""
        for _ in range(self.__height):
            rectangle_str += "#" * self.__width + "\n"
        return rectangle_str.rstrip()

    def __repr__(self):
        """Returns a string representation of the rectangle for debugging."""
        return f"Rectangle({self.__width}, {self.__height})"
