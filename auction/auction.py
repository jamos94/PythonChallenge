from art import logo
print(logo)
print("Welcome to the auction progrom")

another_bidder = True
bids = {}
# create a function to determine the highest bidder
def find_highest_bidder(bid_record):
    """determines the highest bidder"""
    highest_bid = 0
    for bidder in bid_record:
        amount_bid = bid_record[bidder]
        if amount_bid > highest_bid:
            highest_bid = amount_bid
            winner = bidder
    print(f"The winner is {bidder} with a bid of {highest_bid}")

while another_bidder == True:
    # get name
    name = input("What's your name? \n")
    # get input
    bid = int(input("What's your bid?"))
    # another bidder?
    bids[name] = bid
    continue_bidding = input("Is there another bidder? Enter 'yes' or 'no'\n")
    if continue_bidding == 'yes':
        another_bidder = True
    elif continue_bidding == 'no':
        another_bidder = False
        find_highest_bidder(bids)
