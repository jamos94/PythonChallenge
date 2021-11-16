

print("Welcome to Python Pizza Deliveries!")


def place_order():
    size = input("What size pizza do you want? S, M, or L ")
    add_pepperoni = input("Do you want pepperoni? Y or N ")
    extra_cheese = input("Do you want extra cheese? Y or N ")

    final_bill = 0

    #small pizza
    if size == "S":
        final_bill+=15
    if add_pepperoni == "Y":
        final_bill +=2

    #medium pizza
    if size == "M":
        final_bill +=20
    if add_pepperoni == "Y":
        final_bill +=3

    #large pizza
    if size == "L":
        final_bill +=25
    if add_pepperoni == "Y":
        final_bill +=3
    if extra_cheese == "Y":
        final_bill += 1
    print(f"Your final bill is: ${final_bill}.")

order = input("Are you ready to order? Y/N: ")
if order == "y":
    place_order()
#else: return to menu