# --- Project 9 ---

import os


def clear_screen():
    os.system("clear")


logo = '''
  _______ _             _____ _ _            _                        _   _             
 |__   __| |           / ____(_) |          | |       /\             | | (_)            
    | |  | |__   ___  | (___  _| | ___ _ __ | |_     /  \  _   _  ___| |_ _  ___  _ __  
    | |  | '_ \ / _ \  \___ \| | |/ _ \ '_ \| __|   / /\ \| | | |/ __| __| |/ _ \| '_ \ 
    | |  | | | |  __/  ____) | | |  __/ | | | |_   / ____ \ |_| | (__| |_| | (_) | | | |
    |_|  |_| |_|\___| |_____/|_|_|\___|_| |_|\__| /_/    \_\__,_|\___|\__|_|\___/|_| |_|                                                                                        
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

bidders = {}
stop = False

while not stop:
    clear_screen()
    print(logo)
    print("Welcome to silent bidder program.")
    name = input("Enter your name: ")
    amount = float(input("Enter your bid amount: "))

    bidders[name] = amount

    confirm = input("Are there any other bidders? [yes / no]: ").strip().lower()
    if confirm == "no":
        stop = True

winner = ""
largest = 0

for name, amount in bidders.items():
    if amount > largest:
        winner = name
        largest = amount

print(f"The winner of this auction is {winner} with a bid of {largest}!")
