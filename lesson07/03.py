data = [
    {
        "age": 18,
        "name": "Taro",
        "weight": 68
    },
    {
        "age": 19,
        "name": "Seven",
        "weight": 68
    },
    {
        "age": 20,
        "name": "Zoffy",
        "weight": 68
    },
    {
        "age": 21,
        "name": "Leo",
        "weight": 78
    },
    {
        "age": 22,
        "name": "Ace",
        "weight": 78
    },
    {
        "age": 23,
        "name": "Man",
        "weight": 78
    },
    {
        "age": 24,
        "name": "Astra",
        "weight": 58
    },
    {
        "age": 25,
        "name": "Jack",
        "weight": 58
    },
]

new_data = list(map(lambda x: {
    **x,
    "name": x["name"].lower()
}, data))

for x in new_data:
    print(x["age"], x["name"], x["weight"])