'''
Add your functions to this library module to use them again
in other challenges.
'''

import codestudio

def hello_world():
    print("Hello from 'mymod'")

def draw_square(artist,size):
    for count in range(4):
        artist.move_forward(size)
        artist.turn_right(90)

