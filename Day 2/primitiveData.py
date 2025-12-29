# pulling out individual characters in a string = called subscripting

print("Hello"[4])

print("123" + "345") # concatenating the strings


# using actual numbers in calculations
# Integers
print(123 +345)
# Using (_) for separating large integers
x = 123_456_789

# Float
y = 3.1416

# Boolean

True
False

# type error
num_char = len(input("What is your name?"))
# print("your name has " + num_char + " characters")

# using type() returns the type
print(type(num_char))


# type conversion or type casting

new_num_char = str(num_char)
print("your name has " + new_num_char + " characters")

a = 123

b = str(a)
print(type(b))

print(70 + float("100.5")) # 170.5

print(str(70) + str(100))  # 70100