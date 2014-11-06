"""Stage 11: Puzzle 1 of 11

Hello. Me zombie artist. Me love drawing! Help me draw a square in a
special color. Hint: use the functions provided.

"""

import sys
sys.path.append('..')

import codestudio
zombie = codestudio.load('s1level59')

def draw_square():
    """ Draws a square assuming a zombie exists.

    This is how you define a simple (procedure) function in Python.
    Using functions this way is just gouping code steps together so you
    don't have to type them all the time. 

    By the way, this fancy text inside the triple quotes (") is called
    a 'docstring' and used by Python developers to create explanations of
    their functions for others to read and learn from.
    """
    # TODO complete this function block to draw a square
    zombie.move_forward(100)
    zombie.turn_right(90)

def random_color():
    """Returns a random color as a hex string.
    
    This function doesn't need fixing. It's here to show the difference between
    functions that just do stuff and those that return, or give back, a value.
    Think of it as a machine you put stuff into and you get something back. This
    is the same as functions in math.

    Don't worry about the fancy code inside this function, someday soon it
    will make sense. Remember, it doesn't need fixing, you can just use it.
    """
    import random                 # normally at the top of script file
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return '#{:02x}{:02x}{:02x}'.format(r,g,b)

# You can make aliases to functions easily by assigning new names as well,
# which will keep the peace when spelling 'color' or 'colour' out there. Notice
# the functions do not have () at the end. This means we want a reference to
# the function and not the output of the function. As you an see this means
# functions can be passed around just like strings, numbers and anything else
# you can put in a variable.

random_colour = random_color
colour_random = random_color
# TODO go ahead, make your own alias for random_color

# Ok, now let's use them

zombie.color = random_color()
draw_square()

zombie.check()
