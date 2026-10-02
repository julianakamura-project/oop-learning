from turtle import Turtle
ALIGNMENT = "center"
FONT = "Courier"
SIZE = 12
STYLE = "normal"

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(x=0, y=270)
        self.update_score()

    def update_score(self):
        self.write(arg=f"Score: {self.score}",
                   move=False,
                   align=ALIGNMENT,
                   font=(FONT, SIZE, STYLE)
                   )

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.write(arg="GAME OVER",
                   move=False,
                   align=ALIGNMENT,
                   font=(FONT, SIZE, STYLE))