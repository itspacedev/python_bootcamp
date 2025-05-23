import string
import random

letters = list(string.ascii_letters)
numbers = list(string.digits)
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

print("Welcome to the Password Generator!")
n_letters = int(input("How many letters would you like in your password?\n"))
n_numbers = int(input("How many numbers would you like in your password?\n"))
n_symbols = int(input("How many symbols would you like in your password?\n"))

total_length = n_letters + n_numbers + n_symbols
password_characters = []

for index in range(0, total_length):
    options = []
    if n_letters > 0:
        options.append(0)
    if n_numbers > 0:
        options.append(1)
    if n_symbols > 0:
        options.append(2)

    random_type = random.choice(options)

    if random_type == 0:
        password_characters.append(random.choice(letters))
        n_letters -= 1
    if random_type == 1:
        password_characters.append(random.choice(numbers))
        n_numbers -= 1
    if random_type == 2:
        password_characters.append(random.choice(symbols))
        n_symbols -= 1

password = ''.join(password_characters)

random.shuffle(password_characters)
password_shuffled = ''.join(password_characters)

print(f"Your new password is: {password}")
print(f"Your new shuffled password is: {password_shuffled}")
