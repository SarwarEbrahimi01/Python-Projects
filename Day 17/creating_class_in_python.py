# Creating the class in python
# class Car:
#   body of class

# The naming convention in class is PascalCase like----> StudentName
class User:
    # Creating constructor by using one special function called init()
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        # Adding a default value
        self.followers = 0
        self.following = 0

    # Creating the method inside the class
    def follow(self, user):
        user.followers += 1
        self.following += 1


# Creating the object of the class
user_1 = User("001", "angela")
# Creating / Adding attributes to the object
# Note: Attribute ---> A variable that's associated with an object.
# user_1.id = "001"
# user_1.username = "angela"

user_2 = User("002", "sarwar")

# Calling the method of the object
user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)