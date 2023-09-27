#!/usr/bin/python3
"""Defines a square by size and position."""


class Square:
    """Defines a square."""
    def __init__(self, size=0, position=(0, 0)):
        """Initializes a new square."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieves and returns the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size and raises TypeError and ValueError if needed."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >=0")
        self.__size = value

    @property
    def position(self):
        """Retrieves and returns the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position and raises TypeError if needed."""
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers.")
        if not all(isinstance(i, int) and i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers.")
        self.__position = value

    def area(self):
        """Computes and returns the area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Prints the square with the character '#' using position."""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + '#' * self.__size)

    def __str__(self):
        """String representation of the queue."""
        res = []
        if self.__size == 0:
            return ""

        for _ in range(self.__position[1]):
            res.append("")
        for _ in range(self.__size):
            res.append(" " * self.__position[0] + '#' * self.__size)
        return "\n".join(res)
