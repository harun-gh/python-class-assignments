from os import path

file_path = path.join(path.dirname(__file__), "myFile.txt")

with open(file_path, mode="a",encoding="utf-8") as file:
    file.write("ここから追記した\n認知情報科学科\n")