"""Stage 19: Puzzle 4 of 6

Try running this program, and make changes to see what happens. Can you
figure out how it works? (Or delete it and replace it with something
totally different)

"""

import sys
sys.path.append('..')
import codestudio
zombie = codestudio.load('s1level106')

def draw_circle(step):
    saved_speed = zombie.speed
    zombie.speed = 'fastest'
    for count in range(60):
        zombie.move_forward(step)
        zombie.turn_right(6)
    zombie.speed = saved_speed

for count in range(10):
    zombie.color = zombie.random_color()
    draw_circle(6)
    zombie.turn_right(36)

zombie.wait()
