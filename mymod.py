"""Example module to contain functions and variables to reuse.

This file gets loaded as a module (sometimes also called a library) when
you call `import mymod` in your scripts.

"""

import codestudio

class Artist(codestudio.artist.Artist):

    def draw_square(self,size):
        for count in range(4):
            self.move(size)
            self.right()

