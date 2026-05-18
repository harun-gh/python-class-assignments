import turtle

turtle.delay(1)

t = turtle.Turtle()
t.hideturtle()

for i in range(37):
    t.forward(100)
    t.home()
    t.left(i * 10)

turtle.done()