"""Stage 5: Puzzle 2 of 10

Now, draw a square. NOTE: tell the artist to use your favorite color pen
by assigning a color or 'random' to the `artist.pen.color` variable.

"""

import sys
sys.path.append('..')

import codestudio
artist = codestudio.load('s1level25')

# TODO draw a square using 11 code-lines or less
artist.color= 'red'
artist.move_forward(100)

artist.check()
