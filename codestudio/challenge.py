import yaml
from os import path
here = path.abspath(path.dirname(__file__))
files_path = path.join(here,'challenges')

class YamlConfig():

    def __str__(self): return str(self.__dict__)

    def __init__(self,name=None,fname=None):
        if name: self.load(name,fname)

    def load(self,name,fname=None):
        self.name = name
        if not fname:
            fname = path.join(files_path,name+'.yaml')
        with open(fname) as f:
            self.config = yaml.load(f)

class ArtistChallenge():

        def __init__(self,config=False,name=None):
            self.lines = []
            if not config and (name or fname):
                self.config = YamlConfig(

            for line in y['lines']:
                self.lines.append(tuple([int(s) for s in line.split()]))
            self.number_lines = len(self.lines)

    def check(self,solution):
        if len(set(solution)) != self.number_lines: return False
        for line in self.lines:
            backward = (line[2],line[3],line[0],line[1])
            if line not in solution and backward not in solution:
                return False, line
        return True

if __name__ == '__main__':

    # TODO turn this into proper unittests later

    #Challenge('s1level24').dump()
    #Challenge('s1level24',fname='./challenges/s1level24.yaml').dump()

    c = Challenge('s1level24')
    c.raise_exception = False

    # should fail
    solution = [(0,0,100,100)]
    print(c.check(solution))

    # should pass
    solution = [(0,0,100,0), (100,0,100,100)]
    print(c.check(solution))

    # should fail
    solution = [(0,0,100,0), (100,100,100,100)]
    print(c.check(solution))

    # should pass
    solution = [(0,0,100,0), (100,0,100,100), (0,0,100,0)]
    print(c.check(solution))

    # should fail
    solution = [(0,0,100,0), (100,0,100,100), (0,0,0,100)]
    print(c.check(solution))

    # should pass
    solution = [(0,0,100,0), (100,0,100,100), (0,0,0,100)]
    c.strict = False
    print(c.check(solution))

