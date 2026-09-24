import random
import turtle
from turtle import Turtle, Screen
from colors import color_list

timmy = Turtle()
turtle.colormode(255)

def random_color():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    color = (red, green, blue)
    return color

directions = {0, 90, 180, 270}
timmy.pensize(10)
timmy.speed("fastest")

for _ in range(1000):
    angle = random.choice(tuple(directions))
    # timmy.color(random.choice(color_list)[0])
    timmy.color(random_color())
    # timmy.pencolor(random.choice(color_list)[0])
    timmy.setheading(angle)
    timmy.forward(20)

screen = Screen()
screen.exitonclick()