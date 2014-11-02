"""Stage 5: Puzzle 1 of 10

Hi meet the artist. You can write code to make the artist draw almost anything.
Run this code to see the goal. Then add a few lines of code to make the
artist draw over the grey lines of the goal.

Since this is your first artist challenge, we have added a lot of comments
to help. Come back to this one later if you forget. But first let's explain
what code comments are and why to use them.

This type of comment (with three quotes) is called a long-comment or
docstring. Comments like there are included in the documentation
of your Python code (inside the __doc__ special variable). The first
line of a docstring that comes at the top of a script, module, class or
function is the summary. It should be followed by a blank line and then
more description (like we did here). For consistency, always use triple
double quotes. There is more to the whole docstring thing, but that's
enough for now.

You can also use the hash or pound sign to include comments to explain the
code further. These are never included in the documenation of your code and
are to explain something in the code itself.

Hash comments with TODO in them are a convention used by coders to mark
places in the code that need finishing or fixing. Most code editors will
highlight TODO brightly to draw attention to them.

"""

# These two lines tell Python to look in the parent directory that contains
# the folder this file is in. This just means you can run all the challenges
# without having to install the codestudio module and just use it where it is.
# (In programmer terms, this adds to PYTHONPATH where Python searches for mods.)
import sys
sys.path.append('..')

# Here is your main import statment. They always come immediately after any
# docstring comments for your script or module. Every puzzle challenge
# depends on `import codestudio` to work.
import codestudio

# Here is how you load a puzzle challenge and create an artist
artist = codestudio.load('s1level24')

# You can set the artist's pen color with the following (default black)
#artist.pen.color = 'red'
#artist.pen.color = 'random'

# You can change the artist pen size (width) as well (default 7)
#artist.pen.width = 20

# You can change the artist's speed with any of the following (default normal)
#artist.speed = 'slowest'
artist.speed = 'slower'
#artist.speed = 'slow'
#artist.speed = 'normal'
#artist.speed = 'fast'
#artist.speed = 'faster'
#artist.speed = 'fastest'

# Use a few commands to make the artist draw over the grey lines. 

artist.move_forward(100)

# TODO make the artist turn right
#artist.turn_right(90)

# TODO make the artist move forward

# This is how you check your code. It always comes at the end.
artist.check()

