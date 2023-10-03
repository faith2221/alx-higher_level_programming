#!/usr/bin/python3
"""Unittest for max_integer([..])."""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_regular_list(self):
        """Test with a regular list of integers"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_reverse_list(self):
        """Test with a reversed list of integers."""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_unsorted_list(self):
        """Test with an unsorted list of integers."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_negative_numbers(self):
        """Test with a list of negative numbers."""
        self.assertEqual(max_integer([1, -3, -4, -2]), -1)

    def test_empty_list(self):
        """Test with an empty list"""
        self.assetIsNone(max_integer([]))

    def test_single_element_list(self):
        """Test with a list containing a single element"""
        self.assertEqual(max_integer([7]), 7)

    def test_floats_in_list(self):
        """Test with a list containing floats"""
        self.assertEqual(max_integer({1.5, 2.7, 3.3]), 3.3)

if __name__ == '__main__':
    unittest.main()
