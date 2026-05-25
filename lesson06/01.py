import json

my_dict = {
    "name": "ChibaTech",
    "age": 84,
}
print(f"first data: {my_dict}")

my_json = json.dumps(my_dict)
print(f"translated json: {my_json}")

my_dict2 = json.loads(my_json)
print(f"translated dict: {my_dict2}")