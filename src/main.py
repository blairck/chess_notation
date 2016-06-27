"""Where player runs the game"""

import random
import time

import board
import conversion
import games
from settings import RECORD_FILE

def write_record_to_file(a_string, file_name):
    with open(file_name, 'w') as f:
        f.write(a_string)

def get_record_from_file(file_name):
    with open(file_name, 'r') as f:
        result = f.readline()
    return result

if __name__ == '__main__':
    NUMBER_OF_TRIALS = 1
    for i in range(NUMBER_OF_TRIALS):
        X_LOC_CHESS, Y_LOC_CHESS = board.identify_random_square()
        LOCATION = conversion.coordinate_to_alg(X_LOC_CHESS, Y_LOC_CHESS)
        ORIENTATIONS = (True, False)
        GAMES = games.GamePositions()
        BOARD_DESCRIPTION = GAMES.random_game()
        BOARD = board.Board(BOARD_DESCRIPTION,
                            orientation=random.choice(ORIENTATIONS))
        BOARD.highlight_square(X_LOC_CHESS, Y_LOC_CHESS)
        BOARD.update_board_string()
        print(BOARD)
        start = time.time()
        ATTEMPT = input('Enter highlighted square: ')
        end = time.time()
        if ATTEMPT == LOCATION:
            print("Correct!")
        else:
            print("Wrong, the answer was {0}".format(LOCATION))
        print("Attempt took {0} seconds".format(end - start))
