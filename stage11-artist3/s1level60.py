"""Stage 11: Puzzle 2 of 11

Welcome to using methods!  Methods are functions that go with a
class, (think classification, not school). Classes let you organize
code into objects so thinking about them makes sense when things
get complicated. This is called object-oriented programming. You
have been using it all along. An `artist` object (also called
an instance) is created every time you write the line `artist =
codestudio.load()`. Then you tell the artist what to do by calling its
methods, `artist.move_forward(100)` for example. Some compare this to
having a cookie cutter (a class) and making cookies (objects or instances)
using it.

In this puzzle we've created a new Zombie class for you below and started
to define the method `draw_square(self)`. The 'self' is a special variable
that we'll talk about later. It contains a reference to the object so this
method function can see and use other stuff in that same object.

Complete the method so that it will draw a small 50x50 green square when
called in the main program.


"""

import sys
sys.path.append('..')

import codestudio

# We have to define the new class here because it extends the parent class
# from codestudio.Artist

class Zombie(codestudio.Artist):
    """An Artist with a propensity for brains and drawing squares.

    While class definitions look like function definitions they are different.
    The parameter inside the parenthesis () is the parent class. This means
    all Zombies are Artists and can do everything an Artist can do.

    The `start_direction` and `speed` are special variables that goes with
    all Zombies. These are called class or static attributes. An attribute
    is a variable that goes with a class or the objects created from a class.
    """

    start_direction = 90            # facing the east, or right of screen
    speed = 'slow'                  # it is a zombie after all
    color = 'green'                 # it is a zombie after all

    def draw_square(self,size):
        pass # <--- TODO replace with code to draw a square

# This following line is standard best  practice to separate classes
# from the main code in Python. Notice how we have to indent.

if __name__ == '__main__':

    artist = codestudio.load('s1level60')

    # This line makes a new zombie who knows everything the artist does.
    # We pass in the original 'artist' so our zombie can borrow his
    # puzzle to look at and his canvas to draw on.

    zombie = Zombie(artist)

    # and more ...
    zombie.draw_square(50)

    zombie.check()
