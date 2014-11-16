import sys
import math
sys.path.append('..')
import codestudio.gamegrids as gg
from nose.tools import eq_

class TestXYGrid():

    def setup(self):
        self.grid = gg.XYGrid()

    def defaults_test(self):
        eq_(self.grid,[[]])

    def init_test(self):
        eq_(self.grid.init(3,2,'~'), self.grid)
        eq_(self.grid,[['','',''],['','~','~',],['','~','~'],['','~','~']])
        self.grid[1][1] = '*'
        eq_(self.grid,[['','',''],['','*','~',],['','~','~'],['','~','~']])
        self.grid.init(10,10,0)
        self.grid[4][7] = '*'
        tenxten = [
            ['', '', '', '', '', '', '', '', '', '', ''],
            ['', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            ['', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            ['', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            ['', 0, 0, 0, 0, 0, 0, '*', 0, 0, 0],
            ['', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            ['', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            ['', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            ['', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            ['', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            ['', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]
        eq_(self.grid,tenxten)

    def to_text_test(self):
        self.grid.init(3,2,'~')
        self.grid[1][1] = '*'
        eq_(self.grid.to_text(),'* ~ ~ \n~ ~ ~ \n')

    def draw_line_1m_test(self):
        self.grid.init(10,10,'~')
        self.grid.draw_line((1,1,4,4),'*')
        string = ("* ~ ~ ~ ~ ~ ~ ~ ~ ~ \n"
                  "~ * ~ ~ ~ ~ ~ ~ ~ ~ \n"
                  "~ ~ * ~ ~ ~ ~ ~ ~ ~ \n"
                  "~ ~ ~ * ~ ~ ~ ~ ~ ~ \n"
                  "~ ~ ~ ~ ~ ~ ~ ~ ~ ~ \n"
                  "~ ~ ~ ~ ~ ~ ~ ~ ~ ~ \n"
                  "~ ~ ~ ~ ~ ~ ~ ~ ~ ~ \n"
                  "~ ~ ~ ~ ~ ~ ~ ~ ~ ~ \n"
                  "~ ~ ~ ~ ~ ~ ~ ~ ~ ~ \n"
                  "~ ~ ~ ~ ~ ~ ~ ~ ~ ~ \n")
        eq_(self.grid.to_text(),string)

    def draw_lines_test(self):
        self.grid.init(10,10,'~')
        self.grid.draw_lines([(1,1,4,4),(10,0,10,10)],'*')
        string = ("* ~ ~ ~ ~ ~ ~ ~ ~ * \n"
                  "~ * ~ ~ ~ ~ ~ ~ ~ * \n"
                  "~ ~ * ~ ~ ~ ~ ~ ~ * \n"
                  "~ ~ ~ * ~ ~ ~ ~ ~ * \n"
                  "~ ~ ~ ~ ~ ~ ~ ~ ~ * \n"
                  "~ ~ ~ ~ ~ ~ ~ ~ ~ * \n"
                  "~ ~ ~ ~ ~ ~ ~ ~ ~ * \n"
                  "~ ~ ~ ~ ~ ~ ~ ~ ~ * \n"
                  "~ ~ ~ ~ ~ ~ ~ ~ ~ * \n"
                  "~ ~ ~ ~ ~ ~ ~ ~ ~ * \n")
        print(self.grid.to_text())
        eq_(self.grid.to_text(),string)
        assert False

def length_test():
    eq_(gg.length((0,0,1,3)),math.sqrt((1-2)**2+(3-0)**2))

def xy_test():
    end = tuple(round(n) for n in gg.xy(1,3,30,2))
    eq_(end,(2,5))

def slope_test():
    lines = {
        (0,0,1,1): 1.0,
        (1,1,2,2): 1.0,
        (1,1,1,1): None,
        (1,2,2,2): 0.0,
        (2,2,-1,-1): 1.0,
        (0,0,2,3): 1.5,
        (0,0,3,2): 2/3,
        (5,0,10,0): 0.0,
    }
    for line in lines:
        eq_(gg.slope(line),lines[line])

'''
def y_of_test():
    arglist = [
        [(0,0,1,1),1,1],
        [(0,0,1,1),2,2],
        [(0,0,0,0),2,None],
        [(1,0,3,0),2,0],
    ]
    for args in arglist:
        line,x,y = args
        eq_(gg.y_of(line,x),y)

def bounded_y_of_test():
    arglist = [
        [(0,0,1,1),1,1],
        [(0,0,-1,-1),-0.5,-0.5],
        [(0,0,1,1),2,1],
        [(0,0,-1,-1),2,0],
        [(0,0,-1,-1),-2,-1],
        [(0,0,0,0),2,None],
        [(1,0,3,0),2,0],
    ]
    for args in arglist:
        line,x,y = args
        print(line,x)
        eq_(gg.bounded_y_of(line,x),y)
'''

