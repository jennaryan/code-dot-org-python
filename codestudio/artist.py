import turtle
from random import random
#from . import sprite

class Artist():
    '''
    Wraps Python turtle with methods matching the JavaScript from
    the studio.code.org challenges and Artist sections. This is a minimal
    subset of everything Python turtle can do to help encourage students
    to learn turtle and eventually tkinter rather than depend on the
    codestudio module.
    '''

    # TODO log each pixel drawn (no color) to check if correct

    def __init__(self):
        self._turtle = turtle.Turtle()
        self._turtle.pensize(7)
        self.pos = tuple(self._turtle.pos())
        self.lines = []
        self.calls = []
        #self.sprite = sprite.Sprite()

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
        self.lines.append(self.last_pos + self.pos)

    def move_backward(self,amount):
        self.last_pos = tuple(self._turtle.pos())
        self._turtle.backward(amount)
        self.pos = tuple(self._turtle.pos())
        self.lines.append(self.last_pos + self.pos)

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
        
