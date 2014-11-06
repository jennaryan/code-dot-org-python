"""Stage 11: Puzzle 9 of 11

This one's a bit tricky. Use the `draw_snowman()` method and the new
`jump_forward(100)` or just `jump(100)` method, (which is new to
you). Draw 3 snowmen in different colors, 100 pixels apart.

"""

import sys
sys.path.append('..')

import codestudio
import mymod
artist = codestudio.load('s1level67')
zombie = mymod.Zombie(artist)
zombie.speed = 'fastest'

zombie.draw_snowman(150)

zombie.check()
