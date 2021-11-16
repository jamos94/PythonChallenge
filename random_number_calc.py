import random


print("Welcome to the random number program!")
print("Here we will give you a random number. You pick the parameters!")
play = input("Are you ready to fin out if you\'re made for each other? Y/N: ").lower()

def pick_number():
    num1 = input("Enter a first number: ")
    num2 = input("Enter a last number: ")

    random_num = random.randint(num1, num2)

    print(f"Your random number between {num1} and {num2} is {random_num}.")

again = input("Would you like to play again? Y/N: ").lower
if again == "y":
    pick_number()
# else: return to menu
    