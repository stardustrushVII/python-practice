import turtle
import random

turtle.speed(0)
turtle.bgcolor("black")

colors = ["red", "blue", "green", "yellow", "cyan", "magenta", "white"]

for angle in range(0, 360, 10):
    turtle.color(random.choice(colors))
    turtle.circle(100)
    turtle.right(10)

turtle.done()
