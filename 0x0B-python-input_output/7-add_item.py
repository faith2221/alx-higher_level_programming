#!/usr/bin/python3
"""script that adds all arguments to a Python list."""
import sys
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file


filename = "add_item_json"
try:
    counts = load_from_json_file(filename)
except FileNotFoundError:
    counts = []
counts.extend(sys.argv[1:])
save_to_json_file(counts, filename)
