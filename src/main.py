"""Where player runs the game"""

import random
import time

import board
import conversion
import games
from settings import (NUMBER_OF_TRIALS,
                      RECORD_FILE,
                      SAVE_PROGRESS)

class Game(object):
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

        self.x_loc_chess, self.y_loc_chess = board.identify_random_square()
        self.location = conversion.coordinate_to_alg(self.x_loc_chess,
                                                     self.y_loc_chess)

    def main(self):
        self.display_board()
        self.display_status_information()
        quit = self.get_user_input()
        if not quit:
            # check to see if user quit game so we don't save
            self.record_progress()
        return quit

    def write_record_to_file(self, a_string, file_name):
        with open(file_name, 'w') as f:
            f.write(a_string)

    def get_record_from_file(self, file_name):
        with open(file_name, 'r') as f:
            result = f.readline()
        return result

    def get_user_input(self, test_string=None):
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
            print("Wrong, the answer was {0}".format(self.location))
        self.trial_duration = end - start
        print("Attempt took {0:.03f} seconds".format(self.trial_duration))
        return False

    def display_board(self):
        games_source = games.GamePositions()    
        current_board = board.Board(games_source.random_game(),
                                    orientation=random.choice((True, False)))
        current_board.highlight_square(self.x_loc_chess,
                                       self.y_loc_chess)
        current_board.update_board_string()
        print(current_board)

    def display_status_information(self):
        if self.save_progress:
            try:
                # Try to retrieve data from record file
                record = self.get_record_from_file(self.record_file).split(',')
                self.record_total_time = float(record[0])
                self.record_total_trials = int(record[1])
                template = "Average time: {0:.2f}\nTotal seconds: {1:.2f}, \
Total trials: {2}"
                record_total_float = float(self.record_total_trials)
                trial_avg = self.record_total_time/record_total_float
                print(template.format(trial_avg, 
                                      self.record_total_time,
                                      self.record_total_trials))
            except FileNotFoundError:
                print("No record file found.\n\
Creating a new one after this trial: {0}".format(self.record_file))

    def record_progress(self):
        if self.save_progress:
            self.record_total_time += self.trial_duration
            self.record_total_trials = self.record_total_trials + 1
            record = "{0},{1}".format(self.record_total_time,
                                      self.record_total_trials)
            self.write_record_to_file(record, self.record_file)

if __name__ == '__main__':
    for trial_num in range(NUMBER_OF_TRIALS):
        game_trial = Game()
        if game_trial.main():
            # if main() returns True at any time, it means the user quit
            break
