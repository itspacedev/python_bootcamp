import random
import os

print("Welcome to the Number Guessing Game!")

attempts_setting = {
    "easy": 10,
    "hard": 5,
}


def play_number_guessing_game():
    """
    Enables the user to play the game of guessing the number between 1 and 100
    """
    print("I'm thinking of a number between 1 and 100")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

    attempts_left = attempts_setting[difficulty]
    secret_number = random.randint(1, 100)
    win = False

    while not win and attempts_left > 0:
        print(f"You have {attempts_left} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))

        if guess == secret_number:
            win = True
        elif guess > secret_number:
            print("Too high")
            print("Guess again")
        else:
            print("Too low")
            print("Guess again")

        attempts_left -= 1

    if win:
        print(f"You got it! The answer was {secret_number}")
    else:
        print("You've run out of guesses, you lose =(")


restart_game = "y"
while restart_game == "y":
    play_number_guessing_game()
    restart_game = input("Do you want to play one more time? Type 'y' or 'n': ").lower()
    if restart_game == "y":
        os.system("clear")

print("Goodbye =)")
