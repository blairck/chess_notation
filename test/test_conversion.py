import unittest
from src import conversion

class TestNotationConverter(unittest.TestCase):
    """Tests for NotationConverter class"""
    def test_alg_search_good_input_a5(self):
        """Input with 'a5'"""
        actual_result = main.TileLine('w').line
        expected_result = '       '
        self.assertEqual(actual_result, expected_result)