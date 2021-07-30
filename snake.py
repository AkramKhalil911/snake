from turtle import Turtle
MOVE_DISTANCE = 20
STARTING_POSITION = [(-20, 0), (-40, 0)]

class Snake:
    def __init__(self):
        self.newsnake = []
        self.create_snake()
        self.move()

    def create_snake(self):
        for start in STARTING_POSITION:
            self.snake_segment(start)

    def snake_segment(self, position):
        for _ in range(0, 1):
            snake = Turtle("square")
            snake.penup()
            snake.color("white")
            snake.goto(position)
            self.newsnake.append(snake)

    def extend_snake(self):
        self.snake_segment(self.newsnake[-1].position())

    def move(self):
        for step in range(len(self.newsnake) - 1, 0, -1):
            new_x = self.newsnake[step - 1].xcor()
            new_y = self.newsnake[step - 1].ycor()
            self.newsnake[step].goto(new_x, new_y)
        self.newsnake[0].forward(MOVE_DISTANCE)

    def left(self):
        if self.newsnake[0].heading() == 0:
            pass
        else:
            self.newsnake[0].setheading(180)

    def right(self):
        if self.newsnake[0].heading() == 180:
            pass
        else:
            self.newsnake[0].setheading(0)

    def up(self):
        if self.newsnake[0].heading() == 270:
            pass
        else:
            self.newsnake[0].setheading(90)

    def down(self):
        if self.newsnake[0].heading() == 90:
            pass
        else:
            self.newsnake[0].setheading(270)