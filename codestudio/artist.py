import turtle
#from . import sprite

class Artist():
    '''
    Wraps Python turtle with methods matching the JavaScript from
    the studio.code.org challenges and Artist sections. This is a minimal
    subset of everything Python turtle can do to help encourage students
    to learn turtle and eventually tkinter rather than depend on the
    codestudio module.
    '''

    def __init__(self):
        self._turtle = turtle.Turtle()
        self._turtle.pensize(7)
        #self.sprite = sprite.Sprite()

    def speed(self,speed=None):
        return self._turtle.speed(speed)

    def pen_color(self,color=None):
        return self._turtle.pencolor(color)

    def pen_width(self,width=None):
        return self._turtle.penwidth(width)

    def move_forward(self,amount=None):
        return self._turtle.forward(amount)

    def move_backward(self,amount=None):
        return self._turtle.backward(amount)

    def jump_backward(self,amount=None):
        self._turtle.penup()
        self._turtle.backward(amount)
        self._turtle.pendown()

    def jump_forward(self,amount=None):
        self._turtle.penup()
        self._turtle.forward(amount)
        self._turtle.pendown()

    def turn_right(self,amount=None):
        #self.sprite.rotate(amount)
        return self._turtle.right(amount)

    def turn_left(self,amount=None):
        #self.sprite.rotate(-amount)
        return self._turtle.left(amount)

