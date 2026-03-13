# ----- Random Module ----
# import random

# random_integer = random.randint(1, 10)
# random_float = random.random()

# random_float = random.uniform(1, 10)

# print(random_float)

# num = random.randint(0, 1)

# if num == 0:
#     print("Heads!")
# else:
#     print("Tails!")


# ----- Python Lists -----

fruits = ["Mango", "Apple", "Banana", "Pineapple", "Pear", "Cherry"]

print(fruits[0], fruits[1])  # Positive Indexing
print(fruits[-1], fruits[-2])  # Negative Indexing

fruits[4] = "Strawberry"  # Changing the value at specific index
print(fruits)

fruits.append("Grapes")  # Append a single element
print(fruits)

fruits.extend(["Orange", "Kiwi"])  # "Extend" a list to another list
print(fruits)

print(len(fruits))
# print(fruits[len(fruits)]) # IndexError

# Nested Lists

vegetables = ["Carrot", "Potato", "Tomato", "Corn", "Spinach"]

food = [fruits, vegetables]

print(food)

# ----- Challenge - 1 -----

# from random import choice

# friends = list("ABCDE")
# print(choice(friends))
