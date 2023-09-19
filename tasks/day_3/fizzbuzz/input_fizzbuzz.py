# Input fizzbuzz

num = int(input("Please enter a number "))

if num % 3 == 0 and num % 5 == 0:
    print("FizzBuzz!")
elif num % 3 == 0:
    print("Fizz")
elif num % 5 == 0:
    print("Buzz")
else:
    print("Number was not a multiple of 3 or 5")