r'''The basis for the Artist challenges from <http://code.org> built
on `tkinter` only. 

Artist is similar to the great `turtle` standard module for teaching
programming but builds on a foundation of challenge and solution, (which
`turtle` does not):

- Solutions created by students with Artist can be checked against
  a known solution saved as JSON.

- New challenges can be created with Artist by simply `artist.save()` and
  creating challenge stub programs for students to complete that `load()`
  the saved challenge. 

- Artist has only `move_*`, `turn_*`, and `jump_*` and always uses
  verbs to begin method and function names.

- Artist methods correspond one-to-one with those from <http://code.org>
  for easier porting by students.

- Artist supports sprite animation and theming (e.g. zombie, turtle, etc.).

- Artist includes sound and sound theming as well. 

- Artist can be made to be very slow or very, very fast unlike `turtle`

- Artist metaphor matches 'canvas' metaphor used in all graphics coding.

- Artist draws lines individually instead of updating a single line with
  new coordinates so that the `lineslog` can be checked to see if the
  line was drawn forward or backward and give credit for that specific
  line segment. This allows set() to isolate the essential lines when
  checking solutions without throwing out an otherwise good solution
  that was drawn in a different way. This is critical for code.org
  challenges since often there is more than one way to retrace drawn lines
  to get to a new position.

'''

import json
import random
import os
import math
import datetime

from .canvas import Canvas
from .challenge import Challenge
from .sprite import Sprite

#--------------------------------------------------------------------------

def tstamp():
    return datetime.datetime.now().strftime("%Y%m%d%H%M%S")

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
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        return '#{:02x}{:02x}{:02x}'.format(r,g,b)

#--------------------------------------------------------------------------

class Solution():

    def __init__(self):
        self.lines = []
        self.image = None

    def draw(self,canvas):
        '''Draws solution fast (image) or slow (lines) way'''
        if self.image:
            canvas.draw_image(self)
        else:
            canvas.draw_lines(self.lines,color='lightgrey')

#--------------------------------------------------------------------------

class Artist():
    logging = True

    def __init__(self,canvas=None,pen=None,lines=[],
            startx=0,starty=0,start_direction=0,
            speed=20,challenge=None):
        self.canvas = canvas if canvas else Canvas(startx,starty)
        self.canvas.centerx = startx
        self.canvas.centery = starty
        self.pen = pen if pen else Pen()
        self.lines = lines
        self._cache = []
        self.startx = startx
        self.starty = starty
        self.x = 0                       # relative to artist, not canvas
        self.y = 0
        self.lastx = self.x
        self.lasty = self.y
        self.direction = start_direction 
        self.start_direction = start_direction
        self.last_direction = 0
        self.speed = speed

    def __setattr__(self,name,value):
        if name == 'speed':
            self.canvas.speed = value
        super().__setattr__(name,value)

    def __str__(self):
        return json.dumps(self._json())

    def _json(self):
        return {
            "type" : 'artist',
            "lines" : self.lines,
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
        }

    def save(self,name=None,fname=None):
        if os.path.isdir('challenges'):
            fname = os.path.join('challenges', name + '.json')
            assert not os.path.isfile(fname), '{} exists'.format(name)
        else:
            fname = name + '.json' 
        if not name and not fname:
            name = os.path.splitext(os.path.basename(__file__))[0]
            name = name + tstamp()
        with open(fname,'w') as f:
            f.write(str(self))

    def clear(self):
        self._cache = []
        self.lines = []

    def draw(self):
        self.canvas.draw_lines(self._cache)
        self._cache = []

    @staticmethod
    def xy_plus_vec(x=0,y=0,direction=0,amount=0):
        '''Returns a new (x,y) coordinate after adding the amount in
        the given direction
        '''
        newx = math.sin(math.radians(direction)) * amount + x
        newy = math.cos(math.radians(direction)) * amount + y
        return (newx,newy)

    def _move(self,amount):
        (self.x,self.y) = self.xy_plus_vec(self.x,self.y,
                                           self.direction,amount)

    def move(self,amount):
        self.lastx = self.x
        self.lasty = self.y
        self._move(amount)
        line = (self.lastx,self.lasty,self.x,self.y,
                self.pen.color,self.pen.width)
        self._cache.append(line)
        if self.logging:
            self.lines.append(line)
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
        self.canvas.delay()

    def turn_right(self,amount=90):
        self.turn(amount)

    def turn_left(self,amount=90):
        self.turn(-amount)

#--------------------------------------------------------------------------

class ArtistChallenge(Challenge):

    def __init__(self,config=None):
        self.solution = Solution()
        title = 'Artist'
        self.uid = 'code.org'
        self.startx = 0
        self.starty = 0
        self.start_direction = 0
        if config:
            config_keys = config.keys()
            if 'uid' in config_keys:
                self.uid = config['uid']
                title += ' ({})'.format(self.uid)
            if 'title' in config_keys:
                title += ' {}'.format(config['title'])
            if 'start-direction' in config_keys:
                self.start_direction = config['start-direction']
            if 'startx' in config_keys:
                self.startx = config['startx']
            if 'starty' in config_keys:
                self.starty = config['starty']
            if 'lines' in config_keys:
                for line in config['lines']:
                    self.solution.lines.append(tuple(line))
        # composition
        self.canvas = Canvas(self.startx,self.starty)
        self.artist = Artist(self.canvas,startx=self.startx,starty=self.starty,
                start_direction=self.start_direction)
        self.pen = self.artist.pen
        self.title = title

    def setup(self):
        self.solution.draw(self.canvas)

    def draw_solution(self):
        print(self.canvas)
        return self.solution.draw(self.canvas)

    def save(self):
        return self.artist.save(self.uid)

    def check(self):
        lines = [tuple([round(n) for n in l[0:4]]) for l in self.artist.lines]
        solution = [tuple([round(n) for n in l[0:4]]) for l in self.solution.lines]
        number = len(set(solution))
        if len(set(lines)) != number:
            return self.try_again()
        for line in solution:
            backward = (line[2],line[3],line[0],line[1])
            if line not in lines and backward not in lines:
                print('solution line:',line)
                return self.try_again()
        return self.good_job()

    def try_again(self,message='Nope. Try again.'):
        # TODO replace with a canvas splash window graphic
        print(message)
        self.canvas.exit_on_click()

    def good_job(self,message='Perfect! Congrats!'):
        # TODO replace with a canvas splash window graphic
        print(message)
        self.canvas.exit_on_click()

    def wait_for_click(self):
        return self.good_job('Beautiful!')

    wait = wait_for_click

    def speed(self,speed):
        return self.artist.speed(speed)

    def move(self,amount):
        return self.artist.move(amount)

    move_forward = move

    def forward(self,amount=100):
        return self.move(amount)

    def move_backward(self,amount=100):
        return self.move(-amount)

    def backward(self,amount=100):
        return self.move(-amount)

    def jump(self,amount):
        return self.artist.jump(amount)

    jump_forward = jump

    def jump_backward(self,amount=100):
        return self.jump(-amount)

    def turn(self,amount):
        return self.artist.turn(amount)

    turn_right = turn

    def right(self,amount=90):
        return self.turn(amount)

    def turn_left(self,amount=90):
        return self.artist.turn(-amount)

    def left(self,amount=90):
        return self.turn(-amount)

    def save_eps(self,name=__name__):
        self.canvas.save_eps(name)
