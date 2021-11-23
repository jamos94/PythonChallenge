print("Welcome to the rollercoaster!")

def rollercoaster():
    bill = 0 		#created a variable to hold the bill amount
    height = input("What is your height in cm? ")
    if height > 120:
        print("You can ride!")
    age = int(input("what is your age?"))
    if age < 12:
        bill = 5		#adjust bill amount 
        print("Children's tickets are $5") 		#changed ticket bill to listed amount with given age
    elif age <= 18:
        bill = 7
        print("Young adult tickets are $7")		#changed ticket bill to listed amount with given age
    elif age >= 18:
        bill = 12
        print("Adult tickets are $12")			#changed ticket bill to listed amount with given age
        photos_taken = input("Would you like a photo taken? Enter Y or N")
        if photos_taken == "Y":
            bill += 3
        print(f"Your total bill is {bill}.")
    else:
        print("you cannot ride")

ride = input("Would you like to ride? Y/N: ")
if ride == "y":
    rollercoaster()
#else return to menu