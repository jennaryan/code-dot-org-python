"""Stage 15: Puzzle 4 of 10

See if you can figure out how to use `draw_square()` and `draw_triangle()`
(and some other code) to draw a house around the lion.

"""
import sys
sys.path.append('..')
import codestudio
zombie = codestudio.load('s1level85')

def draw_square():
    for count in range(4):
        zombie.move_forward(100)
        zombie.turn_right(90)

def draw_triangle():
    for count in range(3):
        zombie.move_forward(100)
        zombie.turn_right(120)

# ???

zombie.check()
