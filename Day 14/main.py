# # To Do list:
# # import random module
# import random
# # import data from the game_data
# from game_data import data
# # a function that generate random user from the data
# def generate_random_user(random_user):
#     return random.choice(random_user)


# # a function that formats
# def format(account):
#     name = account['name']
#     desciption = account['description']
#     county = account["country"]
#     return f"{name}, a {desciption}, from {county}"

# # print the two user for comparing


# # get user choice
# # guess = input("Which person has the highest followers? Type 'A' or 'B': ")
# # a function that compares two users and return the highest
# def compare(guess, user_A, user_B):
#     if user_A > user_B:
#         return guess == "A"
#     else:
#         return guess == "B"
# # if the user choice is right give socre and continue game the second item should be compared with new one
# # function that calculate the score in case of right answer
# # if not right then game is over

# def play_game():

#     should_continue = True
#     while should_continue:
#         user_a = generate_random_user(data)
#         while user_a == user_b:
#             user_b = generate_random_user(data)

#     print(f"Compare A: {format(user_a)}.")
#     print(f"Against B: {format(user_b)}")


# play_game()

# Solutin form the video
from art import logo, vs
from game_data import data
import random


def format_data(account):
    """Takes the acount data and return the printable format."""
    account_name = account["name"]
    account_desc = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_desc}, from {account_country}"


def check_answer(guess, a_followers, b_followers):
    """Take the user guess and follower counts and returns if they get it right."""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


# Display art
print(logo)
score = 0
game_should_continue = True
account_b = random.choice(data)

# Make the game repeatable.
while game_should_continue:
    # Generate a random account from the game data.

    # Make account at position B become the next account at position A.
    account_a = account_b
    account_b = random.choice(data)
    while account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Against B: {format_data(account_b)}.")

    # Ask the user for a guess
    guess = input("Who has more followrs? Type 'A' or 'B': ").lower()

    # Check if user is correct.
    ## Get follower count of each account.
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    # Clear the screen.
    # clear()
    # print(logo)

    # Give user feedback on their guess.
    # Score keeping.
    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}.")
    else:
        game_should_continue = False
        print(f"Sorry, that's wrong. Final socre: {score}")







