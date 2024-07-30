from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)
        self.speed("fastest")

    def go_up(self):
        if self.ycor() < 270 - (self.shapesize()[0] * 10 / 2):
            self.sety(self.ycor() + 20)

    def go_down(self):
        if self.ycor() > -250 + (self.shapesize()[0] * 10 / 2):
            self.sety(self.ycor() - 20)
