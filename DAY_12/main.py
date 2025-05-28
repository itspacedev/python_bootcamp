enemies = 1


def increase_enemies():
    enemies = 2
    print(f"Enemies inside the function: {enemies}")


increase_enemies()
print(f"Enemies outside the function: {enemies}")


# Local scope
def drink_potion():
    potion_strength = 2
    print(potion_strength)


drink_potion()
# -> NameError: name 'potion_strength' is not defined
# -> because it was defined in the local scope within the function
# print(potion_strength)


# Global scope
player_health = 10


def check_player_health():
    print(f"Player health inside the function: {player_health}")


check_player_health()
print(f"Player health outside the function: {player_health}")

# There is no Block scope in Python
game_level = 3
game_enemies = ["Zombie", "Skeleton", "Alien"]

if game_level < 5:
    new_enemy = game_enemies[0]

print(f"New enemy is: {new_enemy}")

# Modifying variables in the Global Scope
players = 1


def increase_players():
    # Explicitly specifying that we want to modify the global variable 'players'
    global players
    players += 2

    print(f"Players inside the function: {players}")


increase_players()
print(f"Players outside the function: {players}")

# Global constants
PI = 3.14159  # Should be upper case

