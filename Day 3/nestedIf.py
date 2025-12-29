# Nested if/else

#if condition:
#    if anothr condition:
#        do this
#    else:
#        do this
#else:
#    do this

# elif is used instead of nested else / if statements

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        print("You have to pay $5")
    elif age <= 18:
        print("Please pay $7")
    else:
        print("Please pay $12")

else:
    print("Sorry, you have to grow taller before you can ride.")
