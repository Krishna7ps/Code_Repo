import turtle

wn=turtle.Screen()
wn.bgcolor("lightgreen")
t=turtle.Turtle()
t.pensize(3)
t.pencolor("hotpink")

length=5
for i in range(50):
    t.forward(length)
    t.left(90)
    length+=5

wn.mainloop()
