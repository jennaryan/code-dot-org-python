import sys
sys.path.append('..')
import codestudio.gamegrids as g
from nose.tools import assert_equals

def Grid_test():
    grid = g.XYGrid()
    assert_equals(grid,[[]])
    grid.init(3,2,'~')
    assert_equals(str(grid),"~ ~ ~ \n~ ~ ~ \n")
    grid[1][1] = '*'
    assert_equals(str(grid),"* ~ ~ \n~ ~ ~ \n")
    assert False

