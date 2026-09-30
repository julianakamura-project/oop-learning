from turtle import Turtle

INIT_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.body_seg = []
        self.create_snake()
        self.head = self.body_seg[0]

    def create_snake(self):
        for coord in INIT_POSITIONS:
            body = Turtle("square")
            body.color("white")
            body.penup()
            body.goto(coord)
            self.body_seg.append(body)

    def move(self):
        for body_num in range(len(self.body_seg) - 1, 0, -1):
            self.body_seg[body_num].goto(self.body_seg[body_num - 1].xcor(),
                                         self.body_seg[body_num - 1].ycor())
        self.head.forward(MOVE_DISTANCE)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.seth(0)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.seth(90)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(180)

    def down(self):
        if self.head.heading() != UP:
            self.head.seth(270)

    def within_boundary(self):
        if (
                self.head.xcor() > 280 or
                self.head.xcor() < -280 or
                self.head.ycor() > 280 or
                self.head.ycor() < -280
        ):
            return False
        return True