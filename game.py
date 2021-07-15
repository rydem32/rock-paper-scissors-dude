# game.py

import random
import os
from dotenv import load_dotenv

load_dotenv() #> loads contents of the .env file into the script's environment

z = os.getenv("USER_NAME")



#exit()

print("----------------")
print("Welcome", z) # reads the variable from the environment
print("----------------")

print("Rock, Paper, Scissors, Shoot!")


# ask for user input
x = input("Please choose 'rock', 'paper', or 'scissors':")
print(x)

# validate user input
if (x == "rock") or (x == "paper") or (x == "scissors"):
    print("VALID")
else:
    print("OOPS, INVALID, PLEASE TRY AGAIN!")
    exit()

#print("LATER MESSAGES")

print("USER CHOSE: ", x)

# GENERATE A COMPUTER CHOICE
# https://docs.python.org/3/library/random.html
# source: https://stackoverflow.com/questions/306400/how-to-randomly-select-an-item-from-a-list
#
# import random
#
# foo = ['a', 'b', 'c', 'd', 'e']
# print(random.choice(foo))

# more about datatypes lists, and tuples, etc next class
#valid_options = ("rock", "paper", "scissors") # tuple

valid_options = ["rock", "paper", "scissors"]

computer_choice = random.choice(valid_options)


print("COMPUTER CHOICE:", computer_choice)

# DETERMINE THE WINNER
#source: https://realpython.com/python-rock-paper-scissors/#determine-a-winner

if x == computer_choice:
    print(f"Both players selected {x}. It's a tie!")
elif x == "rock":
    if computer_choice == "scissors":
        print("Rock smashes scissors! You win!")
    else:
        print("Paper covers rock! You lose.")
elif x == "paper":
    if computer_choice == "rock":
        print("Paper covers rock! You win!")
    else:
        print("Scissors cuts paper! You lose.")
elif x == "scissors":
    if computer_choice == "paper":
        print("Scissors cuts paper! You win!")
    else:
        print("Rock smashes scissors! You lose.")

print("----------------")
print("Please Play Again")
print("----------------")