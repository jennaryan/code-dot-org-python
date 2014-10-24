import yaml
from os import path
here = path.abspath(path.dirname(__file__))
files_path = path.join(here,'challenges')

class Challenge():

    def __str__(self): return str(self.__dict__)

    def __init__(self,name=None,fname=None):
        self.lines = []
        if name: self.load(name,fname)

    def load(self,name,fname=None):
        if not fname:
            fname = path.join(files_path,name+'.yaml')
        with open(fname) as f:
            y = yaml.load(f)
            self.ref = y['ref']
            for line in y['lines']:
                self.lines.append(tuple(line.split()))


# TODO turn this into proper unittests later
if __name__ == '__main__':
    print(Challenge('s1level24'))
    #Challenge('s1level24').dump()
    #Challenge('s1level24',fname='./challenges/s1level24.yaml').dump()
        
