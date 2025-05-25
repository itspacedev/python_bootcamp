import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''', '''
   +---+
   |   |
   O   |
  /|\  |
  /    |
       |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
      |
      |
      |
      |
=========''']

word_list = ["aardvark", "banana", "apple", "city"]
lives = 6

word = random.choice(word_list)
print(f"Random word is: {word}")

word_length = len(word)
display = []
display_left = word_length
for i in range(0, word_length):
    display.append("_")

game_over = False
while not game_over:
    print(''.join(display))
    letter = input("Guess a letter:").lower()
    for i in range(0, word_length):
        if word[i] == letter:
            display[i] = letter
            display_left -= 1

    if letter not in word:
        lives -= 1
        print("Wrong guess")
        print(stages[lives])

        if lives == 0:
            game_over = True
            print("You lose")

    # print(f"Display left: {display_left}")
    if display_left == 0:
        game_over = True
        print("You win")
