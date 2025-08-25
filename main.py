from turtle import Screen
from food import Food
from scoreBoard import Scoreboard
import time

from food import Food
from snake import Snake

screen = Screen()
screen.bgcolor("black")
screen.title("My Snake game")
screen.tracer(0)
screen.setup(width = 600,height = 600)


snake = Snake()
food = Food()
board = Scoreboard()
is_game_on = True
screen.listen()
screen.onkey(key = "Up",fun = snake.up)
screen.onkey(key = "Down",fun = snake.down)
screen.onkey(key = "Left",fun = snake.left)
screen.onkey(key = "Right",fun = snake.right)
score = 0
while is_game_on:
     screen.update()
     time.sleep(0.1)
     snake.move()

     if snake.head.distance(food) < 15:
          food.refresh()
          snake.extend()
          board.increase_score()
     #detect collision with wall
     if snake.head.xcor() >280 or snake.head.xcor()<-280 or snake.head.ycor() >280 or snake.head.ycor()<-280:
          board.reset()
          snake.reset_snake()
     #detect collision with tail
     for segment in snake.segments[1:]:
          if snake.head.distance(segment) < 10:
               board.reset()
               snake. reset_snake()

screen.exitonclick()