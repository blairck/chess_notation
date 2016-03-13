"""Tests for main module"""
import unittest
from src import main

class TestTileLine(unittest.TestCase):
    """Tests for TileLine class"""
    def test_white_color(self):
        """Input with 'w'"""
        result = main.TileLine('w').line
        self.assertEqual(result, '       ')

    def test_black_color(self):
        """Input with 'b'"""
        result = main.TileLine('b').line
        self.assertEqual(result, "|||||||")

    def test_nonexistant_color(self):
        """Input with 'z' raises error"""
        self.assertRaises(ValueError, main.TileLine, 'z')

    def test_black_with_piece(self):
        """Black line with piece"""
        result = main.TileLine('b', 'K').line
        self.assertEqual(result, "|| K ||")

    def test_white_with_piece(self):
        """White line with piece"""
        result = main.TileLine('w', 'K').line
        self.assertEqual(result, "   K   ")

class TestRowLine(unittest.TestCase):
    """Tests for RowLine class"""
    def test_odd_row(self):
        """Test odd row without pieces"""
        result = main.RowLine("odd").row
        expected = '       |||||||       |||||||       |||||||       |||||||'
        self.assertEqual(result, expected)

    def test_odd_even(self):
        """Test even row without pieces"""
        result = main.RowLine("even").row
        expected = '|||||||       |||||||       |||||||       |||||||       '
        self.assertEqual(result, expected)

    def test_odd_row_pieces(self):
        """Test odd row with pieces"""
        pieces = "RNBQKBNR"
        result = main.RowLine("odd", pieces).row
        expected = '   R   || N ||   B   || Q ||   K   || B ||   N   || R ||'
        self.assertEqual(result, expected)

    def test_even_row_pieces(self):
        """Test even row with pieces"""
        pieces = "RNBQKBNR"
        result = main.RowLine("even", pieces).row
        expected = '|| R ||   N   || B ||   Q   || K ||   B   || N ||   R   '
        self.assertEqual(result, expected)

class TestRowTiles(unittest.TestCase):
    """Tests for RowTiles class"""
    def test_rowtiles(self):
        """For RowTiles class"""
        pieces = "RNBQKBNR"
        result = main.RowTiles("odd", pieces).row_tiles
        expected = '       |||||||       |||||||       |||||||       |||||||\
\n   R   || N ||   B   || Q ||   K   || B ||   N   || R ||\
\n       |||||||       |||||||       |||||||       |||||||'
        self.assertEqual(result, expected)

class TestBoard(unittest.TestCase):
    """Tests for Board class"""
    def test_board(self):
        """Make board with default args"""
        description = ("RNBQKBNR", "PPPPPPPP", None, None,
                       None, None, "pppppppp", "rnbqkbnr")
        result = str(main.Board(description, orientation=True))
        expected = """
       |||||||       |||||||       |||||||       |||||||
   R   || N ||   B   || K ||   Q   || B ||   N   || R ||
       |||||||       |||||||       |||||||       |||||||
|||||||       |||||||       |||||||       |||||||       
|| P ||   P   || P ||   P   || P ||   P   || P ||   P   
|||||||       |||||||       |||||||       |||||||       
       |||||||       |||||||       |||||||       |||||||
       |||||||       |||||||       |||||||       |||||||
       |||||||       |||||||       |||||||       |||||||
|||||||       |||||||       |||||||       |||||||       
|||||||       |||||||       |||||||       |||||||       
|||||||       |||||||       |||||||       |||||||       
       |||||||       |||||||       |||||||       |||||||
       |||||||       |||||||       |||||||       |||||||
       |||||||       |||||||       |||||||       |||||||
|||||||       |||||||       |||||||       |||||||       
|||||||       |||||||       |||||||       |||||||       
|||||||       |||||||       |||||||       |||||||       
       |||||||       |||||||       |||||||       |||||||
   p   || p ||   p   || p ||   p   || p ||   p   || p ||
       |||||||       |||||||       |||||||       |||||||
|||||||       |||||||       |||||||       |||||||       
|| r ||   n   || b ||   k   || q ||   b   || n ||   r   
|||||||       |||||||       |||||||       |||||||       
"""
        self.assertEqual(result, expected)

    def test_board_reversed(self):
        """Make board with reverse orientation"""
        description = ("RNBQKBNR", "PPPPPPPP", None, None,
                       None, None, "pppppppp", "rnbqkbnr")
        result = str(main.Board(description, orientation=False))
        expected = """
       |||||||       |||||||       |||||||       |||||||
   r   || n ||   b   || k ||   q   || b ||   n   || r ||
       |||||||       |||||||       |||||||       |||||||
|||||||       |||||||       |||||||       |||||||       
|| p ||   p   || p ||   p   || p ||   p   || p ||   p   
|||||||       |||||||       |||||||       |||||||       
       |||||||       |||||||       |||||||       |||||||
       |||||||       |||||||       |||||||       |||||||
       |||||||       |||||||       |||||||       |||||||
|||||||       |||||||       |||||||       |||||||       
|||||||       |||||||       |||||||       |||||||       
|||||||       |||||||       |||||||       |||||||       
       |||||||       |||||||       |||||||       |||||||
       |||||||       |||||||       |||||||       |||||||
       |||||||       |||||||       |||||||       |||||||
|||||||       |||||||       |||||||       |||||||       
|||||||       |||||||       |||||||       |||||||       
|||||||       |||||||       |||||||       |||||||       
       |||||||       |||||||       |||||||       |||||||
   P   || P ||   P   || P ||   P   || P ||   P   || P ||
       |||||||       |||||||       |||||||       |||||||
|||||||       |||||||       |||||||       |||||||       
|| R ||   N   || B ||   K   || Q ||   B   || N ||   R   
|||||||       |||||||       |||||||       |||||||       
"""
        self.assertEqual(result, expected)
