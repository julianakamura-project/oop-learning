from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
y_position = 125
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
turtles_list = []
race_on = False

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ").lower()

for color in colors:
    new_turtle = Turtle("turtle")
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.goto(-240, y_position)
    turtles_list.append(new_turtle)
    y_position -= 50

if user_bet:
    race_on = True

while race_on:
    for turtles in turtles_list:
        if turtles.xcor() > 225:
            if turtles.color()[0] == str(user_bet):
                print("You Win!")
            else:
                print(f"You Lose. The winner is {turtles.color()[0]}.")
            race_on = False
            continue
        distance = random.randint(0, 10)
        turtles.forward(distance)

screen.exitonclick()