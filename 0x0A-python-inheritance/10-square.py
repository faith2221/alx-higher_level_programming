#!/usr/bin/python3
"""Defines class Square that inherits from Rectangle (9-rectangle.py)."""
Rectangle = __import__(9-rectangle.py).Rectangle


class Square(Rectangle):
    """Implements a square from a rectangle."""
    def __init__(self, size):
        """Initializes size of square."""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
