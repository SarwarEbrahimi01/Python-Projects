# You are going to write a program that adds to a travel_log.You can
# see a travel_log which is a List that contains 2 Dictionaries.
# Write a function that will work with the following line of code on line 21 to add the entry for Russia to the travel_log.
# add_new_country("Russia",2,["Moscow",Saint Petersburg])
# You've visited Russian 2 times.
# You've been to Moscow and Saint Petersburg.
# DO NOT modify the travel_log directly. You need to create a function that modifies it.
# HINT : 1- look at the function call above to see what the name of the function should be.
# 2- The inputs for the function are positional arguments. The order is very important.
# 3- Feel free to choose your own parameter names.

travel_log = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    {
        "country": "Germany",
        "cities_visited": ["Berline", "Hamburg", "Stuttga"],
        "total_visits": 5
    },
]


# %%%%%%%%%%%% Don't change above %%%%%%%%%%%%%%%

# TODO: Write the function that will allow new country to be added to the travel_log
def add_new_country(country_visited, times_visited, cities_visited):
    new_country = {}
    new_country["country"] = country_visited
    new_country["cities_visited"] = cities_visited
    new_country["total_visits"] = times_visited

    travel_log.append(new_country)


# %%%%%%%%%%% Don't change below %%%%%%%%%%%%%%%%
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
