from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        # Further reduced initial speed
        self.x_move = random.choice([0.2, -0.2])  
        self.y_move = random.choice([0.2, -0.2])  
        self.move_speed = 0.2  
        self.speed("fastest")

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 2.5  

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.2  
        self.x_move = random.choice([0.2, -0.2])  
        self.y_move = random.choice([0.2, -0.2])  
