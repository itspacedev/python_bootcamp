import random

print("Welcome to the Rock Paper Scissors Game!")

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

symbols = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, and 2 for Scissors.\n"))
computer_choice = random.randint(0, 2)

print(f"Your choice is:\n{symbols[user_choice]}")
print(f"Computer choice is:\n{symbols[computer_choice]}")

if user_choice == computer_choice:
    print("It is draw")
else:
    if user_choice == 0:
        if computer_choice == 2:
            print("You win")
        else:
            print("You lose")
    elif user_choice == 1:
        if computer_choice == 0:
            print("You win")
        else:
            print("You lose")
    elif user_choice == 2:
        if computer_choice == 1:
            print("You win")
        else:
            print("You lose")
    else:
        print("You entered incorrect value")
