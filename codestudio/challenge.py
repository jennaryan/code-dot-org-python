import json
import artist

class Challenge():
    '''
    c = ArtistChallenge('s1level24')
    c = ArtistChallenge(fname='s1level24')
    c = ArtistChallenge('sllevel24','./challenges/s1level24.yaml')
    c = ArtistChallenge(name='s1level24')
    c = ArtistChallenge(fname='./challenges/s1level24.yaml')
    c = ArtistChallenge(fname='./challenges/s1level24.yaml',name='s1level24')
    '''

    def __init__(self,name=None,fname=None):
        if not fname and name: fname = path.join(files_path,name+'.json')
        if not name and fname: name = path.splitext(path.basename(fname))[0]
        self.name = name
        self.fname = fname
        self.lines = []
        if fname: self.load(fname)

    def load(self,fname=None):
        '''Loads an artist challenge config (json) file'''
        if fname: self.fname = fname
        with open(self.fname, 'r') as f:
            data = json.load(f)
            if (data['type'].lower() == 'artist'):
                for line in data['lines']:
                    self.lines.append(tuple(line))
                self.number_lines = len(self.lines)


if __name__ == '__main__':

    # TODO turn this into proper unittests later

    c = ArtistChallenge('s1level24')
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

