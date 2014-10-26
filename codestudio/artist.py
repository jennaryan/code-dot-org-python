import turtle
from random import random
#from . import sprite

def flipy(t):
    '''Utility function to use same Cartesian coords as turtle'''
    return (t[0],-t[1],t[2],-t[3])

class Solution():
    '''
    Contains the solution for a given challenge against
    which everything can be tested and which can be displayed
    in greyed out form or image form to illustrate what needs
    to be done graphically.
    '''

    lines = []
    number = []
    image = None
    canvas = None

    def draw_image(self,canvas=None):
        '''Faster method to display the solution'''
        if not canvas: canvas = self.canvas
        pass

    def draw_lines(self,canvas=None):
        if not canvas: canvas = self.canvas
        for line in self.lines:
            canvas.create_line(flipy(line), fill='lightgrey',
                    width=7,capstyle='round',arrow=None)

    def draw(self,canvas=None):
        '''Draws solution fast (image) or slow (lines) way'''
        if not canvas: canvas = self.canvas
        if self.image:
            return self.draw_image(canvas)
        else:
            return self.draw_lines(canvas)

class Log():
    '''Keeps track of all the lines and calls made.'''
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
        self.uid = 'code.org'
        self.title = 'Artist'
        self.solution = Solution()
        self.turtle = turtle.Turtle()
        self.turtle.pensize(7)
        self.pos = tuple(self.turtle.pos())
        self.log = Log()
        self.screen = turtle.Screen()
        self.canvas = self.screen.getcanvas()
        #self.sprite = sprite.Sprite()
        if config:
            config_keys = config.keys()
            if 'uid' in config_keys:
                self.uid = config['uid']
                self.title += ' ({})'.format(self.uid)
            if 'title' in config_keys:
                self.title += ' {}'.format(config['title'])
            for line in config['lines']:
                self.solution.lines.append(tuple(line))
                self.solution.number = len(self.solution.lines)
        self.screen.title(self.title)

    def setup(self):
        self.solution.draw(self.canvas)
        input('Ready?')

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
        
