from turtle import Screen, Turtle
from snake import Snake
import time

## Screen Setup
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("black")
screen.title("Snake")
##

## Game body
snake = Snake()

### Movements
screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)
###

game_on = True
while game_on:
    if not snake.within_boundary():
        game_on = False
        continue
    screen.update()
    time.sleep(0.1)
    snake.move()
##








screen.exitonclick()