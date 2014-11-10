import sys
sys.path.append('..')
import codestudio.artist as a
from nose.tools import assert_equals
from nose.tools import assert_raises

def line_length_test():
    assert_equals(a.line_length((0,0,2,2)), 2.8284271247461903)

def xy_plus_vec_test():
    returned = [round(n) for n in a.xy_plus_vec(0,0,45,2.8284271247461903)]
    assert_equals(returned, [2,2])

def angle_test():
    assert_equals(round(a.angle((0,0,0,2))), 0)
    assert_equals(round(a.angle((0,0,1,2))), 27)
    assert_equals(a.angle((0,0,2,2)), 45)
    assert_equals(round(a.angle((0,0,2,1))), 63)
    assert_equals(a.angle((0,0,2,0)), 90)
    assert_equals(round(a.angle((0,0,2,-1))), 117)
    assert_equals(a.angle((0,0,2,-2)), 135)
    assert_equals(round(a.angle((0,0,1,-2))), 153)
    assert_equals(a.angle((0,0,0,-2)), 180)
    assert_equals(round(a.angle((0,0,-1,-2))), 207)
    assert_equals(a.angle((0,0,-2,-2)), 225)
    assert_equals(round(a.angle((0,0,-2,-1))), 243)
    assert_equals(round(a.angle((0,0,-2,0))), 270)
    assert_equals(round(a.angle((0,0,-2,1))), 297)
    assert_equals(round(a.angle((0,0,-2,2))), 315)
    assert_equals(round(a.angle((0,0,-1,2))), 333)

def line_contains_test():
    assert a.line_contains((0,0,4,4),(2,2))
    assert a.line_contains((1,1,4,4),(2,2))
    assert a.line_contains((2,2,2,2),(2,2))
    assert not a.line_contains((0,0,5,10),(2,2))
    assert not a.line_contains((3,3,4,4),(2,2))
    assert not a.line_contains((3,3,4,4),(10,100))

'''
def join_segments_continuous_test():
    test = [
        [0,0,3,3,'black',7],
        [0,0,2,2,'black',7],
        [1,1,2,2,'black',7],
        [2,2,4,4,'black',7]
    ]
    correct = [
        [0,0,4,4,'black',7]
    ]
    joined = a.join_segments(test)
    assert_equals(joined,correct)
'''
