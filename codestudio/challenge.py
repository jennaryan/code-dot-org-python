import yaml
from os import path
here = path.abspath(path.dirname(__file__))
files_path = path.join(here,'challenges')

class Challenge():

    def __init__(self,name=None,fname=None):
        if name: self.load(name,fname)

    def load(self,name,fname=None):
        if not fname:
            fname = path.join(files_path,name+'.yaml')
        with open(fname) as f:
            self.config = yaml.load(f)

    def dump(self):
        print(self.config)

if __name__ == '__main__':
    Challenge('s1level24').dump()
    Challenge('s1level24',fname='./challenges/s1level24.yaml').dump()
        
