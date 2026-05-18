from os import path

file_path = path.join(path.dirname(__file__), "myFile.txt")

with open(file_path, mode="w",encoding="utf-8") as file:
    file.write("Hello, World!\nこんにちは、世界!\n")