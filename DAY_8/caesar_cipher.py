import string
from art import logo

# Print Caesar cipher logo
print(logo)

alphabet = list(string.ascii_lowercase)
alphabet_length = len(alphabet)


# Encrypt the message
def encrypt(original_text, shift_number):
    encrypted_message = ""
    for letter in original_text:
        index = (alphabet.index(letter) + shift_number) % alphabet_length
        encrypted_message += alphabet[index]
    print(encrypted_message)


# Decrypt the message
def decrypt(original_text, shift_number):
    decrypted_message = ""
    for letter in original_text:
        index = (alphabet.index(letter) - shift_number) % alphabet_length
        decrypted_message += alphabet[index]
    print(decrypted_message)


# Caesar cipher
def caesar(cipher_direction, original_text, shift_number):
    sign = 1
    if cipher_direction == "decode":
        sign = -1

    result_message = ""
    for letter in original_text:
        if letter in alphabet:
            index = (alphabet.index(letter) + sign * shift_number) % alphabet_length
            result_message += alphabet[index]
        else:
            result_message += letter

    print(f"Here is {cipher_direction}d message: {result_message}")


restart = "yes"
while restart == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(cipher_direction=direction, original_text=text, shift_number=shift)

    restart = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n")



