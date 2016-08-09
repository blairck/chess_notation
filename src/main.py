"""Where player runs the game"""

import random
import time

import board
import conversion
import games
from settings import (NOTATION,
                      NUMBER_OF_TRIALS,
                      ORIENTATION,
                      PLAYER_COLOR,
                      RECORD_FILE,
                      SAVE_PROGRESS,
                      STANDARD_POSITION)

# Static helper functions
def write_record_to_file(a_string, file_name):
    """Write one line string to file_name. Always overwrites"""
    with open(file_name, 'w') as record_file:
        record_file.write(a_string)

def get_record_from_file(file_name):
    """Get first (and only) line back from file_name and return it"""
    with open(file_name, 'r') as record_file:
        result = record_file.readline()
    return result

def validate_settings():
    """ Sanity check on the settings. Returns True if okay, False otherwise.
    If multiple settings are wrong, we bail out after the first."""
    result = True
    if NOTATION not in ("alg", "desc"):
        message = "Configuration error, NOTATION has an unexpected value: {0}"
        print(message.format(NOTATION))
        result = False
    elif not isinstance(NUMBER_OF_TRIALS, int):
        message = "Configuration error, NUMBER_OF_TRIALS is not an int: {0}"
        print(message.format(NUMBER_OF_TRIALS))
        result = False
    elif ORIENTATION not in ("white", "black", "random"):
        message = ("Configuration error, "
                   "ORIENTATION has an unexpected value: {0}")
        print(message.format(ORIENTATION))
        result = False
    elif PLAYER_COLOR not in ("white", "black", "random"):
        message = ("Configuration error, "
                   "PLAYER_COLOR has an unexpected value: {0}")
        print(message.format(PLAYER_COLOR))
        result = False
    elif not isinstance(RECORD_FILE, str):
        message = "Configuration error, RECORD_FILE is not a string: {0}"
        print(message.format(RECORD_FILE))
        result = False
    elif not isinstance(STANDARD_POSITION, int):
        message = ("Configuration error, "
                   "STANDARD_POSITION is not an int (bool): {0}")
        print(message.format(STANDARD_POSITION))
        result = False
    return result

class Game(object):
    """Class which represents a single trial of the game"""

    # pylint: disable=too-many-instance-attributes
    # This is where we integrate other classes, so having a lot of
    # configuration attributes is necessary

    def __init__(self,
                 record_file=RECORD_FILE,
                 save_progress=SAVE_PROGRESS,
                 test_mode=False):

        self.record_total_time = 0.0
        self.record_total_trials = 0
        self.trial_duration = 0.0

        self.record_file = record_file
        self.save_progress = save_progress
        self.test_mode = test_mode

        self.orientation = random.choice((True, False))
        self.player_color = random.choice(("white", "black"))
        self.x_loc_chess, self.y_loc_chess = board.identify_random_square()
        self.location = conversion.convert_notation(self.x_loc_chess,
                                                    self.y_loc_chess,
                                                    "alg",
                                                    self.player_color)

    def main(self):
        """Primary entry point where a single game/trial is played.
        Returns True if user quit the game otherwise false"""
        self.display_board()
        self.display_status_information()
        quit_game = self.get_user_input()
        if not quit_game:
            # check to see if user quit game so we don't save
            self.record_progress()
        return quit_game

    def get_user_input(self):
        """ Ask for input from the user """
        start = time.time()
        attempt = input('Enter highlighted square, or \'quit\': ')
        end = time.time()
        if attempt == self.location:
            print("CORRECT!!")
        elif attempt == "quit" or attempt == "q":
            print("Exiting, current trial will not be saved.")
            return True
        else:
            print("{0} is wrong, the answer was {1}".format(attempt,
                                                            self.location))
        self.trial_duration = end - start
        print("Attempt took {0:.03f} seconds".format(self.trial_duration))
        return False

    def display_board(self):
        """Display the updated board with highlighted square"""
        games_source = games.GamePositions()
        current_board = board.Board(games_source.random_game(),
                                    orientation=self.orientation)
        current_board.highlight_square(self.x_loc_chess,
                                       self.y_loc_chess)
        current_board.update_board_string()
        print(current_board)

    def display_status_information(self):
        """Shows game status to the player"""
        if self.save_progress:
            try:
                # Try to retrieve data from record file
                record = get_record_from_file(self.record_file).split(',')
                self.record_total_time = float(record[0])
                self.record_total_trials = int(record[1])
                template = ("Average time: {0:.2f}, Playing as: {1}\n"
                            "Total seconds: {2:.2f}, Total trials: {3}")
                record_total_float = float(self.record_total_trials)
                trial_avg = self.record_total_time/record_total_float
                print(template.format(trial_avg,
                                      self.player_color.capitalize(),
                                      self.record_total_time,
                                      self.record_total_trials))
            except FileNotFoundError:
                print("No record file found.\n\
Creating a new one after this trial: {0}".format(self.record_file))

    def record_progress(self):
        """Saves string representing game progress, if save_progress is True"""
        if self.save_progress:
            self.record_total_time += self.trial_duration
            self.record_total_trials = self.record_total_trials + 1
            record = "{0},{1}".format(self.record_total_time,
                                      self.record_total_trials)
            write_record_to_file(record, self.record_file)

if __name__ == '__main__':
    SETTINGS_OKAY = validate_settings()
    if not SETTINGS_OKAY:
        raise ValueError("Something is not configured correctly, exiting.")
    for trial_num in range(NUMBER_OF_TRIALS):
        game_trial = Game()
        if game_trial.main():
            # if main() returns True at any time, it means the user quit
            break
