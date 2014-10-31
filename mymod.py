'''
Add your functions to this library module to use them again
in other challenges.
'''

import codestudio

def hello_world():
    print("Hello from 'mymod'")

#---------------------------------------------------------------------------
'''
Extending a Class: Subclassing and Inheritance

The traditional way to extend a class is to create a subclass that
inherits everything from the parent class and adds its own methods and
attributes. Strictly typed languages like Java and C++ rely heavily
on inheritance. 

You can even name the class the same as the original as we do in this
example. The module name it belongs to ensures we know which Artist
we are using, (which is why `from codestudio import *` is always evil,
by the way).

Inheritance, while still a standard part of object-oriented programming,
has become the 'evil witch lurking in the forest' (as one author put
it) because it can quickly become overly complicated and hard to keep
track of. You generally know when inheritance is starting to fail you
and other ways of extending should be considered when you start to ask,
"How can I subclass two parent classes?" (multiple inheritance) or "How
can I call the parent class's __init__ and my subclasses as well?" There
are ways of doing these things, but once you start, you've headed down
the dark path of inheritance.
'''

class Artist(codestudio.artist.Artist):
    def draw_square(self,size):
        for count in range(4):
            self.move_forward(size)
            self.turn_right(90)

class ArtistChallenge(codestudio.artist.ArtistChallenge):
    def draw_square(self,size):
        self.artist.draw_square(size)

