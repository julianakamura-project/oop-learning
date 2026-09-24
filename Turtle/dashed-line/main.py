from turtle import Turtle, Screen

tim = Turtle()
tim.teleport(-150)

for _ in range(15):
    tim.pendown()
    tim.forward(10)
    tim.penup()
    tim.forward(10)

screen = Screen()
screen.screensize(1000, 500)
screen.exitonclick()