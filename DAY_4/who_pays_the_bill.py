import random

friends = ["Alice", "Bob", "Charlie", "David", "Megan"]

random_int = random.randint(0, 4)
print(f"Option 1: {friends[random_int]} pays the bill")

random_int2 = random.randint(0, len(friends) - 1)
print(f"Option 2: {friends[random_int2]} pays the bill")

print(f"Option 3: {random.choice(friends)} pays the bill")
