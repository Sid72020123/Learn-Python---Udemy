"""
try:

except:

else:

finally:
"""

# Handling Exceptions

"""
try:
    file = open("not_existent_file.txt", "r")
except FileNotFoundError:
    print("File not found!")
else:
    print(
        "Else block runs when all the code in the Try block runs without errors. File was found and the code in the try block was executed successfully..."
    )
finally:
    print("Finally block runs regardless there was an exception or not...")
"""

# Raising Exceptions

# raise KeyError("This is a key error...")

# --- Coding Exercise 20

"""
fruits = ["Apple", "Pear", "Orange"]


# Catch the exception and make sure the code runs without crashing.
def make_pie(index):
    try:
        fruit = fruits[index]
        print(fruit + " pie")
    except IndexError:
        print("Fruit pie")


make_pie(4)
"""

# --- Coding Exercise 21

"""
facebook_posts = [
    {"Likes": 21, "Comments": 2},
    {"Likes": 13, "Comments": 2, "Shares": 1},
    {"Likes": 33, "Comments": 8, "Shares": 3},
    {"Comments": 4, "Shares": 2},
    {"Comments": 1, "Shares": 1},
    {"Likes": 19, "Comments": 3},
]


def count_likes(posts):

    total_likes = 0
    for post in posts:
        try:
            total_likes = total_likes + post["Likes"]
        except KeyError:
            pass

    return total_likes


count_likes(facebook_posts)
"""

# --- Coding Exercise

# NATO Alphabet Project

import pandas as pd

df = pd.read_csv("nato_phonetic_alphabet.csv")

phonetic_alphabets = {value.letter: value.code for (_, value) in df.iterrows()}

while True:
    word = list(input("Enter a word: ").strip().upper())

    try:
        result = [phonetic_alphabets[letter] for letter in word]
    except KeyError:
        print(
            f"Please enter a word which supported characters only!\nSupported characters: {', '.join(phonetic_alphabets.keys())}\n"
        )
        continue

    print("Result:", " ".join(result))
    break
