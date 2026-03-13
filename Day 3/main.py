# Control FLow with if-else and Conditional Operators

# print("Welcome to the rollercoaster!")

# height = int(input("What is your height in cm? "))

# if height >= 120:
#     print("You can ride the rollercoaster!")
# else:
#     print("Sorry you have to grow taller before you can ride.")


# Modulo operator

# print(10 % 3)

# num = 10
# print(f"The number {num} is {"even" if num % 2 == 0 else "odd"}.")


# print("Welcome to the rollercoaster!")

# height = int(input("What is your height in cm? "))

# if height >= 120:
#     print("You can ride the rollercoaster!")
#     age = int(input("What is your age? "))
#     if age < 12:
#         print("Child tickets cost 5")
#         price = 5
#     elif age <= 18:
#         print("Youth tickets cost 6")
#         price = 6
#     else:
#         print("Adult tickets cost 12")
#         price = 12

#     is_photo = input("Do you want photos? [Y/N] ").strip().upper()
#     if is_photo == "Y":
#         price += 3

#     print(f"The final bill is {price}")

# else:
#     print("Sorry you have to grow taller before you can ride.")


# ----- Pizza Exercise -----
"""
print("Welcome to Pizza Deliveries!")

size = input("What is the size of the pizza you want? [S/M/L]: ").strip().upper()

price = 0

if size == "S":
    price += 15
elif size == "M":
    price += 20
elif size == "L":
    price += 25
else:
    print("Invalid pizza type selected! Please try again...")
    exit(0)

pepperoni = input("Do you want pepperoni on your pizza? [Y/N]: ").strip().upper()

if pepperoni == "Y":
    if size == "S":
        price += 2
    else:
        price += 3

extra_cheese = input("Do you want extra cheese? [Y/N]: ").strip().upper()

if extra_cheese == "Y":
    price += 1

print(f"Final Cost: {price}")
"""


# Logical Operators

print("Welcome to the rollercoaster!")

height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        print("Child tickets cost 5")
        price = 5
    elif age <= 18:
        print("Youth tickets cost 6")
        price = 6
    elif 45 <= age <= 55:  # age >= 45 and age <= 55:
        print("Enjoy the ride free of cost due to midlife crisis!")
        price = 0
    else:
        print("Adult tickets cost 12")
        price = 12

    is_photo = input("Do you want photos? [Y/N] ").strip().upper()
    if is_photo == "Y":
        price += 3

    print(f"The final bill is {price}")

else:
    print("Sorry you have to grow taller before you can ride.")
