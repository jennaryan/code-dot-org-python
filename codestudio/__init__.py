'''
Always want a simple, single `import codestudio`
(otherwise, yes, `import *` is usually unwise)
'''

from . game import *
from . artist import *
from . maze import *
from . farmer import *
from . challenge import *

def load(challenge):
    return Challenge(challenge)
