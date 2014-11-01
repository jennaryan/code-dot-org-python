This contains some extra challenges, some easy and some very hard,
created by others. Want to make your own challenges, even submit them so
others can try? Follow these steps, then send an email or pull request
to [skilstak](http://github.com/skilstak/) to include them.

1. Instead of `load(name)` call `create(name,type,direction)` 
1. Instead of `check()` call `save()`

That's it. Here's an example:

```
import codestudio
artist = codestudio.create('square-loop', 'artist',90)

# draw a square
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
import codestudio
artist = codestudio.load('square-loop')

# draw a square
for count in range(4):
    artist.move_forward(100)
    artist.turn_right(90)

artist.check()
```

Now just remove the code you want coders to figure out and replace with
some comments to give them hints, but they will already get the solution
drawn for them to see. *Make sure your code contains nothing left off,
like loops without a body, because it will stop the solution from even
appearing.* Using `TODO` is a common practice to show this isn't just a
comment that explains some section of the code. Most syntax highlighters
will display it to help know what needs to be changed and where.

```
import codestudio
artist = codestudio.load('square-loop')

# draw a square
for count in range(4):
    # TODO draw one side and turn
    pass

artist.check()
```

Keep in mind that if you want to change your saved challenge later you
will have to remove the `json` file in the `challenges` folder that you
saved for it.

Gotchas for Developers
======================

Don't forget to add the following two lines so that folks can just
solve these extras without moving anything or setting their
`PYTHONPATH`, which they might not have learned how to do yet:

```
import sys
sys.path.append('..')
```

