from art import logo
import random
import os


def deal_card():
    """
    Return a random card from a deck
    """
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def calculate_score(cards):
    """
    Take a list of cards and returns a score calculated from the cards
    """
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def compare(u_score, c_score):
    """
    Takes the user score and the computer score and determines who wins the game
    """
    if u_score == c_score:
        return "Draw!"
    elif c_score == 0:
        return "Lose, opponent has a BlackJack!"
    elif u_score == 0:
        return "Win with a BlackJack!"
    elif u_score > 21:
        return "You went over. You lose :("
    elif c_score > 21:
        return "Opponent went over. You win :)"
    elif u_score > c_score:
        return "You win"
    else:
        return "You lose o_O"


def play_blackjack_game():
    """
    Enables the user to play BlackJack game
    """
    user_cards = []
    computer_cards = []
    user_score = -1
    computer_score = -1
    is_game_over = False

    for _ in range(0, 2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or user_score > 21 or computer_score == 0:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, and the final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, and the final score: {computer_score}")
    print(compare(user_score, computer_score))


while input("Do you want to play a game of BlackJack? Type 'y' or 'n': ").lower() == "y":
    os.system("clear")
    print(logo)

    play_blackjack_game()
