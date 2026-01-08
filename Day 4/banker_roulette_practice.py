# You are going to write a program which will select a random name from a list of names.The person selected will have tl pay for everybody's food bill.
# important: You are not allowed to use the choice() function. Line 8 splits the string names_string into individual names and puts them inside a List called names.
# for this work, you must enter all the names as name followed by comma then space e.g.name,name,name.

import random
#============Split string method=================
print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
names_string = input("Give me everybody's names, seperated by a comma. \n")
names = names_string.split(",")
print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
#============Don't change above code=================

length = len(names)
random_number = random.randint(0,length-1)

print(f"{names[random_number]} is going to pay for the meal today!")
print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")

# alternative way is to use choice() function with less code
# person_who_will_pay = random.choice(names)
