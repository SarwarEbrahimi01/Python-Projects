MENUE = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24
        },
        "cost": 3.0
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


# turn_on = True
# money = 0
# change = 0

# def calculate_money(quarters, dimes, nickles, pennies):
#     money = (quarters*0.25)+(dimes*0.10)+(nickles*0.05)+(pennies*0.01)
#     return money


# #TODO-1:
# while turn_on:
#     user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
#     if user_choice == "espresso":
#         cost = 1.50
#         #TODO-4:
#         if resources["water"] < 50 or resources["coffee"] < 18:
#             print(f"Sorry there is not enough resourcess ")
#         #TODO-5:
#         else:
#             print("Please insert coins.")
#             quarters = int(input("How many quarters?: "))
#             dimes = int(input("How many dimes?: "))
#             nickles = int(input("How many nickles?: "))
#             pennies = int(input("How many pennies?: "))
#             user_money = calculate_money(quarters, dimes, nickles, pennies)
#             #TODO-6:
#             if user_money < cost:
#                 print("Sorry that's not enough money. Money refunded.")
#             elif user_money == cost:
#                 money += user_money
#                 resources["water"] -= 50
#                 resources["coffee"] -= 18
#                 print(f"Here is your {user_choice}. Enjoy!")
#             elif user_money > cost:
#                 change = round(user_money - cost, 2)
#                 money += user_money - change
#                 print(f"Here is ${change} dollars in change.")
#                 resources["water"] -= 50
#                 resources["coffee"] -= 18
#                 print(f"Here is your {user_choice}. Enjoy!")

#     elif user_choice == "latte":
#         cost = 2.50
#         #TODO-4:
#         if resources["water"] < 200 or resources["milk"] < 150 or resources["coffee"] < 24:
#             print(f"Sorry there is not enough resourcess ")
#         #TODO-5:
#         else:
#             print("Please insert coins.")
#             quarters = int(input("How many quarters?: "))
#             dimes = int(input("How many dimes?: "))
#             nickles = int(input("How many nickles?: "))
#             pennies = int(input("How many pennies?: "))
#             user_money = calculate_money(quarters, dimes, nickles, pennies)
#             #TODO-6:
#             if user_money < cost:
#                 print("Sorry that's not enough money. Money refunded.")
#             elif user_money == cost:
#                 money += user_money
#                 money = round(money,2)
#                 resources["water"] -= 200
#                 resources["milk"] -= 150
#                 resources["coffee"] -= 24
#                 print(f"Here is your {user_choice}. Enjoy!")
#             elif user_money > cost:
#                 change = round(user_money - cost, 2)
#                 money += user_money - change
#                 money = round(money,2)
#                 print(f"Here is ${change} dollars in change.")
#                 resources["water"] -= 200
#                 resources["milk"] -= 150
#                 resources["coffee"] -= 24
#                 print(f"Here is your {user_choice}. Enjoy!")


#     elif user_choice == "cappuccino":
#         cost = 3.00
#         #TODO-4:
#         if resources["water"] < 250 or resources["milk"] < 100 or resources["coffee"] < 24:
#             print(f"Sorry there is not enough resourcess ")
#         #TODO-5:
#         else:
#             print("Please insert coins.")
#             quarters = int(input("How many quarters?: "))
#             dimes = int(input("How many dimes?: "))
#             nickles = int(input("How many nickles?: "))
#             pennies = int(input("How many pennies?: "))
#             user_money = calculate_money(quarters, dimes, nickles, pennies)
#             #TODO-6:
#             if user_money < cost:
#                 print("Sorry that's not enough money. Money refunded.")
#             elif user_money == cost:
#                 money += user_money
#                 resources["water"] -= 250
#                 resources["milk"] -= 100
#                 resources["coffee"] -= 24
#                 print(f"Here is your {user_choice}. Enjoy!")
#             elif user_money > cost:
#                 change = round(user_money - cost, 2)
#                 money += user_money - change
#                 print(f"Here is ${change} dollars in change.")
#                 resources["water"] -= 250
#                 resources["milk"] -= 100
#                 resources["coffee"] -= 24
#                 print(f"Here is your {user_choice}. Enjoy!")

#     #TODO-2:
#     elif user_choice == "off":
#         turn_on = False
#     #TODO-3:
#     elif user_choice == "report":
#         print(f"Water: {resources['water']}ml")
#         print(f"Milk: {resources['milk']}ml")
#         print(f"Coffee: {resources['coffee']}g")
#         print(f"Money: ${money}")


# Solution based on the video
def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
        return True


def process_coins():
    """Returns total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    """Returns True when the payment is accepted, or False if money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕ . Enjoy it!")


is_on = True
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENUE[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])


