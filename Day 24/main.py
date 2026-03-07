#%%%%% Reading from a file %%%%%%%%
# You do not need to close the file if you use the "with" and "as" keywords like:
with open("Day 24/my_file.txt") as file:
    contents = file.read()
    print(contents)
# file.close()


#%%%%% Writing to a file %%%%%%
# By default you can write to files because it is read-only(r) so you have to change the mode to writeable(w),
# or if you want to keep to previous text and add the new one use append(a)
# with open("my_file.txt", mode= "a") as file:
#     file.write("\nThis text is written from python")


# if the file doesn't exist it will create it from scratch
# with open("new_file.txt", mode="w") as file:
#     file.write("Hi, this is the new file with some text.")