# write a program that interprets the BMI on a user's weight and height
# It should tell them the interpretation of their BMI base on the BMI value
# 1- under 18.5 they are underweight
# 2- over 18.5 but below 25 they have a normal weight
# 3- over 25 but below 30 they are overweight
# 4- over 30 but below 35 they are obese
# 5- above 35 they are clinically obese.

# $$$$$$$$$$$$$$$$$$$$ Don't Change the following $$$$$$$$$$$$$$$$$$$$$$$$$$$
height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))
# $$$$$$$$$$$$$$$$$$$$ Don't Change the following $$$$$$$$$$$$$$$$$$$$$$$$$$$

bmi = round(weight / height **2)




if bmi  < 18.5:
    print(f"Your BMI is {bmi}, and your are underweight.")

elif bmi < 25:
    print(f"your MBI is {bmi}, and you have a normal weight.")
elif bmi < 30:
    print(f"your BMI is {bmi}, and your are overweight.")
elif bmi < 35:
    print(f"your BMI is {bmi}, and your are obese.")
else:
    print(f"your BMI is {bmi}, and your are clinically obese.")


