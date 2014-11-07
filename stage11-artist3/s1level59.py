"""Stage 11: Puzzle 1 of 11

Hello. Me zombie artist. Me love drawing! Help me draw a square in a
special color. Hint: fix the `draw_square()` function provided.

"""

import sys
sys.path.append('..')

import codestudio
zombie = codestudio.load('s1level59')

def draw_square():
    """ Draws a square assuming a zombie exists."""
    zombie.move_forward(100)
    zombie.turn_right(90)

zombie.color = zombie.random_color()
draw_square()

zombie.check()
