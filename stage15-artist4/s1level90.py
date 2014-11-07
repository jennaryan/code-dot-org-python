"""Stage 15: Puzzle 9 of 10

Can you re-create the `draw house(length)` function without help? Try it,
and then draw a row of houses. Hint: replace 'pass' with your code.

"""

import sys
sys.path.append('..')
import codestudio
zombie = codestudio.load('s1level90')

def draw_square(length):
    for count in range(4):
        zombie.move_forward(length)
        zombie.turn_right(90)

def draw_triangle(length):
    for count in range(3):
        zombie.move_forward(length)
        zombie.turn_right(120)

def draw_house(length):
    pass

# ???

zombie.check()
