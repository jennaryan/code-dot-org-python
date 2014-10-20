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

artist = codestudio.Artist()

for counter in range(50,90,10):
    # draw_a_square
    for count in range(4):
        artist.move_forward(counter)
        artist.turn_right(90)

codestudio.exitonclick()
