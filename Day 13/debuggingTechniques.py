#%%%%%%%%%%%%%%%%% Debugging %%%%%%%%%%%%%%%%%%%%%

# Describe the problem
# def my_function():
#     # for i in range(1,20): # The problem is that i never reaches the value 20 beacuse the range function takes the value 1 value less than the upperbound
#     # The solution is:
#     for i in range(1,21):
#         if i == 20:
#             print("You got it")

# my_function()

# Reproduc the bugg
# from random import randint
# dice_imgs = ["1","2","3","4","5","6"]
# # dice_num = randint(1,6) # in list the index starts from zero go up but here we have 6 but we don't have index 6 in the list and it gives indexError
# # Solution is:
# dice_num = randint(0,5)
# print(dice_imgs[dice_num])

# Play computer
# year = int(input("What's your year of birth? "))
# if year > 1980 and year < 1994:
#     print("You are a millenial.")
# # elif year > 1994: # 1994 is not included in non of the conditions so you should include it in one of the conditions
# # The solution
# elif year >= 1994:
#     print("You are a Gen Z.")

# Fix the Errors
# age = int(input("How old are you? ")) # Cast the input to the int
# if age > 18:
#    print(f"You can drive at age {age}") # indend tinside the if block and put 'f' to change to f-sting

# Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page = int(input("Number of words per page: ")) # The problem is that it should not be comparison operator(==) but an assignment operator(=)
# total_words = pages * word_per_page
# print(total_words)

# Use a Debugger
def mutate(a_list):
    b_list = []
    for item in a_list:
        new_item = item * 2
        b_list.append(new_item) # This line should be indented to add all items to the b_list
    print(b_list)

mutate([1,2,3,5,8,13])