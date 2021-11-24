
from art import logo


def new_bid(name, bid):
    blind_bids[name] = bid

print(logo)

# TODO: create a dictionary 
    # name : bid
another_bid = True
while another_bid == True:
    blind_bids = {}
    name = input("what's your name?")
    bid = input("what's your bid?")
    new_bid(name, bid)
    new_bidder = input("is there another bidder? Y/N: ").lower()
    if new_bidder == "n":
        another_bid = False
#TODO: made the highest bid?
print(blind_bids)