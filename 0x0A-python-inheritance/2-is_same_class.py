#!/usr/bin/python3
"""Defines is_same_class that takes two arguments."""


def is_same_class(obj, a_class):
    """
    uses the built-in 'type()' function to get the type of object 'obj'
    and compares it with the specified class 'a_class'.

    """

    return True if type(obj) is a_class else False
