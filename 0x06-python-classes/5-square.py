#!/usr/bin/python3
"""Defines the square class."""


class Square:
    def __init__(self, size=0):
        """Initializes a new Square Instance."""

        self.size = size

    @property
    def size(self):
        """Retrieves and returns the size of the square."""
        
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
        """Computes and returns the area of the square."""
        
        return self.__size ** 2

    def my_print(self):
        """Prints the square using '#' character."""

        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
