"""Stage 11: Puzzle 8 of 11

Our Zombie has a new `draw_snowman()` method. Draw two snowmen, of height
250 and 100.

"""

import sys
sys.path.append('..')

import codestudio
import mymod
artist = codestudio.load('s1level66')
zombie = mymod.Zombie(artist)
zombie.speed = 'fastest'

zombie.draw_snowman(250)

zombie.check()
