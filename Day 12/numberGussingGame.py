# The solution based on my own logic
# import random
# print("Welcome to the Number Guessing Game!")
# print("I'm thinking of a number between 1 and 100.")

# number = random.randint(1,100)
# remained_attempts = 10
# print(number)
# end_of_game = False

# def compare(attempts):
#     for i in range(attempts):
#         print(f"You have {attempts} attempts remaining to guess the number.")
#         guess = int(input("Make a guess: "))
#         if guess > number:
#             print("Too high")
#             print("Guess again")
#         elif guess < number:
#             print("Too low")
#             print("Guess again")
#         elif guess == number:
#             print(f"You got it. The answer was {number}")
#             break


#         attempts -= 1
#         if attempts < 1:
#             print("You've run out of guesses. You lose")


# difficulty_type = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
# if difficulty_type == "easy":
#     compare(remained_attempts)

# elif difficulty_type == "hard":
#     remained_attempts = 5
#     compare(remained_attempts)


# The solution based on the video
from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


# Function to check user's guess against actual answer.
def check_answer(guess, answer, turns):
    """check answer against guess. Returns the number of turns remaining."""
    if guess > answer:
        print("Too high.")
        return turns - 1
    elif guess < answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}.")


# Make a function to set difficulty.
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def game():
    # Choosing a random number between 1 and 100.
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)
    print(f"Pssst, the answer is {answer}")

    turns = set_difficulty()

    # Repeat the guessing functionality if they get it wrong.
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        # Let the user guess a number.
        guess = int(input("Make a guess: "))
        # Track the number of turns and reduce by 1 if they get it wrong.
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again.")


game()


