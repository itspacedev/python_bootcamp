import random
import os
from art import logo, versus_symbol
from game_data import data


def get_random_data_item():
    """
    Returns a random item from the game data
    """
    return random.choice(data)


def format_data_item(item):
    """
    Formats the data item into a readable string for printing
    """
    return f"{item['name']}, a {item['description']}, from {item['country']}"


def print_data_items_to_compare(item_a, item_b):
    """
    Prints the data items that user needs to compare
    """
    print(f"Compare A: {format_data_item(item_a)}")
    print(versus_symbol)
    print(f"Compare B: {format_data_item(item_b)}")


def guess_is_correct(item_a, item_b, user_guess):
    """
    Checks if the user's guess is correct regarding the highest number of followers among two persons/brands
    """
    if user_guess == "a" and item_a["follower_count"] > item_b["follower_count"]:
        return True
    elif user_guess == "b" and item_a["follower_count"] < item_b["follower_count"]:
        return True
    return False


print(logo)

score = 0
is_game_over = False
while not is_game_over:
    person_a = get_random_data_item()
    person_b = get_random_data_item()

    print_data_items_to_compare(person_a, person_b)

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    os.system("clear")
    print(logo)
    if guess_is_correct(person_a, person_b, guess):
        score += 1
        print(f"You're right! Current score is {score}")
    else:
        is_game_over = True
        print(f"Sorry, that's wrong. Final score: {score}")





