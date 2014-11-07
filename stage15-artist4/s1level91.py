"""Stage 15: Puzzle 10 of 10

You've learned a lot! Now use it to draw whatever you want. Try to draw
a star, or a spiral, or a fancy snowflake.

"""

import sys
sys.path.append('..')
import codestudio
zombie = codestudio.load('s1level91')

def draw_square(length):
    for count in range(4):
        zombie.move_forward(length)
        zombie.turn_right(90)

def draw_triangle(length):
    for count in range(3):
        zombie.move_forward(length)
        zombie.turn_right(120)

def draw_house(length):
    draw_square(length)
    zombie.move_forward(length)
    zombie.turn_right(30)
    draw_triangle(length)

# ???

zombie.wait()
