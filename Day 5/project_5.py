# --- Project 5 ---

from string import ascii_letters, digits, punctuation
from random import choice

letters = list(ascii_letters)
numbers = list(digits)
symbols = list(punctuation)
characters = []

print("Welcome to Random Password Generator!")

num_letters = int(input("How many letters would you like in your password? "))
num_numbers = int(input("How many numbers would you like? "))
num_symbols = int(input("How many symbols would you like? "))

if num_letters + num_numbers + num_symbols == 0:
    print("Not enough characters to generate random password! Please try again...")
    exit(0)

password = ""

# # Easy Version

# for _ in range(num_letters):
#     password += choice(letters)

# for _ in range(num_numbers):
#     password += choice(numbers)

# for _ in range(num_symbols):
#     password += choice(symbols)


# Hard Version

if num_letters > 0:
    characters.extend(letters)
if num_numbers > 0:
    characters.extend(numbers)
if num_symbols > 0:
    characters.extend(symbols)

for _ in range(num_letters + num_numbers + num_symbols):
    password += choice(characters)

print("\nYour password is:", password)
