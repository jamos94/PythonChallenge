from art import logo
from random import choices, choice
print(logo)
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = choice(cards)
    return card
blackjack = 21

# deal out 2 starting cards for player and dealer
player_hand = [11]
dealer_hand = []
#player_hand.append(deal_card())
player_hand.append(deal_card())

dealer_hand.append(deal_card())
dealer_hand.append(deal_card())

print(f"You were delt {player_hand}.")
print(f"The dealer was delt {dealer_hand}.")

scores = [
    sum(dealer_hand),
    sum(player_hand)
        ] 

print(f"Player score: {scores[1]}\n Dealer score: {scores[0]}")


if scores[0] != 21:
    if scores[1] ==21:
        print("BlackJack, player wins")
    else: #scores[1] > 21:
        for card in player_hand:
            if (11 in player_hand):
                print("you have an ace")
                print(player_hand)
            
else:
    print("BlackJack, dealer wins")
