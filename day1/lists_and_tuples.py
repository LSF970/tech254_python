# Collections can store multiple pieces of data inside

# Lists - Called arrays in other languages

shopping_list = ["Salad", "Eggs", "Doughnuts", "Milk", "Salmon"]
# print(shopping_list)
# print(shopping_list)
# print(type(shopping_list))
# print(shopping_list[-1])

shopping_list[2] = "Tomato"
print(shopping_list)

# List methods

# Add something to the end of a list
shopping_list.append("Carrots") # Add to the end
shopping_list.extend(["Water", "Celery"]) # Add multiple
# print(shopping_list)

# Remove items from a list

# shopping_list.remove("Salad") # Gets rid of any instance of "Salad" in list
# print(shopping_list)

# pop method

# shopping_list.pop() # removes the last value of the list, when it has nothing passed to it.
# print(shopping_list)

# shopping_list.pop(1) # Remove a particular index
# carrots = shopping_list.pop(3) # remove an item from the list and store it a variable
# print(carrots)
# print(shopping_list)

# Mixed data type lists

mixture = [1, 2, 3.0, "one", "two", "three", "four"]
print(mixture)

# List slicing

print(mixture[1:3])
print(mixture[::-1])

# Tuples - Immutable, they cannot be changed!

essentials = ("bread", "eggs", "milk")

print(essentials)
print(type(essentials))

essentials[0] = "beans" # Will not work