# List Comprehension

# # new_list = [new_item for item in list]

numbers = [1, 2, 3]
new_list = [n + 1 for n in numbers]
print(new_list)

new_list = [n * 2 for n in range(1, 5)]
print(new_list)

# Conditional List Comprehension

# # new_list = [new_item for item in list if test]

# Coding Exercise 15
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [n**2 for n in numbers]
print(squared_numbers)

# Coding Exercise 16
list_of_strings = ["9", "0", "32", "8", "2", "8", "64", "29", "42", "99"]
numbers = [int(n) for n in list_of_strings]
result = [n for n in numbers if n % 2 == 0]
print(result)

# Coding Exercise 17
with open("file1.txt", "r") as file:
    file_1_contents = file.readlines()

with open("file2.txt", "r") as file:
    file_2_contents = file.readlines()

numbers_1 = [int(content.strip()) for content in file_1_contents]
numbers_2 = [int(content.strip()) for content in file_2_contents]

result = [n for n in numbers_1 if n in numbers_2]

print(result)

# Dictionary Comprehension
