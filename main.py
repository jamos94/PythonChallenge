# Python Developer: Jessica Amos
# Insistution: Southern New Hampshire University
# Challenges written by Dr. Angela on Udemy. 
# 100 days of code: The Complete Python Bootcamp for 2022

###TODO:
    # left off editing menu functionality
    # menu was directing to options with out selection and not directing back to the menu
    # add menus to all other fucntions else statments as needed

import true_love_cal
import random_number_calc
import pizza_delivery
import ticket_booth
import leap_year

print("Welcome to Jessica's Simple Python Programs")
def menu():
    select = input("Choose a menu option by entering the corresponding number: ")
    print("1. Love Calulator") 
    print("2. Random Numbers")
    print("3. Ticket Booth")
    print("4. Coin Toss")
    print("5. Pizza Delivery")
    print("Leap Year Calculator")


while True:
    options = menu.keys()
    options.sort()
    for entry in options:
        print(entry, menu[entry])
    selection = input("Please select a number: ")
    if selection == '1':
        true_love_cal()
    elif selection == '2':
        random_number_calc()
    elif selection == '3':
        ticket_booth()
    elif selection == '5':
        pizza_delivery()
    elif selection == '6':
        leap_year()
    else:
        print("Sorry, that's not a valid entry.")

menu()
