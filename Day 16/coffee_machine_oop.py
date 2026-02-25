from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

#STEP 1:
#Creating Objects
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
is_on = True

#Calling the methods of the objects
# coffee_maker.report()
# money_machine.report()

#STEP 2:
#Check resources sufficients?
while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}):")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        #Check resources sufficients?
        #STEP 3:
            #Process coins.
        #STEP 4:
            #Check transaction successful?
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                #STEP 5:
                #Make coffee
                coffee_maker.make_coffee(drink)

