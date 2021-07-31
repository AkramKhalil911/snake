from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        with open("data.txt", mode="r") as readfile:
            self.highscore = int(readfile.read())
        self.score_number = 0
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

    def reset(self):
        if self.score_number > self.highscore:
            self.highscore = self.score_number
            with open("data.txt", mode="w") as savedscore:
                savedscore.write(str(self.highscore))
        self.score_number = 0
        self.updatescoreboard()