print("Welcome the Tip Calculator Program.")
total_bill = float(input("What was the total bill? $"))
percentage = int(input("What percentage tip would you like to give? 10, 12, or 15 "))
no_of_people = int(input("How many people to split the bill? "))

result = (total_bill/no_of_people) * 1.12

final_result = round(result, 2)

print(f" Each person should pay ${final_result}")


# Alternative solution according to video

print("Welcome to the Tip Calculator Program!")
bill = float(input("What was your total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15 ? "))
people = int(input("How many people to split the bill? "))
tip_as_percentage = tip / 100
total_tip_amount = bill * tip_as_percentage
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = "{:.2f}".format(bill_per_person)
print(f" Each person should pay ${final_amount}")



