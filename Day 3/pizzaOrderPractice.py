# Small Pizza: $15
# Medium Pizza: $20
# Large Pizza: $25
# Pepperoni for Small Pizza: +$2
# Pepperoni for Medium or Large Pizza: +$3
# Extra cheese for any size pizza: +$1


# ****************** Don't Change ***********************
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? (Y/N) ")
extra_cheese = input("Do you want extra cheese? (Y/N) ")
# ****************** Don't Change ***********************

bill = 0

if size == "S":
    bill += 15
    if add_pepperoni == "Y":
        bill += 2
        if extra_cheese == "Y":
            bill += 1
            print(f"Your final bill is ${bill}")
        else:
            print(f"Your final bill is ${bill}")
    else:
        if extra_cheese == "Y":
            bill += 1
            print(f"Your total bill is ${bill}")
        else:
            print(f"Your total bill is ${bill}")
elif size == "M":
    bill += 20
    if add_pepperoni == "Y":
        bill += 3
        if extra_cheese == "Y":
            bill += 1
            print(f"Your total bill is ${bill}")
        else:
            print(f"Your total bill is ${bill}")
    else:
        if extra_cheese == "Y":
            bill += 1
            print(f"Your total bill is ${bill}")
        else:
            print(f"Your total bill is ${bill}")
elif size == "L":
    bill += 25
    if add_pepperoni == "Y":
        bill += 3
        if extra_cheese == "Y":
            bill += 1
            print(f"Your total bill is ${bill}")
        else:
            print(f"Your total bill is ${bill}")
    else:
        if extra_cheese == "Y":
            bill += 1
            print(f"Your total bill is ${bill}")
        else:
            print(f"Your total bill is ${bill}")
else:
    print("You have entered and invalid choice")

# Alternative short Solution
bill = 0
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:
    bill += 25

if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"Your total bill is ${bill}")






