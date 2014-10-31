import codestudio
artist = codestudio.load('s1level41')
#artist = codestudio.create('s1level41','artist')

for count in range(10):
    artist.pen.color = 'random'
    for count in range(4):
        artist.move_forward(20)
        artist.turn_right(90)
    artist.move_forward(20)

#artist.check()
#artist.save_as_solution()
