from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score_number = 0
        self.highscore = 0
        self.score()

    def score(self):
        self.reset()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 270)
        self.updatescoreboard()

    def updatescoreboard(self):
        self.clear()
        self.write(f"Current score: {self.score_number} | High score: {self.highscore}", align="center", font=("Arial", 16, "normal"))

    def increasescore(self):
        self.clear()
        self.score_number += 1
        self.updatescoreboard()

    # def gameover(self):
    #     self.goto(0, 0)
    #     self.penup()
    #     self.hideturtle()
    #     self.color("white")
    #     self.write(f"Game over", align="center", font=("Arial", 16, "normal"))

    def reset(self):
        if self.score_number > self.highscore:
            self.highscore = self.score_number
        self.score_number = 0
        self.updatescoreboard()