# Consider the following for building this app
# W = Forwards
# S = Backwards
# A = Counter-Clockwise
# D = Clockwise
# C = Clear drawing
from turtle import Turtle, Screen

tim = Turtle()


def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def move_counter_clockwise():
    tim.left(10)
    # Alternative
    # new_heading = tim.heading() + 10
    # tim.setheading(new_heading)


def move_clockwise():
    tim.right(10)
    # Alternative
    # new_heading = tim.heading() - 10
    # tim.setheading(new_heading)


def clear_drawing():
    tim.reset()
    # Alternative
    # tim.clear()
    # tim.penup()
    # tim.home()
    # tim.pendown()


screen = Screen()
screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=move_counter_clockwise)
screen.onkey(key="d", fun=move_clockwise)
screen.onkey(key="c", fun=clear_drawing)

screen.exitonclick()