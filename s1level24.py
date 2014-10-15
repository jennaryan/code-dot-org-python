# very first thing must be the JavaScript code from 'Show Code'
''' s1level24
moveForward(100)
turnRight(90)
moveForward(100)
'''

# always import Turtle class (never *)
import turtle

# always create a new Turtle object and give him/her a pen
bob = turtle.Turtle()
bob.pensize(7)
bob.pencolor('red')

# here is where your port goes, notice looks like JavaScript
# use https://docs.python.org/3.4/library/turtle.html for reference
bob.forward(100)
bob.right(90)
bob.forward(100)

# you only need this if not using Python IDLE to keep it from closing early
input()
