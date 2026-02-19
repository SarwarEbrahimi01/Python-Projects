# %%%%%%%%%%%%%%%%%%%%% Blackjack Project %%%%%%%%%%%%%%%%%%%%%%

# Difficulty Normal: Use all hints below to complete the project.
# Difficulty Hard: Use only hints 1,2,3 to complete the project.
# Difficulty Extra Hard: Only use hints 1 & 2 to complete the project.
# Difficulty Expert: Only use all hint 1 to complete the project.

# %%%%%%%%%%%%%%%%%%%%% Our Blackjack House Rules %%%%%%%%%%%%%%%%%%%%%%

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards.
# cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
## The cards in the list have equal probability of  being drawn.
## Cards are not removed from the deck as they are drawn.

# %%%%%%%%%%%%%%%%%%%%%%% Hints %%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# Hint 1: Go to this website and try out the Blackjack game:
#   https://games.washingtonpost.com/games/blackjack/
# Then try out the completed Blackjack project here:
#   https://blackjack-final.appbrewery.repl.run

# Hint 2: Read this breakdown of program requirements:
#   https://listmoz.com/view/6h34
# Then try to create your own flowchart for the program.

# Hint 3: Download and read this flow chart I've created:
#   https://drive.google.com/uc?

# Hint 4: Create a deal_card() function that uses the List below to return a random card.
# 11 is the Ace.
# cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

# Hint 5: Deal the user and computer 2 cards each using deal_card()
# user_cards = []
# computer_cards = []

# Hint 6: Create a function called calculate_scores() that takes a List of cards as input and returns the score.
# Look up the sum() function to help you do this.

# cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

# Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score.0 will represent a blackjack in our game
# Hint 8: Inside calculate_score() check for an 11(ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

# Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then game ends.

# Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function  to add another card to the user_card List. If no, then the game has ended

# Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

# Hint 12: Once the user is done and no longer wants to draw more cards, it's time to let the computer play. The computer should keep drawing cards as it has a score less than 17.

# Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack(0), then user loses. If the user has a blackjack(0), then the user wins.
# If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

# Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py


# Hint 4
import random


def deal_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    # if rand == 11:

    #     return "Ace"
    return card


def play_game():
    # Hint 5
    user_cards = []
    computer_cards = []
    is_game_over = False

    for i in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    # print(user_cards)
    # print(computer_cards)

    # Hint 6
    # def calculate_scores(user, computer):
    #     user_score = sum(user)
    #     computer_score = sum(computer)

    #     if user_score > computer_score:
    #         print(f" user {user_score}")
    #         return user_score
    #     else:
    #         print(f" computer {computer_score}")
    #         return computer_score

    # calculate_scores(user=user_card, computer=computer_card)

    def calculate_score(cards):
        """Take a list of cards and return the score calculated from the cards"""
        # Hint 7
        if sum(cards) == 21 and len(cards) == 2:
            return 0

        # Hint 8
        if 11 in cards and sum(cards) > 21:
            cards.remove(11)
            cards.append(1)
        return sum(cards)

    # Hint 11
    while not is_game_over:
        # Hint 9
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f" Your cards: {user_cards}, current score: {user_score}")
        print(f" Computer's first cards: {computer_cards[0]}")
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:  # Hint 10
            user_answer = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if user_answer == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    # Hint 12
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    # Hint 13
    def compare(u_s, c_s):
        if u_s == c_s:
            return "It's a draw"
        elif c_s == 0:
            return "Lose, opponent has a Blackjack"
        elif u_s == 0:
            return "Win with a Blackjack"
        elif u_s > 21:
            return "You went over. You lose"
        elif c_s > 21:
            return "The opponent went over. You win"
        elif u_s > c_s:
            return "You win"
        else:
            return "You lose"

    print(f"    Your final hand: {user_cards}, final score: {user_score}")
    print(f"    Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))


# Hint 14
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    play_game()












