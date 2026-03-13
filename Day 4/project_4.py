# --- Project 4 ---

import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

ascii_arts = [rock, paper, scissors]

print("Welcome to Rock, Paper & Scissors Game!\n")
# print(rock, paper, scissors)

choice = int(input("Type 0 for Rock, 1 for Paper & 2 for Scissor.\nEnter here: "))

computer_choice = random.randint(0, 2)

# 0 -> Rock
# 1 -> Paper
# 2 -> Scissor

print("You choose:")
print(ascii_arts[choice])
print("-" * 50)
print("\nComputer chose:")
print(ascii_arts[computer_choice])
print("-" * 50)

result = "tie"

if choice == 0:
    if computer_choice == 1:
        result = "lose"
    elif computer_choice == 2:
        result = "win"
elif choice == 1:
    if computer_choice == 0:
        result = "win"
    elif computer_choice == 2:
        result = "lose"
elif choice == 2:
    if computer_choice == 0:
        result = "lose"
    elif computer_choice == 1:
        result = "win"

print(f"\n\nMatch result: {result.title()}!")
