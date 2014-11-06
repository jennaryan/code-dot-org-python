"""Stage 11: Puzzle 10 of 11

Use a for loop to draw a family of snowmen with heights of 110, 100, 90,
80, and 70. The snowmen should all be 60 pixels apart.  Hint: Remember
you are counting backwards (use -). Also use 69 instead of 70 to make
sure you get enough snowmen.  (This is because Python ranges never reach
the number, only as close as they can get to the number.)

"""

import sys
sys.path.append('..')

import codestudio
import mymod
artist = codestudio.load('s1level68')
zombie = mymod.Zombie(artist)
zombie.speed = 'fastest'

for length in range(0): # TODO change to range(??,??,??)
    zombie.draw_snowman(length)
    # TODO turn and jump to next snowman start position

zombie.check()