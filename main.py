import time
from scoreboard import Scoreboard
from food import Food
from turtle import Screen
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game")

snake = Snake()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.tracer(0)

scoreboard = Scoreboard()
food = Food()
should_continue = True

while should_continue:
    screen.update()
    time.sleep(0.1)

    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.increase_snake()

    # Detect collision with tail
    for segment in snake.segment[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            scoreboard.game_over()
            should_continue = False

    snake.passage()
    snake.move()

screen.exitonclick()

# detect collision with wall
# if snake.head.xcor() > 275 or snake.head.xcor() < -275 or snake.head.ycor() > 275 or snake.head.ycor() < -275:
#     scoreboard.game_over()
#     should_continue = False
