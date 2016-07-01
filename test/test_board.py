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

class TestStaticFunctions(unittest.TestCase):
    """Tests for static function helpers for board"""
    def test_identify_random_square(self):
        actual_result_x, actual_result_y = board.identify_random_square()
        expected_result_compare = 0
        self.assertTrue(actual_result_x >= expected_result_compare)
        self.assertTrue(actual_result_y >= expected_result_compare)

class TestBoard(unittest.TestCase):
    """Tests for Board class"""
    @classmethod
    def setUpClass(cls):
        # Shared board description for tests where this required arg
        # isn't important to the result
        cls.shared_description = ["rnbqkbnr",
                                  "pppppppp",
                                  "        ",
                                  "        ",
                                  "        ",
                                  "        ",
                                  "PPPPPPPP",
                                  "RNBQKBNR",]

    maxDiff = None
    def test_board(self):
        """Make board with default args"""
        description = self.shared_description
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
        description = self.shared_description
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

    def test_highlight_square_boundaries(self):
        """Make sure we highlight_square gives ValueError for out of bounds
        coordinates"""
        description = self.shared_description
        the_board = board.Board(description, orientation=False)
        self.assertRaises(ValueError, the_board.highlight_square, 0, 2)
        self.assertRaises(ValueError, the_board.highlight_square, 10, 2)
        self.assertRaises(ValueError, the_board.highlight_square, 1, 0)
        self.assertRaises(ValueError, the_board.highlight_square, 4, 9)

    def test_highlight_square_bad(self):
        """Make sure we highlight_square gives TypeError for bad coordinates"""
        description = self.shared_description
        the_board = board.Board(description, orientation=False)
        self.assertRaises(TypeError, the_board.highlight_square, 'sz', 2)
        self.assertRaises(TypeError, the_board.highlight_square, 4, 'qq')
        self.assertRaises(TypeError, the_board.highlight_square, 'ab', 'cd')

    def test_highlight_square_good(self):
        description = ["rnbqkbnr",
                       "pppppppp",
                       "        ",
                       "        ",
                       "        ",
                       "        ",
                       "PPPPPPPP",
                       "RNBQKBNR",]
        the_board = board.Board(description, orientation=True)
        the_board.highlight_square(2, 3)
        the_board.update_board_string()
        actual_result = str(the_board)
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
|||||||   @   |||||||       |||||||       |||||||       
|||||||       |||||||       |||||||       |||||||       
       |||||||       |||||||       |||||||       |||||||
   P   || P ||   P   || P ||   P   || P ||   P   || P ||
       |||||||       |||||||       |||||||       |||||||
|||||||       |||||||       |||||||       |||||||       
|| R ||   N   || B ||   Q   || K ||   B   || N ||   R   
|||||||       |||||||       |||||||       |||||||       
"""
        self.assertEqual(actual_result, expected_result)

    def test_highlight_square_reversed(self):
        description = ["rnbqkbnr",
                       "pppppppp",
                       "        ",
                       "        ",
                       "        ",
                       "        ",
                       "PPPPPPPP",
                       "RNBQKBNR",]
        the_board = board.Board(description, orientation=False)
        the_board.highlight_square(2, 3)
        the_board.update_board_string()
        actual_result = str(the_board)
        expected_result = """
       |||||||       |||||||       |||||||       |||||||
   R   || N ||   B   || Q ||   K   || B ||   N   || R ||
       |||||||       |||||||       |||||||       |||||||
|||||||       |||||||       |||||||       |||||||       
|| P ||   P   || P ||   P   || P ||   P   || P ||   P   
|||||||       |||||||       |||||||       |||||||       
       |||||||       |||||||       |||||||       |||||||
       |||||||       |||||||       |||||||   @   |||||||
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

    def test_highlight_rowline_good(self):
        description = self.shared_description
        the_board = board.Board(description)
        actual_result = the_board.highlight_rowline("rnbqkbnr", 2)
        expected_result = 'rn@qkbnr'
        self.assertEqual(actual_result, expected_result)

    def test_highlight_rowline_bad_index(self):
        description = self.shared_description
        the_board = board.Board(description)
        self.assertRaises(IndexError,
                          the_board.highlight_rowline,
                          "rnbqkbnr",
                          25)

    def test_highlight_rowline_bad_row(self):
        description = self.shared_description
        the_board = board.Board(description)
        self.assertRaises(TypeError, the_board.highlight_rowline, 5, 2)

    def test_grab_y_index_orientation_true(self):
        description = self.shared_description
        the_board = board.Board(description)
        actual_result = the_board.grab_y_index(5)
        expected_result = 3
        self.assertEqual(actual_result, expected_result)

    def test_grab_y_index_orientation_false(self):
        description = self.shared_description
        the_board = board.Board(description, orientation=False)
        actual_result = the_board.grab_y_index(7)
        expected_result = 6
        self.assertEqual(actual_result, expected_result)

    def test_grab_y_index_bad_coordinates(self):
        description = self.shared_description
        the_board = board.Board(description)
        self.assertRaises(ValueError, the_board.grab_y_index, 10)
        self.assertRaises(ValueError, the_board.grab_y_index, 0)
        self.assertRaises(TypeError, the_board.grab_y_index, "abc")
        self.assertRaises(TypeError, the_board.grab_y_index, None)

    def test_grab_x_index_orientation_true(self):
        description = self.shared_description
        the_board = board.Board(description)
        actual_result = the_board.grab_x_index(5)
        expected_result = 4
        self.assertEqual(actual_result, expected_result)

    def test_grab_x_index_orientation_false(self):
        description = self.shared_description
        the_board = board.Board(description, orientation=False)
        actual_result = the_board.grab_x_index(7)
        expected_result = 1
        self.assertEqual(actual_result, expected_result)

    def test_grab_x_index_bad_coordinates(self):
        description = self.shared_description
        the_board = board.Board(description)
        self.assertRaises(ValueError, the_board.grab_x_index, 10)
        self.assertRaises(ValueError, the_board.grab_x_index, 0)
        self.assertRaises(TypeError, the_board.grab_x_index, "abc")
        self.assertRaises(TypeError, the_board.grab_x_index, None)

    def test_board_description_not_list(self):
        description = ("test string in a tuple")
        self.assertRaises(TypeError, board.Board, description)
