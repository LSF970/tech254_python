# Get the user's height and weight
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

# Change the variables to floats
a = float(height)
b = float(weight)

# Calculate the bmi
bmi = b / (a * a)
bmi = int(bmi)

# print the BMI to the user
print(f"Your BMI is {bmi}")

# Feel free to add on to this program after you have the base version done.