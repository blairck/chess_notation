"""Tests for board module"""
import unittest
from src import board

class TestTileLine(unittest.TestCase):
    """Tests for TileLine class"""
    def test_white_color(self):
        """Input with 'w'"""
        actual_result = board.TileLine('w').line
        expected_result = '       '
        self.assertEqual(actual_result, expected_result)

    def test_black_color(self):
        """Input with 'b'"""
        actual_result = board.TileLine('b').line
        expected_result = "|||||||"
        self.assertEqual(actual_result, expected_result)

    def test_nonexistant_color(self):
        """Input with 'z' raises error"""
        self.assertRaises(ValueError, board.TileLine, 'z')

    def test_black_with_piece(self):
        """Black line with piece"""
        actual_result = board.TileLine('b', 'K').line
        expected_result = "|| K ||"
        self.assertEqual(actual_result, expected_result)

    def test_white_with_piece(self):
        """White line with piece"""
        actual_result = board.TileLine('w', 'K').line
        expected_result = "   K   "
        self.assertEqual(actual_result, expected_result)

class TestRowLine(unittest.TestCase):
    """Tests for RowLine class"""
    def test_odd_row(self):
        """Test odd row without pieces"""
        actual_result = board.RowLine("odd").row
        expected_result = '|||||||       |||||||       |||||||       |||||||\
       '
        self.assertEqual(actual_result, expected_result)

    def test_even_row(self):
        """Test even row without pieces"""
        actual_result = board.RowLine("even").row
        expected_result = '       |||||||       |||||||       |||||||       \
|||||||'
        self.assertEqual(actual_result, expected_result)

    def test_odd_row_pieces(self):
        """Test odd row with pieces"""
        pieces = "RNBQKBNR"
        actual_result = board.RowLine("odd", pieces).row
        expected_result = '|| R ||   N   || B ||   Q   || K ||   B   || N ||\
   R   '
        self.assertEqual(actual_result, expected_result)

    def test_even_row_pieces(self):
        """Test even row with pieces"""
        pieces = "RNBQKBNR"
        actual_result = board.RowLine("even", pieces).row
        expected_result = '   R   || N ||   B   || Q ||   K   || B ||   N   \
|| R ||'
        self.assertEqual(actual_result, expected_result)

    def test_make_row_pieces_exception(self):
        """Tests that make_row_pieces rejects invalid parity"""
        parity_value = "bad_parity"
        pieces_value = "RNBQKBNR"
        board_result = board.RowLine("even", pieces_value)
        self.assertRaises(ValueError,
                          board_result.make_row_pieces,
                          parity_value,
                          pieces_value)

    def test_make_row_exception(self):
        """Tests that make_row rejects invalid parity"""
        parity_value = "bad_parity"
        pieces_value = "RNBQKBNR"
        board_result = board.RowLine("even", pieces_value)
        self.assertRaises(ValueError,
                          board_result.make_row,
                          parity_value)

class TestRowTiles(unittest.TestCase):
    """Tests for RowTiles class"""
    def test_rowtiles(self):
        """For RowTiles class"""
        pieces = "RNBQKBNR"
        actual_result = board.RowTiles("odd", pieces).row_tiles
        expected_result = \
'\n|||||||       |||||||       |||||||       |||||||       \
\n|| R ||   N   || B ||   Q   || K ||   B   || N ||   R   \
\n|||||||       |||||||       |||||||       |||||||       '
        self.assertEqual(actual_result, expected_result)

class TestBoard(unittest.TestCase):
    """Tests for Board class"""
    @classmethod
    def setUpClass(cls):
        # Shared board description for tests where this required arg
        # isn't important to the result
        cls.shared_description = ("rnbqkbnr",
                                  "pppppppp",
                                  "        ",
                                  "        ",
                                  "        ",
                                  "        ",
                                  "PPPPPPPP",
                                  "RNBQKBNR",)

    maxDiff = None
    def test_board(self):
        """Make board with default args"""
        description = ("rnbqkbnr",
                       "pppppppp",
                       "        ",
                       "        ",
                       "        ",
                       "        ",
                       "PPPPPPPP",
                       "RNBQKBNR",)
        actual_result = str(board.Board(description, orientation=True))
        expected_result = """
       |||||||       |||||||       |||||||       |||||||
   r   || n ||   b   || q ||   k   || b ||   n   || r ||
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
|| R ||   N   || B ||   Q   || K ||   B   || N ||   R   
|||||||       |||||||       |||||||       |||||||       
"""
        self.assertEqual(actual_result, expected_result)

    def test_board_reversed(self):
        """Make board with reverse orientation"""
        description = ("rnbqkbnr",
                       "pppppppp",
                       "        ",
                       "        ",
                       "        ",
                       "        ",
                       "PPPPPPPP",
                       "RNBQKBNR",)
        actual_result = str(board.Board(description, orientation=False))
        expected_result = """
       |||||||       |||||||       |||||||       |||||||
   R   || N ||   B   || Q ||   K   || B ||   N   || R ||
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
|| r ||   n   || b ||   q   || k ||   b   || n ||   r   
|||||||       |||||||       |||||||       |||||||       
"""
        self.assertEqual(actual_result, expected_result)

    def test_identify_random_square_good(self):
        description = self.shared_description
        actual_result = board.Board(description).identify_random_square()
        actual_result_x = actual_result[0]
        actual_result_y = actual_result[1]
        expected_result_compare = 0
        self.assertTrue(actual_result_x >= expected_result_compare)
        self.assertTrue(actual_result_y >= expected_result_compare)
