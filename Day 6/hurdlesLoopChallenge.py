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
    turn_left

for move in range(1,7):
   move_function()

# or alternative
for step in range(6):
    move_function()