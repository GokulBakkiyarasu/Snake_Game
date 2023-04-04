from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreCard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreCard()

screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Right", fun=snake.right)
screen.onkey(key="Left", fun=snake.left)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    if scoreboard.current_score <= 15:
        snake.move_easy()
    elif scoreboard.current_score <= 30:
        snake.move_medium()
    else:
        snake.move_hard()
    # Detecting collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.score_count()
        snake.append_segment()
    # Detect collision with wall
    if snake.head.xcor() > 285 or snake.head.xcor() < -285 or snake.head.ycor() > 285 or snake.head.ycor() < -285:
        scoreboard.reset()
        snake.reset()
    # Detect collision with tail
    for segments in snake.segments[1:]:
        if snake.head.distance(segments) < 8:
            scoreboard.reset()
            snake.reset()
screen.exitonclick()
