# You are going to write a program that calculates the average student height from a list of heights.
# e.g. students_heights = [180,124,165,173,189,169,146]
# The average height can calculated by adding all the heights together and dividing by the total number of heights.
# e.g 180+124+165+173+189+169+146 = 1146. There are a total 7 heights in students_heights 1145 / 7 = 163.71428571.
# Average height rounded to the nearest whole number is 164
# Importants: You should not use the sum() or len() functions in your answer.You should try
# to replicate their functionality using what you have learnt about for loops.

#%%%%%%%%%%%%%%%%%%%% Don't Change %%%%%%%%%%%%%%%%%%%%%%%%


students_heights = input("Input a list of students heights ").split()
for n in range(0, len(students_heights)):
    students_heights[n] = int(students_heights[n])
print(students_heights)


#%%%%%%%%%%%%%%%%%%%% Don't Change %%%%%%%%%%%%%%%%%%%%%%%%

total_height = 0
nubmer_of_students = 0
for height in students_heights:
    total_height = total_height + height
    nubmer_of_students += 1

average_height = round(total_height / nubmer_of_students)
print(average_height)



