"""Stage 19: Puzzle 1 of 6

Try running this program, and make changes to see what happens. Can you
figure out how it works? (Or delete it and replace it with something
totally different)

"""
import sys
sys.path.append('..')
import codestudio
zombie = codestudio.load('s1level103')

for counter in range(1,201,1):
    zombie.color = zombie.random_color()
    zombie.move_forward(counter)
    zombie.turn_right(90)

zombie.wait()
