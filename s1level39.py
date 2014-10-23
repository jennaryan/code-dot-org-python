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
import codestudio
import mymod

artist = codestudio.Artist()

for count2 in range(36):
    artist.pen_color(mymod.random_color())
    for count in range(3):
        artist.move_forward(100)
        artist.move_right(120)
    artist.move_right(10)

codestudio.exitonclick()
