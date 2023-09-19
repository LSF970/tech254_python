# Import the random module here
import random

# Split string method - research if needed
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")



# print(names)
unlucky_person = random.choice(names)

# print(unlucky_person)
print(f"Sorry {unlucky_person}, you have been chosen to pay everyone's bill!")