from turtle import Turtle, Screen
import random

tim = Turtle()
# for _ in range(3):
#     tim.color("red")
#     tim.right(120)
#     tim.forward(100)

# for _ in range(4):
#     tim.color("black")
#     tim.right(360/4)
#     tim.forward(100)

# for _ in range(5):
#     tim.color("orange")
#     tim.right(360/5)
#     tim.forward(100)

# for _ in range(6):
#     tim.color("purple")
#     tim.right(360/6)
#     tim.forward(100)

# for _ in range(7):
#     tim.color("grey")
#     tim.right(360/7)
#     tim.forward(100)

# for _ in range(8):
#     tim.color("blue")
#     tim.right(360/8)
#     tim.forward(100)

# for _ in range(9):
#     tim.color("green")
#     tim.right(360/9)
#     tim.forward(100)

# for _ in range(10):
#     tim.color("pink")
#     tim.right(360/10)
#     tim.forward(100)


turtle_colors = [
    "red", "blue", "green", "yellow", "orange", "purple", "pink", "cyan",
    "magenta", "lime", "gold", "navy", "skyblue", "turquoise", "violet",
    "brown", "chocolate", "darkgreen", "lightgreen", "gray", "black",
    "maroon", "indigo", "salmon", "teal", "seashell", "peru",
    "orchid", "plum", "crimson", "khaki", "azure", "beige", "bisque",
    "chartreuse", "coral", "cornflowerblue", "darkorange", "firebrick"
]


def draw_shape(num_of_sides):
    angle = 360 / num_of_sides
    for _ in range(num_of_sides):
        tim.forward(100)
        tim.right(angle)


for shape_side_n in range(3, 11):
    tim.color(random.choice(turtle_colors))
    draw_shape(shape_side_n)

screen = Screen()
screen.exitonclick()