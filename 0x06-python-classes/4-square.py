#!/usr/bin/python3
"""This is the Square class."""


class Square:
    def __init__(self, size=0):
        """Initializes a new square."""
        self.size = size

    @property
    def size(self):
        """Retrieve the size of a square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the area of the square."""
        return self.__size ** 2
