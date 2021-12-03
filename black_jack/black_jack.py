from art import logo
from random import choice
print(logo)
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = choice(cards)
    return card

def checkforAce():
    if score[1] > 21:
        for card in player_hand:
            if card == 11:
                score[1]-= 10
                if score[1] > 21:
                    print("You busted. Sorry you lose.")
                if score[1] < 21:
                    return score[1]
    if score[0] > 21:
        for card in dealer_hand:
            if card == 11:
                score[0]-= 10
                if score[0] > 21:
                    print("Dealer busted, you win.")
                if score[0] <21:
                    return score[0]

def hit_me():
    hit_me = input("Would you like another card? Enter yes or no").lower()
    if hit_me == "yes":
        player_hand.append(deal_card())
        print(player_hand)
    else:
        while dealer_hand > 21:
            dealer_hand.append(deal_card())

# deal out 2 starting cards for player and dealer
player_hand = []
dealer_hand = []
player_hand.append(deal_card())
player_hand.append(deal_card())

dealer_hand.append(deal_card())
dealer_hand.append(deal_card())

print(f"You were delt {player_hand}.\nThe dealer was delt {dealer_hand}.")

score = [
    sum(dealer_hand),
    sum(player_hand)
        ] 


if score[1] == 21:
    print("BlackJack, player wins")
if score[0] == 21:
    print("BlackJack, dealer wins")
if score[0] == 21 and score[1] == 21:
    print("It's a draw")

if score[0] > 21 or score[1] > 21:
    checkforAce()
    if keep_playing == True:

print(f"Player score: {score[1]}\n Dealer score: {score[0]}")

