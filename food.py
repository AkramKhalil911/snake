import random
from turtle import Turtle

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("red")
        self.speed("fastest")
        self.shapesize(0.5, 0.5)
        random_x = round(random.randint(-280, 280), 0)
        random_y = round(random.randint(-280, 280), 0)
        self.goto(random_x, random_y)

    def move(self):
        random_x = round(random.randint(-280, 280), 0)
        random_y = round(random.randint(-280, 280), 0)
        self.goto(random_x, random_y)