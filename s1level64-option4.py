import codestudio
import mymod
artist = codestudio.load('s1level64')

for counter in range(50,90,10):
    mymod.draw_square(artist,counter)

artist.check()
