#!/usr/bin/python3
"""Function that inserts a line of text to a file."""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text to a file
    after each line containing a specific string

    """

    lines_to_insert = ""
    with open(filename) as r:
        lines_to_insert += line
        if search_string in line:
            lines_to_insert += new_string
    with open(filename, 'w') as w:
        w.write(lines_to_insert)
