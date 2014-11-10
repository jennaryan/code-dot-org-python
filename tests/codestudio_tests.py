import sys
sys.path.append('..')
import codestudio.artist as a
from nose.tools import assert_equals

def angle_test():
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
    assert_equals(round(a.angle((0,0,0,2))), 0)
