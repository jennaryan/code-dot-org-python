"""Stage 11: Puzzle 11 of 11

Here's some code to try experimenting with different spirals. What happens
if you change the turn amount? Or set a random color in the loop? Draw
anything you like.

"""

import sys
sys.path.append('..')
import codestudio
import mymod
artist = codestudio.load('s1level69')
zombie = mymod.Zombie(artist)
zombie.speed = 'fast'

zombie.width = 1
for counter in range(100):
    zombie.move(counter)
    zombie.right(91)

zombie.wait()
