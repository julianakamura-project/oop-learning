import random
from turtle import Turtle, Screen
from colors import color_list

timmy = Turtle()
directions = {0, 90, 180, 270}
timmy.pensize(10)
timmy.speed("fastest")
for _ in range(1000):
    angle = random.choice(tuple(directions))
    timmy.color(random.choice(color_list)[0])
    timmy.pencolor(random.choice(color_list)[0])
    timmy.setheading(angle)
    timmy.forward(20)

screen = Screen()
screen.exitonclick()