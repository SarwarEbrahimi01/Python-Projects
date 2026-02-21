# #%%%%%%%%%%%%%% Scope %%%%%%%%%%%%%%%%%%%

# enemies = 1

# def increase_enemies():
#     enemies = 2
#     print(f"enemies iside function: {enemies}")

# increase_enemies()
# print(f"enemies outside function: {enemies}")

# # Local Scope
# # def drink_potion():
# #     potion_strength = 2
# #     print(potion_strength)

# # drink_potion()

# #Global Scope
# player_health = 10

# def game():
#     def drink_potion():
#         potion_strength = 2
#         print(player_health)

#     drink_potion()


# print(player_health)

# # There is no Block Scope

# game_level = 3
# def create_enemy():
#     enemies = ["Skeleton", "Zombie", "Alien"]
#     if game_level < 5:
#         new_enemy = enemies[0]

#     print(new_enemy)

# Modifying Global Scope

# enemies = 1

# def increase_enemies():
#     # global enemies ---> you can use this but it is not recommended
#     # enemies += 1
#     # instead you can return that because it is a professional way
#     return enemies + 1
#     print(f"enemies iside function: {enemies}")

# enemies = increase_enemies()
# print(f"enemies outside function: {enemies}")

# Global constants
# in python global constants are written all in uppercase
# global constants are used when you don't want to change the value of a variable throughout the program
PI = 3.14159
URL = "https://www.google.com"
TWITTER_HANDLE = "@yu_angela"
