import csv
from random import randint
from os import path

def get_random_score() -> int:
    return randint(0, 100)

file_path = path.join(path.dirname(__file__), "result.csv")

with open(file_path, "w", newline="") as file:
    csv_file = csv.writer(file)

    for n in range(1, 140):
        student_id = f"28G7{n:03}"
        math = get_random_score()
        english = get_random_score()
        physics = get_random_score()

        csv_file.writerow([student_id, math, english, physics])