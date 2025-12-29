# Write a program that works out whether if a given number is
# even or odd number. Even numbers can be divided by 2 with no
# no remainder e.g.86 is even because 86/2 =43. 43 does not have any decimal places. Therefor the divison is clean
# e.g 59 is odd because 59/2 = 36.785. Modulo is written as % in python. It gives you the reminder after a divison


# ==================== Don't Change ======================

number = int(input("Which number do you want to check? "))

# ==================== Don't Change ======================


if number % 2 ==0:
    print(f" {number} is an even number. ")

else:
    print(f" {number} is an odd number.")

