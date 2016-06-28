"""Where player runs the game"""

import random
import time

import board
import conversion
import games
from settings import (NUMBER_OF_TRIALS,
                      RECORD_FILE,
                      SAVE_PROGRESS)

def write_record_to_file(a_string, file_name):
    with open(file_name, 'w') as f:
        f.write(a_string)

def get_record_from_file(file_name):
    with open(file_name, 'r') as f:
        result = f.readline()
    return result

if __name__ == '__main__':
    for i in range(NUMBER_OF_TRIALS):
        # Setup some initial variables
        record_total_time = 0.0
        record_total_trials = 0

        # Display the board
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

        # Display status information
        if SAVE_PROGRESS:
            try:
                # Try to retrieve data from record file
                record = get_record_from_file(RECORD_FILE).split(',')
                record_total_time = float(record[0])
                record_total_trials = int(record[1])
                template = "Average time: {0:.2f}\nTotal seconds: {1:.2f}, \
Total trials: {2}"
                trial_average = record_total_time/float(record_total_trials)
                print(template.format(trial_average, 
                                      record_total_time,
                                      record_total_trials))
            except FileNotFoundError:
                print("No record file found.\n\
Creating a new one after this trial: {0}".format(RECORD_FILE))

        # Ask for input from the user
        ATTEMPT = input('Enter highlighted square, or \'quit\': ')
        end = time.time()
        if ATTEMPT == LOCATION:
            print("CORRECT!!")
        elif ATTEMPT == "quit" or ATTEMPT == "q":
            print("Exiting, current trial will not be saved.")
            break
        else:
            print("Wrong, the answer was {0}".format(LOCATION))
        TRIAL_DURATION = end - start
        print("Attempt took {0:.03f} seconds".format(TRIAL_DURATION))

        # Save results of this trial to record file
        if SAVE_PROGRESS:
            record_total_time = record_total_time + TRIAL_DURATION
            record_total_trials = record_total_trials + 1
            write_record_to_file("{0},{1}".format(record_total_time,
                                                  record_total_trials),
                                 RECORD_FILE)
