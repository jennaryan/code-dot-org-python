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

    def __init__(self,proto=None):
        """In most cases you want Artist.from_json() instead."""

        # aggregate
        if proto:
            self.canvas = proto.canvas 
            self.puzzle = proto.puzzle
            self.log = proto.log
            self.uid = proto.uid
            self.type = proto.type
            self.x = proto.x
            self.y = proto.y 
            self.direction = proto.start_direction
            self.startx = proto.startx
            self.starty = proto.starty
            self.lastx = proto.lastx
            self.lasty = proto.lasty 
            self.last_direction = proto.direction
        else:
            self.canvas = Canvas()
            self.puzzle = []
            self.log = []
            self.uid = None
            self.type = 'artist'
            self.x = self.startx
            self.y = self.starty 
            self.direction = self.start_direction
            self.lastx = self.x
            self.lasty = self.y 
            self.last_direction = self.direction

        self.speed = self.speed           # triggers __setattr__
        self._lines_to_draw = []          # drawing cache

    @property
    def title(self):
        return self.canvas.title

    @title.setter
    def title(self,new):
        self._title = new
        if not new:
            if self.uid:
                self.canvas.title = self.uid
        else:
            if self.uid:
                self.canvas.title = new + '  [' + self.uid + ']'
            else:
                self.canvas.title = new

    @title.deleter
    def title(self):
        self.canvas.title = self.uid

    def config(self,conf):
        """Sets attributes based dictionary (usually after JSON load)."""
        for key in conf:
            if key in ('startx','starty','start_direction'):
                setattr(__class__,key,conf[key])
            if key in ('puzzle','uid','title','type'):
                setattr(self,key,conf[key])

    def pen_color(self,color):
        """Just to be compatible with 'Show Code' JavaScript"""
        self.color = color

    @classmethod
    def from_json(cls,json_):
        if type(json_) is str:
            json_ = json.loads(json_) 
        instance = cls()
        instance.config(json_)
        return instance

    def setup(self):
        self.title = self._title                     # for missing uid
        self.direction = self.start_direction
        self.x = self.startx
        self.y = self.starty
        self.draw_lines(self.puzzle, color='lightgrey', speed='fastest')

    def check(self):
        log = [tuple(l[0:4]) for l in self.log]
        puzzle = [tuple(l[0:4]) for l in self.puzzle]
        number = len(set(puzzle))
        if len(set(log)) != number:
            return self.try_again()
        for line in puzzle:
            backward = (line[2],line[3],line[0],line[1])
            if line not in log and backward not in log:
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
                "title": self._title,
                "startx": self.startx,
                "starty": self.starty,
                "start_direction": self.start_direction,
                "puzzle": self.log
            }))

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

    def clear(self):
        self._lines_to_draw = []
        self.log = []

    def draw_lines(self,lines,color=None,speed=None):
        speed = speed if speed else self.speed
        self.canvas.speed = speed
        if color:
            self.canvas.draw_lines(lines,color=color)
        else:
            self.canvas.draw_lines(lines)

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
        if self.color == 'random':
            color = self.random_color()
        else:
            color = self.color
        line = (self.lastx,self.lasty,self.x,self.y,color,self.width)
        self._lines_to_draw.append(line)
        self.log.append(line)
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
        self.canvas.delay()

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

    random_colour = random_color
    colour_random = random_color
    color_random = random_color
