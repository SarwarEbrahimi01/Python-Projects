# A program that tests the compatibility between two people by using the scientific method by BuzzFeed
# Take both people's names and ckeck for the number of times the letters in word TRUE occurs.Then for the letter LOVE.
# Then combine these numbers to make a 2 digit number.
# For love scores less than 10 or greather than 90, "Your score is x, you go together like coke and mentos"
# For love scores between 40 and 50, "Your score is y, you are alright together"
# Otherwise "Your score is z"

# Hint : 1- The lower() 2- The count() fucntion


# &&&&&&&&&&&&&&&&&&&&&&&&& Don't change &&&&&&&&&&&&&&&&&&&&&&&&
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

# &&&&&&&&&&&&&&&&&&&&&&&&& Don't change &&&&&&&&&&&&&&&&&&&&&&&&
name1_to_lower = name1.lower()
name2_to_lower = name2.lower()

name1_count_t = name1_to_lower.count("t")
name1_count_r = name1_to_lower.count("r")
name1_count_u = name1_to_lower.count("u")
name1_count_e = name1_to_lower.count("e")

name1_true_count = name1_count_t + name1_count_r + name1_count_u + name1_count_e

name1_count_l = name1_to_lower.count("l")
name1_count_o = name1_to_lower.count("o")
name1_count_v = name1_to_lower.count("v")
name1_count_e2 = name1_to_lower.count("e")

name1_love_count = name1_count_l + name1_count_o + name1_count_v + name1_count_e2

name2_count_t = name2_to_lower.count("t")
name2_count_r = name2_to_lower.count("r")
name2_count_u = name2_to_lower.count("u")
name2_count_e = name2_to_lower.count("e")

name2_true_count = name2_count_t + name2_count_r + name1_count_u + name2_count_e

name2_count_l = name2_to_lower.count("l")
name2_count_o = name2_to_lower.count("o")
name2_count_v = name2_to_lower.count("v")
name2_count_e2 = name2_to_lower.count("e")

name2_love_count = name2_count_l + name2_count_o + name2_count_v + name2_count_e2

final_true_count = name1_true_count + name2_true_count
final_love_count = name1_love_count + name2_love_count

total_love_score = int(f"{final_true_count}" + f"{final_love_count}")




if total_love_score < 10 or total_love_score > 90:
    print(f"Your score is {total_love_score}, you go together like coke and mentos ")
elif total_love_score >=40 and total_love_score <= 50:
    print(f"Your score is {total_love_score}, you are alright together")
else:
    print(f"your score is {total_love_score}")


# An alternative easy and short solution from video

combined_string = name1 + name2
lower_case_string = combined_string.lower()

t = lower_case_string.count("t")
r = lower_case_string.count("r")
u = lower_case_string.count("u")
e = lower_case_string.count("e")

true = t + r + u + e

l = lower_case_string.count("l")
o = lower_case_string.count("o")
v = lower_case_string.count("v")
e = lower_case_string.count("e")

love = l + o + v + e

love_score = int(str(true) + str(love))

if (love_score < 10) or (love_score > 90):
    print(f"Your score is {total_love_score}, you go together like coke and mentos ")
elif (love_score >=40) and (love_score <= 50):
    print(f"Your score is {total_love_score}, you are alright together")
else:
    print(f"your score is {total_love_score}")