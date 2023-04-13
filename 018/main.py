import turtle as t
from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.hideturtle()
timmy.speed("fastest")

t.colormode(255)
colors = [(113, 96, 71), (169, 157, 130), (57, 39, 20), (94, 85, 119), (146, 133, 97), (100, 83, 94), (85, 66, 34), (59, 40, 52), (210, 197, 157), (223, 211, 179), (0, 139, 139)]

timmy.penup()
timmy.left(90)
timmy.forward(225)
timmy.left(90)
timmy.forward(225)
timmy.right(180)

def dot_line():
    for i in range(9):
        timmy.dot(20, random.choice(colors))
        timmy.forward(50)
    timmy.dot(20, random.choice(colors))

def next_to_right():
    timmy.right(90)
    timmy.forward(50)
    timmy.right(90)

def next_to_left():
    timmy.left(90)
    timmy.forward(50)
    timmy.left(90)

for i in range(5):
    dot_line()
    next_to_right()
    dot_line()
    next_to_left()




screen = Screen()
screen.exitonclick() 