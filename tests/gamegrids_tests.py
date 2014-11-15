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
        self.grid.init(3,2,'~')
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

    def draw_line_test(self):
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
        eq_(self.grid.to_text(),string)

def length_test():
    eq_(gg.length((0,0,1,3)),math.sqrt((1-2)**2+(3-0)**2))

def xy_test():
    end = tuple(round(n) for n in gg.xy(1,3,30,2))
    eq_(end,(2,5))
