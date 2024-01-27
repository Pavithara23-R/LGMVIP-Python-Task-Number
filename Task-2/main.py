from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

#calling class
snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Moving forward the snake
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.3)
    snake.move()

# detect collison with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()


        # detect collison with the wall.
    if snake.head.xcor() > 295 or snake.head.xcor() < -295 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False
        scoreboard.game_over()

        # detect collison with snake body.
        for part in snake.parts:
            if part == snake.head:
                pass
            elif snake.head.distance(part) < 10:
                game_is_on = False
                scoreboard.game_over()

screen.exitonclick()