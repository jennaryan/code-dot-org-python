"""Example module to contain methods, functions and variables for reuse.

This file gets loaded as a module (sometimes also called a library) when
you call `import mymod` in your scripts.

"""

import codestudio

class Artist(codestudio.Artist):

    def draw_square(self,size):
        for count in range(4):
            self.move(size)
            self.right()

