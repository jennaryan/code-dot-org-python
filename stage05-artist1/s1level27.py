"""Stage 5: Puzzle 4 of 10

Draw a triangle whose sides are all in different colors. Hint: you'll have to
figure out how far to turn by testing different values for the
`turn_right(degrees)` function.

"""

import sys
sys.path.append('..')

import codestudio
artist = codestudio.load('s1level27')

for count in range(3):
    artist.color = 'random'
    
artist.check()
