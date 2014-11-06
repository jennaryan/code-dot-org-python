"""Stage 11: Puzzle 4 of 11

Now we're going to get fancy. Change the code to draw 36 squares, 100
pixels wide, and each 10 degrees apart. Hint: adjust the speed by setting
to 'normal', 'fast', 'faster', 'fastest' or a number.

"""

import sys
sys.path.append('..')

import codestudio
import mymod
artist = codestudio.load('s1level62')
zombie = mymod.Zombie(artist)
zombie.speed = 'faster'

for count in range(10):  # hummm
    zombie.color = zombie.random_color()
    zombie.draw_square(50) # hummm
    zombie.turn_right(20) # humm

zombie.check()
