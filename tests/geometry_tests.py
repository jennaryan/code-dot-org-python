import sys
sys.path.append('..')
import codestudio.geometry as g
from nose.tools import assert_equals

def Line_test():
    l = g.Line((1,1,1,1))
    l.color = 'blue'
    assert_equals( l.x, 1 )
    assert l.y == 1
    assert l.dx == 1
    assert l.dy == 1
    assert l.to_tuple() == (1,1,1,1)
    l.x = 0
    l.y = 0
    assert l.to_tuple() == (0,0,1,1)
    assert l.angle == 45
    l.dx = 3
    l.dy = 3
    assert l.to_tuple() == (0,0,3,3)
    assert l.angle == 45
    f = l.flipped()
    assert f.to_tuple() == (3,3,0,0)
    assert f.angle == 225
    f.length += 1
    '''
    f += 1
    assert l < f
    assert l <= l
    assert l == l
    assert l != f
    assert f > l
    assert f >= f
    '''
    assert l in f
    assert l.to_tuple() in f
    assert f not in l
    assert f.to_tuple() not in l
    one = g.Line()
    two = g.Line()
    assert one.same(two)
    two.x = 1
    assert not one.same(two)
    two.y = 1
    one.dx = 1
    one.dy = 1
    assert one.attached(two)
    assert one.start_end(two)
    assert two.end_start(one)
    one.flip()
    assert two.same(one)
    ne = g.Line((0,0,1,1))
    sw = g.Line((0,0,-1,-1))
    assert ne.opposes(sw)
    zero = g.Line((0,0,0,0))
    assert ne.continues(zero)
    assert zero.continues(zero)
    assert zero.precedes(ne)
    ne.flip()
    sw.flip()
    assert ne.faces(sw)

def flip_test():
    line = g.Line((0,0,1,1))
    g.flip(line)
    assert_equals(str(line),"[1, 1, 0, 0, 'black', 7]")

def unique_lines_test():
    lines = [
        [0,0,1,1,'blue',7],
        [0,0,2,2,'red',7],
        [0,0,2,2,'green',7],
        [0,0,1,1,'purple',7],
        [1,1,0,0,'orange',7],
        [0,0,1,1,'yellow',7],
        [-2,-2,1,1,'pink',7],
        [0,0,-3,-3,'chartreuse',7],
        [-4,-4,0,0,'goldenrod',7]
    ]
    unique = [
        (0,0,1,1),
        (0,0,2,2),
        (-2,-2,1,1),
        (0,0,-3,-3),
        (-4,-4,0,0)
    ] 
    assert_equals(g.unique(lines),unique)

def find_joins_test():
    lines = [
        [0,0,0,0,'black',7],
        [0,0,1,1,'blue',7],
        [0,0,2,2,'red',7],
        [0,0,2,2,'green',7],
        [0,0,1,1,'purple',7],
        [1,1,0,0,'orange',7],
        [0,0,1,1,'yellow',7],
        [-2,-2,1,1,'pink',7],
        [0,0,-3,-3,'chartreuse',7],
        [-4,-4,0,0,'goldenrod',7]
    ]
    new = {
        (-1,-1,0,0): True,
        (-1,-1,1,1): True,
        (-1,-1,2,2): True,
        (-4,-4,0,0): True,
        (-2,-2,1,1): True,
        (0,0,-3,-3): True
    }
    remove = {
        (0,0,0,0): True,
        (0,0,1,1): True,
        (0,0,2,2): True,
        (1,1,0,0): True,
        (-1,-1,0,0): True
    } 
    _new, _remove = g.find_joins((-1,-1,0,0),lines)
    assert_equals(_new,new)
    assert_equals(_remove,remove)

