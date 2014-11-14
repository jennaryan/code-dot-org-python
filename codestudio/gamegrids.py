from collections import UserList

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
        for n in range(xsize):
            self.data[n][0] = ''
        for n in range(ysize):
            self.data[0][n] = ''

    def __str__(self):
        d = self.data
        string = ''
        for y in range(self.ysize):
            for x in range(self.xsize):
                string += d[x+1][y+1] + ' '
            string += "\n"
        return string
