"""Stage 19: Puzzle 6 of 6

Try running this program, and make changes to see what happens. Can you
figure out how it works? (Or delete it and replace it with something
totally different)

"""

import sys
sys.path.append('..')
import codestudio
zombie = codestudio.load('s1level108')
zombie.speed = 'faster'

def draw_tree(depth,branches):
    if depth > 0:
        zombie.color = zombie.random_color()
        zombie.move_forward(7*depth)
        zombie.turn_left(130)
        for count in range(branches):
            zombie.turn_right(180/branches)
            draw_tree(depth-1,branches)
        zombie.turn_left(50)
        zombie.jump_backward(7*depth)

draw_tree(9,2)

zombie.wait()
