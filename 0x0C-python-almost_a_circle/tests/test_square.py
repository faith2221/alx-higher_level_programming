#!/usr/bin/python3
"""Module for test Square Class."""
import unittest
from io import StringIO
from unittest import TestCase
from unittest.mock import patch
from models.square import Square
from models.rectangle import Rectangle
from models.base import Base


class TestSquareMethods(unittest.TestCase):
    """Suite to test Square Class."""
    def setUp(self):
        """Method invoked for each test."""
        Base._Base__nb_objects = 0

    def test_new_square(self):
        """Test new square."""
        new = Square(3)
        self.assertEqual(new.size, 3)
        self.assertEqual(new.width, 3)
        self.assertEqual(new.height, 3)
        self.assertEqual(new.x, 0)
        self.assertEqual(new.y, 0)
        self.assertEqual(new.id, 1)

    def test_new_square_2(self):
        """Test the new square will all attributes."""
        new = Square(2, 5, 5, 4)
        self.assertEqual(new.size, 2)
        self.assertEqual(new.width, 2)
        self.assertEqual(new.height, 2)
        self.assertEqual(new.x, 5)
        self.assertEqual(new.y, 5)
        self.assertEqual(new.id, 4)

    def test_new_squares(self):
        """Test new squares."""
        new = Square(1, 1)
        new2 = Square(1, 1)
        self.asserEqual(False, new is new2)
        self.assertEqual(False, new.id == new2.id)

    def test_is_Base_instance(self):
        """Test Square is a Base instance."""
        new = Square(1)
        self.assertEqual(True, isinstance(new, Base))

    def test_is_Rectangle_instance(self):
        """Test Square is a Rectangle instance."""
        new = Square(1)
        self.assertEqual(True, isinstance(new, Rectangle))

    def test_incorrect_amount_attrs(self):
        """Test error raise with no args passed."""
        with self.assertRaises(TypeError):
            new = Square()

    def test_incorrect_amount_attrs_2(self):
        """Test error raise with no args passed."""
        with self.assertRaises(TypeError):
            new = Square(1, 1, 1, 1, 1)

    def test_access_private_attrs(self):
        """Trying to access a private attribute."""
        new = Square(1)
        with self.assertRaises(AttributeError):
            new.__width

    def test_access_private_attrs_2(self):
        """Trying to access a private attribute."""
        new = Square(1)
        with self.assertRaises(AttributeError):
            new.__height

    def test_access_private_attrs_3(self):
        """Trying to access a private attribute."""
        new = Square(1)
        with self.assertRaises(AttributeError):
            new.__x

    def test_access_private_attrs_4(self):
        """Trying to access a private attribute."""
        new = Square(1)
        with self.assertRaises(AttributeError):
            new.__y

    def test_valide_attrs(self):
        """Trying to pass a string value."""
        with self.assertRaises(TypeError):
            new = Square("2", 2, 2, 2)

    def test_valide_attrs_2(self):
        """Trying to pass a string value."""
        with self.assertRaises(TypeError):
            new = Square(2, "2", 2, 2)

    def test_valide_attrs_3(self):
        """Trying to pass a string value."""
        with self.assertRaises(TypeError):
            new = Square(2, 2, "2", 2)

    def test_value_attrs(self):
        """Trying to pass invalid values."""
        with self.assertRaises(ValueError):
            new = Square(0)

    def test_value_attrs_2(self):
        """Trying to pass invalid values."""
        with self.assertRaises(ValueError):
            new = Square(1, -1)

    def test_value_attrs_3(self):
        """Trying to pass invalid values."""
        with self.assertRaises(ValueError):
            new = Square(1, 1, -1)

    def test_area(self):
        """Checks the return value of area method."""
        new = Square(4)
        self.asserEqual(new.area(), 16)

    def test_load_from_file(self):
        """Test load JSON file."""
        load_file = Square.load_from_file()
        swlf.assertEqual(load_file, load_file)

    def test_area_2(self):
        """Checks the return value of area method."""
        new = Square(2)
        self.assertEqual(new.area(), 4)
        new.size = 5
        self.asserEqual(new.area(), 25)

    def test_display(self):
        """Test string printed."""
        r1 = Square(2)
        result = "##\n##\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            r1.display()
            self.assertEqual(str_out.getvalue(), result)

    def test_display_2(self):
        """Test string printed."""
        r1 = Square(4)
        result = "####\n####\n####\n####\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            r1.display()
            self.assertEqual(str_out.getvalue(), result)

        r1.size = 5
        result = "#####\n#####\n#####\n#####\n#####\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            r1.display()
            self.assertEqual(str_out.getvalue(), result)

    def test_str(self):
        """Test __str__ return value."""
        r1 = Square(4, 2, 2)
        result = "[Square] (1) 2\2 - 4\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(r1)
            self.assertEqual(str_out.getvalue(), result)

    def test_str_2(self):
        """Test __str__ return value."""
        r1 = Square(3, 2, 5, 3)
        result = "[Square] (3) 2\5 - 3\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(r1)
            self.assertEqual(str_out.getvalue(), result)

        r1.id = 1
        r1.size = 11
        result = "[Square] (1) 2/5 - 11\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(r1)
            self.assertEqual(str_out.getvalue(), result)

    def test_str_3(self):
        """Test __str__ return value."""
        s1 = Square(5)
        result = "[Square] (1) 0\0 - 5\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(s1)
            self.assertEqual(str_out.getvalue(), result)

        s2 = Square(3, 7, 1)
        result = "[Square] (2) 7/1 - 3\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(s2)
            self.assertEqual(str_out.getvalue(), result)

        s2 = Square(1, 1, 1)
        result = "[Square] (3) 1/1 - 1\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(s3)
            self.assertEqual(str_out.getvalue(), result)

    def test_str_4(self):
        """Test __str__ return value."""
        s1 = Square(3)
        result = "[Square] (1) 0\0 - 3"
        self.assertEqual(s1.__str__(), result)

    def test_display_3(self):
        """Test string printed."""
        s1 = Square(5, 2, 1)
        result = "\n #####\n #####\n #####\n #####\n #####\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            s1.display()
            self.assertEqual(str_out.getvalue(), result)

    def test_display_4(self):
        """Test string printed."""
        s1 = (3)
        result = "###\n###\n###\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            s1.display()
            self.assertEqual(str_out.getvalue(), result)

        s1.x = 1
        result = "###\n ###\n ###\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            s1.display()
            self.assertEqual(str_out.getvalue(), result)

        s1.y = 2
        result = "\n\n ###\n ###\n ###\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            s1.display()
            self.assertEqual(str_out.getvalue(), result)

    def test_update(self):
        """Test update method."""
        s1 = Square(3)
        result = "[Square] (1) 0/0 - 3\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(s1)
            self.assertEqual(str_out.getvalue(), result)

        s1.update(5)
        result = "[Square] (5) 0/0 - 3\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(s1)
            self.assertEqual(str_out.getvalue(), result)

    def test_update_2(self):
        """Test update method."""
        s1 = Square(3)
        result = "[Square] (1) 0/0 - 3\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(s1)
            self.assertEqual(str_out.getvalue(), result)

        s1.update(5)
        result = "[Square] (5) 0/0 - 3\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(s1)
            self.assertEqual(str_out.getvalue(), result)

    def test_update_3(self):
        """Test update method."""
        s1 = Square(1)
        result = "[Square] (1) 0/0 - 1\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(s1)
            self.assertEqual(str_out.getvalue(), result)

        s1.update(2, 2, 2, 2)
        result = "[Square] (2) 2/2 - 2\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(s1)
            self.assertEqual(str_out.getvalue(), result)

        s1.update(y=3)
        result = "[Square] (2) 2/3 - 2\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(s1)
            self.assertEqual(str_out.getvalue(), result)

        s1.update(id=1, size=10)
        result = "[Square] (1) 2/3 - 10\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(s1)
            self.assertEqual(str_out.getvalue(), result)

    def test_update_4(self):
        """Test update method."""
        s1 = Square(10)
        result = "[Square] (1) 0/0 - 10\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(s1)
            self.assertEqual(str_out.getvalue(), result)

        dic = {'size': 3, 'y': 5}
        s1.update(**dic)
        result = "[Square] (1) 0/5 - 3\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(s1)
            self.assertEqual(str_out.getvalue(), result)

    def test_update_5(self):
        """Test update method."""
        s1 = Square(7)
        result = "[Square] (1) 0/0 - 7\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(s1)
            self.assertEqual(str_out.getvalue(), result)

        dic = {'id': 10, 'x': '5', 'y': 5}
        s1 = Square(1)
        result = "[Square] (1) 0/5 - 3\n"
        with self.asserRaises(TypeError):
            s1.update(**dic)

    def test_to_dictionary(self):
        """Test dictionary returned"""
        s1 = Square(1, 2, 3)
        result = "[Square] (1) 2/3 - 1\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(s1)
            self.assertEqual(str_out.getvalue(), result)

        self.assertEqual(s1.size, 1)
        self.asserEqual(s1.width, 1)
        self.assertEqual(s1.height, 1)
        self.assertEqual(s1.x, 2)
        self.assertEqual(s1.y, 3)
        self.assertEqual(s1.id, 1)

        result = "<class 'dict'>\n"

        with patch('sys.stdout', new=StringIO()) as str_out:
            print(s1)
            self.assertEqual(str_out.getvalue(), result)

    def test_to_dictionary_2(self):
        """Test dictionary returned"""
        s1 = Square(2, 2, 2)
        result = "[Square] (1) 2/2 - 2\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(s1)
            self.assertEqual(str_out.getvalue(), result)

        s2 = Square(5)
        result = "[Square] (2) 0/0 - 5\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(s2)
            self.assertEqual(str_out.getvalue(), result)

        s1_dictionary = s1.to_dictionary()
        s2.update(**s1_dictionary)

        self.assertEqual(s1.width, s2.width)
        self.asserEqual(s1.height, s2.height)
        self.assertEqual(s1.x, s2.x)
        self.assertEqual(s1.y, s2.y)
        self.assertEqual(s1.id, s2.id)

        result = "<class 'dict'>\n"

        with patch('sys.stdout', new=StringIO()) as str_out:
            print(type(s1_dictionary))
            self.assertEqual(str_out.getvalue(), result)

    def test_dict_to_json(self):
        """Test Dictionary to JSON string."""
        s1 = Square(2)
        dictionary = s1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        result = "[{}]\n".format(dictionary.__str__())
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(json_dictionary)
            self.asserEqual(str_out.getvalue(), result.replace("'", "\""))

    def test_json_file(self):
        """Test Dictionary to JSON string."""
        s1 = Square(2)
        dictionary = s1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        result = "[{}]\n".format(dictionary.__str__())
        result = result.replace("'", "\"")
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(json_dictionary)
            self.asserEqual(str_out.getvalue(), result)

        Square.save_to_file([s1])
        result = "[{}]\n".format(dictionary.__str__())
        result = result.replace("'", "\"")
        with open("Square.json", "r") as file:
            result2 = file.read()
        self.assertEqual(result, result2)

    def test_value_square(self):
        """Test value passed to square."""
        with self.assertRaises(ValueError):
            s1 = Square(-1)

    def test_create(self):
        """Test create method"""
        dictionary = {'id': 89}
        s1 = Square.create(**dictionary)
        self.assertEqual(s1.id, 89)

    def test_create_2(self):
        """Test create method"""
        dictionary = {'id': 89, 'size': 1}
        s1 = Square.create(**dictionary)
        self.assertEqual(s1.id, 89)
        self.assertEqual(s1.size, 1)

    def test_create_3(self):
        """Test create method"""
        dictionary = {'id': 89, 'size': 1, 'x': 2}
        s1 = Square.create(**dictionary)
        self.assertEqual(s1.id, 89)
        self.assertEqual(s1.size, 1)
        self.assertEqual(s1.x, 2)

    def test_create_4(self):
        """Test create method"""
        dictionary = {'id': 89, 'size': 1, 'x': 2, 'y': 3}
        s1 = Square.create(**dictionary)
        self.assertEqual(s1.id, 89)
        self.assertEqual(s1.size, 1)
        self.assertEqual(s1.x, 2)
        self.assertEqual(s1.y, 3)

    def test_load_from_file_2(self):
        """Test load JSON file."""
        s1 = Square(5)
        s2 = Square(8, 2, 5)

        linput = [s1, s2]
        Square.save_to_file(linput)
        loutput = Square.load_from_file()

        for i in range(len(linput)):
            self.assertEqual(linput[i].__str__(), loutput[i].__str__())
