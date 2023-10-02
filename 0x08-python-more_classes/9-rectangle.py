#!/usr/bin/python3
"""Defines a class called Rectangle."""


class Rectangle:
    """The defined rectangle class."""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializes private instance attributes __width and __height."""
        type(self).number_of_instances += 1
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
        rect = []
        for x in range(self.__height):
            [rect.append(str(self.print_symbol)) for i in range(self.__width)]
            if x != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self):
        """Returns a string representation of the rectangle for debugging."""
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return rect

    def __del__(self):
        """Prints a farewell message when an instance is deleted in the."""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the bigger rectangle on the area."""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """It creates a new Rectangle instance with width == height == size."""
        return cls(size, size)
