import mymod
artist = mymod.load('s1level64')

for counter in range(50,90,10):
    artist.draw_square(counter)

artist.check()
