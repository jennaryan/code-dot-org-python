import turtle
from random import random
#from . import sprite

def flipy(t):
    '''Utility function to use same Cartesian coords as turtle'''
    return (t[0],-t[1],t[2],-t[3])

class Solution():
    lines = []
    number = []

class Log():
    lines = []
    calls = []

class ArtistChallenge():
    '''
    Wraps Python turtle with methods matching the JavaScript from
    the studio.code.org challenges and Artist sections. This is a minimal
    subset of everything Python turtle can do to help encourage students
    to learn turtle and eventually tkinter rather than depend on the
    codestudio module.

    '''

    def __init__(self,config=None):
        self.turtle = turtle.Turtle()
        self.canvas = turtle.getcanvas()
        self.turtle.pensize(7)
        self.pos = tuple(self.turtle.pos())
        self.solution = Solution()
        self.log = Log()
        #self.sprite = sprite.Sprite()
        if config:
            for line in config['lines']:
                self.solution.lines.append(tuple(line))
                self.solution.number = len(self.solution.lines)

    def setup(self):
        '''Setup the display and draw a faded trace as guide'''
        #self.canvas.title("self.
        for line in self.solution.lines:
            self.canvas.create_line(flipy(line), fill='lightgrey',
                    width=7,capstyle='round')
        #input('Ready?')

    def check(self):
        lines = self.log.lines
        solution = self.solution.lines
        number = self.solution.number
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
        return self.turtle.speed(speed)

    def pen_color(self,color):
        if color == 'random':
            color = (random(),random(),random())
        self.calls.append(__name__+'('+str(color)+')')
        return self.turtle.pencolor(color)

    def pen_width(self,width):
        self.calls.append(__name__+'('+str(width)+')')
        return self.turtle.penwidth(width)

    def move_forward(self,amount):
        self.last_pos = tuple(self.turtle.pos())
        self.turtle.forward(amount)
        self.pos = tuple(self.turtle.pos())
        self.log.lines.append(self.last_pos + self.pos)

    def move_backward(self,amount):
        self.last_pos = tuple(self.turtle.pos())
        self.turtle.backward(amount)
        self.pos = tuple(self.turtle.pos())
        self.log.lines.append(self.last_pos + self.pos)

    def jump_backward(self,amount):
        self.turtle.penup()
        self.last_pos = tuple(self.turtle.pos())
        self.turtle.backward(amount)
        self.pos = tuple(self.turtle.pos())
        self.turtle.pendown()

    def jump_forward(self,amount):
        self.turtle.penup()
        self.last_pos = tuple(self.turtle.pos())
        self.turtle.forward(amount)
        self.pos = tuple(self.turtle.pos())
        self.turtle.pendown()

    def turn_right(self,amount):
        #self.sprite.rotate(amount)
        return self.turtle.right(amount)

    def turn_left(self,amount):
        #self.sprite.rotate(-amount)
        return self.turtle.left(amount)

    def save(self,fname='artist.eps'):
        turtle.canvas.postscript(file=fname)
        
