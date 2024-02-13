#!/usr/bin/python3
"""Unittest for Square class"""
import unittest
from models.square import Square
from models.rectangle import Rectangle
from models.base import Base
from unittest.mock import patch
import io
import os
"""Importing unittest, Square and Rectangle modules"""


class TestSquareIniheritance(unittest.TestCase):
    """Tests the square class"""
    def setUp(self):
        """Reset the id attribute to 0 for Base class"""
        Base._Base__nb_objects = 0

    def test_inheritance(self):
        """Check if Square Class is a subclass of Rectangle Class"""
        self.assertTrue(issubclass(Square, Rectangle))


class TestSquareIdInitialization(unittest.TestCase):
    """Test Square Id Initialization"""
    def setUp(self):
        """Reset the id attribute to 0 for Base class"""
        Base._Base__nb_objects = 0

    def test_by_passing_size(self):
        """Passing only heights and width"""
        s = Square(10)
        self.assertEqual(s.id, 1)

        s1 = Square(10, 5)
        self.assertEqual(s1.id, 2)

        s2 = Square(10, 4, 0, 8)
        self.assertEqual(s2.id, 8)
