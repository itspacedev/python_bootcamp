print('''
                         __,,,,_
          _ __..-;''`--/'/ /.',-`-.
      (`/' ` |  \ \ \\ / / / / .-'/`,_
     /'`\ \   |  \ | \| // // / -.,/_,'-,
    /<7' ;  \ \  | ; ||/ /| | \/    |`-/,/-.,_,/')
   /  _.-, `,-\,__|  _-| / \ \/|_/  |    '-/.;.\'
   `-`  f/ ;      / __/ \__ `/ |__/ |
        `-'      |  -| =|\_  \  |-' |
              __/   /_..-' `  ),'  //
          fL ((__.-'((___..-'' \__.'
''')
print("Welcome to Treasure Island!")
print("Your mission is to find the treasure!")

print("\nYou are at a cross road. Where do you want to go?")
left_or_right = input("    Type \"left\" or \"right\"\n").lower()
if left_or_right == "left":

    wait_or_swim = input('You\'ve come to a lake. There is an island in the middle of the lake.\n'
                         '    Type "wait" to wait for a boat. Type "swim" to swim across.\n').lower()

    if wait_or_swim == "wait":
        print("You have come to a castle with three doors - red, blue, and yellow.")
        door = input("    Which door you want to go? Type \"red\", \"blue\", or \"yellow\"\n").lower()
        if door == "yellow":
            print("Congratulations! You win the game!")
        elif door == "red":
            print("You entered the room with a dragon inside. Game over.")
        elif door == "blue":
            print("You entered a room with a beast. Game over.")
        else:
            print("Game over.")
    else:
        print("You attacked by a tiger. Game over.")
else:
    print("You fell into a hole. Game over.")