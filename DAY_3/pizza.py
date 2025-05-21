print("Welcome to the Python Pizza Deliveries!")
size = input("What size pizza do you want? S-small, M-medium, L-large\n")
pepperoni = input("Do you want pepperoni on your pizza? Y-yes, N-no\n")
extra_cheese = input("Do you want extra cheese? Y-yes, N-no\n")

bill = 0

# todo: work out how much they need to pay based on their size choice.
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    print("You entered a wrong pizza size.")

# todo: work out how much to add to their bill based on their pepperoni choice.
if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

# todo: work out their final amount based on whether if they want extra cheese.
if extra_cheese == "Y":
    bill += 1

print(f"Your final bill for a pizza is ${bill}")
