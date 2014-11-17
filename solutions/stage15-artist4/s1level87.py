"""Stage 15: Puzzle 6 of 10

Using `draw_square()` as an example, add an input named "length" to
`draw_triangle()`. Then, draw triangles in different sizes. 

"""

import sys
sys.path.append('..')
import codestudio
zombie = codestudio.load('s1level87')

def draw_square(length):
    for count in range(4):
        zombie.move_forward(length)
        zombie.turn_right(90)

def draw_triangle():
    for count in range(3):
        zombie.move_forward(100)
        zombie.turn_right(120)

# ???

zombie.check()
