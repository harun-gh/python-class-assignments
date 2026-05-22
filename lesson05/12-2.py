# データ格納方式 2

from os import path
import csv

file_path = path.join(path.dirname(__file__), "chiba.csv")

database = []

with open(file_path, mode="r", encoding="utf-8") as file:
    csv_file = csv.reader(file)

    for date, max_temp, min_temp, ave_temp in csv_file:
        database.append({
            "date": date,
            "max": float(max_temp),
            "min": float(min_temp),
            "ave": float(ave_temp)
        })

hottest_data = max(database, key=lambda x: x["max"])
coldest_data = min(database, key=lambda x: x["min"])

print(f"最も暑かった年月: {hottest_data["date"]} ({hottest_data["max"]}度)")
print(f"最も寒かった年月: {coldest_data["date"]} ({coldest_data["min"]}度)")