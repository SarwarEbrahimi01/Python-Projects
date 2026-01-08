import random

rock = '''
✊
'''
paper = '''
🫱
'''
scissors = '''
✌️
'''
game_images = [rock, paper, scissors]
user_choice = int(input("What do you choose? Type 0 for Rocks, 1 for paper or 2 for Scissors.\n "))
if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number, you lose!")
else:
    print(game_images[user_choice])

    computer_choice = random.randint(0, 2)

    print("Computer chose: ")
    print(game_images[computer_choice])

    # if user_choice == 0 and computer_choice == 0:
    #    print("Equal")
    # elif user_choice == 0 and computer_choice == 1:
    #    print("You lose")
    # elif user_choice == 0 and computer_choice ==2:
    #    print("You win")
    # if user_choice == 1 and computer_choice == 0:
    #    print("You win")
    # elif user_choice == 1 and computer_choice == 1:
    #    print("Equal")
    # elif user_choice == 1 and computer_choice ==2:
    #    print("you lose")
    # if user_choice == 2 and computer_choice == 0:
    #    print("You lose")
    # elif user_choice == 2 and computer_choice == 1:
    #    print("You win")
    # elif user_choice == 2 and computer_choice ==2:
    #    print("Equal")

    # The best solution in a shorter and enhanced way from the video

    if user_choice == 0 and computer_choice == 2:  # exception when calculating the logic
        print("You win!")
    elif computer_choice == 0 and user_choice == 2:
        print("You lose!")
    elif computer_choice > user_choice:  # This is true according to the rule
        print("You lose!")
    elif user_choice > computer_choice:
        print("You win!")
    elif computer_choice == user_choice:
        print("It's a draw. ")

