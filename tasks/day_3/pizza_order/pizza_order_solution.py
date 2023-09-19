# Make a program to take an order for Pizza. Ask for size, pepperoni and extra cheese.
# Calculate the bill based on the options chose.

# Ask for inputs regarding options
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

# Set bill
bill = 0

# Calculate bill, use control flow
if size == "S":
    bill += 15
    if add_pepperoni == "Y":
        bill += 2
elif size == "M":
    bill += 20
    if add_pepperoni == "Y":
        bill += 3

elif size == "L":
    bill += 25
    if add_pepperoni == "Y":
        bill += 3
else:
    print("Invalid value")

if extra_cheese == "Y":
    bill += 1

# Print bill

print(f"Your final bill is £{bill}")