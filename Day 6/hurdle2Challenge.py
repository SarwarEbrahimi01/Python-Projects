#Hurdles race: Reeborg has entered a hurdle race, but he doesn't know in advance how long the race is.
# Make him run the course, following a path similar to the one shown,but stopping at the only flag that will
# be shown after teh race has started.
# What you need to know: The function move() and turn_left()
# The condition at_goal() and its negation. How to use while loop. Your program should be valid for world hurdles 1.
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def move_function():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while at_goal() != True :
    move_function()

# or the alternative
while not at_goal():
    move_function()