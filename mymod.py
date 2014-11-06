"""Example module to contain methods, functions and variables for reuse.

This file gets loaded as a module (sometimes also called a library) when
you call `import mymod` in your scripts.

"""

import codestudio

class Zombie(codestudio.Artist):
    start_direction = 90            # facing the east, or right of screen
    speed = 'slow'                  # it is a zombie after all
    color = 'red'                   # it is a zombie after all

    def draw_square(self,size):
        for count in range(4):
            self.move(size)
            self.right()
