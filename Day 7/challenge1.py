# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#    First Step through flow chart
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# Picking a random words and checking answers

# ******** Step 1 *********

word_list = ["ardvark","baboon","camel"]

# TODO-1 - Randomly choose a word from the word_list and assign it to variable called chosen_word.

import random
chosen_word = random.choice(word_list)

# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess.Make quess lowercase.

guess = input("Make a guess of 1 letter: ").lower()

# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

print(chosen_word)
print(guess)
for letter in chosen_word:
    if guess == letter:
        print("Right")
    else:
        print("Wrong")
