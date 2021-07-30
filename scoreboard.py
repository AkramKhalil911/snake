from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.number = 0

    def score(self):
        self.reset()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 270)
        self.number += 1
        self.write(f"Your score = {self.number}", align="center", font=("Arial", 16, "normal"))

    def gameover(self):
        self.goto(0, 0)
        self.penup()
        self.hideturtle()
        self.color("white")
        self.write(f"Game over", align="center", font=("Arial", 16, "normal"))