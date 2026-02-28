# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# %%%%%%%%%%%% Drawing a Spirograph %%%%%%%%%%%%%%%%%


import turtle as t
from turtle import Screen
import random

tim = t.Turtle()
tim.speed(0)
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


# for _ in range(120):
#     tim.color(random_color())
#     tim.circle(100)
#     tim.left(3)

# Alternative method for solving the challenge
def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)


draw_spirograph(5)

screen = Screen()
screen.exitonclick()