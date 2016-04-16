# -*- coding: utf-8 -*-
"""This project quizes the user on chess notation and times the responses"""
class TileLine(object):
    """Class which represents a single line of a tile as a string"""
    def __init__(self, color, piece=None, white=" ", black='|'):
        self.tile_line_template = "{0}{0}{0}{0}{0}{0}{0}"
        if piece:
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
        self.odd_row_line_template = "{0}{1}{0}{1}{0}{1}{0}{1}"
        self.even_row_line_template = "{1}{0}{1}{0}{1}{0}{1}{0}"
        self.pieces_row_line_template = "{0}{1}{2}{3}{4}{5}{6}{7}"
        if pieces:
            self.row = self.make_row_pieces(parity, pieces)
        else:
            self.row = self.make_row(parity)

    def make_row_pieces(self, parity, pieces):
        """Makes row of characters with pieces"""
        if parity == "odd":
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
        elif parity == "even":
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

    def make_row(self, parity):
        """Makes row of characters"""
        if parity == "odd":
            return self.odd_row_line_template.format(self.white_tile,
                                                     self.black_tile)
        elif parity == "even":
            return self.even_row_line_template.format(self.white_tile,
                                                      self.black_tile)

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
    Setting orientation=True means that black appears on the bottom."""
    def __init__(self, description, orientation=True):
        self.board_string = ""
        print(orientation)
        control = 1
        if orientation is False:
            description = list(reversed(description))
        for row in description:
            result = control % 2
            if result == 1:
                parity = "odd"
            else:
                parity = "even"
            if row:
                self.board_string += str(RowTiles(parity, row[::-1]))
            else:
                self.board_string += str(RowTiles(parity))
            control += 1
        self.board_string = "{0}\n".format(self.board_string)

    def __str__(self):
        return self.board_string

if __name__ == '__main__':
    BOARD_DESCRIPTION = ("RNBQKBNR", "PPPPPPPP", None, None,
                         None, None, "pppppppp", "rnbqkbnr")
    BOARD = Board(BOARD_DESCRIPTION, orientation=True)
    print(BOARD)
