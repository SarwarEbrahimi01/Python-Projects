# indexed errors occures when you want to access values beyond the list length
# Nested Lists:

#dirty_dozen = ["Strawberries", "Spinach", "Kale","nectarines","Apples","Grapes","Peaches","Cherries","pears","Tomatoes","Celery","Potatoes"]

#fruits = ["Strawberries","nectarines","Apples","Grapes","Peaches","Cherries","pears"]
#vegetables = ["Spinach", "Kale","Tomatoes","Celery","Potatoes"]

#nested_list_dirty_dozen = [fruits,vegetables]

#print(nested_list_dirty_dozen)
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]

print(dirty_dozen[1][1])