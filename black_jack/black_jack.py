from random import choice
from art import logo
print(logo)
keep_playing = True
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

# hit me deals a random card at request of the user or computer
def hit_me():
    hit_me = input("Would you like another card? Enter yes or no").lower()
    if hit_me == "yes":
        player_hand.append(deal_card())
        score(player_hand)
        print(score[1])
    else:
        while score[0] < 21:
            dealer_hand.append(deal_card())
        

# deal out 2 starting cards for player and dealer
player_hand = []
dealer_hand = []
player_hand.append(deal_card())
player_hand.append(deal_card())

dealer_hand.append(deal_card())
dealer_hand.append(deal_card())

# print cards for first round **TODO** set dealer_hand to dealer_hand[0]
# when code compiles correctly
print(f"You were delt {player_hand}.\nThe dealer was delt {dealer_hand}.")

def sum_of(dealer_hand, player_hand, score):
    for i in player_hand:
       score[0] += i
    for i in dealer_hand:
        score[0] += i

score = {
    int(dealer_hand),
    int(player_hand)
}



while score[0] < 21 or score[1] < 21:
    hit_me()
    print(score)


if score[0] > 21 or score[1] > 21:
    checkforAce()
if score[1] == 21:
    print("BlackJack, player wins")
    keep_playing == False
if score[0] == 21:
    print("BlackJack, dealer wins")
    keep_playing == False
if sum.score[0] == 21 and score[1] == 21:
    print("It's a draw")
    keep_playing == False    
print(f"Player score: {score[1]}\n Dealer score: {score[0]}")


