import turtle

turtle.delay(1)

t = turtle.Turtle()

t.penup()
t.setposition(0, 240)

for i in range(61):
    t.pendown()
    t.right(23)
    t.forward(60 - i)

    if (60 - i) <= 0:
        break;

    t.penup()
    t.right(23)
    t.forward(60 - i)

t.hideturtle()

turtle.done()