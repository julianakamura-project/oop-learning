from turtle import Turtle

class Boundary(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.fillcolor("")
        self.pencolor("white")
        self.shapesize(stretch_wid=29, stretch_len=29)
        self.penup()