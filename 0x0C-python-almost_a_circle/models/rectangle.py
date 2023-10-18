#!/usr/bin/python3
"""Defines a child class called Rectangle."""
from models.base import Base


class Rectangle(Base):
    """Rectangle class that inherits from base."""
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Constructor for the rectangle class.

        Args:
            width (int) : The width of the rectangle.
            height (int): The height of the rectangle.
            x (int): The x-coordinate of the rectangle's position.
            y (int): The y-coordinate of the rectangle's position.
            id (int): The unique identifier of the rectangle.

        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
