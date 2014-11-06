"""Stage 11: Puzzle 2 of 11

Welcome to using methods )!  Methods are functions (or procedures) that
go with a class, (not like in school, like in a classification). Classes
let you organize code into objects. This is called object-oriented
programming. You have been using it all along. An `artist` object (also
called an instance) is created every time you write the line `artist =
codestudio.load()`. Then you tell the artist what to do by calling its
methods, `artist.move_forward(100)` for example.

In this puzzle we've created a new Zombie class for you below and started
to define the method `def draw_square(self):`. Complete the method so that it
will draw a small 50x50 green square when called in the main program.

The `start_direction` and `speed` are special variables that goes with
all Zombies. These are called class or static attributes. An attribute
is a variable that goes with a class or the objects created from a class.

"""

import sys
sys.path.append('..')

import codestudio

# We have to define the new class here because it extends the parent class
# from codestudio.Artist

class Zombie(codestudio.Artist):
    start_direction = 90            # facing the east, or right of screen
    speed = 'slow'                  # it is a zombie after all
    color = 'green'                 # it is a zombie after all

    def draw_square(self,size):
        pass # <--- TODO replace with code to draw a square

# this following line is standard best  practice to separate classes
# from the main code notice how we have to indent

if __name__ == '__main__':

    artist = codestudio.load('s1level60')

    # this line makes a new zombie who knows everything the artist does
    zombie = Zombie(artist)

    # and more ...
    zombie.draw_square(50)

    zombie.check()
