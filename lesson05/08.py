from os import path
from platform import platform

file_path = path.join(path.dirname(__file__), "myIntroduction.txt")

with open(file_path, mode="a", encoding="utf-8") as file:
    file.write(f"オペレーティングシステム: {platform()}\n")