# this file combines functions in previous files in this folder to simplify code 

from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
continue_cipher = True

def caesar(start_text, shift_amount, cipher_direction):
    #encode
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        if char not in alphabet:
            end_text += char
    print(f"The {cipher_direction}d text is {end_text}")

print(logo)

while continue_cipher == True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if shift > len(alphabet):
        shift %=26
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
    restart_cipher = input("Would you like to restart? Y/N:\n ").lower()
    if restart_cipher == 'y':
        continue_cipher == True
    else: 
        print("Goodbye!")
        continue_cipher == False