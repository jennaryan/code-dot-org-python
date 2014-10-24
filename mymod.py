'''
As you port add your functions and class extensions here so you can use
them again in other challenges.
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

class Artist(codestudio.Artist):
    def draw_square(self,size):
        for count in range(4):
            self.move_forward(size)
            self.turn_right(90)

#---------------------------------------------------------------------------
'''
Extending a Class: Binding Methods (and Monkey Patching)

Extending a class this way changes the actual class itself rather than
creating a new subclass. We simply define a method and add (bind) it to
a class we've already defined someplace else.

This is commonly found in dynamic languages such as Python, Ruby, Perl
and especially JavaScript where it is the standard way to define classes
in the first place.

Extending this way can even be done while the program is running (or
'runtime') in which case extending this way is called 'monkey patching',
which refers to changing a pre-defined class in any way after the program
has started.  Some frown upon this because they claim it can make the
class hard to keep track of. Others argue this is always better over
the confusion of inheritance.

In this case we are not 'monkey patching' because we add to the class
before the program ever starts.
'''

def draw_square(self,size):
    for count in range(4):
        self.move_forward(size)
        self.turn_right(90)

'''
Here's where the bind happens. Note that 'draw_square' does not have
parentheses '()' after it. This copies the reference to the method instead
of running the method and passing the return value.
'''

codestudio.Artist.draw_square = draw_square

