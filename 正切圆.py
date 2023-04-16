import turtle
s = turtle.getscreen()
t = turtle.Turtle()
t.pensize(1)
t.fillcolor('red')
t.hideturtle()
turtle.hideturtle()
t.speed(0)

t.begin_fill()
for i in range(4):
    t.fd(100)
    t.rt(90)
t.end_fill()

t.fillcolor('blue')
t.penup()
t.goto(50, -100)
t.pendown()
t.begin_fill()
t.circle(50)
t.end_fill()

t.hideturtle()
turtle.hideturtle()
turtle.done()
