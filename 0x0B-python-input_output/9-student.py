#!/usr/bin/python3
"""Deffines a student class."""


class Student:
    """Representation of a Student instance."""
    def __init__(self, first_name, last_name, age):
        """Initializes a new student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """A dictionary representation of the student."""
        return self.__dict__
