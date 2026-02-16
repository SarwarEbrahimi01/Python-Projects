# %%%%%%%%%%%%%%%%%% Exercise 2 %%%%%%%%%%%%%%%%%%%
# You are painting a wall. The instruction# Instructions
# Prime numbers are numbers that can only be cleanly by itself and 1.
# You need to write a function that checks whether if the number passed into it is a prime number or not.
# e.g. 2 is a prime number because it's only divisible by 1 and 2. But 4 isn't a prime number because you can divide it by 1,2 or 4.


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
def prime_checker(number):
    # My own version
    # if number == 2:
    #     print("It's a prime number")
    # elif number % 2 == 0:
    #     print("It's not a prime number.")

    # elif number % number == 0 and number % 1 == 0:
    #     print("It's a prime number.")

    # Video solution
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False

    if is_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number")


# %%%%%%%%%%%%%%%%%%%%% Don't Change below %%%%%%%%%%%%%%%%%%%
n = int(input("Check this number: "))
prime_checker(number=n)