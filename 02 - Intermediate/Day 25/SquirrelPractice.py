# Goal: make a csv file with counts for each squirrel color

import pandas
data = pandas.read_csv("squirrel_data.csv")
data_colors = data["Primary Fur Color"].tolist()

count_black = len(data[data["Primary Fur Color"] == "Black"])
count_red = len(data[data["Primary Fur Color"] == "Cinnamon"])
count_gray = len(data[data["Primary Fur Color"] == "Gray"])

color_dict = {
    "Fur Color": ["Black", "Red", "Gray"],
    "Count": [count_black, count_red, count_gray]
}

print(color_dict)

df = pandas.DataFrame(color_dict)
df.to_csv("squirrel_count_data.csv")