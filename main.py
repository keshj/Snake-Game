from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

window = Screen()
window.title("My Snake Game")
window.setup(width=600, height=600)
window.bgcolor("Black")
window.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

window.listen()
window.onkey(snake.up, "Up")
window.onkey(snake.down, "Down")
window.onkey(snake.left, "Left")
window.onkey(snake.right, "Right")

is_game_on = True
while is_game_on:
    window.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        snake.extend_snake()
        food.refresh()
        scoreboard.increment_score()

    if snake.head.xcor() > 280 or snake.head.xcor() < -290 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.game_over()
        is_game_on = False

    for segment in snake.segments[1:]:
        if segment.distance(snake.head) < 5:
            scoreboard.game_over()
            is_game_on = False

window.exitonclick()
