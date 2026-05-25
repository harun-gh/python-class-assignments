from os import path
import json

json_path = path.join(path.dirname(__file__), "chiba.json")

with open(json_path, "r", encoding="utf-8") as f:
    data = json.load(f)

    coldest_data = sorted(data.items(), key=lambda x: x[1]["min"])

    print("date \t min")

    for data in coldest_data:
        print(f"{data[0]} \t {data[1]["min"]}")