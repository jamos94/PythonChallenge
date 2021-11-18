# TODO: 
    # create function to call 
    # add conditional statement to return into function or back to menu

import main

row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]

def treasure():
    print(f"{row1}\n{row2}\n{row3}")
    position = input("Where do you want to put the treasure? ")
    # 🚨 Don't change the code above 👆

    #Write your code below this row 👇
    # get coordinates
    x = int(position[0])
    y = int(position[1])

    map[ x - 1] [y - 1] = "X"
    print(f"{row1}\n{row2}\n{row3}")

    restart = input("Would you like to play again? Y/N").casefold()
    if restart == "y":
        treasure()
    else:
        menu()

treasure()
