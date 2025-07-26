import turtle
import random

def random_walker(steps):
    directions = [0, 90, 180, 270]
    for _ in range(steps):
        turtle.setheading(random.choice(directions))
        turtle.forward(20)

# execute
random_walker(100)
turtle.done()
