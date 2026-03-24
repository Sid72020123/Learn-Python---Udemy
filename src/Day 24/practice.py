# Reading and Writing files in Python

# file = open("file.txt", "r")

# print(file.read())

# file.close()


with open("file.txt", "r") as file:
    print(file.read())
