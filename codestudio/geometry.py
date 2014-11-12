"""Basic Azimuth (N,S,E,W) geometry in pure python (mostly as an example).

Students can get a good idea of what factoring away their favorite
game geometry functions look like as a Python module.

This module *does not use Cartesian coordinates*. Instead we use Y as up
or North and calculate degrees clockwise from N. This is how direction and
degrees are presented in code.org and how many game systems use them. It
can be a little daunting for a beginner to make the translations from
`math` functions, using Cartesian, and what they want to work in their
games and puzzles.

Note: If you want high performance geometric analysis you probably want
Shaply and GEOS and not this. 
"""

import math

class Line():

    def __init__(self,line=(0,0,0,0),color='black',width=7,angle=0,length=0):
        d = self.__dict__
        d['angle'] = angle 
        d['length'] = length
        d['x'] = line[0]
        d['y'] = line[1]
        d['dx'] = line[2]
        d['dy'] = line[3]
        d['color'] = color
        d['width'] = width
        self.x = line[0]     # triggers setattr

    def to_tuple(self):
        return (self.x,self.y,self.dx,self.dy)

    def flip(self):
        x = self.dx
        y = self.dy
        self.dx = self.x
        self.dy = self.y
        self.x = x
        self.y = y

    def flipped(self):
        f = __class__()
        x = self.dx
        y = self.dy
        f.dx = self.x
        f.dy = self.y
        f.x = x
        f.y = y
        return f

    def __str__(self):
        return str([self.x,self.y,self.dx,self.dy,self.color,self.width])

    def __lt__(self,other):
        return self.length < other.length
        
    def __le__(self,other):
        return self.length <= other.length

    def __eq__(self,other):
        return self.length == other.length

    def __ne__(self,other):
        return self.length != other.length

    def __gt__(self,other):
        return self.length > other.length

    def __ge__(self,other):
        return self.length >= other.length

    def __iadd__(self,other):
        otype = type(other)
        if otype is int or otype is float:
            self.length += other
        else:
            raise TypeError()
        return self

    def __setattr__(self,name,value):
        d = self.__dict__
        if name in ('x','y','dx','dy'):
            d[name] = value
            line = (d['x'],d['y'],d['dx'],d['dy'])
            d['angle'] = angle(line)
            d['length'] = length(line)
        elif name == 'length':
            d['length'] = value 
            (d['dx'],d['dy']) = xy_plus_vec(d['x'],d['y'],d['angle'],value)
        elif name == 'angle':
            d['angle'] = value
            (d['dx'],d['dy']) = xy_plus_vec(d['x'],d['y'],value,d['length'])
        else:
            super().__setattr__(name,value)

    def __contains__(self, item):
        itype = type(item)
        if itype is Line:
            line = self.to_tuple()
            has_xy = contains(line,(item.x,item.y))
            has_dxdy = contains(line,(item.dx,item.dy))
            return has_xy and has_dxdy
        elif itype is tuple or itype is list:
            if len(item) == 4:
                has_xy = contains(self.to_tuple(),(item[0],item[1])) 
                has_dxdy = contains(self.to_tuple(),(item[2],item[3])) 
                return has_xy and has_dxdy
            elif len(item) == 2:
                return contains(self.to_tuple(),(item[0],item[1])) 
        else:
            raise TypeError()
    
    def attached(self,line):
        if type(line) is __class__: l = line.to_tuple()
        same_start = self.x == l[0] and self.y == l[1]
        same_end = self.dx == l[2] and self.dy == l[3]
        start_end = self.x == l[2] and self.y == l[3]
        end_start = self.dx == l[0] and self.dy == l[1]
        return same_start or same_end or start_end or end_start

    def same(self,line):
        if type(line) is __class__: l = line.to_tuple()
        return self.to_tuple() == l

    def same_start(self,line):
        if type(line) is __class__: l = line.to_tuple()
        return self.x == l[0] and self.y == l[1]

    def same_end(self,line):
        if type(line) is __class__: l = line.to_tuple()
        return self.dx == l[2] and self.dy == l[3]

    def start_end(self,line):
        if type(line) is __class__: l = line.to_tuple()
        return self.x == l[2] and self.y == l[3]

    def end_start(self,line):
        if type(line) is __class__: l = line.to_tuple()
        return self.dx == l[0] and self.dy == l[1]

    def continues(self,line):
        if type(line) is __class__: l = line.to_tuple()
        return self.angle == angle(l) and self.start_end(l) 

    def precedes(self,line):
        if type(line) is __class__: l = line.to_tuple()
        return self.angle == angle(l) and self.end_start(l) 

    def opposing(self,line):
        if type(line) is tuple: line = Line(line)
        if not self.same_start(line): return False
        if not self.angle == line.flipped().angle: return False
        return True

    def facing(self,line):
        if type(line) is tuple: line = Line(line)
        if not self.same_end(line): return False
        if not self.angle == line.flipped().angle: return False
        return True
 
def angle(line):
    dx = line[2] - line[0]
    dy = line[3] - line[1]
    angle = math.degrees(math.atan2(dy,dx))
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
    dx = line[2] - line[0]
    dy = line[3] - line[1]
    return math.sqrt(dx**2 + dy**2) 

def contains(line, point):
    px, py = point[0], point[1]
    x, y = line[0], line[1]
    dx, dy = line[2], line[3]
    factor = (dx-x) * (px-x) - (dy-y) * (py-y)
    if abs(factor) < 0.0001:
        if dx >= x:
            x_in = x <= px <= dx
        else:
            x_in = x >= px >= dx
        if dy >= y:
            y_in = y <= py <= dy
        else:
            y_in = y >= py >= dy
        return x_in and y_in
    return False

def xy_plus_vec(x=0, y=0, direction=0, amount=0):
    '''Returns a new (x,y) coordinate after adding the amount in
    the given direction
    '''
    newx = math.sin(math.radians(direction)) * amount + x
    newy = math.cos(math.radians(direction)) * amount + y
    return (newx,newy)

def unique(lines):
    tuples =  [tuple(l[0:4]) for l in lines]
    unique = []
    for t in tuples:
        flipped = (t[2],t[3],t[0],t[1])
        if t not in unique and flipped not in unique:
            unique.append(t)
    return unique

