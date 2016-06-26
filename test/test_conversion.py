"""Tests for conversion module"""

import unittest
from src import conversion

class TestStaticConversion(unittest.TestCase):
    def test_coordinate_to_alg_1_1(self):
        """Input with (1,1)"""
        actual_result = conversion.coordinate_to_alg(1, 1)
        expected_result = 'a1'
        self.assertEqual(actual_result, expected_result)

    def test_coordinate_to_alg_5_3(self):
        """Input with (5,3)"""
        actual_result = conversion.coordinate_to_alg(5, 3)
        expected_result = 'e3'
        self.assertEqual(actual_result, expected_result)

    def test_coordinate_to_alg_boundaries(self):
        """Make sure we coordinate_to_alg gives ValueError for out of bounds
        coordinates"""
        self.assertRaises(ValueError, conversion.coordinate_to_alg, 0, 2)
        self.assertRaises(ValueError, conversion.coordinate_to_alg, 10, 2)
        self.assertRaises(ValueError, conversion.coordinate_to_alg, 1, 0)
        self.assertRaises(ValueError, conversion.coordinate_to_alg, 4, 9)

    def test_coordinate_to_alg_bad(self):
        """Make sure we coordinate_to_alg gives TypeError for bad\
        coordinates"""
        self.assertRaises(TypeError, conversion.coordinate_to_alg, 'sz', 2)
        self.assertRaises(TypeError, conversion.coordinate_to_alg, 4, 'qq')
        self.assertRaises(TypeError, conversion.coordinate_to_alg, 'ab', 'cd')


class TestNotationConverter(unittest.TestCase):
    """Tests for NotationConverter class"""
    def test_alg_search_good_input_a5(self):
        """Input with 'a5'"""
        n_con = conversion.NotationConverter()
        actual_result = n_con.alg_search('a5')
        expected_result = ('a5', 'qr5', 'qr4')
        self.assertEqual(actual_result, expected_result)

    def test_alg_search_good_input_f7(self):
        """Input with 'f7'"""
        n_con = conversion.NotationConverter()
        actual_result = n_con.alg_search('f7')
        expected_result = ('f7', 'kb7', 'kb2')
        self.assertEqual(actual_result, expected_result)

    def test_alg_search_nonexistant(self):
        """Input which does not exist"""
        n_con = conversion.NotationConverter()
        self.assertRaises(KeyError, n_con.alg_search, 'f99')

    def test_desc_search_good_white(self):
        """Input with good value"""
        n_con = conversion.NotationConverter()
        actual_result = n_con.desc_search('qn3', 'white')
        expected_result = ('b3', 'qn3', 'qn6')
        self.assertEqual(actual_result, expected_result)

    def test_desc_search_good_black(self):
        """Input with good value"""
        n_con = conversion.NotationConverter()
        actual_result = n_con.desc_search('qn6', 'black')
        expected_result = ('b3', 'qn3', 'qn6')
        self.assertEqual(actual_result, expected_result)

    def test_desc_search_nonexistant(self):
        """Input with nonexistant value"""
        n_con = conversion.NotationConverter()
        self.assertRaises(KeyError, n_con.desc_search, 'qn333', 'white')

    def test_desc_search_bad_color(self):
        """Input with wrong color"""
        n_con = conversion.NotationConverter()
        self.assertRaises(ValueError, n_con.desc_search, 'qn3', 'green')

    def test_alg_to_desc_good_black(self):
        """Input with good value"""
        n_con = conversion.NotationConverter()
        actual_result = n_con.alg_to_desc('b3', 'black')
        expected_result = 'qn6'
        self.assertEqual(actual_result, expected_result)

    def test_alg_to_desc_good_white(self):
        """Input with good value"""
        n_con = conversion.NotationConverter()
        actual_result = n_con.alg_to_desc('e5', 'white')
        expected_result = 'k5'
        self.assertEqual(actual_result, expected_result)

    def test_alg_to_desc_nonexistant(self):
        """Input with nonexistant value"""
        n_con = conversion.NotationConverter()
        self.assertRaises(KeyError, n_con.alg_to_desc, 'b999', 'black')

    def test_alg_to_desc_bad_color(self):
        """Input with nonexistant value"""
        n_con = conversion.NotationConverter()
        self.assertRaises(ValueError, n_con.alg_to_desc, 'h2', 'red')

    def test_desc_to_alg_good_black(self):
        """Input with good value"""
        n_con = conversion.NotationConverter()
        actual_result = n_con.desc_to_alg('kb5', 'black')
        expected_result = "f4"
        self.assertEqual(actual_result, expected_result)

    def test_desc_to_alg_good_white(self):
        """Input with good value"""
        n_con = conversion.NotationConverter()
        actual_result = n_con.desc_to_alg('q1', 'white')
        expected_result = "d1"
        self.assertEqual(actual_result, expected_result)

    def test_desc_to_alg_nonexistant(self):
        """Input with nonexistant value"""
        n_con = conversion.NotationConverter()
        self.assertRaises(KeyError, n_con.desc_to_alg, 'kb88', 'white')
