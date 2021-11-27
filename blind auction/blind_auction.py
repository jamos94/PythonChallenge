
from art import logo



print(logo)

# name = input("What's your name?:\n ")
# bid = input("What's your bid?: \n$")
bids = {}
name = ""
bid = 0


def new_bid(name, bid):
    new_bidder = True
    while new_bidder ==True:
        name = input("What's your name?:\n ")
        bid = input("What's your bid?: \n$")
        bids[name] = bid
        new_bidder = input("Is there another bidder?")
        if new_bidder == "y":
            new_bid(name, bid)
        else:
            new_bidder == False
# TODO: create a dictionary 
# name : bid
new_bid(name, bid)

#TODO: made the highest bid?
for bid in bids:
    if bid > bid:
        bid[0] = bid
    print(bid)

print(bids)