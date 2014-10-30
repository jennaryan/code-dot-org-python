r'''The basis for the Artist challenges from <http://code.org> built
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

'''

import tkinter as tk
import random
from .canvas import Canvas
from .challenge import Challenge
from math import radians,sin,cos
from codecs import encode
import json
import logging as log
log.basicConfig(level=log.DEBUG)

#--------------------------------------------------------------------------

class Pen():
    '''Gimme somethin' to write with, man.'''

    def __init__(self):
        self.on = True
        self.color = 'black'
        self.width = 7

    def __setattr__(self,name,value):
        if name == 'color':
            if value == 'random':
                value = self.random_color()
        super().__setattr__(name,value)

    @staticmethod
    def random_color():
        log.debug('random_color()')
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        return '#{:02x}{:02x}{:02x}'.format(r,g,b)

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
            canvas.create_line(canvas.flipy(line), fill='lightgrey',
                    width=7,capstyle='round',arrow=None)

    def _draw_image(self,canvas):
        pass

#--------------------------------------------------------------------------

class TooManyLines(Exception):
    pass

#--------------------------------------------------------------------------

class Artist():
    maxlines = 10000
    wait_for_draw = True
    logging = True

    def __init__(self,canvas=None,pen=None,linelog=[],
            startx=0,starty=0,start_direction=0):
        self.canvas = canvas if canvas else Canvas()
        self.pen = pen if pen else Pen()
        self.linelog = linelog
        self.linecount = 0
        self._cache = []
        self.startx = startx
        self.starty = starty
        self.x = startx
        self.y = starty
        self.lastx = self.x
        self.lasty = self.y
        self.direction = 0
        self.start_direction = start_direction
        self.last_direction = 0

    def __str__(self):
        return json.dumps({
            "linelog" : self.linelog,
            "linecount" : self.linecount,
            "startx": self.startx,
            "starty": self.starty,
            "lastx": self.lastx,
            "lasty": self.lasty,
            "x": self.x,
            "y": self.y,
            "start-direction": self.start_direction,
            "direction": self.direction,
            "pen": {
                "color": self.pen.color,
                "width": self.pen.width
            }
        })

    def clear(self):
        self._cache = []
        self.linelog = []
        self.linecount = 0

    def draw(self):
        for line in self._cache:
            self.canvas.draw_line(line,color=self.pen.color)
        self._cache = []

    @staticmethod
    def xy_plus_vec(x=0,y=0,direction=0,amount=0):
        '''Returns a new (x,y) coordinate after adding the amount in
        the given direction
        '''
        newx = round(sin(radians(direction)) * amount) + x
        newy = round(cos(radians(direction)) * amount) + y
        return (newx,newy)

    def _move(self,amount):
        (self.x,self.y) = self.xy_plus_vec(self.x,self.y,
                                           self.direction,amount)

    def move(self,amount):
        if self.linecount >= self.maxlines:
            raise TooManyLines
        self.lastx = self.x
        self.lasty = self.y
        self._move(amount)
        line = (self.lastx,self.lasty,self.x,self.y)
        self._cache.append(line)
        if self.logging:
            self.linelog.append(line)
        if not self.wait_for_draw:
            self.draw()

    move_forward = move

    def move_backward(self,amount):
        self.move(-amount)

    def jump(self,amount):
        self._move(amount)

    jump_forward = jump

    def jump_backward(self,amount):
        self.jump(-amount)

    def turn(self,amount):
        self.last_direction = self.direction
        self.direction += amount

    def turn_right(self,amount=90):
        self.turn(amount)

    def turn_left(self,amount=90):
        self.turn(-amount)

#--------------------------------------------------------------------------

class ArtistChallenge(Challenge):

    def __init__(self,config=None):
        self.solution = Solution()
        self.canvas = Canvas()
        self.artist = Artist(self.canvas)
        self.pen = self.artist.pen
        self.uid = 'code.org'
        self.title = 'Artist'
        if config:
            config_keys = config.keys()
            if 'uid' in config_keys:
                self.uid = config['uid']
                self.title += ' ({})'.format(self.uid)
            if 'title' in config_keys:
                self.title += ' {}'.format(config['title'])
            if 'start-direction' in config_keys:
                self.artist.direction = config['start-direction']
            for line in config['lines']:
                self.solution.lines.append(tuple(line))
                self.solution.number_lines = len(self.solution.lines)

    def setup(self):
        self.solution.draw(self.canvas)

    def draw_solution(self):
        return self.solution.draw(self.canvas)

    def check(self):
        self.artist.draw()
        lines = self.artist.linelog
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

    def move(self,amount):
        return self.artist.move(amount)

    move_forward = move

    def move_backward(self,amount):
        return self.move(-amount)

    def jump(self,amount):
        return self.artist.jump(amount)

    jump_forward = jump

    def jump_backward(self,amount):
        return self.jump(-amount)

    def turn(self,amount):
        return self.artist.turn(amount)

    turn_right = turn

    def turn_left(self,amount):
        return self.artist.turn_left(amount)

    def save_eps(self,name=__name__):
        self.canvas.save_eps(name)
        
if __name__ == '__main__':
    print(Pen.random_color())
    print(Pen().random_color())

    def turn_right(self,amount):
        return self.artist.turn_right(amount)

    def turn_left(self,amount):
        return self.artist.turn_left(amount)

    def save(self,name=__name__):
        self.canvas.save(name)
        
if __name__ == '__main__':
    print(Pen.random_color())
    print(Pen().random_color())
