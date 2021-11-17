# this file uses a split sting to seperate input
# then len() is used to determine how many entries are given
# and finally I imported the random module to enable random()

# TODO: 
    # create function to call 
    # add conditional statement to return into function or back to menu

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

import random 

num_names = len(names) #finds number of indexices
first = 0
loser = random.randrange(first, num_names - 1)

#convert loser from number to name
print(f"Looks like {names[loser]} is paying!")