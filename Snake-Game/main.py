from turtle import Screen, Turtle
import time

### Screen Setup
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("black")
screen.title("Snake")
###

### Initial Snake
positions = [(0,0), (-20,0), (-40,0)]
body_segments = []
for coord in positions:
    body = Turtle("square")
    body.color("white")
    body.penup()
    body.goto(coord)
    body_segments.append(body)
screen.update()
###

### Movements
def face_right():
    body_segments[0].seth(0)
def face_up():
    body_segments[0].seth(90)
def face_left():
    body_segments[0].seth(180)
def face_down():
    body_segments[0].seth(270)

screen.onkey(key="Up", fun=face_up)
screen.onkey(key="Down", fun=face_down)
screen.onkey(key="Left", fun=face_left)
screen.onkey(key="Right", fun=face_right)
####

### Game body
game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    screen.onkey(key="Up", fun=face_up)
    screen.onkey(key="Down", fun=face_down)
    screen.onkey(key="Left", fun=face_left)
    screen.onkey(key="Right", fun=face_right)
    for body_num in range(len(body_segments)-1, 0, -1):
        body_segments[body_num].goto(body_segments[body_num-1].xcor(),
                                     body_segments[body_num-1].ycor())
    body_segments[0].forward(20)
###








screen.exitonclick()