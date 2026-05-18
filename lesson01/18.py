import turtle

turtle.delay(1)
turtle.colormode(255)

t = turtle.Turtle()

t.pencolor(255, 0, 0)
t.setposition(0, 240)
t.pencolor(255, 128, 0)

for i in range(256):
    t.pencolor(255 - i, 128, i)
    t.forward(256 - i)
    t.right(90)

turtle.done()