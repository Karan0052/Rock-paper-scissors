# This project is a simple Python implementation of the classic Rock, Paper, Scissors game. 
# You can play against the computer by choosing between Rock, Scissors, or Paper. 
# The program will determine the winner based on the user's and the computer's choices.

# Features
# Play Rock, Paper, Scissors against the computer.
# Randomized computer moves.
# Clear instructions for user input.
# Displays if you won, lost, or drew the game.
# Handles incorrect inputs and prompts the user to try again.

import random

def check(comp, user):
  if comp ==user:
    return 0
    
  if(comp == 0 and user ==1):
    return -1
    
  if(comp == 1 and user ==2):
    return -1
    
  if(comp == 2 and user == 0):
    return -1

  if(user > 2):
    return 2


  return 1
    
  
comp = random.randint(0, 2)
user = int(input("0 for Rock\n1 for Scissor\n2 for Paper\n\n"))

score = check(comp, user)

print("You: ", user)
print("Computer: ", comp)


if(score == 0):
  print("Its a draw")
elif (score == -1):
  print("You Lose")
elif (score == 2):
  print ("\nWrong Input \nPlease try again")

else:
  print("You Won")
