"""Stage 5: Puzzle 10 of 10

You made it! Now, draw anything you want. Some fun ideas: a stick figure,
snowflake, or spiral. Also try the new `artist.width` setting. Have fun!

"""

import sys
sys.path.append('..')
import codestudio
artist = codestudio.load('s1level33')
for count in range(100):
    artist.color = artist.random_color()
    artist.width = 5
    artist.move_forward(100)
    artist.left(90)
    artist.move(50)

artist.wait()
