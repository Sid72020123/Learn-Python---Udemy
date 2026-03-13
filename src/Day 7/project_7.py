# --- Project 7 ---

from random import choice
from wordfreq import top_n_list

ascii_art = """
  _                                             
 | |                                            
 | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
 | '_ \\ / _` | '_ \\ / _` | '_ ` _ \\ / _` | '_ \\ 
 | | | | (_| | | | | (_| | | | | | | (_| | | | |
 |_| |_|\\__,_|_| |_|\\__, |_| |_| |_|\\__,_|_| |_|
                     __/ |                      
                    |___/                       
###################################################
"""
print(ascii_art)

word_list = top_n_list("en", 5000)
word_list = [word for word in word_list if len(word) >= 5]

stages = [
    """
  +---+
  |   |
      |
      |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
      |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========""",
]

chosen_word = choice(word_list)
# print(chosen_word)

placeholder = "_" * len(chosen_word)
print(placeholder, f"({len(placeholder)} letters)")

guessed = []
game_over = False
lives = 6

while not game_over:
    display = ""
    print(stages[len(stages) - lives - 1])
    print("#" * 10, f"{lives}/6 LIVES LEFT", "#" * 10)

    guess = (input("Guess a letter: ")).strip()[0].lower()

    if guess in guessed:
        print("\nYou've already guessed:", guess)

    if guess in chosen_word:
        guessed.append(guess)
    else:
        lives -= 1
        print(f"\nYou guessed {guess}, that's not in the word. You lose a life.")

    for letter in chosen_word:
        if letter in guessed:
            display += letter
        else:
            display += "_"
    print(display)

    if display == chosen_word:
        print("#" * 10, "You Won!", "#" * 10)
        game_over = True
    if lives <= 0:
        print("\nYou lost all lives!")
        print("#" * 10, "You Lose!", "#" * 10)
        print("\nThe word was:", chosen_word)
        game_over = True
