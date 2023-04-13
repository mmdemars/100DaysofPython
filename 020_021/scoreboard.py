from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 18, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.goto(0,270)
        self.score = 0
        self.color("white")
        self.penup()
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)


    def score_up(self):
        self.score +=1
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.write("-> GAME OVER <-", align= ALIGNMENT, font = ("Courier", 36, "normal"))