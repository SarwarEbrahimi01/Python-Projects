# While loop syntax
# while something_is_true:
    #Do this
    #Then Do this
    #Then Do this

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

# using while loop as doing the same as for loop in pervious challenge
number_of_hurdels = 6

while number_of_hurdels > 0:
    move_function()
    number_of_hurdels -=1
