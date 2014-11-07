"""Stage 15: Puzzle 3 of 10

Draw triangular fences around the cats and a square fence around the
cow. Tip: test the program as you go along.

"""
import sys
sys.path.append('..')
import codestudio
zombie = codestudio.load('s1level84')

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
