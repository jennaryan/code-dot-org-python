Make your own challenges!
=========================

Here are some extra challenges created by students young and old. Some are
very easy, some very hard. See if you can do them. Then, create your own
challenges to submit and we'll include them as well. Here's how ...

1. Copy the `sample.py` or another than you like.
2. Change `load(whatever)` to `create(your_challenge_name,type,start_direction)` 
3. Change `check()` to `wait()` until you perfect your challenge
4. Change `wait()` to `save()` when you are ready to save it. Then run again.
5. Change the `create()` to `load(your_challenge_name)`
6. Change the `save()` to `check()`
7. Test run it again with your solution
8. Remove or change the lines of code you want players to fix or add
9. Run one last time to test what your players will see
10. Commit your changes to github and let us know about them to include

That's it. Here's an example:

```
import sys
sys.path.append('..')

import codestudio
artist = codestudio.create('square-loop','artist',90)

# TODO draw a square in 3 lines of code
for count in range(4):
    artist.move_forward(100)
    artist.turn_right(90)

artist.save()
```

This will automatically save it into the `challenges` directory for you
and make sure there isn't one already saved there with your unique name.

All you need to do after that is test your challenge by changing
`create()` and `save()` to `load()` and `check()`:

```
import sys
sys.path.append('..')

import codestudio
artist = codestudio.load('square-loop')

# TODO draw a square in 3 lines of code
for count in range(4):
    artist.move_forward(100)
    artist.turn_right(90)

artist.check()
```

Now just remove the code you want coders to figure out and replace with
some comments to give them hints, but they will already get the solution
drawn for them to see. *Make sure your code contains nothing left off,
like loops without a body, because it will stop the solution from even
appearing. Use `pass` if you need to for empty loops and such.* Using
`TODO` is a common practice to show this isn't just a comment that
explains some section of the code. Most syntax highlighters will display
it to help know what needs to be changed and where.

```
import sys
sys.path.append('..')

import codestudio
artist = codestudio.load('square-loop')

# TODO draw a square in 3 lines of code
for count in range(4):
    pass # replace

artist.check()
```

Keep in mind that if you want to change your saved challenge later you
will have to remove the `json` file in the `challenges` folder that you
saved for it. `save()` will never overwrite an existing saved solution
to keep you from breaking others that are already working.

Gotchas for Developers
======================

# Don't forget `sys.path.append('..')`

Don't forget to add the following two lines so that folks can just
solve these extras without moving anything or setting their
`PYTHONPATH`, which they might not have learned how to do yet:

```
import sys
sys.path.append('..')
```

This also allows others to create their own collection of code puzzle
challenges just by creating a directory structure or github repo like this:

```
./challenges/sample.py
./sample.py
./README.md
```

# You don't need `__author__` and `__credits__`

People can see who contributed what by looking where they should, at
the source files on GitHub. Adding these tags just makes more work
to maintain them. Add a README.md file instead.

# Make sure challenge fits on 400 pixel square canvas

This is small, sure, but it allows your challenges to match those from
code.org and fit next to a coding window open on the right. It also allows
for future `codestudio` Python development to add other widgets to the
main window.
