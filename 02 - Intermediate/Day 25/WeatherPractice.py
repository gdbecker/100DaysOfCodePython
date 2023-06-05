# Old way of grabbing a data column
import csv
data_file = open("weather_data.csv")
data = csv.reader(data_file)

temps = []
for row in data:
    if row[1] != "temp":
        temps.append(int(row[1]))

# Using the Pandas library
import pandas
data = pandas.read_csv("weather_data.csv")
temps = data["temp"].tolist()

print(data[data.temp == data.temp.max()])
