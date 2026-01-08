# Lists = used to store related pieces of data. It is like arrays in Java and C++
provinces_of_afghanistan = ["Kabul","Bamyan","Kandahar","Herat","Mazar-e-Sharif"]

print(provinces_of_afghanistan[1])

# the index starts from zero and continue

# it makes sense when offset term is used

#            0       1      2
fruits = ["Cherry","Apple","Pear"]

# You can also use negative index like [-1] but it starts counting from the end of the list
# You can the change the value of list at specific index
fruits[1] = "Banana"
print(fruits)

# You can items to the list called appending by append() function
fruits.append("Orange")
print(fruits)

# using extend() function to add a bunch of items or list to the list

provinces_of_afghanistan.extend(["Daykoundi","Ghazni","Ghour"])
print(provinces_of_afghanistan)