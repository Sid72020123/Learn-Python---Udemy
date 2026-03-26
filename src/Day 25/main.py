# with open("weather_data.csv", "r") as file:
#     print(file.readlines())

# import csv

# # Challenge:
# with open("weather_data.csv", "r") as data_file:
#     data = csv.reader(data_file)
#     print(data)

#     temperatures = []
#     for index, row in enumerate(data):
#         print(row)
#         if index > 0:
#             temperatures.append(int(row[1]))
#     print(temperatures)

# import pandas as pd

# data = pd.read_csv("weather_data.csv")

# print(data)
# print(data["temp"])

# print(data.to_dict())

# temperatures = data["temp"].to_list()

# # print("Average:", sum(temperatures) / len(temperatures)) # --> Long Method

# print(data["temp"].mean())  # --> Simpler / short method

# print(data["temp"].max())

# print(data[data.day == "Monday"])

# print(data[data.temp == data.temp.max()])

# print(data[data.day == "Monday"].condition)

# print((data[data.day == "Monday"].temp[0] * (9 / 5)) + 32)


# Challenge:

import pandas as pd

data = pd.read_csv("squirrel_data.csv")

# print(data)

gray_squirrels = data[data["Primary Fur Color"] == "Gray"]
cinnamon_squirrels = data[data["Primary Fur Color"] == "Cinnamon"]
black_squirrels = data[data["Primary Fur Color"] == "Black"]

gray_squirrels_count = len(gray_squirrels)
cinnamon_squirrels_count = len(cinnamon_squirrels)
black_squirrels_count = len(black_squirrels)

print(gray_squirrels_count, cinnamon_squirrels_count, black_squirrels_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Red"],
    "Count": [gray_squirrels_count, cinnamon_squirrels_count, black_squirrels_count],
}

df = pd.DataFrame(data_dict)
df.to_csv("squirrels_count.csv")
