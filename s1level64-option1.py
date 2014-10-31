import codestudio
artist = codestudio.load('s1level64')

for counter in range(50,90,10):
    for count in range(4):
        artist.move_forward(counter)
        artist.turn_right(90)

artist.check()
