# You are going to write a program which will mark a spot with an X.
# The map is made of 3 rows of blank squares. Your program should allow you to enter
# the position of the treasure using a two-digit system.The first digit is the vertical column number and the second digit is the horizontal row number.

# %%%%%%%%%%%%% Don't Change %%%%%%%%%%%%%%%%%
row1 = ["🪟","🪟","🪟 "]
row2 = ["🪟","🪟","🪟 "]
row3 = ["🪟","🪟","🪟 "]
map = [row1,row2,row3]
print(f"{row1}\n{row2}\n{row3} ")
position = input("Where do you want to put the reasure? ")
# %%%%%%%%%%%%% Don't Change %%%%%%%%%%%%%%%%%
# 23
horizontal = int(position[0]) #2
vertical = int(position[1]) #3

selected_row = map[vertical - 1]
selected_row[horizontal - 1] = "X"

print(f"{row1}\n{row2}\n{row3} ")


