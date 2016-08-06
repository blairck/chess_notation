"""Tests for main module, which rely heavily on Mock"""

import os
import sys
import unittest
import unittest.mock
from unittest.mock import mock_open, MagicMock, patch
from contextlib import contextmanager
from io import StringIO

# pylint: disable=wrong-import-position
# Hacky path nonsense to get src folder on the Python path
SCRIPT_PATH = os.path.dirname(os.path.realpath(sys.argv[0]))
sys.path.append('{0}/../src'.format(SCRIPT_PATH))
import src
from src import main
from src.main import (get_record_from_file,
                      validate_settings,
                      write_record_to_file)

@contextmanager
def captured_output():
    """ Redirects stdout to StringIO so we can inspect Print statements """
    new_out = StringIO()
    old_out = sys.stdout
    try:
        sys.stdout = new_out
        yield sys.stdout
    finally:
        sys.stdout = old_out

class TestMainStaticFunctions(unittest.TestCase):
    """Tests for static function helpers"""
    def test_vs_good(self):
        """Check that validate_settings works correctly"""
        actual_result = validate_settings()
        expected_result = True
        self.assertEqual(actual_result, expected_result)

    def test_vs_bad_notation(self):
        """Check that the validate_settings works with bad notation"""
        with captured_output() as out:
            original_value = src.main.NOTATION
            src.main.NOTATION = "invalid"

            actual_result = validate_settings()
            actual_print = out.getvalue().strip()
            expected_print = ("Configuration error, "
                              "NOTATION has an unexpected value: invalid")

            src.main.NOTATION = original_value
            self.assertFalse(actual_result)
            self.assertEqual(actual_print, expected_print)

    def test_vs_bad_trials(self):
        """Check that the validate_settings works with bad trials"""
        with captured_output() as out:
            original_value = src.main.NUMBER_OF_TRIALS
            src.main.NUMBER_OF_TRIALS = "a string"

            actual_result = validate_settings()
            actual_print = out.getvalue().strip()
            expected_print = ("Configuration error, "
                              "NUMBER_OF_TRIALS is not an int: a string")

            src.main.NUMBER_OF_TRIALS = original_value
            self.assertFalse(actual_result)
            self.assertEqual(actual_print, expected_print)

    def test_vs_bad_orientation(self):
        """Check that the validate_settings works with bad orientation"""
        with captured_output() as out:
            original_value = src.main.ORIENTATION
            src.main.ORIENTATION = "invalid"

            actual_result = validate_settings()
            actual_print = out.getvalue().strip()
            expected_print = ("Configuration error, "
                              "ORIENTATION has an unexpected value: invalid")

            src.main.ORIENTATION = original_value
            self.assertFalse(actual_result)
            self.assertEqual(actual_print, expected_print)

    def test_vs_bad_player_color(self):
        """Check that the validate_settings works with bad player color"""
        with captured_output() as out:
            original_notation = src.main.PLAYER_COLOR
            src.main.PLAYER_COLOR = "invalid"

            actual_result = validate_settings()
            actual_print = out.getvalue().strip()
            expected_print = ("Configuration error, "
                              "PLAYER_COLOR has an unexpected value: invalid")

            src.main.PLAYER_COLOR = original_notation
            self.assertFalse(actual_result)
            self.assertEqual(actual_print, expected_print)

    def test_vs_bad_record_file(self):
        """Check that the validate_settings works with bad record file"""
        with captured_output() as out:
            original_value = src.main.RECORD_FILE
            src.main.RECORD_FILE = 12345

            actual_result = validate_settings()
            actual_print = out.getvalue().strip()
            expected_print = ("Configuration error, "
                              "RECORD_FILE is not a string: 12345")

            src.main.RECORD_FILE = original_value
            self.assertFalse(actual_result)
            self.assertEqual(actual_print, expected_print)

    def test_vs_bad_position(self):
        """Check that the validate_settings works with bad position"""
        with captured_output() as out:
            original_value = src.main.STANDARD_POSITION
            src.main.STANDARD_POSITION = "a string"

            actual_result = validate_settings()
            actual_print = out.getvalue().strip()
            expected_print = ("Configuration error, "
                              "STANDARD_POSITION is not an int (bool): "
                              "a string")

            src.main.STANDARD_POSITION = original_value
            self.assertFalse(actual_result)
            self.assertEqual(actual_print, expected_print)

