# Description #

This is a console-based game to quiz user on chess notation. This project is
also meant to be an exercise in applying best practices of software
development such as: test driven development, static analyzer for
style, PEP-8 standard, unit test everything, and measure code coverage.

Project Status: Maintenance

### Features ###

* Timed trials of identifying squares on a chess board
* Algebraic or descriptive notation
* Saves average time
* Configurable

### Getting Started ###

* To get started

$ make run
#Run the game
env/bin/python src/main.py

```
       |||||||       |||||||       |||||||       |||||||
   R   |||||||       |||||||   R   |||||||   K   |||||||
       |||||||       |||||||       |||||||       |||||||
|||||||       |||||||       |||||||       |||||||       
|||||||       |||||||       |||||||       |||||||   P   
|||||||       |||||||       |||||||       |||||||       
       |||||||       |||||||       |||||||       |||||||
       |||||||   P   || B ||       |||||||   P   |||||||
       |||||||       |||||||       |||||||       |||||||
|||||||       |||||||       |||||||       |||||||       
|| P ||       || P ||   P   || Q ||   P   |||||||       
|||||||       |||||||       |||||||       |||||||       
       |||||||       |||||||       |||||||       |||||||
   n   |||||||       |||||||       |||||||       |||||||
       |||||||       |||||||       |||||||       |||||||
|||||||       |||||||       |||||||       |||||||       
|||||||   p   |||||||   p   || p ||   r   || p ||       
|||||||       |||||||       |||||||       |||||||       
       |||||||       |||||||       |||||||       |||||||
   p   |||||||   p   || @ ||       |||||||       || p ||
       |||||||       |||||||       |||||||       |||||||
|||||||       |||||||       |||||||       |||||||       
|||||||       |||||||       || r ||       || k ||       
|||||||       |||||||       |||||||       |||||||       
```

No record file found.
Creating a new one after this trial: trial_record.txt
Enter highlighted square, or 'quit': 

### Configuring the game ###
* NOTATION can be "alg" (algabraic) or "desc" (descriptive)
* NUMBER_OF_TRIALS determines the trials the player will play before the
program exits
* ORIENTATION determines which player that appears on bottom. Can be "white" or
"black" or "random"
* PLAYER_COLOR = "white" or "black" or "random". Player plays this color This
setting only matters if you have NOTATION set to descriptive, otherwise it is
ignored.
* RECORD_FILE is where the player's average trial times are stored
* SAVE_PROGRESS is whether to save trial times or not. Can be True or False
* STANDARD_POSITION is the layout of chess pieces. This can be True (regular
starting chess position) or False (a random game)

### Troubleshooting ###

* If you try to run src/main.py and you get a FileNotFound error (below) this probably means you are running Python 2. Chess_notation requires Python 3.5 or
later.
Traceback (most recent call last):
  File "src/main.py", line 173, in <module>
    if game_trial.main():
  File "src/main.py", line 102, in main
    self.display_status_information()
  File "src/main.py", line 154, in display_status_information
    except FileNotFoundError:
NameError: global name 'FileNotFoundError' is not defined

### Requirements ###

To use:
* Python 3.5

For developers:
* Virtualenv
* Make
* Pylint
* Coverage

### Todo ###

* See: https://github.com/blairck/chess_notation/issues
