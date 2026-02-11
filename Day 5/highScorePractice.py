# You are going to write a program that calculates the highest score from a list of scores. e.g. students_scores = [78,65,89,86,55,91,64,89]
# Important: You are not allowed to use the max or min functions.The output words must match the example.---> The highest score in the calss is: x

# %%%%%%%%%%%%%%%%%%%%%%%% Don't Change the code %%%%%%%%%%%%%%%%%%

student_scores = input("Input a list of students scores ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)
# %%%%%%%%%%%%%%%%%%%%%%%% Don't Change the code %%%%%%%%%%%%%%%%%%

highest_score = 0
for score in student_scores:
    if score > highest_score:
        highest_score = score
print(f"The highest score in the class is : {highest_score}")


