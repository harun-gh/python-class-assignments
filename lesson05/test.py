import csv

with open("lesson05/chiba.csv", "r") as f:
    data = csv.reader(f)

    for content in data:
        print(content)