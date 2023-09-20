# Functions

# DRY - Don't Repeat Yourself

# Allow us to embed/reference code, making it reusable.

# Making a function

# def print_something(print_string):
#     print(print_string)
#
# print_something("We can pass anything in here!")
# print_something("Like this")
# print_something("And this")

# def greeting(name):
#     print(f"Hello, my name is {name}")
#
# greeting("Luke")
# greeting("Wafa")
# greeting("Doz")

# The return statement - holds a value

# def addition(int1=2, int2=4):
#     return int1 + int2

# print(addition(5, 5))
# print(addition(10, 15))
# print(addition())

# multiple arguments

def multi_args(*multiargs):
    for arg in multiargs:
        print(arg)
    print(type(multiargs))

multi_args(1, 2, 3, 4, "five")

# Type hints - can research this

# Functions good practices

# Add useful comments to explain your functions!
# Clear function names and argument names
# Keep your functions small and compact. Make them do one thing if possible.
# Avoid duplication
# Correct indentation and formatting/syntax
# Organised properly
# Do not use them when not needed
# Functions at the start of your code if possible
# Remember the return statement!
# Consider using type hints




