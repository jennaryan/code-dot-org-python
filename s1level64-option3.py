import codestudio
artist = codestudio.load('s1level64')

# better, suitable for putting into a function library like `mymod`

def draw_square(artist,size):
    for count in range(4):
        artist.move_forward(size)
        artist.turn_right(90)

for counter in range(50,90,10):
    draw_square(artist,counter)

artist.check()
