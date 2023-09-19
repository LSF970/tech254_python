# greet customer
from typing import List

print("Hi samiha, Welcome to the restaurant")

# list of starters
starter_list = ["chicken_wings", "prawns", "Salad"]
print(starter_list)

# taking starter choice
starter_list = input("what starter would you like?")
print("you selected", starter_list)

# list of mains
mains_list = ["Chicken burger", "steak", "pasta"]
print(mains_list)

# taking main choice
main_list = input("what main would you like?")
print("you selected", main_list)

# list of desserts
dessert_list = ["chocolate_cake", "cheese_cake", "ice_cream"]
print(dessert_list)

# tasking dessert choice

dessert_list = input("what dessert would you like?")
print("you selected", dessert_list)

#list of drinks
drinks_list = ["coke", "fanta", "lemonade"]
print(drinks_list)

# taking drinks choice
drinks_list = input("what drink would you like?")
print("you selected", drinks_list)

# summary
print("you selected", starter_list, main_list, dessert_list, drinks_list)