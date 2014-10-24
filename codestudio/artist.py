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
        self.pos = self._turtle.pos()
        #self.sprite = sprite.Sprite()

    def speed(self,speed):
        return self._turtle.speed(speed)

    def pen_color(self,color):
        if color == 'random':
            return self._turtle.pencolor((random(),random(),random()))
        else:
            return self._turtle.pencolor(color)

    def pen_width(self,width):
        return self._turtle.penwidth(width)

    def move_forward(self,amount):
        return self._turtle.forward(amount)

    def move_backward(self,amount):
        return self._turtle.backward(amount)

    def jump_backward(self,amount):
        self._turtle.penup()
        self._turtle.backward(amount)
        self._turtle.pendown()

    def jump_forward(self,amount):
        self._turtle.penup()
        self._turtle.forward(amount)
        self._turtle.pendown()

    def turn_right(self,amount):
        #self.sprite.rotate(amount)
        return self._turtle.right(amount)

    def turn_left(self,amount):
        #self.sprite.rotate(-amount)
        return self._turtle.left(amount)

    def save(self,fname='artist.eps'):
        turtle.getscreen().getcanvas().postscript(file=fname)
        

