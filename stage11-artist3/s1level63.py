"""Stage 11:Puzzle 5 of 11

Draw squares with sides of 50, 60, 70, 80, and 90 pixels. You'll need to call
the `draw_square()` method 5 times.

"""

import sys
sys.path.append('..')

import codestudio
import mymod
artist = codestudio.load('s1level63')
zombie = mymod.Zombie(artist)
zombie.speed = 'fast'

# TODO put the following in a counter loop as explained above
zombie.draw_square(50)

zombie.check()
