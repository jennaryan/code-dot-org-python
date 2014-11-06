"""Stage 11: Puzzle 2 of 11

Welcome to using functions, which let you reuse code with your own
action funtion calls! Try to draw a small 50x50 green square with the
`draw_square()` function imported from your new, very own `mymod` Python
module. Hint: think of modules as checking out a spellbook from a library of
magic to do more with your coding wizardry.

"""

import sys
sys.path.append('..')

import codestudio
import mymod 
#zombie = codestudio.load('s1level60')
zombie = codestudio.create('s1level60','artist',90)
myzombie = mymod.Artist(zombie.canvas)

myzombie.speed = 'slow'

myzombie.draw_square(50)

zombie.wait()
