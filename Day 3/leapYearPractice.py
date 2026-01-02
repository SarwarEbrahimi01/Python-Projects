# Write a program that works out whether if a given year is a leap year. A normal year has 365 days. Leap years have 366 days
# with an extra day in February. Hint: on every year that is evenly divisible by 4 except every year that is evenly divisible by 100
# unless the year is also evenly divisible by 400

# ******************** Don't Change **************************
year = int(input("Which year do you want to check? "))
# ******************** Don't Change **************************


# The code logic
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f" The year {year} is a leap year.")
        else:
            print(f" The year {year} is not a leap year.")
    else:
        print(f"The year {year} is a leap year.")
else:
    print(f" The year {year} is not a leap year.")






