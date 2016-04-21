"""Where player runs the game"""

from src import board

if __name__ == '__main__':
    BOARD_DESCRIPTION = ("rnbqkbnr",
                         "pppppppp",
                         "        ",
                         "        ",
                         "        ",
                         "        ",
                         "PPPPPPPP",
                         "RNBQKBNR",)
    BOARD = board.Board(BOARD_DESCRIPTION, orientation=True)
    print(BOARD)
