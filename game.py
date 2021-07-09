# game.py

print("Rock, Paper, Scissors, Shoot!")


# ask for user input
x = input("Please choose 'rock', 'paper', or 'scissors'")
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
valid_options = ["rock", "paper", "scissors"] # list

c = random.choice(valid_options)

print("COMPUTER CHOSE:", c)


#generate a computer choice


#determine a winner


