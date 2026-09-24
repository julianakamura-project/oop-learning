import turtle
from turtle import Turtle, Screen
import random

tim = Turtle()
tim.speed("fastest")
turtle.colormode(255)
stop = False

def random_color():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    color = (red, green, blue)
    return color

while not stop:
    angle = int(input("Input an angle (1-90): "))
    radius = int(input("Input the radius (10-100): "))

    for _ in range(int(360/angle)):
        tim.color(random_color())
        tim.circle(radius)
        tim.left(angle)

    shift = input("Shift?(y/n): ").lower()
    if shift == 'y':
        tim.left(angle/2)
    elif shift == 'off':
        stop = True

screen = Screen()
screen.exitonclick()