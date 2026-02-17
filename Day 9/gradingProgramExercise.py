# You have access to a database of student_scores in the format of a dictionary.The keys in student_scores are the names of the students and the values are their exam scores.
# Write a program that converts their scores to grades. By the end of your program, you should have a new dictionary called student_grades that should contain studnet names for keys and their grades for values. The final version of the student_grades dictionary will be checked.
# Do not modify the lines 18-24 to change the existing student_scores dictionary.
# Do not write any print statements.
# This is the scoring criteria:
# Scores 91-100: Grade="Outstanding"
# Scores 81-90: Grade="Exceeds Expectations"
# Scores 71-80: Grade="Acceptable"
# Scores 70 or lower: Grade="Fail "

# HINT:
# 1-Remember that looping through a Dictionary will only give you the keys and not the values
# 2- If in doubt as to why you code is not doing what you expected,you can always print out the intermediate values.
# 3- At the end your program, the print statement will show the final student_scores dictionary, do not change this.


# %%%%%%%%%%%%% Don't change %%%%%%%%%%%%%%%%%%%%%
student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
# %%%%%%%%%%%%% Don't change %%%%%%%%%%%%%%%%%%%%%


# TODO-1: Create an empty dictionary called student_grades.
student_grades = {}
# TODO-2: Write your code below to add the grades to student_grades.
for key in student_scores:
    score = student_scores[key]
    if score >= 91 and score <= 100:  # if score > 90
        student_grades[key] = "Outstanding"
    elif score >= 81 and score <= 90:  # if score > 80
        student_grades[key] = "Exceeds Expectations"
    elif score >= 71 and score <= 80:  # if score > 70
        student_grades[key] = "Acceptable"
    else:
        student_grades[key] = "Fail"

print(student_scores)
# Don't change the code below
print(student_grades)
