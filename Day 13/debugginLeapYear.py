# Read this the code in main.py
# Spot the problem.
# Modify the code to fix the program.
# No shortcuts - don't copy-past to replace the code entirly with a working solution.
# Fix the code so that it works and when you hit submit it should pass all the tests.
year = int(input("Which year do you want to check? "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year.")
        else:
            print("Not Leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year.")