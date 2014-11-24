"""Stage 15: Puzzle 4 of 10

See if you can figure out how to use `draw_square()` and `draw_triangle()`
(and some other code) to draw a house around the lion.

"""
import sys
sys.path.append('..')
import codestudio
z = codestudio.load('s1level85')

def draw_square():
    for count in range(4):
        z.move_forward(100)
        z.turn_right(90)

def draw_triangle():
    for count in range(3):
        z.right(120)
        z.move(100)

draw_square()
z.move(100)
z.right()
z.move(100)

z.left(120)
z.move(100)
z.left(120)
z.move(100)

z.check()
