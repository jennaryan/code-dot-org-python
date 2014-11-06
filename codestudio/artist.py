"""Artist puzzles from <http://code.org> built on `tkinter` only. 

Artist is similar to the great `turtle` standard module for teaching
programming but builds on a foundation of challenge and solution, (which
`turtle` does not):

- Subset of basic Python turtle commands (all needed for puzzles).

- Puzzles created by students with Artist can be checked against
  a known solution saved as JSON.

- New puzzles can be created with Artist by simply `artist.save()` and
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
  new coordinates so that the artists drawn `lines` can be checked to
  see if the line was drawn forward or backward and give credit for that
  specific line segment. This allows set() to isolate the essential lines
  when checking solutions without throwing out an otherwise good solution
  that was drawn in a different way. This is critical for code.org puzzles
  since often there is more than one way to retrace drawn lines to get
  to a new position.

"""

import os
import json
import math
import random

from .canvas import Canvas

class Artist():
    start_direction = 0
    startx = 0
    starty = 0
    color = 'black'
    width = 7
    speed = 'normal'

    def __init__(self,canvas=None):
        """In most cases you want Artist.from_json() instead."""
        self.uid = None
        self.type = 'artist'

        # aggregate
        self._canvas = canvas if canvas else Canvas()
        self.puzzle = []
        self.lines = []                   # logged
        self._lines_to_draw = []          # drawing cache

        self.x = 0                       # relative to artist, not canvas
        self.y = 0
        self.direction = 0

        self.lastx = 0
        self.lasty = 0
        self.last_direction = 0

    def __setattr__(self,name,value):
        if name == 'speed':
            self._canvas.speed = value
        if name == 'color':
            if value == 'random':
                value = self.random_color()
        super().__setattr__(name,value)

    @property
    def canvas(self):
        return self._canvas

    @canvas.setter
    def canvas(self,other):
        self._canvas = other

    def config(self,conf):
        """Sets attributes based dictionary (usually after JSON load)."""
        for key in conf:
            if key in ('startx','starty','start_direction'):
                setattr(__class__,key,conf[key])
            if key in ('puzzle','uid','title','type'):
                setattr(self,key,conf[key])

    @classmethod
    def from_json(cls,json_):
        if type(json_) is str:
            json_ = json.loads(json_) 
        instance = cls()
        instance.config(json_)
        return instance

    def setup(self):
        self.direction = self.start_direction
        self.x = self.startx
        self.y = self.starty
        self.speed = 'fastest'
        self.draw_lines(self.puzzle, color='lightgrey')
        self.speed = 'normal'

    def set_color(self,value):
        self.color = value 
        return self.color

    pencolor = set_color

    def set_width(self,value):
        self.width = value 
        return self.color

    penwidth = set_width
    pensize = penwidth

    def check(self):
        lines = [tuple([round(n) for n in l[0:4]]) for l in self.lines]
        puzzle = [tuple([round(n) for n in l[0:4]]) for l in self.puzzle]
        number = len(set(puzzle))
        if len(set(lines)) != number:
            return self.try_again()
        for line in puzzle:
            backward = (line[2],line[3],line[0],line[1])
            if line not in lines and backward not in lines:
                return self.try_again()
        return self.good_job()

    def save(self,name=None,fname=None):
        name = name if name else self.uid
        if os.path.isdir('puzzles'):
            fname = os.path.join('puzzles', name + '.json')
            assert not os.path.isfile(fname), '{} exists'.format(name)
        else:
            fname = name + '.json' 
        with open(fname,'w') as f:
            f.write(json.dumps({
                "uid": self.uid,
                "type": self.type,
                "startx": self.startx,
                "starty": self.starty,
                "start_direction": self.start_direction,
                "puzzle": self.lines
            }))

    def try_again(self,message='Nope. Try again.'):
        # TODO replace with a canvas splash window graphic
        print(message)
        self._canvas.exit_on_click()

    def good_job(self,message='Perfect! Congrats!'):
        # TODO replace with a canvas splash window graphic
        print(message)
        self._canvas.exit_on_click()

    def wait_for_click(self):
        return self.good_job('Beautiful!')

    wait = wait_for_click

    def clear(self):
        self._lines_to_draw = []
        self.lines = []

    def draw_lines(self,lines,color=None):
        if color:
            self._canvas.draw_lines(lines,color=color)
        else:
            self._canvas.draw_lines(lines)

    def draw(self):
        self.draw_lines(self._lines_to_draw)
        self._lines_to_draw = []

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
                self.color,self.width)
        self._lines_to_draw.append(line)
        self.lines.append(line)
        self.draw()

    move_forward = move
    forward = move
    fd = move

    def move_backward(self,amount):
        self.move(-amount)

    backward = move_backward
    back = move_backward
    bk = move_backward

    def jump(self,amount):
        self._move(amount)

    jump_forward = jump

    def jump_backward(self,amount):
        self.jump(-amount)

    def turn(self,amount):
        self.last_direction = self.direction
        self.direction += amount
        self._canvas.delay()

    def turn_right(self,amount=90):
        self.turn(amount)

    right = turn_right
    rt = turn_right

    def turn_left(self,amount=90):
        self.turn(-amount)

    left =  turn_left
    lt = turn_left

    @staticmethod
    def random_color():
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        return '#{:02x}{:02x}{:02x}'.format(r,g,b)
