# -*- coding: utf-8 -*-
"""This project quizes the user on chess notation and times the responses"""

from random import randint

# Static helper functions
def identify_random_square():
    """This returns a tuple of a random square on the board"""
    return(randint(0, 7), randint(0, 7))

class TileLine(object):
    """Class which represents a single line of a tile as a string"""
    def __init__(self, color, piece=None, white=" ", black='|'):
        self.tile_line_template = "{0}{0}{0}{0}{0}{0}{0}"
        if piece == " ":
            self.tile_line_template = "{0}{0}{0}{0}{0}{0}{0}"
        elif piece:
            self.tile_line_template = "{0}{0} {1} {0}{0}"
        self.white = white
        self.black = black
        self.line = self.make_line(color, piece)

    def make_line(self, color, piece):
        """Makes the line of characters"""
        if piece:
            if color == 'w':
                return self.tile_line_template.format(self.white, piece)
            elif color == 'b':
                return self.tile_line_template.format(self.black, piece)
        else:
            if color == 'w':
                return self.tile_line_template.format(self.white)
            elif color == 'b':
                return self.tile_line_template.format(self.black)
        raise ValueError('Unknown color value: {0}'.format(color))

class RowLine(object):
    """Represents a line in a particular row. Can be an even or odd row."""
    def __init__(self, parity, pieces=None):
        self.white_tile = TileLine('w').line
        self.black_tile = TileLine('b').line
        self.odd_row_line_template = "{1}{0}{1}{0}{1}{0}{1}{0}"
        self.even_row_line_template = "{0}{1}{0}{1}{0}{1}{0}{1}"
        self.pieces_row_line_template = "{0}{1}{2}{3}{4}{5}{6}{7}"
        if pieces:
            self.row = self.make_row_pieces(parity, pieces)
        else:
            self.row = self.make_row(parity)

    def make_row_pieces(self, parity, pieces):
        """Makes row of characters with pieces"""
        if parity == "even":
            white_tile1 = TileLine('w', pieces[0]).line
            black_tile1 = TileLine('b', pieces[1]).line
            white_tile2 = TileLine('w', pieces[2]).line
            black_tile2 = TileLine('b', pieces[3]).line
            white_tile3 = TileLine('w', pieces[4]).line
            black_tile3 = TileLine('b', pieces[5]).line
            white_tile4 = TileLine('w', pieces[6]).line
            black_tile4 = TileLine('b', pieces[7]).line
            return self.pieces_row_line_template.format(white_tile1,
                                                        black_tile1,
                                                        white_tile2,
                                                        black_tile2,
                                                        white_tile3,
                                                        black_tile3,
                                                        white_tile4,
                                                        black_tile4)
        elif parity == "odd":
            black_tile1 = TileLine('b', pieces[0]).line
            white_tile1 = TileLine('w', pieces[1]).line
            black_tile2 = TileLine('b', pieces[2]).line
            white_tile2 = TileLine('w', pieces[3]).line
            black_tile3 = TileLine('b', pieces[4]).line
            white_tile3 = TileLine('w', pieces[5]).line
            black_tile4 = TileLine('b', pieces[6]).line
            white_tile4 = TileLine('w', pieces[7]).line
            return self.pieces_row_line_template.format(black_tile1,
                                                        white_tile1,
                                                        black_tile2,
                                                        white_tile2,
                                                        black_tile3,
                                                        white_tile3,
                                                        black_tile4,
                                                        white_tile4)
        raise ValueError('Unknown parity value: {0}'.format(parity))

    def make_row(self, parity):
        """Makes row of characters"""
        if parity == "odd":
            return self.odd_row_line_template.format(self.white_tile,
                                                     self.black_tile)
        elif parity == "even":
            return self.even_row_line_template.format(self.white_tile,
                                                      self.black_tile)
        raise ValueError('Unknown parity value: {0}'.format(parity))

class RowTiles(object):
    """Represents a row of tiles on the board. Can be an even or odd row."""
    def __init__(self, parity, pieces=None):
        row_line_string_blank = RowLine(parity).row
        row_line_string_pieces = RowLine(parity, pieces).row
        row_tiles_template = "\n{0}\n{1}\n{0}"
        self.row_tiles = row_tiles_template.format(row_line_string_blank,
                                                   row_line_string_pieces)
    def __str__(self):
        return self.row_tiles

class Board(object):
    """Returns string of board given current state description.
    Setting orientation=True means that white appears on the bottom."""
    def __init__(self, description, orientation=True):
        self.board_string = ""
        self.highlight_piece = "#"
        self.orientation = orientation
        self.description = description
        if not isinstance(self.description, list):
            raise TypeError("Board description is not a list")
        self.needs_orienting = True
        self.update_board_string()

    def update_board_string(self):
        """This refreshes self.board_string with the current self.description
        for displaying the board to the user"""
        control = 0
        self.board_string = ""
        if not self.orientation and self.needs_orienting:
            self.description = list(reversed(self.description))
            # We want to make sure that we reverse the board only once
            self.needs_orienting = False
        for row in self.description:
            result = control % 2
            if result == 1:
                parity = "odd"
            else:
                parity = "even"
            if row:
                self.board_string += str(RowTiles(parity, row))
            else:
                self.board_string += str(RowTiles(parity))
            control += 1
        self.board_string = "{0}\n".format(self.board_string)

    def insert_square_into_description(self, description, square):
        """unfinished function. updates self.description"""
        """i feel like there is a larger problem here"""
        """there isn't an easy way to iterate through the "board"""
        """the board just gets constructed on demand from the description"""
        """maybe just change the description and functionify board_string?"""
        return self.description

    def highlight_rowline(self, row_string, x_loc_chess):
        """Takes a row from self.description and inserts a highlighted piece
        at x location"""
        row_list = list(row_string)
        row_list[x_loc_chess - 1] = self.highlight_piece
        return "".join(row_list)

    def grab_index(self, y_loc_chess):
        """This grabs the right index based on y_loc_chess and
        orientation. A coordinate with '_chess' refers to the game coordinate,
        as opposed to the array coordinate."""
        if self.orientation:
            # For when white is on bottom
            return 8 - y_loc_chess
        elif not self.orientation:
            # Black on bottom
            return y_loc_chess-1
        else:
            # We don't know what the orientation should be, but don't assume
            error_message = "Unexpected value: orientation = {0}"
            raise ValueError(error_message.format(self.orientation))

    def update_row(self, x_loc_chess, y_loc_chess):
        """Updates self.description to highlight the given square on the
        board"""
        index = self.grab_index(y_loc_chess)
        row = self.highlight_rowline(self.description[index], x_loc_chess)
        self.description[index] = row

    def highlight_square(self,x_loc,y_loc):
        # iterate through board and replace piece with self.highlight_piece
        # probably gonna have to put board description into class variable
        # Have a function to sub in the right character in a particular row
        # Need a function to grab the right row based on y_loc and orientation
        # what should interface be? pass in x,y into new board instance?
        result_description = ("rnbqkbnr",
                              "pppppppp",
                              "        ",
                              "        ",
                              "        ",
                              "        ",
                              "P#PPPPPP",
                              "RNBQKBNR",)

    def __str__(self):
        return self.board_string
