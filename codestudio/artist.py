import turtle
from random import random
#from . import sprite

class Solution():
    lines = []
    number = []

class Log():
    lines = []
    calls = []

class Artist():
    '''
    Wraps Python turtle with methods matching the JavaScript from
    the studio.code.org challenges and Artist sections. This is a minimal
    subset of everything Python turtle can do to help encourage students
    to learn turtle and eventually tkinter rather than depend on the
    codestudio module.
    '''

    def __init__(self,config=None):
        self._turtle = turtle.Turtle()
        self._turtle.pensize(7)
        self.pos = tuple(self._turtle.pos())
        self.solution = Solution()
        self.log = Log()
        #self.sprite = sprite.Sprite()
        for line in config['lines']:
            self.solution.lines.append(tuple(line))
            self.solution.number = len(self.solution.lines)

    def setup(self):
        '''Setup the display and draw a faded trace as guide'''
        pass

    def check(self):
        lines = self.log.lines
        number = self.solution.number
        if len(set(self.log.lines)) != number:
            return self.try_again('Need more.')
        for line in self.solution.lines:
            backward = (line[2],line[3],line[0],line[1])
            if line not in lines and backward not in lines:
                return self.try_again('Missing',line)
        return self.good_job()

    def try_again(self,msg=''):
        # TODO spice this up
        print('Nope.',msg)
        return False

    def good_job(self,msg=None):
        # TODO spice this up
        print('Perfect! Congrats!')
        return True

    def speed(self,speed):
        return self._turtle.speed(speed)

    def pen_color(self,color):
        if color == 'random':
            color = (random(),random(),random())
        self.calls.append(__name__+'('+str(color)+')')
        return self._turtle.pencolor(color)

    def pen_width(self,width):
        self.calls.append(__name__+'('+str(width)+')')
        return self._turtle.penwidth(width)

    def move_forward(self,amount):
        self.last_pos = tuple(self._turtle.pos())
        self._turtle.forward(amount)
        self.pos = tuple(self._turtle.pos())
        self.log.lines.append(self.last_pos + self.pos)

    def move_backward(self,amount):
        self.last_pos = tuple(self._turtle.pos())
        self._turtle.backward(amount)
        self.pos = tuple(self._turtle.pos())
        self.log.lines.append(self.last_pos + self.pos)

    def jump_backward(self,amount):
        self._turtle.penup()
        self.last_pos = tuple(self._turtle.pos())
        self._turtle.backward(amount)
        self.pos = tuple(self._turtle.pos())
        self._turtle.pendown()

    def jump_forward(self,amount):
        self._turtle.penup()
        self.last_pos = tuple(self._turtle.pos())
        self._turtle.forward(amount)
        self.pos = tuple(self._turtle.pos())
        self._turtle.pendown()

    def turn_right(self,amount):
        #self.sprite.rotate(amount)
        return self._turtle.right(amount)

    def turn_left(self,amount):
        #self.sprite.rotate(-amount)
        return self._turtle.left(amount)

    def save(self,fname='artist.eps'):
        turtle.getscreen().getcanvas().postscript(file=fname)
        
