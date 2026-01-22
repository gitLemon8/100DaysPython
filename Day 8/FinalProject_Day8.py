import art
from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# hello 2 -> jgnnq
def encrypt(original_text, shift_amount):
    cipher_text = "" # j
    for letter in original_text:
        if letter not in alphabet:
            cipher_text += letter
        else:
            shifted_position = alphabet.index(letter) + shift_amount # 7 -> 9
            if shifted_position > len(alphabet):
                shifted_position -= len(alphabet)
            cipher_text += alphabet[shifted_position] # h -> j
    print(f"Here is the encoded result: {cipher_text}")

def decrypt(original_text, shift_amount):
    cipher_text = ""
    for letter in original_text:
        if letter not in alphabet:
            cipher_text += letter
        else:
            shifted_position = alphabet.index(letter) - shift_amount # 7 -> 5
            if shifted_position > len(alphabet):
                shifted_position -= len(alphabet)
            cipher_text -= alphabet[shifted_position]
    print(f"Here is the decoded result: {cipher_text}")

def caesar(user_direction, original_text, shift_amount):
    if direction == "encode":
        encrypt(original_text = text, shift_amount = shift)
    elif direction == "decode":
        decrypt(original_text = text, shift_amount = shift)
    else:
        print("Please input valid command")


go_again = True

while go_again:
    print(logo)
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n ").lower()
    text = input("Type your message:\n ").lower()
    shift = int(input("Type the shift number:\n "))

    caesar(user_direction=direction, original_text=text, shift_amount=shift)

    choice = input("Type 'yes' if you want to go again. Otherwise, type 'no':\n ").lower()
    if choice == "no":
        go_again = not go_again
        print("Goodbye!")
    elif choice == "yes":
        go_again = True