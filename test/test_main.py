import unittest
from src import main

class TestTileLine(unittest.TestCase):
	def test_white_input(self):
		result = main.TileLine('w').line
		self.assertEqual(result,'       ')

	def test_black_input(self):
		result = main.TileLine('b').line
		self.assertEqual(result,"|||||||")