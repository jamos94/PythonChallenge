from art import logo
from random import choices, choice
print(logo)
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
blackjack = 21
# deal out 2 starting cards for player and dealer
player_starting = choices(cards, k = 2)
dealer_starting = choices(cards, k = 2)

print(f"You were delt {player_starting}.")
print(f"The dealer was delt {dealer_starting}.")

# add their cards to determine their score
player_score = player_starting[0] + player_starting[1]
dealer_score = dealer_starting[0] + dealer_starting[1]

scores = {dealer_score, player_score}
print(scores)
#if score == blackjack (11 + 10)
for score in scores:
    if score == blackjack:
        print(f"Black jack!")
    if score != blackjack:
        hit = print(input("Would you like another card? Y/N").lower())
        if hit == 'y':
            scores[0] += choice(cards)
            print(scores[0])
        if hit == 'n':
            print("huh?")
# if player has blackjack

# if score > blackjack
    # if card == 11
        # card = 1
        # if score > 21
            # you lose
        # if score < blackjack
            # hit_me = True
    # else: 
        # you lose


# while hit_me = True
    # deal = print(input("Would you like to draw another card? Y/N: ")).lower()
    # if deal == "y"
        # deal another card and find new score
    # deal == "n"
        # deal computer while score is < 17
        # if computer score > blackjack
            # you win
            # hit_me = False
        #hit_me = False

# if user score is > computer score
    # you win
# elif userscore = computerscore
    # draw
#else: 
    # you lose