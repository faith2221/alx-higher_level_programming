#!/usr/bin/python3
"""script that adds all arguments to a Python list."""
import sys
import json


def save_to_json_file(my_obj, filename):
    """The filename is saved."""
    with open(filename, 'w') as file:
        json.dump(my_obj, file)


def load_from_json_file(filename):
    """Creates a object from a JSON file."""
    with open(filename, 'r') as file:
        return json.load(file)


filename = "add_item.json"


try:
    items = load_from_json_file(filename)
except FileNotFoundError:
    items = []

items.extend(sys.argv[1:])
save_to_json_file(items, filename)

print(items)
