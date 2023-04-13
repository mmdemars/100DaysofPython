import turtle as t
from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.shape("turtle")
timmy.color("dark slate gray")

t.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    hue=(r, g, b)
    return hue

# draw a square
# timmy.forward(100)
# timmy.right(90)
# timmy.forward(100)
# timmy.right(90)
# timmy.forward(100)
# timmy.right(90)
# timmy.forward(100)

# line = 1
# for i in range(20):
#     # draw a dashed line - solid then gap 10 paces each for 50 times
#     timmy.pen(pensize=line)
#     timmy.penup()
#     timmy.forward(20)
#     timmy.pendown()
#     timmy.forward(20)
#     line +=1


# make a bunch of shapes in random colors
tones = ['maroon', 'chocolate', 'orange','gold','yellow green','medium aquamarine','dark cyan','dark magenta','deep pink', 'magenta', 'dark slate gray', 'dark olive green']
# sides = 3
# for i in range(10):
#     timmy.color(random.choice(tones))
#     for i in range(sides):
#         timmy.forward(60)
#         timmy.right(360/sides)
#     sides +=1


#take timmy for a random walk

# timmy.forward(20)
# timmy.right(-90)
# timmy.forward(20)
# timmy.right(90)

direction=[0, 90, 180, 270]

# for i in range(300):
#     timmy.pen(pensize=10)
#     timmy.color(random_color())
#     timmy.forward(20)
#     timmy.setheading(random.choice(direction))

timmy.speed("fastest")

# Timmy the Spirograph
#go_go = 10

# def spiro_timtim(size_of_gap):
#     for i in range(int(360/size_of_gap)):
#         timmy.color(random_color())
#         timmy.circle(100)
#         timmy.setheading(timmy.heading() + size_of_gap)
        
        #go_go +=7

# spiro_timtim(3)

# Timmy Hirst


screen = Screen()
screen.exitonclick() 