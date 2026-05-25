import csv
import json
from os import path

csv_path = path.join(path.dirname(__file__), "../lesson05/chiba.csv")
json_path = path.join(path.dirname(__file__), "chiba.json")

database = {}

with open(csv_path, "r", newline="") as f:
    temperatures = csv.reader(f)

    for temperature in temperatures:

        date = temperature[0]
        max_temp = float(temperature[1])
        min_temp = float(temperature[2])
        ave_temp = float(temperature[3])

        database[date] = {
            "max": max_temp,
            "min": min_temp,
            "ave": ave_temp,
        }
    
with open(json_path, "w", encoding="utf-8") as f:
    json.dump(database, f, indent=4, ensure_ascii=False)