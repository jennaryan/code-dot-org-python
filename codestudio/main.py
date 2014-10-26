import json
from . artist import Artist 
from . maze import Maze
from . farmer import Farmer
from os import path
here = path.abspath(path.dirname(__file__))
files_path = path.join(here,'challenges')

def load(name):
    '''Loads an artist challenge config (json) file'''
    fname = path.join(files_path,name+'.json')
    actor = None
    with open(fname, 'r') as f:
        config = json.load(f)
        t = config['type']
        if (t == 'artist'):
            actor = Artist(config)
        elif (t == 'maze'):
            actor = Maze(config)
        elif (t == 'farmer'):
            actor = Farmer(config)
        else:
            raise Exception('Invalid or missing challenge type')
    actor.setup()
    return actor
