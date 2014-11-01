__author__ = 'code.org'
__contributors__ = ['SkilStak Coding Arts']

import codestudio
artist = codestudio.load('s1level41')

# TODO put the following code in a repeat loop
# and add code to draw 10 adjacent squares
# like a ladder

for count in range(10):
    artist.pen.color = 'random'
    for count in range(4):
        artist.move_forward(20)
        artist.turn_right(90)

artist.check()
