import turtle
turtle = turtle.Pen()
turtle.shape('turtle')
n1 = 0
n2 = 0
for i in range(5):
    turtle.penup()
    turtle.setpos(n1 , n2)
    turtle.pendown()
    for j in range(i+3):
        turtle.forward(130)
        turtle.left(360 / (i+3))
    n1 -= 1
    n2 -= 20
    turtle.penup()
    turtle.setpos(n1 , n2)
    turtle.pendown()