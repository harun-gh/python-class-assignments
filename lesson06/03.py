import json
from os import path

file_path = path.join(path.dirname(__file__), "myJSONfile.json")

my_dict = {
    "name": "ChibaTech",
    "age": 84
}
print(f"first data: {my_dict}")

with open(file_path, "w", encoding="utf-8") as f:
    json.dump(my_dict, f, indent=4, ensure_ascii=False)

with open(file_path, "r", encoding="utf-8") as f:
    my_dict2 = json.load(f)
    print(f"translated dict: {my_dict2}")