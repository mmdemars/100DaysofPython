from turtle import Turtle, Screen

bob = Turtle()
screen = Screen()

def move_forward():
    bob.forward(10)

def move_backward():
    bob.backward(10)

def turn_left():
    bob.left(15)

def turn_right():
    bob.right(15)

def start_over():
    bob.reset()

screen.listen()

screen.onkey(key = "space", fun = move_forward)
screen.onkey(key = "s", fun = move_backward)
screen.onkey(key = "c", fun=start_over)
screen.onkey(key = "a", fun=turn_left)
screen.onkey(key = "d", fun=turn_right)


screen.exitonclick()



