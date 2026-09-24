from turtle import Turtle, Screen
from shapes import shapes_sides

tim = Turtle()
tim.shape("turtle")
tim.color("blue")
tim.teleport(-200, -300)

def sides_angle(shape):
    for i in range(len(shapes_sides)):
        if shape in shapes_sides[i]:
            angle = shapes_sides[i]["angle"]
            sides = shapes_sides[i][shape]
            side_size = shapes_sides[i]["side size"]
    return sides, angle, side_size

def move_turtle(angle, side_size):
    tim.forward(side_size)
    tim.left(angle)

shape = input("What shape would you like me to draw?\n(Triangle/Square/Pentagon/Hexagon/"
              "Heptagon/Octagon/Nonagon/Decagon)\n").lower()
number_sides, angle, side_size = sides_angle(shape)
for sides in range(number_sides):
    move_turtle(angle, side_size)

screen = Screen()
screen.exitonclick()
