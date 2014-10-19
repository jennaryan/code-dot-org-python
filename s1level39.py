''' s1level39
for (var count2 = 0; count2 < 36; count2++) {
  penColor(colour_random());
  for (var count = 0; count < 3; count++) {
    moveForward(100);
    turnRight(120);
  }
  turnRight(10);
}
'''
import turtle
import mymod

bob = turtle.Turtle()

for count2 in range(36):
    bob.pencolor(mymod.random_color())
    for count in range(3):
        bob.forward(100)
        bob.right(120)
    bob.right(10)

input()
