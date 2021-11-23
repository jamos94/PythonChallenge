
import main
print("Welcome to the leap year calculator!")


def leapyear():
    year = input("What year would you like to check? ")
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("It's a leap year!")
            else:
                print("It's not a leap year.")
    else:
        print("It's not a leap year.")

play = input("Would you like to pick a year? Y/N: ")
if play == "y":
    leapyear()
else:
    main()