from turtle import Screen
from food import Food
from scoreBoard import Scoreboard
import time

from food import Food
from snake import Snake

"""
   Snake Game (main.py)

   This is the main file for the Snake Game built using Python's `turtle` graphics.
   It initializes the game window, creates the snake, food, and scoreboard objects,
   and manages the main game loop including movement, collision detection, and scoring.

   Modules used:
   - Screen (from turtle): For the game window
   - Snake (custom class): Controls snake movement and growth
   - Food (custom class): Manages random placement of food
   - Scoreboard (custom class): Displays and updates the score

   Controls:
       - Arrow keys (Up, Down, Left, Right) → Move the snake
   """

# Setup the game screen
screen = Screen()
screen.bgcolor("black")
screen.title("My Snake game")
screen.tracer(0)
screen.setup(width = 600,height = 600)

# Create game objects
snake = Snake()
food = Food()
board = Scoreboard()

# Game state variable
is_game_on = True

# Keyboard bindings
screen.listen()
screen.onkey(key = "Up",fun = snake.up)
screen.onkey(key = "Down",fun = snake.down)
screen.onkey(key = "Left",fun = snake.left)
screen.onkey(key = "Right",fun = snake.right)

score = 0

# Main game loop
while is_game_on:
     screen.update()
     time.sleep(0.1)
     snake.move()

     # Detect collision with food
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

# Close game when user clicks the window
screen.exitonclick()