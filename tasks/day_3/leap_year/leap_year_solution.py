# Ask the user for the year they want to check

year = int(input("Which year do you want to check? "))

# leap year =
# / 4 and no reminder
# except every year that is divisble by 100
# unless the year is also evenly divisble by 400

# 2000 / 4 = 500 (leap)
# 2000 / 100 = 20 (not leap)
# 2000 / 40 = 5 (leap)

# Control flow to work out if leap year or not. Will need to be nested. Use Modulo.

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year")
        else:
            ("Not a leap year")
    else:
        print("Leap year")
else:
    print("Not a leap year")