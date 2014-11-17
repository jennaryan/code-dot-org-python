"""Stage 19: Puzzle 5 of 6

Try running this program, and make changes to see what happens. Can you
figure out how it works? (Or delete it and replace it with something
totally different)

"""

import sys
sys.path.append('..')
import codestudio
zombie = codestudio.load('s1level107')

def draw_circle(step):
    saved_speed = zombie.speed
    zombie.speed = 'fastest'
    for count in range(60):
        zombie.move_forward(step)
        zombie.turn_right(6)
    zombie.speed = saved_speed

for counter in range(4,9,4):
    for count in range(10):
        zombie.color = zombie.random_color()
        draw_circle(counter)
        zombie.turn_right(36)

zombie.wait()
