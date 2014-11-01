import codestudio
import mymod
artist = codestudio.load('s1level64')

# TODO finish the mymod.draw_square(artist,counter) function in mymod

# TODO change these values
smallest = 2 
biggest = 2
increment = 1

for counter in range(smallest,biggest,increment):
    mymod.draw_square(artist,counter)

artist.check()
