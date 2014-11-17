"""Stage 15: Puzzle 2 of 10

Using the `draw_square()` function as an example, create a
`draw_triangle()` function and use it. Hint: replace the `pass` with
your steps to draw a triangle.

"""
import sys
sys.path.append('..')
import codestudio
zombie = codestudio.load('s1level83')

def draw_square():
    for count in range(4):
        zombie.move_forward(100)
        zombie.turn_right(90)

def draw_triangle():
    pass

# ???

zombie.check()
