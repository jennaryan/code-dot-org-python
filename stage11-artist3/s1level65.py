"""Stage 11: Puzzle 7 of 11

Here's a program to draw a spiral Make a new program using counter loop
instead of the long way.

"""

import sys
sys.path.append('..')
import codestudio
import mymod
artist = codestudio.load('s1level65')
zombie = mymod.Zombie(artist)

# zombie.move_forward(25)
# zombie.turn_right(90)
# zombie.move_forward(30)
# zombie.turn_right(90)
# zombie.move_forward(40)
# zombie.turn_right(90)
# zombie.move_forward(45)
# zombie.turn_right(90)
# zombie.move_forward(50)
# zombie.turn_right(90)
# zombie.move_forward(55)
# zombie.turn_right(90)
# zombie.move_forward(60)
# zombie.turn_right(90)
# zombie.move_forward(70)
# zombie.turn_right(90)

zombie.check()