class TestMain(unittest.TestCase):
    """Tests for Main class"""
    def test_settings(self):
        """Sanity check that the class settings are being assigned"""
        trial = main.Game(record_file="test.txt",
                          save_progress=True,
                          test_mode=True)
        self.assertEqual(trial.trial_duration, 0)
        self.assertEqual(trial.record_total_time, 0.0)
        self.assertEqual(trial.record_total_trials, 0)
        self.assertEqual(trial.record_file, "test.txt")
        self.assertEqual(trial.save_progress, True)
        self.assertEqual(trial.test_mode, True)
        self.assertTrue(trial.x_loc_chess)
        self.assertTrue(trial.y_loc_chess)
        self.assertTrue(trial.location)

    def test_main_no_quit(self):
        """Test main event loop where user doesn't quit"""
        trial = main.Game(record_file="test.txt", save_progress=True)
        trial.display_board = MagicMock(return_value=None)
        trial.display_status_information = MagicMock(return_value=None)
        user_quit = False
        trial.get_user_input = MagicMock(return_value=user_quit)
        trial.record_progress = MagicMock(return_value=None)
        actual_result = trial.main()

        trial.display_board.assert_called_once_with()
        trial.display_status_information.assert_called_once_with()
        trial.get_user_input.assert_called_once_with()
        trial.record_progress.assert_called_once_with()
        self.assertEqual(actual_result, user_quit)

    def test_main_quit(self):
        """Test main event loop where user quits"""
        trial = main.Game(record_file="test.txt", save_progress=True)
        trial.display_board = MagicMock(return_value=None)
        trial.display_status_information = MagicMock(return_value=None)
        user_quit = True
        trial.get_user_input = MagicMock(return_value=user_quit)
        trial.record_progress = MagicMock(return_value=None)
        actual_result = trial.main()

        trial.display_board.assert_called_once_with()
        trial.display_status_information.assert_called_once_with()
        trial.get_user_input.assert_called_once_with()
        trial.record_progress.assert_not_called()
        self.assertEqual(actual_result, user_quit)

    # pylint: disable=no-self-use
    # Mock has its own assert methods, but tests are run by unittest
    # This means we can't use normal unittest "self.assert" methods
    @patch('games.GamePositions.random_game')
    @patch('board.Board')
    def test_display_board(self, board, rand_game):
        """Check that we update the trial game board as expected"""
        board.highlight_square = MagicMock(return_value=None)
        game_position = ["r r   k ",
                         "pp q  Rp",
                         "     pp ",
                         "   p  N ",
                         "      Q ",
                         "        ",
                         "PP   PPP",
                         "  R   K ",]
        rand_game.return_value = game_position
        trial = main.Game(record_file="test.txt", save_progress=True)
        trial.display_board()

        rand_game.assert_called_once_with()
        board.assert_called_once_with(game_position,
                                      orientation=trial.orientation)

    @patch('board.Board.highlight_square')
    @patch('board.Board.update_board_string')
    def test_display_board_methods(self, ub_string, hl_square):
        """Check that Board methods are also used as expected"""
        trial = main.Game(record_file="test.txt", save_progress=True)
        trial.display_board()

        hl_square.assert_called_once_with(trial.x_loc_chess,
                                          trial.y_loc_chess)
        actual_result = ub_string.call_count
        expected_result = 2
        self.assertEqual(actual_result, expected_result)

    def test_record_progress_save(self):
        """Check that game progress is recoreded correctly"""
        main.write_record_to_file = MagicMock(return_value=None)
        trial = main.Game(record_file="test.txt", save_progress=True)
        trial.record_progress()

        main.write_record_to_file.assert_called_once_with('0.0,1', 'test.txt')

    def test_record_progress_dont_save(self):
        """Check that no action is taken if save_progress is False"""
        main.write_record_to_file = MagicMock(return_value=None)
        trial = main.Game(record_file="test.txt", save_progress=False)
        trial.record_progress()

        main.write_record_to_file.assert_not_called()

    def test_display_status_save(self):
        """Check that display_status_information uses right logic when
        save_progress is True"""
        main.get_record_from_file = MagicMock(return_value="305.1,31")
        trial = main.Game(record_file="test.txt", save_progress=True)
        trial.display_status_information()

        main.get_record_from_file.assert_called_once_with(trial.record_file)

    def test_display_status_dont_save(self):
        """Check that no action is taken if save_progress is False"""
        main.get_record_from_file = MagicMock(return_value="305.1,31")
        trial = main.Game(record_file="test.txt", save_progress=False)
        trial.display_status_information()

        main.get_record_from_file.assert_not_called()

    @patch('builtins.input', side_effect=["a1"])
    def test_get_user_input_correct(self, mock_input):
        """Check get_user_input with correct input"""
        trial = main.Game(record_file="test.txt", save_progress=False)
        trial.location = "a1"
        actual_result = trial.get_user_input()
        expected_result = False

        self.assertTrue(mock_input.called)
        self.assertEqual(actual_result, expected_result)

    @patch('builtins.input', side_effect=["quit"])
    def test_get_user_input_quit(self, mock_input):
        """Check get_user_input with user quitting the game"""
        trial = main.Game(record_file="test.txt", save_progress=False)
        actual_result = trial.get_user_input()
        expected_result = True

        self.assertTrue(mock_input.called)
        self.assertEqual(actual_result, expected_result)

    @patch('builtins.input', side_effect=["aasdasdf"])
    def test_get_user_input_unknown(self, mock_input):
        """Check get_user_input with unknown input"""
        trial = main.Game(record_file="test.txt", save_progress=False)
        actual_result = trial.get_user_input()
        expected_result = False

        self.assertTrue(mock_input.called)
        self.assertEqual(actual_result, expected_result)

    def test_get_record_from_file(self):
        """Check get_record_from_file with getting text from file"""
        with patch('builtins.open',
                   mock_open(read_data="foo_bar")) as m_file:
            actual_result = get_record_from_file("fizz")
            expected_result = "foo_bar"
            m_file.assert_called_with('fizz', 'r')
            self.assertEqual(actual_result, expected_result)

    def test_write_record_to_file(self):
        """Check write_record_to_file output to file"""
        with patch('builtins.open',
                   mock_open(read_data="foo_bar")) as m_file:
            write_record_to_file("fake_string", "fake_file")
            m_file.assert_called_with("fake_file", "w")
