"""Tests for the GamePositions class"""


import unittest
from src import games

class TestGamePositions(unittest.TestCase):
    """Tests for the GamePositions"""
    def test_random_game_specific(self):
        """Tests for specific result"""
        g_pos = games.GamePositions()
        actual_result = g_pos.random_game(1)
        expected_result = ("  r  rk ",
                           "pp   pp ",
                           "    bb p",
                           "q  p P Q",
                           "   P    ",
                           "  N     ",
                           "PP    PP",
                           " K R B R",)
        self.assertEqual(actual_result, expected_result)

    def test_random_game_rand_output(self):
        """Tests for random result (happy path)"""
        g_pos = games.GamePositions()
        actual_result = g_pos.random_game()
        expected_result = 8
        self.assertEqual(len(actual_result), expected_result)
