""" This module has a list of game positions, and the class will return
a random one to the Board()."""

import random

# All game positions are from:
# Burgess, Graham et all, The World's Greatest Chess Games. New York:
# Carroll & Graf Publishers, 2004. Book
GAME_POSITIONS = []
# Game position 1 - pg 40. Black to play
GAME_POSITIONS.append(["r r   k ",
                       "pp q  Rp",
                       "     pp ",
                       "   p  N ",
                       "      Q ",
                       "        ",
                       "PP   PPP",
                       "  R   K ",])
# Game position 2 - pg 43. Black to play
GAME_POSITIONS.append(["  r  rk ",
                       "pp   pp ",
                       "    bb p",
                       "q  p P Q",
                       "   P    ",
                       "  N     ",
                       "PP    PP",
                       " K R B R",])
# Game position 3 - pg 51. Black to play
GAME_POSITIONS.append(["   b  k ",
                       "pppR r  ",
                       "  n p   ",
                       "  P   P ",
                       "  BP P  ",
                       "P   PN  ",
                       " P      ",
                       "  K     ",])
# Game position 4 - pg 53. Black to play
GAME_POSITIONS.append(["r bqkb r",
                       " p n ppp",
                       "    p   ",
                       "pPnpP   ",
                       "     P  ",
                       "P NBBN  ",
                       "  P   PP",
                       "R  Q RK ",])
# Game position 5 - pg 60. Black to play
GAME_POSITIONS.append(["r b r  k",
                       "pp  Npbp",
                       "      p ",
                       "  B p PP",
                       "     P  ",
                       "  n     ",
                       "PPP     ",
                       "R   KB R",])
# Game position 6 - pg 74. Black to play
GAME_POSITIONS.append(["r bq rk ",
                       "p pnbppp",
                       " p   n  ",
                       "   p  B ",
                       "Q  P    ",
                       "  N PN  ",
                       "PP   PPP",
                       "  R KB R",])
# Game position 7 - pg 84. Black to play
GAME_POSITIONS.append(["    r k ",
                       "p  K   p",
                       "      p ",
                       " bpP    ",
                       "    P   ",
                       " PQ     ",
                       "PB     q",
                       "  R     ",])
# Game position 8 - pg 87. White to play
GAME_POSITIONS.append(["r b  rk ",
                       "  p  ppp",
                       "p  b    ",
                       " p      ",
                       "      nq",
                       " BP  Q P",
                       "PP P PP ",
                       "RNB R K ",])
# Game position 9 - pg 92. White to play
GAME_POSITIONS.append(["r  qr k ",
                       " p  bppp",
                       "   p n  ",
                       "p  P  B ",
                       "   Q    ",
                       "     N  ",
                       "PP   PPP",
                       "R   R K ",])
# Game position 10 - pg 102. Black to play
GAME_POSITIONS.append(["      k ",
                       "     p  ",
                       "  n p p ",
                       "   p    ",
                       "   P    ",
                       " r RK PP",
                       "        ",
                       "   N    ",])
# Game position 11 - pg 105. White to play
GAME_POSITIONS.append(["rnbq rk ",
                       "pp    pp",
                       "  pbp   ",
                       "   p p  ",
                       "  PPn   ",
                       "P NBPN  ",
                       " PQ  PPP",
                       "R B  RK ",])
# Game position 12 - pg 114. White to play
GAME_POSITIONS.append(["r    rk ",
                       "   qb pp",
                       "p b p   ",
                       " p p p n",
                       "   P    ",
                       " QN   PP",
                       "PP BPPBK",
                       "  R  R  ",])
# Game position 13 - pg 121. Black to play
GAME_POSITIONS.append(["  q   k ",
                       "     pb ",
                       "p     pp",
                       " p      ",
                       "   rP   ",
                       "P  nP   ",
                       "NP  Q PP",
                       "   R  K ",])
# Game position 14 - pg 124. Black to play
GAME_POSITIONS.append(["    r k ",
                       "p pq   p",
                       " p pprp ",
                       "n       ",
                       "P PPQP  ",
                       "  PB  P ",
                       "       P",
                       "R   R K ",])
# Game position 15 - pg 134. White to play
GAME_POSITIONS.append(["rnbq rk ",
                       "ppp  ppp",
                       "     n  ",
                       "   p    ",
                       "   N    ",
                       "   Q  P ",
                       "PPPNPPBP",
                       "R   K  R",])
# Game position 16 - pg 32. Black to play
GAME_POSITIONS.append(["r bq rk ",
                       "ppp  pbp",
                       "  npn p ",
                       "    p   ",
                       "    P  P",
                       "  PPNN  ",
                       "PPB  PP ",
                       "R BQK  R",])
# Game position 17 - pg 12. Black to play
GAME_POSITIONS.append(["    Br k",
                       " b    pp",
                       "  P     ",
                       "p    p  ",
                       "  Qpp   ",
                       "    q b ",
                       "PP    KP",
                       "  R  R  ",])
# Game position 18 - pg 15. White to play
GAME_POSITIONS.append(["rnb kbnr",
                       "p pp ppp",
                       "        ",
                       " p      ",
                       "  B Pp q",
                       "        ",
                       "PPPP  PP",
                       "RNBQ KNR",])
# Game position 19 - pg 24. Black to play
GAME_POSITIONS.append([" r  k r ",
                       "pbppRp p",
                       " bn  P  ",
                       "        ",
                       "Q       ",
                       "B PB q  ",
                       "P    PPP",
                       "   R  K ",])
# Game position 20 - pg 27. Black to play
GAME_POSITIONS.append(["r r   k ",
                       "pb  qppp",
                       " p  pn  ",
                       "   p    ",
                       "   P    ",
                       " P BPP  ",
                       "PB Q  PP",
                       "    RRK ",])

STANDARD_GAME = ["rnbqkbnr",
                 "pppppppp",
                 "        ",
                 "        ",
                 "        ",
                 "        ",
                 "PPPPPPPP",
                 "RNBQKBNR",]

class GamePositions(object):
    """This class returns a random board positions"""
    def __init__(self):
        self.g_pos = GAME_POSITIONS

    def random_game(self, pos=None):
        """Returns a random game position, or a specific one for testing"""
        if pos:
            return self.g_pos[pos]
        else:
            return random.choice(self.g_pos)
