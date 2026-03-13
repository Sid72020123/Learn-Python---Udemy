# --- Project 12 ---

from random import randint

logo = """
  _____                   ________         _  __           __          
 / ___/_ _____ ___ ___   /_  __/ /  ___   / |/ /_ ____ _  / /  ___ ____
/ (_ / // / -_|_-<(_-<    / / / _ \\/ -_) /    / // /  ' \\/ _ \\/ -_) __/
\\___/\\_,_/\\__/___/___/   /_/ /_//_/\\__/ /_/|_/\\_,_/_/_/_/_.__/\\__/_/   
"""

print(logo)
print("Welcome to the Number Guessing Game!")
print("\nI'm thinking of a number between 1 and 100.")

difficulty = input("\nChoose a difficulty. Type 'easy' or 'hard': ").strip().lower()

chances = 0
random_number = randint(1, 100)
win = False

if difficulty == "easy":
    chances = 10
elif difficulty == "hard":
    chances = 5
else:
    print("Invalid difficulty chosen! Please try again...")
    exit(0)

while chances > 0:
    print(f"You have {chances} attempt(s) remaining to guess the number.")
    user_guess = int(input("Make a guess: "))

    if user_guess > random_number:
        print("Too high.")
    elif user_guess < random_number:
        print("Too low.")
    else:
        print(f"Your got it! The answer was {random_number}.")
        win = True
        break
    print("Guess again.")
    chances -= 1

if not win:
    print(f"You've run out of guesses, you lose. The answer was {random_number}.")