def join_lines_test():
    lines = [
        [0,0,0,0,'black',7],
        [0,0,1,1,'blue',7],
        [0,0,2,2,'red',7],
        [0,0,2,2,'green',7],
        [0,0,1,1,'purple',7],
        [1,1,0,0,'orange',7],
        [0,0,1,1,'yellow',7],
        [-2,-2,1,1,'pink',7],
        [0,0,-3,-3,'chartreuse',7],
        [-4,-4,0,0,'goldenrod',7]
    ]
    joined = [
        (-2, -2, 1, 1), (-2, -2, 1, 1), (1, 1, -3, -3),
            (-3, -3, 1, 1), (-4, -4, 0, 0), (-4, -4, 1, 1), (-4, -4, 2, 2), (2, 2, -3, -3), (0, 0, 1, 1), (-3, -3, 2, 2), (0, 0, 2, 2), (0, 0, -3, -3)]
    _joined, _new = g.join_lines(lines)
    #print('_JOINED:',_joined)
    #print('JOINED:',joined)
    print('NEW:',_new.keys())
    assert_equals(_joined,joined)

def simplify_test():
    lines = [
        [0,0,0,0,'black',7],
        [0,0,1,1,'blue',7],
        [0,0,2,2,'red',7],
        [0,0,2,2,'green',7],
        [0,0,1,1,'purple',7],
        [1,1,0,0,'orange',7],
        [0,0,1,1,'yellow',7],
        [-2,-2,1,1,'pink',7],
        [0,0,-3,-3,'chartreuse',7],
        [-4,-4,0,0,'goldenrod',7]
    ]
    simplified = [(-4,-4,2,2)]
    assert_equals(g.simplify(lines),simplified)

def length_test():
    assert g.length((0,0,2,2)) == 2.8284271247461903

def xy_plus_vec_test():
    returned = [round(n) for n in g.xy_plus_vec(0,0,45,2.8284271247461903)]
    assert returned == [2,2]

def angle_test():
    assert round(g.angle((0,0,0,2))) == 0
    assert round(g.angle((0,0,1,2))) ==  27
    assert g.angle((0,0,2,2)) ==  45
    assert round(g.angle((0,0,2,1))) == 63
    assert g.angle((0,0,2,0)) == 90
    assert round(g.angle((0,0,2,-1))) == 117
    assert g.angle((0,0,2,-2)) == 135
    assert round(g.angle((0,0,1,-2))) == 153
    assert g.angle((0,0,0,-2)) == 180
    assert round(g.angle((0,0,-1,-2))) == 207
    assert g.angle((0,0,-2,-2)) == 225
    assert round(g.angle((0,0,-2,-1))) == 243
    assert round(g.angle((0,0,-2,0))) == 270
    assert round(g.angle((0,0,-2,1))) == 297
    assert round(g.angle((0,0,-2,2))) == 315
    assert round(g.angle((0,0,-1,2))) == 333

def contains_test():
    assert g.contains((0,0,4,4),(2,2))
    assert g.contains((1,1,4,4),(2,2))
    assert g.contains((2,2,2,2),(2,2))
    assert not g.contains((0,0,5,10),(2,2))
    assert not g.contains((3,3,4,4),(2,2))
    assert g.contains((-2,-2,4,4),(2,2))
    assert g.contains((3,3,-1,-1),(3,3))
    assert not g.contains((3,3,-1,-1),(4,3))
    assert g.contains((3,3,-1,-1),(0,0))
    assert not g.contains((3,3,4,4),(10,100))
    assert g.contains((3, 3, -0.707106781186547, -0.7071067811865479),(0,0))

'''
def join_segments_continuous_test():
    test = [
        [0,0,3,3,'black',7],
        [0,0,2,2,'black',7],
        [1,1,2,2,'black',7],
        [2,2,4,4,'black',7]
    ]
    correct = [
        [0,0,4,4,'black',7],
        [1,1,4,4,'black',7]
    ]
    joined = g.join_segments(test)
    assert_equals(joined,correct)

def join_segments_asubsegr_test():
    test = [
        [0,0,4,4,'black',7],
        [1,1,4,4,'black',7]
    ]
    correct = [
        [0,0,4,4,'black',7]
    ]
    joined = g.join_segments(test)
    assert_equals(joined,correct)
'''
