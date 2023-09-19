# If the bill was $150.00, split between 5 people, with 12% tip.

# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60

# Tip: There are 2 ways to round a number. Work this out yourself, google is your friend!

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill in £? "))
tip = bill * 0.12
full_bill = int(bill + tip)
print(f"Your total bill is {full_bill}")

split_num = float(input("How many people would you like to split it with? "))
split_bill = full_bill / split_num
print(f"Each of you will pay £{split_bill:.2f}, thank you and come again!")

