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

    def tuple(self):
        return (self.x,self.y,self.dx,self.dy)

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
            line = self.tuple()
            d['angle'] = angle(line)
            d['length'] = line_length(line)
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
            line = self.tuple()
            x = item.x
            y = item.y
            dx = item.dx
            dy = item.dy
            has_xy = contains(line,(x,y))
            has_dxdy = contains(line,(dx,dy))
            return has_xy and has_dxdy
        elif itype is tuple or itype is list:
            if len(item) == 4:
                has_xy = contains(self.tuple(),(item[0],item[1])) 
                has_dxdy = contains(self.tuple(),(item[2],item[3])) 
                return has_xy and has_dxdy
            elif len(item) == 2:
                return contains(self.tuple(),(item[0],item[1])) 
        else:
            raise TypeError()

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

def line_length(line):
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

def join_segments(lines):
    print('join segments')
    joined = []
    for line in lines:
        print('=' * 60)
        print('*' * 60)
        print('=' * 60)
        print('line',line)
        start = (line[0],line[1])
        end = (line[2],line[3])
        length = line_length(line)
        color = line[4]
        width = line[5]
        direction = angle(line)
        reversed_direction = direction + 180
        is_subseg = False
        #print('start',start)
        #print('end',end)
        #print('length',length)
        #print('color',color)
        #print('widt',width)
        #print('direction',direction)
        #print('reversed_direction',reversed_direction)
        if reversed_direction > 360:
            reversed_direction -= 360
        for other in lines:
            print('=' * 60)
            print('other',other)
            o_start = (other[0],other[1])
            o_end = (other[2],other[3])
            o_length = line_length(line)
            o_direction = angle(other)
            o_color = other[4]
            o_width = other[5]
            o_reversed_direction = o_direction + 180
            #print('o_start',o_start)
            #print('o_end',o_end)
            #print('o_length',o_length)
            #print('o_color',o_color)
            #print('o_width',o_width)
            #print('o_direction',o_direction)
            #print('o_reversed_direction',o_reversed_direction)
            shorter = (length < o_length)
            print('{}: {} is shorter than {}'.format(shorter,line,other))
            same_direction = direction == o_direction
            print('{}: same direction: {} == {}'.format(same_direction,direction,o_direction))
            opposite_direction = reversed_direction == o_direction
            same_start = start == o_start
            print('{}: {} same start as {}'.format(same_start,line,other))
            same_end = end == o_end
            print('{}: {} same end as {}'.format(same_end,line,other))
            start_in = contains(other,start) 
            print('{}: {} starts in {}'.format(start_in,start,other))
            end_in = contains(other,end) 
            print('{}: {} ends in {}'.format(end_in,end,other))
            start_end = start == o_end
            print('{}: {} start is end of {}'.format(start_end,line,other))
            end_start = end == o_start
            print('{}: {} end is start of {}'.format(end_start,line,other))
            attached = same_start or same_end or start_end or end_start
            print('{}: {} is attached to {}'.format(attached,line,other))
            same = same_start and same_end
            print('{}: {} is identical to {}'.format(same,line,other))
            flipped = start_end and end_start
            print('{}: {} is flipped version of to {}'.format(flipped,line,other))
            continuous = same_direction and end_start
            print('{}: {} continues {}'.format(continuous,line,other))
            facing = opposite_direction and same_end
            print('{}: {} faces {}'.format(facing,line,other))
            away = opposite_direction and same_start
            print('{}: {} away {}'.format(away,line,other))
            asubseg = same_direction and same_start and shorter
            print('{}: {} is a subseg with same start as {}'.format(asubseg,line,other))
            asubsegr = opposite_direction and same_end and shorter
            print('{}: {} is a subseg reversed with same end as {}'.format(asubsegr,line,other))
            subseg = start_in and end_in
            print('{}: {} is contained within {}'.format(subseg,line,other))
            if same or flipped:
                if line not in joined:
                    print('{} not in joined. Adding.'.format(line))
                    joined.append(line)
                    continue
                else:
                    print('duplicate')
            elif asubseg or asubsegr or subseg:
                print('{} is a subseg of {}'.format(line,other))
                print('Ignoring')
                continue
            elif continuous:
                print('continuous')
                new_line = [
                    start[0],start[1],
                    o_end[0],o_end[1],
                    color, width
                ]
                joined.append(new_line)
            elif facing:
                print('facing')
                new_line = [
                    end[0],end[1],
                    o_end[0],o_end[1],
                    color, width
                ]
                joined.append(new_line)
            elif away:
                print('away')
                new_line = [
                    start[0],start[1],
                    o_start[0],o_start[1],
                    color, width
                ]
                joined.append(new_line)
            else:
                print('{} is not attached to {}'.format(line,other))
    return joined
