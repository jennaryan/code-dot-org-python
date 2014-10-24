import yaml
from os import path
here = path.abspath(path.dirname(__file__))
files_path = path.join(here,'challenges')

class MissingLine(Exception):
    '''
    A special exception class to allow hints to be associated with
    particular different check failures.
    '''
    def __init__(self,line,hint=None):
        super().__init__()
        self.line = line
        self.hint = hint

class Challenge():

    def __str__(self): return str(self.__dict__)

    def __init__(self,name=None,fname=None):
        self.lines = []
        self.raise_exception = False
        if name: self.load(name,fname)

    def load(self,name,fname=None):
        if not fname:
            fname = path.join(files_path,name+'.yaml')
        with open(fname) as f:
            y = yaml.load(f)
            self.ref = y['ref']
            for line in y['lines']:
                self.lines.append(tuple([int(s) for s in line.split()]))

    def check(self,solution):
        for line in self.lines:
            backward = (line[2],line[3],line[0],line[1])
            if line not in solution and backward not in solution:
                if self.raise_exception: 
                    raise MissingLine(line)
                else:
                    return False, line
        return True

if __name__ == '__main__':

    # TODO turn this into proper unittests later

    #Challenge('s1level24').dump()
    #Challenge('s1level24',fname='./challenges/s1level24.yaml').dump()

    c = Challenge('s1level24')
    c.raise_exception = False

    one = [(0,0,100,100)]
    print(c.check(one))

    two = [(0,0,100,0), (100,0,100,100)]
    print(c.check(two))
