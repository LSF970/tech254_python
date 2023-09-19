# Get the user's height and weight

height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

# Calculate bmi

bmi = weight / (height * height)

# Control Flow block to send message dependent on BMI
if bmi < 18.5:
    print(f"Your bmi is {bmi:.1f}, you are underweight")
elif bmi <= 25:
    print(f"Your bmi is {bmi:.1f}, you are normal weight")
elif bmi <= 30:
    print(f"Your bmi is {bmi:.1f}, you are slightly overweight")
elif bmi <= 35:
    print(f"Your bmi is {bmi:.1f}, you are obese")
elif bmi > 35:
    print(f"Your bmi is {bmi:.1f}, you are clinically obese")
else:
    print("Those inputs were not valid")