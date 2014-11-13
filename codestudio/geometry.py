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
        return flip(self)

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
        if type(line) is __class__:  line = line.to_tuple()
        return self.to_tuple() == line

    def same_start(self,line):
        if type(line) is __class__: line = line.to_tuple()
        return self.x == line[0] and self.y == line[1]

    def same_end(self,line):
        if type(line) is __class__: line = line.to_tuple()
        return self.dx == line[2] and self.dy == line[3]

    def start_end(self,line):
        if type(line) is __class__: line = line.to_tuple()
        return self.x == line[2] and self.y == line[3]

    def end_start(self,line):
        if type(line) is __class__: line = line.to_tuple()
        return self.dx == line[0] and self.dy == line[1]

    def continues(self,line):
        if type(line) is tuple: line = Line(line)
        if not self.start_end(line):
            return False
        elif self.length == 0 or line.length == 0:
            return True
        elif self.angle == line.angle:
            return True
        else:
            return False

    def precedes(self,line):
        if type(line) is tuple: line = Line(line)
        if not self.end_start(line):
            return False
        elif self.length == 0 or line.length == 0:
            return True
        elif self.angle == line.angle:
            return True
        else:
            return False

    def opposes(self,line):
        if type(line) is tuple: line = Line(line)
        if not self.same_start(line):
            return False
        elif self.length == 0 or line.length == 0:
            return True
        elif self.angle == line.flipped().angle:
            return True
        else:
            return False

    def faces(self,line):
        if type(line) is tuple: line = Line(line)
        if not self.same_end(line):
            return False
        elif self.length == 0 or line.length == 0:
            return True
        elif self.angle == line.flipped().angle:
            return True
        else:
            return False

def flip(line):
    ltype = type(line)
    if ltype is tuple:
        return (line[2],line[3],line[0],line[1])
    elif ltype is list:
        x = line[0]
        y = line[1]
        line[0] = line[2]
        line[1] = line[3]
        line[2] = x
        line[3] = y
        return line
    elif ltype is Line:
        x = line.dx
        y = line.dy
        line.dx = line.x
        line.dy = line.y
        line.x = x
        line.y = y
    else:
        raise TypeError()
    return line

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

def to_tuples(lines):
    converted = []
    for line in lines:
        ltype = type(line)
        if ltype is Line:
            line = line.to_tuple()
        elif ltype is tuple or ltype is list:
            line = tuple(line[0:4])
        else:
            raise TypeError()
        converted.append(line)
    return converted

def to_lines(lines):
    converted = []
    for line in lines:
        ltype = type(line)
        if ltype is tuple:
            line = Line(line)
        elif ltype is list:
            line = Line(tuple(line))
        elif ltype is Line:
            pass
        else:
            raise TypeError()
        converted.append(line)
    return converted

def unique(lines):
    lines = to_tuples(lines)
    unique = [] 
    for line in lines:
        flipped = flip(line)
        if line not in unique and flipped not in unique:
            unique.append(line)
    return unique

def find_joins(line,lines):
    line = Line(line)
    line_t = line.to_tuple()
    new = {}
    remove = {}
    for other in lines:
        other = Line(other)
        other_t = other.to_tuple()
        if other.same(line):
            continue
        elif other in line:
            remove[other_t] = True
            new[line_t] = True
        elif line in other:
            remove[line_t] = True
            new[other_t] = True
        elif line.precedes(other):
            remove[line_t] = True
            remove[other_t] = True
            n = (line.x,line.y,other.dx,other.dy)
            new[n] = True
        elif line.continues(other):
            remove[line_t] = True
            remove[other_t] = True
            n = (other.x,other.y,line.dx,line.dy)
            new[n] = True
        elif line.opposes(other):
            remove[line_t] = True
            remove[other_t] = True
            n = (line.dx,line.dy,other.dx,other.dy)
            new[n] = True
        elif line.faces(other):
            remove[line_t] = True
            remove[other_t] = True
            n = (line.x,line.y,other.x,other.y)
            new[n] = True
        else:
            pass
    return new, remove

def join_lines(lines):
    lines = unique(lines)
    remove = {}
    new = {} 
    for line in lines:
        _new, _remove = find_joins(line,lines)
        new.update(_new)
        remove.update(_remove)
    joined = [l for l in lines if l not in remove]
    joined.extend(new)
    return joined, new

def simplify(lines):
    while True:
        lines, new = join_lines(lines)
        if not new:
            break
    return lines
