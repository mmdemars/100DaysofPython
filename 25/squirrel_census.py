import pandas as pd 

data = pd.read_csv("./2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# for col in data.columns:
#     print(col)

fur = data["Primary Fur Color"].unique()
print(fur)

fur_counts = data["Primary Fur Color"].value_counts()
print(fur_counts)

fur_counts.to_csv("./fur_counts.csv")