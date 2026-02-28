from turtle import Turtle, Screen
tim= Turtle()
tim.shape("turtle")
tim.color("red")
for _ in range(15):
    tim.pendown()
    tim.forward(10)
    tim.penup()
    tim.forward(10)

# Alternative Solution
# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()



screen = Screen()
screen.exitonclick()