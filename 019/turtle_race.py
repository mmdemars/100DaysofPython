from turtle import Turtle, Screen
import random
screen = Screen()

is_race = False

screen.setup(500, 400)

colors = ["gray", "cyan", "teal", "green", "gold", "purple"]
all_turtles = []

user_bet = screen.textinput(title="Make your bet!", prompt = "Who will win the race? gray, cyan, teal, green, gold, purple")
print(user_bet)
height = -120
speed = [1,2,3,4,5,6,7,8,9,10]

#turtles are made and move to starting line

for turtle_index in range(0,6):
    tim = Turtle(shape="turtle")
    tim.penup()
    tim.goto(x=-230, y = height)
    height +=50
    tim.color(colors[turtle_index])
    all_turtles.append(tim)

if user_bet:
    is_race = True

while is_race:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            winning_turtle = turtle.pencolor()
            if winning_turtle == user_bet:
                print(f"You win! The {winning_turtle} was the fastest!")
            else:
                print(f"You lose! The {user_bet} turtle was not the fastest. The {winning_turtle} turtle won.")
            is_race=False
        random_distance = random.choice(speed)
        turtle.forward(random_distance)

screen.exitonclick()
