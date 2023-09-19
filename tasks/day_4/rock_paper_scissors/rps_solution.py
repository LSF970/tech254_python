import random

print("Welcome to The Rock, Paper, Scissors game")
plays = ["rock", "paper", "scissors"]
player_play = input("Please choose a play. Enter Rock, Paper or Scissors ")
cpu_play = random.choice(plays)
print(f"You chose {player_play}")
print(f"The CPU chose {cpu_play}")

if player_play.lower() == "rock":
    if cpu_play == "rock":
        print("TIE")
    elif cpu_play == "paper":
        print("CPU WINS")
    else:
        print("PLAYER WINS")

if player_play.lower() == "paper":
    if cpu_play == "paper":
        print("TIE")
    elif cpu_play == "scissors":
        print("CPU WINS")
    else:
        print("PLAYER WINS")

if player_play.lower() == "scissors":
    if cpu_play == "scissors":
        print("TIE")
    elif cpu_play == "rock":
        print("CPU WINS")
    else:
        print("PLAYER WINS")


