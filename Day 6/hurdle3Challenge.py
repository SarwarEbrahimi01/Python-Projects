# Reeborg has entered a hurdle race.Make him run the course, following the path shown.
# The position and number of hurdles change each time this world is reloaded.
# What you need to know: 1- The function move() and turn_left()
# 2- The condition front_is_clear() or wall_in_front(),at_goal() and their negation
# 3- How to use a while loop and if statement
# Your program should also be valid for worlds Hurdles 1 and Hurdles 2

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def move_function():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while at_goal() != True: # or while not at_goal():
    if wall_in_front == True:
        move_function()
    else:
        move()