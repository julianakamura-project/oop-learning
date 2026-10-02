from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from border import Boundary
import time

## Screen Setup
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("black")
screen.title("Snake")
##

## Game components
snake = Snake()
food = Food()
scoreboard = Scoreboard()
boundary = Boundary()

### Movements
screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

## Game body
game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    ### Collision with Food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    ### Collision with boundary
    if (
            snake.head.xcor() > 280 or
            snake.head.xcor() < -290 or
            snake.head.ycor() > 280 or
            snake.head.ycor() < -280
    ):
        game_on = False
        scoreboard.game_over()

    ### Collision with tail
    for segment in snake.body_seg[1:-1]:
        if snake.head.distance(segment) < 10:
            game_on = False
            scoreboard.game_over()








screen.exitonclick()