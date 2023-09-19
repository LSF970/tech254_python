# Use modulo to check if odd or even

# Ask user for number as input

number = int(input("Which number do you want to check? "))

# Check if odd or even using modulo
odd_or_even = number % 2

# Make decision dependant on whether modulo returned 0 or not
if odd_or_even == 0:
    print("The number is even!")
else:
    print("The number is odd")

# Print goodbye message
print("Thank you for playing. See you.")

# Can you make this program repeat after the user's number is checked?