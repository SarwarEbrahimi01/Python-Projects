# Create a program using maths and f_strings that tell us how many days, weeks
# months we have left if we live until 90 years old.
# It will take your current age as the input and output a message with our time left in this format.
# Where x,y and z are replaced with the actual calculated numbers.
# You have x days, y weeks and z months

# ================= Don't change ========================

age = input("What is your current age? ")

# ================= Don't change ========================

# Hint 1 year = 365 days, 52 weeks, 12 months

max_age = 90
max_months = max_age * 12
max_weeks = max_age * 52
max_days = max_age * 365

users_age = int(age)
users_months = users_age * 12
users_weeks = users_age * 52
users_days = users_age * 365

months_left = max_months - users_months
weeks_left = max_weeks - users_weeks
days_left = max_days - users_days

print(f"You have {days_left} days left , {weeks_left} weeks left , {months_left} months left")


# The video solution in a shorter way

age_as_int = int(age)
years_left = 90 - age_as_int
days_left = years_left * 365
months_left = years_left * 12
weeks_left = years_left * 52

result = f"You have {days_left} days, {weeks_left} weeks, {months_left} months left"

print(result)