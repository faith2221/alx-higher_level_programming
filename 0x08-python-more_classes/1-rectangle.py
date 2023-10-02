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
        self.__height = value
