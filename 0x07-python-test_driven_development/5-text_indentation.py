#!/usr/bin/python3
"""Defines the text_indentation."""


def text_indentation(text):
    """Prints text with two new lines after each '.', '?', and ':'."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    res = ""
    newline = True

    for c in text:
        if newline and c == ' ':
            continue
        elif c in ['.', '?', ':']:
            res += c + '\n\n'
            newline = True
        else:
            res += c
            newline = False

    print(res)
