import os
from art import logo

# Print auction logo
print(logo)
print("Welcome to the secret auction!")

auction_bids = []

add_another_bid = "yes"
while add_another_bid == "yes":

    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    auction_bids.append({"name": name, "bid": bid})

    add_another_bid = input("Are there any other bidders? Type 'yes' or 'no'.").lower()
    if add_another_bid == "yes":
                os.system("clear")

if len(auction_bids) > 0:
    winner = auction_bids[0]
    for bidder in auction_bids:
        if bidder["bid"] > winner["bid"]:
            winner = bidder

    print(f"The winner is {winner['name']} with a bid of ${winner['bid']}")
else:
    print("There are no bids :(")


