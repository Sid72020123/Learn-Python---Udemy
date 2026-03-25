# with open("weather_data.csv", "r") as file:
#     print(file.readlines())

# import csv

# with open("weather_data.csv", "r") as data_file:
#     data = csv.reader(data_file)
#     print(data)

#     temperatures = []
#     for index, row in enumerate(data):
#         print(row)
#         if index > 0:
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas as pd

data = pd.read_csv("weather_data.csv")

print(data)
print(data["temp"])

print(data.to_dict())
