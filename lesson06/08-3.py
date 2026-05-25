from os import path
import json

json_path = path.join(path.dirname(__file__), "chiba.json")
json_addtional_path = path.join(path.dirname(__file__), "chiba-3.json")

restructered_data = {}

with open(json_path, "r", encoding="utf-8") as f:
    for date, data in json.load(f).items():
        restructered_data[date] = {
            "max": data["max"],
            "min": data["min"],
            "ave": data["ave"]
        }

with open(json_addtional_path, "w", encoding="utf-8") as f:
    json.dump(restructered_data, f)

with open(json_addtional_path, "r", encoding="utf-8") as f:
    data = json.load(f)

    hottest_data = sorted(data.items(), key=lambda x: x[1]["max"], reverse=True)
    coldest_data = sorted(data.items(), key=lambda x: x[1]["min"])

    print(f"最も暑かった年月: {hottest_data[0][0]} ({hottest_data[0][1]["max"]}度)")
    print(f"2番目に暑かった年月: {hottest_data[1][0]} ({hottest_data[1][1]["max"]}度)")
    print(f"最も寒かった年月: {coldest_data[0][0]} ({coldest_data[0][1]["min"]}度)")
    print(f"2番目に暑かった年月: {coldest_data[1][0]} ({coldest_data[1][1]["min"]}度)")