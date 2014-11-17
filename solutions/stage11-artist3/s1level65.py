"""Stage 11: Puzzle 7 of 11

Here's a program to draw a spiral Make a new program using counter loop
and your `draw_square()` function instead of the long way.

"""

import sys
sys.path.append('../..')
import codestudio
z = codestudio.load('s1level65')
'''
for length in range(25,71,5):
    print(length)
    z.move_forward(length)
    z.right()
'''
z.move_forward(25)
z.turn_right(90)
z.move_forward(30)
z.turn_right(90)
z.move_forward(35)
z.turn_right(90)
z.move_forward(40)
z.turn_right(90)
z.move_forward(45)
z.turn_right(90)
z.move_forward(50)
z.turn_right(90)
z.move_forward(55)
z.turn_right(90)
z.move_forward(60)
z.turn_right(90)

z.check()
