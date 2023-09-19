# What are operators?

# Symbols that execute a particular mathematical or logical function.

# Arithmetic operators:
# +, -, *, /, %

# Logical (Comparison) operators:
# >, <, ==, !=, >=, <=

# Numeric types

# int, float, complex

a = 24
b = 16.5

# print(a > b)

one_third = 1 / 3
# print(one_third)
# print(type(one_third * 3))

# Strings
single_quotes = 'Look! Single quotes'
double_quotes = "Look! 'Double quotes'"

print(double_quotes)

# string slicing

# H e l l o   W o r l d !
# 0 1 2 3 4 5 6 7 8 9 10 11

hw = "Hello World!"

# print(hw[6:])
# print(hw[:5])
# print(hw[0])

# String methods

strip_string = "Hi my name is Luke                    "
# print(len(strip_string))
# print((strip_string.strip()))

example_text = "here's some text with lot's of text"

# print(example_text.count("e")) # count sets of characters in string
# print(example_text.lower()) # Turns characters into lowercase
# print(example_text.capitalize())
# print(example_text.replace("with", ","))

# Casting

a = 2
b = 5.4
c = "3"

print(a + b + int(c))

# Concatenation

d = " theres now a number 25.4 unless we put a space in"

print(str(a) + ", " +  str(b) + d)

# f-strings

name = "Lassie"
years = 7
height_cm = 60.2

print(f"{name} is {years} years old and {height_cm}cm tall")

snoop = "Snoopy"
snoop_years = 52

print(f"{name.upper()} IS {snoop_years * 7} YEARS OLD IN DOG YEARS!")

# Rounding

pi = 3.14159265359

print(f"Pi to 3 decimal places: {pi:.3f}") # 3.142
print(f"Pi to 5 decimal places: {pi:.5f}") # 3.142

# Percentages

score = 16
max_score = 26


print(f"You scored {score/max_score}")
print(f"You scored {score/max_score:%}")
print(f"You scored {score/max_score:.2%}")
print(f"You scored {score/max_score:.0%}")


