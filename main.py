from turtle import Screen
import time

from scoreboard import Scoreboard
from snake import Snake
from food import Food

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

isTrue = True
snake = Snake()
food = Food()
scoreboard = Scoreboard()

snake.create_snake()
screen.listen()
screen.onkeypress(snake.left, "Left")
screen.onkeypress(snake.right, "Right")
screen.onkeypress(snake.up, "Up")
screen.onkeypress(snake.down, "Down")
while isTrue == True:
    screen.update()
    time.sleep(0.1)
    snake.move()
    print(snake.newsnake[0].pos())

    if snake.newsnake[0].distance(food.pos()) < 15:
        food.move()
        snake.extend_snake()
        scoreboard.increasescore()

    for new_snake in snake.newsnake:
        if new_snake.xcor() > 290 or new_snake.xcor() < -290 or new_snake.ycor() > 290 or new_snake.ycor() < -290:
            scoreboard.reset()
            snake.resetsnake()

    for snakebody in snake.newsnake[1:]:
        if snake.newsnake[0].distance(snakebody) < 10:
            scoreboard.reset()
            snake.resetsnake()

screen.exitonclick()
