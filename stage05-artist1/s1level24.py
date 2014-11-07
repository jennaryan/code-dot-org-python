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

import sys
sys.path.append('..')
import codestudio
artist = codestudio.load('s1level24')

artist.move_forward(100)
# TODO replace this line with code to make the artist turn right
# TODO replace this line with code make the artist move forward

artist.check()

