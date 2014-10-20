''' s1level64
var counter;

for (counter = 50; counter <= 90; counter += 10) {
   // draw_a_square
   for (var count = 0; count < 4; count++) {
        moveForward((counter));
        turnRight(90);
   }
}
'''


import codestudio
import mymod

artist = mymod.Artist()

for counter in range(50,90,10):
    artist.draw_square(counter)

codestudio.exitonclick()
