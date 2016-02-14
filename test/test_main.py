"""Tests for main module"""
import unittest
from src import main

class TestTileLine(unittest.TestCase):
    """Tests for TileLine class"""
    def test_white_input(self):
        """Tests input with 'w'"""
        result = main.TileLine('w').line
        self.assertEqual(result, '       ')

    def test_black_input(self):
        """Tests input with 'b'"""
        result = main.TileLine('b').line
        self.assertEqual(result, "|||||||")
