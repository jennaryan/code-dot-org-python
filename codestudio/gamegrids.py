from collections import UserList
import math

class XYGrid(UserList):
    """Traditional coordinate game grid.

    grid = XYGrid().init(10,10,'~')
    grid[1][2] = '*'
    print(grid)

    """

    def __init__(self,value=[[]]):
        self.data = value

    def init(self,xsize=0,ysize=0,value=None):
        self.xsize = xsize
        self.ysize = ysize
        self.data = [[value for y in range(ysize+1)] for x in range(xsize+1)]
        for x in range(xsize+1):
            self.data[x][0] = ''
        for y in range(ysize+1):
            self.data[0][y] = ''

    def to_text(self):
        d = self.data
        string = ''
        for y in range(self.ysize):
            for x in range(self.xsize):
                string += d[x+1][y+1] + ' '
            string += "\n"
        return string

    def draw_line(self,line,value=1):
        (x1,y1,x2,y2) = line
        angle = bearing(line)
        self.data[x1][y1] = value
        self.data[x2][y2] = value
        for i in range(round(length(line))):
            (dx,dy) = xy(x1,y1,angle,i)
            self.data[round(dx)][round(dy)] = value

    def draw_lines(self,lines,value=None):
        for line in lines:
            self.draw_line(line,value)

def bearing(line):
    angle = math.degrees(math.atan2(line[3]-line[1],line[2]-line[0]))
    if 0 <= angle <= 90:
        return 90 - angle
    elif 90 < angle <= 180:
        return 180 - angle + 270 
    elif 0 > angle >= -90:
        return 90 - angle
    elif -90 > angle > -180:
        return 90 - angle

def length(line):
    """Thank you Pythagoras. You would have loved Python."""
    return math.sqrt((line[2] - line[0]) ** 2 + (line[3] - line[1]) ** 2)

def xy(x=0, y=0, direction=0, amount=0):
    """Returns a new (x,y) coordinate after adding the amount in
    the given direction."""
    angle = math.radians(direction)
    return (math.sin(angle) * amount + x, math.cos(angle) * amount + y)

class XYZGrid(UserList):
    """Adds 3rd dimension mostly for layering on XYGrids"""
    pass

class XYBitGrid(UserList):
    """Ultra fast XY grid as packed struct composed of boolean on/offs"""
    pass
