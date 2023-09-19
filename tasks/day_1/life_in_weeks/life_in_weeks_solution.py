# Get the user's age in years
age = input("What is your current age? ")


# Calculate how many days, months and years they have left assuming a certain lifespan

age_as_int = int(age)

years_remaining = 90 - age_as_int
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12

# Print the values back to the user
message = f"Assuming you will live until 90, you have {days_remaining} days, {weeks_remaining}  weeks, and {months_remaining} months left."
print(message)