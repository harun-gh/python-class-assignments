# データ格納方式 3

from os import path
import csv

file_path = path.join(path.dirname(__file__), "chiba.csv")

database = {}

with open(file_path, "r", newline="") as file:
    data = csv.reader(file)

    for date, max_temp, min_temp, ave_temp in data:
        database[date] = {
            "max": float(max_temp),
            "min": float(min_temp),
            "ave": float(ave_temp)
        }

(hottest_date, hottest_data) = max(database.items(), key=lambda x: x[1]["max"])
(coldest_date, coldest_data) = min(database.items(), key=lambda x: x[1]["min"])

print(f"最も暑かった年月: {hottest_date} ({hottest_data["max"]}度)")
print(f"最も寒かった年月: {coldest_date} ({coldest_data["min"]}度)")