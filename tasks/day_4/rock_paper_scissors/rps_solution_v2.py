import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
game_images = [rock, paper, scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, type 1 for Paper, Type 3 for Scissors. \n"))
if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number")
# Print the image associated with the user's choice
else:
    print(game_images[user_choice])

    cpu_choice = random.randint(0, 2)
    # Print the image associated with the cpu's choice
    print(f"CPU chose:")
    print(game_images[cpu_choice])

    if user_choice == 0 and cpu_choice == 2:
        print("YOU WIN!")
    elif cpu_choice == 0 and user_choice == 2:
        print("YOU LOST!")
    elif cpu_choice > user_choice:
        print("YOU LOST!")
    elif user_choice > cpu_choice:
        print("YOU WIN")
    elif cpu_choice == user_choice:
        print("IT'S A DRAW")



