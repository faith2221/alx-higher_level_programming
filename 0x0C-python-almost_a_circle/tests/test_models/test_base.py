#!/usr/bin/python3
""" Module for the base case."""
import unittest
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle
from io import StringIO
from unittest import TestCase
from unittest.mock import patch


class TestBaseMethods(unittest.TestCase):
    """Suite to test Base Class"""

    def setUp(self):
        """Method invoked for each test"""
        Base._Base__nb_objects = 0

    def test_id(self):
        """Test assigned id which checks if an id is correctly assigned."""
        new = Base(1)
        self.assertEqual(new.id, 1)

    def test_id_default(self):
        """Test default id which  verifies that the default ID."""
        new = Base()
        self.assertEqual(new.id, 1)

    def test_id_nb_objects(self):
        """Test id_nb_objects."""
        new = Base()
        new2 = Base()
        new3 = Base()
        self.assertEqual(new.id, 1)
        self.assertEqual(new2.id, 2)
        self.assertEqual(new3.id, 3)

    def test_id_mix(self):
        """Test id_mix."""
        new = Base()
        new2 = Base(1024)
        new3 = Base()
        self.assertEqual(new.id, 1)
        self.assertEqual(new2.id, 1024)
        self.asserEqual(new3.id, 2)

    def test_string_id(self):
        """Test string_id."""
        new = Base('1')
        self.assertEqual(new.id, '1')

    def test_more_args_id(self):
        """Test more_args_id."""
        with self.assertRaise(TypeError):
            new = base(1, 1)

    def test_access_private_attrs(self):
        """Test to access_private_attrs."""
        new = Base()
        with self.assertRaise(AttributeError):
            new.__nb_objects

    def test_save_to_file(self):
        """Test to save_to_file_2."""
        Square.save_to_file(None)
        result = "[]\n"
        with open("Square.json", "r") as file:
            with patch('sys.stdout', new=StringIO()) as str_out:
                print(file.read())
                self.assertEqual(str_out.getvalue(), result)
        try:
            os.remove("Square.json")
        except Exception:
            pass

        Square.save_to_file([])
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_save_to_file_2(self):
        """Test to save_to_file_1."""
        Rectangle.save_to_file(None)
        result = "[]\n"
        with open("Rectangle.json", "r") as file:
            with patch('sys.stdout', new=StringIO()) as str_out:
                print(file.read())
                self.assertEqual(str_out.getvalue(), result)
        try:
            os.remove("Rectangle.json")
        except Exception:
            pass

        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")
