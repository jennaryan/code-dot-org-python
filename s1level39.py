import codestudio
artist = codestudio.load('s1level39')

for count2 in range(36):
    artist.pen.color = 'random'
    for count in range(3):
        artist.move_forward(100)
        artist.turn_right(120)
    artist.turn_right(10)

artist.check()

