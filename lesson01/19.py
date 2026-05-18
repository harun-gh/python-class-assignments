import turtle
import random

turtle.setup(800, 800)

t = turtle.Turtle()

while True:
    t.forward(random.random() + 72)
    t.right(random.random() + 412)

turtle.done()