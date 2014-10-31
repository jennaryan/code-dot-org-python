import codestudio
artist = codestudio.load('s1level64')

# good, but uses a global artist, which is not best

def draw_square(size):
    for count in range(4):
        artist.move_forward(size)
        artist.turn_right(90)

for counter in range(50,90,10):
    draw_square(counter)

artist.check()
