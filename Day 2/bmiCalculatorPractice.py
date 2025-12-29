# Write a program that calculates the Body Mass Index(BMI)
# from a user's weight and height. The BMI is a measure of some's weight taking into account their height e.g. if a tall
#person and a short person both weigh the same amount, the short person is usually more overweight.
# The BMI is calculated by dividing a person's weigh in kg by the square of their height im m

# ================= Don't change ======================
height = input("Enter your height in m: ")
weight = input("Enter your weight in kg: ")
# ================= Don't change ======================
weight2 = float(weight)
height2 = float(height)
bmi = weight2 / height2 **2
print(int(bmi))

age = 18
height = 175
print("You are " + str(age) + " years old" + "and your height is " + str(height) + "m")

print(f"You are {age} years old" + f"and your height is {height} m")
