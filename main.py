# Python Developer: Jessica Amos
# Insistution: Southern New Hampshire University
# Challenges written by Dr. Angela on Udemy. 
# 100 days of code: The Complete Python Bootcamp for 2022

###TODO:
    # left off editing menu functionality
    # menu was directing to options with out selection and not directing back to the menu
    # add menus to all other fucntions else statments as needed
    # conditional statement for random name generator
    # conditional statement for treasure map

import true_love_cal
import treasure_map
import pizza_delivery
import ticket_booth
import leap_year
import rock_paper_scissor

# print("Welcome to Jessica's Simple Python Programs")

def menu():
    print('''Welcome to Jessica's Simple Python Programs\n
    -------------------------- 
     1. Love Calulator\n     
     2. Random Numbers\n   
     3. Ticket Booth\n  
     4. Coin Toss\n
     5. Pizza Delivery\n
     6. Leap Year Calculator\n
    --------------------------\n''')
    selection = input("Choose a menu option by entering the corresponding number: ")
# while True:
#     options = menu.keys()
#     options.sort()
#     for entry in options:
#         print(entry, menu[entry])
    # selection = input("Please select a number: ")
    if selection == '1':
        true_love_cal()
    elif selection == '2':
        treasure_map()
    elif selection == '3':
        ticket_booth()
    elif selection == '5':
        pizza_delivery()
    elif selection == '6':
        leap_year()
    #elif selection == '7:
        #you_pay()
    #elif selection == '8:
        #treasure_map()
    else:
        print("Sorry, that's not a valid entry.")

print(menu())
