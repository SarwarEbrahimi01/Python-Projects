# write a program that adds the digits in a 2 digit
# number.e.g if the input was 35, them the output should be 3+5 = 8

# ===========Don't Change ==========================
two_digit_number = input("Type a two digit number: ")
#=============Don't Change ==========================
print(type(two_digit_number))

first_digit = two_digit_number[0]
second_digit = two_digit_number[1]

result = int(first_digit) + int(second_digit)
print(result)
# Alternative way
print(int(two_digit_number[0]) + int(two_digit_number[1]))


# change the following code that instead of 7 we get 3
print(3*3+3/3-3)
print(3*(3+3)/3-3)


