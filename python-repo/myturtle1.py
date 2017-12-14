import turtle

wn.clearscreen()
t=turtle.Turtle()
t.pensize(3)
import random
length=25
angle=93
for i in range(100):
    turtle.speed(10)
    t.pencolor(random.choice(["green","blue"]))
    t.forward(length)
    t.right(angle)
    length+=5
    wn.bgcolor(random.choice(["green","blue"]))
wn.bgcolor("lightgreen")
