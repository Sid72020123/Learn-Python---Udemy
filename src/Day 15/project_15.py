# --- Project 15 ---

# Coffee Machine Program

from os import system

LOGO = """
     )))     _____ _           ___      __  __           __  __         _    _          _  
    (((     |_   _| |_  ___   / __|___ / _|/ _|___ ___  |  \\/  |__ _ __| |_ (_)_ _  ___| |
  +-----+     | | | ' \\/ -_) | (__/ _ \\  _|  _/ -_) -_) | |\\/| / _` / _| ' \\| | ' \\/ -_)_|
  |     |]    |_| |_||_\\___|  \\___\\___/_| |_| \\___\\___| |_|  |_\\__,_\\__|_||_|_|_||_\\___(_)
  `-----'                                                                                 
  ##########################################################################################
"""


MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    },
}


resources = {
    "water": {
        "quantity": 300,
        "unit": "mL",
    },
    "milk": {
        "quantity": 200,
        "unit": "mL",
    },
    "coffee": {
        "quantity": 100,
        "unit": "g",
    },
    "money": {
        "quantity": 0,
        "unit": "dollars",
    },
}


def display_menu():
    print(f"{' Menu '.title():=^40}")
    max_length = max(len(name) for name in MENU) + 2
    print(f"{'Item':^{max_length}}     {'Cost':^{max_length}}")
    print(f"{"-"*max_length}     {"-"*max_length}")
    for resource, data in MENU.items():
        print(f"{resource.title():<{max_length}} ==> $ {data['cost']}")
    print()


def display_report():
    print(f"\n{' Available Resources ':=^50}\n")
    max_length = max(len(name) for name in resources) + 2
    print(f"{'Resource':<{max_length}}     {'Quantity'}")
    print(f"{"-"*max_length}     {"-"*max_length}")
    for resource, data in resources.items():
        print(f"{resource:<{max_length}} ==> {data['quantity']} {data['unit']}")


def check_resources(coffee_type):
    coffee_ingredients = MENU[coffee_type]["ingredients"]
    for ingredient, quantity in coffee_ingredients.items():
        if quantity > resources[ingredient]["quantity"]:
            return [
                False,
                ingredient,
                quantity,
                resources[ingredient]["quantity"],
                resources[ingredient]["unit"],
            ]
    return [True]


def convert_cents_to_dollars(quarters, dimes, nickles, pennies):
    return quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01


def make_coffee_cup(coffee_type, money):
    change = 0
    coffee_recipe = MENU[coffee_type]
    coffee_ingredients = coffee_recipe["ingredients"]
    for ingredient, quantity in coffee_ingredients.items():
        resources[ingredient]["quantity"] -= quantity
    resources["money"]["quantity"] += coffee_recipe["cost"]
    change = money - coffee_recipe["cost"]
    return round(change, 2)


while True:
    system("clear")
    print(LOGO)
    display_menu()

    choice = input("What would you like? (espresso/latte/cappuccino): ").strip().lower()

    if choice == "off":
        print("\nCoffee Machine powering off...\nBye!")
        break
    elif choice == "report":
        display_report()
    elif choice in MENU.keys():
        enough_resources = check_resources(choice)
        coffee_recipe = MENU[choice]
        if not enough_resources[0]:
            print(
                f"\nThere is not enough {enough_resources[1]} to make {choice}!\n\tRequired Amount => {enough_resources[2]} {enough_resources[-1]}\n\tAvailable Amount => {enough_resources[3]} {enough_resources[-1]}"
            )
        else:
            quarters = int(input("Enter the no. of quarters: "))
            dimes = int(input("Enter the no. of dimes: "))
            nickles = int(input("Enter the no. of nickles: "))
            pennies = int(input("Enter the no. of pennies: "))

            total_coins = convert_cents_to_dollars(quarters, dimes, nickles, pennies)
            # print(total_coins)
            if total_coins >= coffee_recipe["cost"]:
                change = make_coffee_cup(choice, total_coins)
                print(f"\n ☕ Here is your {choice.title()}. Enjoy!")
                if change:
                    print(f"\n 💵 Here is your change of $ {change}")
            else:
                print(
                    f"\nSorry, that's not enough money to make {choice}! Please try again...\n"
                )
    else:
        print("\nInvalid choice entered! Please try again...\n")
    input("\nPress any key to return to main menu...")
