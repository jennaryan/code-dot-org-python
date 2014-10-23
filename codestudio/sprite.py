import tkinter
from os import path
here = path.abspath(path.dirname(__file__))

class Sprite():
    '''Simple graphic sprite class to handle animation and rotation'''
    def __init__(self,canvas=None):
        self.sheet = None
        self.speed = 1

        # used mostly just to display sprites during debugging
        if not canvas:
            root = tkinter.Tk()
            canvas = tkinter.Canvas(root,width=500,height=500)
            canvas.pack()
            self.canvas = canvas
        else:
            self.canvas = canvas

    def from_sheet(self,sheet=None, fname=None, count=1,
            x1=0,y1=0,x2=0,y2=0,dx=0,dy=0,
            cols=None,rows=None,):
        '''
        Load one or more sprite frame images from uniform grid sprite
        sheet either from a file or an existing sheet that has already
        been loaded into memory. Multiple sprites of different sizes can
        reside on the same sheet.
        '''
        self.fname = fname
        self.sheet = sheet

        if sheet:
            # TODO
            pass
        elif fname:
            pass
            #path = path.join(here,'resources','artist','artist.gif' )
            #fname = tkinter.ttk.PhotoImage(file='')
        else:
            raise(ValueError)

    def step(self):
        '''Step to the next animation frame'''
        pass

    def animate(self):
        pass

    def rotate(self,amount):
        print('would rotate')
