from random import choice

notation_map = (('a1','qr1','qr8'),('b1','qn1','qn8'),('c1','qb1','qb8'),
                ('d1','q1','q8'),('e1','k1','k8'),('f1','kb1','kb8'),
                ('g1','kn1','kn8'),('h1','kr1','kr8'),('a2','qr2','qr7'),
                ('b2','qn2','qn7'),('c2','qb2','qb7'),('d2','q2','q7'),
                ('e2','k2','k7'),('f2','kb2','kb7'),('g2','kn2','kn7'),
                ('h2','kr2','kr7'),('a3','qr3','qr6'),('b3','qn3','qn6'),
                ('c3','qb3','qb6'),('d3','q3','q6'),('e3','k3','k6'),
                ('f3','kb3','kb6'),('g3','kn3','kn6'),('h3','kr3','kr6'),
                ('a4','qr4','qr5'),('b4','qn4','qn5'),('c4','qb4','qb5'),
                ('d4','q4','q5'),('e4','k4','k5'),('f4','kb4','kb5'),
                ('g4','kn4','kn5'),('h4','kr4','kr5'),('a5','qr5','qr4'),
                ('b5','qn5','qn4'),('c5','qb5','qb4'),('d5','q5','q4'),
                ('e5','k5','k4'),('f5','kb5','kb4'),('g5','kn5','kn4'),
                ('h5','kr5','kr4'),('a6','qr6','qr3'),('b6','qn6','qn3'),
                ('c6','qb6','qb3'),('d6','q6','q3'),('e6','k6','k3'),
                ('f6','kb6','kb3'),('g6','kn6','kn3'),('h6','kr6','kr3'),
                ('a7','qr7','qr2'),('b7','qn7','qn2'),('c7','qb7','qb2'),
                ('d7','q7','q2'),('e7','k7','k2'),('f7','kb7','kb2'),
                ('g7','kn7','kn2'),('h7','kr7','kr2'),('a8','qr8','qr1'),
                ('b8','qn8','qn1'),('c8','qb8','qb1'),('d8','q8','q1'),
                ('e8','k8','k1'),('f8','kb8','kb1'),('g8','kn8','kn1'),
                ('h8','kr8','kr1'),)

x_axis = ('a','b','c','d','e','f','g','h')
y_axis = ('1','2','3','4','5','6','7','8')
for i in range(1000000):
        x_rand = choice(x_axis)
        y_rand = choice(y_axis)
        location = "{0}{1}".format(x_rand, y_rand)
        for item in notation_map:
                if location == item[0]:
                        #print "{0} -> {1}".format(location, item[1])
                        break
