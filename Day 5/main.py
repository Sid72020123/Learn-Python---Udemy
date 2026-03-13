# --- Python Loops ---

# for Loop

fruits = [
    "Mango",
    "Apple",
    "Banana",
    "Pineapple",
    "Strawberry",
    "Cherry",
    "Grapes",
    "Orange",
    "Kiwi",
]

for fruit in fruits:
    print(fruit)
    # print(fruit + " pie")

# --- Coding Challenge ---

# from random import randint

# student_scores = [
#     randint(0, 200) for _ in range(50)
# ]  # Generate 50 random student scores list
# total_exam_score = sum(student_scores)  # Add all list elements
# maximum_score = max(student_scores)  # Maximum number from the list

# print("Total Exam Score:", total_exam_score)
# print("Maximum Score:", maximum_score)

# # total = 0
# # for score in student_scores:
# #     total += score

# # print(total)

# maximum = student_scores[0]

# for score in student_scores:
#     if score > maximum:
#         maximum = score

# print(maximum)


# for loops and range() function

# total = 0

# for number in range(1, 101):
#     total += number

# print(total)
