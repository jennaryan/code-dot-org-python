"""Stage 15: Puzzle 7 of 10

Add an input named "length" to `draw_house()` and build a big house for
the elephant (with edges 150 pixels long)

"""

import sys
sys.path.append('..')
import codestudio
zombie = codestudio.load('s1level88')

def draw_square(length):
    for count in range(4):
        zombie.move_forward(length)
        zombie.turn_right(90)

def draw_triangle(length):
    for count in range(3):
        zombie.move_forward(length)
        zombie.turn_right(120)

def draw_house():
    draw_square(100)
    zombie.move_forward(100)
    zombie.turn_right(30)
    draw_triangle(100)

# ???

zombie.check()
