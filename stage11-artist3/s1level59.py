"""Stage 11: Puzzle 1 of 11

Hello. Me zombie artist. Me love drawing! Help me draw a square in a
special color.  Important note: you have all the same actions just
with a zombie artist now.

"""

import sys
sys.path.append('..')
import codestudio
zombie = codestudio.load('s1level59')

for count in range(4):
    zombie.move(100)
    zombie.right()

zombie.check()
