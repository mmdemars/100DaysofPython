
# with open("./weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)


import csv

# with open("./weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
# print(temperatures)


import pandas as pd

data = pd.read_csv("./weather_data.csv")
# print(data["temp"])

# data_dict = data.to_dict()
# print(data_dict)
# temp_list = data["temp"].to_list()
# print(temp_list)

# hot = data["temp"].max()
# cool = data["temp"].min()

# print(f"the maximum temperature was {hot}")
# print(f"the maximum temperature was {cool}")

# print(data[data.day == "Monday"])
# monday = data[data.day == "Monday"]
# mon_temp = int(monday.temp)
# far = (mon_temp *2)+30
# print(f"The temperature on Monday was {far} degrees Farenheit")

# Create a dataframe from scratch
data_dict = {
    "students": ["Joe", "Marlene", "Angela", "Francine"],
    "scores": [82, 71, 95, 24]
}
data = pd.DataFrame(data_dict)
data.to_csv("./new_data.csv")