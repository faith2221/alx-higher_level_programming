#!/usr/bin/python3
"""Defines a child class square ."""
Rectangle = __import__('9-rectangle.py').Rectangle


class Square(Rectangle):
    """Implements the square class from rectangle class."""
    def __init__(self, size):
        """Validates size using integer_validator from parent class."""
        self.integer_validator("size", size)

        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """Returns a string representation of square."""
        return "[Square] {}/{}".format(self.__size, self.__size)
