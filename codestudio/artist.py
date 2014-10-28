r"""The basis for the Artist challenges from <http://code.org> built
on `tkinter` only. 

Artist is a similar to the great `turtle` standard module for teaching
programming but with these main differences:

- Artist has only `move_*`, `turn_*`, and `jump_*` and always uses
  verbs to begin method and function names.

- Artist methods correspond one-to-one with those from <http://code.org>
  for easier porting by students.

- Artist supports sprite animation and theming (e.g. zombie, turtle, etc.).

- Artist includes sound and sound theming as well. 

- Artist can be made to be very slow or very, very fast unlike `turtle`

- Artist metaphor matches 'canvas' metaphor used in all graphics coding.

- Artist challenge and solution paths can be loaded and saved in JSON

"""

import tkinter as tk
import random as r
from .canvas import Canvas
from .challenge import Challenge

def flipy(line):
    return (line[0],-line[1],line[2],-line[3])

#--------------------------------------------------------------------------

class Pen():
    """Gimme somethin' to write with, man."""

    def __init__(self):
        self.on = True
        self.color = 'black'
        self.width = 7

    @staticmethod
    def random_color():
        return (r.random(),r.random(),r.random())

#--------------------------------------------------------------------------

class Solution():

    def __init__(self):
        self.lines = []
        self.number_lines = []
        self.image = None

    def draw(self,canvas):
        '''Draws solution fast (image) or slow (lines) way'''

        if self.image:
            return self._draw_image(canvas)
        else:
            return self._draw_lines(canvas)

    def _draw_lines(self,canvas):
        for line in self.lines:
            canvas.create_line(flipy(line), fill='lightgrey',
                    width=7,capstyle='round',arrow=None)

    def _draw_image(self,canvas):
        pass

#--------------------------------------------------------------------------

class Log():
    '''Keeps track of all the lines and calls made.'''
    lines = []
    calls = []

#--------------------------------------------------------------------------

class Artist():
    def __init__(self,canvas=None,pen=Pen(),log=Log()):
        self.canvas = canvas if canvas else Canvas()
        self.pen = pen
        self.log = log
        self.x = canvas.centerx
        self.y = canvas.centery
        self.lastx = self.x
        self.lasty = self.y

    def move_forward(self,amount):
        pass
        """self.last_pos = tuple(self.artist.pos())
        self.artist.forward(amount)
        self.pos = tuple(self.artist.pos())
        self.log.lines.append(self.last_pos + self.pos)
        """

    def move_backward(self,amount):
        pass

    def jump_forward(self,amount):
        pass

    def jump_backward(self,amount):
        pass

    def turn_left(self,amount):
        pass

    def turn_right(self,amount):
        pass

#--------------------------------------------------------------------------

class ArtistChallenge(Challenge):

    def __init__(self,config=None):
        self.solution = Solution()
        self.canvas = Canvas()
        self.artist = Artist(self.canvas)
        self.uid = 'code.org'
        self.title = 'Artist'
        if config:
            config_keys = config.keys()
            if 'uid' in config_keys:
                self.uid = config['uid']
                self.title += ' ({})'.format(self.uid)
            if 'title' in config_keys:
                self.title += ' {}'.format(config['title'])
            for line in config['lines']:
                self.solution.lines.append(tuple(line))
                self.solution.number_lines = len(self.solution.lines)

    def setup(self):
        self.solution.draw(self.canvas)
        input('Ready?')

    def draw_solution(self):
        return self.solution.draw(self.canvas)

    def check(self):
        lines = self.log.lines
        solution = self.solution.lines
        number = self.solution.number_lines
        if len(set(lines)) != number:
            return self.try_again('Need more.')
        for line in solution:
            backward = (line[2],line[3],line[0],line[1])
            if line not in lines and backward not in lines:
                return self.try_again('Missing' + str(line))
        return self.good_job()

    def try_again(self,msg=''):
        print('Nope.',msg)
        input()
        return False

    def good_job(self,msg=None):
        print('Perfect! Congrats!')
        input()
        return True

    def speed(self,speed):
        return self.artist.speed(speed)

    def move_forward(self,amount):
        return self.artist.move_forward(amount)

    def move_backward(self,amount):
        return self.artist.move_backward(amount)

    def jump_backward(self,amount):
        return self.artist.jump_backward(amount)

    def jump_forward(self,amount):
        return self.artist.jump_forward(amount)

    def turn_right(self,amount):
        return self.artist.turn_right(amount)

    def turn_left(self,amount):
        return self.artist.turn_left(amount)

    def save(self,name=__name__):
        self.canvas.save(name)
        
if __name__ == '__main__':
    print(Pen.random_color())
    print(Pen().random_color())
