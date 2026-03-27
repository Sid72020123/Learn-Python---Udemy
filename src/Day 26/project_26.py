# --- Project 26 ---

# NATO Alphabet Project

import pandas as pd

df = pd.read_csv("nato_phonetic_alphabet.csv")

phonetic_alphabets = {value.letter: value.code for (_, value) in df.iterrows()}

word = list(input("Enter a word: ").strip().upper())

result = [phonetic_alphabets[letter] for letter in word]

print("Result:", " ".join(result))
