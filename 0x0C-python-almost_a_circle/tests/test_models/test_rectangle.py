#!/usr/bin/python3
"""Module for test Rectangle Class."""
import unittest
from io import StringIO
from unittest import TestCase
from unittest.mock import patch
from models.square import Square
from models.rectangle import Rectangle
from models.base import Base


class TestSquareMethods(unittest.TestCase):
    """Suite to test Rectangle Class."""
    def setUp(self):
        """Method invoked for each test."""
        Base._Base__nb_objects = 0

    def test_new_rectangle(self):
        """Test new rectangle."""
        new = Rectangle(1, 1)
        self.assertEqual(new.width, 1)
        self.assertEqual(new.height, 1)
        self.assertEqual(new.x, 0)
        self.assertEqual(new.y, 0)
        self.assertEqual(new.id, 1)

    def test_new_rectangle__2(self):
        """Test the new rectangle will all attributes."""
        new = Rectangle(2, 3, 5, 5, 4)
        self.assertEqual(new.width, 2)
        self.assertEqual(new.height, 3)
        self.assertEqual(new.x, 5)
        self.assertEqual(new.y, 5)
        self.assertEqual(new.id, 4)

    def test_new_rectangles(self):
        """Test new rectangles."""
        new = Rectangle(1, 1)
        new2 = Rectangle(1, 1)
        self.asserEqual(False, new is new2)
        self.assertEqual(False, new.id == new2.id)

    def test_is_Base_instance(self):
        """Test Rectangle is a Base instance."""
        new = Rectangle(1)
        self.assertEqual(True, isinstance(new, Base))

    def test_incorrect_amount_attrs(self):
        """Test error raise with 1 args passed."""
        with self.assertRaises(TypeError):
            new = Rectangle(1)

    def test_incorrect_amount_attrs_2(self):
        """Test error raise with no args passed."""
        with self.assertRaises(TypeError):
            new = Rectangle()

    def test_access_private_attrs(self):
        """Trying to access a private attribute."""
        new = Rectangle(1, 1)
        with self.assertRaises(AttributeError):
            new.__width

    def test_access_private_attrs_2(self):
        """Trying to access a private attribute."""
        new = Rectangle(1, 1)
        with self.assertRaises(AttributeError):
            new.__height

    def test_access_private_attrs_3(self):
        """Trying to access a private attribute."""
        new = Rectangle(1, 1)
        with self.assertRaises(AttributeError):
            new.__x

    def test_access_private_attrs_4(self):
        """Trying to access a private attribute."""
        new = Rectangle(1, 1)
        with self.assertRaises(AttributeError):
            new.__y

    def test_valide_attrs(self):
        """Trying to pass a string value."""
        with self.assertRaises(TypeError):
            new = Rectangle("2", 2, 2, 2, 2)

    def test_valide_attrs_2(self):
        """Trying to pass a string value."""
        with self.assertRaises(TypeError):
            new = Rectangle(2, "2", 2, 2, 2)

    def test_valide_attrs_3(self):
        """Trying to pass a string value."""
        with self.assertRaises(TypeError):
            new = Rectangle(2, 2, "2", 2, 2)

    def test_valide_attrs_4(self):
        """Trying to pass a string value."""
        with self.assertRaises(TypeError):
            new = Rectangle(2, 2, 2, "2", 2)

    def test_value_attrs(self):
        """Trying to pass invalid values."""
        with self.assertRaises(ValueError):
            new = Rectangle(0, 1)

    def test_value_attrs(self):
        """Trying to pass invalid values."""
        with self.assertRaises(ValueError):
            new = Rectangle(1, 0)

    def test_value_attrs_2(self):
        """Trying to pass invalid values."""
        with self.assertRaises(ValueError):
            new = Rectangle(1, 1, -1)

    def test_value_attrs_3(self):
        """Trying to pass invalid values."""
        with self.assertRaises(ValueError):
            new = Rectangle(1, 1, 1, -1)

    def test_area(self):
        """Checks the return value of area method."""
        new = Rectangle(4, 5)
        self.asserEqual(new.area(), 20)

    def test_area_2(self):
        """Checks the return value of area method."""
        new = Rectangle(2, 2)
        self.asserEqual(new.area(), 4)
        new.width = 5
        self.assertEqual(new.area(), 10)
        new.height = 5
        self.assertEqual(new.area(), 25)

    def test_area_3(self):
        """Checks the return value of area method."""
        new = Rectangle(3, 8)
        self.asserEqual(new.area(), 24)
        new2 = Rectangle(10, 10)
        self.assertEqual(new.area(), 100)

    def test_display(self):
        """Test string printed."""
        r1 = Rectangle(2, 5)
        result = "##\n##\n##\n##\n##\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            r1.display()
            self.assertEqual(str_out.getvalue(), result)

    def test_display_2(self):
        """Test string printed."""
        r1 = Rectangle(2, 2)
        result = "##\n##\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            r1.display()
            self.assertEqual(str_out.getvalue(), result)

        r1.width = 5
        result = "#####\n#####\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            r1.display()
            self.assertEqual(str_out.getvalue(), result)

    def test_str(self):
        """Test __str__ return value."""
        r1 = Rectangle(2, 5, 2, 4)
        result = "[Rectangle] (1) 2\4 - 2/5\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(r1)
            self.assertEqual(str_out.getvalue(), result)

    def test_str_2(self):
        """Test __str__ return value."""
        r1 = Rectangle(3, 2, 8, 8, 10)
        result = "[Rectangle] (10) 8/8 - 7/15\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(r1)
            self.assertEqual(str_out.getvalue(), result)

        r1.id = 1
        r1.width = 7
        r1.height = 15
        result = "[Square] (1) 8/8 - 7/15\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(r1)
            self.assertEqual(str_out.getvalue(), result)

    def test_str_3(self):
        """Test __str__ return value."""
        r1 = Rectangle(5, 10)
        result = "[Rectangle] (1) 0\0 - 5/10\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(r1)
            self.assertEqual(str_out.getvalue(), result)

        r2 = Rectangle(25, 86, 4, 7)
        result = "[Rectangle] (2) 4/7 - 25/86\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(s2)
            self.assertEqual(str_out.getvalue(), result)

        r3 = Rectangle(1, 1, 1, 1)
        result = "[Rectangle] (3) 1/1 - 1/1\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(r3)
            self.assertEqual(str_out.getvalue(), result)

    def test_str_4(self):
        """Test __str__ return value."""
        r1 = Rectangle(3, 3)
        result = "[Square] (1) 0\0 - 3/3"
        self.assertEqual(s1.__str__(), result)

    def test_display_3(self):
        """Test string printed."""
        r1 = Square(5, 4, 1, 1)
        result = "\n #####\n #####\n #####\n #####\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            r1.display()
            self.assertEqual(str_out.getvalue(), result)

    def test_display_4(self):
        """Test string printed."""
        r1 = (3, 2)
        result = "###\n###\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            r1.display()
            self.assertEqual(str_out.getvalue(), result)

        r1.x = 4
        result = "    ####\n    ####\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            r1.display()
            self.assertEqual(str_out.getvalue(), result)

        r1.y = 2
        result = "\n\n     ###\n    ###\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            r1.display()
            self.assertEqual(str_out.getvalue(), result)

    def test_to_dictionary(self):
        """Test dictionary returned"""
        r1 = Rectangle(1, 2, 3, 4, 1)
        result = "[Rectangle] (1) 3/4 - 1/2\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(r1)
            self.assertEqual(str_out.getvalue(), result)

        self.asserEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 4)
        self.assertEqual(r1.id, 1)

        result = "<class 'dict'>\n"

        with patch('sys.stdout', new=StringIO()) as str_out:
            print(r1)
            self.assertEqual(str_out.getvalue(), result)

    def test_to_dictionary_2(self):
        """Test dictionary returned"""
        r1 = Rectangle(2, 2, 2, 2)
        result = "[Rectangle] (1) 2/2 - 2/2\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(r1)
            self.assertEqual(str_out.getvalue(), result)

        r2 = Square(5, 7)
        result = "[Rectangle] (2) 0/0 - 5/7\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(r2)
            self.assertEqual(str_out.getvalue(), result)

        r1_dictionary = r1.to_dictionary()
        r2.update(**r1_dictionary)

        self.assertEqual(r1.width, r2.width)
        self.asserEqual(r1.height, r2.height)
        self.assertEqual(r1.x, r2.x)
        self.assertEqual(r1.y, r2.y)
        self.assertEqual(r1.id, r2.id)

        result = "<class 'dict'>\n"

        with patch('sys.stdout', new=StringIO()) as str_out:
            print(type(r1_dictionary))
            self.assertEqual(str_out.getvalue(), result)

    def test_dict_to_json(self):
        """Test Dictionary to JSON string."""
        r1 = Rectangle(2, 2)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        result = "[{}]\n".format(dictionary.__str__())
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(json_dictionary)
            self.asserEqual(str_out.getvalue(), result.replace("'", "\""))

    def test_check_value(self):
        """Test value passed to square."""
        with self.assertRaises(ValueError):
            r1 = Rectangle(-1, 2)

    def test_check_value_2(self):
        """Test value passed to square."""
        with self.assertRaises(ValueError):
            r1 = Rectangle(-1, 2)

    def test_create(self):
        """Test create method"""
        dictionary = {'id': 89}
        s1 = Rectangle.create(**dictionary)
        self.assertEqual(r1.id, 89)

    def test_create_2(self):
        """Test create method"""
        dictionary = {'id': 89, 'width': 1}
        r1 = Rectangle.create(**dictionary)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 1)

    def test_create_3(self):
        """Test create method"""
        dictionary = {'id': 89, 'width': 1, 'height': 2}
        r1 = Rectangle.create(**dictionary)
        self.assertEqual(s1.id, 89)
        self.assertEqual(s1.width, 1)
        self.assertEqual(s1.height, 2)

    def test_create_4(self):
        """Test create method"""
        dictionary = {'id': 89, 'width': 1, 'height': 2, 'x': 3}
        r1 = Rectangle.create(**dictionary)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 3)

    def test_create_5(self):
        """Test create method"""
        dictionary = {'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4}
        r1 = Rectangle.create(**dictionary)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 4)

    def test_load_from_file_2(self):
        """Test load JSON file."""
        load_file = Rectangle.load_from_file()
        self.asserEqual(load_file, [])

    def test_load_from_file_2(self):
        """Test load JSON file."""
        r1 = Rectangle(5, 5)
        r2 = Rectangle(8, 2, 5, 5)

        linput = [r1, r2]
        Rectangle.save_to_file(linput)
        loutput = Rectangle.load_from_file()

        for i in range(len(linput)):
            self.assertEqual(linput[i].__str__(), loutput[i].__str__())
