"""Stage 15: Puzzle 5 of 10

Now create a new `draw_house()` function and use it to house two
cats. Hint: copy one of the existing functions to make your own from
the code you created in the last puzzle by replacing `pass`.

"""

import sys
sys.path.append('..')
import codestudio
zombie = codestudio.load('s1level86')

def draw_square():
    for count in range(4):
        zombie.move_forward(100)
        zombie.turn_right(90)

def draw_triangle():
    for count in range(3):
        zombie.move_forward(100)
        zombie.turn_right(120)

def draw_house():
    pass

# ???

zombie.check()
