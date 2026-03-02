# In order to develop this game we need to divide the problem into 7 separate tasks/Steps
from turtle import Screen, Turtle
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# Step 1:
# Create a snake body

# Step 2:
# Move the snake: Animating the Snake Segments on Screen

# Step 3:
# Create a Snake Class and Move to OOP

# Step 4:
# Control the snake

snake = Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

screen.exitonclick()