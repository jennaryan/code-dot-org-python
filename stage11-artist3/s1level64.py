"""Stage 11: Puzzle 6 of 11

Ok, this program will use a counter, to draw the same squares as last
time. You want the square to be the same size as the counter, so use the
"counter" loop. Here's how.

Counter loops are the same as the simple `for count in range(4):` loops
just with extra numbers inside the parenthesis and instead of ignoring
the `count` variable that gets set every time through the loop we name is
`counter` and use it in the loop in place of something else. It doesn't
have to be named `counter` but we use that name for consistency in these
puzzles. 

    for counter in range(5,50,5):
        print(counter)

The first number is the one to start with, the second the one to end with,
and the third is how much to count by.

Note how much cleaner Python loops are than the ones used in JavaScript
(from 'Show Code') and other languages.

"""

import sys
sys.path.append('..')

import codestudio
import mymod
artist = codestudio.load('s1level63')
zombie = mymod.Zombie(artist)
zombie.speed = 'fast'

for counter in range(50,90,10):
    zombie.draw_square()  # TODO fix me

zombie.check()
