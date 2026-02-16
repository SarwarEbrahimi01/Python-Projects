#Review
#Create a function called greet().
#Write three (3) print statements inside the function
#Call your function and run your code

#Simple function
def greet():
    print("Hi there, you have called this function")
    print("Tell me what you are going to do with this function")
    print("Let me know if you are ready")

greet()

#Function that allows for input
def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name} ?")

greet_with_name("Sarwar")

#Function with more than 1 input
def greet_with(name,location):
    print(f"Hello {name}")
    print(f"What is it like in {location}")
greet_with("Wasiq","Bamyan")

#                                      name   location
#Positional Argument ----> greet_with("wasiq","Bamyan")
#                          greet_with("Bamyan","Wasiq")

#                                        name           location
#Keyword Argument -------> greet_with(name="Wasiq",location="Bamyan")
#                          greet_with(location="Bamyan",name="Wasiq")
#                                         location         name

greet_with(location="Kabul",name="Ahmad")
