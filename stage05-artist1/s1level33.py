"""Stage 5: Puzzle 10 of 10

You made it! Now, draw anything you want. Some fun ideas: a stick figure,
snowflake, or spiral. Also try the new `artist.pen.width` setting. Have fun!

"""

import sys
sys.path.append('..')

import codestudio
artist = codestudio.load('s1level33')

# try one of these if you like
#artist.pen.color = 'random'
#artist.pen.width = 1

artist.move_forward(100)

artist.wait()
