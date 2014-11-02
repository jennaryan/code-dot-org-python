"""Stage 11: Puzzle 1 of 11

Hello. Me zombie artist. Me love drawing! Help me draw a square in a
special color. Important note: we are using the short forms of the actions
(function calls) now to change things up a bit.

"""

import sys
sys.path.append('..')

import codestudio
zombie = codestudio.load('s1level59')

# TODO finish drawing a square using a repeat (for) loop
zombie.move(100)
zombie.right()

zombie.check()
