import json
from . artist import ArtistChallenge
from . maze import MazeChallenge
from . farmer import FarmerChallenge
from os import path
here = path.abspath(path.dirname(__file__))
files_path = path.join(here,'challenges')

def load(uid):
    '''Loads an artist challenge config (json) file'''
    fname = path.join(files_path,uid+'.json')
    actor = None
    with open(fname, 'r') as f:
        config = json.load(f)
        if not config['uid']: config['uid'] = uid
        t = config['type']
        if (t == 'artist'):
            challenge = ArtistChallenge(config)
        elif (t == 'maze'):
            challenge = MazeChallenge(config)
        elif (t == 'farmer'):
            challenge = FarmerChallege(config)
        else:
            raise Exception('Invalid or missing challenge type')
    challenge.setup()
    return challenge
