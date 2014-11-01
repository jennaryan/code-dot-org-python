import codestudio
artist = codestudio.load('s1level39')

# TODO correct this code to make a triangle 36 times.
# How many degrees should the turns be? (Hint: after
# 360 degrees of turning the drawing will come full circle.)

for count2 in range(36):
    artist.pen.color = 'random'
    for count1 in range(3):
        artist.move_forward(100)
        artist.turn_right(120)
    artist.turn_right(0) # humm, change this to what?

artist.check()

