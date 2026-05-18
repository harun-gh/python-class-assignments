import csv
from os import path

file_path = path.join(path.dirname(__file__), "chiba.csv")

with open(file_path, "r", newline="") as file:
    temperatures = csv.reader(file)

    for temperature in temperatures:

        date = temperature[0]
        max_temp = float(temperature[1])
        min_temp = float(temperature[2])
        ave_temp = float(temperature[3])

        print(f"date: {date} type: {type(date)}")
        print(f"max: {max_temp} type: {type(max_temp)}")
        print(f"min: {min_temp} type: {type(min_temp)}")
        print(f"ave: {ave_temp} type: {type(ave_temp)}")