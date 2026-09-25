from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
tim.speed("fastest")

def move_forward():
    tim.forward(10)
def move_backward():
    tim.backward(10)
def turn_left():
    tim.left(10)
def turn_right():
    tim.right(10)
def clear():
    tim.home()
    tim.setheading(0)
    tim.clear()
    draw()
def draw():
    tim.pendown()
def stop_drawing():
    tim.penup()

screen.listen()

screen.onkey(key="w", fun=move_forward)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="c", fun=clear)
screen.onkey(key="1", fun=draw)
screen.onkey(key="2", fun=stop_drawing)

screen.exitonclick()