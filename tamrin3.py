from secrets import token_urlsafe
import turtle
turtle.shape("turtle")
n = 10
for i in range (4,20) :
    for _ in range (i) :
        turtle.forward(1 + 2*n)
        turtle.right(360 / n )
    n+1
    