"""This module converts notation between algebraic and descriptive notation"""

NOTATION_MAP = (('a1', 'qr1', 'qr8'), ('b1', 'qn1', 'qn8'),
                ('c1', 'qb1', 'qb8'), ('d1', 'q1', 'q8'), ('e1', 'k1', 'k8'),
                ('f1', 'kb1', 'kb8'), ('g1', 'kn1', 'kn8'),
                ('h1', 'kr1', 'kr8'), ('a2', 'qr2', 'qr7'),
                ('b2', 'qn2', 'qn7'), ('c2', 'qb2', 'qb7'), ('d2', 'q2', 'q7'),
                ('e2', 'k2', 'k7'), ('f2', 'kb2', 'kb7'), ('g2', 'kn2', 'kn7'),
                ('h2', 'kr2', 'kr7'), ('a3', 'qr3', 'qr6'),
                ('b3', 'qn3', 'qn6'), ('c3', 'qb3', 'qb6'), ('d3', 'q3', 'q6'),
                ('e3', 'k3', 'k6'), ('f3', 'kb3', 'kb6'), ('g3', 'kn3', 'kn6'),
                ('h3', 'kr3', 'kr6'), ('a4', 'qr4', 'qr5'),
                ('b4', 'qn4', 'qn5'), ('c4', 'qb4', 'qb5'), ('d4', 'q4', 'q5'),
                ('e4', 'k4', 'k5'), ('f4', 'kb4', 'kb5'), ('g4', 'kn4', 'kn5'),
                ('h4', 'kr4', 'kr5'), ('a5', 'qr5', 'qr4'),
                ('b5', 'qn5', 'qn4'), ('c5', 'qb5', 'qb4'), ('d5', 'q5', 'q4'),
                ('e5', 'k5', 'k4'), ('f5', 'kb5', 'kb4'), ('g5', 'kn5', 'kn4'),
                ('h5', 'kr5', 'kr4'), ('a6', 'qr6', 'qr3'),
                ('b6', 'qn6', 'qn3'), ('c6', 'qb6', 'qb3'), ('d6', 'q6', 'q3'),
                ('e6', 'k6', 'k3'), ('f6', 'kb6', 'kb3'), ('g6', 'kn6', 'kn3'),
                ('h6', 'kr6', 'kr3'), ('a7', 'qr7', 'qr2'),
                ('b7', 'qn7', 'qn2'), ('c7', 'qb7', 'qb2'), ('d7', 'q7', 'q2'),
                ('e7', 'k7', 'k2'), ('f7', 'kb7', 'kb2'), ('g7', 'kn7', 'kn2'),
                ('h7', 'kr7', 'kr2'), ('a8', 'qr8', 'qr1'),
                ('b8', 'qn8', 'qn1'), ('c8', 'qb8', 'qb1'), ('d8', 'q8', 'q1'),
                ('e8', 'k8', 'k1'), ('f8', 'kb8', 'kb1'), ('g8', 'kn8', 'kn1'),
                ('h8', 'kr8', 'kr1'),)

# Static helper functions
def coordinate_to_alg(x_chess, y_chess):
    """Takes chess numerical coordinates and returns an algebraic notation
    string"""
    xy_min_chess = 1
    xy_max_chess = 8
    if (not isinstance(x_chess, int) or
            not isinstance(y_chess, int)):
        error_message = "Bad value coordinates: \
x_chess = {0}, y_chess = {1}".format(x_chess, y_chess)
        raise TypeError("Coordinates are not ints")
    elif (x_chess < xy_min_chess or
          x_chess > xy_max_chess or
          y_chess < xy_min_chess or
          y_chess > xy_max_chess):
        error_message = "Unexpected value coordinates: \
x_chess = {0}, y_chess = {1}".format(x_chess, y_chess)
        raise ValueError(error_message)

    result = ""
    notation_letters = 'abcdefgh'
    result = result + notation_letters[x_chess-1]
    result = result + str(y_chess)
    return result

class NotationConverter(object):
    """Class converts notation between algebraic and descriptive notation"""
    def __init__(self):
        self.n_map = NOTATION_MAP

    def alg_search(self, location):
        """Search for a particular algebraic notation or raise LookupError"""
        for item in self.n_map:
            if location == item[0]:
                return item
        raise KeyError("Unable to find: {0}".format(location))

    def desc_search(self, location, color):
        """Search for a particular descriptive notation with color"""
        if color == "white":
            item_index = 1
        elif color == "black":
            item_index = 2
        else:
            error_msg = "Player color is not black or white: {0}"
            raise ValueError(error_msg.format(color))
        for item in self.n_map:
            if location == item[item_index]:
                return item
        raise KeyError("Unable to find: {0}".format(location))

    def alg_to_desc(self, location, color):
        """Converts an algebraic to descriptive position"""
        position_map = self.alg_search(location)
        if color == "white":
            return position_map[1]
        elif color == "black":
            return position_map[2]
        else:
            error_msg = "Player color is not black or white: {0}"
            raise ValueError(error_msg.format(color))

    def desc_to_alg(self, location, color):
        """Converts a descriptive to algebraic position"""
        position_map = self.desc_search(location, color)
        return position_map[0]

