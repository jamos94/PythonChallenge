# TODO: 
    # create function to call 
    # add conditional statement to return into function or back to menu
import random
from art import image_choice

#Write your code below this line 👇


player_choice = int(input("What do you chose? Type 0 for Rock, 1 for Paper or 2 for scissors.\n"))

print(image_choice[player_choice])
if player_choice > 2:
  print(f"Wrong input selection, you chose {player_choice}. Type 0 for Rock, 1 for Paper or 2 for scissors. ")

print("Computer chose: \n")

computer_choice = random.choice(image_choice)
print(computer_choice)

if computer_choice == player_choice:
  print("It's a draw")
if computer_choice == 0 and player_choice == 1:
  print("You win")
if computer_choice == 1 and player_choice == 0:
  print("You lose")
if computer_choice == 2 and player_choice == 0:
  print("You win")
if computer_choice == 1 and player_choice == 2:
  print("You win")
if computer_choice == 2 and player_choice == 1:
  print("You loose")
if computer_choice == 0 and player_choice == 2:
  print("You loose")