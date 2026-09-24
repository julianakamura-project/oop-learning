from turtle import Turtle, Screen
from colors import color_list
import random

tom = Turtle()
tom.shape("arrow")
tom.color("blue")
tom.teleport(-50)
sides = 3

for shapes in range(8):
    color = random.choice(color_list)[0]
    tom.pencolor(color)
    for _ in range(sides):
        tom.forward(100)
        tom.left(360/sides)
    sides += 1

screen = Screen()
screen.exitonclick()