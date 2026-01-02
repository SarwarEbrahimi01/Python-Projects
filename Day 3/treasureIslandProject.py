print("Welcome to the Treasure Island.")
print("Your mission is to find the treasure.")
choice1 = input("You're at a cross road. Where do you want to go? Type \"left\" or \"right\" \n ").lower()

if choice1 == "left":
    choice2 = input("Do you want to swim or wait for a boat? Type \"swim\" or \"wait\"\n ").lower()
    if choice2 == "wait":
        choice3 = input("Which door you want to go? Type \"Red\", \"Blue\" or \"Yellow\"\n ").lower()
        if choice3 == "yellow":
            print("Horray! you win the game")
        elif choice3 == "red":
            print("you're burned by fire. Game Over!")
        else:
            print("Game Over!")
    else:
        print("Attacked by trout. Game Over")
else:
    print("You fall into a hole.Game Over")




