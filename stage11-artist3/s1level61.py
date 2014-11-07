"""Stage 11: Puzzle 3 of 11

Use repeat (for) loops to draw 3 squares of size 100, each 120 degrees
apart. And do it in 3 different, random colors.

Hint: Use your new Zombie class, which we have moved into `mymod.py`
library module for you.

"""

import sys
sys.path.append('..')
import codestudio
import mymod
artist = codestudio.load('s1level61')
zombie = mymod.Zombie(artist)

zombie.color = zombie.random_color()
zombie.draw_square(100)

zombie.check()
