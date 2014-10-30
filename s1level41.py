import codestudio
artist = codestudio.create('s1level41','artist')

artist.speed = 'fastest'

for count in range(10):
    artist.pen.color = 'random'
    for count in range(4):
        artist.move_forward(20)
        artist.turn_right(90)
    artist.move_forward(20)

artist.save_as_solution()

