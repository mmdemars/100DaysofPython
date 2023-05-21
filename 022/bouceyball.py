from turtle import Turtle
import random

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 10

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x,new_y)

    def bounce(self):
        self.y_move *= -1

    def slapped(self):
        if self.x_move < 0:
            self.x_move -= random.randrange(1,3)
            self.y_move -= random.randrange(1,3)
        elif self.x_move > 0:
            self.x_move += random.randrange(1,3)
            self.y_move += random.randrange(1,3)
        self.x_move *= -1

    def reset_position(self):
        self.goto(0,0)
        if self.x_move > 0:
            self.x_move = 10
            self.y_move = 10
        else:
            self.x_move = -10
            self.y_move = -10
        self.slapped()