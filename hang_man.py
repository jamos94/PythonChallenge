# HANGMAN! 
# this program uses lists, loops, functions, and conditional statements

# COMPUTER CHOOSES RANDOM WORD FROM WORD LIST --> random()
# COMPUTER DISPLAYS NUMBER OF CHARACTERS IN WORD --> len()
# USER GUESSES A LETTER IN THE WORD     --> print(input()), userGuess()
# COMPUTER DETERMINES IF LETTER Is INCLUDED IN WORD --> convert word to list, check list for input letter
# IF LETTER IS IN WORD
    # COMPUTER REVEALS LETTERS IN CHARACTER POSITIONS 
    # user guesses again -- > userGuess()
# ELSE: 
    # USER LOOSES 1 OF 3 STRIKES
    #IF USER LOSS = 3
        #GAME OVER

import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["aardvark", "baboon", "camel"]
chosen_word = ""
empty_letter = "_"
end_game = False
word_length = len(chosen_word)
chosen_word = random.choice(word_list)
lives = 6
# Testing code
print(f'Pssst, the solution is {chosen_word}.')


# For each letter in the chosen_word, add a "_" to 'display'.
# So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.
display = []

for letter in chosen_word:
    display.append("_")  # for each character in the chosen word a "_" is added using append()


# loop continues until all blanks are filled 
while not end_game:
    guess = input("Guess a letter: ").lower()
    # checking is guess in in chosen word
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            letter = display[position]
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_game = True
            print("you lose")


    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    if '_' not in display:
        end_game = True
        print("You won!")
    
    print(stages[lives])
