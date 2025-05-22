import random

random_integer = random.randint(0, 1)
print(f"Random integer number is: {random_integer}")

if random_integer == 0:
    print("Heads")
else:
    print("Tails")