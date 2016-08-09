"""Settings used for running the game in main.py"""

# NOTATION can be "alg" (algabraic) or "desc" (descriptive)
NOTATION = "alg"

# Number of trials the player will play before the program exits
NUMBER_OF_TRIALS = 5

# Player that appears on bottom. Can be "white" or "black" or "random"
ORIENTATION = "white"

# PLAYER_COLOR = "white" or "black" or "random". Player plays this color
# This setting only matters if you have NOTATION set to descriptive,
# otherwise it is ignored.
PLAYER_COLOR = "white"

# This is where the player's average trial times are stored
RECORD_FILE = "trial_record.txt"

# Whether to save trial times or not. Can be True or False
SAVE_PROGRESS = True

# STANDARD_POSITION is the layout of chess pieces.
# This can be True (regular starting chess position) or False (a random game)
STANDARD_POSITION = False
